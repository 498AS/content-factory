"""False-friend numerics validator.

In ES/CA, "billion" (EN, 10^9) is NOT "billon"/"bilio" (those mean 10^12).
The correct translation is "mil millones" (ES) / "mil milions" (CA).

Flags any occurrence of suspect terms in ES/CA outputs and warns the user
to verify them manually. Exits 0 (advisory).

Lang detection by filename suffix:
  *_en.md / english markers -> skip
  *_ca.md / catalan markers -> CA mode
  default -> ES mode
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ES_SUSPECT_PATTERNS = [
    (r"\bbillón(es)?\b", "'billón' suele ser falso amigo de 'billion' (EN). 'billion' = 'mil millones' en ES, no 'billón'."),
    (r"\bbilliones?\b", "'billion(es)' no existe en ES. Usar 'mil millones' o 'billones' segun el numero real."),
]
CA_SUSPECT_PATTERNS = [
    (r"\bbilions?\b", "'bilions' suele ser falso amigo de 'billions' (EN). 'billion' = 'mil milions' en CA, no 'bilions'."),
    (r"\bbiliones?\b", "Forma castellanizada incorrecta en CA. Usar 'mil milions' para billions."),
]


def detect_lang(path: Path) -> str:
    name = path.name.lower()
    if name.endswith("_en.md") or "_en_" in name or name.endswith(".en.md"):
        return "en"
    if name.endswith("_ca.md") or "_ca_" in name or name.endswith(".ca.md"):
        return "ca"
    if name.endswith("_es.md") or "_es_" in name or name.endswith(".es.md"):
        return "es"
    return "es"


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return issues
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return issues

    lang = detect_lang(path)
    if lang == "en":
        return issues
    patterns = CA_SUSPECT_PATTERNS if lang == "ca" else ES_SUSPECT_PATTERNS

    for lineno, line in enumerate(text.splitlines(), 1):
        for pattern, msg in patterns:
            for m in re.finditer(pattern, line, flags=re.IGNORECASE):
                snippet = line.strip()[:120]
                issues.append(f"{path}:{lineno}: {msg} | linea: '{snippet}'")
    return issues


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return 0
    path = Path(argv[1])
    issues = check_file(path)
    for it in issues:
        print(f"[numbers] {it}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
