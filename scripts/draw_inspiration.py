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


DIMENSIONS = {'一': 'world', '二': 'space', '三': 'relation', '四': 'action', '五': 'blind',
              '六': 'mood', '七': 'visual', '八': 'archetype'}
CATEGORY_ALIASES = {'古风': '传统东方/修仙', '修仙': '传统东方/修仙',
                    '科幻': '赛博/未来科幻', '赛博': '赛博/未来科幻',
                    '都市': '现代都市/异能', '废土': '异星废土/末日',
                    '压迫': '压迫/紧绷', '温暖': '温暖/轻盈', '荒凉': '悲壮/诡异/荒凉',
                    '单色': '单色/无彩', '水墨': '写意/绘制', '霓虹': '光学/数字',
                    '孤狼': '游离/反抗', '守护者': '守护/担当', '背叛者': '伪装/矛盾'}


def load_cards(path):
    cards = []
    dimension = category = None
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        heading = re.match(r'^## ([一二三四五六七八])、', line)
        if heading:
            dimension = DIMENSIONS[heading.group(1)]
            category = '反常规/混搭盲盒' if dimension == 'blind' else None
        subheading = re.match(r'^### \d+\. (.+)$', line)
        if subheading:
            category = subheading.group(1)
        if line.startswith('- '):
            item = re.fullmatch(r'- \*\*【([^】]+)】\*\*：(.+。)', line)
            if not item or not dimension or not category:
                raise ValueError(f'Malformed inspiration card: {line}')
            tag, description = item.groups()
            cards.append({'id': f'{dimension}::{category}::{tag}', 'dimension': dimension,
                          'category': category, 'tag': tag, 'description': description})
    if not cards or len({c['id'] for c in cards}) != len(cards):
        raise ValueError('Empty library or duplicate card IDs')
    return cards


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
    seen = set(history.get('seen', []))
    last = set(by_dimension.get(dimension, history.get('last_batch', [])))
    category = CATEGORY_ALIASES.get(category, category)
    pool = [c for c in cards if c['dimension'] == dimension
            and (not category or category in c['category']) and c['tag'] not in excluded_tags]
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
    parser.add_argument('--category', help='Exact/partial subcategory or alias, e.g. 古风 or 科幻')
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
