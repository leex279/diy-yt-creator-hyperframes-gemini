# Content Brief: Claude Managed Agents Launch — Dreaming, Outcomes, Multiagent, Webhooks

## Video Metadata
- **Slug**: `claude-managed-agents-launch`
- **Template**: shorts/anthropic
- **Duration**: 90s minimum, target 120-150s, hard cap 180s
- **Tone**: high-energy news-explainer with Anthropic dark-stage aesthetic; technical but punchy; "the moat just got real" framing
- **Voice Profile**: `voice_profile: news-explainer` — launch announcement, not tutorial. Phase 2 will read `brand-voice-news-explainer.md`.
- **Target Audience**: developers and AI builders shipping production agent workflows on Claude Platform; secondary = decision makers / tech leads evaluating agent infra
- **Key Angle**: The production-agent moat just got real — agents that **dream** (learn from past sessions), **delegate** (lead-agent → parallel specialists), and **self-grade** (rubric-graded outcomes loops with webhook callbacks). Dreaming is research preview; the other three ship today on Claude Platform.
- **Topic Type**: PRODUCT_TOOL (launch announcement of an existing product line — Claude Managed Agents — gaining four named features)
- **Research Depth**: STANDARD (90-180s, ~5 sources, locked-fact source.md + 1 fetched blog + ~3 corroborating articles + vidiq enrichment)

---

## Core Value Proposition
Claude Managed Agents now ship four agentic primitives — dreaming (research preview), outcomes, multiagent orchestration, and webhooks (public beta) — that turn one-shot agents into self-improving fleets you can trust to grade and finish their own work.

---

## Target Audience
**Primary**: developers and AI builders running production agents on Claude Platform — they already pay for Sonnet/Opus tokens, already wrestle with quality drift, parallel coordination, and "is it actually done yet?" polling.
**Secondary**: tech leads / engineering managers deciding which agent platform to standardize on; AI-curious builders who follow Anthropic launches.
**What they know**: tool-calling, prompts, basic agent loops, the term "rubric eval", that polling for completion sucks. Familiar with Claude Code, Sonnet 4.6, the Claude Platform.
**What they care about**: shipping reliable agent workflows without babysitting; not paying for re-runs; production-grade observability (webhooks > polling); whether the moat is real or just demo-ware.

---

## Pain Points
1. **One-shot amnesia**: agents start every session from zero — no memory of yesterday's tool calls, mistakes, or the team's tribal knowledge. [VISUAL: HIGH — same prompt, same mistake, three sessions stacked]
2. **Quality is vibes-based**: you eyeball outputs and re-prompt. There's no rubric, no auto-iteration, just `await response`. [VISUAL: HIGH — pass/fail rubric grader checking output]
3. **Parallel work is DIY**: today you hand-roll a "router agent" that calls subagents over HTTP and reconciles state. Brittle. [VISUAL: HIGH — orchestrator + 4 parallel specialist columns]
4. **Polling is paying twice**: long-running agents = while-loops, status checks, dead sessions. You pay for the tokens AND the wait. [VISUAL: MEDIUM — polling cron icon → webhook bell]
5. **No production trust signal**: "is the agent done? did it pass? what's the verification story?" — without these, agents stay in demo land. [VISUAL: HIGH — community quote: "running a fleet making decisions"]

---

## Key Features & Benefits
| Feature | Benefit (user-facing) | Differentiator? | Metric | Visual Potential | Demo? |
|---------|----------------------|-----------------|--------|-----------------|-------|
| **Dreaming** (research preview) | Agents learn from yesterday's sessions and surface team-wide patterns/preferences without you curating memory | Yes — first managed-agent platform to ship sleep-time learning as a primitive | Reviews past sessions → extracts patterns → curates memories | HIGH — "dream cycle" visualization (sessions in → memory store out) | Yes — Anthropic blog has a dreaming visualization PNG |
| **Outcomes** (public beta) | Write a rubric, a separate grader auto-iterates the agent until it passes | Yes — graders run in their own context window | +10pt task success vs standard prompting; +8.4% docx, +10.1% pptx generation quality | HIGH — rubric checklist ticking off, fail→retry loop | Yes — rubric → grader → iterate visual |
| **Multiagent orchestration** (public beta) | Lead agent delegates parallel work to specialists with their own model/prompt/tools, on a shared filesystem | Yes — persistent events, shared FS, every agent remembers what it did | Harvey: ~6× completion rate; Netflix: parallel build-log analysis | HIGH — lead → 4 columns, parallel timeline | Yes — orchestration column diagram |
| **Webhooks** (public beta) | Get notified when work is done — stop polling | No (existing pattern) but new for Managed Agents | "closes the loop for real production workflows" (community) | MEDIUM — polling cron strikethrough → webhook bell | Yes — POST callback animation |
| **Available today** | Outcomes, multiagent, webhooks ship now on Claude Platform; dreaming is gated by request form | Distinguishes shipped vs preview | "Today on Claude Platform" | HIGH — RP-vs-public-beta status pill row | Yes — status badge row |

