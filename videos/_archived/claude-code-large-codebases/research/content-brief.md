# Content Brief — claude-code-large-codebases

**Generated**: 2026-05-14
**Topic type**: ARTICLE_RESPONSE
**Source authority**: `videos/claude-code-large-codebases/tmp/source.md` (verbatim Anthropic blog post)
**Template**: long-form/anthropic (1920×1080, ~480s, friendly-educational)

This brief is the **authoritative input** for Phase 1 (plan), Phase 2 (script), and Phase 2.5 (critique). Downstream phases MUST NOT invent claims beyond what is grounded here in `tmp/source.md`.

---

## 1. Hook Candidates

All hooks below are grounded in article specifics — each can be defended with a verbatim quote or paraphrase from `tmp/source.md`. Scored 1-10 on (a) stop-power, (b) source-fidelity, (c) thesis-setup.

### Hook A — RECOMMENDED — Score 9/10

> **"Five extension points. Two capabilities. Three patterns. Anthropic just published their own playbook for running Claude Code in a large codebase — and the part most teams miss is that the harness matters more than the model."**

- **Stop-power**: 9 — three short numbered phrases trigger Zeigarnik effect ("what are they?")
- **Source-fidelity**: 10 — 5 + 2 + 3 are exact article counts; "the harness matters more than the model" is a near-verbatim section heading.
- **Thesis-setup**: 9 — primes the harness-over-model thesis the entire video reinforces.
- **Trace**: §"The harness matters as much as the model" (heading) + §"five extension points — CLAUDE.md files, hooks, skills, plugins, and MCP servers" + §"Two additional capabilities, LSP integrations and subagents" + §"three patterns appeared consistently".

### Hook B — Score 8/10

> **"Most teams think Claude Code's power comes from the model. Anthropic just told us the truth: it's everything around the model — and they published the full playbook."**

- **Stop-power**: 8 — opens with a misconception flip, classic anti-slop pattern.
- **Source-fidelity**: 10 — "One of the most common misconceptions about Claude Code is that its capabilities are solely defined by the model used" is verbatim source.
- **Thesis-setup**: 9 — strong, but slightly less specific than Hook A.
- **Trace**: §"The harness matters as much as the model", paragraph 1.

### Hook C — Score 7/10

> **"Multi-million-line monorepos. Thousands of developers. Decades-old legacy code. Anthropic just laid out what actually works — and most of the wins aren't from the model."**

- **Stop-power**: 8 — scale-establishing numbers create authority.
- **Source-fidelity**: 10 — quoted phrases are verbatim from article paragraph 2.
- **Thesis-setup**: 7 — flags the harness angle but more diffusely than A.
- **Trace**: §"Claude Code is running in production across multi-million-line monorepos..."

### Hook D — Backup — Score 7/10

> **"Anthropic just dropped Part 1 of a brand-new series: Claude Code at scale. Here's everything in the playbook — the 5 extension points, the 2 capabilities, and the 3 patterns separating teams that ship from teams that stall."**

- **Stop-power**: 7 — relies on series-launch novelty.
- **Source-fidelity**: 10 — series name and counts are exact.
- **Thesis-setup**: 8 — frames as authoritative reference.
- **Trace**: §"This article is part of Claude Code at scale, a new series..."

**Pick Hook A for the script.** Strongest combination of specificity, source-grounding, and thesis-priming.

---

## 2. Story Arc — Recommended Scene Order

Total target: ~480s (8 min). 12 scenes mapped to `templates/long-form/anthropic/compositions/` archetypes. Image anchors per `tmp/image-map.md`.

