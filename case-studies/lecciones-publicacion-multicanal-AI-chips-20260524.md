---
title: Lecciones de la publicación multicanal · proyecto AI Chips Economy
date: 2026-05-24
project: AI Chips Economy (23 mayo 2026)
status: live
channels-published: 8
related:
  - "[[proceso-fabricacion-chips-ia-20260524]]"
  - "[[playbook-publicacion-zoopa-3-idiomas-20260523]]"
  - "[[guia-linkedin-voz-carlos-ortet-20260510]]"
tags: [content-factory, lessons-learned, x-twitter, facebook, wordpress, geo, ai-chips]
---

# Lecciones de la publicación multicanal · AI Chips Economy

> Cierra el ciclo del proyecto "El tejido invisible de la IA" (publicado entre 23-24 mayo 2026). Captura las decisiones operativas y los aprendizajes nuevos no documentados antes para que el próximo proyecto multicanal arranque con todo en sitio.

## URLs canónicas (todas live)

| Canal | URL | Idioma |
|-------|-----|--------|
| Blog zoopa.es | https://zoopa.es/es/geo-ia-visibilidad/tejido-invisible-ia-chips-geopolitica/ | ES |
| Blog zoopa.es | https://zoopa.es/en/innovation-technology/invisible-fabric-ai-chips-geopolitics/ | EN |
| Blog zoopa.es | https://zoopa.es/ca/innovacio-tecnologia/teixit-invisible-ia-xips-geopolitica/ | CA |
| Medium | https://medium.com/@carlosortet/the-invisible-fabric-of-ai-chips-are-not-a-war-between-two-but-a-global-fabric-zoopa-es-1ece5d274e3d | EN |
| Substack | https://open.substack.com/pub/carlosortet/p/el-tejido-invisible-de-la-ia | ES |
| LinkedIn personal | (publicado con vídeo nativo, URL EN en comentario) | ES |
| X / Twitter | https://x.com/carlos_ortet/status/2058492127642865883 (hilo 19 tuits) | ES |
| WhatsApp Canal | Publicado | ES |
| Quora | Respuesta 1 de 4 publicada | EN |
| carlosortet.com | https://carlosortet.com (publicación con 5 links: EN/ES/CA Zoopa + Medium + Substack) | EN |

**Pendientes manuales (el usuario los hace por su mano):**
- Facebook personal (versión nativa long-form preparada — pegar + adjuntar infografía + URL en comentario)
- Facebook page Zoopa / 498A (versión share-del-CEO preparada)
- Quora respuestas 2-4 (cadencia 24-48h entre cada una)

## Lo nuevo que aprendimos en este proyecto

### 1) X / Twitter — automatización de hilos vía Playwright CLI (sin API)

- **NO necesita Twitter API**. Playwright headless con sesión persistente basta para hilos de 19+ tuits.
- **UTF-8 perfecto** con `playwright-cli -s=x type "$TUIT"` (a diferencia de pbcopy + Cmd+V, que corrompe acentos en composer X / LinkedIn / Substack).
- **Mecánica de hilo**: tipear T1 → re-snapshot → grep ref del botón `"Add post"` (cambia cada iteración) → click → tipear T2 → loop. Cerrar con click en `"Post all"`.
- **Señal de éxito**: URL pasa de `/compose/post` → `/home` en 2-3 seg.
- **Pre-flight**: validar TODOS los tuits ≤280 chars antes de empezar. Script Python con `len(t)` + flag `⚠️ EXCEEDS by N`. Si excede: trims rápidos (Semiconductores → Semis, hispanohablante → hispano).
- **Verificación post-publicación**: `playwright-cli -s=x goto /USER/with_replies` + `eval document.querySelectorAll("a[href*=status]")` → ID más bajo = tuit starter del hilo.

→ Guardado en: `~/.claude/skills/content-factory/references/lessons-learned.md` § "X / Twitter · hilo (añadido mayo 2026)"

### 2) X / Twitter — VOZ Y TONO (lo más importante)

El primer hilo que publicamos sonaba demasiado "típico de IA". El usuario detectó las expresiones formulaicas. Lanzamos research deep y consolidamos un **manual de voz X anti-LLM** de 3.250 palabras.

