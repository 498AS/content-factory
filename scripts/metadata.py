"""metadata.py — Helper CLI para metadata.json por proyecto.

Schema en _system/metadata-schema.md.

Subcomandos:
  init <project>                       crea metadata.json si no existe
  set-generated <project> --channels k1,k2
  add-publication <project> --channel k --url ... [--wp-post-id N] [--account N] [--categories 2231,2233] [--featured-media N]
  set-source-words <project> [--auto]  cuenta palabras de source.md
  set-tags <project> --tags t1,t2
  set-note <project> --note "..."
  summary <project>                    imprime resumen
  recent --days N                      lista publicaciones recientes en todos los proyectos
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "2.0"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def project_path(name: str) -> Path:
    p = REPO_ROOT / name
    if not p.exists():
        raise SystemExit(f"ERROR: proyecto '{name}' no existe en {REPO_ROOT}")
    return p


def metadata_path(project: str) -> Path:
    return project_path(project) / "metadata.json"


def load(project: str) -> dict:
    fp = metadata_path(project)
    if not fp.exists():
        return {
            "project_id": project,
            "created_at": utc_now(),
            "source_words": None,
            "system_prompt_version": SCHEMA_VERSION,
            "channels_generated": [],
            "published": {},
            "metrics": {},
            "tags": [],
            "notes": "",
        }
    with fp.open(encoding="utf-8") as f:
        return json.load(f)


def save(project: str, data: dict) -> None:
    fp = metadata_path(project)
    fp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> int:
    fp = metadata_path(args.project)
    if fp.exists() and not args.force:
        print(f"[skip] {fp} ya existe (usar --force para sobrescribir)")
        return 0
    data = load(args.project) if not fp.exists() else {
        "project_id": args.project,
        "created_at": utc_now(),
        "source_words": None,
        "system_prompt_version": SCHEMA_VERSION,
        "channels_generated": [],
        "published": {},
        "metrics": {},
        "tags": [],
        "notes": "",
    }
    save(args.project, data)
    print(f"[ok] {fp}")
    return 0


def cmd_set_generated(args: argparse.Namespace) -> int:
    data = load(args.project)
    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    if args.replace:
        data["channels_generated"] = channels
    else:
        existing = set(data.get("channels_generated", []))
        existing.update(channels)
        data["channels_generated"] = sorted(existing)
    save(args.project, data)
    print(f"[ok] channels_generated: {data['channels_generated']}")
    return 0


def cmd_add_publication(args: argparse.Namespace) -> int:
    data = load(args.project)
    entry: dict = {
        "url": args.url,
        "published_at": args.published_at or utc_now(),
    }
    if args.wp_post_id is not None:
        entry["wp_post_id"] = args.wp_post_id
    if args.account:
        entry["account"] = args.account
    if args.categories:
        entry["categories"] = [int(x) for x in args.categories.split(",") if x.strip()]
    if args.featured_media is not None:
        entry["featured_media"] = args.featured_media

    data.setdefault("published", {})[args.channel] = entry

    generated = set(data.get("channels_generated", []))
    generated.add(args.channel)
    data["channels_generated"] = sorted(generated)

    save(args.project, data)
    print(f"[ok] published.{args.channel} = {json.dumps(entry, ensure_ascii=False)}")
    return 0


def cmd_set_source_words(args: argparse.Namespace) -> int:
    data = load(args.project)
    if args.value is not None:
        data["source_words"] = args.value
    elif args.auto:
        src = project_path(args.project) / "source.md"
        if not src.exists():
            print(f"ERROR: {src} no existe")
            return 1
        text = src.read_text(encoding="utf-8")
        words = len(re.findall(r"\b\w+\b", text))
        data["source_words"] = words
    else:
        print("ERROR: pasa --value N o --auto")
        return 1
    save(args.project, data)
    print(f"[ok] source_words = {data['source_words']}")
    return 0


def cmd_set_tags(args: argparse.Namespace) -> int:
    data = load(args.project)
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    data["tags"] = tags
    save(args.project, data)
    print(f"[ok] tags = {tags}")
    return 0


def cmd_set_note(args: argparse.Namespace) -> int:
    data = load(args.project)
    data["notes"] = args.note
    save(args.project, data)
    print(f"[ok] notes set ({len(args.note)} chars)")
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    data = load(args.project)
    print(f"Project:   {data.get('project_id')}")
    print(f"Created:   {data.get('created_at')}")
    print(f"Source:    {data.get('source_words')} palabras")
    print(f"Tags:      {', '.join(data.get('tags') or [])}")
    print(f"Generated: {len(data.get('channels_generated') or [])} canales")
    for c in data.get("channels_generated") or []:
        print(f"  - {c}")
    pub = data.get("published") or {}
    print(f"Published: {len(pub)} canales")
    for c, info in pub.items():
        url = info.get("url", "")
        when = info.get("published_at", "")
        print(f"  - {c}  {when}  {url}")
    return 0


def cmd_recent(args: argparse.Namespace) -> int:
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    rows: list[tuple[str, str, str, str]] = []
    for md in REPO_ROOT.glob("project*/metadata.json"):
        try:
            data = json.loads(md.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for channel, info in (data.get("published") or {}).items():
            ts = info.get("published_at")
            if not ts:
                continue
            try:
                t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except ValueError:
                continue
            if t < cutoff:
                continue
            rows.append((ts, data.get("project_id", md.parent.name), channel, info.get("url", "")))
    rows.sort()
    for ts, project, channel, url in rows:
        print(f"{ts}  {project}  {channel}  {url}")
    if not rows:
        print(f"(sin publicaciones en los ultimos {args.days} dias)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="metadata.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init")
    sp.add_argument("project")
    sp.add_argument("--force", action="store_true")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("set-generated")
    sp.add_argument("project")
    sp.add_argument("--channels", required=True)
    sp.add_argument("--replace", action="store_true")
    sp.set_defaults(func=cmd_set_generated)

    sp = sub.add_parser("add-publication")
    sp.add_argument("project")
    sp.add_argument("--channel", required=True)
    sp.add_argument("--url", required=True)
    sp.add_argument("--wp-post-id", type=int)
    sp.add_argument("--account")
    sp.add_argument("--categories")
    sp.add_argument("--featured-media", type=int)
    sp.add_argument("--published-at")
    sp.set_defaults(func=cmd_add_publication)

    sp = sub.add_parser("set-source-words")
    sp.add_argument("project")
    sp.add_argument("--value", type=int)
    sp.add_argument("--auto", action="store_true")
    sp.set_defaults(func=cmd_set_source_words)

    sp = sub.add_parser("set-tags")
    sp.add_argument("project")
    sp.add_argument("--tags", required=True)
    sp.set_defaults(func=cmd_set_tags)

    sp = sub.add_parser("set-note")
    sp.add_argument("project")
    sp.add_argument("--note", required=True)
    sp.set_defaults(func=cmd_set_note)

    sp = sub.add_parser("summary")
    sp.add_argument("project")
    sp.set_defaults(func=cmd_summary)

    sp = sub.add_parser("recent")
    sp.add_argument("--days", type=int, default=7)
    sp.set_defaults(func=cmd_recent)

    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
