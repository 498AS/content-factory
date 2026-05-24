# Zoopa Voices · network de profesionales europeos en tech/IA

> Producto interno V1 (spec). Sección curada de profesionales en zoopa.es/voices con 1 página por persona. Backlinks DA60+ cruzados, mentions en LinkedIn Zoopa, GEO co-citation. Diseñado como add-on natural de [[servicio-authority-boost-90-20260524|Authority Boost 90]] y como driver de network effect para la agencia.
>
> Fecha: 2026-05-24
> Owner: Carlos Ortet (curaduría) · Mer Canet (producción) · Junior dev (build)
> Estado: **spec V1 · launch waits for 5-6 voices reales (Carlos + Mer + Daniel + 2-3 clientes AB90)**

---

## 0. Resumen ejecutivo

**Qué es.** Una subsección en zoopa.es (`/voices` o `/network`) que aloja perfiles individuales curados de profesionales europeos en IA, tech, GEO, innovación. Cada profile = 1 página con bio, foto, links a su contenido propio, quote destacable, schema.org Person estructurado.

**Por qué.** Network effect. Cada profile añade valor al directorio entero. Backlinks DA60+ desde zoopa.es a webs personales DA20-40 boost SEO de los profesionales. Zoopa posiciona como "el curator/connector del talento tech EU" sin gastar dinero en paid media.

**Cómo se monetiza.** Inclusión gratuita para clientes Authority Boost 90 (paid). Inclusión gratuita curada para profesionales del network de Carlos (no clientes). NO pago directo por listing — el valor está en la curaduría, no en el ticket.

---

## 1. Por qué tiene sentido ahora

- **Carlos publica con cierta cadencia** (blog Zoopa, Substack, LinkedIn, X, Medium). Cada profile featured genera 1 mention en al menos 1 canal de Zoopa, que es backlink + social proof
- **Authority Boost 90 lanzando V1.5** (Q3 2026): los clientes pueden ser los primeros 2-3 voices
- **GEORadar mide LLM visibility**: tener `zoopa.es/voices/{persona}` como entity reconocida por LLMs eleva la presencia del profesional en queries del nicho
- **Schema.org Person + sameAs** estructurado convierte cada profile en una entity citable por motores generativos
- **Coste marginal cero**: WordPress en zoopa.es ya está + Polylang Pro para multi-idioma + Rank Math para SEO. Templates mczoopa style ya validados

---

## 2. Estructura de cada profile

### Layout `/voices/[slug]`

```
[Hero] Foto profesional centrada + nombre + role en 1 línea
[Bio] 80-120 palabras (no más, no menos)
[Tags] País · sector · role (ej. Spain · Tech founder · AI/GEO)
[Quote] 1 frase destacable extraída de su escritura
[Featured writing] 3-5 artículos suyos (incluido 1 "Zoopa pick")
[Talks & Press] si aplica (3-5 elementos)
[Owned media links] web personal, Substack, Medium, LinkedIn, etc.
[Sameas Schema.org Person] estructurado JSON-LD
[Featured at Zoopa Network desde] fecha
```

### Schema.org Person markup