---

## Proof Points (Scene-Ready)
| Stat/Claim | Formatted Value | Comparison Baseline | Source URL | Visual Format | Shock Factor |
|-----------|----------------|-------------------|-----------|--------------|-------------|
| Outcomes lift on task success | "+10 points" | vs standard prompting loop | https://claude.com/blog/new-in-claude-managed-agents | counter / bar | 7/10 |
| Docx file-generation quality lift | "+8.4%" | (no rubric baseline) | https://claude.com/blog/new-in-claude-managed-agents | mini bar pair | 6/10 |
| Pptx file-generation quality lift | "+10.1%" | (no rubric baseline) | https://claude.com/blog/new-in-claude-managed-agents | mini bar pair | 6/10 |
| Harvey legal-agent completion rate | "~6× completion rate" | their internal pre-multiagent baseline | https://claude.com/blog/new-in-claude-managed-agents | counter / multiplier slam | 9/10 |
| Wisedocs review speed | "50% faster reviews" | their pre-Managed-Agents baseline | https://claude.com/blog/new-in-claude-managed-agents | side-by-side timer | 7/10 |
| X-post reach within hours | "1M views · 8K likes · 702 RTs · 3.8K bookmarks · 377 replies" | for the announcement post | source.md (X screenshot) | metric strip | 8/10 |
| Pricing transparency | "$0.08 per session-hour + standard token rates" | tokens billed as standard API | https://platform.claude.com/docs/en/managed-agents/overview | callout pill | 5/10 |
| Beta header required | `managed-agents-2026-04-01` | beta-gated SDK header | https://platform.claude.com/docs/en/managed-agents/overview | code pill | 5/10 |

> All proof points sourced. None marked unsourced.

---

## Visual Concepts
1. **The Four-Pillar Status Row** — four pills rendered side-by-side. **Dreaming** (research preview, gated badge with "Request access"), **Outcomes** (public beta, green badge), **Multiagent** (public beta), **Webhooks** (public beta). Pills enter step-by-step (one every ~5s, paced to narration). Badge color encodes status. This is the spine of the video — it answers "what shipped vs what's gated" in one frame.
2. **Dream Cycle Loop** — three sessions on the left fade into a "memory store" cylinder in the middle, which radiates curated memories rightward into a fresh agent. Continuous loop animation. Optional ZZZ overlay (subtle, not cartoonish). Use the dreaming PNG from the Anthropic blog as the hero illustration with our motion overlaid.
3. **Rubric Grader Loop** — top: the agent's draft output (a code block / a doc preview). Middle: a rubric card with three checklist items, two checked green, one red. Bottom: arrow loops back to "Iterate". On the second pass all three turn green. Counter ticks "Pass 1 → Pass 2 → ✓".
4. **Lead-Agent Orchestration Column Diagram** — top: a lead agent box. Below it, four parallel columns labeled "deploy history", "error logs", "metrics", "support tickets" — Netflix's example from the blog. Each column has its own model/prompt/tools chip. Column timelines progress in parallel. Final convergence arrow back up to a "shared filesystem" frame.
5. **Polling vs Webhook Strikethrough** — left half: a cron icon polling every 30s with `await session.status()` calls stacked. Right half: a single webhook arrow firing once with a green checkmark. Left half greys out and a slash cuts across.
6. **Status Pills + Beta Header Code Pill** — code-formatted line `anthropic-beta: managed-agents-2026-04-01`. Pricing pill `$0.08/session-hour + standard token rates`. Side-by-side row.
7. **Community-Sentiment Strip** — three anonymous quote cards reveal one at a time, each with a glow accent. NO handles, NO avatars (per source.md hard rule). Quotes paraphrased: "the orchestration layer is where the real moat lives" / "webhooks finally close the loop for real production workflows" / "trust question gets unavoidable when you're running a fleet".
8. **Dynamous Endcard** — standard outro per playbook. "If you want to learn more about AI, check out the dynamous.ai community."

