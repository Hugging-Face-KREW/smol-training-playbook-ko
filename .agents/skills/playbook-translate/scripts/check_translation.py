#!/usr/bin/env python3
"""Check this study's line correspondence and protected MDX elements.

FAIL items break the team rules and return exit code 1.
WARN items need a human decision and never change the exit code.
Input files are never modified.
"""
import argparse
from collections import Counter
from pathlib import Path
import re
import sys

# Values a reader sees. Everything else in JSX, config and frontmatter must stay as in the source.
TRANSLATABLE_ATTRS = {'title', 'caption', 'alt', 'label', 'aria-label', 'placeholder'}
TRANSLATABLE_CONFIG_KEYS = {'title', 'label', 'xAxisLabel', 'yAxisLabel'}
TRANSLATABLE_FRONTMATTER_KEYS = {'title', 'subtitle', 'description'}

URL = re.compile(r'https?://[^\s)"\'<>\]`]+')
LINK_TARGET = re.compile(r'\]\(([^)\s]+)')
INLINE_CODE = re.compile(r'`[^`\n]+`')
INLINE_MATH = re.compile(r'(?<!\\)\$\$.*?(?<!\\)\$\$|(?<![\\$])\$(?!\$).*?(?<![\\$])\$(?!\$)|\\\(.*?\\\)|\\\[.*?\\\]')
CITATION = re.compile(r'\[(@[^\]]+)\]')
CITATION_KEY = re.compile(r'@([\w:./-]+)')
FOOTNOTE = re.compile(r'\[\^[^\]]+\]')
TAG = re.compile(r'</?([A-Za-z][\w.]*)')
ATTR_NAME = re.compile(r'(?<![\w-])([A-Za-z_][\w-]*)=(?=["\'{])')
ATTR_STRING = re.compile(r'(?<![\w-])([A-Za-z_][\w-]*)=("[^"]*"|\'[^\']*\')')
CONFIG_KEY = re.compile(r'(?:^|[{,])\s*([A-Za-z_]\w*)\s*:')
NUMBER = re.compile(r'\d+(?:[.,]\d+)*')
ENGLISH_WORD = re.compile(r'\b[A-Za-z][a-z]+\b')
PRONOUN = re.compile(r'(그것|이것|저것|그들|그녀)(은|는|이|가|을|를|의|도|에게|에|과|와|만|으로|로)?')
COLON_PROSE = re.compile(r':\s+\S|:[가-힣]')  # 3:1, 10:30, URLs and code are not matched
# A heading label before the colon is fine in Korean: "**핵심 아이디어**: ...", "**참고:** ...", "참고: ...".
LABEL_PREFIX = re.compile(r'^\s*(?:>\s*)?(?:[-*+]|\d+\.)?\s*'
                          r'(?:(?:\*\*|__)[^*_:\n]{1,30}(?::(?:\*\*|__)|(?:\*\*|__):)|[^\s:*_]{1,8}:)')
HANGUL = re.compile(r'[가-힣]')
HEADING_MARK = re.compile(r'^(#{1,6})\s')


def read_lines(path):
    # Preserve CRLF and final-newline differences for exact scope checks.
    return Path(path).read_bytes().decode('utf-8').splitlines(keepends=True)


def line_end(line):
    return '\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else '\r' if line.endswith('\r') else ''


def parse_range(value):
    try:
        start, end = map(int, value.split(':'))
    except ValueError:
        raise argparse.ArgumentTypeError('Use inclusive START:END, e.g. 1402:2054')
    if start < 1 or end < start:
        raise argparse.ArgumentTypeError('Require 1 <= START <= END')
    return start, end


def classify(lines):
    """Label each line: frontmatter, code, math, import, jsx (multi-line tag or config block) or prose."""
    kinds = ['prose'] * len(lines)
    fence = None
    math_end = None
    in_tag = False
    brace_depth = 0
    start = 0
    if lines and lines[0].strip() == '---':
        kinds[0] = 'frontmatter'
        for index in range(1, len(lines)):
            kinds[index] = 'frontmatter'
            if lines[index].strip() == '---':
                start = index + 1
                break
    for index in range(start, len(lines)):
        stripped = lines[index].strip()
        if fence:
            kinds[index] = 'code'
            if re.fullmatch(re.escape(fence[0]) + '{' + str(fence[1]) + r',}\s*', stripped):
                fence = None
            continue
        if math_end:
            kinds[index] = 'math'
            if stripped == math_end:
                math_end = None
            continue
        match = re.match(r'^(`{3,}|~{3,})', stripped)
        if match:
            marker = match.group(1)
            fence = (marker[0], len(marker))
            kinds[index] = 'code'
            continue
        if stripped in ('$$', r'\['):
            kinds[index] = 'math'
            math_end = '$$' if stripped == '$$' else r'\]'
            continue
        if stripped.startswith('import ') or stripped.startswith('export '):
            kinds[index] = 'import'
            continue
        if brace_depth > 0 or in_tag:
            kinds[index] = 'jsx'
        if re.match(r'^<[A-Za-z][\w.]*\s*$', stripped) or (re.match(r'^<[A-Za-z][\w.]*\s', stripped) and '>' not in stripped):
            in_tag = True
            kinds[index] = 'jsx'
        if '={{' in stripped or brace_depth > 0:
            brace_depth = max(0, brace_depth + stripped.count('{') - stripped.count('}'))
            kinds[index] = 'jsx'
        if in_tag and brace_depth == 0 and ('/>' in stripped or stripped.endswith('>')):
            in_tag = False
    return kinds


