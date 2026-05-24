#!/usr/bin/env python3
"""
Anti-LLM patterns validator for content-factory outputs.

Detects (per orthography-rules.md § 3):
- 3.1: Em-dash (—) and en-dash (–) in body text
- 3.2: Relative temporal markers (esta semana, este año, hoy, etc.)
- 3.3: Formulaic LLM phrases (Lectura completa con datos verificados, etc.)
- 3.4: Arrow bullets (→) used as list markers

Usage:
    python3 validate_anti_llm_patterns.py path/to/file.md [path/to/file2.txt ...]
    python3 validate_anti_llm_patterns.py output/*.md output/*.txt

Exit code: 0 = clean, 1 = violations found.
"""
import sys, re, argparse
from pathlib import Path


# Em-dash and en-dash patterns
DASH_PATTERNS = [
    (re.compile(r'—'), '— (em-dash, U+2014)', '. / : / , / ()'),
    (re.compile(r'–'), '– (en-dash, U+2013)', '-'),
]

# Temporal relative markers (Spanish + English)
TEMPORAL_PATTERNS = [
    (re.compile(r'\besta semana\b', re.IGNORECASE), 'esta semana', 'fecha exacta o atemporal'),
    (re.compile(r'\beste mes\b', re.IGNORECASE), 'este mes', 'mes concreto'),
    (re.compile(r'\beste año\b', re.IGNORECASE), 'este año', 'año concreto (en 2026)'),
    (re.compile(r'\bayer\b', re.IGNORECASE), 'ayer', 'fecha concreta'),
    (re.compile(r'\bma[ñn]ana\b', re.IGNORECASE), 'mañana', 'fecha concreta'),
    (re.compile(r'\bhoy\b', re.IGNORECASE), 'hoy', 'sin marcador o fecha'),
    (re.compile(r'\brecientemente\b', re.IGNORECASE), 'recientemente', 'fecha exacta'),
    (re.compile(r'\b[uú]ltimamente\b', re.IGNORECASE), 'últimamente', 'periodo concreto'),
    (re.compile(r'\bactualmente\b', re.IGNORECASE), 'actualmente', 'eliminar o "en 2026"'),
    (re.compile(r'\ben los [uú]ltimos d[ií]as\b', re.IGNORECASE), 'en los últimos días', 'periodo concreto'),
    (re.compile(r'\ben los [uú]ltimos meses\b', re.IGNORECASE), 'en los últimos meses', 'periodo concreto'),
    (re.compile(r'\bthis week\b', re.IGNORECASE), 'this week', 'specific date or atemporal'),
    (re.compile(r'\bthis month\b', re.IGNORECASE), 'this month', 'specific month'),
    (re.compile(r'\bthis year\b', re.IGNORECASE), 'this year', 'specific year (in 2026)'),
    (re.compile(r'\btoday\b', re.IGNORECASE), 'today', 'remove or specific date'),
    (re.compile(r'\brecently\b', re.IGNORECASE), 'recently', 'specific date'),
    (re.compile(r'\bcurrently\b', re.IGNORECASE), 'currently', 'remove or specific time'),
    (re.compile(r'\blately\b', re.IGNORECASE), 'lately', 'specific period'),
    (re.compile(r'\bnowadays\b', re.IGNORECASE), 'nowadays', 'remove or rewrite'),
]

