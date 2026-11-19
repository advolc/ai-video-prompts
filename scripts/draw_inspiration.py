"""Draw 5-6 diverse inspiration cards, with optional session history."""
import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import random
import re
import sys
import tempfile

if sys.version_info < (3, 8):
    raise SystemExit('This tool requires Python 3.8 or newer.')


def is_within(path, root):
    """Python 3.8-compatible containment check on already-resolved paths."""
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def save_history(path, state):
    """Replace only a complete JSON file, preserving old history on write failure."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=str(path.parent),
                                         prefix='.' + path.name + '-', suffix='.tmp', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(state, stream, ensure_ascii=False, indent=2)
        os.replace(str(temporary), str(path))
        temporary = None
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


DIMENSIONS = {'\u4e00': 'world', '\u4e8c': 'space', '\u4e09': 'relation', '\u56db': 'action', '\u4e94': 'blind',
              '\u516d': 'mood', '\u4e03': 'visual', '\u516b': 'archetype'}
CATEGORY_ALIASES = {'\u53e4\u98ce': '\u4f20\u7edf\u4e1c\u65b9/\u4fee\u4ed9', '\u4fee\u4ed9': '\u4f20\u7edf\u4e1c\u65b9/\u4fee\u4ed9',
                    '\u79d1\u5e7b': '\u8d5b\u535a/\u672a\u6765\u79d1\u5e7b', '\u8d5b\u535a': '\u8d5b\u535a/\u672a\u6765\u79d1\u5e7b',
                    '\u90fd\u5e02': '\u73b0\u4ee3\u90fd\u5e02/\u5f02\u80fd', '\u5e9f\u571f': '\u5f02\u661f\u5e9f\u571f/\u672b\u65e5',
                    '\u538b\u8feb': '\u538b\u8feb/\u7d27\u7ef7', '\u6e29\u6696': '\u6e29\u6696/\u8f7b\u76c8', '\u8352\u51c9': '\u60b2\u58ee/\u8be1\u5f02/\u8352\u51c9',
                    '\u5355\u8272': '\u5355\u8272/\u65e0\u5f69', '\u6c34\u58a8': '\u5199\u610f/\u7ed8\u5236', '\u9713\u8679': '\u5149\u5b66/\u6570\u5b57',
                    '\u5b64\u72fc': '\u6e38\u79bb/\u53cd\u6297', '\u5b88\u62a4\u8005': '\u5b88\u62a4/\u62c5\u5f53', '\u80cc\u53db\u8005': '\u4f2a\u88c5/\u77db\u76fe'}


ENGLISH_DIMENSIONS = {'world': 'world', 'space': 'space', 'relationship': 'relation',
                      'action': 'action', 'blind mix': 'blind', 'mood': 'mood',
                      'visual': 'visual', 'archetype': 'archetype'}

def compatibility_records():
    path = Path(__file__).resolve().parents[1] / 'assets' / 'inspiration-compatibility.json'
    if not path.is_file():
        return []
    return json.loads(path.read_text(encoding='utf-8'))['records']

def load_cards(path):
    records = compatibility_records()
    id_map = {r['key']: r['id'] for r in records}
    id_map.update({r['legacy_id']: r['id'] for r in records})
    cards = []
    dimension = category = None
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        old_heading = re.match(r'^## ([\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b])\u3001', line)
        new_heading = re.fullmatch(r'## (World|Space|Relationship|Action|Blind Mix|Mood|Visual|Archetype)', line, re.I)
        if old_heading:
            dimension = DIMENSIONS[old_heading.group(1)]
            category = '\u53cd\u5e38\u89c4/\u6df7\u642d\u76f2\u76d2' if dimension == 'blind' else None
        elif new_heading:
            dimension = ENGLISH_DIMENSIONS[new_heading.group(1).casefold()]
            category = 'Unconventional / Blind Mix' if dimension == 'blind' else None
        subheading = re.match(r'^### \d+\. (.+)$', line)
        if subheading:
            category = subheading.group(1)
        if line.startswith('- '):
            item = re.fullmatch(r'- \*\*\[([^\]]+)\]\*\*: (.+[.!?])', line)
            if item is None:
                item = re.fullmatch(r'- \*\*\u3010([^\u3011]+)\u3011\*\*\uff1a(.+\u3002)', line)
            if not item or not dimension or not category:
                raise ValueError(f'Malformed inspiration card: {line}')
            tag, description = item.groups()
            key = f'{dimension}::{category}::{tag}'
            cards.append({'id': id_map.get(key, key), 'dimension': dimension,
                          'category': category, 'tag': tag, 'description': description})
    if not cards or len({c['id'] for c in cards}) != len(cards):
        raise ValueError('Empty library or duplicate card IDs')
    return cards

def normalize_legacy(history, category, excluded_tags):
    records = compatibility_records()
    aliases = {r['legacy_id']: r['id'] for r in records}
    categories = {}; tags = defaultdict(set)
    for record in records:
        old = record['legacy_id'].split('::', 2)
        new = record['key'].split('::', 2)
        categories[old[1]] = new[1]
        tags[old[2]].add(new[2])
    normalized = dict(history)
    for field in ('seen', 'last_batch'):
        normalized[field] = [aliases.get(value, value) for value in history.get(field, [])]
    normalized['last_by_dimension'] = {
        key: [aliases.get(value, value) for value in values]
        for key, values in history.get('last_by_dimension', {}).items()
    }
    category = CATEGORY_ALIASES.get(category, category)
    category = categories.get(category, category)
    excluded = set(excluded_tags)
    for tag in excluded_tags:
        excluded.update(tags.get(tag, ()))
    return normalized, category, excluded


def balanced_sample(pool, count, rng):
    groups = defaultdict(list)
    for card in pool:
        groups[card['category']].append(card)
    result = []
    while groups and len(result) < count:
        categories = list(groups)
        rng.shuffle(categories)
        for category in categories:
            group = groups[category]
            result.append(group.pop(rng.randrange(len(group))))
            if not group:
                del groups[category]
            if len(result) == count:
                break
    return result


def draw(cards, dimension, category=None, count=6, history=None, excluded_tags=(), rng=None):
    if count not in (5, 6):
        raise ValueError('Each batch must contain 5 or 6 cards')
    rng = rng or random.SystemRandom()
    if history is not None and not isinstance(history, dict):
        raise ValueError('History must be a JSON object')
    history = history or {}
    for field in ('seen', 'last_batch'):
        if not isinstance(history.get(field, []), list) or any(not isinstance(x, str) for x in history.get(field, [])):
            raise ValueError(f'History {field} must be a string list')
    if type(history.get('draws', 0)) is not int or history.get('draws', 0) < 0:
        raise ValueError('History draws must be a nonnegative integer')
    by_dimension = history.get('last_by_dimension', {})
    if not isinstance(by_dimension, dict) or any(not isinstance(v, list) or any(not isinstance(x, str) for x in v) for v in by_dimension.values()):
        raise ValueError('History last_by_dimension must contain string lists')
    history, category, excluded_tags = normalize_legacy(history, category, excluded_tags)
    by_dimension = history.get('last_by_dimension', {})
    seen = set(history.get('seen', []))
    last = set(by_dimension.get(dimension, history.get('last_batch', [])))
    category = CATEGORY_ALIASES.get(category, category)
    pool = [c for c in cards if c['dimension'] == dimension
            and (not category or category.casefold() in c['category'].casefold()) and c['tag'] not in excluded_tags]
    if len(pool) < count:
        raise ValueError(f'Only {len(pool)} eligible cards; cannot draw {count} distinct cards')
    fresh = [c for c in pool if c['id'] not in seen]
    older = [c for c in pool if c['id'] in seen and c['id'] not in last]
    recent = [c for c in pool if c['id'] in last]
    result = []
    for tier in (fresh, older, recent):
        result.extend(balanced_sample(tier, count - len(result), rng))
        if len(result) == count:
            break
    rng.shuffle(result)
    selected = [c['id'] for c in result]
    updated = {'seen': sorted(seen | set(selected)), 'last_batch': selected,
               'last_by_dimension': {**by_dimension, dimension: selected},
               'draws': history.get('draws', 0) + 1}
    return {'cards': result, 'fresh_count': sum(c['id'] not in seen for c in result),
            'reused_count': sum(c['id'] in seen for c in result),
            'recent_repeat_count': sum(c['id'] in last for c in result),
            'eligible_pool_size': len(pool),
            'pool_seen_after_draw': all(c['id'] in updated['seen'] for c in pool)}, updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dimension', required=True, choices=list(DIMENSIONS.values()))
    parser.add_argument('--category', help='Exact or partial English category; legacy localized aliases remain accepted')
    parser.add_argument('--count', type=int, default=6, choices=(5, 6))
    parser.add_argument('--exclude-tags', nargs='*', default=[], help='Cards incompatible with current settings')
    parser.add_argument('--history', type=Path, help='Optional JSON session history in project work directory')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        history = {}
        if args.history:
            history_path = args.history.resolve()
            if is_within(history_path, root):
                raise ValueError('Keep draw history in project work, outside the installed skill')
            if history_path.is_file():
                history = json.loads(history_path.read_text(encoding='utf-8'))
            if not history_path.parent.is_dir():
                raise ValueError('History parent directory must already exist')
        cards = load_cards(root / 'references' / 'inspiration-library.md')
        result, updated = draw(cards, args.dimension, args.category, args.count, history, args.exclude_tags)
        if args.history:
            save_history(history_path, updated)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(2, f'Draw failed: {error}\n')


if __name__ == '__main__':
    main()
