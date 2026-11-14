#!/usr/bin/env python3
"""Spatial QA gate: does a fight ledger actually use three-dimensional space?

Usage: python scripts/check_spatial.py ledger.json

Ledger JSON:
{ "mode": "duel", "runtime_s": 15,
  "arena": {"has_height": true, "landmarks": [{"id": "R1", "x": 7, "y": 3, "z": 0, "type": "slope"}]},
  "beats": [ {"t": 0, "A": {"x":0,"y":0,"z":0,"facing":0,"anchor":null},
                       "B": {"x":2.5,"y":0,"z":0,"facing":180,"anchor":null},
              "event": "...", "answer": "slip" } ] }
Units are body-lengths (BL); z is the feet elevation above the base floor; facing is degrees (0 = +X).
"answer" is the displacement used to answer the previous beat:
  advance|retreat|slip|arc|pivot|pass|level_down|level_up|pushoff|funnel|obstacle|plant

This checks the DESIGN (the ledger), not a generated video. Thresholds are starting heuristics (see
references/spatial-tactics.md) and are mode-aware. Exit code 1 if any check FAILS.
"""
import json, math, sys

# per-mode: which checks apply. "waive" = not required; "relax" = lower threshold
PROFILE = {
    "duel":       dict(sweep=60, lateral=1.0, linearity=0.05, anchors=True,  level=True,  run=2),
    "last_stand": dict(sweep=60, lateral=1.0, linearity=0.05, anchors=True,  level=True,  run=2),
    "brawl":      dict(sweep=60, lateral=1.0, linearity=0.05, anchors=False, level=False, run=2),
    "sparring":   dict(sweep=30, lateral=0.5, linearity=0.03, anchors=False, level=False, run=3),
    "ambush":     dict(sweep=45, lateral=1.0, linearity=0.05, anchors=False, level=False, run=2),
    "dominance":  dict(sweep=45, lateral=1.0, linearity=0.05, anchors=False, level=False, run=2),
    "stealth":    dict(sweep=None, lateral=1.0, linearity=None, anchors=True, level=False, run=3),
    "flight":     dict(sweep=None, lateral=1.0, linearity=None, anchors=True, level=True,  run=3),
    "group":      dict(sweep=45, lateral=1.0, linearity=0.05, anchors=False, level=False, run=2),
    "ritual":     dict(sweep=None, lateral=None, linearity=None, anchors=False, level=False, run=99),
}

def ang(ax, ay, bx, by): return math.degrees(math.atan2(by - ay, bx - ax))
def wrap(d): return (d + 180) % 360 - 180

