#!/usr/bin/env python3
"""Lint the skill folder. Usage: python scripts/check_skill.py [path]

Checks (exit code 1 if any fail):
  - SKILL.md exists, has name/description front matter, stays under size budget
  - every reference file stays under its size budget
  - every relative markdown link resolves
  - only SKILL.md may claim precedence over other files (no competing authorities)
  - every file in references/ is routed from SKILL.md
"""
import re, sys, pathlib

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SKILL_MAX = 7000        # characters
REF_MAX = 30000         # characters per reference file
AUTHORITY = re.compile(
    r"(overrides? (all|every)|supersedes? (all|every)|highest (priority|red line|prohibition)|"
    r"takes? precedence over (all|every|any))", re.I)
LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)#\s]+)")

problems = []

def read(p):
    return p.read_text(encoding="utf-8")

skill = ROOT / "SKILL.md"
if not skill.exists():
    sys.exit("SKILL.md not found")
s = read(skill)
m = re.match(r"---\n(.*?)\n---", s, re.S)
if not m or "name:" not in m.group(1) or "description:" not in m.group(1):
    problems.append("SKILL.md: missing name/description front matter")
if len(s) > SKILL_MAX:
    problems.append(f"SKILL.md: {len(s)} chars exceeds budget {SKILL_MAX}")

md_files = sorted(p for p in ROOT.rglob("*.md"))
for p in md_files:
    t = read(p)
    rel = p.relative_to(ROOT)
    if p.parent.name == "references" and len(t) > REF_MAX:
        problems.append(f"{rel}: {len(t)} chars exceeds budget {REF_MAX}")
    for link in LINK.findall(t):
        target = (p.parent / link).resolve()
        if not target.exists():
            problems.append(f"{rel}: broken link -> {link}")
    if p != skill and p.name != "MIGRATION.md" and AUTHORITY.search(t):
        problems.append(f"{rel}: claims precedence over other files; only SKILL.md may")

for ref in sorted((ROOT / "references").glob("*.md")):
    if f"references/{ref.name}" not in s:
        problems.append(f"references/{ref.name}: not routed from SKILL.md")

total = sum(len(read(p)) for p in md_files)
print(f"{len(md_files)} markdown files, {total:,} characters total, SKILL.md {len(s):,}")
if problems:
    print("\nFAIL")
    for x in problems:
        print(" -", x)
    sys.exit(1)
print("OK")