**Anti-patrones detectables como "escrito por IA"** (en orden de obvio a sutil):
1. Em-dashes (—) excesivos
2. "No es X, es Y" / antítesis ("También es, técnicamente, falsa")
3. "La conclusión:", "El cuello no es geopolítico, es técnico" (cierres formulaicos)
4. "Lectura completa con datos verificados y fuentes:" (CTA pomposo)
5. Listas con flechas → (rule-of-three obsesivo)
6. Palabras-marcador: delve into, panorama, ecosistema, robusto, crucial, vibrante
7. Castellano académico (subjuntivos forzados, "cabe destacar que")
8. Longitud uniforme — todos los tuits cerca de 280 chars = firma IA

**Lo que SÍ funciona** (Visakan Veerasamy, Naval, Sahil Bloom):
- Hilos cortos (3-12 unidades de consideración, NO 19)
- Ritmo asimétrico (mezclar tuits de 30 y de 280 chars)
- Castellano oral (contracciones, "o sea", "lo que pasa es que", "venga")
- Opener con dato raro / contradicción / mini-historia (NO "🧵", NO "Thread:")
- Cierre human-first (pregunta abierta concreta, o link sin frase ceremoniosa)

→ Guardado en: `~/.claude/skills/content-factory/references/x-twitter-voice-style.md` (manual completo + checklist 15 items pre-publish)
→ Integrado en SKILL.md `## Estilo específico por canal` como OBLIGATORIO para `x_twitter_ready.txt` y `threads_ready.txt`

### 3) Facebook — pivote de link card a NATIVO long-form

**Insight clave**: FB penaliza posts con links externos (-60/-80% reach). El long-form nativo (250-300 palabras) + imagen propia + URL **en el primer comentario** genera 5-10× más reach orgánico.

- Versión nativa long-form en `output/facebook_personal.md` reescrita.
- Imagen nativa: infografía v2 chip manufacturing (sube como foto, no como link).
- URL del Substack: pegada como primer comentario inmediatamente después de publicar.
- Sin hashtags (FB no los premia).
- Privacidad recomendada: Amigos o Amigos de amigos (no Público — dilución algorítmica).

### 4) WordPress REST API — quirks descubiertos

- **`POST /wp/v2/media` con body raw `image/png`** → 406 Not Acceptable (WAF / ModSecurity bloquea).
- **Fix**: subir via `multipart/form-data` con boundary explícito + headers `Accept: application/json` + `User-Agent: Mozilla/5.0 ...`. Funciona.
- **Bonus**: el plugin de optimización del servidor convierte PNG → JPG automáticamente (manda title como "image/jpeg" en la response). No molesta para nuestro uso.
- **`POST /wp/v2/media/{id}` JSON** → también requiere `Accept: application/json` para evitar 406.
- Insertar imagen en posts existentes: editar `content.raw`, hacer `replace(marker, marker + figure_html, 1)` con marker = `<h2>literal del heading</h2>`, luego POST de update. Mismo patrón para ES/EN/CA con marker traducido al idioma.

### 5) Auto-update de carlosortet.com (regla del skill)

Cuando el autor es Carlos Ortet y publicamos en Substack además del blog y Medium, hay que **AÑADIR la entrada** o **AÑADIR el 5º link** a `~/Documents/03_PERSONAL/carlosortet/src/data/resume.tsx` (objeto `publications[0]`) → `npm run build` → commit + push a `main`. Inmediato deploy en Cloudflare Pages.

→ Regla #8 ya documentada en SKILL.md PASO 1.
→ Hoy se actualizó con el 5º link Substack: commit `11a7a0c`.

## Métricas a vigilar (próximos 7 días)

| Canal | KPI principal | Target |
|-------|---------------|--------|
| WP zoopa.es | Pageviews + tiempo en página + scroll depth | >2.500 PV combinados, >3 min, >70% |
| Substack | Open rate + click-through + new subs | >35%, >10%, +20 |
| Medium | Reads + read ratio + claps | >500, >40%, >100 |
| LinkedIn | Impressions + engagement rate + clicks comment | >5.000, >5%, >100 |
| X | Impressions + likes + bookmarks + replies | >2.000, >50, >100, >10 |
| FB personal | Reach + reactions + comments + link clicks first comment | >300, >20, >10, >30 |

## Próximas iteraciones del skill content-factory