def mask_translatable(line):
    line = re.sub(r'(?<![\w-])(' + '|'.join(map(re.escape, TRANSLATABLE_ATTRS)) +
                  r')=("[^"]*"|\'[^\']*\'|\{`[^`]*`\}|\{"[^"]*"\})', r'\1=<T>', line)
    line = re.sub(r'(?<![\w-])(' + '|'.join(TRANSLATABLE_CONFIG_KEYS) +
                  r')(\s*:\s*)("[^"]*"|\'[^\']*\'|`[^`]*`)', r'\1\2<T>', line)
    return line


def strip_markup(line):
    """Prose text without code, math, URLs, link targets, citations and tags."""
    text = INLINE_CODE.sub(' ', line)
    text = INLINE_MATH.sub(' ', text)
    text = LINK_TARGET.sub('](', text)
    text = URL.sub(' ', text)
    text = CITATION.sub(' ', text)
    text = FOOTNOTE.sub(' ', text)
    text = re.sub(r'<[^>]*>', ' ', text)
    return text


def tokens(line):
    citations = [key for group in CITATION.findall(line) for key in CITATION_KEY.findall(group)]
    fixed_attrs = [f'{name}={value}' for name, value in ATTR_STRING.findall(line) if name not in TRANSLATABLE_ATTRS]
    return {
        'URL': Counter(URL.findall(line)),
        'link target': Counter(LINK_TARGET.findall(line)),
        'inline code': Counter(INLINE_CODE.findall(line)),
        'inline math': Counter(INLINE_MATH.findall(line)),
        'citation key': Counter(citations),
        'footnote': Counter(FOOTNOTE.findall(line)),
        'tag name': Counter(TAG.findall(line)),
        'attribute name': Counter(ATTR_NAME.findall(line)),
        'fixed attribute value': Counter(fixed_attrs),
    }


def describe(counter_a, counter_b):
    missing = list((counter_a - counter_b).elements())[:3]
    added = list((counter_b - counter_a).elements())[:3]
    parts = []
    if missing:
        parts.append('missing ' + ', '.join(map(str, missing)))
    if added:
        parts.append('added ' + ', '.join(map(str, added)))
    return '; '.join(parts)


