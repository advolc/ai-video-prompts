#!/usr/bin/env python3
"""Measure an actual video; no claim about acting, blocking or sound quality.

Usage: python scripts/analyze_clip.py clip.mp4 [--json metrics.json] [--sheet sheet.png]
Requires FFmpeg and FFprobe on PATH. Cuts are heuristic candidates; pixel motion
includes camera movement and cannot establish that actors changed positions.
See analyze_clip.md alongside this script for examples, metric definitions and errors.
"""
import argparse
import json
import math
from pathlib import Path
import re
import statistics
import subprocess

def run(cmd):
    result=subprocess.run(cmd,capture_output=True,timeout=120)
    if result.returncode:
        detail=result.stderr.decode(errors='replace')[-2000:]
        raise ValueError(f'{cmd[0]} exited {result.returncode}: {detail.strip()}')
    return result

def probe(video):
    result=run(['ffprobe','-v','error','-select_streams','v:0','-show_entries',
                'stream=width,height,r_frame_rate:format=duration','-of','json',str(video)])
    data=json.loads(result.stdout)
    if not data.get('streams'): raise ValueError('Input has no video stream')
    stream=data['streams'][0]
    n,d=stream['r_frame_rate'].split('/')
    fps=int(n)/int(d) if int(d) else 0.0
    duration=float(data.get('format',{}).get('duration',0))
    if not math.isfinite(duration) or duration<=0: raise ValueError('Input has no positive finite duration')
    return dict(duration=duration,width=stream['width'],height=stream['height'],fps=round(fps,3))

def cuts(video,threshold):
    # showinfo emits INFO messages; '-v error' would silently hide every timestamp.
    result=run(['ffmpeg','-hide_banner','-nostdin','-v','info','-i',str(video),
                '-an','-vf',f"select='gt(scene,{threshold})',showinfo",'-f','null','-'])
    times=re.findall(r'pts_time:([0-9.+eE-]+)',result.stderr.decode(errors='replace'))
    return sorted({round(float(value),3) for value in times})

def energy(video,fps=8,width=160,height=90):
    raw=run(['ffmpeg','-nostdin','-v','error','-i',str(video),'-an','-vf',
             f'fps={fps},scale={width}:{height},format=gray','-f','rawvideo','-']).stdout
    size=width*height
    frames=[raw[i:i+size] for i in range(0,len(raw)-size+1,size)]
    differences=[sum(abs(a-b) for a,b in zip(x,y))/size for x,y in zip(frames,frames[1:])]
    return [statistics.mean(differences[i:i+fps]) for i in range(0,len(differences),fps)]

def percentile(values,p):
    if not values: return 0.0
    ordered=sorted(values)
    return ordered[min(len(ordered)-1,int(p/100*len(ordered))) ]

def analyze(video):
    info=probe(video)
    per=energy(video)
    median=statistics.median(per) if per else 0.0
    peaks=[]
    for i in range(1,len(per)-1):
        if per[i]>max(1e-6,1.15*median) and per[i]>=per[i-1] and per[i]>=per[i+1] and (not peaks or i-peaks[-1]>=2):
            peaks.append(i)
    interior=per[2:-2] if len(per)>6 else per
    still=sum(x<=max(1e-6,0.5*median) for x in interior)/max(1,len(interior))
    hold=0
    for value in reversed(per):
        if value<=max(1e-6,0.2*median): hold+=1
        else: break
    return dict(info,cuts={str(t):cuts(video,t) for t in (0.08,0.15,0.25)},
                energy_per_second=[round(x,3) for x in per],median=round(median,3),
                peaks_at_s=peaks,peak_count=len(peaks),stillness_ratio=round(still,3),
                end_hold_s=min(info['duration'],hold),
                dynamic_range_p90_over_p10=round(percentile(per,90)/max(0.1,percentile(per,10)),3),
                measurement_scope='Cut candidates and pixel motion only; camera motion is included. Actor paths, acting, audio and lip sync require direct review.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('clip',type=Path)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--sheet',type=Path)
    args=parser.parse_args()
    video=args.clip.resolve()
    outputs=[p.resolve() for p in (args.json,args.sheet) if p is not None]
    if not video.is_file(): parser.error('Input video does not exist')
    if video in outputs or len(outputs)!=len(set(outputs)):
        parser.error('Outputs must be distinct from each other and from the input video')
    try:
        result=analyze(video)
        payload=json.dumps(result,ensure_ascii=False,indent=2)
        if args.sheet:
            n=min(120,max(6,math.ceil(result['duration']/2.5)))
            args.sheet.parent.mkdir(parents=True,exist_ok=True)
            run(['ffmpeg','-nostdin','-v','error','-y','-i',str(video),'-an','-vf',
                 f"fps={n/result['duration']:.8f},scale=480:-1,tile=4x{math.ceil(n/4)}",
                 '-frames:v','1',str(args.sheet)])
            if not args.sheet.is_file() or not args.sheet.stat().st_size:
                raise ValueError('Contact sheet was not produced')
        if args.json:
            args.json.parent.mkdir(parents=True,exist_ok=True)
            args.json.write_text(payload,encoding='utf-8')
        print(payload)
    except (OSError,ValueError,KeyError,ZeroDivisionError,subprocess.TimeoutExpired) as error:
        parser.exit(2,f'Analysis failed: {error}\n')

if __name__=='__main__': main()