---

## Visual Metaphor Inventory
| Concept | Metaphor | How It Animates | Source/Inspiration |
|---------|----------|----------------|-------------------|
| Dreaming reviews past sessions | Sleep-cycle / consolidation | Sessions fade in → swirl into memory cylinder → curated memories radiate out | Anthropic's own "dreaming" framing + blog visualization PNG |
| Outcomes rubric loop | Teacher with red pen | Rubric checklist with red→green tick conversion, second-pass all-green | Editorial review (Spiral case study) |
| Multiagent orchestration | Conductor + parallel orchestra sections | Lead agent at top, 4 specialist columns playing parallel timelines, convergence | Netflix build-log example |
| Webhooks vs polling | Doorbell vs knock-knock-knock | Cron icon polling repeatedly (cluttered) → single webhook bell ringing once | Industry-standard pattern |
| Research preview vs public beta | Velvet rope vs open door | Two doors side-by-side: dreaming behind a velvet rope with "Request access" pill; the other three with "Open today" green check | Status differentiation from source.md hard rule |

---

## Demo Opportunity Inventory
| What to Demo | Format | URL (if screenshot) | Dark/Light | Wow Factor | Notes |
|-------------|--------|---------------------|------------|-----------|-------|
| Anthropic blog dreaming visualization | screenshot/illustration | https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8e9ad765c7eed52dcf468_Claude-Managed-Agents-Blog-Followup-Dreaming.png | dark | 9/10 | Already linked in source.md — download to assets/ |
| Anthropic blog Sessions UI | screenshot | https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8ea208aefcf18345ee3ef_Claude-Managed-Agents-Blog-Followup-Sessions-UI.png | dark | 8/10 | Use as the orchestration / sessions visual; download locally |
| Lead-agent → 4 columns diagram | hand-built HTML/CSS | N/A | dark | 8/10 | Build with HyperFrames primitives; pure motion |
| Rubric grader checklist | hand-built HTML/CSS | N/A | dark | 8/10 | 3-row checklist, red→green tween |
| Webhook POST snippet | code block | N/A | dark | 6/10 | Single-line code pill with `POST /your-callback` arrow |
| Beta header `managed-agents-2026-04-01` | code pill | https://platform.claude.com/docs/en/managed-agents/overview | dark | 5/10 | Inline code chip — proof of "real, today" |
| X announcement metric strip (1M views etc.) | hand-built numeric strip | N/A (source.md screenshot already on disk) | dark | 7/10 | NO handles per source.md rule |
| Anonymous community quote cards | hand-built quote tiles | N/A | dark | 7/10 | NO handles, NO names, NO avatars |

---

## Architecture Diagram Opportunities
| System/Flow | Components | Reveal Order | Complexity |
|------------|-----------|-------------|-----------|
| Multiagent orchestration | Lead agent → 4 specialists (own model/prompt/tools) → shared filesystem → persistent events | lead → first specialist → 3 more in parallel stagger → shared-FS frame | medium |
| Outcomes loop | Agent → output → grader (separate context) → rubric → fail → iterate → pass | agent → output → grader → fail-arrow → loop → pass | simple |
| Dreaming cycle | Session N-2, N-1, N → memory store → pattern extraction → curated memory injected into next session | sessions stack → memory cylinder → radiate out | medium |
| Webhooks vs polling | left: while-loop with status checks; right: single webhook callback | both reveal together → strikethrough left | simple |

---

