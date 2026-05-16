# Retention Strategy: claude-for-small-business

> **Update 2026-05-14 — Scene 7 split + Canva x-post integration**
> Scene 7 is now split into TWO visual halves backed by the same Anthropic-confirmation narrative:
> 1. **Article half (0 → ~3.5s of Phase 7)**: original article-hero screenshot with marker-circle on the May 13 date.
> 2. **Canva tweet half (~3.7 → 16s of Phase 7)**: animated x-post block customized for Canva's official @canva tweet confirming the partnership.
>
> The x-post block was installed via `npx hyperframes add x-post` and customized at `compositions/x-post.html` with: avatar wired to `assets/logos/canva-logo.png`, display name "Canva" with verified badge, handle "@canva", body matching the real tweet text, timestamp "3:58 PM · May 14, 2026", and engagement metrics (20 replies, 40 RTs, 295→296 likes on the in-card "like" beat, 25.9K views). Mounted via `data-composition-src` with `data-composition-id="x-post"` matching the child's internal id (per `.claude/rules/sub-composition-wiring.md`).
>
> **Why**: real social-proof signal — Anthropic announced + Canva publicly confirmed the partnership on X. Two-source receipt beats single-source receipt for trust + share-worthiness.
>
> **Narration / timing update**:
> - Scene 7 narration rewritten: "And this isn't a rumor. Anthropic announced it on May 13th. And Canva just confirmed the partnership on X. The receipts hold up. The customers do too."
> - `audio/narration.wav` regenerated → 142.24s, 358 words. `transcript.json` re-anchored.
> - narration-A.wav re-sliced: 0 → 64.249s (was 0 → 63.62s).
> - narration-B.wav re-sliced: tr_t 64.549 → end (duration 77.689s, was 77.51s).
> - **NEW comp_t formula for Scene 6-9 narration**: `comp_t = 99.273 + (tr_t - 64.549)` (was `98.62 + (tr_t - 64.549)`).
> - **NEW phase data-start values**: Scene 6 = **99.273** (was 106), Scene 7 = **117.273** (was 124), Scene 8 = **133.273** (was 140), Scene 9 = **155.273** (was 162). Composition end stays at exactly **180.0s**; Scene 9 terminal hold absorbed +0.6s drift (was ~14s, now ~24.7s of which last ~3.9s is narration-free thumbnail freeze).
> - **Scene 7 mid-split** = narration anchor "And Canva just confirmed" at tr_t 86.282 → comp_t **121.006** (Phase 7 t ≈ 3.73s). At that beat: article fades out, Canva x-post enters with `back.out(1.4)` scale entrance.

> **Time-anchor convention**: every retention pick lists both `transcript_t` (offset within `audio/narration.wav` — what `transcript.json` reports) AND `composition_t` (offset on the composition timeline that `index.html` wires via `data-start`). The conversion is `composition_t = transcript_t + 6.0` because Scene 1 is a 6-second silent thumbnail hold (`<audio id="narration">` starts at `data-start="6.0"` once wired).
>
> **Scene 5 clip-duck reality check** (load-bearing — composition build MUST handle): the script narration plays continuously transcript_t 0 → 141.85s, but Scene 5 visually inserts a 29s embedded YouTube companion-demo clip between the "Here's what it actually looks like." narration phrase (ends at transcript_t 63.62s) and the "Full demo's in the description." capper. **Recommendation**: split the single `audio/narration.wav` into TWO `<audio>` elements at composition build time:
> - `<audio id="narration-A">` — transcript 0–63.62s — wired at composition_t 6.0–69.62s.
> - 29s clip-duck where `assets/clips/anthropic-clip.mp4` plays at composition_t ≈ 69.62–98.62s with its own audio (or muted with caption pill).
> - `<audio id="narration-B">` — transcript 64.55–141.85s — wired at composition_t ≈ 98.62–175.92s.
>
> This means every anchor in Scenes 6–9 below lists composition_t assuming continuous playback (+6s offset only). Composition build MUST add `+29.0s` to every Scene 6–9 composition_t when wiring `data-start` on retention beats, OR slice narration and re-anchor relative to the post-clip narration segment start. The transcript_t and anchor_word_index values stay correct in both schemes — only the final `data-start` math changes.
>
> **Scene 9 nuance**: the transcript narration ends at transcript_t 141.85s ("community."). Scene 9 outro & terminal hold extend to composition_t 180s with no narration in the last ~4–5s — that hold is a static thumbnail freeze (intentional). The plan budgets `data_duration` 18s for Scene 9 — the final hold is held silence with the thumbnail-grade composition frozen on screen.

---

## Summary Table

| Scene | Pattern (from §7)                        | Primitives                                                                 | Captions                | Audio-Reactive | Transition Out  | Total Picks |
|-------|------------------------------------------|----------------------------------------------------------------------------|-------------------------|----------------|-----------------|-------------|
| 01    | `hero-slam` (modified — static thumbnail)| `gsap-stagger-grid` (fade-out only)                                        | none                    | none           | `blur-crossfade`| 2           |
| 02    | `hero-slam` (5-tab grid + slam-cut)      | `gsap-stagger-grid`, `marker-highlight` ×2                                 | `caption-fade-slide`    | none           | `blur-crossfade`| 5           |
| 03    | `stat-pill-row` + named-skill-chips-row  | `gsap-counter-tween` ×2, `gsap-stagger-grid`, `marker-highlight`           | none                    | none           | `blur-crossfade`| 5           |
| 04    | hub-spoke (custom)                       | `gsap-stagger-grid`, `gsap-path-draw`, `marker-highlight`                  | `caption-fade-slide`    | none           | `blur-crossfade`| 5           |
| 05    | video-frame-embed + thumbnail-pointer    | `gsap-stagger-grid`, `marker-highlight`                                    | `caption-fade-slide`    | none           | `blur-crossfade`| 4           |
| 06    | quote-card with chip-pop reveals         | `gsap-stagger-grid`, `marker-highlight`                                    | none                    | none           | `blur-crossfade`| 3           |
| 07    | screenshot-frame with marker callouts    | `gsap-stagger-grid`, `marker-circle`, `marker-highlight`                   | `caption-fade-slide`    | none           | `blur-crossfade`| 5           |
| 08    | logo-strip + trust-bullets + LT          | `gsap-stagger-grid`, `marker-highlight`                                    | none                    | none           | `blur-crossfade`| 3           |
| 09    | `cta-url-slam` + thumbnail-grade close   | `gsap-stagger-grid`, `marker-circle`                                       | none                    | none           | none (final)    | 3           |

**Primary transition**: `blur-crossfade` on 8 of 8 phase-to-phase transitions (100%). No accent transitions — shape-backdrop reposition + `cinematic-whoosh` SFX layered at every transition carry the variety per [`feedback_shape_rearrange_on_whoosh_default`](../../.claude/memory/...) and `audio-design.md`.

**Constraint tallies** (validated against `retention-components-hyperframes.md` §8):
- Max 2 markers per scene: ✅ all scenes ≤ 2 markers
- Caption groups overlap: ✅ none — captions only on Scenes 02, 04, 05, 07 and never overlapping
- Exit animations on non-final scenes: ✅ none — every transition handled by `blur-crossfade`
- One primary transition: ✅ `blur-crossfade` everywhere (100%)
- No equalizer / spectrum: ✅ no `audio-reactive-*` used (template defaults to no audio-reactivity on text in dark-stage Anthropic aesthetic)

---

## Scene-by-Scene Detail

### Scene 01: Thumbnail-Grade Hook Hold (data_start=0s, data_duration=6s)

**Words in scene**: 0 (silent thumbnail hold — no narration; YouTube auto-thumbnail picks frame 0)

**Anchor moments**:
- 0.0s — composition start. All thumbnail-grade elements at full opacity (`tl.set` at t=0). Required by [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md): topic statement ≥120px, visual anchor, brand chrome, outcome receipt all visible.
- 5.5s — fade-out begins (5.5→6.0s) as Scene 02 elements crossfade in.

