---
name: engagement-hooks-framework
description: Engineer outstanding hooks and high-retention narration for video scripts using the Triple-Threat Hook (visual + text + spoken alignment), Violent Contrast (200-unit lean-and-snap), One-Question-Loop sentence flow, and Lego-Brick outlier deconstruction. Use when authoring or auditing scripts for diy-yt-creator videos (Phase 2 / Phase 2.5), when the user asks to "improve the hook", "make the intro stronger", "increase retention", "audit script engagement", "deconstruct outlier videos", or when an existing script feels slow, generic, or fails to stop the scroll. Complements (does NOT replace) phase2-script and phase2-5-critique.
---

# Engagement Hooks Framework

Engineer hooks and narration that earn the click AND hold attention. Distilled from the Faceless Creator's Master Blueprint, the Kallaway hook system, and 5 outlier-video transcript audits (TubeBuddy + Kallaway + Open Residency interview).

## Position in the pipeline

This skill is an **enhancement layer** on top of `/diy-yt-creator:phase2-script` and `/diy-yt-creator:phase2-5-critique`. The existing pipeline enforces voice rules, banned phrases, story arc, and CTA structure. This skill enforces what those gates don't catch: **whether the hook physically stops the scroll, whether each sentence pulls the next one in, and whether visual + text + spoken hook align as one weapon.**

Use this skill in three modes:

| Mode | When | Output |
|---|---|---|
| **Author** | Inside Phase 2 (Step 3) — writing the hook + first 60s | Hook block + opening narration that passes the audit |
| **Audit** | After Phase 2 / before Phase 2.5 — review a draft | Per-line audit report: which checks pass, which fail, suggested rewrites |
| **Deconstruct** | Before Phase 1 — analyze outlier reference videos | Lego-Brick deconstruction: which bricks held world-class, which need iteration |

## Workflow

### Mode 1: Authoring a hook + opening 60s

1. **Read the brief** — `videos/<slug>/research/content-brief.md` and `videos/<slug>/plan.md` (Phase 1 must be done).
2. **Pick the hook pattern** — read [`references/triple-threat-hook.md`](references/triple-threat-hook.md). Decide which of the 5 alignment patterns fits.
3. **Build the contrast spectrum** — read [`references/violent-contrast.md`](references/violent-contrast.md). Write the +100 anchor (common belief), then the -100 snap. Aim for the full 200-unit arc, not 100.
4. **Draft the spoken hook** as a chained sentence flow. Apply the One-Question-Loop pattern from [`references/one-question-loop.md`](references/one-question-loop.md) — every sentence raises the question the next sentence answers.
5. **Cue visual + text** — annotate `[VISUAL: ...]` and `[TEXT: ...]` inside the hook block. These get translated to composition markup later, but the alignment must be DESIGNED at script time, not retrofitted.
6. **Run the engagement audit** — use [`references/audit-checklist.md`](references/audit-checklist.md) to self-check before declaring done.

### Mode 2: Auditing an existing script

1. Read `videos/<slug>/scripts/full-script.md`.
2. Run the audit checklist in [`references/audit-checklist.md`](references/audit-checklist.md) — return a per-check PASS/FAIL with line citations.
3. For every FAIL, propose a concrete rewrite using the patterns in the relevant reference file.
4. Do NOT modify the script directly unless the user asks. Audit-mode produces a report; the user (or Phase 2) applies rewrites.

### Mode 3: Deconstructing outlier videos (pre-planning)

1. Identify 3-5 outlier videos in the niche (5x-10x channel average — use Sandcastles or vidIQ).
2. For each, fill the deconstruction template in [`references/lego-brick-deconstruction.md`](references/lego-brick-deconstruction.md).
3. Score each brick (Topic / Angle / Hook / Story / Visual / Audio / Format) on 1-10 vs. our last 3 videos.
4. Hold the world-class bricks (8+) constant. Iterate aggressively on the lacking ones (≤5).
5. Output: a "carry-forward" list that feeds Phase 1 plan generation.

## Reference files

Read only the file matching the current mode — keeps context lean.

- [`references/triple-threat-hook.md`](references/triple-threat-hook.md) — Visual + text + spoken alignment. Author mode.
- [`references/violent-contrast.md`](references/violent-contrast.md) — The 200-unit lean-and-snap technique with worked examples.
- [`references/one-question-loop.md`](references/one-question-loop.md) — Sentence-to-sentence flow rules.
- [`references/audit-checklist.md`](references/audit-checklist.md) — Engagement audit (Eyes-Closed Test, Two Dopamine Hits, density rules). Audit mode.
- [`references/lego-brick-deconstruction.md`](references/lego-brick-deconstruction.md) — Outlier-video deconstruction template. Deconstruct mode.
- [`references/winning-patterns.md`](references/winning-patterns.md) — Annotated hook patterns extracted from the 5 reference transcripts.

## Hard rules across all modes

1. **Never invent stats or facts.** This skill shapes narration; it does NOT generate claims. Every claim must trace to `videos/<slug>/research/content-brief.md` or `tmp/source.md`.
2. **Never override the brand-voice profile.** If `brand-voice-news-explainer.md` says "no em dashes in narration", this skill respects that. The engagement frame layers on top, never in conflict.
3. **Never replace `phase2-5-critique`.** This skill catches what the critique misses (scroll-stop force, sentence pull, hook alignment). The critique still runs.
4. **Hooks must work without sound.** ~85% of social-feed playback starts muted. Visual + text alignment is non-negotiable. If only the spoken hook lands, the video already lost.
5. **The hook is 0.0s to 4.0s, not "the first scene".** After 4s you're in proof / payoff territory, not hooking.
6. **Audit findings are advisory in autonomous mode.** When called from `/diy-yt-creator:full-auto`, output the audit report but do NOT block the pipeline — Phase 2.5 is the blocking authority.

## What this skill is NOT

- A replacement for `phase2-script.md` (it shapes the hook + first 60s, not the full script)
- A replacement for `phase2-5-critique.md` (it doesn't enforce banned phrases, voice profile, or CTA)
- A replacement for `phase1-plan.md` (it doesn't pick scenes / durations / retention components)
- A general writing-quality skill (it's tuned specifically for vertical short-form + faceless long-form on YouTube)

## When invoked from `/diy-yt-creator` commands

- Phase 2 (`phase2-script.md`) Step 3 should call this skill in **author mode** when building the hook variant.
- Phase 2.5 (`phase2-5-critique.md`) does NOT need to call this — it has its own scoring. But a writer can call this skill manually after Phase 2 lands a draft and before Phase 2.5 runs, as an additional quality gate.
- Phase 1 (`phase1-plan.md`) outlier-analysis step can call this skill in **deconstruct mode** when ≥3 reference videos exist in the brief.

## Self-improvement

When a hook ships and the video over- or under-performs vs. expectation:

1. Note which audit checks passed/failed at ship time.
2. Note actual retention curve at the 3s, 10s, 30s marks.
3. If a video with a "PASS" audit underperformed, the audit is missing a check — propose the new check and add it to `references/audit-checklist.md` with the failure-mode example.
4. If a video that violated a check overperformed, the check might be too strict — relax it with a note explaining why.

This skill grows from real ship-data, not theory.
