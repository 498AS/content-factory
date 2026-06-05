<!--
SEO METADATA (no publicar com a contingut visible; abocar als camps de Rank Math)
Title: La trampa dels tokens: dependre d'un sol proveïdor d'IA és un risc financer | Zoopa
Meta description: El preu per token s'enfonsa i la factura puja igual. Dependre d'un sol model d'un sol proveïdor signa tres xecs en blanc. La resposta és l'estratègia multimodel.
Slug: trampa-tokens-risc-proveidor-unic-estrategia-multimodel
Focus keyword: estratègia multimodel
Secondary keywords: trampa dels tokens, lock-in d'IA, risc de proveïdor únic, model routing, IA sobirana, cost d'inferència
Canonical: https://zoopa.es/ca/innovacio-tecnologia/trampa-tokens-risc-proveidor-unic-estrategia-multimodel/
Category: Innovació i Tecnologia (CA equivalent), GEO, IA i Visibilitat
Tags: estratègia multimodel, lock-in, tokens, model routing, IA sobirana, cost d'inferència, LLM, resiliència
-->

# La trampa dels tokens: dependre d'un sol proveïdor d'IA és un risc financer

<figure style="margin: 24px 0 40px 0;">
  <img src="https://zoopa.es/wp-content/uploads/2026/06/trampa-tokens-estrategia-multimodelo-placeholder.jpg" alt="Il·lustració de la trampa dels tokens: el preu per token cau mentre la factura total puja, i una arquitectura multimodel encamina cada tasca al model adequat amb fallback entre proveïdors" style="width: 100%; height: auto; border-radius: 4px; display: block;" />
  <figcaption style="font-size: 0.9em; color: #64748b; text-align: center; margin-top: 12px; font-style: italic;">El preu per token s'enfonsa i la factura puja alhora. La defensa estructural no és negociar el preu, és no dependre d'un sol proveïdor.</figcaption>
</figure>
<!-- IMATGE: substituir el src placeholder per la featured image real abans de publicar, o assignar featured_media per API. -->

Cada pocs mesos algú proclama que la IA és cada cop més barata i que el cost ha deixat de ser un problema. Té raó, per token. I cada pocs mesos la teva factura d'inferència torna a pujar. També és cert. Les dues coses passen alhora i no es cancel·len. Aquesta és la trampa dels tokens.

