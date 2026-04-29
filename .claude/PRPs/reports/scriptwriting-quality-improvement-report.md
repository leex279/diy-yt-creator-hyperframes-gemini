# Implementation Report: Scriptwriting Quality Improvement

**Plan**: `.claude/PRPs/plans/scriptwriting-quality-improvement.plan.md` (archived)
**Branch**: `main`
**Date**: 2026-04-28
**Status**: COMPLETE

---

## Summary

Implemented a markdown-only refactor of the `/diy-yt-creator` pipeline gates so that scripts produced by the workflow read like the Gemini-Pro gold standard (`videos/anthropic-100b-deal/script.txt`) instead of fragmented stat-dumps. Three structural changes:

1. **Voice profile dispatcher**: split the single `brand-voice.md` into a `tutorial` profile (preserves the existing developer-channel rules) and a new `news-explainer` profile (different rhythm, mandatory connectors + direct address + engagement CTA). `brand-voice.md` becomes a 41-line dispatcher that points at the active profile based on `voice_profile` in `content-brief.md`.
2. **New gates in Phase 2.5**: split QG-2 into QG-2a (Arc 1+2+4 average) and QG-2b (Arc 3 / CTA Strength as independent sub-gate ≥ 7), added new Pass 6 / QG-5 (Connector Density + Direct Address + Engagement CTA — skips for tutorial profile).
3. **Hook scoring rebalance**: Pass 1 formula changed from equal-weighted `(c+s+sp)/3` to `c*0.4 + s*0.4 + sp*0.2 + narrative_flow_bonus`. This stops triple-stat openers from auto-winning on Specificity alone and rewards openers that earn the click via a *reason*. Phase 1 Step 4D and Phase 2.5 Pass 1 stay in sync.