**Picks**:
1. `gsap-stagger-grid` — **fade-out only** at composition_t 5.5–6.0s. Pattern: `tl.to([#s1-topic-slam, #s1-outcome, #s1-anthropic-mark], { opacity: 0, duration: 0.5, stagger: 0.05 }, 5.5)`. NO entrance animation — thumbnail elements are placed via `tl.set({}, {}, 0)` at full opacity to guarantee frame 0 is thumbnail-grade per [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md).
2. `blur-crossfade` to Scene 02 — composition_t 5.5–6.0s, `duration: 0.5s`, ease: `sine.inOut`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh        # phase transition
    anchor_word_index: null       # no narration in scene 1; anchor by scene boundary
    composition_data_start: 6.0   # fires AT the visual transition moment (T1) per audio-design.md HARD rule
    offset_seconds: 0
    duration_seconds: 1.5         # 1.5s exposure of full decay tail per audio-design.md
    track_index: 3
    volume: 0.11                  # cinematic-whoosh per audio-design.md
```

**Why these picks**: Scene 1 is a held thumbnail-grade still. [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) explicitly relaxes the 5s visual-pacing rule for this opening hold (≤2.5s; extended here to 5.5s because there is zero narration competing — flagged in `notes.md` per plan). The only pick is the fade-out at 5.5s (which counts as visual change for `visual-pacing-5s` — phase exit beat). No SFX beyond the whoosh on the transition out.

---

### Scene 02: The Sunday-Night Scramble (data_start=6s, data_duration=22s)

**Words in scene**: 53 (transcript indices 0–52, transcript_t 0.046 → 18.448s = composition_t 6.046 → 24.448s)

**Anchor moments**:
- transcript_t 0.046s (i=0) `"Every"` — composition_t **6.046s** — first word, narration entrance
- transcript_t 3.738s (i=12) `"make"` — composition_t **9.738s** — "will I make payroll?" key phrase
- transcript_t 4.887s (i=17) `"tabs."` — composition_t **10.887s** — five tabs slam ("You open five tabs.")
- transcript_t 6.30s (i=20) `"QuickBooks."`, (i=22) `"PayPal."`, (i=24) `"Gmail."`, (i=26) `"bank."`, (i=28) `"provider."` — tabs roll in
- transcript_t 12.921s (i=33) `"But"` — composition_t **18.921s** — **PIVOT WORD**
- transcript_t 13.522s (i=34) `"Anthropic"` — composition_t 19.522s — brand reveal
- transcript_t 15.568s (i=43) `"minutes."` — composition_t **21.568s** — receipt hook ("answers it in five minutes")

**Picks**:
1. **`caption-fade-slide`** for the whole scene — caption pill at y=1280 displays the spoken sentence in 3-5 word groups, fade-slide on each group's word start per transcript. Group breaks chosen on script comma/period boundaries.
2. **`gsap-stagger-grid`** on the 5 browser-tab icons — staggered entrance at composition_t **10.887, 12.0, 13.0, 14.0, 15.0s** (anchored to narration order `tabs / QuickBooks / PayPal / Gmail / bank / payroll`; spacing tight because narrator names them in 5s window per script).
3. **`marker-highlight`** ×1 (sweep-1) on the phrase **"will I make payroll?"** — `trigger_s`: composition_t **9.738s** (start of word `"make"`), `sweep_duration`: 0.5s, ease: `power2.out`.
4. **`marker-highlight`** ×2 (sweep-2) on the word **"five minutes"** — `trigger_s`: composition_t **21.0s** (just before "minutes" word at 21.568s — sweep leads the spoken receipt by ~0.5s for read-ahead), `sweep_duration`: 0.5s, ease: `power2.out`. ✅ Inside the 2-marker cap.
5. **`blur-crossfade`** to Scene 03 — composition_t 27.5–28.0s (after slam-cut completion).

**Slam-cut beat (PIVOT)**: at composition_t **18.921s** (word "But"), a slam-cut occurs: 5-tab cluster vanishes via `tl.set` to `opacity:0`, `/plan-payroll` 240px prompt slams in via `back.out(1.7)` over 0.4s. This is the open-loop resolution setup.

**visual-pacing-5s check** (composition_t):
- 6.046 (first word/caption fade) → 9.738 (sweep-1) = **3.7s** ✅
- 9.738 → 10.887 (tabs.) = **1.1s** ✅
- 10.887 → 12.0 (tab-2) → 13.0 → 14.0 → 15.0 = each **~1s** ✅
- 15.0 (last tab) → 18.921 (PIVOT) = **3.9s** ✅
- 18.921 → 21.0 (sweep-2) = **2.1s** ✅
- 21.0 → 21.568 (minutes word) → 24.448 (bundle. scene exit) = **3.4s** to exit ✅
All gaps ≤ 5s. ✅

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                      # tab-1 (QuickBooks) entrance
    anchor_word_index: 20         # "QuickBooks."
    composition_data_start: 10.887 # tied to "tabs." slam moment for percussive precision (i=17)
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # tab-2 (PayPal) entrance
    anchor_word_index: 22
    composition_data_start: 12.0   # spaced ~1s after tab-1; reuses track 3 (sequential, no overlap)
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # tab-3 (Gmail)
    anchor_word_index: 24
    composition_data_start: 13.0
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # tab-4 (bank)
    anchor_word_index: 26
    composition_data_start: 14.0
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # tab-5 (payroll provider)
    anchor_word_index: 28
    composition_data_start: 15.0
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: glitch-zap               # PIVOT word "But" — pivot accent
    anchor_word_index: 33         # "But"
    composition_data_start: 18.871 # leads spoken word by 0.05s (percussive within 0.05s cap)
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4                 # concurrent with layered impact-slam on slam-cut
    volume: 0.09
  - cue: impact-slam              # slam-cut to /plan-payroll prompt
    anchor_word_index: 33         # "But" pivot moment
    composition_data_start: 18.871
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 5                 # concurrent w/ glitch-zap on track 4
    volume: 0.15
  - cue: cinematic-whoosh         # phase transition
    anchor_word_index: null
    composition_data_start: 28.0   # T2 — visual transition moment
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3                 # whoosh sits alone on track 3 at this moment (pops have ended)
    volume: 0.11
```

**Why these picks**: Scene 2 is the loop-setup pain scene. The hero word/phrase to land is "will I make payroll?" (the unresolved question) — marker-highlight gives it the ink the narrator's voice doesn't. The slam-cut at "But" is the loop-opener pivot — needs layered SFX punctuation per the cinematic-hook plan (`impact-slam` + `glitch-zap`). The 5 tab pops are an enumerated list (per `step-by-step-reveal.md`) but narrated tight (5 names in 4s) so quick stagger is correct here. Caption-fade-slide reinforces narration so first-time viewers (typically 80%+ on Shorts) can follow without audio.

---

### Scene 03: The Reveal — 15 + 15 (data_start=28s, data_duration=24s)

**Words in scene**: 56 (transcript indices 53–108, transcript_t 19.760 → 42.756s = composition_t 25.760 → 48.756s)

> **Note**: transcript anchors run from t=19.76 → 42.76s but the plan budgets Scene 3 from composition_t 28 → 52. Narration actually starts crossing into Scene 3 territory at the word "bundle." (i=52, transcript_t 18.448 / composition_t 24.448). Scene boundary mismatch is ~3.5s — composition build will tighten the visual phase 3 to enter at composition_t 24.5 (when "bundle." lands) instead of 28. I'm anchoring the visual beats to the transcript word, not the plan's nominal 28s.

**Anchor moments**:
- transcript_t 18.448s (i=52) `"bundle."` — composition_t **24.448s** — scene 3 opens, first word
- transcript_t 19.760s (i=53) `"15"` — composition_t **25.760s** — **FIRST 15 number** (counter trigger)
- transcript_t 22.198s (i=58) `"reusable"` — composition_t **28.198s** — **SECOND 15 implicit** (skills counter trigger, narrator says "plus 15 reusable skills")
- transcript_t 27.398s (i=71) `"chaser."` — composition_t **33.398s** — chip 1 (invoice chaser)
- transcript_t 28.385s (i=73) `"analyzer."` — composition_t **34.385s** — chip 2 (margin analyzer)
- transcript_t 29.442s (i=75) `"prepper."` — composition_t **35.442s** — chip 3 (month-end prepper)
- transcript_t 31.346s (i=77) `"organizer."` — composition_t **37.346s** — chip 4 (tax-season organizer)
- transcript_t 32.437s (i=79) `"reviewer."` — composition_t **38.437s** — chip 5 (contract reviewer)
- transcript_t 34.027s (i=81) `"triager."` — composition_t **40.027s** — chip 6 (lead triager)
- transcript_t ~38–42s (i=85–105) closer phrase "the bundle is what's new, because the model was never the bottleneck"

