#!/usr/bin/env python3
"""Lint a final video prompt for the Lens-layer grammar (replaces v1's export_prompt.py).

Usage:
  python scripts/lint_prompt.py prompt.txt [--tier extended|standard|compact] [--lang en|zh|auto] [--seconds N]
  cat prompt.txt | python scripts/lint_prompt.py -

Also warns when movement verbs are mostly linear (steps in/back, retreats) and few are spatial.
Finds PATTERNS only. It cannot judge meaning: a clean lint does not mean a good prompt,
and a flag is a question, not a verdict. Exit code 1 if any ERROR is found.
"""
import re, sys, argparse

def rules():
    E, W = "ERROR", "warn"
    return [
        # production scaffolding / design leakage
        (E, "scaffolding", r"\bG\d{1,3}\b|\bGEN[_ ]?\d+\b|\bCLIP[_ ]?\d+\b|\bSHOT[_ ]?\d+\b"),
        (E, "scaffolding", r"\b\d{1,3}\s*[-\u2013\u2014]\s*\d{1,3}\s*(s|sec|seconds)\b|\d{1,3}\s*[-\u2013\u2014~\uff5e]\s*\d{1,3}\s*\u79d2"),
        (E, "scaffolding", r"(?i)\b(must[- ]do|ambient (detail|slot)|seam|same as (before|previous|above)|see (above|prefix)|as before)\b|\u5fc5\u6267\u884c|\u6c1b\u56f4\u989d|\u63a5\u7f1d|\u540c\u4e0a|\u540c\u524d\u6bb5|\u89c1\u524d\u7f00"),
        (E, "label/heading", r"(?m)^\s*(#{1,6}\s|[-*\u2022]\s|\u3010|\[[A-Za-z\u4e00-\u9fff ]{1,20}\]\s*$)"),
        (E, "label/heading", r"(?m)^\s*(Camera|Lighting|Subject|Setting|Audio|Dialogue|Action|Style|Look|Slot \d|\u955c\u5934|\u5149\u7ebf|\u4e3b\u4f53|\u573a\u666f|\u5bf9\u767d|\u52a8\u4f5c|\u98ce\u683c)\s*[:\uff1a]"),
        (E, "design-jargon", r"(?i)\b(subtext|power dynamics?|status ledger|micro-?expressions?|motif|vulnerab\w+|dominan\w+|tension|beat \d+|tier [abc]|texture pass|lens layer)\b|\u6f5c\u53f0\u8bcd|\u5f20\u529b|\u6743\u529b\u5173\u7cfb|\u5fae\u8868\u60c5|\u6bcd\u9898|\u5fc3\u7406\u52a8\u4f5c|\u5730\u4f4d\u5173\u7cfb|\u6a21\u5757"),
        # constraints / negations / explanation
        (W, "conditional", r"(?i)\b(only (after|when|if)|must|should|has to|needs to|in order to|so that)\b|\u5fc5\u987b|\u5e94\u8be5|\u53ea\u6709.{0,12}\u624d|\u4ec5\u5f53|\u4e3a\u4e86"),
        (W, "negation", r"(?i)\b(no|not|never|without|don'?t|doesn'?t|isn'?t|cannot|can'?t|avoid|none)\b|\u4e0d\u8981|\u4e0d\u5f97|\u7981\u6b62|\u6ca1\u6709|\u4e0d\u80fd|\u907f\u514d|\u5207\u52ff|\u65e0\u9700"),
        (W, "explanation", r"(?i)\b(to show|to convey|to suggest|because|as a sign of|symboli[sz]\w*|represent\w*|indicat\w*)\b|\u8868\u73b0\u51fa|\u663e\u793a\u51fa|\u8c61\u5f81\u7740|\u56e0\u4e3a|\u4ee3\u8868\u7740"),
        (W, "control-param", r"(?i)\b(\d{3,4}p|\d{1,3}\s?(?:s|sec|secs|seconds)|\d{2,3}\s?fps)\b|\d{1,3}\s?\u79d2\u949f?(?=[,\uff0c.\u3002\s]|$)|\d{3,4}[pP]\b"),
        # empty evaluatives
        (W, "evaluative", r"(?i)\b(stunning|epic|masterpiece|flawless|perfect(ly)?|gorgeous|breathtaking|ultra[- ]?(detailed|realistic)|8k|4k|cinematic masterpiece|award[- ]winning)\b|\u9707\u64bc|\u5b8c\u7f8e|\u7edd\u7f8e|\u53f2\u8bd7\u7ea7|\u6770\u4f5c|\u6781\u81f4|\u7535\u5f71\u611f\u62c9\u6ee1"),
        # emotion labels that need a physical proxy beside them
        (W, "emotion-label", r"(?i)\b(angry|furious|nervous|anxious|scared|afraid|sad|devastated|happy|tense|menacing|vulnerable)\b|\u6124\u6012|\u7d27\u5f20|\u5bb3\u6015|\u60b2\u4f24|\u5fc3\u8651|\u538b\u6291|\u9634\u9a98"),
        (W, "cliche", r"(?i)\b(devilish (smile|grin)|pupils? (quak|shak|dilat)\w*|veins? bulg\w*|sharp intake of breath|piercing gaze|steely gaze)\b|\u5632\u89d2\u52fe\u8d77\u4e00\u62b9|\u7728\u5b54\u5267\u70c8|\u9752\u7b4b\u66b4\u8d77"),
    ]