# Formulaic LLM phrases (ES + EN)
FORMULAIC_PATTERNS = [
    (re.compile(r'Esa frase la oir[áa]s en cada', re.IGNORECASE), '"Esa frase la oirás en cada panel..."', 'cortar la frase'),
    (re.compile(r'Tambi[eé]n es, t[eé]cnicamente, falsa', re.IGNORECASE), '"También es, técnicamente, falsa"', '"Y es falsa" o reformular'),
    (re.compile(r'Lectura completa con datos verificados', re.IGNORECASE), '"Lectura completa con datos verificados y fuentes:"', '"Lo conté aquí:" o nada'),
    (re.compile(r'^\s*La conclusi[oó]n:\s*$', re.IGNORECASE | re.MULTILINE), '"La conclusión:" como cierre', 'terminar con frase sin etiqueta'),
    (re.compile(r'\bdelve into\b', re.IGNORECASE), '"delve into"', 'mirar / entrar / abrir'),
    (re.compile(r'\bdeep dive\b', re.IGNORECASE), '"deep dive"', 'análisis / mirada profunda'),
    (re.compile(r'\bleverage\b', re.IGNORECASE), '"leverage"', 'usar / aprovechar'),
    (re.compile(r'\brobust\b', re.IGNORECASE), '"robust"', 'sólido / firme'),
    (re.compile(r'\b(crucial|pivotal)\b', re.IGNORECASE), '"crucial" / "pivotal"', 'quitar el adjetivo'),
    (re.compile(r'\b(groundbreaking|revolutionary|cutting-edge)\b', re.IGNORECASE), 'adjetivo vacío', 'dato medible o quitar'),
    (re.compile(r'\bharness\b.*\b(power|potential)\b', re.IGNORECASE), '"harness the power/potential of"', 'usar / aprovechar'),
    (re.compile(r'\bunlock\b.*\b(potential|value)\b', re.IGNORECASE), '"unlock potential/value"', 'reformular concreto'),
    (re.compile(r'\btapestry\b', re.IGNORECASE), '"tapestry"', 'nombrar la cosa concreta'),
    (re.compile(r'\b(landscape|ecosystem)\b', re.IGNORECASE), '"landscape" / "ecosystem"', 'sector / industria / red'),
    (re.compile(r'\bvibrant\b', re.IGNORECASE), '"vibrant"', 'algo medible'),
    (re.compile(r'\bfundamentalmente\b', re.IGNORECASE), '"fundamentalmente"', 'borrar'),
    (re.compile(r'\besencialmente\b', re.IGNORECASE), '"esencialmente"', 'borrar'),
    (re.compile(r'\bmerece la pena destacar que\b', re.IGNORECASE), '"merece la pena destacar que"', 'destacarlo y ya'),
    (re.compile(r'\bcabe destacar que\b', re.IGNORECASE), '"cabe destacar que"', 'destacarlo y ya'),
    (re.compile(r'\bnavigate the\b', re.IGNORECASE), '"navigate the"', 'pasar por / lidiar con'),
    (re.compile(r'\bel verdadero \w+\b', re.IGNORECASE), '"el verdadero X"', 'dato directo'),
    (re.compile(r'\bTe lo explico en \d+ tuits', re.IGNORECASE), '"Te lo explico en N tuits"', 'empezar directo con dato'),
    (re.compile(r'\baqu[ií] va una historia\b', re.IGNORECASE), '"aquí va una historia"', 'empezar directo'),
    (re.compile(r'\baqu[ií] va un hilo\b', re.IGNORECASE), '"aquí va un hilo"', 'empezar directo'),
]

# Arrow bullets (→ used as list marker, not in arrow notation like A→B)
ARROW_PATTERNS = [
    (re.compile(r'^[\s\-\*]*→\s+\S', re.MULTILINE), '→ como bullet de lista', 'punto y aparte + frase'),
]

# Lines that look like HN auto-flag triggers (company + funding number)
HN_FLAG_PATTERN = re.compile(
    r'^\s*[\*\-]\s+[A-Z][A-Za-z\s\.\(\)]+\([A-Z]{2}\)\.?\s*[\$€]?\d+[KkMm]?\b',
    re.MULTILINE
)


def line_for_offset(content: str, offset: int) -> int:
    """Get line number for character offset."""
    return content.count('\n', 0, offset) + 1


def excerpt(content: str, offset: int, length: int, context: int = 40) -> str:
    """Get context excerpt around a match."""
    start = max(0, offset - context)
    end = min(len(content), offset + length + context)
    text = content[start:end].replace('\n', '\\n')
    return f"...{text}..."


