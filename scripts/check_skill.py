#!/usr/bin/env python3
"""Lint the skill package. Usage: python scripts/check_skill.py [path]

Fails (exit 1) on:
  - SKILL.md missing name/description front matter, or over the size budget
  - broken relative links
  - competing authority claims outside SKILL.md and core/precedence.md
  - leftover v1 gates: the old 3+2 budget law, "lean不加载"/"仅full" opt-in gating, the ten-character dialogue cap
  - a file in references/, lens/, dialogue/ not routed from SKILL.md
Warns on tiny stub files.
"""
import os, re, sys
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
SKILL_MAX = 14000
EXEMPT_AUTH = {"SKILL.md", "core/precedence.md", "MIGRATION.md", "README.md", "evals/cases.md", "examples/legacy-v1"}
AUTH = re.compile(r"(最高红线|最高禁令|最高优先|优先于所有|覆盖所有|高于所有|最高裁决|overrides? all|highest priority|supersedes? all)")
GATE = re.compile(r"(?<![\d.+])3\+2(?![\d.+])|lean不加载|lean跳过|lean不补|仅full|十个汉字|10个汉字")
LINK = re.compile(r"\]\(([^)\s]+?)\)")
problems, warns = [], []

def rd(p): return open(p, encoding="utf-8").read()
mds = []
for r, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith(".md"): mds.append(os.path.relpath(os.path.join(r, f), ROOT).replace("\\", "/"))
mds.sort()
sk = rd(os.path.join(ROOT, "SKILL.md"))
m = re.match(r"---\n(.*?)\n---", sk, re.S)
if not m or "name:" not in m.group(1) or "description:" not in m.group(1): problems.append("SKILL.md: missing name/description front matter")
if len(sk) > SKILL_MAX: problems.append(f"SKILL.md: {len(sk)} chars exceeds {SKILL_MAX}")

for rel in mds:
    t = rd(os.path.join(ROOT, rel))
    legacy = rel.startswith("examples/legacy-v1") or rel.startswith("PATCHES-")
    for lk in ([] if rel.startswith("PATCHES-") else LINK.findall(t)):
        if re.match(r"^(https?:|mailto:|#)", lk): continue
        path = lk.partition("#")[0]
        if path and not os.path.exists(os.path.normpath(os.path.join(ROOT, os.path.dirname(rel), path))):
            problems.append(f"{rel}: broken link -> {lk}")
    if not legacy and not any(rel == e or rel.startswith(e) for e in EXEMPT_AUTH) and AUTH.search(t):
        problems.append(f"{rel}: claims authority over other files ({AUTH.search(t).group(0)})")
    if not legacy and rel not in ("MIGRATION.md", "README.md", "core/pipeline.md", "evals/cases.md", "lens/lens-layer.md") and GATE.search(t):
        problems.append(f"{rel}: leftover v1 gate ({GATE.search(t).group(0)})")
    if len(t) < 1000 and not legacy and not rel.startswith(("models/", "assets/")): warns.append(f"{rel}: only {len(t)} chars (stub?)")

for d in ("references", "lens", "dialogue"):
    for f in sorted(os.listdir(os.path.join(ROOT, d))):
        if f.endswith(".md") and f"{d}/{f}" not in sk:
            problems.append(f"{d}/{f}: not routed from SKILL.md")
total = sum(len(rd(os.path.join(ROOT, r))) for r in mds)
print(f"{len(mds)} markdown files, {total:,} characters, SKILL.md {len(sk):,}")
for w in warns: print("  warn:", w)
if problems:
    print("FAIL")
    for p in problems: print(" -", p)
    sys.exit(1)
print("OK")