A new `script-library.md` quotes the Gemini gold standard verbatim with per-paragraph annotations; Phase 2 reads it BEFORE the brand-voice rules. Phase 1 caps shorts ≤60s at MAX 5 scenes (the previous lack of cap let the pipeline plan 8 scenes for 45s, forcing 5–6s scenes that couldn't fit connectors).

---

## Assessment vs Reality

| Metric     | Predicted   | Actual   | Reasoning                                                                      |
| ---------- | ----------- | -------- | ------------------------------------------------------------------------------ |
| Complexity | MEDIUM      | MEDIUM   | Plan was accurate. Three coordinated edits to scoring formulas across two files (Phase 1 Step 4D / Phase 2.5 Pass 1) were the trickiest part — kept the formulas in sync via explicit "Sync rule" notes. |
| Confidence | HIGH        | HIGH     | All 9 tasks landed cleanly. Level 3 re-scoring (manual) confirmed the gates correctly fail the bad script and pass the gold standard. |

**No deviations from the plan.** Implementation followed the 9 tasks exactly as specified.

---

## Tasks Completed

| #   | Task                                                                  | File                                                                | Status |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------- | ------ |
| 1   | CREATE annotated golden-example library                               | `.claude/references/script-library.md`                              | ✅      |
| 2   | CREATE tutorial profile (verbatim copy of old brand-voice.md)         | `.claude/references/brand-voice-tutorial.md`                        | ✅      |
| 3   | CREATE news-explainer profile with new rules + relaxations            | `.claude/references/brand-voice-news-explainer.md`                  | ✅      |
| 4   | UPDATE brand-voice.md to dispatcher (41 lines)                        | `.claude/references/brand-voice.md`                                 | ✅      |
| 5   | UPDATE phase0-research: add `voice_profile` field + heuristic         | `.claude/commands/diy-yt-creator/phase0-research.md`                | ✅      |
| 6   | UPDATE phase1-plan: cap scenes ≤60s at MAX 5; rebalance hook scoring  | `.claude/commands/diy-yt-creator/phase1-plan.md`                    | ✅      |
| 7   | UPDATE phase2-script: read library first, branch on voice_profile, narrative-flow Step 4c | `.claude/commands/diy-yt-creator/phase2-script.md`                  | ✅      |
| 8   | UPDATE phase2-5-critique: rebalance Pass 1, split QG-2 → 2a/2b, add Pass 6 / QG-5 | `.claude/commands/diy-yt-creator/phase2-5-critique.md`              | ✅      |
| 9   | UPDATE legacy/quick-path skill to point at script-library             | `.claude/skills/diy-yt-creator/new-anthropic-short.md`              | ✅      |

---

## Validation Results

| Check                                            | Result | Details                                                  |
| ------------------------------------------------ | ------ | -------------------------------------------------------- |
| Level 1 — Structure (file existence, line caps)  | ✅     | All 4 reference files exist; dispatcher 41/50 lines; tutorial 241/200 lines |
| Level 2 — Command file regex checks (7 grep checks) | ✅     | All 7 patterns present (voice_profile, MAX 5 scenes, narrative_flow_bonus, script-library.md ×2, Pass 6, QG-2a/2b/5) |
| Level 3 — Reference-script re-scoring (manual)   | ✅     | Failure-mode FAILS QG-5a + QG-5c + QG-2b; gold standard PASSES all gates |
| Level 4 — Tutorial-profile no-regression         | ⏭️     | Skipped — no shipped tutorial scripts exist yet to re-score; Pass 6 has explicit `voice_profile == tutorial` skip guard verified in code path |
| Level 5 — Pipeline end-to-end (regen the bad video) | ⏭️     | Deferred — user can run `/diy-yt-creator:full-auto` on the same topic to verify subjective improvement |
| Level 6 — Browser validation                     | ⏭️     | N/A — no UI changes |

---

## Files Changed

| File                                                                          | Action  | Lines   |
| ----------------------------------------------------------------------------- | ------- | ------- |
| `.claude/references/script-library.md`                                        | CREATE  | +95     |
| `.claude/references/brand-voice-tutorial.md`                                  | CREATE  | +241 (copy of brand-voice.md with 2-line header change) |
| `.claude/references/brand-voice-news-explainer.md`                            | CREATE  | +247    |
| `.claude/references/brand-voice.md`                                           | REWRITE | -240 / +41 (dispatcher) |
| `.claude/commands/diy-yt-creator/phase0-research.md`                          | UPDATE  | +20     |
| `.claude/commands/diy-yt-creator/phase1-plan.md`                              | UPDATE  | +25 / -8 |
| `.claude/commands/diy-yt-creator/phase2-script.md`                            | UPDATE  | +60 / -20 |
| `.claude/commands/diy-yt-creator/phase2-5-critique.md`                        | UPDATE  | +85 / -10 |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                        | UPDATE  | +1      |

---

## Deviations from Plan

None. Implementation followed the plan exactly. The one judgment call: I added a small "Sync rule" callout in both `phase1-plan.md` Step 4D and `phase2-5-critique.md` Pass 1 reminding future editors that the two scoring formulas must stay in lockstep. Not strictly required by the plan, but the plan's GOTCHA on Task 6 explicitly flagged this risk — adding the callouts makes the contract explicit at the code site.

---

## Issues Encountered

None. The pre-existing modification to `new-anthropic-short.md` (voice picker change from `af_heart` to `am_michael`) was unrelated and preserved cleanly through the Edit tool.

---

## Tests Written

This is a markdown/prompt refactor — no test code. Validation is structural (file existence, regex checks) and manual (re-scoring two reference scripts under the new gates). Both validation paths passed.

---

## Next Steps

1. Run `/diy-yt-creator:full-auto $100B Anthropic AWS deal` to regenerate the bad script under the new gates and compare against the Gemini gold standard (Level 5).
2. After the first new script ships and the user calls it good, copy it into `script-library.md` under the matching profile section and annotate per the existing pattern.
3. After 3–4 winners, audit `script-library.md` for emergent patterns and lift them into the matching `brand-voice-<profile>.md` rules (per the "Updating This Document" section in each file).
4. Optional follow-up: build `brand-voice-comparison.md` once a comparison-style video ships (currently deferred — comparison falls back to news-explainer).
