# Pre-publish checklist

The default review mode. Every BLOCKER and HIGH finding must clear before YouTube upload. MEDIUM and LOW are advisory but should be reviewed.

Invoked by: `/video-review <slug>` (default) or `/video-review <slug> --mode pre-publish`

## All pre-render items (must pass)

See `pre-render.md` — everything there is also a pre-publish gate.

## Additional must-pass items (HIGH)

### Pacing & timing

- [ ] No phase has a > 5.0s gap between consecutive entrance times AND between last entrance and phase exit (relaxations: opening hold ≤ 2.5s, closing hold ≤ 2.5s, ≤ 1.0s final-breath)
- [ ] Every enumerated list of 4+ items reveals one beat at a time with ≥ 3s stagger (not the `+0.7s` flourish stagger)
- [ ] Every `tl.from(target, { opacity: 0 }, t)` at `t > 5` has an explicit `tl.set(target, { opacity: 0 }, 0)` OR `immediateRender: false`
- [ ] Long-form scene-to-scene continuity: every scene's `data-start + data-duration` matches the next scene's `data-start` within ±0.5s (or has crossfade overlap)
- [ ] No track-index overlap on percussive SFX cues
- [ ] `cinematic-whoosh` data-duration = 1.5 (not 0.84)
- [ ] `cinematic-whoosh` fires at exact phase-transition sceneT (NOT sceneT - 0.4)
- [ ] SFX-to-visual drift ≤ 0.05s on percussive cues (impact-slam, scale-slam, screen-shake, spring-pop, pop, glitch-zap)
- [ ] SFX-to-visual drift ≤ 0.15s on non-percussive cues (whoosh, ambient)

### Layout & readability (Shorts only)

- [ ] All Shorts typography meets the per-role minimums from `.claude/rules/shorts-typography.md`
- [ ] First frame (t=0) is thumbnail-grade: topic ≥ 120px + visual anchor + brand chrome (logo ≥ 40px) + outcome ≥ 36px
- [ ] First frame is NOT black/empty/dark stage with only chrome (YouTube auto-thumbnail picks this)
- [ ] Last frame is thumbnail-grade: same 5 elements + ≥ 1.5s static hold + no trailing animations
- [ ] Last frame is NOT a solo CTA pill, fade-to-black, or brand-wordmark-alone
- [ ] No horizontal-bar marker overlays on source-screenshot bar charts (use marker-circles, pill-rows, scale-pulses, or stat-counters instead)
- [ ] Shape-backdrop rearranges on every phase transition (paired with cinematic-whoosh)
- [ ] WCAG AA contrast on headlines/body text
- [ ] No layout overflow on any element

### Script & content

- [ ] Heteronym audit clean (no risky `live`/`lead`/`read`/`close` adjective-vs-verb ambiguity in the spoken script)
- [ ] Tech-term pronunciation audit clean (TTS script uses `engine-x`, `A P I`, `dynamous dot AI`, etc.)
- [ ] Engagement CTA present in ALL 3 places:
  - Spoken closer (last 3-5s of narration) is a real debate question
  - `#cta-question` element in the LAST phase of `index.html`
  - Final paragraph of `youtube-description.md`
- [ ] All 3 CTAs reference the SAME claim (consistent wording across surfaces)
- [ ] No banned CTA phrases anywhere ("What do you think?", "Let me know in the comments", "Drop your thoughts below", "How would you build this differently?", etc.)
- [ ] Hostinger banner reads "Try Hostinger" / "Self-host" NOT "Sponsored by Hostinger"

### YouTube metadata

- [ ] `videos/<slug>/youtube-description.md` exists
- [ ] Structure order: SEO hook → `----` → Dynamous block → `----` → [Chapters for long-form] → Resources → `----` → Hostinger block → `----` → engagement question → hashtags
- [ ] Dynamous block PRESENT (mandatory on every video, independent of the `dynamousPromotion` meta flag which only gates on-screen promotion)
- [ ] Dynamous block exact format: `🚀` opener, BOTH URLs (`dynamous.ai/?code=646a60` AND `shorturl.smartcode.diy/dynamous_ai_10_percent_discount`), `👉` before the discount link, wrapped in `----` separators
- [ ] Hostinger block exact format (URL `/DIYSMARTCODE`, wrapped in `----` separators)
- [ ] Hashtag count is 15-25
- [ ] First 200 chars contain 2-3 target keywords (front-loaded, no generic hooks, no `→` arrows)
- [ ] Description CTA matches spoken + on-screen CTAs verbatim
- [ ] Long-form ONLY: Chapters section present, timestamps account for any `-<N>x.mp4` ffmpeg speedup (`data-start / speed_factor`)
- [ ] Shorts ONLY: NO Chapters section
- [ ] Every URL in description returns 200 (WebFetch validated)

## Verdict mapping

| Outcome | Action |
|---------|--------|
| All BLOCKER + HIGH pass | Ready to publish |
| Any BLOCKER fails | Same as pre-render: fix before render |
| Any HIGH fails | Address before upload — these are the differences between a good video and an outstanding one |
| Only MEDIUM/LOW | Reviewer's call; usually safe to ship and capture in a follow-up |
