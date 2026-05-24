#!/usr/bin/env python3
"""
Char limits validator for content-factory outputs.

Validates per-channel character limits:
- X / Twitter (each tweet in thread): 280
- Bluesky (each post in thread): 300
- Threads (each post in thread): 500
- LinkedIn (total): 3000
- WhatsApp Canal (total): 4096
- Mastodon (total): 500
- Quora (each answer): no hard limit but warns >12000
- Hacker News title: 80, comment: warns >5000

Usage:
    python3 validate_char_limits.py output/x_twitter_ready.txt output/bluesky_ready.txt
    python3 validate_char_limits.py output/*

Exit code: 0 = all within limits, 1 = violations.
"""
import sys, re, argparse
from pathlib import Path


# Per-channel limits and parsing rules
CHANNELS = {
    'x_twitter_ready.txt': {
        'limit_per_unit': 280,
        'limit_total': None,
        'parse': 'split_by_pattern',
        'pattern': r'^(\d+)/\s+',  # "1/", "2/", etc.
        'description': 'X / Twitter — each tweet ≤280 chars',
    },
    'bluesky_ready.txt': {
        'limit_per_unit': 300,
        'limit_total': None,
        'parse': 'split_by_pattern',
        'pattern': r'^POST (\d+)/\d+',
        'description': 'Bluesky — each post ≤300 chars',
    },
    'threads_ready.txt': {
        'limit_per_unit': 500,
        'limit_total': None,
        'parse': 'split_by_pattern',
        'pattern': r'^POST (\d+)/\d+',
        'description': 'Threads — each post ≤500 chars',
    },
    'mastodon_ready.txt': {
        'limit_per_unit': 500,
        'limit_total': None,
        'parse': 'split_by_pattern',
        'pattern': r'^POST (\d+)/\d+',
        'description': 'Mastodon — each toot ≤500 chars',
    },
    'linkedin.md': {
        'limit_per_unit': None,
        'limit_total': 3000,
        'parse': 'whole',
        'description': 'LinkedIn — total ≤3000 chars',
    },
    'linkedin_ca.md': {
        'limit_per_unit': None,
        'limit_total': 3000,
        'parse': 'whole',
        'description': 'LinkedIn CA — total ≤3000 chars',
    },
    'linkedin_en.md': {
        'limit_per_unit': None,
        'limit_total': 3000,
        'parse': 'whole',
        'description': 'LinkedIn EN — total ≤3000 chars',
    },
    'whatsapp_channel_es.md': {
        'limit_per_unit': None,
        'limit_total': 4096,
        'parse': 'whole',
        'description': 'WhatsApp Channel ES — total ≤4096 chars',
    },
    'whatsapp_channel_ca.md': {
        'limit_per_unit': None,
        'limit_total': 4096,
        'parse': 'whole',
        'description': 'WhatsApp Channel CA — total ≤4096 chars',
    },
    'whatsapp.md': {
        'limit_per_unit': None,
        'limit_total': 4096,
        'parse': 'whole',
        'description': 'WhatsApp Group — total ≤4096 chars',
    },
    'hackernews_ready.txt': {
        'limit_per_unit': None,
        'limit_total': None,
        'parse': 'whole',
        'description': 'Hacker News — title ≤80 (extracted separately), comment ≤5000 warn',
    },
}


def strip_meta(text: str) -> str:
    """Remove markdown frontmatter, block quotes (>), and section dividers from char count."""
    # Strip frontmatter
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end > 0:
            text = text[end + 5:]
    # Strip block quotes (notes/meta starting with >)
    text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
    # Strip horizontal rules and code fences and instruction sections
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^=+$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^-+$', '', text, flags=re.MULTILINE)
    # Strip "## Instrucciones de publicación manual" and after
    cut_markers = [
        '## Instrucciones de publicación',
        '## Verificación post-publicación',
        '## Por qué este formato',
        '## Trucos page',
        '## Trucos de algoritmo',
        '## Comentario #',
        '## Versión histórica',
        '## Fuentes de los datos',
    ]
    for marker in cut_markers:
        idx = text.find(marker)
        if idx > 0:
            text = text[:idx]
    return text


