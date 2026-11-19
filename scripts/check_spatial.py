#!/usr/bin/env python3
"""Validate two-fighter design data, not generated video or artistic quality.
Usage: python scripts/check_spatial.py ledger.json
Each beat: t, A/B poses with x/y/z/facing and optional anchor.
Optional requirements: min_lateral_bl, min_bearing_sweep_deg,
min_height_change_bl, min_anchor_changes. Only use for explicit project goals.
Exit: 0 valid data/targets met; 1 target missed; 2 invalid data.
"""
import json, math, sys
TARGETS = {'min_lateral_bl':'lateral_bl','min_bearing_sweep_deg':'bearing_sweep_deg','min_height_change_bl':'max_individual_height_range_bl','min_anchor_changes':'anchor_changes'}
def number(v, label):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
        raise ValueError(label+' must be finite numeric data')
    return v

def analyze(ledger):
    if not isinstance(ledger,dict): raise ValueError('ledger must be an object')
    beats=ledger.get('beats')
    if not isinstance(beats,list) or len(beats)<2: raise ValueError('at least two timed beats required')
    arena=ledger.get('arena',{})
    if not isinstance(arena,dict): raise ValueError('arena must be an object')
    marks=arena.get('landmarks',[])
    if not isinstance(marks,list): raise ValueError('landmarks must be a list')
    ids=[]
    for mark in marks:
        if not isinstance(mark,dict) or not isinstance(mark.get('id'),str) or not mark['id']: raise ValueError('landmark needs nonempty id')
        ids.append(mark['id'])
    if len(ids)!=len(set(ids)): raise ValueError('duplicate landmarks')
    previous=None
    for i,beat in enumerate(beats):
        if not isinstance(beat,dict): raise ValueError('beat must be an object')
        t=number(beat.get('t'),'time')
        if t<0 or (previous is not None and t<=previous): raise ValueError('times must be nonnegative and strictly increasing')
        previous=t
        for actor in ('A','B'):
            pose=beat.get(actor)
            if not isinstance(pose,dict): raise ValueError('missing actor pose')
            for key in ('x','y','z','facing'): number(pose.get(key),actor+'.'+key)
            anchor=pose.get('anchor')
            if anchor is not None and (not isinstance(anchor,str) or anchor not in ids): raise ValueError('unknown anchor')
    runtime=number(ledger.get('runtime_s',beats[-1]['t']),'runtime_s')
    if runtime<=0 or runtime<beats[-1]['t']: raise ValueError('runtime must include all beat times')
    req=ledger.get('requirements',{})
    if not isinstance(req,dict): raise ValueError('requirements must be an object')
    for key,value in req.items():
        if key not in TARGETS: raise ValueError('unknown requirement: '+key)
        if number(value,key)<0: raise ValueError('negative requirement')
        if key=='min_anchor_changes' and int(value)!=value: raise ValueError('anchor count must be integer')
    heights={}; changes={}
    for actor in ('A','B'):
        zs=[b[actor]['z'] for b in beats]
        heights[actor]=max(zs)-min(zs)
        changes[actor]=sum(beats[i][actor].get('anchor')!=beats[i-1][actor].get('anchor') for i in range(1,len(beats)))
    a,b=beats[0]['A'],beats[0]['B']; dx,dy=b['x']-a['x'],b['y']-a['y']; norm=math.hypot(dx,dy)
    lateral=max(abs((q[k]['x']-a['x'])*dy-(q[k]['y']-a['y'])*dx)/norm for q in beats for k in ('A','B')) if norm else None
    angles=[]
    for q in beats:
        x,y=q['B']['x']-q['A']['x'],q['B']['y']-q['A']['y']
        angles.append(math.degrees(math.atan2(y,x)) if math.hypot(x,y) else None)
    sweep=None if None in angles else sum(abs((v-u+180)%360-180) for u,v in zip(angles,angles[1:]))
    metrics=dict(lateral_bl=lateral,bearing_sweep_deg=sweep,max_individual_height_range_bl=max(heights.values()),anchor_changes=sum(changes.values()),height_range_by_actor=heights,anchor_changes_by_actor=changes)
    failures=[k for k,v in req.items() if metrics[TARGETS[k]] is None or metrics[TARGETS[k]]<v]
    return dict(metrics=metrics,requirements=req,unmet_requirements=failures,status='TARGET_MISSED' if failures else 'VALID_DESIGN_DATA',scope='Design observations only; no contact, facing, plausible speed, artistic quality or video verification. Height means foot elevation, not ducking posture.')

def main():
    if len(sys.argv)!=2: print(__doc__); return 2
    try:
        with open(sys.argv[1],encoding='utf-8-sig') as f: result=analyze(json.load(f))
    except (OSError,ValueError,TypeError) as error:
        print('INVALID_DATA:',error); return 2
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if result['unmet_requirements'] else 0
if __name__=='__main__': sys.exit(main())
