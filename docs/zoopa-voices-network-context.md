# Zoopa Voices · network de profesionales (context note)

> Add-on natural de Authority Boost 90. Subsección curada `zoopa.es/voices` con profiles individuales de profesionales europeos en tech/IA. Backlinks DA60+ cruzados, mentions en LinkedIn Zoopa, GEO co-citation. Spec V1 completa en vault.

## En una frase

Zoopa Voices = un directorio curado en zoopa.es donde cada profesional tech EU tiene 1 página con bio + links + quote + Schema.org Person, intercambiándose backlinks con la web personal del profesional y obteniendo mentions cruzadas en LinkedIn/Substack Zoopa.

## Por qué importa para content-factory skill

- Cuando un cliente AB90 entra al programa, se le ofrece **inclusión gratuita** en Zoopa Voices como add-on
- Cada profile genera **1 mention en LinkedIn Zoopa** (post de bienvenida) + **1 quote en newsletter mensual** "Tech Voices Europe"
- Estos mentions son outputs que el skill content-factory **debe generar** cuando se añade un voice nuevo
- Templates para "Welcome to Zoopa Voices" post + newsletter edition serán parte del catálogo de canales

## Templates futuros (cuando V1 launch)

| Output | Cuándo se genera | Canal |
|---|---|---|
| `zoopa_voices_welcome_post_{voice}.md` | Cada nuevo voice | LinkedIn Zoopa Page |
| `zoopa_voices_newsletter_ed_{N}.md` | 1x al mes | Substack Zoopa o Mailchimp |
| `zoopa_voices_profile_html_{voice}.md` | Cada nuevo voice | Página WP zoopa.es/voices/[slug] |
| `zoopa_voices_voice_invite_email_{voice}.md` | Outreach a candidato | Email |

Estos NO existen aún. Se añadirán al `references/channel-catalog.md` cuando se inicie la build V1.

## Inclusión en Authority Boost 90

Niveles de inclusión por tier:

| Tier AB90 | Inclusión Zoopa Voices |
|---|---|
| Quick Audit | NO incluido |
| Starter | Mención en monthly digest (no profile propio) |
| **Personal** | Profile completo + featured 1x en LinkedIn Zoopa |
| **Empresa** | Profile completo + featured 1x LinkedIn + quote en newsletter |
| Sostenido | Mantiene profile + actualización trimestral |

## Launch criteria

V1 NO se lanza públicamente hasta tener **5-6 voices reales activos**:
- Carlos Ortet (siempre)
- Mer Canet (interna Zoopa)
- Daniel Ebo (interna Zoopa)
- 2-3 clientes AB90 V1.5 confirmados

Hasta entonces: `/voices` en staging interno con noindex.

## Referencias

- Spec completa: vault `02_GEO_GENERAL/proyecto-zoopa-voices-network-20260524.md`
- Servicio madre: vault `02_GEO_GENERAL/servicio-authority-boost-90-20260524.md`
- Pricing context: `docs/pricing-economics-ab90.md`