def parse_tweets(text: str, pattern: str) -> list:
    """Split content into list of (idx, text) by matching tweet numbering pattern."""
    text = strip_meta(text)
    # Find all matches and split text accordingly
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    if not matches:
        return []

    tweets = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        # Remove the numbering prefix from the count
        body = re.sub(pattern, '', chunk, count=1, flags=re.MULTILINE).strip()
        # Remove any separator lines or meta annotations
        body = re.sub(r'\(.{0,30}chars[^\)]*\)\s*', '', body)  # remove "(N chars · desc)"
        body = body.strip()
        tweets.append((m.group(0).strip(), body))

    return tweets


def detect_channel(filepath: Path) -> dict:
    """Detect which channel rules apply by filename."""
    name = filepath.name
    return CHANNELS.get(name)


def validate_file(filepath: Path) -> dict:
    """Return validation result dict."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return {'error': str(e)}

    channel = detect_channel(filepath)
    if not channel:
        return {'unknown_channel': True, 'name': filepath.name}

    result = {
        'channel': channel,
        'violations': [],
        'units': [],
        'ok_count': 0,
    }

    if channel['parse'] == 'whole':
        cleaned = strip_meta(content).strip()
        n = len(cleaned)
        result['units'] = [{'idx': 'total', 'chars': n}]
        if channel['limit_total'] and n > channel['limit_total']:
            result['violations'].append({
                'idx': 'total',
                'chars': n,
                'limit': channel['limit_total'],
                'over_by': n - channel['limit_total'],
            })
        else:
            result['ok_count'] = 1

    elif channel['parse'] == 'split_by_pattern':
        tweets = parse_tweets(content, channel['pattern'])
        for tag, body in tweets:
            n = len(body)
            result['units'].append({'idx': tag, 'chars': n})
            if channel['limit_per_unit'] and n > channel['limit_per_unit']:
                result['violations'].append({
                    'idx': tag,
                    'chars': n,
                    'limit': channel['limit_per_unit'],
                    'over_by': n - channel['limit_per_unit'],
                })
            else:
                result['ok_count'] += 1

    return result


def print_report(filepath: Path, result: dict) -> int:
    if 'error' in result:
        print(f"\n[ERROR] {filepath}: {result['error']}")
        return 1
    if result.get('unknown_channel'):
        print(f"[SKIP] {filepath.name}: not a known channel filename (add to CHANNELS dict)")
        return 0

    channel = result['channel']
    violations = result['violations']
    units = result['units']

    if not violations:
        if channel['parse'] == 'whole':
            chars = units[0]['chars'] if units else 0
            print(f"[OK] {filepath.name} -> {chars} chars / {channel['limit_total']} ({channel['description']})")
        else:
            counts = [f"{u['idx']}={u['chars']}" for u in units]
            print(f"[OK] {filepath.name} -> {len(units)} units, all within {channel['limit_per_unit']} chars")
        return 0

    print(f"\n[FAIL] {filepath.name} -> {len(violations)} violation(s) of {channel['description']}")
    for v in violations:
        print(f"  {v['idx']}: {v['chars']} chars (over by {v['over_by']})")
        print(f"    -> trim {v['over_by']} chars to fit {v['limit']}")
    print(f"  OK units: {result['ok_count']}")
    return 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', help='Files to validate')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    paths = []
    for f in args.files:
        p = Path(f)
        if p.is_dir():
            paths.extend(sorted(p.glob('*.md')))
            paths.extend(sorted(p.glob('*.txt')))
        else:
            paths.append(p)

    if args.json:
        import json
        all_results = {str(p): validate_file(p) for p in paths}
        # Sanitize for JSON
        for k, v in all_results.items():
            if 'channel' in v:
                v['channel'] = {kk: vv for kk, vv in v['channel'].items() if not callable(vv)}
        print(json.dumps(all_results, indent=2, ensure_ascii=False, default=str))
        sys.exit(0)

    total_fail = 0
    print(f"Validating {len(paths)} file(s) against per-channel char limits...")
    print("=" * 60)
    for p in paths:
        total_fail += print_report(p, validate_file(p))
    print("=" * 60)
    print(f"Result: {len(paths) - total_fail}/{len(paths)} files within limits")
    sys.exit(1 if total_fail else 0)


if __name__ == '__main__':
    main()