## Competitive Landscape
| Alternative | Key Difference | Where Topic Wins | Where Alternative Wins |
|------------|---------------|-----------------|---------------------|
| OpenAI Assistants API + Swarm | OpenAI's multi-agent SDK is open-source orchestration helper, but no managed runtime + no graded-outcomes primitive + no scheduled "dreaming" memory | Managed runtime, sleep-time learning, rubric-graded loop are all platform-level | Wider model selection if you need GPT |
| LangGraph / LangChain agents | DIY orchestration framework, no managed runtime | No infra to host, billed per session-hour, persistent events on shared FS | Self-hosted, model-agnostic |
| Custom router-agent + own webhook server | Full control, but every team rebuilds the same plumbing | Plumbing solved at platform layer; rubric grader runs in its own context | Total control over scaling and cost shape |
| AWS Bedrock Agents | Managed runtime exists but no rubric-graded outcomes loop, no dreaming | Outcomes + dreaming are platform-native; 10pt task-success lift documented | AWS-native IAM / VPC integration |

---

## Notable Adopters
| Company/Person | How They Use It | Why It Matters for Video |
|---------------|----------------|------------------------|
| **Harvey** | Legal-work coordination via multiagent orchestration | "~6× completion rate" — biggest shock-stat candidate; legal = high-stakes credibility |
| **Netflix** | Build-log analysis agent using parallel specialists | Recognizable cult-hop name; concrete parallel use case (deploy history / error logs / metrics / support tickets) |
| **Spiral (Every)** | Writing agent using outcomes to enforce editorial standards | Editorial = relatable rubric use case; great for "rubric grader" demo voiceover |
| **Wisedocs** | Document quality checks | "50% faster reviews" — concrete time-savings stat |

---

## Market Context & Timing Signal
- **Market size**: agentic-AI tooling category is the dominant 2026 platform race; Anthropic competing with OpenAI (Assistants/Swarm), AWS (Bedrock Agents), Google (Vertex Agent Builder).
- **Growth**: "AI agents" YouTube monthly search ≈ 614K (vidiq); "claude managed agents" ≈ 592K monthly searches with 76 overall opportunity score (vidiq) — high-volume, mid-competition.
- **Why NOW**: Announced **live at "Code with Claude" event on May 6, 2026**. Within hours: 1M post views, 8K likes. Dreaming is the first sleep-time-learning primitive shipped by a major managed-agent platform. Webhooks closing the polling loop is what community calls "production-grade." This is a launch news-cycle moment.

---

## Messaging Hierarchy

### Must Include [Visual Treatment]
- **The four-pillar status row** — dreaming (RP) + outcomes / multiagent / webhooks (public beta). [Status Pill Row]
- **Dreaming = sleep-time learning across past sessions** — the differentiator no other platform ships. [Dream Cycle Loop visualization]
- **Outcomes = rubric + separate grader + auto-iterate** — with the +10pt task-success stat. [Rubric Grader Loop]
- **Multiagent = lead → parallel specialists on shared FS** — Netflix example, Harvey 6× stat. [Lead-Agent Orchestration Diagram]
- **Webhooks = closes the polling loop** — community quote: "real production workflows." [Polling vs Webhook strikethrough]
- **"Available today on Claude Platform"** — but dreaming is gated by request form. [Status pill row + form URL]
- **Hard distinction**: research-preview vs public-beta. Mixing these up = factual error per source.md. [Two-doors metaphor visual]

### Should Include
- Pricing transparency: $0.08/session-hour + standard token rates [pricing pill]
- Beta header `managed-agents-2026-04-01` [code chip — proof of "real, today, SDK-callable"]
- One anonymized community quote about the trust/verification question [quote card]
- "Code with Claude" event context [overline / chyron above hook]

### Could Include
- Outcomes' file-generation lift (+8.4% docx, +10.1% pptx) [mini bar pair]
- X reach metrics (1M views) [metric strip — careful, not the focus]
- Wisedocs 50% faster [side-by-side timer]

### Omit
- Specific @-handles, display names, or avatars from any community reaction (HARD RULE per source.md)
- Any speculation about what's coming next (no roadmap data in source)
- Any pricing detail not from blog/docs (no fabrication)
- Comparisons to non-major-platform alternatives we can't source

---

## Hook Architecture

