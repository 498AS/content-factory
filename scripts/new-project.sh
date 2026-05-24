#!/usr/bin/env bash
# new-project.sh — Crea un proyecto de content-factory con estructura estandar.
#
# Uso:
#   ./_system/new-project.sh             # interactivo, pide tema
#   ./_system/new-project.sh tema-corto  # tema desde argumento
#   ./_system/new-project.sh tema --paste # crea source.md desde el portapapeles

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

THEME="${1:-}"
PASTE="${2:-}"

if [[ -z "$THEME" ]]; then
  read -rp "Tema (corto, sin espacios; ej: 'small-llms'): " THEME
fi

THEME="${THEME// /-}"
THEME="${THEME//_/-}"
THEME="$(echo "$THEME" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]-')"

if [[ -z "$THEME" ]]; then
  echo "ERROR: tema vacio o invalido tras normalizacion." >&2
  exit 1
fi

DATE="$(date +%d%m%Y)"
PROJECT="project_${DATE}_${THEME}"

if [[ -d "$PROJECT" ]]; then
  echo "ERROR: la carpeta '$PROJECT' ya existe." >&2
  exit 1
fi

mkdir -p "$PROJECT/output"

if [[ "$PASTE" == "--paste" ]] && command -v pbpaste >/dev/null 2>&1; then
  pbpaste > "$PROJECT/source.md"
  WORDS=$(wc -w < "$PROJECT/source.md" | tr -d ' ')
  echo "[ok] source.md creado desde portapapeles ($WORDS palabras)."
else
  cat > "$PROJECT/source.md" <<'EOF'
# Source

<!-- Pega aqui el contenido fuente del proyecto. -->
<!-- Si hay multiples items, todos se trataran como igualmente importantes. -->
EOF
  echo "[ok] source.md creado vacio. Pega el contenido fuente."
fi

cat > "$PROJECT/metadata.json" <<EOF
{
  "project_id": "$PROJECT",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "source_words": null,
  "channels_generated": [],
  "published": {},
  "metrics": {},
  "system_prompt_version": "2.0"
}
EOF

echo
echo "  Proyecto:    $PROJECT"
echo "  Source:      $PROJECT/source.md"
echo "  Output:      $PROJECT/output/"
echo "  Metadata:    $PROJECT/metadata.json"
echo
echo "Siguiente paso en Claude Code:"
echo "  /content-factory $PROJECT"
echo
echo "  o simplemente: 'lanza el proyecto $PROJECT'"

if command -v open >/dev/null 2>&1 && [[ "$PASTE" != "--paste" ]]; then
  open "$PROJECT/source.md" 2>/dev/null || true
fi