def pca_ratio(pts):  # kept for reference; no longer used by the gate
    n = len(pts)
    if n < 3: return 0.0
    mx = sum(p[0] for p in pts) / n; my = sum(p[1] for p in pts) / n
    sxx = sum((p[0]-mx)**2 for p in pts) / n; syy = sum((p[1]-my)**2 for p in pts) / n
    sxy = sum((p[0]-mx)*(p[1]-my) for p in pts) / n
    tr = sxx + syy; det = sxx*syy - sxy*sxy
    disc = max(0.0, tr*tr/4 - det)
    l1 = tr/2 + math.sqrt(disc); l2 = tr/2 - math.sqrt(disc)
    return 0.0 if l1 < 1e-9 else max(0.0, l2) / l1

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    L = json.load(open(sys.argv[1], encoding="utf-8"))
    mode = L.get("mode", "duel"); P = PROFILE.get(mode, PROFILE["duel"])
    beats = L["beats"]; runtime = float(L.get("runtime_s") or (beats[-1]["t"] - beats[0]["t"]) or 10)
    arena = L.get("arena", {}); has_height = bool(arena.get("has_height"))
    n_land = len(arena.get("landmarks", []))
    A = [(b["A"]["x"], b["A"]["y"], b["A"]["z"]) for b in beats]
    B = [(b["B"]["x"], b["B"]["y"], b["B"]["z"]) for b in beats]
    theta = [ang(a[0], a[1], b[0], b[1]) for a, b in zip(A, B)]
    deltas = [wrap(theta[i] - theta[i-1]) for i in range(1, len(beats))]

    # line-lock run: consecutive beats with no break (bearing >= 30 deg, or Z >= 0.5, or an anchor change)
    run = best = 0
    for i in range(1, len(beats)):
        a0, a1, b0, b1 = beats[i-1]["A"], beats[i]["A"], beats[i-1]["B"], beats[i]["B"]
        brk = abs(deltas[i-1]) >= 30 or max(abs(a1["z"]-a0["z"]), abs(b1["z"]-b0["z"])) >= 0.5 \
              or a1.get("anchor") != a0.get("anchor") or b1.get("anchor") != b0.get("anchor")
        run = 0 if brk else run + 1
        best = max(best, run)

    # lateral deviation from the initial duel line
    dx, dy = B[0][0]-A[0][0], B[0][1]-A[0][1]; norm = math.hypot(dx, dy) or 1.0
    def perp(p): return abs((p[0]-A[0][0])*dy - (p[1]-A[0][1])*dx) / norm
    lateral = max(max(perp(p) for p in A), max(perp(p) for p in B))

    sweep = sum(abs(d) for d in deltas) / max(runtime/10, 0.1)       # degrees per 10 s
    zs = [p[2] for p in A + B]; zrange = max(zs) - min(zs)
    declared_levels = any(b.get("answer") in ("level_up", "level_down", "pushoff") for b in beats)
    anchors = {b[s].get("anchor") for b in beats for s in ("A", "B")} - {None}
    answers = [b.get("answer") for b in beats[1:] if b.get("answer")]
    plant = (answers.count("plant") / len(answers)) if answers else 0.0
    # bearing coverage: circular variance of the duel-line bearing. ~0 when the duel stays on one line, large when it sweeps around.
    cs = sum(math.cos(math.radians(x)) for x in theta) / len(theta); sn = sum(math.sin(math.radians(x)) for x in theta) / len(theta)
    lin = 1 - math.hypot(cs, sn)

    rows = []; fail = False
    def chk(name, ok, val, need, waived=False):
        nonlocal fail
        tag = "WAIVED" if waived else ("PASS" if ok else "FAIL")
        if tag == "FAIL": fail = True
        rows.append(f"  {tag:6s} {name:24s} {val:<26s} need {need}")
    chk("line-lock run", best <= P["run"], f"{best} beats", f"<= {P['run']}", P["run"] == 99)
    chk("lateral deviation", lateral >= (P["lateral"] or 0), f"{lateral:.2f} BL", f">= {P['lateral']} BL", P["lateral"] is None)
    chk("bearing sweep", sweep >= (P["sweep"] or 0), f"{sweep:.0f} deg/10s", f">= {P['sweep']}", P["sweep"] is None)
    lv_ok = (zrange >= 0.5) if has_height else declared_levels
    chk("level change", lv_ok, f"z range {zrange:.2f}, declared={declared_levels}", ">= 0.5 BL (or a declared level event on flat ground)", not P["level"])
    chk("anchors", len(anchors) >= 2 or n_land < 2, f"{len(anchors)} distinct", ">= 2 in a terrain-rich arena", not P["anchors"])
    chk("plant-and-absorb share", plant <= 1/3, f"{plant:.0%}", "<= 33%")
    chk("bearing coverage", lin >= (P["linearity"] or 0), f"circ. variance {lin:.2f}", f">= {P['linearity']} (duel line covers several directions)", P["linearity"] is None)
    print(f"mode: {mode}   beats: {len(beats)}   runtime: {runtime:g}s")
    print("\n".join(rows))
    print("RESULT:", "FAIL (linear or under-used space; re-stage the displacements)" if fail else "PASS")
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    main()