### Cult-Hopping References
| Brand/Person/Concept | Why It Works | Where to Use (Hook/Mid/CTA) |
|---------------------|-------------|---------------------------|
| **Anthropic** itself | Source-of-truth brand — every dev recognizes the wordmark | Hook + CTA |
| **Claude Platform** | The runtime everyone watching is already paying for | Hook + Mid |
| **Code with Claude** event | Live-from-keynote framing = newsy urgency | Hook |
| **Netflix** | Recognizable cult-hop, real customer of multiagent | Mid (orchestration demo) |
| **Harvey** | Legal-AI cult-hop; the 6× stat lands hardest with their name attached | Mid (multiagent stat reveal) |
| **"Dreaming"** as a concept | Anthropic's own anthropomorphic framing — viewers will notice | Hook (mind-blown opener) |
| **Public beta vs research preview** badge metaphor | Velvet rope analogy is universally legible | Mid (status row) |

### Common Ground by Audience
- **Technical**: "you've shipped one agent. now you need to run a fleet of them — and verify they're not hallucinating in parallel."
- **General**: "Claude agents now learn while you sleep, grade their own homework, and call you when they're done."
- **Decision Makers**: "managed-agent runtime with rubric-based QA + scheduled memory consolidation = the production-trust story your CTO wanted."

### Contrarian Angles (Uno Reverse)
1. **"Dreaming" sounds like a marketing word — but it's the only feature that's NOT generally available.** Outcomes / multiagent / webhooks are public beta and shipping today. The flagship-named feature is gated by a form.
   - Evidence: source.md locked-fact table; X-post lead "research preview"; thread reply 1 "Request access: claude.com/form/claude-managed-agents".
2. **The real production unlock isn't dreaming — it's webhooks.** The community quote in source.md singles out webhooks as "what finally closes the loop for real production workflows." Sleep-time learning is the headline; the boring async primitive is the actual moat.
   - Evidence: source.md Reaction C; webhook subscribe pattern from thread reply 2.
3. **Multiagent orchestration in public beta forces the verification question that one-agent setups dodge.** Per source.md Reaction A: "running a fleet making decisions… which instance actually earned the result?" — capability is solved; verification is the open problem.
   - Evidence: source.md Reaction A.

### Mind-Blowing Stats
| Stat | Value | Shock Factor (1-10) | Source URL |
|------|-------|-------------------|-----------|
| Harvey legal-agent completion rate | "~6× completion rate" | 9/10 | https://claude.com/blog/new-in-claude-managed-agents |
| Outcomes lift on task success | "+10 points vs standard prompting" | 8/10 | https://claude.com/blog/new-in-claude-managed-agents |
| X-post reach in hours | "1M views in hours" | 8/10 | source.md (X screenshot) |
| Wisedocs reviews | "50% faster" | 7/10 | https://claude.com/blog/new-in-claude-managed-agents |
| Generation quality lift | "+8.4% docx, +10.1% pptx" | 6/10 | https://claude.com/blog/new-in-claude-managed-agents |
| Pricing | "$0.08/session-hour + token cost" | 5/10 | https://platform.claude.com/docs/en/managed-agents/overview |

### Preview Hook Teasers (for Scene 00 / opening 5s)
1. **"Anthropic just made Claude agents DREAM."** — bold scroll-stop opener; uses Anthropic's own framing.
2. **"6× completion. +10 points. Available today."** — three receipts in one breath; teases the body proof points.
3. **"In this video: the four primitives that just made the production-agent moat real."** — promise statement.

### Primary Open Loop Suggestion
- **Setup** (Scene 01-02): "Three of these are shipping today. One is locked behind a form. Can you guess which?" — leverage the research-preview vs public-beta distinction as the hook tension.
- **Resolution** (Scene 06-07): Reveal — the *named* flagship feature (dreaming) is the gated one; the boring plumbing (webhooks) and the workhorses (outcomes, multiagent) are what actually shipped today.

---

