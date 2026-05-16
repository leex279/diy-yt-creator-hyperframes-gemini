# Severity rubric

How `video-review` agents grade findings.

## BLOCKER

Definition: the issue will either prevent successful render, produce a broken MP4, or violate a content rule the user has documented as hard (engagement CTA missing, fabricated claim, no YouTube description).

Examples:
- Render compiler errors (`font-family: var(--sans|--mono)`)
- Sub-composition `data-composition-id` mismatch (studio silently bails)
- Missing `<video>` source (45s FrameCapture timeout)
- Composition duration shorter than narration.wav
- Engagement CTA missing in any of 3 surfaces (spoken / on-screen / description)
- Banned CTA phrase in the closer ("What do you think?")
- Unsourced numeric/dated/quoted claim
- `youtube-description.md` missing
- Lint reports errors

Action: **DO NOT RENDER or PUBLISH.** Auto-fix where the recipe is deterministic; otherwise stop and ask.

## HIGH

Definition: the issue produces a video that renders successfully but is meaningfully worse than the channel's quality bar — viewers will notice, retention will drop, search will underperform.

Examples:
- Phase has a > 5.0s static gap
- Enumerated list of 4+ items revealed all at once
- `tl.from()` at t>5 without `tl.set` / `immediateRender: false`
- SFX-to-visual drift > 0.05s on a percussive cue
- Shorts text below typography minimum
- First or last frame fails the 5-element thumbnail-grade check
- Bar-chart marker overlay anti-pattern
- WCAG AA contrast failure
- Layout overflow
- Heteronym pronunciation risk in the spoken script
- CTA wording doesn't match across the 3 surfaces
- YouTube description structure violation (order, missing Dynamous/Hostinger block, wrong hashtag count)
- Chapter timestamps not adjusted for ffmpeg speedup
- URL returns 404

Action: **fix before publish.** Render is OK to invoke; rendered MP4 stays in `videos/<slug>/out/` while fixes land.

## MEDIUM

Definition: the issue is a quality improvement — fixing it makes the video noticeably better, but viewers may not consciously identify what's wrong.

Examples:
- Tech-term pronunciation risk (`npm` read as "nuh-pem")
- Card entrance not aligned to word anchor (drift 0.15-0.30s)
- Shape-backdrop doesn't rearrange on phase transition
- Oversized image (>2× canvas)
- Heavy backdrop-filter stack (>3 layers)
- Hook score 5-6 (not weak, not strong)
- Banned section in description (`Key Concepts`)
- vidIQ research artifact missing
- Forbidden `→` characters in description

Action: **reviewer's call.** Usually worth fixing if time allows; safe to ship if a deadline is real.

## LOW

Definition: minor polish or future-proofing. Won't be noticed by viewers; doesn't affect search or retention.

Examples:
- Narration speed drifts > 20% from expected (only matters if you forgot a speedup)
- Render filename uses `short.mp4` (only matters when multiple Shorts exist)
- Hostinger wording reads as "Sponsored" (mostly stylistic)
- HDR claim with no HDR source

Action: **note as follow-up.** Don't block ship; capture in `videos/<slug>/notes.md` if you want to come back.

---

## Cross-agent dedup

When two agents report the same `rule` at the same `location` (e.g., timing-pacer §8 and render-validator §8 both flag composition-duration-vs-narration), the orchestrator keeps the higher-severity report and discards the duplicate. If severities differ, the orchestrator uses the higher severity.

## Severity drift

A finding's severity can shift based on context:

- A WCAG AA failure on a 200ms-on-screen decorative pill → MEDIUM (not HIGH).
- A WCAG AA failure on the dominant hero word → BLOCKER (not HIGH).
- A 5.1s static gap that lands during a deliberate "breath" moment before a fade → MEDIUM (not HIGH) — but only when documented in `videos/<slug>/notes.md`.

Agents should default to the rubric above; orchestrator/user can override per finding.
