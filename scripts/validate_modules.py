"""Validate module metadata, local links and reachability (Python 3.8+).

Module frontmatter uses scalar strings and inline string arrays. This deliberately
small YAML subset needs no third-party package. SKILL.md uses the host schema.
"""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

LAYERS = ('core', 'ux', 'visual', 'narrative', 'production', 'sound', 'post',
          'distribution', 'management', 'quality')
FIELDS = ('id', 'layer', 'priority', 'depends_on', 'conflicts_with', 'load_when', 'not_for')
LIST_FIELDS = ('depends_on', 'conflicts_with', 'load_when', 'not_for')


def inside(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def scalar(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        value = json.loads(raw)
        if not isinstance(value, str):
            raise ValueError('Expected a string')
        return value
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    if not raw or raw[0] in '[{':
        raise ValueError('Expected a nonempty scalar')
    return raw


def string_list(raw):
    try:
        value = json.loads(raw)
    except ValueError:
        if not (raw.startswith('[') and raw.endswith(']')):
            raise ValueError('Use an inline array, e.g. ["module-id"]')
        value = [scalar(x) for x in re.split(r',\s*(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', raw[1:-1]) if x.strip()]
    if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
        raise ValueError('Expected a string array')
    if len(set(value)) != len(value):
        raise ValueError('Duplicate array items')
    return value


def parse_frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing frontmatter at start of file')
    values = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        item = re.fullmatch(r'([a-z_]+):\s*(.*)', line)
        if not item:
            raise ValueError('Use flat frontmatter with inline arrays: ' + line)
        key, raw = item.groups()
        if key in values:
            raise ValueError('Duplicate frontmatter field: ' + key)
        values[key] = string_list(raw) if key in LIST_FIELDS else scalar(raw)
    missing = set(FIELDS) - set(values)
    if missing:
        raise ValueError('Missing fields: ' + ', '.join(sorted(missing)))
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', values['id']):
        raise ValueError('Module id must be lowercase ASCII kebab-case')
    if values['layer'] not in LAYERS:
        raise ValueError('Unknown layer: ' + values['layer'])
    if values['priority'] not in ('P0', 'P1', 'P2', 'P3'):
        raise ValueError('Unknown priority')
    if not values['load_when']:
        raise ValueError('load_when must describe at least one trigger')
    return values


def link_targets(path, text, root, errors):
    targets = []
    # Ignore fenced examples so example syntax is not mistaken for a live link.
    text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)
    for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', text):
        href = match.group(1).strip()
        if href.startswith('<') and '>' in href:
            href = href[1:href.index('>')]
        else:
            href = re.split(r'\s+[\"\']', href, maxsplit=1)[0]
        if not href or href.startswith('#'):
            continue
        if re.match(r'^[A-Za-z]:[\\/]', href):
            errors.append(str(path.relative_to(root)) + ': private absolute file link: ' + href)
            continue
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if not inside(target, root):
            errors.append(str(path.relative_to(root)) + ': link escapes package: ' + href)
        elif not target.exists():
            errors.append(str(path.relative_to(root)) + ': broken link: ' + href)
        else:
            targets.append(target)
    return targets


def validate(root):
    root = root.resolve()
    errors, modules, by_path, text_by_path = [], {}, {}, {}
    paths = list((root / 'references').rglob('*.md'))
    for layer in LAYERS:
        paths.extend((root / layer).rglob('*.md'))
    for path in sorted(paths):
        text = path.read_text(encoding='utf-8-sig')
        try:
            meta = parse_frontmatter(text)
            if meta['id'] in modules:
                raise ValueError('Duplicate module id: ' + meta['id'])
            if path.relative_to(root).parts[0] != 'references' and path.relative_to(root).parts[0] != meta['layer']:
                raise ValueError('Metadata layer differs from directory')
            modules[meta['id']] = meta
            by_path[path.resolve()] = meta['id']
        except ValueError as error:
            errors.append(str(path.relative_to(root)) + ': ' + str(error))
    for mid, meta in modules.items():
        for target in meta['depends_on'] + meta['conflicts_with']:
            if target not in modules:
                errors.append(mid + ': unknown module reference: ' + target)
        if set(meta['depends_on']) & set(meta['conflicts_with']):
            errors.append(mid + ': same module is both dependency and conflict')
    visiting, visited = set(), set()

    def visit(mid):
        if mid in visiting:
            errors.append('Dependency cycle at ' + mid)
            return
        if mid in visited or mid not in modules:
            return
        visiting.add(mid)
        for dep in modules[mid]['depends_on']:
            visit(dep)
        visiting.remove(mid)
        visited.add(mid)
    for mid in modules:
        visit(mid)
    links = {}
    for path in root.rglob('*.md'):
        text = path.read_text(encoding='utf-8-sig')
        text_by_path[path.resolve()] = text
        links[path.resolve()] = link_targets(path, text, root, errors)
    reached, pending = set(), [(root / 'SKILL.md').resolve()]
    while pending:
        current = pending.pop()
        if current in reached:
            continue
        reached.add(current)
        pending.extend(links.get(current, []))
        mid = by_path.get(current)
        if mid:
            pending.extend(p for p, target in by_path.items() if target in modules[mid]['depends_on'])
    for path, mid in by_path.items():
        if path not in reached:
            errors.append(mid + ': unreachable from SKILL.md')
    return {'ok': not errors, 'modules': len(modules),
            'markdown_files': len(text_by_path), 'reachable_modules': sum(p in reached for p in by_path),
            'errors': errors,
            'scope': 'Static package structure only; not model behavior, video or external URL verification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        report = validate(args.root)
    except (OSError, ValueError) as error:
        parser.exit(2, 'Validation failed: ' + str(error) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