## Suggested Narrative Arc (Kallaway Formula)
1. **Context Lean-In** (~0-4s): "Anthropic just made Claude agents dream." Bold visual: the dream-cycle hero shot.
2. **Scroll-Stop** (~4-7s): "But the headline isn't dreaming." (Uno-reverse setup.)
3. **Contrarian Snapback** (~7-12s): "Three other primitives shipped today — and they're the actual moat." Reveal the four-pillar status row.
4. **Solution** (~12-25s): Frame Claude Managed Agents as the platform — four primitives, three shipping, one gated.
5. **Features (Benefit-Led)** (~25-95s): One scene per primitive — Dreaming (sleep-time learning), Outcomes (rubric grader, +10pt stat), Multiagent (Netflix example, Harvey 6×), Webhooks (closes the loop).
6. **Trust** (~95-115s): Anonymous community sentiment strip + pricing pill + beta header code chip.
7. **CTA** (~115-130s): "Available today on the Claude Platform. Dreaming is gated — request access at claude.com/form/claude-managed-agents." Hand off to Dynamous endcard.

Total target: ~120-130s narration + a ~5s endcard tail = 125-135s render. Acceptable within 90-180s window.

---

## Suggested Scene Structure
| # | Scene Name | Duration Est. | Key Visual | Key Stat/Quote |
|---|-----------|--------------|-----------|---------------|
| 00 | Preview Hook | 5-7s | Dream-cycle hero shot + "Anthropic just made Claude agents DREAM" hero text | bold opener |
| 01 | Scroll-Stop / Open Loop | 6-8s | Two doors side-by-side: research-preview (gated) vs public-beta (open) | "Three shipped today. One is gated. Can you guess which?" |
| 02 | The Four Pillars | 12-15s | Four-pillar status row, pills enter step-by-step | "Dreaming · Outcomes · Multiagent · Webhooks" |
| 03 | Dreaming = sleep-time learning | 18-22s | Dream-cycle loop visualization | "Reviews past sessions, extracts patterns, curates memories." |
| 04 | Outcomes = rubric grader | 18-22s | Rubric grader loop, red→green tick | "+10pt task success vs standard prompting." |
| 05 | Multiagent = lead delegates | 18-22s | Lead-agent + 4 parallel specialist columns | "Harvey: ~6× completion rate." |
| 06 | Webhooks = closes the loop | 10-14s | Polling-vs-webhook strikethrough | "Closes the loop for real production workflows." (anon quote) |
| 07 | Trust strip | 10-12s | Pricing pill + beta header code chip + 1 anon quote tile | "$0.08/session-hour · `managed-agents-2026-04-01`" |
| 08 | CTA + Dynamous endcard | 8-10s | Status row recap + form URL + Dynamous outro | "Available today. Request dreaming access at claude.com/form/claude-managed-agents." |

Total: ~105-132s narration. Inside 90-180s window with margin.

---

## Suggested Video Title Options
1. **"Anthropic Just Made Claude Agents DREAM"** — stat-led / contrarian / Anthropic's own framing [vidiq score: **84/100**]
2. **"The Production Agent Moat Just Got Real"** — angle-led / matches user's hint phrase [vidiq score: **78/100**]
3. **"Claude Agents Now Dream, Grade, and Orchestrate"** — feature-led / parallel structure [vidiq score: **72/100**]
4. **"Anthropic Just Shipped 4 Agent Primitives"** — news-led / specific count
5. **"Claude Managed Agents: Dreaming, Outcomes, Webhooks"** — keyword-rich / SEO-led

**Recommended**: Title #1 (vidiq 84). Falls back to #2 if "DREAM" feels too clickbait for the channel voice.

All under 60 chars: #1=37, #2=38, #3=44, #4=39, #5=51.

---

## SEO Keywords
| Keyword / Phrase | Search Intent | Volume Estimate |
|-----------------|--------------|----------------|
| claude managed agents | direct product lookup | high (vidiq vol 86 / 592K monthly) |
| ai agents | category-level | high (vidiq vol 86 / 614K monthly) |
| agentic ai | category | high (vidiq vol 84 / 400K monthly) |
| ai orchestration | feature-specific | medium (vidiq vol 63 / 18K monthly) |
| multi agent orchestration | feature-specific | medium (vidiq vol 65 / 23K monthly) |
| anthropic ai | brand | high (vidiq vol 73 / 72K monthly) |
| claude code | adjacent / Anthropic ecosystem | very high (vidiq vol 100 / 8.2M monthly) |
| claude sonnet 4.6 | model | medium (vidiq vol 62 / 14K monthly) |
| how to use claude code | tutorial intent | high (vidiq vol 88 / 737K monthly) |

