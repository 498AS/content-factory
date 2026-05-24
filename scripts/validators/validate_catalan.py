"""Catalan-specific orthography validator.

Checks that *_ca.md files include expected catalan-specific characters
when corresponding words appear:
- ç (ce trencada): in "informacio", "organitzacio", etc.
- l·l (punt volat): in "intel·ligencia", "col·laborar", "sol·licitar"
- accents: minimal pass for common words

Advisory only. Exits 0.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Word-stem -> expected form patterns. If the bare stem appears without the
# special character, flag it.
CE_TRENCADA_HINTS = [
    (r"\binformaci[oó]\b", "informació", "ç"),
    (r"\borganitzaci[oó]\b", "organització", "ç"),
    (r"\bproducci[oó]\b", "producció", "ç"),
    (r"\bdireccí?[oó]\b", "direcció", "ç"),
    (r"\bcomunicaci[oó]\b", "comunicació", "ç"),
    (r"\baplicaci[oó]\b", "aplicació", "ç"),
    (r"\bsoluci[oó]\b", "solució", "ç"),
    (r"\bcanc[oó]\b", "cançó", "ç"),
]

PUNT_VOLAT_HINTS = [
    (r"\bintelligenc", "intel·ligencia", "l·l"),
    (r"\bcollabor", "col·laborar", "l·l"),
    (r"\bsollicit", "sol·licitar", "l·l"),
    (r"\bcollocaci", "col·locació", "l·l"),
    (r"\billegal\b", "il·legal", "l·l"),
]

FALSE_FRIENDS = [
    (r"\bbilions?\b", "'bilions' es falso amigo. Usar 'mil milions' para billions."),
]


def detect_lang(path: Path) -> str:
    name = path.name.lower()
    if name.endswith("_ca.md") or "_ca_" in name or name.endswith(".ca.md"):
        return "ca"
    return "other"


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    if detect_lang(path) != "ca":
        return issues
    if not path.exists():
        return issues
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return issues

    if "ç" not in text and re.search(r"\b(informaci|organitzaci|producci|direcci|comunicaci|aplicaci|soluci)[oó]", text, flags=re.IGNORECASE):
        issues.append(f"{path}: archivo CA sin ningun caracter 'ç'. Verificar ortografia (informació, organització, producció...).")

    if "l·l" not in text and "L·L" not in text:
        for pattern, expected, _ in PUNT_VOLAT_HINTS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                issues.append(f"{path}: archivo CA con palabra que requiere 'l·l' (punt volat). Falta el caracter en el documento. Esperado: '{expected}'.")
                break

    for lineno, line in enumerate(text.splitlines(), 1):
        for pattern, msg in FALSE_FRIENDS:
            for _ in re.finditer(pattern, line, flags=re.IGNORECASE):
                snippet = line.strip()[:120]
                issues.append(f"{path}:{lineno}: {msg} | linea: '{snippet}'")

    return issues


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return 0
    path = Path(argv[1])
    issues = check_file(path)
    for it in issues:
        print(f"[catalan] {it}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
