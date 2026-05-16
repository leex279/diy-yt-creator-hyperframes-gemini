# Anti-Slop Reference

The structural causes of "AI slop" in tech narration and the rules that prevent them. Layered on top of (NOT duplicating) the existing banned-phrase enforcement in `brand-voice-news-explainer.md` §B.1 and `faceless-tech-scriptwriting-playbook.md` §11.

This file is the methodology layer. The brand-voice files are the phrase-list layer. If you find yourself adding banned phrases here, add them to `brand-voice-news-explainer.md` instead — single source of truth.

---

## The three structural causes of slop

AI sounds like AI for three reasons. Each has a corresponding gate in this pipeline.

| Cause | What it looks like | Gate that prevents it |
|---|---|---|
| **Generality** — describing instead of arguing | "Claude Code makes developers more productive." | Phase 0 Thesis (QG-0I) + Phase 2.5 Pass 4 Arc 4 |
| **Unsourced authority** — "studies show", "experts agree" | "Most developers find that..." | Phase 0 Receipts (QG-0H) + Phase 2.5 Pass 5 (QG-4) authority-without-evidence ban |
| **Filler** — sentences that don't carry information | "Let's now look at why this matters." | Phase 2.5 Pass 7 JCRR audit (advisory) |

The three together cover the bulk of the failure modes. Banned-phrase lists catch surface-level slop ("delve into", "leverage", "game-changer"). Methodology gates catch deep slop — generic ideas wrapped in specific words.

---

## The Phase 0 Receipt Gate

**Where**: `phase0-research.md` Step 2H.3 (QG-0H).

**Rule**: Phase 1 cannot start until the brief has either:
- ≥ 3 named, linkable receipts (URL + version/date + one-line summary), OR
- Explicit `topic_type: CONCEPT` override for abstract topics with no public linkable artifacts

**Why this works**: Most slop happens when the model is asked to write about a topic it has no specific evidence for. With three real receipts in the brief, the model has nowhere to invent — it can either cite the receipt or stay quiet. Without receipts, "studies show 73%" becomes the path of least resistance.

**Receipt examples** (good — would pass):
- `https://www.anthropic.com/news/skills — 2025-10 — names the discovery + invocation mechanism`
- `https://github.com/anthropics/claude-code/releases/tag/v1.2.0 — 2025-10-14 — release notes confirming Skills shipped`
- Reddit thread with named developer reactions, e.g., `https://reddit.com/r/ClaudeAI/comments/abc123 — 2025-10 — community reaction to Skills launch`

**Not receipts** (would fail):
- "Industry consensus is that Skills are popular" — no URL, no source
- "Many developers have reported success" — generic, unverifiable
- A WebSearch snippet without a real underlying URL

**CONCEPT override** is for genuinely abstract topics (e.g., "What is RAG?", "What is a vector database?") that don't have one specific announcement to point at. CONCEPT does NOT relax the authority-without-evidence ban — Phase 2.5 Pass 5 still flags "experts agree" / "studies show" without inline source.

---

## The Falsifiable Thesis

**Where**: `phase0-research.md` Step 2H.2 (QG-0I), referenced in `phase2-script.md` Step 1.

**Rule**: Every brief must include a `## Thesis` section with one sentence that is:
- Falsifiable — could be wrong if the facts were different
- Argumentative — not descriptive

**Why this works**: Generic AI output describes; it almost never argues. A falsifiable thesis forces the script to take a position. The position can be wrong — that's the point. A wrong thesis can be debated and revised; a generic description is just noise.

**Bad theses** (descriptive — model can produce these without research):
- "Claude Code is a new AI coding tool."
- "The Anthropic-AWS deal is a major partnership."
- "Skills are useful for developers."

