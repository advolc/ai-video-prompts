#!/usr/bin/env python3
"""Read exact source sections for one or more task routes, without summarizing.
Usage: python scripts/read_route.py action dialogue [--stats]
       python scripts/read_route.py --list
Only paths inside the skill root may be read. Unknown routes/headings fail closed.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def section(root, entry):
    path = (root / entry['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('source escapes skill root')
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    heading = entry['heading']
    indices = [i for i, line in enumerate(lines) if line == heading]
    if len(indices) != 1: raise ValueError(f'heading missing or ambiguous: {entry}')
    start = indices[0]
    level = len(heading)-len(heading.lstrip('#'))
    if not level: raise ValueError('section must be a Markdown heading')
    end = len(lines)
    for i in range(start+1, len(lines)):
        if lines[i].startswith('#'):
            n=len(lines[i])-len(lines[i].lstrip('#'))
            if n <= level and lines[i][n:n+1]==' ':
                end=i;break
    return '\n'.join(lines[start:end]).rstrip()+'\n'

def collect(root, routes):
    manifest=json.loads((root/'assets/routes.json').read_text(encoding='utf-8'))
    entries=[]
    for route in routes:
        if route not in manifest['routes']: raise ValueError('unknown route: '+route)
    if any(manifest['routes'][k]['uses_common_prompt'] for k in routes):
        entries.extend(manifest['common_prompt'])
    for k in routes: entries.extend(manifest['routes'][k]['sections'])
    seen=set();result=[]
    for e in entries:
        key=(e['path'],e['heading'])
        if key in seen:continue
        seen.add(key);result.append((e,section(root,e)))
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('routes',nargs='*')
    ap.add_argument('--list',action='store_true')
    ap.add_argument('--stats',action='store_true')
    a=ap.parse_args()
    try:
        if a.list:
            print('\n'.join(json.loads((ROOT/'assets/routes.json').read_text(encoding='utf-8'))['routes']));return 0
        if not a.routes: ap.error('choose a route or --list')
        items=collect(ROOT,a.routes)
        if a.stats:
            print(json.dumps(dict(routes=a.routes,sections=len(items),files=len({e['path'] for e,t in items}),characters=sum(len(t) for e,t in items)),indent=2))
        else:
            for e,t in items:print(f"\nSOURCE: {e['path']} :: {e['heading']}\n{t}")
    except (OSError,ValueError,KeyError,TypeError) as error:
        print('INVALID_ROUTE:',error);return 2
    return 0

if __name__=='__main__':raise SystemExit(main())