LIMITS = {  # (en_words_min, en_words_max, zh_chars_min, zh_chars_max)
    "extended": (320, 520, 650, 1000),
    "standard": (150, 250, 300, 500),
    "compact": (60, 110, 120, 220),
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--tier", default="extended", choices=list(LIMITS))
    ap.add_argument("--lang", default="auto", choices=["auto", "en", "zh"])
    ap.add_argument("--seconds", type=float, default=0, help="clip runtime; above 10 s the Extended target scales to ~25-35 words/s (~50-70 chars/s)")
    a = ap.parse_args()
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    zh = len(re.findall(r"[\u4e00-\u9fff]", text))
    en_words = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", text))
    lang = a.lang if a.lang != "auto" else ("zh" if zh > en_words else "en")

    findings = []
    lines = text.split("\n")
    for sev, cat, pat in rules():
        rx = re.compile(pat)
        for i, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                findings.append((i, sev, cat, m.group(0).strip()[:40]))
    # dialogue stage directions in parentheses
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"\((?:pause|beat|silence|\u505c\u987f|\u6c89\u9ed8)[^)]*\)|\uff08(?:\u505c\u987f|\u6c89\u9ed8)[^\uff09]*\uff09", line, re.I):
            findings.append((i, "ERROR", "stage-direction", m.group(0)))
    # linear-movement check: movement that lives only on the duel line (see references/spatial-tactics.md)
    LIN = re.compile(r"(?i)\b(?:steps?|stepped|stepping)\s+(?:in|back|forward)\b|\bretreat\w*|\badvanc\w*|\bhalf (?:a )?step\b|\bgives? ground\b|\bpulls? (?:back|in)\b|\bback(?:s|ing)? (?:away|off)\b|\u8fdb\u534a\u6b65|\u9000\u534a\u6b65|\u540e\u9000|\u524d\u8fdb|\u4e0a\u524d\u4e00\u6b65|\u9000\u4e00\u6b65|\u64a4\u6b65|\u540e\u64a4")
    SPA = re.compile(r"(?i)\b(?:circl\w+|arcs?|arcing|around|orbit\w*|slides? off|slip\w*|sidestep\w*|pivot\w*|cuts? past|passes? (?:past|by)|behind (?:him|her|them|the)|leaps?|springs?|vault\w*|climb\w*|drops? (?:under|to|low)|ducks?|rolls?|pushes? off|off the line|outside (?:the|his|her))\b|\u7ed5|\u73af\u7ed5|\u4fa7\u95ea|\u4fa7\u79fb|\u79bb\u7ebf|\u7a7f\u8eab|\u8eab\u540e|\u8dc3|\u817e|\u6500|\u7ffb\u6eda|\u6eda|\u6c89\u8eab|\u501f\u529b|\u8e6c")
    nlin, nspa = len(LIN.findall(text)), len(SPA.findall(text))
    if nlin >= 4 and nspa * 2 < nlin:
        findings.append((0, "warn", "linear-movement", f"{nlin} linear moves vs {nspa} spatial (circle, slip, pass, level, push-off)"))
    findings.sort()

    lo, hi = (LIMITS[a.tier][0], LIMITS[a.tier][1]) if lang == "en" else (LIMITS[a.tier][2], LIMITS[a.tier][3])
    if a.tier == "extended" and a.seconds > 10:
        lo, hi = (int(25 * a.seconds), int(35 * a.seconds)) if lang == "en" else (int(50 * a.seconds), int(70 * a.seconds))
    n = en_words if lang == "en" else zh
    unit = "words" if lang == "en" else "characters"
    errs = sum(1 for f in findings if f[1] == "ERROR")
    warns = len(findings) - errs
    for ln, sev, cat, frag in findings:
        print(f"line {ln:3d}  {sev:5s}  {cat:15s}  {frag}")
    print(f"\nlength: {n} {unit} (target for {a.tier}, {lang}: {lo}-{hi})", end="")
    print("  OK" if lo <= n <= hi else ("  SHORT" if n < lo else "  LONG (check the model's limit)"))
    print(f"{errs} error(s), {warns} warning(s). Flags are questions: a negation inside a quoted line of dialogue is fine.")
    sys.exit(1 if errs else 0)

if __name__ == "__main__":
    main()
