# Perfect-quality checklist

Maximum-strictness mode. Every finding at every severity is reported. Use when the goal is a video with zero defects — a hero release video, a sponsorship deliverable, a content piece you want to keep referencing for years.

Invoked by: `/video-review <slug> --mode perfect`

## All pre-publish items (must pass)

See `pre-publish.md` — every BLOCKER and HIGH finding from there is also gated in perfect mode.

## Additional items reported (MEDIUM + LOW)

### Pacing & timing

- [ ] Card entrances aligned to word anchors in `transcript.json` (drift ≤ 0.15s)
- [ ] Every `tl.from()` in long-form `compositions/scene-*.html` at position > 5s has `immediateRender: false`
- [ ] Pacing density ≥ 0.8 entrances per 5s across every phase

### Layout & readability

- [ ] Recommended typography sizes used (not just the minimums)
- [ ] No oversized source images (every image ≤ 2× canvas dimensions on each axis)
- [ ] No CSS has > 3 stacked `backdrop-filter` layers
- [ ] No `backdrop-filter: blur()` radius > 64px over a large region
- [ ] Visual screenshot pass run via `--visual` and every phase frame manually verified

### Script & content

- [ ] Hook score ≥ 7.0 on the four engagement-hooks-framework dimensions (curiosity gap, stakes clarity, specificity, visual-text-spoken alignment)
- [ ] Narration speed within ±20% of expected from script word count
- [ ] Every claim in the script has an inline reference to a research/ artifact

### YouTube metadata

- [ ] `videos/<slug>/research/vidiq-keywords.md` exists with documented seed terms + outliers + trending data
- [ ] First 200 chars match top 2-3 keywords from the vidIQ shortlist
- [ ] Every chapter title (long-form) is SEO-optimized: front-loaded keyword + number/proper noun where relevant
- [ ] No banned sections in description (`Key Concepts`, `Key Stats`, `About This Video`, etc.)
- [ ] No `→` or `->` arrow characters in description
- [ ] Title (if `meta.json.title` exists) ≤ 70 chars with keyword front-loaded

### Render correctness

- [ ] Render filename references use `<slug>.mp4`, not `short.mp4`
- [ ] If HDR delivery is documented, at least one source `<video>` has BT.2020/PQ/HLG color metadata
- [ ] `npx hyperframes lint` returns 0 warnings (not just 0 errors)

## Verdict mapping

| Outcome | Action |
|---------|--------|
| Everything passes | Ship it — this is the bar |
| Any LOW remains | Acceptable to ship if user agrees; capture as follow-up note in `videos/<slug>/notes.md` |
| Any MEDIUM remains | Reviewer's call — most warrant a fix before final render but none should block in an emergency |

Perfect-mode is intended for content that needs to age well or compete with the channel's best videos. For day-to-day video review, `pre-publish` is the right mode.