**Picks**:
1. **`gsap-counter-tween`** on `#s3-workflows-counter` — tweens 0 → 15, `roundProps: "innerText"`. `tween_s_range`: composition_t **[25.26, 26.06]** (lead-in 0.5s before word `15` at 25.76, settle 0.3s after `15` ends at 25.76 + duration). Duration 0.8s, ease `power2.out`.
2. **`gsap-counter-tween`** on `#s3-skills-counter` — tweens 0 → 15. `tween_s_range`: composition_t **[27.70, 28.50]** (lead-in 0.5s before word `reusable` at 28.198). Duration 0.8s, ease `power2.out`.
3. **`marker-highlight`** ×1 — sweep under the dual-pill `15 + 15` row when both counters settle. `trigger_s`: composition_t **28.80s** (0.3s after skills counter settles), `sweep_duration`: 0.5s, ease `power2.out`. ✅ inside 2-marker cap.
4. **`gsap-stagger-grid`** on 6 skill chips — staggered entrance, one chip per `chaser/analyzer/prepper/organizer/reviewer/triager` word start:
   - chip-1 at composition_t **33.398s**
   - chip-2 at composition_t **34.385s**
   - chip-3 at composition_t **35.442s**
   - chip-4 at composition_t **37.346s**
   - chip-5 at composition_t **38.437s**
   - chip-6 at composition_t **40.027s**
   Each chip enters via `tl.set("#chip-N", {y: 30, opacity: 0, scale: 0.92}, 0); tl.to("#chip-N", {y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "back.out(1.5)"}, T_word_start)` per [`step-by-step-reveal.md`](../../.claude/rules/step-by-step-reveal.md) hidden-until-reveal pattern (required to prevent flash-at-frame-0).
5. **`blur-crossfade`** to Scene 04 — composition_t 51.5–52.0s, `duration: 0.5s`, ease `sine.inOut`.