---

## Keyword Research (vidiq)
**Used.** Three calls: keyword_research × 2 (`claude managed agents`, `multi agent orchestration`), title scoring × 3, trending × 1.

### Keyword opportunities
| Keyword | Volume (vidiq) | Competition | Overall | Recommended Use |
|---------|----------------|-------------|---------|-----------------|
| claude managed agents | 86 | 39 | **76** | primary keyword — title + description first line |
| ai orchestration | 63 | 44 | 61 | secondary — body of description |
| anthropic ai | 73 | 67 | 57 | hashtags / channel context |
| multi agent orchestration | 65 | 52 | 58 | description body |
| claude api tutorial | 61 | 29 | **65** | description body — low-competition opportunity |
| cursor vs claude | 56 | 24 | **64** | adjacent — could power a follow-up video |

### Currently trending in this niche (top short-form Claude/Anthropic videos, last ~7 days)
1. "60 AI Agents Inside Claude Code (Free Setup Guide)" — Duncan Rogoff — 237K views, 2148 vph, 3.1% engagement
2. "This 33 Page Claude Masterclass by Anthropic will save 30+ hours weekly" — Roshni Chellani — 36K views, 248 vph, 3.2% engagement
3. "Anthropic Just Dropped Claude Computer Use CLI 🫨" — Charlie Automates — 11.6K views, 146 vph, 4.5% engagement

Pattern: hook-led, claim-numbered, Anthropic-branded titles dominate. Our title #1 fits this pattern.

### Title scores (short-form)
| Candidate | vidiq score |
|-----------|-------------|
| "Anthropic Just Made Claude Agents DREAM" | **84/100** |
| "The Production Agent Moat Just Got Real" | 78/100 |
| "Claude Agents Now Dream, Grade, and Orchestrate" | 72/100 |

---

## Technical Terms (TTS Pronunciation)
| Term | Pronunciation Note |
|------|-------------------|
| Anthropic | "an-THROW-pic" — keep capital A |
| Sonnet | "SAH-net" |
| Opus | "OH-pus" |
| Haiku | "HIGH-koo" |
| Claude | "KLOHD" — single syllable |
| webhooks | "WEB-hooks" — common dev term, no spacing |
| rubric | "ROO-brick" |
| orchestration | "or-keh-STRAY-shun" |
| multiagent | "MULTI-agent" — pronounce as two words |
| Harvey | normal |
| Netflix | normal |
| Wisedocs | "WISE-docs" |
| Spiral | normal |
| `managed-agents-2026-04-01` | shown on screen only — do NOT read aloud (date string) |
| dynamous | "die-NAM-us" |

---

## Viewer Objections to Preempt
1. **"Isn't this just Anthropic copying OpenAI's Assistants API?"** — preempt by noting Anthropic is shipping rubric-graded outcomes (separate grader context window, not just function-calling) and scheduled dreaming (sleep-time learning), neither of which exist in Assistants/Swarm today.
2. **"Why is dreaming gated when it's the headline feature?"** — acknowledge openly. Use it as the open-loop tension: the boring plumbing (webhooks) shipped, the named flagship (dreaming) is gated. Honest framing builds trust.
3. **"Show me the SDK code, not the marketing."** — show the beta header chip + pricing pill on screen. Source the docs URL in the description. Don't fake a code demo.
4. **"6× completion rate from Harvey — vs what baseline?"** — clarify on screen as "vs their pre-multiagent baseline" per blog. Don't hide the relativity.
5. **"Will this make my polling code obsolete?"** — yes, intentionally. Show the strikethrough.

---

## Competitor Video Analysis
| Video/Channel | Hook Used | What They Miss |
|--------------|-----------|---------------|
| Duncan Rogoff "60 AI Agents Inside Claude Code" | claim-numbered + setup-guide CTA | Doesn't cover Managed Agents at all — Claude Code agents are the IDE-side, not the platform managed-runtime |
| Charlie Automates "Anthropic Just Dropped Claude Computer Use CLI" | "Just dropped" + emoji reaction | Computer-use focus, not managed-agents |
| Roshni Chellani "33 Page Claude Masterclass" | savings-promise framing | Education-led, not launch-news |

