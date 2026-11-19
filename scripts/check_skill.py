#!/usr/bin/env python3
"""Check current skill structure, links/anchors, routing, stale gates and debris.

Usage: python scripts/check_skill.py [skill-folder]
This is a package check, not proof of good choreography or model behavior.
"""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

AUTH = re.compile(r'\u6700\u9ad8\u7ea2\u7ebf|\u6700\u9ad8\u7981\u4ee4|\u6700\u9ad8\u4f18\u5148|\u4f18\u5148\u4e8e\u6240\u6709|\u8986\u76d6\u6240\u6709|\u9ad8\u4e8e\u6240\u6709|\u6700\u9ad8\u88c1\u51b3|overrides? all|highest priority|supersedes? all', re.I)
GATE = re.compile(r'(?<![\d.+])3\+2(?![\d.+])|lean(?:\u4e0d\u52a0\u8f7d|\u8df3\u8fc7|\u4e0d\u8865|\u672a\u5c55\u5f00)|\u4ec5(?:\u5728)?\s*full|\u5341\u4e2a\u6c49\u5b57|10\u4e2a\u6c49\u5b57|(?:\u4ec5)?\u5728\u7528\u6237\u660e\u786e\u8981\u6c42\u6216\u63a5\u53d7\u63a8\u8350\u540e(?:\u8bfb\u53d6|\u542f\u7528)|\u672a\u6388\u6743\u5355\u53e5\u6df1\u6316|\u4e00\u53e5\u8bdd\u534f\u8bae\u63a8\u8350|\u7ea6?\s*5\s*\u79d2\s*[≤<]\s*3\s*\u6761[^。\n]*\u4ea4\u4e92', re.I)
LINK = re.compile(r'\]\(([^)\s]+?)\)')
JUNK_DIRS = {'.git', '__pycache__', '.pytest_cache', 'node_modules', '__MACOSX'}
JUNK_FILES = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}

def prose(text):
    lines=[]
    fence=None
    for line in text.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            mark=match.group(1)[0]
            if fence is None: fence=mark
            elif fence==mark: fence=None
            continue
        if fence is None: lines.append(line)
    return '\n'.join(lines)

def anchors(text):
    used={}; result=set()
    for line in prose(text).splitlines():
        match=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
        if not match: continue
        slug=re.sub(r'[^\w\-\s]','',match.group(1).lower(),flags=re.UNICODE)
        slug=re.sub(r'\s','-',slug.strip())
        n=used.get(slug,0); used[slug]=n+1
        result.add(slug if n==0 else f'{slug}-{n}')
    return result

def check(root):
    errors=[]; warns=[]; files=[]
    for p in root.rglob('*'):
        parts=p.relative_to(root).parts
        if '.git' in parts: continue
        if p.is_dir() and p.name in JUNK_DIRS: errors.append(f'{p.relative_to(root)}: runtime cache/artifact directory')
        if p.is_file():
            if p.name in JUNK_FILES or p.suffix.lower() in {'.pyc','.pyo','.tmp','.bak','.swp','.log'} or p.name.endswith('~'):
                errors.append(f'{p.relative_to(root)}: runtime cache/temporary file')
            files.append(p)
    mds={p.relative_to(root).as_posix():p.read_text(encoding='utf-8-sig') for p in files if p.suffix=='.md'}
    sk=mds.get('SKILL.md','')
    fm=re.match(r'---\n(.*?)\n---',sk,re.S)
    if not fm or not all(re.search(r'^'+key+r':\s*\S',fm.group(1),re.M) for key in ('name','description')):
        errors.append('SKILL.md: missing name/description front matter')
    if len(sk)>14000: errors.append('SKILL.md: exceeds 14000 character entrypoint budget')
    for rel,text in sorted(mds.items()):
        p=root/rel; body=prose(text)
        for raw in LINK.findall(body):
            if re.match(r'^[a-z][a-z0-9+.-]*:',raw,re.I): continue
            path,_,fragment=unquote(raw).partition('#')
            dest=(p.parent/path).resolve() if path else p.resolve()
            if not dest.exists():
                errors.append(f'{rel}: broken link -> {raw}')
            elif fragment and dest.is_file() and dest.suffix=='.md':
                if fragment.lower() not in anchors(dest.read_text(encoding='utf-8-sig')):
                    errors.append(f'{rel}: missing heading -> {raw}')
        if rel not in {'SKILL.md','core/precedence.md','README.md','evals/cases.md'} and AUTH.search(body):
            errors.append(f'{rel}: competing authority claim ({AUTH.search(body).group(0)})')
        if GATE.search(body): errors.append(f'{rel}: stale gate ({GATE.search(body).group(0)})')
        if len(text.strip())<120 and not rel.startswith(('models/','assets/')):
            warns.append(f'{rel}: extremely short document; inspect purpose')
    # Discoverability is graph reachability, not direct mention in the entrypoint.
    # Existing package-root code paths and relative Markdown links are both supported.
    graph={}
    for rel, body in mds.items():
        targets=set()
        candidates=LINK.findall(prose(body)) + re.findall(r'`([^`\n]+\.(?:md|json|py))`',body)
        for raw in candidates:
            raw=unquote(raw).split('#',1)[0]
            if not raw or re.match(r'^[a-z][a-z0-9+.-]*:',raw,re.I): continue
            for dest in ((root/rel).parent/raw,root/raw):
                dest=dest.resolve()
                if dest.is_relative_to(root) and dest.is_file():
                    targets.add(dest.relative_to(root).as_posix());break
        graph[rel]=targets
    seen=set();pending=['SKILL.md']
    while pending:
        rel=pending.pop()
        if rel in seen:continue
        seen.add(rel);pending.extend(graph.get(rel,()))
    for rel in mds:
        if rel not in seen and rel!='README.md': errors.append(f'{rel}: unreachable from entrypoint')
    try:
        import json
        from read_route import section, collect
        owners=json.loads((root/'assets/owners.json').read_text(encoding='utf-8'))
        for key,entry in owners.items(): section(root,entry)
        routes=json.loads((root/'assets/routes.json').read_text(encoding='utf-8'))
        for name in routes['routes']: collect(root,[name])
    except (OSError,ValueError,KeyError,TypeError) as error:
        errors.append(f'route/owner registry: {error}')
    for p in files:
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('scripts/','assets/templates/')) and p.suffix in {'.py','.md'}:
            if not any(rel in t or p.name in t for src,t in mds.items() if src!=rel):
                errors.append(f'{rel}: no documented entry/caller')
    print(f'{len(files)} runtime files, {len(mds)} markdown files, {sum(map(len,mds.values())):,} characters, SKILL.md {len(sk):,}')
    for w in warns: print('  warn:',w)
    if errors:
        print('FAIL')
        for e in errors: print(' -',e)
        return 1
    print('OK')
    return 0

def main():
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    if not root.is_dir():
        print('FAIL: skill folder does not exist'); return 1
    try: return check(root)
    except (OSError,UnicodeError) as error:
        print(f'FAIL: {error}'); return 1

if __name__=='__main__':
    sys.exit(main())