def validate_file(filepath: Path) -> dict:
    """Return dict with violations per category."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return {'error': str(e)}

    # Strip meta sections (HTML comments, code blocks, frontmatter)
    # Don't validate content inside ``` code blocks
    stripped = content
    # Remove frontmatter
    if stripped.startswith('---\n'):
        end = stripped.find('\n---\n', 4)
        if end > 0:
            stripped = ' ' * (end + 5) + stripped[end + 5:]
    # Mask code blocks
    def mask_block(m):
        return ' ' * len(m.group(0))
    stripped = re.sub(r'```.*?```', mask_block, stripped, flags=re.DOTALL)
    # Mask inline code
    stripped = re.sub(r'`[^`]+`', mask_block, stripped)
    # Mask URLs
    stripped = re.sub(r'https?://\S+', mask_block, stripped)

    violations = {
        'dashes': [],
        'temporal': [],
        'formulaic': [],
        'arrows': [],
        'hn_flag_pattern': [],
    }

    for pat, name, alt in DASH_PATTERNS:
        for m in pat.finditer(stripped):
            violations['dashes'].append({
                'line': line_for_offset(stripped, m.start()),
                'match': name,
                'alternative': alt,
                'excerpt': excerpt(stripped, m.start(), len(m.group())),
            })

    for pat, name, alt in TEMPORAL_PATTERNS:
        for m in pat.finditer(stripped):
            violations['temporal'].append({
                'line': line_for_offset(stripped, m.start()),
                'match': name,
                'alternative': alt,
                'excerpt': excerpt(stripped, m.start(), len(m.group())),
            })

    for pat, name, alt in FORMULAIC_PATTERNS:
        for m in pat.finditer(stripped):
            violations['formulaic'].append({
                'line': line_for_offset(stripped, m.start()),
                'match': name,
                'alternative': alt,
                'excerpt': excerpt(stripped, m.start(), len(m.group())),
            })

    for pat, name, alt in ARROW_PATTERNS:
        for m in pat.finditer(stripped):
            violations['arrows'].append({
                'line': line_for_offset(stripped, m.start()),
                'match': name,
                'alternative': alt,
                'excerpt': excerpt(stripped, m.start(), len(m.group())),
            })

    for m in HN_FLAG_PATTERN.finditer(stripped):
        violations['hn_flag_pattern'].append({
            'line': line_for_offset(stripped, m.start()),
            'match': 'bullet con empresa+pais+cifra (patron HN auto-flag)',
            'alternative': 'prosa fluida sin bullets cuando publiques en HN/Reddit',
            'excerpt': excerpt(stripped, m.start(), len(m.group())),
        })

    return violations


def print_report(filepath: Path, violations: dict) -> int:
    """Print human report. Return 1 if any violations, 0 if clean."""
    if 'error' in violations:
        print(f"\n[ERROR] {filepath}: {violations['error']}")
        return 1

    total = sum(len(v) for v in violations.values())
    if total == 0:
        print(f"[OK] {filepath} -> clean (0 violations)")
        return 0

    print(f"\n[FAIL] {filepath} -> {total} violation(s)")
    for category, items in violations.items():
        if not items:
            continue
        print(f"  {category} ({len(items)}):")
        for v in items[:5]:
            print(f"    line {v['line']}: {v['match']}")
            print(f"      -> alternative: {v['alternative']}")
            print(f"      -> excerpt: {v['excerpt']}")
        if len(items) > 5:
            print(f"    ... +{len(items)-5} more")
    return 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', help='Files to validate')
    parser.add_argument('--strict', action='store_true',
                       help='Fail on any violation (default: only on dashes/temporal)')
    parser.add_argument('--json', action='store_true', help='Output JSON')
    args = parser.parse_args()

    paths = []
    for f in args.files:
        p = Path(f)
        if p.is_dir():
            paths.extend(p.glob('*.md'))
            paths.extend(p.glob('*.txt'))
        else:
            paths.append(p)

    if not paths:
        print("No files to check.")
        sys.exit(0)

    total_fail = 0
    if args.json:
        import json
        all_results = {}
        for p in paths:
            all_results[str(p)] = validate_file(p)
        print(json.dumps(all_results, indent=2, ensure_ascii=False))
        sys.exit(0)

    print(f"Validating {len(paths)} file(s) against anti-LLM patterns...")
    print("=" * 60)
    for p in paths:
        v = validate_file(p)
        total_fail += print_report(p, v)

    print("=" * 60)
    print(f"Result: {len(paths) - total_fail}/{len(paths)} files clean")
    sys.exit(1 if total_fail else 0)


if __name__ == '__main__':
    main()
