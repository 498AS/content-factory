"""Validator runner — entrypoint for Claude Code PostToolUse hook.

Reads JSON from stdin (the hook payload), extracts tool_input.file_path,
and runs the relevant validators if the path is inside a content-factory
project's output/ directory.

Hook payload contract (Claude Code):
  {
    "hook_event_name": "PostToolUse",
    "tool_name": "Write" | "Edit" | "MultiEdit",
    "tool_input": {"file_path": "...", ...},
    ...
  }

Output: warnings on stdout. Always exits 0 (advisory).

Manual usage:
  python3 run_all.py /path/to/output/blog.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

VALIDATORS_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(VALIDATORS_DIR))

import validate_titles  # noqa: E402
import validate_numbers  # noqa: E402
import validate_catalan  # noqa: E402
import validate_blog_completeness  # noqa: E402

OUTPUT_EXTS = {".md", ".txt"}


def file_path_from_stdin() -> Path | None:
    if sys.stdin.isatty():
        return None
    raw = sys.stdin.read().strip()
    if not raw:
        return None
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return None
    tool_input = payload.get("tool_input") or {}
    fp = tool_input.get("file_path")
    if not fp:
        return None
    return Path(fp)


def is_target(path: Path) -> bool:
    if path.suffix.lower() not in OUTPUT_EXTS:
        return False
    parents = {p.name for p in path.parents}
    return "output" in parents


def run(path: Path) -> list[str]:
    issues: list[str] = []
    issues.extend(f"[titles] {it}" for it in validate_titles.check_file(path))
    issues.extend(f"[numbers] {it}" for it in validate_numbers.check_file(path))
    issues.extend(f"[catalan] {it}" for it in validate_catalan.check_file(path))
    issues.extend(f"[blog] {it}" for it in validate_blog_completeness.check_file(path))
    return issues


def main(argv: list[str]) -> int:
    if len(argv) >= 2:
        path = Path(argv[1])
    else:
        path = file_path_from_stdin()
    if path is None:
        return 0
    if not path.exists():
        return 0
    if not is_target(path):
        return 0

    issues = run(path)
    if not issues:
        return 0

    print(f"[content-factory validators] {path.name}: {len(issues)} aviso(s)")
    for it in issues:
        print(f"  {it}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