1. **Auto-trim de tuits > 280**: el script Python `validators/run_all.py` debería rechazar `x_twitter_ready.txt` si algún tuit excede 280 chars.
2. **Auto-aplicar voz X**: integrar el checklist de 15 items pre-publish (de `x-twitter-voice-style.md`) como validator que falla si detecta >3 anti-patrones en `x_twitter_ready.txt`.
3. **Auto-generar FB native + URL en comentario**: añadir el template `facebook_personal_native.md` al catálogo del skill como variante por defecto (la versión link-card pasa a ser fallback).
4. **WP media upload helper**: añadir `scripts/publisher/wp_media_upload.py` con multipart form-data + retry-on-406, para no reinventarlo en cada proyecto.
5. **Validator global anti-LLM**: extender `run_all.py` con check de em-dash (`—` `–`), referencias temporales relativas ("esta semana", "este año", "hoy", "recientemente") y frases formulaicas ("también es, técnicamente, falsa", "lectura completa con datos verificados"). Falla el output con lista de offsets.

## Adiciones después del cierre inicial (24 may 2026, tarde)

### Bluesky + Threads reescritos

Tras feedback del autor, el primer borrador de Bluesky+Threads sonaba a IA (em-dashes, "esta semana", "no es X es Y", CTAs ceremoniosos). Reescritos aplicando reglas nuevas en `orthography-rules.md` § 3:

- Bluesky: 5 posts asimétricos (293/160/247/297/177 chars), ritmo no uniforme.
- Threads: 4 posts (493/455/491/292 chars), tono ligeramente más casual.
- Ambos sin em-dash, sin referencias temporales, sin antítesis formulaica.

→ `~/.claude/skills/content-factory/references/orthography-rules.md` § 3 (nuevo, global a todos los canales): prohíbe em-dash, temporales relativos, frases LLM formulaicas, bullets con flechas →.
→ `SKILL.md` actualizado con bullet en "Reglas derivadas" remitiendo a § 3 como obligatorio en PASO 3.6.

### Hacker News listo con research curado

Submission preparado con:
- Title 79 chars: "The invisible fabric of AI: chips aren't a US-China war, but a 30-country chain"
- URL canonical EN (zoopa.es)
- Primer comentario OP con **7 startups europeas de chips IA verificadas 2024-2026**:

  1. **Axelera AI** (NL): $200M+ total, Metis chip en producción H2 2024, €61.6M grant EuroHPC mar 2025 para Titania chiplet, Europa AIPU shipping H1 2026
  2. **SiPearl** (FR): Rhea1 tape-out jul 2025, sampling early 2026, será CPU del Jupiter exascale en Jülich
  3. **OpenChip** (ES Catalonia): €111M EU Next Gen, colaboración con NEC + BSC para RISC-V vector compute accelerator HPC
  4. **Black Semiconductor** (DE): €254.4M raise oct 2024 (€228.7M IPCEI + €25.7M Porsche/Project A), graphene photonics fab en Aachen, volumen 2029
  5. **Codasip** (DE/CZ): seleccionada para DARE project (€240M EU), en venta desde jul 2024 — fork crítico para sovereignty RISC-V
  6. **GreenWaves Technologies** (FR): GAP9 RISC-V edge AI, 150 GOPS @ 0.33mW/GOP, shipping en hearables
  7. **Quintauris** (DE JV): Bosch+Infineon+Nordic+NXP+Qualcomm+ST, RT-Europa launching enero 2026

  Umbrella: DARE (Digital Autonomy with RISC-V in Europe) €240M-380M cubriendo ~12 instituciones.

→ Lección operativa: para HN, el comentario OP debe **añadir información que NO está en el artículo** (no recomendar el artículo) para desactivar el flag de self-promo. Las startups EU funcionan porque son data fresca, verificable, y conectan con el ángulo del paper.

## Referencias

- [[proceso-fabricacion-chips-ia-20260524]] — conocimiento técnico del proceso de fabricación (5 etapas)
- [[playbook-publicacion-zoopa-3-idiomas-20260523]] — Polylang Pro + Rank Math + featured media
- [[guia-linkedin-voz-carlos-ortet-20260510]] — voz personal LinkedIn
- Skill files (no en vault, en `~/.claude/skills/content-factory/`):
  - `references/lessons-learned.md` (+ secciones nuevas: FB personal/page, X / Twitter · hilo)
  - `references/x-twitter-voice-style.md` ⭐ nuevo
  - `references/substack-style.md` (v1.2)
  - `SKILL.md` (tabla "Estilo específico por canal" actualizada)
- Project workspace: `/Users/cop/Documents/claudecode-proj/contentfactory/proyecto-AI-chips-economy-23052026/`
