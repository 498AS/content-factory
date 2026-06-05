<!--
SEO METADATA (do not publish as visible content; load into Rank Math fields)
Title: The token trap: relying on a single AI provider is a financial risk | Zoopa
Meta description: The price per token collapses and your bill rises anyway. Building on one model from one provider signs three blank cheques. The answer is a multi-model strategy.
Slug: token-trap-single-ai-provider-financial-risk-multimodel-strategy
Focus keyword: multi-model strategy
Secondary keywords: token trap, AI vendor lock-in, single provider risk, model routing, sovereign AI, inference cost
Canonical: https://zoopa.es/en/innovation-technology/token-trap-single-ai-provider-financial-risk-multimodel-strategy/
Category: Innovación y Tecnología (EN equivalent), GEO / AI Visibility
Tags: multi-model strategy, lock-in, tokens, model routing, sovereign AI, inference cost, LLM, resilience
-->

# The token trap: relying on a single AI provider is a financial risk

<figure style="margin: 24px 0 40px 0;">
  <img src="https://zoopa.es/wp-content/uploads/2026/06/trampa-tokens-estrategia-multimodelo-placeholder.jpg" alt="Illustration of the token trap: the price per token falls while the total bill rises, and a multi-model architecture routes each task to the right model with provider fallback" style="width: 100%; height: auto; border-radius: 4px; display: block;" />
  <figcaption style="font-size: 0.9em; color: #64748b; text-align: center; margin-top: 12px; font-style: italic;">The price per token collapses and the bill rises at the same time. The structural defence is not negotiating price, it is not depending on a single provider.</figcaption>
</figure>
<!-- IMAGE: replace the placeholder src with the real featured image before publishing, or set featured_media via API. -->

Every few months someone declares that AI keeps getting cheaper and that cost has stopped being a problem. They are right, per token. And every few months your inference bill goes up again. That is also true. Both things happen at once and they do not cancel out. That is the token trap.