def frontmatter_check(source, target, current_key):
    """Return (problem or None, current top-level key)."""
    key_match = re.match(r'^(\s*-?\s*)([A-Za-z_][\w-]*):', source)
    if key_match:
        indent, key = key_match.groups()
        if not indent:
            current_key = key
        if not target.startswith(indent + key + ':'):
            return f'frontmatter key "{key}" changed', current_key
        if key not in TRANSLATABLE_FRONTMATTER_KEYS and source != target:
            return f'frontmatter value of "{key}" changed (only title/subtitle/description are translated)', current_key
        return None, current_key
    if (source.strip() in ('---', '') or current_key not in TRANSLATABLE_FRONTMATTER_KEYS) and source != target:
        return 'frontmatter line outside title/subtitle/description changed', current_key
    return None, current_key


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--source', required=True, help='Fixed English original')
    parser.add_argument('--translation', required=True, help='Translated MDX after work')
    parser.add_argument('--before', help='Exact translation snapshot taken before work')
    parser.add_argument('--range', action='append', required=True, type=parse_range,
                        dest='ranges', help='Inclusive source lines START:END; repeat as needed')
    parser.add_argument('--max-items', type=int, default=15, help='Items shown per category (default 15)')
    args = parser.parse_args(argv)
    try:
        source = read_lines(args.source)
        translated = read_lines(args.translation)
        before = read_lines(args.before) if args.before else None
    except (OSError, UnicodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2

    errors = []
    warnings = []

    def fail(category, message):
        errors.append((category, message))

    def warn(category, message):
        warnings.append((category, message))

    if len(source) != len(translated):
        fail('line count', f'source={len(source)}, translation={len(translated)}')
    if before is not None and len(before) != len(translated):
        fail('line count', f'changed during edit: before={len(before)}, after={len(translated)}')
    for start, end in args.ranges:
        if end > len(source) or end > len(translated):
            print(f'FAIL [range] {start}:{end} exceeds source or translation line count')
            print('FAILED. No files were modified.')
            return 1

    selected = sorted({i for start, end in args.ranges for i in range(start - 1, end)})
    selected_set = set(selected)
    kinds = classify(source)
    frontmatter_key = None
    for i in range(len(source)):
        if i not in selected_set:
            if kinds[i] == 'frontmatter':
                match = re.match(r'^([A-Za-z_][\w-]*):', source[i])
                if match:
                    frontmatter_key = match.group(1)
            continue
        original, target = source[i], translated[i]
        where = f'L{i+1}'
        if (not original.strip()) != (not target.strip()):
            fail('blank line', f'{where}: blank-line position differs from source')
        if line_end(original) != line_end(target):
            fail('line ending', f'{where}: line ending differs from source')
        kind = kinds[i]
        if kind in ('code', 'math', 'import'):
            if original != target:
                fail('protected line', f'{where}: {kind} line differs from source')
            continue
        if kind == 'frontmatter':
            problem, frontmatter_key = frontmatter_check(original.rstrip('\r\n'), target.rstrip('\r\n'), frontmatter_key)
            if problem:
                fail('frontmatter', f'{where}: {problem}')
            continue
        if kind == 'jsx':
            if mask_translatable(original) != mask_translatable(target):
                fail('jsx/config', f'{where}: only title/caption/alt/label values may change on this line')
            source_keys = Counter(CONFIG_KEY.findall(original))
            target_keys = Counter(CONFIG_KEY.findall(target))
            if source_keys != target_keys:
                fail('config key', f'{where}: {describe(source_keys, target_keys)}')
        source_tokens, target_tokens = tokens(original), tokens(target)
        for category, counter in source_tokens.items():
            if counter != target_tokens[category]:
                fail(category, f'{where}: {describe(counter, target_tokens[category])}')
        if kind != 'prose':
            continue
        # The site takes heading ids from the English line with the same number
        # (app/plugins/remark/source-heading-ids.mjs), so the heading marker must stay.
        source_mark, target_mark = HEADING_MARK.match(original), HEADING_MARK.match(target)
        if (source_mark and source_mark.group(1)) != (target_mark and target_mark.group(1)):
            fail('heading level', f'{where}: heading marker must stay as in the source')
        prose_source, prose_target = strip_markup(original), strip_markup(target)
        if original == target:
            if len(ENGLISH_WORD.findall(prose_source)) >= 3:
                warn('untranslated', f'{where}: identical to the English source')
            continue
        numbers_source = Counter(NUMBER.findall(prose_source))
        numbers_target = Counter(NUMBER.findall(prose_target))
        if numbers_source != numbers_target:
            warn('number', f'{where}: {describe(numbers_source, numbers_target)}')
        pronouns = [m.group(0) for m in PRONOUN.finditer(prose_target)]
        if pronouns:
            warn('pronoun', f'{where}: {", ".join(pronouns[:3])} -> name what it refers to, or drop it')
        text = prose_target.rstrip('\r\n')
        label = LABEL_PREFIX.match(text)
        body = text[label.end():] if label else text
        if HANGUL.search(body) and COLON_PROSE.search(body):
            warn('colon', f'{where}: colon joins Korean clauses; use a connective or split the sentence on this line')

    if before is not None:
        for i in range(min(len(before), len(translated))):
            if i not in selected_set and before[i] != translated[i]:
                fail('outside range', f'L{i+1}: changed outside assigned ranges')
            if line_end(before[i]) != line_end(translated[i]):
                fail('line ending', f'L{i+1}: line ending changed during edit')

    def report(label, items):
        grouped = {}
        for category, message in items:
            grouped.setdefault(category, []).append(message)
        for category, messages in grouped.items():
            print(f'{label} [{category}] {len(messages)} item(s)')
            for message in messages[:args.max_items]:
                print(f'  {message}')
            if len(messages) > args.max_items:
                print(f'  ... {len(messages) - args.max_items} more')

    report('FAIL', errors)
    report('WARN', warnings)
    if errors:
        print(f'FAILED: {len(errors)} issue(s), {len(warnings)} warning(s). No files were modified.')
        return 1
    print('PASS: line correspondence, blank lines, line endings, heading levels, code/math/import lines, frontmatter, '
          'JSX/config keys and fixed values, URLs, link targets, inline code/math, citation keys, footnotes.')
    print('PASS: outside-range content unchanged.' if before is not None else
          'SKIP: outside-range mutation check; provide --before to enable it.')
    if warnings:
        print(f'{len(warnings)} warning(s) above need a human decision; they do not fail the check.')
    print('Manual review still required: meaning, per-line order, MDX/HTML validity, figures and real link navigation.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