**visual-pacing-5s check** (composition_t):
- 24.448 ("bundle." entrance) → 25.260 (counter-1 start) = **0.8s** ✅
- 25.260 → 27.70 (counter-2 start) = **2.4s** ✅
- 27.70 → 28.80 (marker sweep) = **1.1s** ✅
- 28.80 → 33.398 (chip-1) = **4.6s** ✅ (under 5s — script narrates the "plus 15 reusable skills, pre-built and wired" phrase here, no extra beats needed — narration carries this 4.6s gap)
- 33.398 → 34.385 → 35.442 → 37.346 → 38.437 → 40.027 = each **~1-2s** ✅
- 40.027 (chip-6) → 51.5 (scene exit / blur start) = **11.5s** ❌ **VIOLATION**
- **FIX**: insert (a) `marker-highlight` re-trigger on `#s3-bundle-pill` at composition_t 43.0s (during narration "the bundle is what's new") — but we're at the 2-marker cap already.
- **REVISED FIX**: scale-pulse + glow on `#s3-workflows-counter` + `#s3-skills-counter` together at composition_t 43.0s, then again at composition_t 47.5s. Per `visual-pacing-5s.md`, scale-pulse does NOT count as a content beat. Therefore:
- **CORRECTED FIX**: split the chip stagger to deliver content beats further apart. Push chip-4 (organizer) reveal to composition_t 38.5s, chip-5 to 41.0s, chip-6 to 43.5s — at the cost of mis-aligning narration. **NOT acceptable** — narration sync is the higher-priority rule.
- **FINAL FIX**: insert a 7th content beat — a `marker-highlight` accent under the closing phrase **"the model was never the bottleneck"** at composition_t **46.5s** (word "bottleneck" at i=104). This DOES exceed the 2-marker cap and so requires demoting one. **DEMOTE** the sweep-on-`15+15` pill (pick #3 above) to a non-marker `scale-pulse` (which is *visual emphasis* but not a marker per `screenshot-anchor-markers.md` exception list). The two real markers become: (a) `marker-highlight` on `chaser.` chip when it first lands (sweep accent, visible the moment it enters) ← this is already part of chip-1 styling — **NOT a separate marker pick**. Actually, the cleanest fix is to add a `marker-burst` on the closing phrase "never the bottleneck" — that is a different marker primitive on the 2-marker cap, so the cap becomes 2 (`marker-highlight` on `15+15` row + `marker-burst` on `bottleneck`).
- **APPLIED**: keep pick #3 marker-highlight on `15+15`, ADD a 6th pick:
6. **`marker-burst`** ×1 — radiating-lines burst from the word `"bottleneck"` (i=104, transcript_t 40.766s) at composition_t **46.766s**, `duration: 0.4s`. This is the third 5s gap-filler and the conceptual punchline. ✅ Inside 2-marker cap (1× `marker-highlight` + 1× `marker-burst` ≠ 3 markers; `marker-burst` is a distinct primitive, but cap is on total marker-* primitives — re-reading `retention-components-hyperframes.md` §1: "max 2 marker highlights per scene". Reading conservatively: 2 marker primitives per scene total. Therefore Scene 3 has exactly 2: marker-highlight + marker-burst. ✅).

Revised pick list (final): 1=counter-1, 2=counter-2, 3=marker-highlight, 4=stagger-grid chips, 5=blur-crossfade, 6=marker-burst.

**Revised visual-pacing-5s check** (composition_t):
- 40.027 (chip-6) → 43.0 (mid-narration "what's new") — no beat scheduled but: I can ADD a `scale-pulse` on the `#s3-15plus15-row` at composition_t 43.0s (NOT counted as beat per `visual-pacing-5s.md`). That alone fails the rule.
- 40.027 → 46.766 (marker-burst on "bottleneck") = **6.7s** ❌ still over.
- **FINAL applied fix**: word `i=98 "bolt"` at transcript_t 39.18s — wait, that's BEFORE chip-6. Let me re-anchor: i=84 word "what's" transcript_t 35.20s; i=88 word "model" transcript_t 36.31s ... actually narration "the bundle is what's new, because the model was never the bottleneck" runs from i=83 to i=108 — transcript_t ~34.5 to 42.7s. So in the gap composition_t 40 → 46.7, the narration phrase "the model was never the bottleneck" is being spoken. ADD a 7th beat: `marker-highlight` (re-skin pick #3) sweeps under the word `"model"` (i=88, transcript_t 36.31s, comp_t 42.31s) — actually that's INSIDE the chip stagger window. Wait, my chip times had chip-6 at 40.027s.
- **CLEAN FIX**: re-purpose the scale-pulse on counters — schedule a content-bearing `audio-reactive` swap. Drop the scale-pulse idea. Instead: ADD a new caption pill **"the bundle ≠ a new model"** entrance at composition_t **43.5s** during the "the bundle is what's new" narration. This is a NEW content element (caption pill = step-by-step-reveal content), reveals during the closing narration phrase, and bridges the gap. Pick #7: caption pill content beat.

**ACCEPTED final picks**:
1. `gsap-counter-tween` workflows → 15 (composition_t 25.26–26.06s)
2. `gsap-counter-tween` skills → 15 (composition_t 27.70–28.50s)
3. `marker-highlight` on `15 + 15` row (composition_t 28.80s, 0.5s sweep)
4. `gsap-stagger-grid` on 6 skill chips (composition_t 33.398–40.027s, narration-anchored)
5. New content beat — `#s3-bundle-thesis-pill` ("the bundle ≠ a new model") fades in at composition_t **43.5s** during "the bundle is what's new" narration (transcript_t 37.5–38s). Bridges the 4s gap from chip-6 to scene exit.
6. `marker-burst` on **"bottleneck"** at composition_t **46.766s**, duration 0.4s. ✅ 2nd marker primitive.
7. `blur-crossfade` to Scene 04 — composition_t 51.5–52.0s.

**Re-validated visual-pacing-5s** (composition_t):
- 24.448 → 25.26 → 27.70 → 28.80 → 33.398 → 34.385 → 35.442 → 37.346 → 38.437 → 40.027 → 43.5 → 46.766 → 51.5
- Max gap: 40.027 → 43.5 = **3.5s** ✅, 43.5 → 46.766 = **3.3s** ✅, 46.766 → 51.5 = **4.7s** ✅. **ALL CLEAR.**

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam               # workflows counter slam to 15
    anchor_word_index: 53         # "15"
    composition_data_start: 25.710 # word.start 25.760 minus 0.05 lead-in (percussive)
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: scale-slam               # skills counter slam to 15
    anchor_word_index: 58         # "reusable" (proxy for spoken "15 reusable skills")
    composition_data_start: 28.148 # word.start 28.198 minus 0.05 lead-in
    offset_seconds: -0.05
    duration_seconds: 0.73
    track_index: 3                 # sequential (>2s after track-3 prior cue) — reusable
    volume: 0.15
  - cue: spring-pop               # chip 1 — invoice chaser
    anchor_word_index: 71         # "chaser."
    composition_data_start: 33.398
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 2 — margin analyzer
    anchor_word_index: 73
    composition_data_start: 34.385
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 3 — month-end prepper
    anchor_word_index: 75
    composition_data_start: 35.442
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 4 — tax-season organizer
    anchor_word_index: 77
    composition_data_start: 37.346
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 5 — contract reviewer
    anchor_word_index: 79
    composition_data_start: 38.437
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 6 — lead triager
    anchor_word_index: 81
    composition_data_start: 40.027
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: impact-slam              # marker-burst on "bottleneck" — punchline punctuation
    anchor_word_index: 104        # "bottleneck"
    composition_data_start: 46.716 # word.start 46.766 minus 0.05 lead-in
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh         # T3 transition
    anchor_word_index: null
    composition_data_start: 52.0
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 3 is the structural reveal of the video's term-brand ("15 + 15 bundle"). The dual-counter-tween IS the visual receipt — `gsap-counter-tween` is the canonical pick for narrator-said-number-aloud moments per §9 quick lookup. Six skill chips enumerated tight need `gsap-stagger-grid` anchored to the spoken word per [`step-by-step-reveal.md`](../../.claude/rules/step-by-step-reveal.md). The `marker-burst` on `"bottleneck"` punctuates the conceptual reframe ("the model was never the bottleneck — the *bundle* was missing"). Added bundle-thesis pill bridges the 5s gap from chip-6 to scene exit per [`visual-pacing-5s.md`](../../.claude/rules/visual-pacing-5s.md).

---

### Scene 04: Integration Constellation (data_start=52s, data_duration=22s)

**Words in scene**: 51 (transcript indices 109–159, transcript_t 43.280 → 60.860s = composition_t 49.280 → 66.860s)

> Same plan↔transcript mismatch as Scene 3 — composition build will tighten visual phase 4 to enter at composition_t ~49.3 instead of 52.

**Anchor moments**:
- transcript_t 43.280s (i=109) `"QuickBooks,"` — composition_t **49.280s** — logo 1
- transcript_t 44.070s (i=110) `"PayPal,"` — composition_t **50.070s** — logo 2
- transcript_t 44.592s (i=111) `"HubSpot,"` — composition_t **50.592s** — logo 3
- transcript_t 45.103s (i=112) `"Canva,"` — composition_t **51.103s** — logo 4
- transcript_t 45.602s (i=113) `"DocuSign,"` — composition_t **51.602s** — logo 5
- transcript_t 46.589s (i=115) `"Workspace,"` — composition_t **52.589s** — logo 6 (Google Workspace)
- transcript_t 48.110s (i=118) `"365."` — composition_t **54.110s** — logo 7 (Microsoft 365)
- transcript_t 49.93s (i=119) `"HubSpot"` (second mention) — composition_t **55.93s** — "first CRM connector" callout setup
- transcript_t 50.943s (i=123) `"first"` — composition_t **56.943s** — "first CRM connector for Claude" key claim
- transcript_t 54.04s (i=132) `"ever"` — composition_t **60.04s** — "If you've ever tried" rhetorical bridge to next scene

**Picks**:
1. **`gsap-stagger-grid`** on 7 integration logos orbiting central Claude mark — each logo enters anchored to its spoken word:
   - QuickBooks at composition_t **49.280s**
   - PayPal at composition_t **50.070s**
   - HubSpot at composition_t **50.592s**
   - Canva at composition_t **51.103s**
   - DocuSign at composition_t **51.602s**
   - GW at composition_t **52.589s**
   - MS365 at composition_t **54.110s**
   Hidden-until-reveal pattern per [`step-by-step-reveal.md`](../../.claude/rules/step-by-step-reveal.md): `tl.set("#logo-N", {scale: 0.6, opacity: 0, x: 0, y: 0}, 0)` then `tl.to(...)` to settle at orbit position. Use `back.out(1.4)` for the settle.
2. **`gsap-path-draw`** on 7 SVG glowing edges connecting each logo to the central Claude mark — each edge animates `strokeDashoffset` over 0.4s, triggered +0.3s after each logo settles. So edge-1 starts at composition_t **49.680s**, edge-2 at 50.470s, etc.
3. **`marker-highlight`** ×1 — sweep under the caption pill "first CRM connector for Claude" when it enters. `trigger_s`: composition_t **56.943s** (word `first`), `sweep_duration`: 0.5s, ease `power2.out`.
4. **`caption-fade-slide`** caption pill `#s4-caption-crm` — text "first CRM connector for Claude" enters at composition_t **56.443s** (0.5s lead-in before the spoken word "first" lands), fades out at composition_t **60.0s**.
5. **`blur-crossfade`** to Scene 05 — composition_t 73.5–74.0s.

**Scene closing beat**: at composition_t **60.04s** (word "ever"), narration says "If you've ever tried to run an SMB with a generic chatbot that can't see your books, this is the difference." — VISUAL accompaniment: a brief 0.4s `scale-pulse` on the central Claude mark + a synthetic dotted-line crossout over a `#s4-generic-chatbot-ghost` strawman element (faint gray ghost label) that fades in at composition_t 60.5s and is struck through at 62.5s. This is the negative-framing visual lock (per [`story-locks.md`](../../.claude/references/story-locks.md) Lock #4). Not counted as marker — uses `strike-cross` SFX cue.

**visual-pacing-5s check** (composition_t):
- 49.280 → 50.070 → 50.592 → 51.103 → 51.602 → 52.589 → 54.110 — all ≤ 1.5s ✅
- 54.110 (last logo) → 56.443 (caption pill enters) = **2.3s** ✅
- 56.443 → 56.943 (marker sweep) = **0.5s** ✅
- 56.943 → 60.04 (negative-frame pulse + ghost element enters) = **3.1s** ✅
- 60.04 → 60.5 (ghost element) → 62.5 (strike-cross) → 66.86 (scene narration end) → 73.5 (exit) = max gap 62.5→66.86 = **4.4s** ✅
- 66.86 → 73.5 = **6.6s** ❌ — narration ends at 66.86 but scene continues until 74.0. **FIX**: composition build will shrink Scene 4 visual phase to exit at composition_t ~67.5–68.0 (immediately after narration ends, blur-crossfade to Scene 5 framing). The plan's nominal 52→74 scene boundaries reflect a slower-narration assumption; actual narration runs faster.

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                      # logo 1 QuickBooks
    anchor_word_index: 109
    composition_data_start: 49.280
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 2 PayPal
    anchor_word_index: 110
    composition_data_start: 50.070
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 3 HubSpot
    anchor_word_index: 111
    composition_data_start: 50.592
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 4 Canva
    anchor_word_index: 112
    composition_data_start: 51.103
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 5 DocuSign
    anchor_word_index: 113
    composition_data_start: 51.602
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 6 Google Workspace
    anchor_word_index: 115
    composition_data_start: 52.589
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # logo 7 Microsoft 365
    anchor_word_index: 118
    composition_data_start: 54.110
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: strike-cross             # generic-chatbot ghost crossout
    anchor_word_index: 132         # "ever" — proxy for "generic chatbot that can't see"
    composition_data_start: 62.5
    offset_seconds: 0
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh         # T4 transition
    anchor_word_index: null
    composition_data_start: 68.0   # actual visual exit (narration done at 66.86)
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 4 demonstrates the "integration constellation" — partner logos with edges drawn to a central Claude mark IS the visual receipt of "these workflows live INSIDE these tools, not bolted on." `gsap-path-draw` is the canonical pick for hand-drawn connector flows (per §5). The marker-highlight on "first CRM connector" amplifies a specific stat the script wants the viewer to hold (HubSpot's verifiable first-party claim, per Phase 2b fact-check). The `strike-cross` on the generic-chatbot ghost executes the Negative Frame story lock — concrete "what Claude is NOT" before "what Claude IS."

---

### Scene 05: The Companion Demo (data_start=74s, data_duration=32s)

**Words in scene**: 11 (transcript indices 154–164, transcript_t 60.34 → 64.55s)

> **MOST COMPLEX SCENE** — clip-duck mechanics. Narration runs only 4 seconds across this 32-second scene; the rest is the embedded YT clip playing with its own audio.

**Anchor moments (narration audio)**:
- transcript_t 60.34s (i=154) `"Here's"` — composition_t **66.34s** — opening clause
- transcript_t 61.298s (i=157) `"looks"` — composition_t **67.298s** — "what it actually looks like" — marker target
- transcript_t 62.55s (i=159) `"like."` — composition_t **68.55s** — end of opening clause
- **[PAUSE in script]** → ~5s of narration silence
- transcript_t 62.69s (i=160) `"Full"` — composition_t **68.69s** — start of capper
- transcript_t 63.063s (i=163) `"description."` — composition_t **69.063s** — end of capper, then **29s clip plays**

> **Clip-duck mechanics for composition build**:
> The narration.wav as transcribed has NO 29s gap — the script's `[PAUSE]` was respected by ElevenLabs as ~1-2s of breath, not 29s of silence. The 29s clip must be inserted by:
> - **Option A**: Splitting `narration.wav` into `narration-A.wav` (transcript 0–63.62s, transcript_t before "description.") + `narration-B.wav` (transcript 64.55s onward, starting with "Because"). Use `ffmpeg -i narration.wav -t 63.62 narration-A.wav && ffmpeg -i narration.wav -ss 64.55 narration-B.wav`. Wire as two `<audio>` elements with `data-start` 6.0 (A) and 98.62 (B). Clip plays composition_t 69.62–98.62 with own audio at duck-volume 0.45 or muted with caption.
> - **Option B**: Mute the 29s narration overlap (use `data-volume="0"` on the relevant `<audio>` window) — not supported by HyperFrames per `audio-design.md` (no per-frame volume), so **Option A is mandatory**.

**Picks**:
1. **`gsap-stagger-grid`** on frame chrome — orange border-glow rectangle + caption pill enter at composition_t **66.0s** and **66.5s** (stagger 0.5s). Hidden-until-reveal pattern.
2. **`caption-fade-slide`** caption pill `#s5-cap-actually` — text "what it actually looks like →" enters at composition_t **66.50s**, fades out at composition_t **69.62s** (just before clip plays). Position above the video frame.
3. **`marker-highlight`** ×1 — sweep under the word `"actually"` in the caption pill. `trigger_s`: composition_t **66.798s** (0.5s before spoken `looks` at 67.298s — sweep leads narration by ~0.5s for read-ahead emphasis), `sweep_duration`: 0.4s, ease `power2.out`.
4. **Video frame embed** — `<video>` element wrapped in a div per `hyperframes-pitfalls.md` (never animate `<video>` dimensions directly). Wrapper at composition_t 69.62s loads `assets/clips/anthropic-clip.mp4` and plays for 29s (until composition_t 98.62s). Frame border glow pulses subtly via `audio-reactive-glow`? — **NO**, `audio-design.md` and the Anthropic template disallow audio-reactivity on text in the dark-stage aesthetic, AND the clip has its own audio that would drive the reactivity in ways that conflict with the rest of the composition. **APPLY**: a deterministic 4s `gsap.to` loop on the border-glow `box-shadow` color cycling subtly orange→amber→orange — counts as ambient persistence, not a content beat.
5. **Pointer card** — `#s5-pointer-card` ("Full demo: link in description") enters at composition_t **98.62s** (just as clip ends and narration-B begins with "Because" at composition_t 70.55 + 29 = **99.55s**). Hidden-until-reveal: `tl.set({opacity: 0, y: 30}, 0); tl.to({opacity: 1, y: 0, duration: 0.4}, 98.62)`. Held until composition_t 105.5s, then `blur-crossfade` to Scene 06 at composition_t 106.0s.
6. **`blur-crossfade`** to Scene 06 — composition_t 105.5–106.0s.

**visual-pacing-5s check** (composition_t):
- 66.0 (frame chrome) → 66.5 (caption pill) → 66.798 (marker sweep) → 67.298 (spoken `looks`) → 69.62 (clip starts) — all ≤ 3s ✅
- **CLIP PLAYS 69.62–98.62** = 29s of continuous video motion. Per [`visual-pacing-5s.md`](../../.claude/rules/visual-pacing-5s.md), a video element with rendered frames changing counts as visible foreground motion — NOT static. ✅
- 98.62 (pointer card enters) → 99.55 ("Because" narration resumes — start of Scene 6) = **0.9s** ✅
- The 29s clip itself: no marker callouts on the clip per [`screenshot-anchor-markers.md`](../../.claude/rules/screenshot-anchor-markers.md) (the clip is a real first-party screencast — synthetic overlays compete with its own UI).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh         # frame chrome entrance
    anchor_word_index: null
    composition_data_start: 66.0
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh         # T5 — clip-end / narration-B handoff
    anchor_word_index: null
    composition_data_start: 98.62  # clip ends, narration-B about to start
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
  # NOTE: NO SFX during the 29s clip — the clip carries its own audio at duck-volume.
  # NOTE: composition build MUST verify the clip's audio doesn't peak louder than narration
  # peak (~-6 dBFS). Use ffmpeg loudnorm or set clip <audio data-volume="0.45"> if needed.
```

**Why these picks**: Scene 5 is the loop-resolution payoff scene. The viewer who heard "will I make payroll?" 60s ago now sees the workflow do it in real time. The frame-chrome + caption pill prep the viewer's attention BEFORE the clip plays, so they understand what they're looking at without re-listening. The marker-sweep on `actually` reinforces the "this is the receipt, not a marketing render" framing. The 29s clip is the longest single-beat in the composition but is acceptable per `visual-pacing-5s.md` because the clip itself has continuous motion.

---

### Scene 06: The Lina Ochman Quote (data_start=106s, data_duration=18s)

> **Post-clip composition time offset**: every composition_t below assumes continuous narration. After Scene 5's 29s clip-duck insertion, **add +29s to every composition_t** when wiring `data-start` in `index.html`. Transcript_t and anchor_word_index are correct as-is.

**Words in scene**: 38 (transcript indices 164–201, transcript_t 64.549 → 78.596s = continuous composition_t 70.549 → 84.596s, **post-clip composition_t ≈ 99.55 → 113.60s**)

**Anchor moments** (transcript_t / continuous composition_t / post-clip composition_t):
- i=164 `"Because"` — tr_t 64.549 / cont 70.549 / **post-clip 99.55s** — scene 6 opens, loop opener
- i=170 `"500."` — tr_t 67.0 / **post-clip ≈101.97** — "Fortune 500" pivot phrase
- i=171 `"Lina"` — tr_t 67.27 / **post-clip ≈102.27**
- i=173 `"Ochman"` — tr_t 67.846 / **post-clip ≈102.85** — attribution
- i=189 `"15-person"` — tr_t 72.908 / **post-clip ≈107.91** — HVAC chip
- i=190 `"H"` (i=191 `V`, i=192 `A`, i=193 `C`) — H V A C spelled
- i=198 `"30-person"` — tr_t 75.381 / **post-clip ≈110.38** — landscaper chip
- i=203 `"50-person"` — tr_t 78.051 / **post-clip ≈113.05** — brokerage chip
- i=208 `"now."` — tr_t 80.954 / **post-clip ≈115.95** — "Until now" rhetorical peak

**Picks**:
1. **`gsap-stagger-grid`** on quote-card structural elements + 3 chips:
   - Quote-card frame at post-clip composition_t **99.55s** (scene 6 entry)
   - Quote text fades in at **100.5s**
   - Attribution row (Lina Ochman + Anthropic mark + role) at **102.85s** (anchored to spoken word `"Ochman"`)
   - Chip-1 (HVAC) at **107.91s** (anchored to `"15-person"`)
   - Chip-2 (landscaper) at **110.38s** (anchored to `"30-person"`)
   - Chip-3 (brokerage) at **113.05s** (anchored to `"50-person"`)
   Hidden-until-reveal: each chip `tl.set({y: 30, opacity: 0, scale: 0.92}, 0); tl.to(...)` at its word.
2. **`marker-highlight`** ×1 — sweep under the recurring phrase "Not for" (or under each "Not for the N-person …" line via sequential markers). Apply ONE sweep on the FIRST "Not for" instance — word "Not" at i=187 (preceding `"15-person"`), tr_t ~72.3 / **post-clip ≈ 107.3s**, sweep_duration: 0.5s. The pattern is conveyed by chip stagger; one marker is enough.
3. **`blur-crossfade`** to Scene 07 — composition_t (post-clip) **116.45–117.0s**.

**Scene closing beat** at "Until now" (word i=208, post-clip composition_t ≈ 115.95s): brief 0.5s `scale-pulse` on the entire quote-card (1.0 → 1.04 → 1.0) — emphasis without adding a marker. This is the rhetorical peak that sets up Scene 7's article-screenshot proof.

**visual-pacing-5s check** (post-clip composition_t):
- 99.55 (frame) → 100.5 (quote text) = **0.95s** ✅
- 100.5 → 102.85 (attribution) = **2.4s** ✅
- 102.85 → 107.3 (marker sweep) = **4.5s** ✅
- 107.3 → 107.91 (chip-1) = **0.6s** ✅
- 107.91 → 110.38 (chip-2) = **2.5s** ✅
- 110.38 → 113.05 (chip-3) = **2.7s** ✅
- 113.05 → 115.95 (until-now scale-pulse) = **2.9s** ✅
- 115.95 → 116.45 (exit) = **0.5s** ✅
**All ≤ 5s.** ✅

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # chip 1 — 15-person HVAC
    anchor_word_index: 189
    composition_data_start: 107.91  # post-clip composition_t (continuous = 78.908; add +29 for clip-duck)
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 2 — 30-person landscaper
    anchor_word_index: 198
    composition_data_start: 110.38
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # chip 3 — 50-person brokerage
    anchor_word_index: 203
    composition_data_start: 113.05
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh         # T6 transition
    anchor_word_index: null
    composition_data_start: 117.0
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 6 cements the "not Fortune 500" positioning. Quote-card with chip-pop reveals is the canonical pattern for "this is the receipt + here are the three specific examples that anchor it." Chips named by the spoken size (15/30/50-person) per [`step-by-step-reveal.md`](../../.claude/rules/step-by-step-reveal.md) so the viewer sees each example land as the narrator names it. ONE marker on "Not for" (the negative-framing trigger) is sufficient — the chip pattern carries the rest. `scale-pulse` on "Until now" is the rhetorical peak transition into Scene 7's proof.

---

### Scene 07: The Article Screenshot Proof (data_start=124s, data_duration=16s)

**Words in scene**: 39 (transcript indices 209–247, transcript_t 81.4 → 95.36s, **post-clip composition_t ≈ 116.4 → 130.4s**)

**Anchor moments** (post-clip composition_t):
- i=209 `"And"` / i=212 `"isn't"` — scene opens "And this isn't a rumor"
- i=213 `"rumor."` — tr_t 82.382 / **post-clip ≈ 117.38s** — first key claim
- i=219 `"May"` / i=220 `"13th,"` — tr_t 84.74 / **post-clip ≈ 119.74s** — **DATE for marker-circle**
- i=222 `"Claude"` / i=223 `"Cowork,"` — tr_t 85.9 / **post-clip ≈ 120.9s** — product name
- i=232 `"receipts"` — tr_t 89.5 / **post-clip ≈ 124.5s** — "the receipts hold up" callback

**Picks**:
1. **`gsap-stagger-grid`** — screenshot frame enters at post-clip composition_t **117.0s** (0.5s fade-in), caption pill `#s7-cap-source` ("Anthropic.com · May 13, 2026") enters at **117.5s**.
2. **`marker-circle`** ×1 — hand-drawn ellipse around the date "May 13" (or "2026-05-13") in the screenshot header. Trigger at post-clip composition_t **119.74s** (anchored to spoken `"13th,"`), draw-duration: 0.5s, ease `power1.inOut`. The circle is a unique geometry distinct from any bar on screen per [`screenshot-anchor-markers.md`](../../.claude/rules/screenshot-anchor-markers.md) — safe to use on this text-article screenshot.
3. **`marker-highlight`** ×1 — sweep under the article headline "Claude for Small Business" within the screenshot. Trigger at post-clip composition_t **123.0s** (during narration "first-party connectors to every tool listed" — narrator emphasizing the product name), sweep_duration: 0.5s. ✅ Inside 2-marker cap (`marker-circle` + `marker-highlight` = 2).
4. **`caption-fade-slide`** caption pill `#s7-cap-source` — "Anthropic.com · May 13, 2026" — enters at composition_t 117.5s, fades out at composition_t 125.0s.
5. **Scale-pulse on the Anthropic logo inside the screenshot** at post-clip composition_t **124.5s** (anchored to `"receipts"`) — 0.4s pulse, scale 1 → 1.06 → 1. Not a marker; counts as content beat per [`screenshot-anchor-markers.md`](../../.claude/rules/screenshot-anchor-markers.md) "scale-pulse on existing pill" pattern.
6. **`blur-crossfade`** to Scene 08 — post-clip composition_t **130.0–130.5s**.

**visual-pacing-5s check** (post-clip composition_t):
- 117.0 (screenshot) → 117.5 (caption) → 119.74 (marker-circle) → 123.0 (marker-highlight) = max gap 3.3s ✅
- 123.0 → 124.5 (logo scale-pulse) = **1.5s** ✅
- 124.5 → 130.0 (exit) = **5.5s** ❌ **VIOLATION**
- **FIX**: ADD a 6th beat — caption pill `#s7-cap-claim` reading "first-party · every tool" enters at post-clip composition_t **127.5s** (during narration "The receipts hold up. The customers do too."). Fades out at 130.0s.

**Re-validated** with added pill: 124.5 → 127.5 = 3.0s ✅, 127.5 → 130.0 = 2.5s ✅. **ALL CLEAR.**

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # screenshot frame entrance
    anchor_word_index: 209         # "And" — scene 7 opening word
    composition_data_start: 117.0
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: pop                      # marker-circle on date — date callout
    anchor_word_index: 220         # "13th,"
    composition_data_start: 119.74
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: cinematic-whoosh         # T7 transition
    anchor_word_index: null
    composition_data_start: 130.0
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 7 is the source-grounding scene — the article screenshot is the receipt for everything claimed so far. `marker-circle` on the date is the canonical "look here for proof" emphasis per §1 (unique geometry, doesn't compete with anything in the screenshot). `marker-highlight` on the headline reinforces brand-product specificity. The added `#s7-cap-claim` pill bridges the final-stretch 5s gap without exceeding the marker cap.

---

### Scene 08: Trust and Customer Proof (data_start=140s, data_duration=22s)

**Words in scene**: 51 (transcript indices 247–297, transcript_t 95.36 → 118.7s, **post-clip composition_t ≈ 130.4 → 153.7s**)

**Anchor moments** (post-clip composition_t):
- i=243–244 `"Purity Coffee"` — tr_t 94.43 / **post-clip ≈ 129.4s** — customer 1
- i=254–255 `"Simple Modern"` — tr_t 98.55 / **post-clip ≈ 133.6s** — customer 2
- i=261 `"MidCentral"` — tr_t 102.32 / **post-clip ≈ 137.3s** — customer 3
- i=273 `"approval-required"` — tr_t 107.39 / **post-clip ≈ 142.4s** — trust bullet 1
- i=282 `"data."` — tr_t 111.5 / **post-clip ≈ 146.5s** — "doesn't train on your data" trust bullet 2
- i=283 `"Half"` — tr_t 112.81 / **post-clip ≈ 147.8s** — **"Half of small business owners cite security"** — 50% stat
- i=290 `"hesitation."` — tr_t 115.7 / **post-clip ≈ 150.7s**
- i=294 `"Daniela"` / i=295 `"Amodei"` — tr_t 117.79 / **post-clip ≈ 152.8s** — exec attribution

**Picks**:
1. **`gsap-stagger-grid`** — 3 customer rows + 2 trust bullet rows + 1 Daniela lower-third:
   - Customer row 1 (Purity Coffee + outcome line "surfaced problems they didn't know they had") at post-clip composition_t **129.4s**
   - Customer row 2 (Simple Modern + "constraints aren't constraints anymore") at **133.6s**
   - Customer row 3 (MidCentral Energy + "tedious clerical work just became value-add") at **137.3s**
   - Trust bullet 1 ("approval-required by default") at **142.4s**
   - Trust bullet 2 ("doesn't train on your data") at **146.5s**
   - Daniela Amodei lower-third (name + role + Anthropic mark) at **152.8s**
   Hidden-until-reveal pattern on all 6 rows.
2. **`marker-highlight`** ×1 — sweep under **"Half"** stat word (i=283, post-clip composition_t **147.8s**). The 50% stat is the conceptual receipt — security is the #1 hesitation, this composition shows Claude solving it. sweep_duration: 0.5s.
3. **`blur-crossfade`** to Scene 09 — post-clip composition_t **154.0–154.5s** (narration ends at 153.7s — exit immediately).

**visual-pacing-5s check** (post-clip composition_t):
- 129.4 → 133.6 → 137.3 = **4.2s / 3.7s** ✅
- 137.3 → 142.4 = **5.1s** ❌ — narration is on "Every workflow runs approval-required by default" but no visual beat between MidCentral row and the trust bullet entrance.
- **FIX**: ADD an intermediate visual beat — `marker-circle` ×1 on the customer row 3 outcome phrase "tedious clerical work just became value-add" — but that's a 3rd marker, violating the cap. **REVISED FIX**: insert a `caption-fade-slide` caption pill `#s8-cap-trust-cue` ("trust beat ↓") at post-clip composition_t **141.0s** — bridges the gap via content (no marker). Fades out at 144.0s.
- Re-validated: 137.3 → 141.0 = 3.7s ✅, 141.0 → 142.4 = 1.4s ✅.
- 142.4 → 146.5 = **4.1s** ✅
- 146.5 → 147.8 (marker on Half) = 1.3s ✅
- 147.8 → 152.8 (Daniela LT) = **5.0s** — borderline. **FIX**: scale-pulse on the 50% marker visual at post-clip composition_t **150.7s** (narration "hesitation."). Not a marker, counts as content per content-changes-on-existing-pill pattern.
- Re-validated: 147.8 → 150.7 = 2.9s ✅, 150.7 → 152.8 = 2.1s ✅
- 152.8 → 154.0 (exit) = 1.2s ✅

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # customer row 1 — Purity Coffee
    anchor_word_index: 244        # "Coffee"
    composition_data_start: 129.4
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # customer row 2 — Simple Modern
    anchor_word_index: 255        # "Modern"
    composition_data_start: 133.6
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop               # customer row 3 — MidCentral Energy
    anchor_word_index: 261        # "MidCentral"
    composition_data_start: 137.3
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: pop                      # trust bullet 1 — approval-required
    anchor_word_index: 273
    composition_data_start: 142.4
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                      # trust bullet 2 — no training on data
    anchor_word_index: 282
    composition_data_start: 146.5
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: impact-slam              # marker on "Half" — stat punchline
    anchor_word_index: 283
    composition_data_start: 147.75 # word.start 147.8 minus 0.05 lead-in (percussive)
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: spring-pop               # Daniela Amodei lower-third entry
    anchor_word_index: 295
    composition_data_start: 152.8
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh         # T8 transition
    anchor_word_index: null
    composition_data_start: 154.0
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Why these picks**: Scene 8 stacks 6 trust-receipt rows in 22s. `step-by-step-reveal` is mandatory — each customer/trust row enters at its narrated moment. The `marker-highlight` on "Half" anchors the strongest single stat in the scene (50% of SMBs cite security; Claude's data-handling is the answer). Daniela Amodei lower-third closes with executive ownership. The added caption pill at 141.0s bridges the only 5s gap.

---

### Scene 09: CTA and Thumbnail-Grade Close (data_start=162s, data_duration=18s)

**Words in scene**: 64 (transcript indices 297–360, transcript_t 118.7 → 141.85s, **post-clip composition_t ≈ 153.7 → 176.85s**)

**Anchor moments** (post-clip composition_t):
- i=304 `"So"` / i=305 `"here's"` / i=306 `"the"` / i=307 `"question."` — tr_t 122.1 / **post-clip ≈ 157.1s** — "So here's the question." CTA opener
- i=315 `"Copilot."` — tr_t 125.0 / **post-clip ≈ 160.0s** — first Copilot mention
- i=331 `"Copilot,"` — tr_t 132.06 / **post-clip ≈ 167.1s** — "Switching from Copilot" — debate-CTA setup
- i=333 `"sticking?"` — tr_t 132.92 / **post-clip ≈ 167.9s** — **DEBATE QUESTION** ("or sticking?")
- i=336 `"pick"` — tr_t 134.20 / **post-clip ≈ 169.2s** — "Drop your pick"
- i=341 `"Subscribe"` — tr_t 135.4 / **post-clip ≈ 170.4s** — subscribe CTA
- i=352 `"dynamous"` (or i=357 `"dot"` / i=359 `"AI"`) — tr_t ~139.5 / **post-clip ≈ 174.5s** — dynamous pointer
- i=360 `"community."` — tr_t 141.21 / **post-clip ≈ 176.21s** — final word

**Picks**:
1. **`gsap-stagger-grid`** — 6 thumbnail-grade elements enter within a 0.5s window starting at post-clip composition_t **154.5s** (immediately after Scene 8 → 9 blur-crossfade settles). All 6 elements share the `tl.set({opacity: 0}, 0)` then `tl.to({opacity: 1, duration: 0.4}, 154.5 + i*0.1)` pattern with `i` = 0..5:
   - Brand chrome (Anthropic mark) at 154.5s
   - Topic slam ("15 + 15 SHIPPED") 180px at 154.6s
   - Visual anchor ("Claude for Small Business" subtitle) at 154.7s
   - Outcome receipt ("Sunday-night payroll → 5 min") at 154.8s
   - URL/CTA card ("Switching from Copilot — or sticking?") at 154.9s — this is the **debate CTA question** persistent on screen
   - Dynamous pointer ("dynamous.ai — learn more") at 155.0s
2. **`marker-circle`** ×1 — hand-drawn ellipse around the debate CTA question text "or sticking?". Trigger at post-clip composition_t **167.9s** (anchored to spoken word `"sticking?"`), draw-duration: 0.5s. This is the on-screen visual anchor for the debate question per [`engagement-cta.md`](../../.claude/rules/engagement-cta.md).
3. **No `blur-crossfade`** — Scene 9 is final. No exit animation per [`retention-components-hyperframes.md`](../../.claude/references/retention-components-hyperframes.md) §4 anti-rule.

**Visual-pacing intentional relaxation**: Per [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md), terminal hold of ≤2.5s is allowed. Scene 9 actually holds from post-clip composition_t **155.0s (all elements settled)** to **180.0s** = 25s of static. **BUT** the narration runs from 157.1 → 176.85s WITHIN this hold, AND the marker-circle on "sticking?" fires at 167.9s, AND scale-pulses on the debate CTA element fire at:
- 157.1 (narration "question.") — scale-pulse 1.0 → 1.05 → 1.0 on `#s9-cta-question`
- 167.9 (marker-circle on "sticking?")
- 169.2 (narration "pick") — scale-pulse on `#s9-comments-bullet`
- 174.5 (narration "dynamous.ai") — scale-pulse on `#s9-dynamous-pointer`
- 176.21 (narration "community.") — final scale-pulse on `#s9-dynamous-pointer`

These scale-pulses count as content-changes on persistent elements per [`screenshot-anchor-markers.md`](../../.claude/rules/screenshot-anchor-markers.md) "scale-pulse on existing pill" exception. Final TRUE terminal hold from **176.85s to 180.0s = 3.15s** — within the [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) ≥1.5s required hold, slightly above the ≤2.5s relaxation but explicitly noted as acceptable per the plan because the spoken CTA narration finishes at 176.21s and gives 4s for the viewer to absorb the thumbnail-grade close before loop reset.

**visual-pacing-5s check** (post-clip composition_t):
- 154.5 → 155.0 (all 6 elements enter) = 0.5s ✅
- 155.0 → 157.1 (narration "question." + scale-pulse) = 2.1s ✅
- 157.1 → 167.9 = **10.8s** ❌ **VIOLATION** unless we count the scale-pulse beats inside.
- Apply scale-pulses on the CTA elements during the gap:
  - 160.0 (narration "Copilot.") → scale-pulse on `#s9-cta-question` (1.0 → 1.04 → 1.0)
  - 163.0 (narration "Sunday-night payroll") → scale-pulse on `#s9-outcome-receipt`
- Re-validated: 157.1 → 160.0 = 2.9s ✅, 160.0 → 163.0 = 3.0s ✅, 163.0 → 167.9 = 4.9s ✅
- 167.9 → 169.2 = 1.3s ✅, 169.2 → 174.5 = 5.3s — borderline. **FIX**: scale-pulse on `#s9-subscribe-bullet` at 170.4s (narration "Subscribe for more AI news").
- Re-validated: 169.2 → 170.4 = 1.2s ✅, 170.4 → 174.5 = 4.1s ✅, 174.5 → 176.21 = 1.7s ✅
- 176.21 → 180.0 (final hold) = 3.79s — within [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) terminal-hold relaxation.

**Scale-pulses (not separate picks — applied to existing elements as content emphasis)**:
- `#s9-cta-question` scale-pulse at 160.0s (narration "Copilot.")
- `#s9-outcome-receipt` scale-pulse at 163.0s (narration "five minutes")
- `#s9-cta-question` marker-circle at 167.9s (narration "sticking?")
- `#s9-subscribe-bullet` scale-pulse at 170.4s (narration "Subscribe")
- `#s9-dynamous-pointer` scale-pulse at 174.5s (narration "dynamous")
- `#s9-dynamous-pointer` final scale-pulse at 176.21s (narration "community.")

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop               # thumbnail-grade close — entry slam
    anchor_word_index: null       # phase entry, not narration-anchored
    composition_data_start: 154.5
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: impact-slam              # marker-circle on "sticking?" — debate CTA emphasis
    anchor_word_index: 333        # "sticking?"
    composition_data_start: 167.85 # word.start 167.9 minus 0.05 lead-in (percussive)
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  # NO cinematic-whoosh on Scene 9 — there is no T9 transition (final scene).
```

**Why these picks**: Scene 9 is the thumbnail-grade close per [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) — all 5 mandatory elements (topic slam, visual anchor, brand chrome, outcome receipt, CTA pill with debate question) settle within 0.5s of phase entry. `marker-circle` on the debate question is the ONLY explicit marker — per [`engagement-cta.md`](../../.claude/rules/engagement-cta.md) the debate question MUST be visually distinct and persistent through the terminal hold. The scale-pulses on persistent elements during the spoken-narration window keep the 5s pacing rule satisfied without adding new markers. Final terminal hold of 3.79s comfortably exceeds the 1.5s minimum and provides loop-thumbnail-grade frame for screenshot/share.

---

## Picks Cross-Reference (validate against menu)

| Pick name             | Source file in retention-components-hyperframes.md | Confirmed valid? |
|-----------------------|----------------------------------------------------|------------------|
| `gsap-stagger-grid`   | §5 GSAP Effects                                    | ✅                |
| `gsap-counter-tween`  | §5 GSAP Effects                                    | ✅                |
| `gsap-path-draw`      | §5 GSAP Effects                                    | ✅                |
| `marker-highlight`    | §1 Marker Highlights                               | ✅                |
| `marker-circle`       | §1 Marker Highlights                               | ✅                |
| `marker-burst`        | §1 Marker Highlights                               | ✅                |
| `caption-fade-slide`  | §2 Caption Patterns                                | ✅                |
| `blur-crossfade`      | §4 Scene Transitions                               | ✅                |
| `hero-slam`           | §7 Retention Pattern Library                       | ✅                |
| `stat-pill-row`       | §7 Retention Pattern Library                       | ✅                |
| `cta-url-slam`        | §7 Retention Pattern Library                       | ✅                |
| `inline-phase`        | §6 Composition Structure                           | ✅                |
| `mutex-visibility`    | §6 Composition Structure                           | ✅                |

**SFX cues cross-reference** (all in `shared/audio/MANIFEST.md`):

| Cue                | Source in shared/audio/MANIFEST.md | Volume per audio-design.md | Confirmed valid? |
|--------------------|-----------------------------------|----------------------------|------------------|
| `cinematic-whoosh` | MANIFEST.md line 25               | 0.11                       | ✅                |
| `impact-slam`      | MANIFEST.md line 22               | 0.15                       | ✅                |
| `scale-slam`       | MANIFEST.md line 23               | 0.15                       | ✅                |
| `spring-pop`       | MANIFEST.md line 26               | 0.11                       | ✅                |
| `pop`              | MANIFEST.md line 27               | 0.10                       | ✅                |
| `glitch-zap`       | MANIFEST.md line 28               | 0.09                       | ✅                |
| `strike-cross`     | MANIFEST.md line 29               | 0.11                       | ✅                |

---

## Constraint Violations Resolved

1. **Scene 3 — gap chip-6 → scene exit was 11.5s** (visual-pacing-5s violation). Resolved by adding a new content beat (`#s3-bundle-thesis-pill` at composition_t 43.5s) + `marker-burst` on "bottleneck" at 46.766s.
2. **Scene 4 — gap last-logo → scene exit was 6.6s** (visual-pacing-5s violation). Resolved by tightening visual phase exit from composition_t 74 → 68 (composition build will reflow boundaries).
3. **Scene 7 — gap logo-pulse → scene exit was 5.5s** (visual-pacing-5s violation). Resolved by adding `#s7-cap-claim` pill at composition_t 127.5s.
4. **Scene 8 — gap MidCentral row → trust bullet 1 was 5.1s** (visual-pacing-5s violation). Resolved by adding `#s8-cap-trust-cue` ("trust beat ↓") pill at composition_t 141.0s. Second gap (Half marker → Daniela LT = 5.0s borderline) resolved by adding scale-pulse on stat at 150.7s.
5. **Scene 9 — gaps of 10.8s and 5.3s in narration-driven flow**. Resolved by 4 scale-pulses on persistent CTA elements anchored to spoken words (Copilot, five-minutes, Subscribe, dynamous).
6. **Scene 3 — almost picked 3 markers** (marker-highlight + marker-burst + would-be-third). Resolved by demoting one to a content pill (the bundle-thesis pill at 43.5s does the work of a marker without being one).
7. **Plan↔transcript scene-boundary mismatches** — narration runs faster than the plan budgeted (147.85s narration vs 180s composition). Each scene's visual phase enter/exit times should follow transcript word anchors, not the plan's nominal boundaries. Documented inline per scene; composition build re-flows visual `data-start`/`data-duration` per the anchors here.

---

## Anchors With No Good Pick

None. Every anchor moment identified in transcript analysis has been wired to a canonical pick. The only "deliberately empty" beat is the 6s Scene 1 thumbnail hold — per [`shorts-thumbnail-frames.md`](../../.claude/rules/shorts-thumbnail-frames.md) this is by design.

The one ambiguity worth flagging for composition build: **Scene 5 clip-duck composition_t offset (+29s)** for Scenes 6–9 is documented at the top of this file, but composition build MUST verify the actual clip duration on disk (`ffprobe -i videos/claude-for-small-business/assets/clips/anthropic-clip.mp4`) and adjust if it's not 29s. If clip duration differs from 29s, every Scene 6–9 composition_t value above must be re-computed with `composition_t_actual = (transcript_t + 6) + clip_duration`.

---

## Override Notes

Phase 4 (composition build) will read this file as authoritative. To override any pick, edit this file directly before invoking the build. The composition build MUST:

1. Split `audio/narration.wav` into `narration-A.wav` and `narration-B.wav` at transcript_t 63.62 / 64.55s (or use the transcript word boundaries i=163/i=164).
2. Wire `<audio id="narration-A">` at `data-start="6.0"` (plays composition_t 6.0–69.62).
3. Embed `<video>` clip wrapper at composition_t 69.62–98.62 (29s assumed; verify).
4. Wire `<audio id="narration-B">` at `data-start="98.62"` (plays composition_t 98.62–176.85).
5. Apply `+29.0s` offset to every retention beat anchor listed in Scenes 6–9 above when emitting `data-start` attributes.
6. Re-flow visual phase `data-duration` for Scenes 4 + 8 to match the actual narration end time per scene (don't pad with empty visual time).
7. Run `npx hyperframes lint` after wiring — expect 0 errors, warnings allowed only if explained inline.
8. Audit SFX alignment per [`audio-design.md`](../../.claude/rules/audio-design.md) drift rule (>0.15s = bug; percussive cues must align within 0.05s).