Cada profile incluye `<script type="application/ld+json">`:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{Nombre completo}",
  "jobTitle": "{Role}",
  "url": "https://{personal-site}",
  "sameAs": [
    "https://twitter.com/{handle}",
    "https://bsky.app/profile/{handle}",
    "https://www.linkedin.com/in/{handle}",
    "https://medium.com/@{handle}",
    "https://{handle}.substack.com",
    "https://github.com/{handle}",
    "https://www.wikidata.org/wiki/Q{number}"
  ],
  "description": "{Bio 80-120 palabras}",
  "memberOf": {
    "@type": "Organization",
    "name": "Zoopa Voices Network",
    "url": "https://zoopa.es/voices"
  }
}
```

### Multi-idioma

- `/es/voices/[slug]` · `/en/voices/[slug]` · `/ca/voices/[slug]` con Polylang Pro
- Profiles con audiencia global por defecto en EN
- Carlos + voices catalanes/españoles también en ES + CA

---

## 3. Modelos posibles de inclusión

| Modelo | Pros | Cons | Decisión |
|---|---|---|---|
| A) Invite-only curado | Exclusividad + prestige | Lento de escalar | — |
| B) Pago €500-1K listing | Revenue directo | Riesgo de spam y dilución | NO |
| C) Free para AB90, paid para externos | Best of both | Híbrido requiere lógica | — |
| **D) Free totalmente, monetización indirecta via AB90** | Network effect rápido, Zoopa = curator | Sin revenue directo | **SÍ V1** |

**V1 decision: Modelo D**. Free para todos los voices invitados. Curaduría = filtro de calidad. Revenue indirecto via conversión a AB90.

---

## 4. Mecánica de promoción cruzada

### Cuando se añade un voice nuevo

1. **Post LinkedIn Zoopa Page** anunciándolo ("Welcome to Zoopa Voices: [name]")
2. **Tweet/post Bluesky** desde @Zoopa o desde Carlos personal mencionando al voice
3. **Newsletter mensual** con 3-4 voices nuevos como "Tech Voices Europe – Edition N"
4. **Notificación a otros voices** sugiriendo retweet/share
5. **El voice nuevo recibe** package con: link a su page, 3-4 piezas pre-aprobadas para compartir, badge "Zoopa Voice" SVG para su web

### Backlinks recíprocos (implementación semi-automatizada)

- Cada voice añade "Featured at Zoopa Voices" link en su web personal
- Script semi-automático verifica el backlink mensualmente
- Si el voice deja de tener el backlink, sale de "Active voices" (queda en archive)

---

## 5. Cómo enchufa con karma-boost plan Carlos

| Etapa | Cuándo | Acción |
|---|---|---|
| 1 | Sem 1-2 (25-31 may, 1-7 jun) | Carlos es el **primer profile** (eat-your-own-dog-food) |
| 2 | Sem 3-4 (8-21 jun) | Invitamos **5 voices fundadores**: Mer Canet, Daniel Ebo, 2-3 partners EU tech conocidos por Carlos, 1 académico/periodista |
| 3 | Mes 2-3 (jul-ago) | Cada profile genera 1 mention de Zoopa en su web/LinkedIn → backlinks recíprocos |
| 4 | Mes 3+ (sep+) | Producto = "Become a Zoopa Voice" listing como CTA en cualquier presentación AB90 |

---

## 6. Cómo enchufa con Authority Boost 90

Add-on natural incluido en tiers Personal y Empresa de AB90:

| Tier AB90 | Inclusión Zoopa Voices |
|---|---|
| Quick Audit | NO (no incluido, sample) |
| Starter | Mención en monthly digest (no profile propio) |
| **Personal** | **Profile completo + featured 1x en LinkedIn Zoopa** |
| **Empresa** | **Profile completo + featured 1x LinkedIn + 1 quote en newsletter Zoopa** |
| Sostenido | Mantiene profile + actualización trimestral |

Esto añade ~3h de trabajo interno por cliente Personal (sin alterar el margen 75%).

---

## 7. Launch criteria · cuándo lanzamos V1 público

**NO lanzar antes de tener 5-6 voices reales activos**. Razón: un directorio con 1-2 voices se ve abandonado/spam. Necesitamos masa crítica visual para credibilidad.

Composición mínima para V1 launch:

| Voice | Status | Cuándo |
|---|---|---|
| Carlos Ortet | confirmado (siempre) | sem 1 |
| Mer Canet | confirmado (interna Zoopa) | sem 1-2 |
| Daniel Ebo | confirmado (interna Zoopa) | sem 1-2 |
| Cliente AB90 #1 (V1.5 founder) | pendiente outreach | Q3 2026 |
| Cliente AB90 #2 (V1.5 founder) | pendiente outreach | Q3 2026 |
| Cliente AB90 #3 ó voice invitado | pendiente outreach | Q3 2026 |

Hasta tener los 3 clientes AB90 confirmados, V1 se mantiene **en staging interno** (zoopa.es/voices accesible pero noindex + no enlazado desde menu).

---

## 8. Stack técnico V1

| Componente | Implementación |
|---|---|
| **CMS** | WordPress en zoopa.es con Custom Post Type "Voice" |
| **Template** | mczoopa style (consistencia con resto de Zoopa) |
| **Multi-idioma** | Polylang Pro (ya configurado) |
| **SEO** | Rank Math (ya activo) |
| **Schema.org** | Plugin Yoast Schema o custom code |
| **Sitemap** | Auto-generado vía Rank Math, incluir `/voices/*` |
| **llms.txt** | Añadir `Voices: https://zoopa.es/voices/sitemap.xml` |
| **Backlinks check** | Script Python mensual (semi-auto) |
| **Newsletter** | Substack (ya activo, cuenta carlosortet.substack.com) o Mailchimp |

### Esfuerzo dev V1

| Tarea | Horas | Owner |
|---|---|---|
| Custom Post Type "Voice" + ACF fields | 4h | Junior dev |
| Template profile (HTML + CSS mczoopa style) | 6h | Junior dev + Mer review |
| Multi-idioma setup | 2h | Junior dev |
| Schema.org Person JSON-LD generator | 3h | Junior dev |
| llms.txt + sitemap update | 1h | Junior dev |
| Index page `/voices` con grid de voices | 4h | Junior dev + Mer |
| Newsletter template "Tech Voices Europe" | 3h | Mer |
| Curación inicial 6 voices (bio + foto + links + quote) | 12h | Carlos + Mer |
| **Total V1 launch** | **35h** | distribuido |

Coste interno V1: 35h × €30 blended (incluye más junior dev hours) = **~€1.050**. Asumido como inversión, no facturable.

---

## 9. KPIs Zoopa Voices

### Métricas a 6 meses post-launch

| Métrica | Target |
|---|---|
| Voices activos | 12-15 |
| Backlinks salientes (Zoopa → voices) | 12-15 |
| Backlinks recíprocos verificados | 8-12 |
| Domain Authority increase voices promedio | +5-10 |
| Conversiones a AB90 atribuibles a Voices | 2-3 clientes |
| LLM citations "Zoopa Voices" en queries del nicho | 5-10/mes (medido vía GEORadar) |
| Newsletter "Tech Voices Europe" subscribers | 200-400 |

### Métricas a 12 meses

| Métrica | Target |
|---|---|
| Voices activos | 25-35 |
| Authority Boost 90 clientes acumulados | 8-12 |
| Network effect mentions Zoopa monthly | 15-25 |
| Zoopa Voices reconocido en sectoriales tech (mention en TechCrunch ES, etc.) | 1-2 mentions |

---

## 10. Anti-patrones a evitar

- **NO incluir voices que no son activos publicando** (profile abandonado quema la credibilidad del directorio)
- **NO aceptar self-nominations sin filtro** (curaduría es el moat)
- **NO permitir voices que solo prom autocontenido** (debe haber 70% contenido editorial vs 30% promocional máximo)
- **NO cobrar por listing** (revenue directo destruye la network value)
- **NO lanzar sin 5-6 voices iniciales** (parece muerto)

---

## 11. Roadmap V1 → V3

| Versión | Cuándo | Hito |
|---|---|---|
| **Spec V1 (este doc)** | 24 may 2026 | Definición producto + criterios launch |
| **Pre-launch interno** | jun-jul 2026 | Carlos + Mer + Daniel listed (staging, noindex) |
| **V1 public launch** | Q3 2026 | 5-6 voices live + announcement post + newsletter ed.1 |
| **V1.5** | Q4 2026 | 12-15 voices · primer GEORadar "Voices" report |
| **V2** | 2027 H1 | 25+ voices · API / Wikidata claim · Newsletter establecida |
| **V3** | 2027 H2 | Voices Awards anual · Eventos físicos sectoriales |

---

## 12. Próximos pasos inmediatos (2 semanas)

| Sem | Acción | Owner |
|---|---|---|
| 1 (25-31 may) | Carlos prepara su profile draft (bio + quote + photo + featured writing) | Carlos |
| 1 | Mer y Daniel preparan sus profiles | Mer, Daniel |
| 2 (1-7 jun) | Junior dev empieza Custom Post Type + template en staging | Junior dev |
| 2 | Mer prepara newsletter template "Tech Voices Europe Edition 1" | Mer |

**No publicar `/voices` en menú principal hasta tener 5-6 voices** (criterio launch).

---

## Referencias

- [[servicio-authority-boost-90-20260524|Authority Boost 90 — servicio madre]]
- [[karma-boost-carlos-ortet-20260524|Plan personal Carlos · case study V1]]
- [[../07_CONTENT_FACTORY/MOC Content Factory|MOC Content Factory]]
- [[../02_GEO_GENERAL/MOC GEO General|MOC GEO General]]
- Skill interno: `~/.claude/skills/content-factory/` (LEO)

---

*Spec creada el 24 may 2026 tras incidente HN dang + revisión pricing AB90. Launch pendiente de 2-3 clientes AB90 V1.5 confirmados.*
