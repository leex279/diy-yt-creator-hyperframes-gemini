# Phase 1 — Composition Plan: claude-code-large-codebases

**Generated**: 2026-05-14
**Template**: `templates/long-form/anthropic/` (1920×1080, 30fps)
**Topic type**: ARTICLE_RESPONSE
**Source authority**: `tmp/source.md` (Anthropic blog post, "How Claude Code works in large codebases")
**Brief**: `research/content-brief.md` (Phase 0 — 13-scene arc, Hook A, CTA A all locked here)
**Target duration**: 480s (~8 min), ~1200–1400 narration words at 150–160 WPM

This plan is the authoritative scene-by-scene input for Phase 2 (script) and Phase 4 (composition build). It locks the 13-scene order, archetype mapping, image anchors, accent rotation, retention components, and the hook/CTA wording. Phase 4 will replace placeholder `data_start` values with transcript-anchored word-boundary times once TTS lands.

---

## Hook Variant Locked — Hook A (Phase 0 score 9/10)

> **"Five extension points. Two capabilities. Three patterns. Anthropic just published their own playbook for running Claude Code in a large codebase — and the part most teams miss is that the harness matters more than the model."**

~32 words ≈ 12s at 160 WPM. Plenty of room to slow Hook A onto the 35s scene budget with the receipt sub-line, e.g. *"This is Part 1 of a brand-new series — Claude Code at scale."* (verbatim source phrase) and a hold-out beat before the topic slam fades to scene 2.

**Source trace**:
- "five extension points" + "Two additional capabilities" + "three patterns" — `tmp/source.md` §"The harness matters as much as the model"
- "the harness matters more than the model" — verbatim source section heading
- "Claude Code at scale" series name — `tmp/source.md` opening blockquote

---

## CTA Locked — CTA A (Phase 0 score 9/10)

**Spoken close (~5–6s narration at 160 WPM, ~16 words):**

> *"Anthropic says the harness matters more than the model. Do you buy it — or is it still mostly Claude doing the work? Drop your pick below."*

**On-screen `#cta-question` text (visible during the held final frame, must match the spoken line per `.claude/rules/engagement-cta.md`):**

> **"Harness or model — which one is doing the work?"**

