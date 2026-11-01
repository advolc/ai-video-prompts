"""Export one event as a label-free plain draft, or an explicit engineering extract."""
import argparse
from pathlib import Path
import re
import sys

if sys.version_info < (3, 8):
    raise SystemExit('This tool requires Python 3.8 or newer.')


class TemplateError(ValueError):
    pass


def block(text, kind, event=None, required=True):
    suffix = f' {event}' if event else ''
    start, end = f'<!-- {kind}_START{suffix} -->', f'<!-- {kind}_END{suffix} -->'
    counts = text.count(start), text.count(end)
    if counts == (0, 0) and not required:
        return ''
    if counts != (1, 1):
        raise TemplateError(f'{kind}{suffix}: expected one start/end pair')
    first = text.index(start) + len(start)
    last = text.index(end)
    if last < first:
        raise TemplateError(f'{kind}{suffix}: reversed markers')
    value = text[first:last].strip()
    if '<!--' in value or not value:
        raise TemplateError(f'{kind}{suffix}: empty or nested block')
    return value


def numbered_lines(text, label, minimum, maximum):
    values = re.findall(rf'^【{label}(\d+)】[ \t]*(.*)$', text, flags=re.M)
    if not minimum <= len(values) <= maximum:
        raise TemplateError(f'{label}: expected {minimum}..{maximum} lines, got {len(values)}')
    if [int(n) for n, _ in values] != list(range(1, len(values) + 1)):
        raise TemplateError(f'{label}: numbering must start at 1 without gaps or duplicates')
    if any(not value.strip() for _, value in values):
        raise TemplateError(f'{label}: blank value')
    if len(re.findall(rf'^【{label}[^】]*】', text, re.M)) != len(values):
        raise TemplateError(f'{label}: use a numbered label')


def check_field_lines(text, allow_event_heading=False):
    """Reject silent loss of unlabelled or duplicate fields during plain export."""
    seen = set()
    for line in text.splitlines():
        if not line.strip():
            continue
        if allow_event_heading and re.fullmatch(r'### G\d+｜.+', line):
            continue
        item = re.fullmatch(r'【([^】]+)】[ \t]*(.*)', line)
        if not item:
            raise TemplateError('Keep each field on one labelled line; an unlabelled line would be lost')
        label, value = item.groups()
        if not value.strip():
            raise TemplateError(f'Blank field: {label}')
        if label in seen:
            raise TemplateError(f'Duplicate field: {label}')
        seen.add(label)


def as_sentence(value):
    value = value.strip()
    return value if not value or value.endswith(('。', '！', '？', '.', '!', '?')) else value + '。'


def render_plain(fixed, action, seam):
    def value(line):
        return re.sub(r'^【[^】]+】\s*', '', line.strip())

    fixed_text = ''.join(as_sentence(value(line)) for line in fixed.splitlines() if line.strip())
    fields = dict(re.findall(r'^【([^】]+)】[ \t]*(.+)$', action, re.M))
    start = fields['起点状态']
    incoming = ''.join(as_sentence(value(line)) for line in seam.splitlines() if line.strip())
    opening = as_sentence(start if start.startswith('开始时') else '开始时，' + start)
    ordered = [v for k, v in fields.items() if re.fullmatch(r'必执行\d+', k)]
    ordered += [fields[k] for k in ('单元摄影', '长镜头声明') if k in fields]
    ordered += [v for k, v in fields.items() if re.fullmatch(r'氛围\d+|禁止\d+', k)]
    ordered += [fields['原生音频']] if '原生音频' in fields else []
    ending = fields['终点状态']
    ending = as_sentence(ending if ending.startswith('结束时') else '结束时，' + ending)
    action_text = ''.join(as_sentence(v) for v in ordered)
    return '\n\n'.join(p for p in (fixed_text, incoming + opening, action_text, ending) if p) + '\n'


def extract_prompt(text, event, output_format='plain'):
    if not re.fullmatch(r'G\d{2,}', event):
        raise TemplateError('Event must be an explicit ID such as G01')
    fixed = block(text, 'FIXED')
    action = block(text, 'EVENT', event)
    seam = block(text, 'SEAM', event, required=False)
    check_field_lines(fixed)
    check_field_lines(action, allow_event_heading=True)
    if seam:
        check_field_lines(seam)
    headings = re.findall(r'^### (G\d+)｜.+$', action, re.M)
    if headings != [event]:
        raise TemplateError('Expected exactly one event heading matching selected ID')
    numbered_lines(action, '必执行', 1, 3)
    numbered_lines(action, '氛围', 0, 2)
    numbered_lines(action, '禁止', 0, 2)
    for label in ('起点状态', '终点状态'):
        rows = re.findall(rf'^【{label}】[ \t]*(.+)$', action, re.M)
        if len(rows) != 1:
            raise TemplateError(f'Expected one nonempty {label}')
    result = '\n\n'.join(part for part in (fixed, action, seam) if part).strip() + '\n'
    if re.search(r'_{4,}', result):
        raise TemplateError('Unfilled placeholder in selected generation content')
    if re.search(r'^\s*(?:#{1,6}\s*)?(?:【)?(?:控制层|管理层|QA清单|平台适配表)', result, re.M):
        raise TemplateError('Non-generation section inside export markers')
    if output_format == 'structured':
        return result
    if output_format != 'plain':
        raise TemplateError('Unknown output format')
    # Unknown action fields must not silently disappear during plain export.
    known = r'必执行\d+|氛围\d+|禁止\d+|起点状态|终点状态|单元摄影|长镜头声明|原生音频'
    for label in re.findall(r'^【([^】]+)】', action, re.M):
        if not re.fullmatch(known, label):
            raise TemplateError(f'Unsupported action field for plain export: {label}')
    return render_plain(fixed, action, seam)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--event', required=True, help='One explicit event ID, such as G01')
    parser.add_argument('--format', dest='output_format', choices=('plain', 'structured'), default='plain',
                        help='plain removes engineering labels; structured is for production review only')
    parser.add_argument('--output', type=Path, help='New output file; existing files are preserved')
    args = parser.parse_args()
    try:
        result = extract_prompt(args.input.read_text(encoding='utf-8-sig'), args.event, args.output_format)
        if args.output:
            with args.output.open('x', encoding='utf-8') as stream:
                stream.write(result)
        else:
            sys.stdout.write(result)
    except (OSError, TemplateError) as error:
        parser.exit(2, f'Export failed: {error}\n')


if __name__ == '__main__':
    main()