**Good theses** (falsifiable — the model can't produce these without specific evidence):
- "Claude Code's plan-first agent mode prevents the codebase damage that direct-edit agents cause — but only if the developer reads the plan before approving."
- "The Anthropic-AWS $100B deal is a hedge against Nvidia, not against capacity — Anthropic locked in non-Nvidia silicon before Nvidia's next-gen launch made the price spike permanent."
- "Skills aren't 'another extension system' — they're the first install mechanism that lets ChatGPT-grade prompt engineering ship as version-controlled artifacts in the repo, and the discovery surface stays silent so most CC users haven't noticed."

The good ones could each be wrong. That's why they're useful.

---

## The JCRR Line Test

**Where**: `phase2-5-critique.md` Pass 7 (advisory only).

Every sentence in narration should be one of four types. Sentences that are none of these are filler — delete them.

| Type | What it does | Example |
|---|---|---|
| **J** — Judgment | Your opinion or angle on the topic | "This is a bigger shift than most developers realize." |
| **C** — Claim | A verifiable factual statement | "The context window expanded from 200K to 1M tokens in v3." |
| **R** — Reason | Explains why a claim matters | "That means entire repos fit in a single session without truncation." |
| **R** — Receipt | Links the claim to its source (often inline attribution) | "The March 12th changelog lists this as the primary change." |

**Filler patterns** (Pass 7 flags these):
- Restatement: "In other words, what I'm saying is..."
- Meta-narration: "Let's now look at..." / "Now that we've covered X, let's move to Y."
- Empty transition: "But here's where it gets interesting..."
- Summary of the section just delivered: "So that's how X works."
- Vague amplifier with no information: "This is huge." / "This changes everything."

**Pass 7 thresholds** (advisory, NOT blocking):
- Flag any section with > 2 consecutive Filler sentences
- Report the overall percentage of JCRR vs. Filler across the script
- Per-scene breakdown where useful

**Why advisory, not blocking**: Sentence classification at scale tends to drift between LLM runs. Pass 7 produces a percentage that correlates with retention over time; once we have ship data showing the threshold matters, it can be promoted to blocking.

---

## The Specificity Ladder

**Where**: This is a writing principle, applied during Phase 2 script authoring. Phase 2.5 doesn't enforce it programmatically — it's caught by the JCRR audit and the existing audit-checklist D3 (Substance layer).

**Rule**: Every abstract claim must descend at least one specificity rung in the next sentence. Going Abstract → Specific → Evidence is ideal. Abstract → Abstract is slop.

```
Abstract:    "AI coding tools are improving."
Specific:    "Claude Code v1.3 reduced context window waste by running sub-agents per file."
Evidence:    "The March 2025 changelog PR shows 40% fewer tokens on a 50-file codebase."
```

You don't always need to reach the Evidence rung. But Abstract sentences that aren't followed by a Specific sentence within 1-2 lines are slop — the viewer's mental model didn't advance.

This is the same principle behind the audit-checklist D3 ("Substance layer") rule. The Specificity Ladder is the per-sentence operationalization.

---

## The 50% Deletion Rule

**Where**: This is a writing discipline, applied during Phase 2 self-review. Not enforced by a gate.

**Rule**: After drafting, delete at least 50% of the first draft. Targets for deletion:

- Sentences that restate the previous sentence in different words
- Sentences explaining why something matters instead of showing it
- Filler transitions ("Let's look at...", "Now that we've covered...")
- Multiple examples where one is sufficient
- Section-summary sentences ("So that's how X works.")

If a sentence does NOT add new information to the previous sentence, it goes. The reader (or TTS-listener) can already remember the prior sentence — restating it adds latency without adding signal.

This is hard to enforce automatically because "new information" is qualitative. The JCRR audit (Pass 7) is the closest programmatic proxy — Filler sentences are exactly the candidates for deletion.

---

## How this layers with existing infrastructure

This file does NOT duplicate phrase-level rules. The single source of truth for banned phrases is:

- `.claude/references/brand-voice-news-explainer.md` §B.1 — generic AI bans, hype bans, hedging bans, **Authority-Without-Evidence bans** (added with this anti-slop layer)
- `.claude/references/faceless-tech-scriptwriting-playbook.md` §11 — Critical / High / Medium phrase tables

Phase 2.5 Pass 5 (QG-4) reads both and BLOCKS the script if any Critical or High phrase appears. That gate already covers ~70% of the surface-level slop the playbook proposed adding.

What this file adds is the **methodology** that prevents slop from being generated in the first place:

| Phase | Anti-slop mechanism |
|---|---|
| Phase 0 | Receipt Gate (QG-0H) + Thesis (QG-0I) — prevents generation without evidence |
| Phase 2 | Read Thesis, bind receipts to scenes — script must argue the thesis, not describe |
| Phase 2.5 Pass 5 | Authority-Without-Evidence ban — catches "experts agree" / "studies show" |
| Phase 2.5 Pass 7 | JCRR audit (advisory) — catches Filler sentences QG-1..6 don't see |
| Phase 2b | Receipt cross-check — every per-scene Receipt URL must trace to the brief's Receipts list |

If a slop pattern leaks past all of these, that's the signal to extend brand-voice-news-explainer.md §B.1 — not to extend this file.

---

## When this file grows

Add a new section here when:

1. A new structural slop pattern is identified (something that's NOT a phrase-level miss)
2. A methodology rule needs documentation that doesn't fit phrase-list format
3. The receipt gate or thesis rule develops a new edge case worth recording

Do NOT add new banned phrases here — they belong in brand-voice-news-explainer.md §B.1.
