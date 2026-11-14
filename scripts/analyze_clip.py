#!/usr/bin/env python3
"""Objective, crude measurements for comparing generated fight clips.

Usage: python analyze_clip.py clip.mp4 [--json out.json] [--sheet sheet.png]

Measures (all computed from pixels; none replaces watching the clip):
  - duration, resolution, fps
  - hard cuts (ffmpeg scene detection at three thresholds)
  - motion energy per second (mean absolute frame difference at 8 fps, 160x90 gray)
      * peaks: local maxima above 1.15x median, at least 1.5 s apart (rhythm variation)
      * stillness ratio: share of interior seconds below 0.5x median (resets and standoffs)
      * end hold: trailing seconds below 0.2x median (ending as pause vs. ending as result)
      * dynamic range: p90 / p10 of per-second energy (flat vs. varied intensity)
Camera motion is included in the energy, so read it with the frames, not instead of them.
"""
import subprocess, sys, json, argparse, statistics, re

def run(cmd): return subprocess.run(cmd, capture_output=True)

def probe(v):
    o = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
             "stream=width,height,r_frame_rate:format=duration", "-of", "json", v]).stdout
    j = json.loads(o); s = j["streams"][0]; n, d = s["r_frame_rate"].split("/")
    return dict(duration=float(j["format"]["duration"]), width=s["width"], height=s["height"], fps=round(int(n) / int(d), 2))

def cuts(v, th):
    e = run(["ffmpeg", "-v", "error", "-i", v, "-vf", f"select='gt(scene,{th})',showinfo", "-f", "null", "-"]).stderr.decode(errors="ignore")
    return [round(float(x), 2) for x in re.findall(r"pts_time:([0-9.]+)", e)]

def energy(v, fps=8, w=160, h=90):
    raw = run(["ffmpeg", "-v", "error", "-i", v, "-vf", f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"]).stdout
    fr = [raw[i:i + w * h] for i in range(0, len(raw) - w * h + 1, w * h)]
    d = [sum(abs(a - b) for a, b in zip(x, y)) / (w * h) for x, y in zip(fr, fr[1:])]
    per = [statistics.mean(d[i:i + fps]) for i in range(0, len(d) - fps + 1, fps)]
    return per

def pct(xs, p):
    s = sorted(xs); return s[min(len(s) - 1, int(p / 100 * len(s)))]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("clip"); ap.add_argument("--json"); ap.add_argument("--sheet")
    a = ap.parse_args()
    info = probe(a.clip); per = energy(a.clip)
    med = statistics.median(per)
    peaks = []
    for i in range(1, len(per) - 1):
        if per[i] > 1.15 * med and per[i] >= per[i - 1] and per[i] >= per[i + 1] and (not peaks or i - peaks[-1] >= 2):
            peaks.append(i)
    interior = per[2:-2] if len(per) > 6 else per
    still = sum(1 for x in interior if x < 0.5 * med) / max(1, len(interior))
    hold = 0
    for x in reversed(per):
        if x < 0.2 * med: hold += 1
        else: break
    r = dict(info, cuts={str(t): cuts(a.clip, t) for t in (0.08, 0.15, 0.25)},
             energy_per_second=[round(x, 1) for x in per], median=round(med, 1), peaks_at_s=peaks,
             peak_count=len(peaks), stillness_ratio=round(still, 2), end_hold_s=hold,
             dynamic_range_p90_over_p10=round(pct(per, 90) / max(0.1, pct(per, 10)), 1))
    print(json.dumps(r, ensure_ascii=False, indent=1))
    if a.json: open(a.json, "w", encoding="utf-8").write(json.dumps(r, ensure_ascii=False, indent=1))
    if a.sheet:
        n = max(6, int(info["duration"] / 2.5))
        run(["ffmpeg", "-v", "error", "-y", "-i", a.clip, "-vf", f"fps={n / info['duration']:.4f},scale=480:-1,tile=4x{(n + 3) // 4}", "-frames:v", "1", a.sheet])

if __name__ == "__main__":
    main()
