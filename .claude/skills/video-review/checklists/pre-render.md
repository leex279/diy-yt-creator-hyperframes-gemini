# Pre-render checklist

The smallest gate. Every BLOCKER must clear before invoking `npx hyperframes render`. HIGH/MEDIUM/LOW findings are advisory in this mode.

Invoked by: `/video-review <slug> --mode pre-render`

## Must pass (BLOCKER)

- [ ] `npx hyperframes lint videos/<slug>` returns 0 errors (warnings allowed)
- [ ] No `font-family: var(--sans|--mono)` in `videos/<slug>/**/*.html`
- [ ] Every `data-composition-src` parent ↔ child `data-composition-id` matches
- [ ] Every parent sub-comp mount has `class="clip"` + `data-start` + `data-track-index` + `data-width` + `data-height`
- [ ] Every `<video src="...">` source file exists at the referenced path
- [ ] Every `<audio src="...">` source file exists at the referenced path
- [ ] Composition duration ≥ narration.wav length (within 0.5s tolerance — extend with `tl.set({}, {}, TOTAL_DURATION)` if short)
- [ ] Every timed element has `class="clip"` + `data-start` + `data-duration` + `data-track-index` (audio/video elements may omit `class="clip"`)
- [ ] No unsourced numeric / dated / quoted claims in the script

## Sources

Each item above maps to a rule:

- Lint errors → `.claude/rules/hyperframes-pitfalls.md` (lint is authoritative for what it catches)
- Font-family blocker → `.claude/rules/hyperframes-pitfalls.md` §8
- Sub-comp wiring → `.claude/rules/sub-composition-wiring.md`
- Missing video/audio sources → `.claude/rules/hyperframes-pitfalls.md` §6 + lint `audio_src_not_found`
- Composition duration → `.claude/rules/hyperframes-pitfalls.md` §1
- Required clip attrs → `CLAUDE.md` Key Rules #1, #2
- No fabrication → memory `feedback_no_fabrication_source_only`

## Verdict mapping

| Outcome | Action |
|---------|--------|
| All BLOCKER items pass | Render is safe to invoke |
| Any BLOCKER fails | DO NOT render. Apply auto-fixes if available; otherwise fix manually and re-run review |

`pre-render` mode intentionally ignores HIGH findings — those are publish-quality, not render-correctness. Use `pre-publish` to gate publish.
