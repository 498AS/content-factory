"""Title sentence-case validator.

Checks that markdown headings (# ... ######) use sentence case:
- Only the first letter of the heading capitalized
- Proper nouns and acronyms preserved
- The rest in lowercase

Outputs warnings to stdout. Exits 0 always (advisory).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ACRONYMS = {
    "IA", "AI", "SEO", "SEM", "GEO", "LLM", "LLMS", "API", "APIs",
    "SaaS", "B2B", "B2C", "FAQ", "FAQs", "CTA", "CTAs", "UX", "UI",
    "CSS", "HTML", "JSON", "XML", "URL", "URLs", "PDF", "MCN",
    "NPS", "GA4", "TLS", "RSS", "OG", "WP", "REST", "CLI", "MCP",
    "ZOOPA", "498AS", "SAM", "GEORADAR",
    "OK", "ID", "IDs", "IT", "OS",
}

KNOWN_PROPER_NOUNS = {
    "Carlos", "Ortet", "Zoopa", "498AS", "498A", "GEOradar", "GEORADAR",
    "OpenAI", "Anthropic", "ChatGPT", "Claude", "Gemini", "Google",
    "Meta", "Microsoft", "Apple", "Amazon", "Perplexity",
    "WordPress", "LinkedIn", "Substack", "Medium", "Twitter", "Threads",
    "WhatsApp", "Telegram", "YouTube", "Reddit", "TikTok", "Instagram",
    "Mastodon", "Bluesky", "Farcaster", "Mirror", "Discord", "Quora",
    "Hashnode", "HackerNoon", "DZone", "Polylang", "Yoast",
    "Carles", "Porta", "Wired", "Axios",
    "Barcelona", "Madrid", "Catalunya", "Espanya", "Espana",
    "Europa", "America", "Amerca",
    "PortAventura", "Shambala", "Atmos", "Dolby",
    "Long", "Night", "Crown", "Robot", "Tenet", "Interstellar",
    "Wire", "Detective", "True", "Crime",
    "Samsung", "Sony", "Sonos", "LG", "TCL", "Hisense", "Panasonic",
    "GoPro", "iPhone", "MacBook", "Crystal",
    "Midjourney", "Sora", "Flux", "Reality",
    "DaVinci", "Resolve", "Baselight",
    "BVM-HX310", "TikTok", "Spotify",
    "Atlas", "Studio", "EBU", "R128",
    "Si", "No",
}


def is_proper_or_acronym(token: str) -> bool:
    cleaned = re.sub(r"[^\w·-]", "", token)
    if not cleaned:
        return True
    if cleaned in ACRONYMS or cleaned.upper() in ACRONYMS:
        return True
    if cleaned in KNOWN_PROPER_NOUNS:
        return True
    if len(cleaned) <= 4 and cleaned.isupper():
        return True
    if cleaned[0].isdigit():
        return True
    return False


def find_title_case_in_heading(text: str) -> list[str]:
    """Return list of suspect tokens that look Title-Cased."""
    tokens = text.split()
    if len(tokens) < 3:
        return []
    suspects: list[str] = []
    for i, tok in enumerate(tokens):
        if i == 0:
            continue
        cleaned = re.sub(r"[^\w·-]", "", tok)
        if not cleaned:
            continue
        if cleaned[0].isupper() and not is_proper_or_acronym(tok):
            suspects.append(tok)
    if len(suspects) >= max(2, len(tokens) // 3):
        return suspects
    return []


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return issues
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return issues

    for lineno, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not m:
            continue
        heading = m.group(2).strip()
        heading_clean = re.sub(r"\*([^*]+)\*", "TITLE", heading)
        heading_clean = re.sub(r"_([^_]+)_", "TITLE", heading_clean)
        heading_clean = re.sub(r"<em>([^<]+)</em>", "TITLE", heading_clean, flags=re.IGNORECASE)
        heading_clean = re.sub(r"<i>([^<]+)</i>", "TITLE", heading_clean, flags=re.IGNORECASE)
        heading_clean = re.sub(r"`([^`]+)`", "TITLE", heading_clean)
        heading_clean = re.sub(r"[~]", "", heading_clean)
        suspects = find_title_case_in_heading(heading_clean)
        if suspects:
            issues.append(
                f"{path}:{lineno}: heading parece Title Case (sentence case esperado). "
                f"Tokens sospechosos: {', '.join(suspects[:5])}"
            )
    return issues


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return 0
    path = Path(argv[1])
    issues = check_file(path)
    for it in issues:
        print(f"[titles] {it}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