Anem amb la conclusió abans que amb el preàmbul: la trampa és real, però és asimètrica. El preu per unitat de capacitat cau a un ritme històric, i tot i així el cost d'operar puja, perquè cada millora dels models crema molts més tokens. I mentrestant, qui construeix el seu producte sobre un únic model d'un únic proveïdor acumula un risc que no apareix a cap factura: el que aquest proveïdor decideixi per tu el preu, la continuïtat i el consum. La resposta estructural, ja avalada per Gartner i operativa en producció, és l'arquitectura multimodel. La resta d'aquest article explica per què, i què fer.

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin: 48px 0; padding: 32px; background: linear-gradient(135deg, #0d9488 0%, #1a365d 100%); border-radius: 6px; color: #fff;">
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">150x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">va caure el preu per token entre GPT-4 i GPT-4o, segons Altman</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">3x a 18x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">puja a l'any el cost absolut d'operar models en frontera</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">85%</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">d'estalvi encaminant entre models, retenint el 95% del rendiment</div>
  </div>
</div>
<p style="font-size: 0.85em; color: #64748b; text-align: center; margin: -32px 0 40px 0;">Fonts: Sam Altman, "Three Observations" · The Price of Progress (MIT/Epoch, arXiv 2511.23455) · RouteLLM (LMSYS / UC Berkeley)</p>

<div style="background: linear-gradient(135deg, #ebf8ff 0%, #f0fff4 100%); border-left: 4px solid #0d9488; border-radius: 0 8px 8px 0; padding: 24px 28px; margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h3 style="margin: 0 0 16px 0; font-size: 1.1em; font-weight: 700; color: #1a365d; letter-spacing: 0.01em;">El que necessites saber</h3>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: #2d3748;">
    <li style="margin-bottom: 8px;"><strong>El preu cau, però la teva factura puja.</strong> El preu per capacitat equivalent baixa entre 5x i 10x a l'any. Alhora, el cost d'operar en frontera puja entre 3x i 18x a l'any, perquè els models de raonament i els agents cremen molts més tokens.</li>
    <li style="margin-bottom: 8px;"><strong>El lock-in ha deixat de ser teoria.</strong> El gener de 2026 OpenAI va retirar GPT-4o i altres models de ChatGPT per decisió unilateral. El proveïdor controla el cicle de vida del model del qual depens.</li>
    <li style="margin-bottom: 8px;"><strong>El preu d'avui pot estar subvencionat.</strong> Sequoia va xifrar en 600.000 milions de dòlars el forat entre la inversió en IA i els ingressos que la justifiquen. Si el preu actual no és rendible per al proveïdor, el teu marge de demà depèn de decisions alienes.</li>
    <li style="margin-bottom: 8px;"><strong>La mètrica correcta no és el preu per token.</strong> És la relació entre la qualitat de l'output i el seu cost. Mesurar la productivitat per tokens consumits només convé a qui ven tokens.</li>
    <li style="margin-bottom: 8px;"><strong>La defensa és arquitectura, no negociació.</strong> Encaminar cada tasca al model adequat, amb fallback entre proveïdors i opció sobirana, dona resiliència i eficiència en una sola decisió de disseny.</li>
  </ul>
</div>

## Les dues veritats que conviuen

La conversa de mercat es va quedar amb el titular fàcil: "la IA és cada cop més barata". És cert per token i enganyós per negoci. Per entendre la trampa cal sostenir dos fets alhora.

**Per unitat, la IA s'abarateix a un ritme sense precedents.** El preu per assolir un nivell de rendiment determinat cau entre 5x i 10x a l'any, segons el paper de referència *The Price of Progress* (MIT i Epoch AI). Les dades primàries d'Epoch ho afinen: la mediana és de 50x a l'any, i filtrant només el posterior al gener de 2024 puja a 200x. Tres veus de màxima autoritat convergeixen en la mateixa xifra rodona. Guido Appenzeller (a16z) ho va batejar com a "LLMflation" i resumeix: "el cost de la inferència ha caigut un factor de 1.000 en tres anys". Sam Altman ho xifra en un 10x cada dotze mesos, amb un 150x concret entre GPT-4 i GPT-4o. Ethan Mollick (Wharton): "quan va sortir GPT-4 costava uns 50 dòlars treballar amb un milió de tokens; ara costa uns 14 cèntims".

**I tot i així el cost per tasca puja.** Aquí hi ha la trampa, i el mateix paper la nomena sense embuts: el cost absolut d'operar models en frontera puja entre 3x i 18x a l'any, perquè cada millora marginal de rendiment exigeix substancialment més inferència. El mecanisme té nom: consum de tokens. Un model agèntic gasta entre 5 i 30 vegades més tokens per tasca que un chatbot estàndard, segons Gartner. En codi agèntic, Microsoft Research mesura fins a 1.000 vegades més tokens que un xat de codi. I el consum és estocàstic: la mateixa tasca executada dues vegades pot diferir fins a 30x en tokens totals. Més tokens no vol dir més precisió.

Gartner ho resumeix sense pietat: cap al 2030 la inferència costarà als proveïdors més d'un 90% menys que el 2025, però aquest estalvi no arribarà al client, perquè el consum creix més de pressa del que cau el preu.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  El preu per token continuarà caient i serà una distracció. La variable que decideix el teu marge cap al 2030 és el consum, no el preu unitari.
</blockquote>

## El lock-in ha deixat de ser teoria

Fins aquí, tot és qüestió de cost. La part que gairebé ningú pressuposta és la de control. Qui construeix un producte, un servei o un flux de treball sobre un únic model d'un únic proveïdor signa tres xecs en blanc alhora.

1. **Xec de preu.** Acceptes el pricing que el proveïdor fixi demà.
2. **Xec de continuïtat.** Acceptes que el model continuï existint.
3. **Xec de consum.** Acceptes que cada millora de capacitat multipliqui els tokens que pagues.

El xec de continuïtat ja té víctimes. El 29 de gener de 2026 OpenAI va anunciar la retirada de GPT-4o, GPT-4.1, GPT-4.1 mini i o4-mini de ChatGPT, efectiva dues setmanes després. La justificació oficial: només el 0,1% d'usuaris continuava triant GPT-4o cada dia després de la migració a GPT-5.2. El moviment #keep4o va reunir 21.000 signatures. No va canviar res.

La lliçó no és sobre GPT-4o. És sobre qui decideix. El proveïdor poda els models de baix ús encara que una minoria en depengui en producció. Si el teu prompt engineering, les teves avaluacions i el teu producte estan calibrats sobre un model concret, la seva retirada és el teu problema, no el seu. Convé un matís honest: aquesta retirada va aplicar a la interfície de ChatGPT, no a l'API, que "no canvia de moment". Però el patró de migració forçada és el que importa.

Andrej Karpathy va posar nom al risc de fons. Quan els grans models cauen, diu, és "com una apagada d'intel·ligència al món: el planeta es torna més ximple com més depenem d'aquests models". El seu marc és precís: els LLM "tenen ara propietats de serveis públics", com l'electricitat o l'aigua. Dependre d'una sola utility, sense alternativa, és el risc.

## Depens d'una economia que encara perd diners

Hi ha un segon cost, més especulatiu però igual de rellevant per al teu pressupost: depens d'un mercat els comptes del qual encara no quadren. David Cahn, de Sequoia Capital, va plantejar el 2024 el càlcul més citat del sector i el va titular "la pregunta dels 600.000 milions": el forat entre el que s'ha invertit en infraestructura d'IA i els ingressos que ho haurien de justificar. Cahn no és cap agorer, ho diu amb calma: "les febres especulatives són part de la tecnologia; qui mantingui el cap fred tindrà l'oportunitat de construir empreses importants".

L'evidència verificada confirma la caiguda de preus i les deprecacions de models. No confirma les economies internes dels laboratoris, però els senyals contextuals apunten en una direcció incòmoda: un usuari de pagament a 200 dòlars al mes pot arribar a consumir tokens per valor de 5.000, i als inversors dels grans labs se'ls demana "aguantar uns anys més". La pregunta de negoci és la mateixa en l'escenari optimista (els models es commoditzen i el preu baixa) i en el pessimista (consolidació i pujada de preus): si el preu actual està subvencionat per capital de risc, què li passa al teu marge quan els labs hagin de ser rendibles?

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  Construir sobre un sol model d'un sol proveïdor és signar tres xecs en blanc alhora: el de preu, el de continuïtat i el de consum.
</blockquote>

## La resposta: estratègia multimodel

La bona notícia és que la defensa no és esperar que el mercat s'estabilitzi ni renegociar tarifes. És una decisió d'arquitectura, i ja està validada per l'analista de referència. Gartner, el març de 2026, ho diu sense ambigüitat: "el valor s'acumularà a les plataformes capaces d'orquestrar càrregues a través d'un portafoli divers de models. Les tasques rutinàries d'alta freqüència s'han d'encaminar a models petits i de domini específic. La inferència cara dels models frontera ha d'estar fortament restringida i reservada per al raonament complex d'alt marge".

Això és exactament l'enfocament que apliquem a Zoopa: agents que distribueixen les tasques entre models, triant l'adequat per cost i capacitat, amb fallbacks entre proveïdors. I l'estalvi està quantificat. RouteLLM, de LMSYS i UC Berkeley, encamina entre un model fort i un de feble segons la complexitat del prompt: estalvia més del 85% al benchmark MT Bench retenint el 95% del rendiment de GPT-4. A MMLU l'estalvi és del 45% i a GSM8K del 35%. El 85% és el cas més favorable, no la mitjana, però fins i tot el terra d'aquest rang canvia l'economia d'operar IA a escala.

No cal construir l'encaminament des de zero. Les eines de producció ja existeixen: l'Auto Router d'OpenRouter selecciona el model d'un pool curat segons la complexitat, amb un paràmetre explícit de tradeoff cost-qualitat; LiteLLM, open source i self-hostable, és un gateway a més de 100 APIs amb fallback automàtic en cadena ordenada entre proveïdors; i el mateix RouteLLM és codi obert.

### L'arquitectura sostenible, en quatre capes

1. **Classificació de la tasca.** Cada petició s'etiqueta per complexitat abans de tocar un model.
2. **Encaminament per cost i capacitat.** Les tasques trivials van a models petits; el raonament complex, a frontera, i restringit.
3. **Fallback multiproveïdor.** Una cadena ordenada entre laboratoris diferents. Si un cau, puja de preu o deprecia un model, el sistema no se n'assabenta.
4. **Opció sobirana o open-weight.** Per a dada sensible o per desacoblar-se del pagament per token, models self-hosted dins de la cadena.

Això és resiliència (no depens d'un proveïdor) més eficiència (no pagues frontera per tasques trivials) en una sola decisió de disseny.

## El que veiem des de la trinxera

> Aquesta secció està pendent de casos reals amb client anomenat. Sense ells, aquest bloc és divulgació. Amb ells, és posicionament. Omplir abans de publicar (vegeu el bloc 3 del source).

[EXEMPLE 1: història real d'un projecte recent]
Client: <client o branded content intern, anonimitzat si hi ha NDA>
Tensió: <quin problema de dependència, cost o continuïtat va aparèixer>
Decisió: <què es va fer: routing per nivells, fallback entre proveïdors, opció open-weight, sostre de consum>
Lliçó: <quina regla se'n va treure>

[EXEMPLE 2: història real d'un projecte recent]
Client: <client o anonimitzat si hi ha NDA>
Tensió: <quin problema va aparèixer>
Decisió: <què es va fer>
Lliçó: <quina regla se'n va treure>

El que sí que podem avançar com a patró: en els projectes que toquem, el risc gairebé mai es percep fins que el proveïdor canvia alguna cosa. Puja un preu, deprecia un model o ajusta una quota, i de cop un sistema que funcionava passa a dependre d'una decisió que no va prendre ningú de l'equip. L'arquitectura multimodel no és una optimització tècnica, és la diferència entre assabentar-te d'aquest canvi o no assabentar-te'n.

<div style="background: #1a1a1a; color: #fff; padding: 32px; margin: 40px 0; border-radius: 4px; text-align: center;">
  <p style="margin: 0 0 12px 0; font-size: 0.9em; opacity: 0.8; text-transform: uppercase; letter-spacing: 1px;">Estratègia d'IA amb cap</p>
  <p style="margin: 0 0 20px 0; font-size: 1.3em; line-height: 1.4;">Això és el que fem. Dissenyem sistemes d'IA que encaminen cada tasca al model adequat i no depenen d'un sol proveïdor.</p>
  <a href="https://zoopa.es/ca/serveis/estrategia/" style="display: inline-block; background: #fff; color: #1a1a1a; padding: 12px 28px; text-decoration: none; font-weight: 600; border-radius: 2px;">Això és el nostre →</a>
</div>

## Quan dependre d'un sol proveïdor suma i quan resta

Res d'això és un al·legat contra els grans laboratoris ni contra els models frontera. Són tecnologia extraordinària, i per a molts arrencaments apostar per un sol proveïdor és la decisió correcta. La diferència entre sumar o restar no és el proveïdor, és el context.

Un sol proveïdor suma quan estàs validant una idea, el volum és baix, no manegues dada regulada i la velocitat d'arribar al mercat pesa més que el marge. En aquesta fase, muntar encaminament i fallback és complexitat prematura. Resta quan el sistema entra en producció a escala, quan el cost d'inferència comença a notar-se al compte de resultats, quan manegues dades subjectes al RGPD o a normativa sectorial, o quan aquell model s'ha tornat una peça estructural del teu producte. Allà, la dependència deixa de ser una comoditat i passa a ser una exposició. La regla pràctica: recolzar-te en un proveïdor mentre és opcional, dissenyar la sortida abans que sigui obligatòria.

## IA sobirana: la independència com a cobertura de risc

La quarta capa de l'arquitectura, l'opció sobirana, mereix un apunt a part, perquè Europa ja ha decidit que la dependència de proveïdors estatunidencs és un risc d'Estat, no només d'empresa. Mistral va tancar el setembre de 2025 una Sèrie C de 1.700 milions d'euros amb valoració d'11.700 milions, liderada per ASML, i construeix els seus propis centres de dades per deixar de dependre del núvol estatunidenc. DeepSeek va demostrar per la via del cost que l'estat de l'art no exigeix CapEx massiu ni models tancats: el llançament del seu model R1 va esborrar 600.000 milions de dòlars de la capitalització de NVIDIA en un sol dia, la caiguda diària més gran d'una empresa en la història dels Estats Units. Tots dos publiquen models open-weight, executables en infraestructura pròpia.

Per a una empresa, la sobirania es tradueix en una decisió concreta: el self-hosting. La seva economia depèn del volum (el punt d'equilibri davant d'una API premium ronda els 256 milions de tokens al mes, amb la utilització de la GPU com a variable crítica), però hi ha un cas en què el càlcul de cost deixa d'importar. Per a càrregues amb dades subjectes a HIPAA, RGPD o SOC2, sense un acord de tractament de dades les APIs de consum no poden processar legalment aquesta informació. Allà el self-hosting deixa de ser una decisió de cost i passa a ser de jurisdicció. Amb el Reglament Europeu d'IA plenament aplicable des del 2 d'agost de 2026, aquesta frontera deixarà de ser teòrica per a molts sectors.

## Què fer si construeixes o ja operes amb IA

La trampa dels tokens no es desactiva negociant el preu. Es desactiva amb governança i disseny. Aquestes són les palanques que de debò mouen el risc i la factura.

1. **Mesura la qualitat per cost, no el consum.** L'objectiu és el mínim de tokens per a la màxima qualitat de sortida, no el màxim de tokens per aparentar productivitat. Premiar "tokens cremats" subvenciona la feina inútil.
2. **Classifica cada tasca abans de triar model.** No enviïs una classificació trivial al model més gran. Entre un flagship i un model petit hi ha un ordre de magnitud de diferència de preu.
3. **Munta fallback entre proveïdors des del dia u.** Una cadena ordenada entre labs diferents converteix la caiguda, la pujada de preu o la deprecació d'un proveïdor en un no-esdeveniment.
4. **Reserva una opció open-weight per a la dada sensible.** Tant per compliment com per desacoblar-te del pagament per token a les càrregues que ho justifiquin.
5. **Pressuposta sobre el percentil alt.** Com que el consum és estocàstic, pren diverses execucions de cada tasca representativa i pressuposta sobre el cas dolent, no sobre la mitjana. Fixa sostres de tokens per resposta i talls de bucle als agents.
6. **Aprofita el prompt caching.** Reutilitzar la part estable d'un prompt baixa el cost d'input fins a un 90% en alguns proveïdors. És de les optimitzacions de més retorn amb prompts llargs i repetits.

## Llavors, quina és la sortida?

Tornem al principi. Per token, la IA és cada cop més barata, i ho continuarà sent. En agregat, la teva factura puja, i ho continuarà fent mentre el consum creixi més de pressa que el preu. Però el cost no és el risc més gran. El risc més gran és no tenir alternativa: dependre d'un model que un altre pot encarir, retirar o saturar sense comptar amb tu. L'estratègia multimodel resol les dues coses amb la mateixa decisió, perquè converteix cada proveïdor en intercanviable. Dissenyar-la ara, mentre és opcional, costa una fracció del que costarà improvisar-la quan el marge ja estigui compromès.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  La sostenibilitat de l'estratègia de models és avantatge competitiu ara. Després és supervivència.
</blockquote>

<div style="background: #000; color: #fff; padding: 36px; margin: 48px 0; border-radius: 4px;">
  <h2 style="margin: 0 0 12px 0; color: #fff; font-size: 1.4em;">Parlem-ne</h2>
  <p style="margin: 0 0 24px 0; opacity: 0.8; line-height: 1.6;">Si el teu producte o la teva operació depenen avui d'un sol model d'un sol proveïdor, convé tenir aquesta conversa abans que el proveïdor decideixi per tu, no després. T'expliquem com dissenyem arquitectures multimodel a Zoopa i 498A.</p>
  <a href="https://zoopa.es/ca/contacta/" style="display: inline-block; background: #fff; color: #000; padding: 14px 32px; text-decoration: none; font-weight: 600;">Parlem-ne →</a>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Glossari</h2>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Token</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Unitat mínima de text que un model processa i factura. No és una paraula ni una lletra, sinó un fragment. Com que el model prediu i cobra token a token, el token és la moneda real de l'economia dels LLM. El català i el castellà consumeixen més tokens per idea que l'anglès, perquè els tokenitzadors es van entrenar sobretot amb anglès.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Inferència</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Cada ús d'un model ja entrenat. L'entrenament és el cost de capital del proveïdor; la inferència és el cost recurrent que paga el client. Tota la trampa dels tokens viu a la inferència.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Tokens de raonament (reasoning tokens)</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Tokens que un model de raonament genera "pensant en veu alta" abans de la resposta final. Solen ocupar milers per consulta, l'usuari no els veu però sí que els paga, i es facturen com a sortida, la partida cara. Són la causa que el raonament dispari la factura.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Sistema agèntic</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Patró en què el model no només respon, sinó que planifica i executa tasques de diversos passos en bucle, fent servir eines. Cada pas reinjecta el context acumulat com a input, així que el consum creix de manera no lineal i invisible. És el major amplificador de despesa de tokens.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Model routing (encaminament de models)</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Sistema que, davant de cada petició, decideix automàticament quin model convé: les simples a un model petit i barat, les complexes a un de gran. Optimitza cost i qualitat sense que l'usuari triï. Una de les defenses més efectives contra la trampa.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Fallback</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Mecanisme de respatller: si el model o proveïdor principal falla, puja de preu o deprecia un model, el sistema reintenta automàticament amb una alternativa. Aporta resiliència davant de la dependència d'un únic proveïdor.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Open-weight</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Model els pesos del qual es publiquen i es poden descarregar i executar en infraestructura pròpia, encara que no necessàriament amb dades o llicència plenament lliures. Només els models open-weight o open-source permeten escapar del cost per token allotjant el model pel teu compte.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Sobirania d'IA</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Capacitat d'una organització o país de controlar la seva pròpia infraestructura d'IA (models, còmput, dades) sense dependre críticament de tercers estrangers. És el principal argument no econòmic per al self-hosting i els models open-weight.</p>
  </div>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Preguntes freqüents</h2>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Què és la trampa dels tokens?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">És la paradoxa que el preu per token cau any rere any mentre la factura total d'IA de moltes empreses puja. Passa perquè els models de raonament i els agents consumeixen molts més tokens per tasca, així que el consum creix més de pressa del que baixa el preu unitari.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Per què és un risc dependre d'un sol proveïdor d'IA?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Perquè el proveïdor controla el cicle de vida del model: pot pujar el preu, retirar el model o canviar les quotes sense comptar amb tu. El gener de 2026 OpenAI va retirar GPT-4o de ChatGPT malgrat una petició amb 21.000 signatures. Si el teu producte està calibrat sobre un model concret, la seva retirada és el teu problema.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Què és una estratègia multimodel?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">És una arquitectura que encamina cada tasca al model més adequat per cost i capacitat, amb fallback automàtic entre proveïdors i una opció de model sobirà o open-weight per a la dada sensible. Dona resiliència davant de la dependència i eficiència davant del sobrecost en una sola decisió de disseny. Gartner l'avala com l'enfocament on s'acumularà el valor.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Quant s'estalvia encaminant entre models?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">RouteLLM, de LMSYS i UC Berkeley, documenta fins a un 85% d'estalvi retenint el 95% del rendiment de GPT-4 al seu benchmark més favorable. En altres benchmarks l'estalvi és del 45% i del 35%. La xifra exacta depèn molt de la tasca, però fins i tot el terra del rang canvia l'economia d'operar IA a escala.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Quan compensa el self-hosting d'un model open-weight?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Per cost, a partir d'un volum alt (el punt d'equilibri davant d'una API premium ronda els 256 milions de tokens al mes, amb la utilització de la GPU com a factor crític). Però per a dades subjectes al RGPD, HIPAA o SOC2 sense acord de tractament, el self-hosting pot ser l'única via conforme, i llavors la decisió deixa de ser de cost i passa a ser de jurisdicció.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Cal construir l'encaminament des de zero?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">No. Les eines de producció ja existeixen: l'Auto Router d'OpenRouter selecciona el model d'un pool curat segons la complexitat, i LiteLLM (open source i self-hostable) és un gateway a més de 100 APIs amb fallback automàtic en cadena entre proveïdors. El mateix RouteLLM també és codi obert.</p>
  </div>
</div>