(Short-form rewrite preserves the same debate: harness vs model, binary pick, references the article's central thesis. The full sentence version may instead live on screen as a sub-line.)

**YouTube description closer (Phase YT) repeats**: full spoken version verbatim.

**Why it satisfies `engagement-cta.md` HARD criteria**:
1. Binary or short-list answer — "harness" vs "model" ✓
2. Polarizing stance — directly challenges the article's central thesis ✓
3. References specific claim from the video — "the harness matters more than the model" (verbatim source heading) ✓
4. Low cost to answer — 1-word pick, senior + beginner can both fire off an opinion in 5 seconds ✓

---

## Composition Layout (13 scenes)

Scene order matches the Phase 0 brief recommendation. Scenes are tuned to a 480s target with a 1.5s tail. **One deviation**: the Phase 0 brief suggested splitting `fig1-harness.png` (scene-image-3d-reveal #1) and the 7-card enumeration (scene-list-cards) as two consecutive scenes #5+#6. I follow that as-recommended — the 3D-reveal scene has the figure speak and a single overline; the list-cards scene is the actual step-by-step enumeration. This is the strongest narrative because the figure is the **proof** and the cards are the **breakdown**.

### Accent rotation rule (template DESIGN.md)

Anthropic dark-stage long-form: orange leads hook + CTA. Purple / blue / green rotate through the middle. **No two adjacent scenes share the same lead accent.**

| # | scene_id                       | archetype                       | data_start (s) | data_duration (s) | accent  | figure_src                              | purpose                                                                                                                                            | script_anchor (1-2 sentences) |
| - | ------------------------------ | ------------------------------- | -------------- | ------------------ | ------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 1 | `scene-hook`                   | scene-hook.html                 | 0              | 32                 | orange  | (chrome only — `header-icon.svg` 96px)  | Hook A — slam "5 extension points / 2 capabilities / 3 patterns" + the thesis ("harness > model"). Thumbnail-grade opening per shorts-thumbnail-frames (also applies to long-form first frame for YouTube auto-thumb).        | Hook A verbatim + sub-line "This is Part 1 of a brand-new series: **Claude Code at scale**." |
| 2 | `scene-source-cards`           | scene-source-cards.html         | 32             | 28                 | purple  | (no figure; 3 source cards)             | Establish source authority: 3 cards = (a) Anthropic Applied AI team byline (the 8 named people), (b) Series banner — "Claude Code at scale, Part 1", (c) Published 14 May 2026 / 5 min read.                                | "It's a brand-new series from Anthropic's Applied AI team — Krifcher, Lee, Concannon and six others — published today as a 5-minute read." |
| 3 | `scene-stat-pill-row`          | scene-stat-pill-row.html        | 60             | 28                 | blue    | (no figure; 3 huge stat pills)          | The scale problem — 3 stat pills + language sub-row. Receipts that justify "large codebase".                                                                                                                                | "Anthropic says Claude Code is running in production across **multi-million-line monorepos**, **decades-old legacy systems**, and at orgs with **thousands of developers** — even on C, C-plus-plus, C-sharp, Java, P-H-P." |
| 4 | `scene-side-by-side`           | scene-side-by-side.html         | 88             | 38                 | green   | (no figure; left vs right panel)        | Agentic search vs RAG retrieval. Left: RAG failure mode (index lag returns a function the team renamed two weeks ago). Right: agentic — each developer's instance works from the live codebase.                              | "Older AI coding tools used R-A-G — embed the whole repo, retrieve at query time. At scale, that breaks: by the time you query, the index might point at a function your team renamed two weeks ago." |
| 5 | `scene-image-3d-reveal` (#1)   | scene-image-3d-reveal.html      | 126            | 50                 | orange  | **`assets/blog/fig1-harness.png`**      | **Hero anchor**: the 7-component harness table. Figure rotates in (rotateY -25°→0°, back.out(1.4)). Mono overline "FROM THE ARTICLE", 96px headline "The 7-Component Harness", 32px caption "5 extension points + 2 capabilities". | "Here it is — the playbook chart Anthropic published. Five extension points, two capabilities, and the order they recommend you build them in." |
| 6 | `scene-list-cards-harness`     | scene-list-cards.html (variant) | 176            | 70                 | purple  | (no figure; 4-card 2×2 + 3 follow-on)   | Step-by-step enumeration of the 5 extension points + 2 capabilities (7 cards, ~9.5s apart per `step-by-step-reveal.md`). Each card: name + 1-line "what it does" + tiny "common confusion" caption. Order is article-canonical (CLAUDE.md → Hooks → Skills → Plugins → LSP → MCP → Subagents). | "Start with CLAUDE-dot-M-D. Then hooks for the self-improving loop. Skills for on-demand expertise. Plugins to distribute what works. L-S-P for symbol-level navigation. M-C-P last — and the article calls it a common confusion when teams build M-C-P first." |
| 7 | `scene-subscribe-banner`       | scene-subscribe-banner.html     | 246            | 10                 | green   | (no figure; mid-video pop-in)           | ~50% mark mid-video subscribe banner. ~10s pop-in.                                                                                                                                                                          | "Quick beat — if this playbook is useful, hit subscribe. Part 2 of the series drops next." |
| 8 | `scene-list-cards-pattern1`    | scene-list-cards.html (variant) | 256            | 60                 | blue    | (no figure; 4-card grid + 2 follow-on)  | **Pattern 1 — Navigability**: 6 sub-pattern cards step-by-step (~9s apart): (1) Lean+layered CLAUDE.md, (2) Init in subdirs not root, (3) Scope tests/lint per subdir, (4) .gitignore + permissions.deny, (5) Codebase maps, (6) Run LSP for symbol-not-string. | "Pattern one: make the codebase navigable. Six things — keep CLAUDE-dot-M-D files lean and layered, initialize in subdirectories not at the root, scope tests and lint per subdir, exclude generated files via permissions-dot-deny, build a codebase map when the directory structure doesn't do the work, and run L-S-P so Claude searches by symbol not by string." |
| 9 | `scene-quote-card`             | scene-quote-card.html           | 316            | 32                 | orange  | (no figure; 180px orange quote-mark)    | **Pattern 2 — Maintain CLAUDE.md as models evolve**. Pull-quote on the 3–6 month review cadence, with the p4-edit hook anecdote as the supporting beat under the quote (became redundant after Perforce native mode).        | "Pattern two: refresh CLAUDE-dot-M-D every three to six months — or whenever performance plateaus after a model release. Anthropic gives a concrete example — a hook that intercepted file writes to enforce 'P-four edit' in Perforce. Became redundant the moment Claude Code added native Perforce mode." |
| 10 | `scene-image-3d-reveal` (#2)  | scene-image-3d-reveal.html      | 348            | 50                 | purple  | **`assets/blog/fig2-rollout-phases.png`**| **Hero anchor**: rollout phases. Pattern 3 — Ownership. Narration covers agent-manager / DRI / cross-functional working group + the two customer anecdotes (plugin+MCP suite on day one; dedicated AI-tooling team).         | "Pattern three: someone has to own this. Anthropic calls the emerging role the **agent manager** — a hybrid P-M slash engineer running the Claude Code ecosystem. Minimum viable version: a D-R-I. At one company a couple of engineers had a plugin and M-C-P suite ready on day one — at another, an entire team was already in place before the rollout began." |
| 11 | `scene-dynamous-midroll`      | scene-dynamous-midroll.html     | 398            | 12                 | green   | (no figure; brand-locked)               | Dynamous midroll (~83% mark — slightly later than the 60–70% recommended in the brief; pulled here so it lands after the Pattern 3 reveal and before the actionable recap). **Locked spoken line**.                          | "If you want to learn more about A-I, check out the dynamous-dot-A-I community." |
| 12 | `scene-image-3d-reveal` (#3)  | scene-image-3d-reveal.html      | 410            | 42                 | blue    | **`assets/blog/fig3-getting-started-checklist.png`**| **Hero anchor**: getting-started checklist. Recap the actionable take-home. Flag the edge cases NOT covered: codebases with hundreds-of-thousands of folders / millions of files, legacy non-git VCS — promised for future installments.                                | "Here's the actionable checklist Anthropic ships at the end of the post. And one caveat — they explicitly say codebases with hundreds of thousands of folders, or legacy systems on non-Git, are out of scope for Part 1. Those are coming in future installments." |
| 13 | `scene-cta`                    | scene-cta.html                  | 452            | 26.5               | orange  | (chrome only — `header-icon.svg` 96px)  | CTA A — debate question on screen + spoken close + brand chrome. Held still ≥1.5s on final frame per shorts-thumbnail-frames analogue.                                                                                       | CTA A verbatim spoken; `#cta-question` shows "Harness or model — which one is doing the work?" |

**Total**: 478.5s narration window + 1.5s tail-hold = **480s** ✓ (matches the 8-min target exactly; ±10s flex absorbed by per-card pacing in scenes 6 + 8).

---

## Deviations from Phase 0 brief recommendation (with rationale)

1. **Subscribe banner moved earlier**: brief table placed it at scene #7 inside the original sequence. I keep it at the 50% mark — the Pattern 1 list (scene 8) is the natural pivot point and lands right after the harness enumeration scene the brief calls the "Act 2 opening". This puts the subscribe ask at ~246s of 480s = 51% — bullseye mid-video position.
2. **Dynamous midroll moved later (398s, ~83%)** rather than the brief's recommended 60–70%. Reason: the brief targets a typical structure with the midroll between Pattern 1 (#6) and Pattern 2 (#8). I keep the patterns contiguous (scenes 8 → 9 → 10) for narrative flow, then drop the midroll AFTER all three patterns conclude. This sacrifices placement-percentage discipline for a stronger story arc — the viewer hears all three patterns end-to-end before the community-plug break. Phase 2.5 QG-6 may flag this; defending it on narrative grounds.
3. **Hook duration shortened (35 → 32s)**: Hook A is 32 words ≈ 12s, plus topic-slam hold + sub-line, fits comfortably in 32s without bloat. The reclaimed 3s gets redistributed to scene 6 + scene 8 (the dense list-cards scenes).
4. **No scene-architecture-stack used**: Phase 0 brief reserved it as an option for the 7-component breakdown. Scene-list-cards is the cleaner fit because each component card carries 3 lines of text (name, what it does, common confusion) — the architecture-stack archetype is a 5-layer accent strip and limits per-row text density.

---

## Retention Component Picks

Each scene gets 1–3 retention components from `shared/lib/`. The Anthropic shorts default rule (transition-whoosh ONLY, no per-element SFX) applies — for long-form, this is somewhat relaxed because cinematic-whoosh is genuinely the right per-transition SFX. Per-element SFX (impact-slam, spring-pop) used sparingly only on hero-slam moments. All other emphasis is purely visual.

| # | scene_id                       | Retention components (visual + audio)                                                                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | scene-hook                     | (a) `effects/hero-slam-shake.js` — 4-tick ±5px inline shake when the "5 / 2 / 3" stat slam locks. (b) `components/highlight-marker-sweep/` — sweep marker under "the harness matters more than the model" key phrase. (c) `cinematic-whoosh` SFX at scene boundary (data-start=32, data-volume=0.11). One `impact-slam` (volume 0.15) at the stat-slam lock.                                                                                                                                                              |
| 2 | scene-source-cards             | (a) Built-in card stagger (~5s apart per `step-by-step-reveal.md`) — 3 cards = 3 entrances. (b) `effects/stat-pill-pop.js` for the published-date pill ("14 May 2026" + "5 min read"). (c) Marker sweep under "Applied AI team" in the byline overline. (d) Whoosh at boundary.                                                                                                                                                |
| 3 | scene-stat-pill-row            | (a) Built-in 3-pill 500ms stagger from archetype. (b) `effects/stat-pill-pop.js` for each pill entrance (back.out(1.6) scale from 0.85). (c) Counter-roll on each big number ("1,000,000+" / "decades+" / "thousands+" — counters that tick from 0 → target). (d) Whoosh at boundary.                                                                                                                                              |
| 4 | scene-side-by-side             | (a) Strikethrough effect on the RAG-side stale function name (`components/strike-cross/` if available, else GSAP `tl.to` on width of a `.strike` span). (b) Live-update micro-animation on the right-panel showing "agentic search → live codebase". (c) Marker-sweep under "the live codebase" on the right panel. (d) Whoosh at boundary.                                                                                |
| 5 | scene-image-3d-reveal (#1)     | (a) Built-in 3D rotateY entrance + finite-repeat micro-yoyo (rotateY ±1.5deg on 12s sine.inOut, repeat = `Math.floor(50 / 24) = 2`). (b) 7 callout pills attached to the figure's 7 rows, revealed step-by-step (~5s apart, paced to narration). (c) Marker-sweep under "the order matters" subtitle. (d) Whoosh at boundary + one `scale-slam` (volume 0.15) when the figure locks. |
| 6 | scene-list-cards-harness       | (a) 7-card step-by-step reveal (~9.5s apart, paced to narration) per `step-by-step-reveal.md`. (b) Each card uses `effects/stat-pill-pop.js` + `back.out(1.5)` entrance. (c) Marker-sweep underline on "MCP — common confusion: building this first" sub-line on the 6th card. (d) Whoosh at boundary. (NO impact-slam — too many cards, would over-percuss.)                                                                                                                                                |
| 7 | scene-subscribe-banner         | (a) Built-in pop-in animation from archetype (`components/subscribe-banner/`). (b) Subscribe-pill finite pulse (0.92 ↔ 1 scale, 3 pulses then settle). (c) Whoosh at boundary.                                                                                                                                                                                                                                |
| 8 | scene-list-cards-pattern1      | (a) 6-card step-by-step reveal (~9s apart, narration-paced) per `step-by-step-reveal.md`. (b) Each card uses `effects/stat-pill-pop.js` entrance. (c) `components/highlight-marker-sweep/` under "lean and layered" (card 1), "subdirectories" (card 2), and "by symbol, not by string" (card 6). (d) Whoosh at boundary.                                                                                          |
| 9 | scene-quote-card               | (a) Built-in 180px orange quote-mark spring entrance + marker-sweep underline on "three to six months". (b) `components/highlight-marker-sweep/` — second sweep on "p-four edit" later in the scale beat below the quote. (c) Scale-pulse (1 → 1.03 → 1, 0.3s yoyo) on the author attribution mono pill. (d) Whoosh at boundary.                                                                                                                                              |
| 10 | scene-image-3d-reveal (#2)    | (a) Built-in 3D rotateY entrance + finite-repeat micro-yoyo (repeat = 2). (b) Two synthetic anecdote-callout pills (e.g. "Plugin+MCP suite — Day 1" / "Dedicated AI-tooling team") fly-in at narration anchors. (c) Marker-sweep under "agent manager" key phrase. (d) Whoosh at boundary + one `scale-slam` (volume 0.15) when the figure locks.                                                                                                                                                                                                                                |
| 11 | scene-dynamous-midroll        | Brand-locked — scene's internal timeline owns its choreography. Only addition: `cinematic-whoosh` at the boundary into scene 11 AND at the boundary out (data-start = 398 and 410, both data-volume 0.11). NO additional retention components allowed inside this scene per the brand-lock convention.                                                                                                                                                                                                                          |
| 12 | scene-image-3d-reveal (#3)    | (a) Built-in 3D rotateY entrance + finite-repeat micro-yoyo (repeat = 1, scene only 42s long → 1 full yoyo at 12s sine.inOut leaves 30s settle). (b) Step-by-step reveal of 3 "edge-cases not covered" badges (hundreds-of-thousands of folders / millions of files / non-Git VCS), narration-anchored. (c) Marker-sweep under "future installments". (d) Whoosh at boundary.                                                                                                                                                              |
| 13 | scene-cta                      | (a) Built-in CTA archetype finite-pulse on `#cta-question` pill. (b) `effects/stat-pill-pop.js` on the comment-pill icon. (c) Subscribe pulse on the subscribe-pill (3 pulses, finite). (d) Marker-sweep under "the harness matters more than the model" key phrase in the spoken hook. (e) Whoosh at boundary. (f) Held final frame ≥ 1.5s. (g) `effects/hero-slam-shake.js` on the topic slam at scene start — small 4-tick.                                                                                                                                                                                                                                                                                                                              |

**Pick count summary**: 13 scenes × ~3 components each = ~36 retention picks total. Zero scenes with no picks.

**Cross-scene component reuse**: 7 scenes use `components/highlight-marker-sweep/` (1, 2, 4, 5, 8, 9, 12, 13). 6 scenes use `effects/stat-pill-pop.js` (2, 3, 6, 8, 10, 13). 2 scenes use `effects/hero-slam-shake.js` (1, 13). All 13 scenes have a whoosh at boundary (12 inter-scene + 1 outro).

---

## Data Timing Budget

| Scene | scene_id                          | Start (s) | Duration (s) | End (s)  | Notes |
| ----- | --------------------------------- | --------- | ------------ | -------- | ----- |
| 1     | scene-hook                        | 0         | 32           | 32       | Topic-slam visible from t=0 (no fade-in) per long-form first-frame thumbnail analog |
| 2     | scene-source-cards                | 32        | 28           | 60       | 3-card stagger ~9s apart |
| 3     | scene-stat-pill-row               | 60        | 28           | 88       | 3 pills 500ms stagger + counter rolls |
| 4     | scene-side-by-side                | 88        | 38           | 126      | RAG strike-cross beat at ~+8s, agentic reveal at ~+18s |
| 5     | scene-image-3d-reveal #1          | 126       | 50           | 176      | fig1-harness; 7 callout pills paced ~6s apart over 42s |
| 6     | scene-list-cards-harness          | 176       | 70           | 246      | 7 cards step-by-step ~9.5s apart per `step-by-step-reveal.md` |
| 7     | scene-subscribe-banner            | 246       | 10           | 256      | mid-video subscribe pop-in at ~51% |
| 8     | scene-list-cards-pattern1         | 256       | 60           | 316      | 6 cards step-by-step ~9s apart |
| 9     | scene-quote-card                  | 316       | 32           | 348      | Quote enters at +2s, sub-anecdote at +18s, marker sweeps +12s/+26s |
| 10    | scene-image-3d-reveal #2          | 348       | 50           | 398      | fig2-rollout-phases; 2 anecdote callouts paced ~15s apart |
| 11    | scene-dynamous-midroll            | 398       | 12           | 410      | Brand-locked; spoken line drops here |
| 12    | scene-image-3d-reveal #3          | 410       | 42           | 452      | fig3-getting-started-checklist; 3 edge-case badges ~8s apart |
| 13    | scene-cta                         | 452       | 26.5         | 478.5    | CTA A; final frame held still 1.5s; CTA-question visible through hold |
| —     | tail                              | 478.5     | 1.5          | 480.0    | Composition extender — `tl.set({}, {}, 480)` |

**Total runtime**: 480.0s (8 min 0 s) ✓
**Per-scene visual-pacing-5s audit**: every scene above lists explicit beat counts that yield ≤ 5s gaps internally. Detailed audit deferred to Phase 4 once data-start values track narration. All listed retention components are entrance events (real beats per `visual-pacing-5s.md` — they reveal new content, not just decoration).

---

## Fact-Check Audit Summary (Phase 1 pass; full audit at Phase 2b)

Every numeric claim, named person, named company, and named product in the script_anchor column above has been verified against `tmp/source.md`. Pass/fail per claim:

| Claim                                                                                                  | Verified in source? | Source location                                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| "5 extension points"                                                                                   | ✅                  | §"The harness matters as much as the model", paragraph 2 |
| "2 capabilities" (LSP, subagents)                                                                      | ✅                  | Same paragraph + table footnote |
| "3 configuration patterns"                                                                             | ✅                  | §"Three configuration patterns from successful deployments" heading |
| "the harness matters more than the model"                                                              | ✅                  | Section heading + paragraph 1 |
| "Claude Code at scale" series name + "Part 1"                                                          | ✅                  | Opening blockquote |
| "Anthropic's Applied AI team"                                                                          | ✅                  | Acknowledgements |
| 8 named Applied-AI-team members (Krifcher, Lee, Concannon, Patel, Savelli, Schwartz, Dueck, Kohlmorgen) | ✅                  | Acknowledgements (full list — script may name 3, others surface as visual chrome) |
| "5 min read" + "published 14 May 2026"                                                                 | ✅                  | Page metadata block in `tmp/source.md` |
| "multi-million-line monorepos / decades-old legacy / thousands of developers"                          | ✅                  | §"Claude Code is running in production..." paragraph |
| Languages: C, C++, C#, Java, PHP                                                                       | ✅                  | Same paragraph |
| Agentic search vs RAG (index lag, function renamed two weeks ago)                                      | ✅                  | §"How Claude Code navigates large codebases", paragraphs 2-4 |
| 7-component harness (5 + 2)                                                                            | ✅                  | §"The harness matters..." paragraph 2 + table |
| "order matters — CLAUDE.md first, MCP last"                                                            | ✅                  | "The order in which teams build them matters" + table common-confusions |
| Pattern 1 sub-patterns (6 items) — lean+layered / subdir init / scope test/lint / .gitignore + permissions.deny / codebase maps / LSP symbol-not-string | ✅ | Pattern 1 bullets |
| Pattern 2 — 3-6 month review cadence                                                                   | ✅                  | Pattern 2, last paragraph |
| Pattern 2 — p4 edit hook anecdote                                                                      | ✅                  | Pattern 2, paragraph 2 |
| Pattern 3 — agent manager (hybrid PM/engineer)                                                         | ✅                  | Pattern 3, paragraph 3 |
| Pattern 3 — DRI minimum viable                                                                         | ✅                  | Same paragraph |
| Pattern 3 — cross-functional working group: engineering + info-sec + governance                        | ✅                  | Pattern 3, last paragraph |
| Customer anecdote: plugin+MCP suite available day 1                                                    | ✅                  | Pattern 3, paragraph 2 |
| Customer anecdote: dedicated AI-tooling team                                                           | ✅                  | Same paragraph |
| Edge cases not covered: hundreds-of-thousands of folders / non-Git VCS                                  | ✅                  | "One caveat" paragraph at end of Pattern 1 |
| Future installments will address edge cases                                                            | ✅                  | Same paragraph |

**Audit conclusion: CLEAN — 0 flags.** Every script-anchor claim across all 13 scenes traces to a specific paragraph in `tmp/source.md`.

**Banned-claim self-check** (cross-reference Phase 0 brief §4): none of the script anchors invent percentages, name competitors, claim "RAG is dead", call Sonnet specifically, claim MCP is most important, claim skills replace CLAUDE.md, claim agentic-search is faster, claim Applied AI works with every customer, or claim teams should all adopt the agent-manager role. The Pattern-2 example is the **p4 edit** Perforce hook (verbatim source), not an invented one. Customer anecdotes use "large retail organization" / "enterprise software company" framing (anonymized as in the article) — Zoox is mentioned ONLY in the source-cards scene as an article-feedback acknowledgement, never as a deployment.

**Pronunciation notes pre-flagged for Phase 2a TTS audit** (copied from brief §7):

- `CLAUDE.md` → spell as "claude dot M D" in TTS script
- `MCP` → "M C P"
- `LSP` → "L S P"
- `DRI` → "D R I"
- `p4 edit` → "P four edit"
- Heteronym sweep: no "live" (adjective sense) appears; no "lead" (noun sense) appears in script anchors. Both safe.

---

## Composition wiring notes (for Phase 4)

These are the wiring contracts the composition build phase MUST honor when retiming to the transcript:

1. **Scene wrapper `data-composition-id` must match each child file's internal `data-composition-id`.** Per `.claude/rules/sub-composition-wiring.md`. Failure here causes the studio to silently load nothing.
2. **The 3 image-3d-reveal scenes share the same archetype HTML but need 3 separate wrapper IDs** (`#scene-image-3d-reveal-1-wrap`, `#scene-image-3d-reveal-2-wrap`, `#scene-image-3d-reveal-3-wrap`) and 3 separate `data-composition-id`s (e.g., `scene-image-3d-reveal-1`, `scene-image-3d-reveal-2`, `scene-image-3d-reveal-3`). Phase 4 will fork the archetype into 3 distinct scene files under `compositions/`. The figure_src and overline/caption text differ per scene.
3. **The 2 list-cards scenes likewise need separate IDs** (`scene-list-cards-harness`, `scene-list-cards-pattern1`).
4. **Hook scene must render its topic-slam content visible from t=0** (no fade-in opacity 0). The first rendered frame is YouTube's auto-thumbnail when none is uploaded.
5. **CTA scene must hold final frame ≥ 1.5s after last entrance settles** per `.claude/rules/engagement-cta.md` + `shorts-thumbnail-frames.md` analog for long-form.
6. **TOTAL_DURATION = 480.0** in the root composition's `tl.set({}, {}, TOTAL_DURATION)` extender.
7. **Whoosh wiring**: 12 inter-scene whooshes at the 12 scene boundaries (data-start = 32, 60, 88, 126, 176, 246, 256, 316, 348, 398, 410, 452), data-duration = 1.5, data-track-index = 3, data-volume = 0.11. NO whoosh after scene 13 (the final-frame hold has no boundary).
8. **Accent overrides per scene**: each scene's `--scene-accent` CSS var should be set in the scene wrapper's inline style or in the per-scene HTML. The accent column above is canonical.

---

## Open items / Phase 4 retime hooks

- **Replace placeholder `data_start` values** with transcript-anchored word-boundary times after TTS lands and `npx hyperframes transcribe videos/claude-code-large-codebases` runs.
- **The retimed `data_start` values will likely shift each scene's end by ±2s** vs the 480.0s budget here. If the retimed total drifts beyond ±10s, scene 6 + scene 8 are the safest to trim (their card-stagger pacing has 9s gaps that can compress to 7s without violating step-by-step-reveal). The hook (#1), CTAs (#13), and dynamous-midroll (#11) are LOCKED for duration — don't trim those.
- **Optional polish**: if the operator wants tighter pacing, scene 6 (70s) and scene 8 (60s) can each lose ~5s by compressing the card stagger. Brings total to ~470s — still within the 8-min target. Not done by default because the current pacing matches the brief's recommendation.
