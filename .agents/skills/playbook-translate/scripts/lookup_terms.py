#!/usr/bin/env python3
"""Look up English AI/ML terms in terms.kr (PyTorchKR/terms-kr, MIT).

Reads the public JSON data, not the JavaScript page. Falls back to the GitHub
repository when terms.kr is unreachable. Results are cached for a day.

  python3 lookup_terms.py loss "gradient accumulation" ablation
  python3 lookup_terms.py --search parallel
"""
import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import urllib.request

SOURCES = ['https://terms.kr/data/', 'https://raw.githubusercontent.com/PyTorchKR/terms-kr/main/data/']
CACHE = Path(tempfile.gettempdir()) / 'terms-kr-cache'
MAX_AGE = 24 * 3600


def fetch(name):
    cached = CACHE / name
    if cached.exists() and time.time() - cached.stat().st_mtime < MAX_AGE:
        return json.loads(cached.read_text(encoding='utf-8'))
    last_error = None
    for base in SOURCES:
        try:
            request = urllib.request.Request(base + name, headers={'User-Agent': 'playbook-translate'})
            with urllib.request.urlopen(request, timeout=15) as response:
                text = response.read().decode('utf-8')
            data = json.loads(text)
            CACHE.mkdir(exist_ok=True)
            cached.write_text(text, encoding='utf-8')
            return data
        except (OSError, ValueError) as exc:
            last_error = exc
    if cached.exists():
        return json.loads(cached.read_text(encoding='utf-8'))
    raise OSError(f'cannot load {name}: {last_error}')


def load_terms():
    terms = []
    for name in fetch('index.json'):
        data = fetch(name)
        terms.extend(data if isinstance(data, list) else data.get('terms', []))
    return terms


def normalize(text):
    return ' '.join(text.lower().replace('-', ' ').replace('_', ' ').split())


def variants(query):
    base = normalize(query)
    forms = {base}
    if base.endswith('ies'):
        forms.add(base[:-3] + 'y')
    elif base.endswith('es'):
        forms.update({base[:-2], base[:-1]})
    elif base.endswith('s'):
        forms.add(base[:-1])
    return forms


def show(entry):
    print(entry['term'])
    for meaning in entry.get('meanings', []):
        line = f"  -> {meaning.get('korean', '?')}"
        if meaning.get('synonyms'):
            line += f"  (synonyms: {', '.join(meaning['synonyms'])})"
        print(line)
        if meaning.get('definition'):
            print(f"     {meaning['definition']}")
    if entry.get('notes'):
        print(f"  notes: {entry['notes']}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('terms', nargs='*', help='English terms to look up exactly')
    parser.add_argument('--search', help='Substring search over English terms, Korean and synonyms')
    args = parser.parse_args(argv)
    if not args.terms and not args.search:
        parser.error('give terms or --search')
    try:
        terms = load_terms()
    except OSError as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    index = {normalize(entry['term']): entry for entry in terms}
    missing = []
    for query in args.terms:
        found = next((index[form] for form in variants(query) if form in index), None)
        if found:
            show(found)
        else:
            missing.append(query)
    if args.search:
        needle = normalize(args.search)
        for entry in terms:
            haystack = [entry['term']] + [m.get('korean', '') for m in entry.get('meanings', [])]
            haystack += [s for m in entry.get('meanings', []) for s in m.get('synonyms', [])]
            if any(needle in normalize(item) for item in haystack):
                show(entry)
    if missing:
        print('NOT IN terms.kr: ' + ', '.join(missing))
    print(f'({len(terms)} terms loaded. terms.kr data are AI-drafted; the team glossary takes precedence.)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