Implication: there is **no direct competitor short** on the Managed-Agents launch yet. First-mover window for our short.

---

## Quality Gate Results
| Gate | Check | Result | Notes |
|------|-------|--------|-------|
| QG-0A | Proof points >= 5 | **PASS** | 8 sourced proof points |
| QG-0B | Contrarian angles >= 3 | **PASS** | 3 angles, all evidence-sourced |
| QG-0C | Visual metaphor >= 1 | **PASS** | 5 metaphors |
| QG-0D | Demo opportunity >= 1 | **PASS** | 8 demo opportunities |
| QG-0E | SEO keywords >= 3 | **PASS** | 9 keywords with vidiq volume data |
| QG-0F | All stats sourced | **PASS** | every proof point has a source URL; none unsourced |
| QG-0G | Cult-hop refs >= 3 | **PASS** | 7 references |

All gates **PASS**.

---

## Gaps / Needs User Input
- **Image assets**: download the two Anthropic blog PNGs (`Claude-Managed-Agents-Blog-Followup-Dreaming.png` and `…-Sessions-UI.png`) into `videos/claude-managed-agents-launch/assets/` before Phase 4 (composition build). HyperFrames bundler rejects external URLs.
- **Pricing source confirmation**: pricing data ($0.08/session-hour) came from third-party guides + docs page summaries via WebSearch. Phase 2b should re-verify directly at https://platform.claude.com/docs/en/managed-agents/overview before letting any pricing number on screen. If unconfirmed, **drop the pricing pill** rather than risk a fabrication.
- **Beta header value**: `managed-agents-2026-04-01` likewise from third-party summary. Re-verify in Phase 2b — if unconfirmed, drop the code chip.
- **No Anthropic team quotes or named architecture diagrams** in the blog post itself. We have customer outcome stats but no in-product UI screenshots beyond the two blog PNGs. Visuals must be hand-built from those + composed primitives.
- **Voice profile decision**: locked to `news-explainer` per heuristic (live launch announcement). If Phase 2 wants `tutorial` framing, flag back to user.

---

## Sources
| Source | URL | Used For |
|--------|-----|---------|
| Anthropic blog post (primary) | https://claude.com/blog/new-in-claude-managed-agents | All feature definitions, customer stats, performance lifts |
| Locked-fact source.md | videos/claude-managed-agents-launch/source.md | X-post text, community reactions (anonymized), status distinctions |
| X screenshot (announcement) | C:\Users\Leex279\Pictures\Screenpresso\2026-05-07_00h23_44.png | reach metrics + thread quotes |
| Dreaming visualization PNG | https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8e9ad765c7eed52dcf468_Claude-Managed-Agents-Blog-Followup-Dreaming.png | hero visual asset (download local) |
| Sessions UI PNG | https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8ea208aefcf18345ee3ef_Claude-Managed-Agents-Blog-Followup-Sessions-UI.png | orchestration visual asset (download local) |
| Anthropic dreaming form | https://claude.com/form/claude-managed-agents | CTA URL — verify live in Phase 2b |
| Claude Platform docs | https://platform.claude.com/docs/en/managed-agents/overview | Pricing, rate limits, beta header — needs Phase 2b re-verification |
| Cryptobriefing news article | https://cryptobriefing.com/anthropic-claude-agents-dreaming/ | Corroboration of feature status |
| The New Stack | https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/ | Corroboration |
| InfoWorld | https://www.infoworld.com/article/4156852/anthropic-rolls-out-claude-managed-agents.html | Corroboration |
| SD Times | https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/ | Corroboration |
| WaveSpeed pricing summary | https://wavespeed.ai/blog/posts/claude-managed-agents-pricing-2026/ | Pricing reference (third-party — needs primary-source re-verify) |
| Verdent pricing guide | https://www.verdent.ai/guides/claude-managed-agents-pricing | Pricing reference (third-party) |
| vidiq keyword research | (MCP tool call) | SEO volume + competition data |
| vidiq title scoring | (MCP tool call) | Title CTR scores |
| vidiq trending | (MCP tool call) | Niche competitor analysis |
