---
title: Content Factory — Workspace WriterBatch
tipo: project-index
cliente: Interno Zoopa
proyecto_path: ~/Documents/claudecode-proj/contentfactory/
fecha_creacion: 2026-05-07
estado: activo
tags:
  - project-index
  - content-factory
  - writerbatch
  - workspace
---

# Content Factory — Workspace WriterBatch

## Quick Access

- **Código:** `cd ~/Documents/claudecode-proj/contentfactory`
- **Tipo:** Workspace operativo — sistema WriterBatch Zoopa para generación de contenido multicanal

---

## Contexto

Workspace raíz del sistema WriterBatch (Content Factory) de Zoopa: genera contenido multicanal (hasta 35 canales, 4 idiomas) a partir de un `source.md` con preguntas pre-publicación, generación de outputs y revisión ortográfica/estilo. Contiene la infraestructura común (`_system/`, `publisher/`, `validators/`, scripts `create_project.sh`, `new-project.sh`, `metadata.py`) y todos los proyectos individuales generados (clawdbook, content-library, ai-overviews-research, chatgpt-shopping-images, project-* fechados, etc.).

---

## Entregables locales

- `_system/HOW-TO-NEW-PROJECT.md`, `launch.md`, `metadata-schema.md`
- `_system/create_project.sh`, `new-project.sh`, `metadata.py`
- `_system/checklist_linkedin_zoopa.rtf`, `LLMS_ZOOPA_EXTENSO.TXT`
- Subproyectos: `clawdbook/`, `content-library/`, `ai-overviews-research/`, `project_*/`

---

## Notas

Skill propia `content-factory` orquesta el workflow completo (selección de canales, preguntas, generación, revisión). Doc índice del workspace — los sub-proyectos individuales viven dentro de la carpeta y no se documentan por separado en el vault.

---

*Creado: 2026-05-07 (auditoría vault)*