| # | Scene archetype                      | Duration | Purpose                                                                                                                                       | Image anchor                  |
| - | ------------------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| 1 | `scene-hook.html`                    | ~35s     | Hook A — "5 extension points. 2 capabilities. 3 patterns." Slam the three numbers + thesis ("harness > model"). Open thumbnail-grade.         | `header-icon.svg` (small chrome) |
| 2 | `scene-source-cards.html`            | ~30s     | Establish source authority — Anthropic blog series "Claude Code at scale", Part 1. Surface the URL + date + reading time + Applied AI team byline. | `header-icon.svg`             |
| 3 | `scene-stat-pill-row.html`           | ~35s     | The scale problem — "multi-million-line monorepos, decades-old legacy systems, dozens of microservices, thousands of developers". 4 stat pills + the language list (C / C++ / C# / Java / PHP) as a sub-row. | —                             |
| 4 | `scene-side-by-side.html`            | ~45s     | Agentic search vs RAG retrieval — left side RAG failure mode ("returns a function the team renamed two weeks ago"), right side agentic ("each developer's instance works from the live codebase"). | —                             |
| 5 | `scene-image-3d-reveal.html`         | ~55s     | **Hero anchor: `fig1-harness.png`** — the 7-component harness table. Narration walks through the 5 + 2 components with callout pills naming each row. Ends on the thesis: "the order matters — CLAUDE.md first, MCP last." | **`fig1-harness.png`**        |
| 6 | `scene-list-cards.html`              | ~60s     | The 7 harness components as enumerated cards (step-by-step reveal, ~6s per card): CLAUDE.md → Hooks → Skills → Plugins → LSP → MCP → Subagents. Each card: name + 1-line "what it does" + 1-line "common confusion" from the article table. | —                             |
| 7 | `scene-subscribe-banner.html`        | ~12s     | Mid-video subscribe banner (~50% mark). Quick beat: "If this playbook is useful, hit subscribe — Part 2 of the series drops next."            | —                             |
| 8 | `scene-list-cards.html` (variant)    | ~70s     | **Pattern 1: Navigability** — the 6 sub-patterns from the article as cards (lean+layered CLAUDE.md, subdir init, scoped tests/lint, .gitignore + permissions.deny, codebase maps, LSP symbol-not-string). Tight step-by-step reveal. | —                             |
| 9 | `scene-quote-card.html`              | ~35s     | **Pattern 2: Maintain CLAUDE.md as models evolve** — pull-quote on the "3-6 month review" cadence + p4 edit anecdote as supporting beat below the quote. | —                             |
| 10 | `scene-image-3d-reveal.html`        | ~55s     | **Hero anchor: `fig2-rollout-phases.png`** — **Pattern 3: Ownership**. Narration covers agent-manager / DRI / cross-functional working group + the two customer anecdotes (plugin+MCP suite on day one; dedicated AI-tooling team). | **`fig2-rollout-phases.png`** |
| 11 | `scene-dynamous-midroll.html`       | ~18s     | Dynamous midroll (~60-70% mark). Locked spoken line: "If you want to learn more about AI, check out the dynamous.ai community."               | —                             |
| 12 | `scene-image-3d-reveal.html`        | ~40s     | **Hero anchor: `fig3-getting-started-checklist.png`** — the takeaway recap. Surfaces the article's "Getting started" checklist + edge-cases call-out (hundreds-of-thousands of folders, non-git VCS — promised for future installments). | **`fig3-getting-started-checklist.png`** |
| 13 | `scene-cta.html`                    | ~30s     | Engagement CTA — debate-sparking question on screen + spoken close + brand chrome. Total runtime ~520s — trim scenes 6/8/10 by 5-10s each to hit ~480s. | `header-icon.svg`             |

**Note**: 13 scenes total (12 + the CTA) — Phase 1 may consolidate scenes 5/6 (the harness fig + the 7-card enumeration) into a single scene if the time budget is tight. Recommended consolidation: shorten Scene 6 to ~45s with quicker card reveals.

**Figure → scene anchoring** (per `tmp/image-map.md`):
- `fig1-harness.png` → Scene 5 (~Act 2 opening, after the hook + problem framing)
- `fig2-rollout-phases.png` → Scene 10 (~Act 3 — ownership / rollout)
- `fig3-getting-started-checklist.png` → Scene 12 (~recap, immediately before CTA)
- `header-icon.svg` → chrome only (hook + CTA, 96-120px accent — never hero)

---

## 3. Must-Mention Checklist (QG-3 enforcement)

Every item below MUST appear in the final script. Phase 2.5 QG-3 will reject scripts missing any.

| # | Required content                                                                                                                                                                                          | Trace in source                                                                  |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 1 | Claude Code uses **agentic search** (no embedding index), not RAG retrieval                                                                                                                                | §"Claude Code navigates a codebase the way a software engineer would..."          |
| 2 | The article explains **why RAG fails at scale** (index lag, references stale renames/deletes)                                                                                                              | §"By the time a developer queries the index, it reflects the codebase as it existed days, weeks, or even hours ago" |
| 3 | The **5 extension points** + **2 capabilities** = 7-component harness                                                                                                                                       | §"The harness is built from five extension points... Two additional capabilities" |
| 4 | **Order matters**: CLAUDE.md first, MCP last                                                                                                                                                                | §"The order in which teams build them matters"                                    |
| 5 | The **3 configuration patterns**: (1) navigability — lean layered CLAUDE.md, subdir init, scoped tests/lint, .gitignore + permissions.deny, codebase maps, LSP for symbol-not-string search; (2) actively maintaining CLAUDE.md as models evolve (3-6 month review); (3) assigning ownership — agent-manager / DRI / cross-functional working group | §"Three configuration patterns from successful deployments"                       |
| 6 | **Languages explicitly named**: C, C++, C#, Java, PHP                                                                                                                                                       | §"languages that teams don't always associate with AI coding tools, such as C, C++, C#, Java, PHP" |
| 7 | **Customer anecdote**: large retail organization with an internal-analytics plugin                                                                                                                          | §"a large retail organization we work with built a skill connecting Claude to their internal analytics platform" |
| 8 | **Customer anecdote**: enterprise software co. with org-wide LSP deployment for C / C++                                                                                                                     | §"One enterprise software company we worked with deployed LSP integrations org-wide" |
| 9 | **Customer anecdote**: plugin+MCP suite available on day one of rollout                                                                                                                                      | §"At one company, a couple of engineers built a suite of plugins and MCPs that were available on day one" |
| 10 | **Customer anecdote**: another company with a dedicated AI-coding-tools team                                                                                                                                | §"At another, an entire team focused on managing AI coding tools had the infrastructure in place" |
| 11 | **Edge cases NOT covered** in this article: hundreds-of-thousands of folders / millions of files, legacy non-git VCS — promised for future installments                                                     | §"codebases with hundreds of thousands of folders and millions of files, or legacy systems on non-git version control" |
| 12 | The article is **first installment** of the new **"Claude Code at scale"** series                                                                                                                            | §"This article is part of Claude Code at scale, a new series"                     |
| 13 | The **"agent manager"** is a hybrid PM/engineer role; DRI is the minimum viable version                                                                                                                      | §"An emerging role in several organizations is an agent manager: a hybrid PM/engineer function" |
| 14 | The **cross-functional working group** is engineering + information security + governance reps                                                                                                                | §"engineering, information security, and governance representatives"               |
| 15 | **3 to 6 month** configuration-review cadence                                                                                                                                                                | §"every three to six months"                                                       |

**Coverage target**: 15 / 15. If Phase 2 drops below 13 / 15, QG-3 fails.

---

## 4. Banned-Claim List

NEVER make any of these claims. Each is either fabricated (not in source) or a misreading of the source. Phase 2b fact-check will reject any of these.

| # | Banned claim                                                                                                                                                                                    | Why banned                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1 | "Anthropic recommends X% of teams adopt Y"                                                                                                                                                       | No percentages or adoption stats in the article. Avoid all invented numbers.                                                |
| 2 | Naming specific customers beyond what the article says (e.g., "Stripe uses LSP", "Shopify built a plugin")                                                                                       | Article uses anonymized "large retail organization", "enterprise software company". The only named customer is **Zoox** (via Amit Navindgi in acknowledgements) — and even Zoox is only credited as **providing feedback on the article**, not as a deployment. |
| 3 | "Cursor/Windsurf/Aider does RAG — Claude Code does agentic search"                                                                                                                               | Article says "the AI coding tools" (past tense, generic). Don't name competitors the article doesn't name.                  |
| 4 | "Claude Sonnet 4.x is required" / model-version-specific claims                                                                                                                                  | Article makes the opposite point — harness > model — and doesn't specify model versions.                                    |
| 5 | "MCP is the most important extension point"                                                                                                                                                       | Article explicitly says MCP is LAST in order — building MCP first is called out as a "common confusion".                    |
| 6 | "Skills replace CLAUDE.md"                                                                                                                                                                        | Article positions them as complementary — skills are progressive disclosure, CLAUDE.md is always-loaded.                    |
| 7 | "Agentic search is faster than RAG"                                                                                                                                                              | Article doesn't claim speed; the claim is freshness / accuracy at scale (no stale index).                                   |
| 8 | "RAG-based AI coding tools are dead / dying"                                                                                                                                                     | Article describes RAG's failure modes at scale — not a death-sentence claim.                                                |
| 9 | "Anthropic's Applied AI team works with every customer"                                                                                                                                          | Article says Applied AI "works directly with engineering teams to translate these patterns" — bespoke engagement, not universal. |
| 10 | "All teams should adopt the agent manager role"                                                                                                                                                  | Article positions agent manager as an "emerging role in several organizations" — minimum viable is just a DRI.              |
| 11 | "The 3-6 month review must happen on a fixed schedule"                                                                                                                                            | Article says "every three to six months, but it's also worth doing one whenever performance feels like it's plateaued"      |
| 12 | "Subagents are an extension point"                                                                                                                                                                | Article footnotes them as a **delegation capability**, not a configured extension point. LSP and Subagents are CAPABILITIES, the 5 extension points are the actual extension layer. |
| 13 | "RAG indexes the entire codebase at query time"                                                                                                                                                  | Article says embedding happens at ingest time; retrieval at query time is fast. The failure mode is index lag, not query cost. |
| 14 | Hot takes the article doesn't take (e.g., "this is a death blow to indexing-based tools", "Anthropic is throwing shade at Cursor")                                                                | Article is professional / neutral. Mirror that voice — no editorialization.                                                  |
| 15 | "Claude Code performs best on C / C++"                                                                                                                                                            | Article says "Claude Code performs better than most teams expect" in these languages — comparative to expectation, not absolute best. |

---

## 5. Engagement CTA Candidates

All candidates: debate-sparking, binary or short-list answer, reference a specific article claim, low cost to answer. Per `.claude/rules/engagement-cta.md`.

### CTA A — RECOMMENDED — Score 9/10

> **"Anthropic says the harness matters more than the model. Do you buy it — or do you think it's still mostly Claude Sonnet doing the heavy lifting? Drop your pick below."**

- **Binary**: yes ("harness" vs "model") ✓
- **Polarizing**: yes — directly challenges the article's central thesis ✓
- **References specific claim**: "the harness matters more than the model" (article section heading) ✓
- **Low cost**: 5-second answer ✓

### CTA B — Score 8/10

> **"Anthropic says you should review your CLAUDE.md every three to six months. Too long? Too short? When was YOUR last cleanup?"**

- **Binary/short-list**: "too long" / "too short" / "just right" / "never" ✓
- **Polarizing**: yes — most viewers will say "never" and that's its own bait ✓
- **References specific claim**: "every three to six months" ✓
- **Low cost**: 5-second answer ✓

### CTA C — Score 7/10

> **"Anthropic's calling the new role an 'agent manager' — hybrid PM-slash-engineer running the Claude Code ecosystem. Real job? Or rebranded DevEx? Where do you stand?"**

- **Binary**: real job / rebrand ✓
- **Polarizing**: yes — engineering culture has strong opinions on titles ✓
- **References specific claim**: "agent manager: a hybrid PM/engineer function" ✓
- **Low cost**: 5-second answer ✓
- **Note**: slightly more niche audience (people who care about role titles) — hence the lower score vs A.

### CTA D — Backup — Score 6/10

> **"Five extension points, two capabilities, three patterns. Which one would YOU build first? CLAUDE.md, hooks, or skills? Drop it below."**

- **Short-list**: yes (CLAUDE.md / hooks / skills) ✓
- **Polarizing**: medium — less debate-forcing than A/B/C ✓
- **References specific claim**: the 5+2 breakdown ✓
- **Low cost**: 5-second answer ✓

**Pick CTA A for spoken close + on-screen `#cta-question` + youtube-description.md closer.** The harness-vs-model debate is the article's central tension and the most defensible source-grounded CTA.

---

## 6. Source Citations Map

Every key claim in the script must trace to a specific paragraph or table entry in `tmp/source.md`. This map is what Phase 2b uses to fact-check.

| Claim                                                                                                                                          | Source location                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 5 extension points                                                                                                                              | §"The harness matters as much as the model", paragraph 2                                                |
| 2 capabilities (LSP, subagents)                                                                                                                 | Same paragraph + table footnote                                                                          |
| 3 configuration patterns                                                                                                                        | §"Three configuration patterns from successful deployments" (heading)                                   |
| "harness matters more than the model"                                                                                                           | §"The harness matters as much as the model" (section heading) + "the ecosystem built around the model—the harness—determines how Claude Code performs more than the model alone" |
| Agentic search vs RAG                                                                                                                           | §"How Claude Code navigates large codebases", paragraphs 2-4                                            |
| Languages: C / C++ / C# / Java / PHP                                                                                                            | §"Claude Code is running in production..." paragraph + "languages that teams don't always associate"     |
| Multi-million-line monorepos / thousands of developers                                                                                          | Same paragraph                                                                                            |
| CLAUDE.md = "context files Claude reads automatically at the start of every session"                                                            | §"CLAUDE.md files come first" paragraph                                                                  |
| Hook stop-hook reflection / start-hook dynamic load                                                                                             | §"Hooks make the setup self-improving", paragraph 1                                                      |
| Skills = progressive disclosure                                                                                                                  | §"Skills keep the right expertise available on-demand"                                                   |
| Skills can be path-scoped                                                                                                                       | §"Skills can also be scoped to specific paths"                                                           |
| Plugin bundles skills + hooks + MCP                                                                                                              | §"Plugins distribute what works"                                                                         |
| LSP enables symbol-level navigation, beats grep on common function names                                                                        | §"Language server protocol (LSP) integrations" + Pattern 1, "Running LSP servers so Claude searches by symbol, not by string" |
| MCP exposes structured search, internal docs, ticketing                                                                                          | §"MCP servers extend everything"                                                                         |
| Subagent = isolated Claude instance with own context, returns final result                                                                       | §"Subagents split exploration from editing"                                                              |
| Lean + layered CLAUDE.md                                                                                                                         | Pattern 1, bullet 1                                                                                      |
| Initialize in subdirs, not at repo root; Claude walks up the tree                                                                                | Pattern 1, bullet 2                                                                                      |
| Scope test/lint per subdir                                                                                                                       | Pattern 1, bullet 3                                                                                      |
| `.gitignore` + `permissions.deny` in `.claude/settings.json`                                                                                     | Pattern 1, bullet 4                                                                                      |
| Codebase maps for non-standard structures                                                                                                        | Pattern 1, bullet 5                                                                                      |
| LSP for symbol-not-string                                                                                                                        | Pattern 1, bullet 6                                                                                      |
| 3-6 month review cadence; or after major model releases                                                                                          | Pattern 2, last paragraph                                                                                |
| p4 edit hook example (Perforce native mode)                                                                                                       | Pattern 2, paragraph 2                                                                                   |
| Agent manager = hybrid PM/engineer                                                                                                                | Pattern 3, paragraph 3                                                                                   |
| DRI = minimum viable owner                                                                                                                       | Same paragraph                                                                                            |
| Cross-functional working group: engineering + info-sec + governance                                                                              | Pattern 3, last paragraph                                                                                |
| Customer anecdotes (4)                                                                                                                           | Pattern 3, paragraph 2 + earlier "large retail organization"                                            |
| Edge cases not covered: hundreds-of-thousands of folders / millions of files / non-git VCS                                                       | "One caveat" paragraph at end of Pattern 1                                                              |
| Series name: "Claude Code at scale"                                                                                                              | Opening blockquote                                                                                       |
| Applied AI team works with customers                                                                                                              | §"Applying these patterns to your organization", last paragraph                                          |

---

## 7. Pronunciation Notes (copied from brief.md)

These will be enforced in Phase 2a TTS script audit. Source: `videos/claude-code-large-codebases/brief.md` Technical Terms section.

| Term      | Spelling for TTS                       | Reason                                                                                       |
| --------- | -------------------------------------- | -------------------------------------------------------------------------------------------- |
| CLAUDE.md | "claude dot M D" or "CLAUDE dot M D"   | Read as filename, not a sentence. `eleven_multilingual_v2` reads "claude dee em dee" otherwise. |
| MCP       | "M C P"                                | Spell out — the engine reads "mcp" as "mick-puh" otherwise.                                  |
| LSP       | "L S P"                                | Spell out.                                                                                   |
| RAG       | "rag" (one word)                       | The engine reads "rag" correctly in context. Verify after first chunk.                       |
| DRI       | "D R I"                                | Spell out.                                                                                   |
| monorepo  | "mono-repo" (compound, no hyphen needed) | Engine handles correctly; flagged for caution only.                                          |
| subagent  | "sub-agent" (compound)                 | Same — engine handles, flagged for caution.                                                  |
| p4 edit   | "P four edit"                          | The Perforce command — only one anecdote uses it.                                            |
| Sonnet    | "sonnet"                               | Default reading is correct. Capitalize in script for emphasis.                               |

**Heteronyms audit (per `.claude/rules/tts-pronunciation.md`)**:
- The word **"live"** appears in the article in the verb sense ("Claude Code is running in production") — no adjective-sense ambiguity. Safe.
- The word **"lead"** does NOT appear as a noun in the source article. If it surfaces in the script (e.g., "a lead agent"), swap to `primary` / `head`.
- The word **"read"** appears in present tense throughout the article ("Claude reads automatically", "Claude reads files"). Safe — sentence context disambiguates.

---

## 8. vidIQ Keyword Snapshot Summary

Full snapshot: [`vidiq-keywords.md`](./vidiq-keywords.md). For YouTube description SEO only — does NOT shape script content.

**Top 5 keywords by opportunity** (volume × competition, scoped to article topic):
1. `claude skills` — vol 91.3, comp 45.2, 1.3M est. searches/month
2. `claude code tutorial` — vol 91.1, comp 50.0, 1.27M searches/month
3. `claude code` — vol 100, comp 61.1, 7.45M searches/month
4. `claude code skills` — vol 84.3, comp 39.7, 446k searches/month
5. `how to use claude code` — vol 87.4, comp 40.8, 713k searches/month

**Chosen primary keyword for the title**: `claude code` + `large codebase` (compound). High-volume head paired with low-competition long-tail differentiator. Aligns with the source article's URL slug.

**Recommended long-tail variants** (3-5 for description front-loading + hashtags):
1. `claude code at scale` (article series name, exact match, zero competition)
2. `CLAUDE.md best practices` (12k searches, 31 competition)
3. `claude code skills` (446k searches, 39.7 competition)
4. `claude code mcp` (85k searches, 50.6 competition)
5. `claude code subagents` (47k searches, 38.4 competition)

**Title-draft candidates** (5 — Phase YT picks the winner; not script-relevant):
1. **Claude Code in Large Codebases — Anthropic's Own Playbook**
2. **The 7 Things That Make Claude Code Work at Scale (Anthropic's Playbook)**
3. **Anthropic Just Published Their Claude Code Playbook for Large Codebases**
4. **CLAUDE.md, Skills, MCP — Anthropic's Playbook for Claude Code at Scale**
5. **The Harness Matters More Than the Model — Anthropic on Claude Code at Scale**

---

## 9. Gaps / User Input Needed

**None blocking Phase 1.** All required inputs are in `tmp/source.md`, brief.md, and image-map.md. The article is complete, the images are downloaded, the pronunciation notes are provided, and the engagement-CTA candidates from the brief are usable as-is (CTA A is the polished version of brief option #1).

**Optional polish (not blocking)**:
- The user may want to pick CTA A vs CTA B based on which debate they actually want to host on their channel — both are equally valid. Default is CTA A. Phase 2 / 2.5 can confirm.
- Title decision (Phase YT) — 5 candidates listed; user can pick or let Phase YT recommend by SEO ranking.

---

## 10. Voice / Style Discipline

Per brief.md Voice/Style Notes — copy these into Phase 2.5 QG-2a:

- Source-grounded language only: "Anthropic explains", "the article lays out", "Anthropic's Applied AI team observed", "the post notes".
- NEVER "I think" / "in my opinion" / "my hot take is".
- The video is a **faithful response** to Anthropic's own playbook, not commentary on it.
- Open on a number or punchline from the article (Hook A uses "5 / 2 / 3").
- End with a debate-sparking CTA that ties to the harness-vs-model tension (CTA A).
- Friendly-educational tone, NOT news-explainer (no breathless "JUST IN" framing) and NOT tutorial (no "first, you'll need...").