Here is the conclusion before the detour: the trap is real, but it is asymmetric. The price per unit of capability is falling at a historic pace, and yet the cost of operating rises, because every model improvement burns far more tokens. Meanwhile, anyone who builds their product on a single model from a single provider is accumulating a risk that shows up on no invoice: the risk that the provider decides your price, your continuity and your consumption for you. The structural answer, already endorsed by Gartner and running in production, is multi-model architecture. The rest of this article explains why, and what to do.

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin: 48px 0; padding: 32px; background: linear-gradient(135deg, #0d9488 0%, #1a365d 100%); border-radius: 6px; color: #fff;">
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">150x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">drop in price per token from GPT-4 to GPT-4o, per Altman</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">3x to 18x</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">yearly rise in the absolute cost of running frontier models</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 3.4em; font-weight: 800; line-height: 1; margin-bottom: 8px;">85%</div>
    <div style="font-size: 0.95em; opacity: 0.9; line-height: 1.4;">savings from routing between models while keeping 95% of performance</div>
  </div>
</div>
<p style="font-size: 0.85em; color: #64748b; text-align: center; margin: -32px 0 40px 0;">Sources: Sam Altman, "Three Observations" · The Price of Progress (MIT/Epoch, arXiv 2511.23455) · RouteLLM (LMSYS / UC Berkeley)</p>

<div style="background: linear-gradient(135deg, #ebf8ff 0%, #f0fff4 100%); border-left: 4px solid #0d9488; border-radius: 0 8px 8px 0; padding: 24px 28px; margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h3 style="margin: 0 0 16px 0; font-size: 1.1em; font-weight: 700; color: #1a365d; letter-spacing: 0.01em;">What you need to know</h3>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: #2d3748;">
    <li style="margin-bottom: 8px;"><strong>The price falls, but your bill rises.</strong> The price for equivalent capability drops between 5x and 10x a year. At the same time, the cost of running at the frontier rises between 3x and 18x a year, because reasoning models and agents burn far more tokens.</li>
    <li style="margin-bottom: 8px;"><strong>Lock-in is no longer theory.</strong> In January 2026 OpenAI retired GPT-4o and other models from ChatGPT by unilateral decision. The provider controls the lifecycle of the model you depend on.</li>
    <li style="margin-bottom: 8px;"><strong>Today's price may be subsidised.</strong> Sequoia put the gap between AI investment and the revenue that justifies it at 600 billion dollars. If today's price is not profitable for the provider, tomorrow's margin depends on decisions you do not make.</li>
    <li style="margin-bottom: 8px;"><strong>The right metric is not price per token.</strong> It is the ratio of output quality to cost. Measuring productivity by tokens consumed only benefits whoever sells tokens.</li>
    <li style="margin-bottom: 8px;"><strong>The defence is architecture, not negotiation.</strong> Routing each task to the right model, with provider fallback and a sovereign option, delivers resilience and efficiency in a single design decision.</li>
  </ul>
</div>

## The two truths that coexist

The market conversation settled on the easy headline: "AI keeps getting cheaper." It is true per token and misleading per business. To understand the trap you have to hold two facts at once.

**Per unit, AI is getting cheaper at an unprecedented rate.** The price to reach a given performance level falls between 5x and 10x a year, according to the reference paper *The Price of Progress* (MIT and Epoch AI). Epoch's primary data refine this: the median is 50x a year, and filtering only post January 2024 it rises to 200x. Three top authorities converge on the same round figure. Guido Appenzeller (a16z) coined the term "LLMflation" and sums it up: "the cost of LLM inference has dropped by a factor of 1,000 in 3 years." Sam Altman puts it at 10x every twelve months, with a concrete 150x between GPT-4 and GPT-4o. Ethan Mollick (Wharton): "when GPT-4 came out it was around 50 dollars to work with a million tokens; now it costs around 14 cents."

**And the cost per task still rises.** Here is the trap, and the same paper names it bluntly: the absolute cost of running frontier models rises between 3x and 18x a year, because every marginal gain in performance demands substantially more inference. The mechanism has a name: token consumption. An agentic model spends between 5 and 30 times more tokens per task than a standard chatbot, according to Gartner. In agentic coding, Microsoft Research measures up to 1,000 times more tokens than a coding chat. And consumption is stochastic: the same task run twice can differ by up to 30x in total tokens. More tokens does not mean more accuracy.

Gartner sums it up without mercy: by 2030 inference will cost providers more than 90% less than in 2025, but that saving will not reach the customer, because consumption grows faster than price falls.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  The price per token will keep falling and it will be a distraction. The variable that decides your margin toward 2030 is consumption, not unit price.
</blockquote>

## Lock-in is no longer theory

So far this is all about cost. The part almost nobody budgets for is control. Anyone who builds a product, a service or a workflow on a single model from a single provider signs three blank cheques at once.

1. **Price cheque.** You accept whatever pricing the provider sets tomorrow.
2. **Continuity cheque.** You accept that the model keeps existing.
3. **Consumption cheque.** You accept that every capability upgrade multiplies the tokens you pay for.

The continuity cheque already has victims. On 29 January 2026 OpenAI announced it would retire GPT-4o, GPT-4.1, GPT-4.1 mini and o4-mini from ChatGPT, effective two weeks later. The official justification: only 0.1% of users still chose GPT-4o daily after the migration to GPT-5.2. The #keep4o movement gathered 21,000 signatures. Nothing changed.

The lesson is not about GPT-4o. It is about who decides. The provider prunes low-usage models even when a minority depends on them in production. If your prompt engineering, your evals and your product are calibrated on a specific model, its retirement is your problem, not theirs. One honest caveat: this retirement applied to the ChatGPT interface, not the API, which "does not change for now." But the forced-migration pattern is what matters.

Andrej Karpathy named the underlying risk. When the leading models go down, he says, it is "kind of like an intelligence brownout in the world: the planet just gets dumber the more reliance we have on these models." His framing is precise: LLMs "feel like they have properties of utilities right now," like electricity or water. Depending on a single utility, with no alternative, is the risk.

## You depend on an economy that still loses money

There is a second cost, more speculative but just as relevant to your budget: you depend on a market whose accounts do not yet add up. David Cahn, of Sequoia Capital, posed the most cited calculation in the sector in 2024 and called it "AI's 600 billion dollar question": the gap between what has been invested in AI infrastructure and the revenue that should justify it. Cahn is no doom-monger, he says it calmly: "speculative frenzies are part of technology, and those who remain level-headed have the chance to build extremely important companies."

The verified evidence confirms the price falls and the model deprecations. It does not confirm the labs' internal economics, but the contextual signals point in an uncomfortable direction: a paying user at 200 dollars a month can consume up to 5,000 dollars worth of tokens, and investors in the major labs are asked to "hold on a few more years." The business question is the same in the optimistic scenario (models commoditise and prices fall) and the pessimistic one (consolidation and price rises): if today's price is subsidised by venture capital, what happens to your margin when the labs have to be profitable?

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  Building on one model from one provider is signing three blank cheques at once: price, continuity and consumption.
</blockquote>

## The answer: a multi-model strategy

The good news is that the defence is not waiting for the market to settle or renegotiating rates. It is an architecture decision, and the reference analyst already endorses it. Gartner, in March 2026, says it without ambiguity: "value will accrue to the platforms able to orchestrate workloads across a diverse portfolio of models. Routine, high-frequency tasks should be routed to small, domain-specific models. Expensive frontier inference should be tightly restricted and reserved exclusively for complex, high-margin reasoning."

That is exactly the approach we apply at Zoopa: agents that distribute tasks across models, choosing the right one by cost and capability, with fallbacks between providers. And the saving is quantified. RouteLLM, from LMSYS and UC Berkeley, routes between a strong model and a weak one based on prompt complexity: it saves more than 85% on the MT Bench benchmark while retaining 95% of GPT-4's performance. On MMLU the saving is 45% and on GSM8K 35%. The 85% is the most favourable case, not the average, but even the floor of that range changes the economics of running AI at scale.

You do not have to build the routing from scratch. Production tools already exist: OpenRouter's Auto Router picks the model from a curated pool based on complexity, with an explicit cost-quality trade-off parameter; LiteLLM, open source and self-hostable, is a gateway to more than 100 APIs with automatic ordered-chain fallback between providers; and RouteLLM itself is open source.

### The sustainable architecture, in four layers

1. **Task classification.** Every request is tagged by complexity before it touches a model.
2. **Cost-and-capability routing.** Trivial tasks go to small models; complex reasoning to the frontier, and restricted.
3. **Multi-provider fallback.** An ordered chain across different labs. If one goes down, raises prices or deprecates a model, the system does not notice.
4. **Sovereign or open-weight option.** For sensitive data or to decouple from per-token billing, self-hosted models inside the chain.

This is resilience (you do not depend on one provider) plus efficiency (you do not pay frontier prices for trivial tasks) in a single design decision.

## What we see from the trenches

> This section is pending real cases with a named client. Without them, this block is general commentary. With them, it is positioning. Fill in before publishing (see block 3 of the source).

[EXAMPLE 1: real story from a recent project]
Client: <client or internal branded content, anonymised if under NDA>
Tension: <what dependency, cost or continuity problem appeared>
Decision: <what was done: tiered routing, provider fallback, open-weight option, consumption cap>
Lesson: <what rule was drawn>

[EXAMPLE 2: real story from a recent project]
Client: <client or anonymised if under NDA>
Tension: <what problem appeared>
Decision: <what was done>
Lesson: <what rule was drawn>

What we can share as a pattern: in the projects we touch, the risk is rarely felt until the provider changes something. A price goes up, a model is deprecated, a quota is adjusted, and suddenly a system that worked depends on a decision no one on the team made. Multi-model architecture is not a technical optimisation, it is the difference between finding out about that change or not.

<div style="background: #1a1a1a; color: #fff; padding: 32px; margin: 40px 0; border-radius: 4px; text-align: center;">
  <p style="margin: 0 0 12px 0; font-size: 0.9em; opacity: 0.8; text-transform: uppercase; letter-spacing: 1px;">Smart AI strategy</p>
  <p style="margin: 0 0 20px 0; font-size: 1.3em; line-height: 1.4;">This is what we do. We design AI systems that route each task to the right model and do not depend on a single provider.</p>
  <a href="https://zoopa.es/en/services/strategy/" style="display: inline-block; background: #fff; color: #1a1a1a; padding: 12px 28px; text-decoration: none; font-weight: 600; border-radius: 2px;">This is our thing →</a>
</div>

## When a single provider helps and when it hurts

None of this is a case against the major labs or against frontier models. They are extraordinary technology, and for many early-stage builds betting on a single provider is the right call. The difference between helping and hurting is not the provider, it is the context.

A single provider helps when you are validating an idea, volume is low, you handle no regulated data, and speed to market matters more than margin. At that stage, building routing and fallback is premature complexity. It hurts when the system goes into production at scale, when inference cost starts showing up in the P&L, when you handle data subject to GDPR or sector regulation, or when that model has become a structural part of your product. There, dependency stops being a convenience and becomes an exposure. The practical rule: lean on one provider while it is optional, design the exit before it becomes mandatory.

## Sovereign AI: independence as a risk hedge

The fourth layer of the architecture, the sovereign option, deserves a note of its own, because Europe has already decided that depending on US providers is a risk of state, not just of business. In September 2025 Mistral closed a 1.7 billion euro Series C at an 11.7 billion valuation, led by ASML, and is building its own data centres to stop depending on US cloud. DeepSeek proved through cost that the state of the art does not require massive CapEx or closed models: the launch of its R1 model wiped 600 billion dollars off NVIDIA's market cap in a single day, the largest one-day drop for any company in US history. Both publish open-weight models that run on your own infrastructure.

For a company, sovereignty translates into a concrete decision: self-hosting. Its economics depend on volume (the breakeven against a premium API is around 256 million tokens a month, with GPU utilisation as the critical variable), but there is a case where the cost calculation stops mattering. For workloads with data subject to HIPAA, GDPR or SOC2, without a data processing agreement consumer APIs cannot legally process that information. There, self-hosting stops being a cost decision and becomes one of jurisdiction. With the EU AI Act fully applicable from 2 August 2026, that line will stop being theoretical for many sectors.

## What to do if you build or already run AI

The token trap is not defused by negotiating price. It is defused with governance and design. These are the levers that actually move the risk and the bill.

1. **Measure quality per cost, not consumption.** The goal is the minimum tokens for the maximum output quality, not the maximum tokens to look productive. Rewarding "tokens burned" subsidises useless work.
2. **Classify each task before choosing a model.** Do not send a trivial classification to the biggest model. Between a flagship and a small model there is an order of magnitude of difference in price.
3. **Set up provider fallback from day one.** An ordered chain across different labs turns an outage, a price rise or a deprecation into a non-event.
4. **Reserve an open-weight option for sensitive data.** For compliance and to decouple from per-token billing on the workloads that justify it.
5. **Budget on the high percentile.** Since consumption is stochastic, take several runs of each representative task and budget on the bad case, not the average. Set per-response token caps and loop limits on agents.
6. **Use prompt caching.** Reusing the stable part of a prompt cuts input cost by up to 90% with some providers. It is one of the highest-return optimisations with long, repeated prompts.

## So what is the way out?

Back to the start. Per token, AI keeps getting cheaper, and it will keep doing so. In aggregate, your bill rises, and it will keep rising as long as consumption grows faster than price. But cost is not the biggest risk. The biggest risk is having no alternative: depending on a model that someone else can make dearer, retire or saturate without consulting you. A multi-model strategy solves both with the same decision, because it makes every provider interchangeable. Designing it now, while it is optional, costs a fraction of what it will cost to improvise it once the margin is already compromised.

<blockquote style="border-left: 4px solid #0d9488; margin: 40px 0; padding: 24px 32px; background: #f8fafc; font-size: 1.35em; line-height: 1.5; color: #1a365d; font-style: italic; font-weight: 500;">
  A sustainable model strategy is a competitive advantage now. Later it is survival.
</blockquote>

<div style="background: #000; color: #fff; padding: 36px; margin: 48px 0; border-radius: 4px;">
  <h2 style="margin: 0 0 12px 0; color: #fff; font-size: 1.4em;">Let's talk</h2>
  <p style="margin: 0 0 24px 0; opacity: 0.8; line-height: 1.6;">If your product or your operation depends today on a single model from a single provider, it is worth having this conversation before the provider decides for you, not after. We will tell you how we design multi-model architectures at Zoopa and 498A.</p>
  <a href="https://zoopa.es/en/contact/" style="display: inline-block; background: #fff; color: #000; padding: 14px 32px; text-decoration: none; font-weight: 600;">Let's talk →</a>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Glossary</h2>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Token</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">The smallest unit of text a model processes and bills. Not a word or a letter, but a fragment. Since the model predicts and charges token by token, the token is the real currency of LLM economics. Spanish consumes more tokens per idea than English, because tokenizers were trained mostly on English.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Inference</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Each use of an already-trained model. Training is the provider's capital cost; inference is the recurring cost the customer pays. The entire token trap lives in inference.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Reasoning tokens</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">Tokens a reasoning model generates "thinking out loud" before the final answer. They usually run to thousands per query, the user does not see them but does pay for them, and they bill as output, the expensive line. They are why reasoning blows up the bill.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Agentic system</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">A pattern where the model does not just answer but plans and executes multi-step tasks in a loop, using tools. Each step re-injects the accumulated context as input, so consumption grows non-linearly and invisibly. It is the biggest amplifier of token spend.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Model routing</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">A system that, for each request, automatically decides which model is best: simple ones to a small, cheap model, complex ones to a large one. It optimises cost and quality without the user choosing. One of the most effective defences against the trap.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Fallback</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">A backup mechanism: if the primary model or provider fails, raises prices or deprecates a model, the system automatically retries with an alternative. It provides resilience against depending on a single provider.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">Open-weight</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">A model whose weights are published and can be downloaded and run on your own infrastructure, though not necessarily with fully free data or licence. Only open-weight or open-source models let you escape per-token cost by hosting the model yourself.</p>
  </div>

  <div style="margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #edf2f7;">
    <strong style="color: #1a365d; font-size: 1em;">AI sovereignty</strong>
    <p style="margin: 6px 0 0 0; color: #4a5568; line-height: 1.6; font-size: 0.93em;">The ability of an organisation or country to control its own AI infrastructure (models, compute, data) without critically depending on foreign third parties. It is the main non-economic argument for self-hosting and open-weight models.</p>
  </div>
</div>

<div style="margin: 2em 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <h2 style="font-size: 1.3em; color: #1a365d; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #0d9488;">Frequently asked questions</h2>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">What is the token trap?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">It is the paradox that the price per token falls year after year while the total AI bill of many companies rises. It happens because reasoning models and agents consume far more tokens per task, so consumption grows faster than the unit price falls.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Why is depending on a single AI provider a risk?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">Because the provider controls the model lifecycle: it can raise the price, retire the model or change quotas without consulting you. In January 2026 OpenAI retired GPT-4o from ChatGPT despite a petition with 21,000 signatures. If your product is calibrated on a specific model, its retirement is your problem.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">What is a multi-model strategy?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">It is an architecture that routes each task to the most suitable model by cost and capability, with automatic provider fallback and a sovereign or open-weight option for sensitive data. It delivers resilience against dependency and efficiency against overspend in a single design decision. Gartner endorses it as the approach where value will accrue.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">How much do you save by routing between models?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">RouteLLM, from LMSYS and UC Berkeley, documents up to 85% savings while retaining 95% of GPT-4's performance on its most favourable benchmark. On other benchmarks the saving is 45% and 35%. The exact figure depends heavily on the task, but even the floor of the range changes the economics of running AI at scale.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">When is self-hosting an open-weight model worth it?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">On cost, above a high volume (breakeven against a premium API is around 256 million tokens a month, with GPU utilisation as the critical factor). But for data subject to GDPR, HIPAA or SOC2 without a processing agreement, self-hosting can be the only compliant route, and then the decision stops being about cost and becomes about jurisdiction.</p>
  </div>

  <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0;">
    <h3 style="margin: 0 0 12px 0; font-size: 1.05em; font-weight: 700; color: #1a365d;">Do you have to build the routing from scratch?</h3>
    <p style="margin: 0; color: #4a5568; line-height: 1.7; font-size: 0.95em;">No. Production tools already exist: OpenRouter's Auto Router picks the model from a curated pool based on complexity, and LiteLLM (open source and self-hostable) is a gateway to more than 100 APIs with automatic chained fallback between providers. RouteLLM itself is also open source.</p>
  </div>
</div>
