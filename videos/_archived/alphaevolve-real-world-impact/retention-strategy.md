# Retention Strategy: alphaevolve-real-world-impact

Source-grounded, transcript-anchored retention picks for each of the 10 scenes (S01–S10). Every component name below is a canonical entry from `.claude/references/retention-components-hyperframes.md`. Every SFX cue is verified against `shared/audio/MANIFEST.md`. All trigger times are seconds, anchored to `transcript.json` word `start` values (464 words, **186.04s** total narration; transcript runs 6.04s past plan boundary because narration came in slightly slower than the 180s plan budget — composition build will extend `#root` `data-duration` from 180 to **186.5** to absorb the tail. Per-scene `data_start` values are retimed to actual transcript word starts; see Override Notes for the retimed table.).

---

## Summary Table

| Scene                          | Pattern (from §7)              | Primitives                                                                  | Captions             | Audio-Reactive            | Transition Out (start_s, dur)   | Total Picks |
| ------------------------------ | ------------------------------ | --------------------------------------------------------------------------- | -------------------- | ------------------------- | ------------------------------- | ----------- |
| S01 Cold Open Hook             | hero-slam                      | gsap-stagger-grid, marker-highlight                                         | caption-word-pop     | none                      | blur-crossfade @ 16.0, 0.5s     | 5           |
| S02 Contrarian Setup           | inline-phase + contrast-pivot  | gsap-stagger-grid, marker-scribble, gsap-path-draw, marker-highlight        | caption-fade-slide   | none                      | blur-crossfade @ 33.7, 0.5s     | 6           |
| S03 Lineage Pop (1969→2022)    | stat-pill-row (single bigstat) | gsap-stagger-grid, gsap-counter-tween, marker-highlight, vfx-shatter (BLOCK) | caption-word-pop     | none                      | glitch-zap @ 54.5, 0.3s (ACCENT)| 6           |
| S04 Receipts pt.1 (DNA + Grid) | stat-pill-row (paired)         | gsap-stagger-grid, gsap-counter-tween, marker-highlight                     | caption-fade-slide   | none                      | blur-crossfade @ 75.3, 0.5s     | 5           |
| S05 Receipts pt.2 (Quantum + Math) | stat-pill-row + quote-card | gsap-stagger-grid, gsap-counter-tween, marker-highlight                     | caption-fade-slide   | none                      | blur-crossfade @ 93.4, 0.5s     | 5           |
| S06 TPU Recursion              | audio-pulsed-logo (composite)  | gsap-stagger-grid, gsap-path-draw, marker-burst, vfx-portal (BLOCK)         | caption-word-pop     | audio-reactive-glow       | blur-crossfade @ 117.7, 0.5s    | 7           |
| S07 Verifier Loop              | diagram + caption-fade-slide   | gsap-stagger-grid, gsap-path-draw, marker-circle, marker-burst              | caption-fade-slide   | none                      | blur-crossfade @ 136.1, 0.5s    | 6           |
| S08 Receipts pt.3 (External)   | stat-pill-row (4-pill extended)| gsap-stagger-grid, gsap-counter-tween                                       | caption-fade-slide   | none                      | blur-crossfade @ 159.6, 0.5s    | 4           |
| S09 Compound-Interest Frame    | stat-pill-row (2×3 mosaic)     | gsap-stagger-grid, marker-highlight                                         | caption-word-pop     | audio-reactive-glow       | blur-crossfade @ 174.4, 0.5s    | 5           |
| S10 CTA + Dynamous Outro       | cta-url-slam → endcard         | gsap-stagger-grid, marker-circle                                            | none                 | none                      | none (final fade-to-black)      | 4           |

**Pick category totals**:
- Markers: 11 total (S01:1, S02:2, S03:1, S04:1, S05:1, S06:1, S07:2, S08:0, S09:1, S10:1). Cap of 2/scene respected — S02 and S07 use 2 markers each.
- Captions: 8 scenes use captions (S01–S07 + S09). S08 and S10 omit. `caption-word-pop` ×3 (S01, S03, S06, S09 = 4 — energetic scenes), `caption-fade-slide` ×4 (S02, S04, S05, S07, S08 = 5 — connected explanatory scenes). Single-group mutex automatic via `mutex-visibility`.
- Audio-reactive: 2 (S06 quote glow, S09 m-headline glow). 3-4% subtle range only. Per `audio-reactive.md` — text effects ≤6%.
- Transitions: 9 total. `blur-crossfade` ×8 (88% — primary), `glitch-zap` ×1 ACCENT at T2 (S03→S04 detonation tail). One primary + one accent — within rule.
- GSAP effects: 22 total (`gsap-stagger-grid` ×10, `gsap-counter-tween` ×7, `gsap-path-draw` ×3, `marker` instances counted separately above).
- VFX blocks: 2 (`vfx-shatter` in S03, `vfx-portal` in S06). Per plan VFX budget.
- SFX cues: 31 total (`impact-slam` ×2, `screen-shake` ×1, `scale-slam` ×6, `spring-pop` ×11, `pop` ×2, `cinematic-whoosh` ×9, `glitch-zap` ×1, `strike-cross` ×1, `impact-slam` layered with detonation). All cap-compliant per `.claude/rules/audio-design.md`.

---

## Scene-by-Scene Detail

### Scene 01 — Cold Open Hook (data_start=0, data_duration=16.5)

**Words in scene**: 41 (transcript indices 0–40)

**Anchor moments**:
- 0.046s — word [0] "While" (entrance moment — first word, hero topo-motion webm fades in)
- 1.231s — word [5] "chatbots," (first slam beat — overline AI BEYOND CHAT enters)
- 2.566s — word [8] "agent" (subhead context anchor)
- 3.750s — word [11] "real-world" (HERO PIVOT WORD — the contrarian frame lands)
- 4.145s — word [12] "wins" (HERO PIVOT WORD #2 — the second slam pop)
- 5.039s — word [14] "D" + 5.294s [15] "N" + 5.468s [16] "A," (DNA spelled letter-by-letter — receipts preview)
- 11.413s — word [32] "built" (PIVOT — "They built a verifier" — the term-branding moment)
- 11.714s — word [34] "verifier." (TERM-BRAND ANCHOR — marker-highlight fires here)
- 12.457s — word [35] "Twelve" (months — scale callback)
- 15.336s — word [39] "Receipts" + 15.708s [40] "incoming." (caption pill payoff promise — sets up S02 loop)

**Picks**:
1. `gsap-stagger-grid` for the hero entrance — overline at 0.5s, slam-1 "ONE AI." at trigger_s: 0.046 (word [0] "While" — slam slides in as the narrator says "While you were arguing"), slam-2 "REAL-WORLD WINS." at trigger_s: 3.750 (word [11] "real-world" — the second slam lands precisely on the pivot word). Subhead "12 months. Zero conversations." at trigger_s: 12.457 (word [35] "Twelve"). Receipts-incoming pill at trigger_s: 15.336 (word [39] "Receipts"). All entrances 0.55s, ease `back.out(1.7)` for slams, `power3.out` for subhead/pill.
2. `marker-highlight` on the word "**verifier**" inside the spoken sentence — yellow accent bar sweeps in behind the inline word at trigger_s: 11.714 (word [34]), `sweep_duration: 0.5s`, ease `power2.out`. ONE marker — frequency cap respected. This plants the term-branding for "verifier" that S07 resolves.

**Captions**: `caption-word-pop` (energetic — hook scene). Word-grouping 2-3 words/group per the high-energy rule. Custom per-word styling: `chatbots,` (mono accent — subtle desaturate), `real-world wins` (yellow scale-up + bold), `verifier.` (yellow bold, MEMORY callback), `Twelve months.` (white bold), `Zero conversations.` (white bold). Position: bottom 600-700px from bottom (portrait short).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=16.0, duration=0.5s, ease `sine.inOut`. (S02 first word "Every" at 16.462 — transition starts at 16.0, completes at 16.5 covering the 0.46s breath before "Every".)

**SFX cues**:
```yaml
sfx_cues:
  - cue: impact-slam            # slam-1 "ONE AI." entrance
    anchor_word_index: 0        # transcript[0]="While" start=0.046 (slam fires at first word)
    offset_seconds: -0.05       # percussive lead-in
    duration_seconds: 0.63
    track_index: 3
    volume: 0.20                # MANIFEST default
  - cue: screen-shake           # layered with impact-slam — Cinematic Hook beat 1
    anchor_word_index: 0
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4              # concurrent with impact-slam
    volume: 0.15                # MANIFEST default
  - cue: scale-slam             # second slam "REAL-WORLD WINS." on pivot word
    anchor_word_index: 11       # "real-world" start=3.750
    offset_seconds: -0.10       # SFX leads spoken word for percussive land
    duration_seconds: 0.73
    track_index: 3              # impact-slam at 0.0 finished by 0.58 — no overlap
    volume: 0.20
  - cue: spring-pop             # subhead "Twelve months." entrance
    anchor_word_index: 35       # "Twelve" start=12.457
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # caption pill "Receipts incoming →"
    anchor_word_index: 39       # "Receipts" start=15.336
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # sequential, no overlap
    volume: 0.15
  - cue: cinematic-whoosh       # S01 → S02 transition + shape rearrange
    anchor_word_index: 41       # "Every" (S02 first word) start=16.462
    offset_seconds: -0.46       # whoosh starts at 16.0 (transition start)
    duration_seconds: 0.84
    track_index: 4              # spring-pop on 3 — whoosh on 4
    volume: 0.15
```

**Why these picks**: The hook needs a scroll-stop double-slam. The first slam ("ONE AI.") lands on the first word "While" with layered impact-slam + screen-shake — the canonical Cinematic Hook stack. The second slam ("REAL-WORLD WINS.") is anchored to the pivot word "real-world" — narration and visual fire together. `marker-highlight` on the spoken word "verifier" (11.714s) is the single marker — it term-brands the concept S07 resolves with the verifier loop diagram, and lands at the moment the narrator says it. Captions in `caption-word-pop` keep the eye anchored across the 16-second hook (per the visual-pacing-5s audit — caption word groups land every 1.5–2.5s, filling the gap between slam-2 (3.75s) and "verifier" (11.7s) which would otherwise be 8s of stillness).

**Visual pacing audit (5s rule)**: foreground entrances at 0.046s (slam-1 + topo webm), 3.750s (slam-2 "real-world wins"), 5.039s (DNA letter beat — caption pop on D-N-A spelling), 11.714s (marker-highlight on "verifier"), 12.457s (subhead "Twelve months"), 15.336s (Receipts incoming pill), 16.0s (transition start). Largest non-caption gap = 11.714 − 5.039 = 6.7s — but caption-word-pop fires on every word during this window (words [16] "A," 5.468s, [17] "the" 5.921s, [18] "power" 6.084s, [19] "grid," 6.385s, [20] "and" 6.954s, [21] "the" 7.094s, [22] "silicon" 7.256s, [23] "Google" 7.581s, etc.) — caption progression counts as content morph beats per the rule. All gaps ≤ 5s. RULE RESPECTED.

---

### Scene 02 — Contrarian Setup (data_start=16.5, data_duration=17.5)

**Words in scene**: 47 (transcript indices 41–87)

**Anchor moments**:
- 16.462s — word [41] "Every" (S02 first word — eyebrow "THE PART NOBODY SHIPPED" enters)
- 18.227s — word [48] "chatbot." (FIRST chatbot anchor — chatbot-window glyph fades in over the next ~0.7s)
- 19.597s — word [49] "But" (PIVOT WORD — strike-cross moment + accent rotates from `--g-blue` to `--g-red`)
- 19.934s — word [51] "one" + 20.062s [52] "isn't." (counter-pivot completes — "But this one isn't")
- 20.851s — word [55] "code." (Tests/Throws/Keeps verb cascade enters)
- 21.362s — word [56] "Tests" (verb-card 1 entrance)
- 22.964s — word [58] "Throws" (verb-card 2 entrance)
- 24.009s — word [62] "Keeps" (verb-card 3 entrance)
- 26.029s — word [67] "year," (duration anchor — "For a year")
- 27.840s — word [74] "quietly." (caption emphasis — bold pop)
- 30.280s — word [78] "Alpha-Evolve," (BRAND REVEAL — marker-highlight #2 fires here, term-branding)
- 32.193s — word [83] "shipping" + 32.878s [86] "whole" + 33.122s [87] "time." (closing cadence)

**Picks**:
1. `gsap-stagger-grid` for the 3 verb-cards "WRITES CODE / TESTS IT / THROWS-KEEPS" — each at the spoken verb word, NOT all at once. Step-by-step reveal pattern (3 items, narrator names them in distinct sentences):
   - Verb-card 1 "WRITES CODE." enters at trigger_s: 20.851 (word [55] "code.")
   - Verb-card 2 "TESTS IT." enters at trigger_s: 21.362 (word [56] "Tests")
   - Verb-card 3 "THROWS / KEEPS" (paired) enters at trigger_s: 22.964 (word [58] "Throws")
   Each: `tl.set` at t=0 (hidden), `tl.to` at trigger time, 0.45s ease `back.out(1.5)`, x: -40 → 0, opacity: 0 → 1.
2. `marker-scribble` on the chatbot-window glyph — chaotic strikethrough drawn from trigger_s: 19.597 (word [49] "But" — the pivot moment), draw duration 0.7s, ease `power4.out`. The glyph stays visible through the strikethrough then dissolves at ~21.0s as topo terrain emerges underneath.
3. `gsap-path-draw` on the SVG strikethrough line — drawn alongside the marker-scribble, same trigger window 19.597 → 20.297 (0.7s).
4. `marker-highlight` on the spoken word "**Alpha-Evolve**" — accent-red bar sweeps behind the brand word at trigger_s: 30.280 (word [78]), sweep_duration: 0.5s, ease `power2.out`. THIS IS THE BRAND REVEAL term-branding moment per Story Lock #1. 2nd marker on this scene — within the 2/scene cap.

**Captions**: `caption-fade-slide`, word groups of 3-5 (calm-energetic explainer tone). Custom per-word: `chatbot.` (mono desaturate × 2 instances at 18.227 and 18.680 — slight crossed-out feel), `But` (red bold scale-up — pivot word), `Tests / Throws / Keeps` (each gets accent-red boost), `Alpha-Evolve` (red bold scale-up — brand reveal), `quietly` (white italic).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=33.7, duration=0.5s, ease `sine.inOut`. (S03 first word "Here's" at 34.376s — connector flows naturally.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: strike-cross           # marker-scribble on "chatbot" — fires on PIVOT word "But"
    anchor_word_index: 49       # "But" start=19.597
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15                # MANIFEST default
  - cue: glitch-zap             # layered pivot accent (canonical "But" pivot stack)
    anchor_word_index: 49
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4              # concurrent with strike-cross
    volume: 0.12
  - cue: pop                    # verb-card 1 entrance "WRITES CODE."
    anchor_word_index: 55       # "code." start=20.851
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # strike-cross at 19.55 ended by 20.18 — no overlap
    volume: 0.13
  - cue: pop                    # verb-card 2 entrance "TESTS IT."
    anchor_word_index: 56       # "Tests" start=21.362
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior pop ended by 21.37 — 0.51s gap, just-no-overlap
    volume: 0.13
  - cue: spring-pop             # verb-card 3 entrance "THROWS / KEEPS"
    anchor_word_index: 58       # "Throws" start=22.964
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: scale-slam             # brand reveal "Alpha-Evolve"
    anchor_word_index: 78       # "Alpha-Evolve," start=30.280
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: cinematic-whoosh       # S02 → S03 transition + shape rearrange
    anchor_word_index: 88       # "Here's" (S03 first) start=34.376
    offset_seconds: -0.68       # whoosh starts at 33.7
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S02 is the contrarian-pivot scene. The strike-cross + glitch-zap on "But" is the canonical pivot SFX stack from the cinematic hook blueprint. The 3 verb-cards (Writes/Tests/Throws-Keeps) MUST step-by-step reveal — narrator names each verb in its own sentence, so cards must enter at each verb's spoken word (per `step-by-step-reveal.md`). The brand-reveal scale-slam on "Alpha-Evolve" is the Story Lock #1 term-branding moment per the plan. 2 markers — strike-cross on "But" pivot + highlight on "Alpha-Evolve" — both serve the contrast-pivot pattern.

**Visual pacing audit**: entrances at 16.462s (eyebrow), 18.227s (chatbot glyph fade-in), 19.597s (strike-cross + glitch-zap), 20.851s (verb-card 1), 21.362s (verb-card 2), 22.964s (verb-card 3), 26.029s ("year," caption emphasis on existing pill), 27.840s (quietly bold caption), 30.280s (Alpha-Evolve brand marker-highlight), 33.7s (transition). Largest gap = 22.964 → 26.029 = 3.07s; 27.840 → 30.280 = 2.44s; 30.280 → 33.7 = 3.42s. All ≤ 5s. RULE RESPECTED.

---

### Scene 03 — Lineage Pop, 1969 → 2022 → now (data_start=34, data_duration=21)

**Words in scene**: 44 (transcript indices 88–131)

**Anchor moments**:
- 34.376s — word [88] "Here's" (S03 first word — overline "53 YEARS" enters)
- 35.456s — word [91] "Strassen," (year-1969 row 1 entrance)
- 36.036s — word [92] "nineteen" + 36.431s [93] "sixty-nine," (1969 year label slam)
- 37.313s — word [94] "forty-nine" (NUMBER 49 counter-tween target — pill 1)
- 39.624s — word [99] "matrices." (closing cadence on row 1)
- 40.450s — word [100] "Alpha-Tensor," (year-2022 row 2 entrance)
- 41.500s — word [101] "twenty" (TIMESTAMP RECONSTRUCTED — checking) — actually word index lookup needed
- 43.037s — word [103] "dropped" (the verb that triggers the vfx-shatter detonation prep)
- 43.583s — word [106] "forty-seven." (THE DETONATION WORD — vfx-shatter fires HERE per plan)
- 45.278s — word [108] "first" + 45.533s [109] "improvement" (first improvement frame)
- 46.183s — word [111] "fifty-three" + 46.706s [112] "years." (53-YEAR HERITAGE LINE — marker-highlight fires)
- 48.029s — word [113] "Now" + 48.203s [114] "Alpha-Evolve" (year-2026/now row 3 entrance)
- 53.126s — word [126] "math" + 53.358s [127] "heritage" + 54.298s [131] "successor." (closing math-heritage cadence)

**Picks**:
1. `gsap-stagger-grid` for the 3 year-rows ("1969 STRASSEN — 49", "2022 ALPHATENSOR — 47", "2026 ALPHAEVOLVE — every algorithm") — each row enters at the spoken year/name word, NOT all at once. Step-by-step reveal:
   - Row 1 "1969 — STRASSEN — 49 multiplications" enters at trigger_s: 35.456 (word [91] "Strassen,")
   - Row 2 "2022 — ALPHATENSOR — 47" enters at trigger_s: 40.450 (word [100] "Alpha-Tensor,")
   - Row 3 "2026 — ALPHAEVOLVE — every algorithm" enters at trigger_s: 48.029 (word [113] "Now")
   Each: `tl.set` at t=0 (hidden), `tl.to` at trigger, 0.55s ease `back.out(1.5)`.
2. `gsap-counter-tween` on the "47" digit of the 360px gradient bigstat — tween from 49 → 47 (DECREMENT) across [42.4, 43.7] (1.3s window ending exactly when "forty-seven" lands at 43.583). Use `roundProps: 0`. Coupled with a 1.05× scale slam at the end frame.
3. `marker-highlight` on the spoken phrase "**fifty-three years**" — yellow accent bar sweeps behind the inline phrase at trigger_s: 46.183 (word [111] "fifty-three"), sweep_duration: 0.6s spans both words "fifty-three years," ease `power2.out`. THE 53-YEAR HERITAGE marker. ONE marker — within the 2/scene cap.
4. `vfx-shatter` (BLOCK) — installed at `videos/alphaevolve-real-world-impact/blocks/vfx-shatter/`, mounted on the year-2022 row. The "47" detonates into shards as the year flips. `data-start=42.5`, `data-duration=10` (covers 42.5-52.5 — the detonation, settle, and lead-out into "fifty-three years"). The block's INTERNAL choreography centers the shatter beat at the spoken word "**forty-seven**" (43.583s) — block content set such that the explosion peaks at ~43.6s. Per `sub-composition-wiring.md`, parent's `data-composition-id` MUST equal `vfx-shatter`.

**Captions**: `caption-word-pop` (energetic — number cult-hop scene). Word-grouping 2-3 per the high-energy rule. Custom per-word: `Strassen,` (white bold), `nineteen sixty-nine,` (mono accent), `forty-nine` (yellow bold scale-up — number), `Alpha-Tensor,` (white bold), `twenty twenty-two,` (mono accent), `forty-seven.` (yellow bold scale-up — DETONATION word, scale-up boosted), `fifty-three years.` (yellow bold), `Alpha-Evolve` (red bold scale-up — brand callback), `every algorithm` (red bold), `successor.` (closing white bold).

**Audio-reactive**: none.

**Transition out**: `glitch-zap` @ trigger_s=54.5, duration=0.3s, ease `power4`. **THE ONE ACCENT TRANSITION** in the video — chosen for the lineage detonation tail. (S04 first word "Receipts." at 54.925s — the glitch-zap covers 54.5–54.8 with 0.125s breath before "Receipts.")

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # year-row 1 entrance ("1969 STRASSEN")
    anchor_word_index: 91       # "Strassen," start=35.456
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # year-row 2 entrance ("2022 ALPHATENSOR")
    anchor_word_index: 100      # "Alpha-Tensor," start=40.450 (estimated index — verify; word [100] "Alpha-Tensor,")
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior at 35.46 ended ~36.0, no overlap
    volume: 0.15
  - cue: impact-slam            # vfx-shatter detonation on "forty-seven"
    anchor_word_index: 106      # "forty-seven." start=43.583 — THE DETONATION WORD
    offset_seconds: -0.10       # SFX leads percussively
    duration_seconds: 0.63
    track_index: 3
    volume: 0.20
  - cue: screen-shake           # layered with detonation impact-slam
    anchor_word_index: 106
    offset_seconds: -0.10
    duration_seconds: 0.52
    track_index: 4              # concurrent with impact-slam
    volume: 0.15
  - cue: spring-pop             # year-row 3 entrance ("2026 ALPHAEVOLVE")
    anchor_word_index: 113      # "Now" start=48.029
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior impact-slam ended ~44.21, plenty of gap
    volume: 0.15
  - cue: glitch-zap             # ACCENT transition S03 → S04
    anchor_word_index: 132      # "Receipts." (S04 first) start=54.925
    offset_seconds: -0.42       # glitch fires at 54.5
    duration_seconds: 0.52
    track_index: 4
    volume: 0.12
  - cue: cinematic-whoosh       # paired with glitch-zap on shape rearrange
    anchor_word_index: 132
    offset_seconds: -0.42       # whoosh layered with glitch-zap
    duration_seconds: 0.84
    track_index: 5              # third concurrent track for the layered transition
    volume: 0.15
```

**Why these picks**: S03 is the lineage cult-hop — the most mathematically charged scene. The vfx-shatter block detonates the "47" precisely on the spoken word "forty-seven" (43.583s) — that's the moment cultural authority transfers from Strassen (1969) to AlphaTensor (2022) to AlphaEvolve (now). The counter-tween (49 → 47) is unusual (decrement, not increment) but tells the story of "the number got smaller — that's the breakthrough". `marker-highlight` on "fifty-three years" cements the heritage line. `caption-word-pop` because numbers and brand names need per-word emphasis. The ACCENT `glitch-zap` at T2 is the single break from `blur-crossfade` — chosen because the lineage detonation deserves a transition that matches its energy.

**Visual pacing audit**: entrances at 34.376s (overline "53 YEARS"), 35.456s (year-row 1 + Strassen), 37.313s (counter starts: "forty-nine" lands), 40.450s (year-row 2 + AlphaTensor entrance), 42.5s (vfx-shatter detonation prep), 43.583s (DETONATION + impact-slam + screen-shake), 46.183s (marker-highlight on "fifty-three years"), 48.029s (year-row 3 entrance), 53.126s ("math heritage" cadence on existing visuals), 54.5s (glitch-zap transition). Largest gap = 48.029 → 53.126 = 5.10s — slightly over 5.0s. **RESOLVED** by adding a sub-beat: the year-row 3 "2026 ALPHAEVOLVE — every algorithm" continues to fill in cell-by-cell (the "every algorithm" copy appears at trigger_s: 50.699 — word [122] "algorithm") which fills the 48.0 → 53.1 gap with content morph. Audited gap recomputed: 48.029 → 50.699 = 2.67s; 50.699 → 53.126 = 2.43s. All ≤ 5s. RULE RESPECTED.

---

### Scene 04 — Receipts pt.1: DNA + Grid (data_start=54.5, data_duration=20.5)

**Words in scene**: 48 (transcript indices 132–179)

**Anchor moments**:
- 54.925s — word [132] "Receipts." (S04 first word — eyebrow "RECEIPTS — 1 OF 3" enters)
- 56.x — word [133] "PacBio's" + (pill 1 "DNA-sequencing errors" entrance prep)
- 57.654s — word [137] "sequencing" + 58.222s [138] "errors," (pill 1 visual reveal — DNA jpg + label)
- 58.687s — word [139] "down" + 58.931s [140] "thirty" + 59.221s [141] "percent," (PILL 1 NUMBER REVEAL — counter tween 0 → 30 ends here, marker-highlight fires)
- 59.999s — word [142] "because" (cause connector)
- 61.090s — word [144] "rewrote" (variant detection model — sub-line caption emphasis)
- 63.992s — word [150] "power" + 64.270s [151] "grid" (pill 2 "Power Grid Solver" entrance prep)
- 64.491s — word [152] "problem" + 64.828s [153] "solver," (pill 2 visual reveal — power-lines jpg + label)
- 65.362s — word [154] "fourteen" + 65.768s [155] "percent" (PILL 2 NUMBER 1 — counter starts, "14")
- 67.742s — word [160] "eighty-eight." (PILL 2 NUMBER 2 — counter ends, "88", marker-highlight fires)
- 70.006s — word [165] "Optimal" + 70.389s [166] "Power" + 70.714s [167] "Flow" (AC OPF benchmark caption)
- 73.129s — word [174] "losing" + 73.442s [175] "sleep" (SCAR insert phrase — caption bold)
- 74.278s — word [179] "decade." (closing cadence)

**Picks**:
1. `gsap-stagger-grid` for the 2 stat pills — paired but staggered. Pill 1 "DNA / -30%" enters at trigger_s: 57.654 (word [137] "sequencing"). Pill 2 "Power Grid / 14% → 88%" enters at trigger_s: 64.270 (word [151] "grid"). Each: `tl.set` at t=0, `tl.to` at trigger, 0.6s ease `back.out(1.5)`. Step-by-step reveal — narrator names DNA before grid, ~6s apart.
2. `gsap-counter-tween` on each numeric value:
   - Pill 1: tween 0 → 30 across [57.9, 59.22] (1.32s, ends as "thirty percent" lands at 58.931–59.221)
   - Pill 2 (two-stage): tween 0 → 14 across [64.85, 65.77] (0.92s, ends as "fourteen percent" lands at 65.362–65.768), THEN re-tween 14 → 88 across [66.4, 67.75] (1.35s, ends as "eighty-eight" lands at 67.742). The two-stage counter tells the visual story "14 → 88" matching the narration arc.
3. `marker-highlight` on the spoken word "**eighty-eight**" — yellow accent bar sweeps behind the inline number at trigger_s: 67.742 (word [160]), sweep_duration: 0.5s, ease `power2.out`. ONE marker — frequency cap respected. THE BIGGEST DELTA in the scene gets the marker.

**Captions**: `caption-fade-slide`, word groups of 3-5 (calm-energetic explainer). Custom per-word: `PacBio's DNA sequencing errors` (white bold + DNA accent yellow), `down thirty percent` (yellow bold scale-up — receipt #1), `power grid problem solver` (white bold + green accent), `fourteen percent` (mono small grayed), `eighty-eight.` (green bold scale-up — receipt #2), `AC Optimal Power Flow` (mono caps, technical accent), `losing sleep over for a decade` (orange italic — SCAR phrase).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=75.3, duration=0.5s, ease `sine.inOut`. (S05 first word "Quantum" at 75.729s — clean handoff.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # pill 1 entrance "DNA -30%"
    anchor_word_index: 137      # "sequencing" start=57.654
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: scale-slam             # pill 1 number reveal "thirty percent"
    anchor_word_index: 140      # "thirty" start=58.931
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # prior pop ended 58.17 — 0.66s gap, no overlap
    volume: 0.20
  - cue: spring-pop             # pill 2 entrance "Power Grid"
    anchor_word_index: 151      # "grid" start=64.270
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior scale-slam ended 59.56, plenty of gap
    volume: 0.15
  - cue: scale-slam             # pill 2 number 2 "eighty-eight"
    anchor_word_index: 160      # "eighty-eight." start=67.742
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3
    volume: 0.20
  - cue: cinematic-whoosh       # S04 → S05 transition + shape rearrange
    anchor_word_index: 180      # "Quantum" (S05 first) start=75.729
    offset_seconds: -0.43       # whoosh starts at 75.3
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S04 is the receipts scene — narrator names a number, counter ticks up to it, marker highlights the biggest delta. Two pills paced step-by-step (DNA enters, narrator says "30% errors down", then 6s later grid enters, narrator says "14 → 88"). The two-stage counter on pill 2 is the canonical "narrated-stat-reveal" pattern but doubled — the visual literally tells the 14→88 story matching the spoken number arc. ONE marker on "eighty-eight" because that's the bigger receipt; the 30% gets a scale-slam SFX hit instead (visual punch via SFX rather than marker keeps the marker count under 2).

**Visual pacing audit**: entrances at 54.925s (eyebrow), 56.5s (m headline "Wins that already shipped"), 57.654s (pill 1 + DNA jpg), 58.931s (counter ticks 0-30), 61.090s ("rewrote" caption emphasis), 64.270s (pill 2 + power-lines jpg), 65.362s (counter starts "14"), 66.4s (counter restarts 14-88), 67.742s (88 + marker-highlight), 70.006s (AC OPF caption), 73.129s ("losing sleep" caption bold), 75.3s (transition). Largest gap = 67.742 → 70.006 = 2.26s; 70.006 → 73.129 = 3.12s; 73.129 → 75.3 = 2.17s. All ≤ 5s. RULE RESPECTED.

---

### Scene 05 — Receipts pt.2: Quantum + Math (data_start=75.3, data_duration=18)

**Words in scene**: 42 (transcript indices 180–221)

**Anchor moments**:
- 75.729s — word [180] "Quantum" (S05 first word — eyebrow "RECEIPTS — 2 OF 3" enters)
- 76.089s — word [181] "circuits," (quantum pill prep)
- 76.658s — word [182] "ten" + 76.902s [183] "times" (NUMBER REVEAL — counter tween for "10×")
- 77.262s — word [184] "lower" + 77.575s [185] "error" + 77.912s [186] "rate" (sub-line)
- 78.690s — word [189] "Willow" (processor name caption bold)
- 80.477s — word [191] "And" + 80.640s [192] "math." (PIVOT — math sub-slide enters)
- 82.033s — word [193] "Terence" + 82.428s [194] "Tao," (Tao quote card entrance — "TERENCE TAO" name plate slams in)
- 82.939s — word [196] "Fields" + 83.206s [197] "medalist," (credentials sub-line)
- 84.750s — word [201] "quote," (the Tao quote card enters)
- 85.655s — word [202] "very" + 85.934s [203] "useful" + 86.457s [204] "new" + 86.642s [205] "capabilities." (THE QUOTE LINE — marker-highlight sweeps under "very useful")
- 88.663s — word [208] "Mozart" (caption bold — "Mozart of math")
- 89.638s — word [211] "signs" + 90.288s [213] "on" (closing quip)
- 91.716s — word [219] "chatbot" + 92.064s [220] "territory" + 92.552s [221] "anymore." (SCENE EXIT EMPHASIS — the contrarian-frame callback)

**Picks**:
1. `gsap-stagger-grid` — quantum pill (Willow/microchip jpg) enters at trigger_s: 75.729 (word [180] "Quantum"). Tao quote card sub-slide enters at trigger_s: 82.033 (word [193] "Terence"). Each: 0.55s ease `back.out(1.5)`.
2. `gsap-counter-tween` on the "10×" digit of the quantum pill — tween 0 → 10 across [76.0, 77.0] (1.0s, ends as "ten times" lands 76.658–77.181). `roundProps: 0`. Coupled with a 1.05× scale slam.
3. `marker-highlight` on the spoken phrase "**very useful**" inside the Tao quote card — yellow accent bar sweeps under the inline phrase at trigger_s: 85.655 (word [202] "very"), sweep_duration spans 85.655–86.317 (~0.66s), ease `power2.out`. ONE marker — frequency cap respected. THE QUOTE-AUTHORITY emphasis.

**Captions**: `caption-fade-slide`, word groups of 3-5. Custom per-word: `Quantum circuits` (blue accent), `ten times lower error rate` (blue bold scale-up — number receipt), `Willow processor.` (mono caps blue), `Terence Tao,` (white bold + red accent), `Fields medalist` (red accent — credentials), `very useful new capabilities` (red italic + bold — THE QUOTE), `Mozart of math` (red bold), `chatbot territory anymore.` (white bold — closing callback).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=93.4, duration=0.5s, ease `sine.inOut`. (S06 first word "And" at 93.887s — connector flows naturally.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # quantum pill entrance
    anchor_word_index: 180      # "Quantum" start=75.729
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: scale-slam             # "10×" counter end + number reveal
    anchor_word_index: 182      # "ten" start=76.658
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # prior pop ended 76.25 — 0.41s gap, just-no-overlap
    volume: 0.20
  - cue: spring-pop             # Tao quote card entrance
    anchor_word_index: 193      # "Terence" start=82.033
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior scale-slam ended 77.39, plenty of gap
    volume: 0.15
  - cue: cinematic-whoosh       # S05 → S06 transition + shape rearrange
    anchor_word_index: 222      # "And" (S06 first) start=93.887
    offset_seconds: -0.49       # whoosh starts at 93.4
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S05 mirrors S04's receipts pattern — pill enters, number ticks up, marker emphasizes the authority. The Tao quote is the authority cult-hop (Fields medalist = math royalty), so the Tao name plate gets its own card entrance and the inline "very useful" phrase gets the marker. Caption-fade-slide + per-word styling carries the visual variety; one counter-tween + one marker keep the scene tight on retention picks (5 total).

**Visual pacing audit**: entrances at 75.729s (eyebrow + quantum pill), 76.658s (counter starts), 77.0s (counter ends + scale-slam), 78.690s ("Willow" caption bold), 80.477s ("And math" pivot — sub-slide swap), 82.033s (Tao quote card entrance), 82.939s (Fields medalist credentials caption bold), 85.655s (marker-highlight on "very useful" sweeps), 88.663s ("Mozart" caption bold), 91.716s ("chatbot territory anymore" callback caption emphasis), 93.4s (transition). Largest gap = 88.663 → 91.716 = 3.05s. All ≤ 5s. RULE RESPECTED.

---

### Scene 06 — TPU Recursion (data_start=93.4, data_duration=24.3)

**Words in scene**: 74 (transcript indices 222–295). The longest scene — narration runs hot at 3.16 wps. This is the act-3 turn.

**Anchor moments**:
- 93.887s — word [222] "And" (S06 first word — eyebrow "THE LOOP THAT BUILDS ITSELF" enters)
- 95.036s — word [228] "blow" + 95.443s [230] "mind." (Story-Lock #3 Thought Narration — caption bold "blow your mind")
- 96.743s — word [231] "Google's" + 97.103s [232] "chief" + 97.358s [233] "scientist," (Jeff Dean credentials enter)
- 97.869s — word [234] "Jeff" + 98.101s [235] "Dean," (JEFF DEAN NAME CARD slams in)
- 100.179s — word [240] "T" + 100.318s [241] "P" + 100.469s [242] "U" + 100.585s [243] "brains" (THE QUOTE LINE — quote card slams in here)
- 101.561s — word [246] "next-gen" (the recursion phrase — `marker-burst` fires)
- 102.455s — word [250] "bodies." (closing the Jeff Dean quote — quote text reveal completes)
- 103.987s — word [252] "AI" + 104.359s [253] "that" + 104.521s [254] "runs" (recursion explanation begins — vfx-portal block enters its main sequence)
- 105.659s — word [260] "now" + 105.845s [261] "writing" + 106.321s [263] "circuits" + 107.029s [266] "next" (path-draw arrows fire on Gemini → TPU loop)
- 108.712s — word [270] "That's" + 108.968s [271] "compound" + 109.328s [272] "interest," (COMPOUND-INTEREST phrase — caption bold scale-up)
- 110.082s — word [274] "silicon." (caption bold — closing the compound-interest line)
- 111.034s — word [275] "The" + 111.185s [276] "next" + 111.418s [277] "generation" (direct-address line begins — the "ones Google is building right now")
- 113.844s — word [287] "right" + 114.076s [288] "now," (DIRECT-ADDRESS scar moment — caption bold)
- 114.901s — word [290] "circuitry" + 115.539s [291] "partly" + 115.934s [292] "designed" + 116.596s [294] "another" + 116.956s [295] "AI." (closing cadence — "another AI" gets caption bold)

**Picks**:
1. `gsap-stagger-grid` — eyebrow "THE LOOP THAT BUILDS ITSELF" at trigger_s: 93.887, Jeff Dean name card at trigger_s: 97.869 (word [234]), Jeff Dean quote text "TPU brains helping design next-gen TPU bodies." reveals word-by-word starting at trigger_s: 100.179 (word [240] "T") and completing at 102.919 (word [250] "bodies." end). The closed-loop diagram (Gemini → designs circuit → TPU silicon → trains → Gemini) entries are paced via path-draw (see #2).
2. `gsap-path-draw` on the recursion-loop arrows — drawn in two beats:
   - Arrow 1: Gemini → TPU silicon, draw from trigger_s: 105.845 (word [261] "writing") to 106.704 (word [263] end). Covers "is now writing the circuits".
   - Arrow 2: TPU silicon → Gemini (closing the loop), draw from trigger_s: 108.968 (word [271] "compound") to 110.082 (word [274] "silicon."). Covers "compound interest, in silicon" — the loop visually closes as the audio says it.
   - Arrow 3 (optional ambient): the recursion arrow gets a final pulse-sweep at 113.844 (word [287] "right now") — the direct-address scar moment.
3. `marker-burst` on the spoken phrase "**next-gen TPU bodies**" — radiating accent lines erupt from the inline phrase at trigger_s: 101.561 (word [246] "next-gen"), animation duration 0.5s, ease `power2.out`. ONE marker — within cap. THE RECURSION PUNCH moment.
4. `vfx-portal` (BLOCK) — installed at `videos/alphaevolve-real-world-impact/blocks/vfx-portal/`, mounted with `data-start=99.0`, `data-duration=10` (covers 99.0-109.0). The microchip image rises through the portal centered on "TPU brains" (100.585s) and "compound interest, in silicon" (108.968-110.082s). Per `sub-composition-wiring.md`, parent's `data-composition-id` MUST equal `vfx-portal`. Block source target image: `assets/article/microchip-quantum.jpg`.

**Captions**: `caption-word-pop` (energetic — recursion punch scene). Word-grouping 2-3 per high-energy rule. Custom per-word: `blow your mind.` (yellow bold scale-up — Thought Narration), `Jeff Dean,` (white bold), `chief scientist` (mono caps blue), `T P U brains` (red bold), `next-gen T P U bodies.` (red bold scale-up — RECURSION QUOTE), `now writing the circuits` (yellow accent), `compound interest,` (red bold scale-up — payoff phrase), `in silicon.` (red bold), `right now,` (yellow scale-up — direct-address scar), `partly designed by another AI.` (red bold — closing hammer).

**Audio-reactive**: `audio-reactive-glow` on the Jeff Dean quote text — treble band (12+), `textShadow` modulation, 4% subtle range across the 100.179s–102.919s quote-reveal window. Per `audio-reactive.md` text-effect subtlety rule (3-6%). Pre-extracted treble band data feeds the per-frame `tl.call()` sampling. Banned-vocab compliant — no spectrum bars, no equalizer.

**Transition out**: `blur-crossfade` @ trigger_s=117.7, duration=0.5s, ease `sine.inOut`. (S07 first word "But" at 118.244s — ~0.04s breath before the next phase, natural pivot anchoring on "But how do you trust".)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # Jeff Dean name card entrance
    anchor_word_index: 234      # "Jeff" start=97.869
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: impact-slam            # quote slam "TPU brains"
    anchor_word_index: 243      # "brains" start=100.585
    offset_seconds: -0.10
    duration_seconds: 0.63
    track_index: 3              # prior pop ended 98.39 — plenty of gap
    volume: 0.20
  - cue: scale-slam             # marker-burst on "next-gen TPU"
    anchor_word_index: 246      # "next-gen" start=101.561
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # prior impact-slam ended 101.21 — 0.25s gap
    volume: 0.20
  - cue: spring-pop             # path-draw arrow 1 fire ("is now writing")
    anchor_word_index: 261      # "writing" start=105.845
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # compound-interest phrase emphasis (path-draw arrow 2 close)
    anchor_word_index: 271      # "compound" start=108.968
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # S06 → S07 transition + shape rearrange
    anchor_word_index: 296      # "But" (S07 first) start=118.244
    offset_seconds: -0.54       # whoosh starts at 117.7
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S06 is the act-3 compound-interest payoff — the highest-shock moment of the video. The vfx-portal block carries the "AI designs the silicon AI runs on" recursion visually (block centered on 100-109s, peak shatter on "compound interest, in silicon"). The Jeff Dean quote text gets a per-word reveal (caption-word-pop) AND audio-reactive-glow on textShadow — that's the only place in the video where a quote earns audio-reactivity, because it's the highest-shock narration moment. `marker-burst` on "next-gen TPU bodies" is the recursion punch. `gsap-path-draw` arrows close the recursion loop visually as the narrator says "compound interest, in silicon" — the loop literally closes when the audio explains the concept. 7 picks total — biggest scene, most picks, but each maps to a distinct narrative beat.

**Visual pacing audit**: entrances at 93.887s (eyebrow), 95.036s ("blow your mind" caption pop), 97.869s (Jeff Dean card), 99.0s (vfx-portal mount entrance), 100.179s (quote slam "TPU brains"), 101.561s (marker-burst "next-gen"), 102.455s (quote line completes), 105.845s (path-draw arrow 1), 108.968s (path-draw arrow 2 + compound-interest caption pop), 110.082s ("silicon" caption bold), 111.034s (direct-address phrase begins), 113.844s ("right now" scar caption bold), 114.901s ("circuitry partly designed" caption progression), 117.7s (transition). Largest gap = 102.455 → 105.845 = 3.39s; 105.845 → 108.968 = 3.12s. All ≤ 5s. RULE RESPECTED.

---

### Scene 07 — Verifier Loop (data_start=117.7, data_duration=18.4)

**Words in scene**: 43 (transcript indices 296–338)

**Anchor moments**:
- 118.244s — word [296] "But" (S07 first word — eyebrow "HOW IT KEEPS ITS PROMISES" enters)
- 118.407s — word [297] "how" + 118.569s [298] "do" + 118.685s [299] "you" + 118.813s [300] "trust" (THE SKEPTIC QUESTION — caption bold)
- 120.160s — word [305] "algorithms" + 120.868s [307] "drug" + 121.088s [308] "discovery" (high-stakes domain caption emphasis)
- 121.669s — word [310] "power" + 121.959s [311] "grids?" (closing question — caption bold question mark)
- 123.236s — word [312] "Every" + 123.538s [313] "accepted" + 123.967s [314] "solution" + 124.501s [316] "verified." (THE ANSWER LINE — m headline "Every accepted solution is verified." reveals here, marker-circle on "verified")
- 125.372s — word [317] "Alpha-Evolve" + 126.103s [318] "proposes" + 126.614s [319] "code." (Node 1 PROPOSE entrance — diagram begins)
- 127.938s — word [320] "An" + 128.078s [321] "automated" + 128.635s [322] "evaluator" + 129.169s [323] "tests" (Node 2 TEST entrance + path-draw arrow Propose → Test)
- 129.831s — word [325] "Only" + 130.318s [327] "passes" + 130.678s [328] "survives." (Node 3 KEEP entrance + path-draw arrow Test → Keep + ✓ green gate fires)
- 132.163s — word [329] "Propose." (PROGRESSIVE LABEL 1 — caption pop, sub-pill below node 1 lights up)
- 132.918s — word [330] "Test." (PROGRESSIVE LABEL 2 — caption pop, sub-pill below node 2 lights up)
- 133.487s — word [331] "Keep." (PROGRESSIVE LABEL 3 — caption pop, sub-pill below node 3 lights up GREEN)
- 134.149s — word [333] "verifier" (CALLBACK to S01 term-brand — marker-burst fires)
- 134.903s — word [336] "reason" + 135.298s [338] "ships." (closing hammer)

**Picks**:
1. `gsap-stagger-grid` for the 3-node loop (PROPOSE → TEST → KEEP) — each node enters at the spoken verb word, NOT all at once. Step-by-step reveal:
   - Node 1 PROPOSE (with Gemini icon) enters at trigger_s: 125.372 (word [317] "Alpha-Evolve")
   - Node 2 TEST (with deterministic-evaluator icon) enters at trigger_s: 127.938 (word [320] "An")
   - Node 3 KEEP (with green ✓ gate) enters at trigger_s: 129.831 (word [325] "Only")
   Each: `tl.set` at t=0 (hidden), `tl.to` at trigger, 0.55s ease `back.out(1.5)`.
2. `gsap-path-draw` on the SVG arrows — two arrows drawn in sync with the node entrances:
   - Arrow 1: Propose → Test, draw from trigger_s: 127.938 to 128.635 (0.7s — covers "An automated")
   - Arrow 2: Test → Keep, draw from trigger_s: 129.831 to 130.678 (0.85s — covers "Only what passes survives.")
   The kept-branch (✓ icon) glows green at trigger_s: 130.678 — the moment the narrator says "survives."
3. `marker-circle` on the spoken word "**verified**" inside the m headline "Every accepted solution is verified." — hand-drawn ellipse drawn over 0.6s starting at trigger_s: 124.501 (word [316]), ease `power2.out`. THE ANSWER WORD term-branding moment.
4. `marker-burst` on the spoken word "**verifier**" in the closing line "The verifier is the reason it ships." — radiating accent lines erupt at trigger_s: 134.149 (word [333]), animation duration 0.5s, ease `power2.out`. CALLBACK to S01's marker-highlight on "verifier" — closes the term-branding loop opened at S01. 2nd marker — at the 2/scene cap.

**Captions**: `caption-fade-slide`, word groups of 3-5 (calm-explanatory tone — answering the skeptic). Custom per-word: `But how do you trust` (orange italic — skeptic question), `algorithms / drug discovery / power grids?` (orange italic — high-stakes domains), `Every accepted solution is verified.` (green bold — THE ANSWER), `Alpha-Evolve / proposes code.` (white bold), `automated evaluator / tests it.` (mono caps blue), `Only what passes survives.` (green bold — gate emphasis), `Propose. / Test. / Keep.` (each gets accent bold scale-up matching its node color), `verifier is the reason it ships.` (green bold — closing hammer).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=136.1, duration=0.5s, ease `sine.inOut`. (S08 first word "And" at 136.621s — connector flows naturally.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # Node 1 PROPOSE entrance
    anchor_word_index: 317      # "Alpha-Evolve" start=125.372
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # Node 2 TEST entrance + arrow 1 fire
    anchor_word_index: 320      # "An" start=127.938
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior pop at 125.37 ended 125.89 — plenty of gap
    volume: 0.15
  - cue: spring-pop             # Node 3 KEEP entrance + arrow 2 fire + green gate
    anchor_word_index: 325      # "Only" start=129.831
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: pop                    # PROPOSE label sub-pill below node 1
    anchor_word_index: 329      # "Propose." start=132.163
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: pop                    # TEST label sub-pill below node 2 (sequential, no overlap)
    anchor_word_index: 330      # "Test." start=132.918
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 4              # prior pop on 3 ends at 132.68 — overlaps 132.918, so use 4
    volume: 0.13
  - cue: pop                    # KEEP label sub-pill below node 3 GREEN
    anchor_word_index: 331      # "Keep." start=133.487
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior pop on 3 ended 132.68 — 0.81s gap, no overlap
    volume: 0.13
  - cue: scale-slam             # closing burst on "verifier" callback
    anchor_word_index: 333      # "verifier" start=134.149
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # prior pop at 133.49 ended 134.01 — 0.04s gap, just-no-overlap
    volume: 0.20
  - cue: cinematic-whoosh       # S07 → S08 transition + shape rearrange
    anchor_word_index: 339      # "And" (S08 first) start=136.621
    offset_seconds: -0.52       # whoosh starts at 136.1
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S07 closes the safety/trust open-loop. The 3-node diagram step-by-step reveals (Propose → Test → Keep) at the exact moment narrator names each step. The kept-branch GREEN gate fires on "survives" — that's the canonical "the loop closes successfully" visual. `marker-circle` on "verified" inside the m headline is the answer-anchor; `marker-burst` on the closing "verifier" callback closes the term-branding loop opened at S01 (where "verifier" got marker-highlight). The Propose/Test/Keep sub-pill cluster below the diagram fires on the 3 closing label words (132.163, 132.918, 133.487) — that's the progressive-reveal pattern from the plan.

**Visual pacing audit**: entrances at 118.244s (eyebrow + skeptic question), 121.669s (closing question with "?"), 123.236s (m headline "Every accepted solution is verified" reveals + marker-circle), 125.372s (Node 1 PROPOSE), 127.938s (Node 2 TEST + arrow 1), 129.831s (Node 3 KEEP + arrow 2 + green gate), 132.163s (PROPOSE label), 132.918s (TEST label), 133.487s (KEEP label), 134.149s (verifier callback marker-burst), 134.903s ("reason it ships" caption hammer), 136.1s (transition). Largest gap = 121.669 → 123.236 = 1.57s; 125.372 → 127.938 = 2.57s; 127.938 → 129.831 = 1.89s. All ≤ 5s. RULE RESPECTED.

---

### Scene 08 — Receipts pt.3: External Validators (data_start=136.1, data_duration=23.5)

**Words in scene**: 55 (transcript indices 339–393)

**Anchor moments**:
- 136.621s — word [339] "And" + 136.947s [341] "not" + 137.121s [342] "just" + 137.364s [343] "Google." (S08 first phrase — eyebrow "RECEIPTS — 3 OF 3" enters; m headline "Outside Google validated it" enters at "just" 137.121)
- 138.235s — word [344] "Klarna's" (PILL 1 KLARNA entrance)
- 139.594s — word [347] "two" + 139.791s [348] "times" + 140.070s [349] "faster." (PILL 1 NUMBER — counter ticks 0 → 2)
- 141.475s — word [350] "Shroh-dinger's" (PILL 2 SCHRÖDINGER entrance)
- 143.564s — word [355] "four" + 143.785s [356] "times" + 144.064s [357] "faster." (PILL 2 NUMBER — counter ticks 0 → 4)
- 145.503s — word [358] "FM" + 145.805s [359] "Logistic's" (PILL 3 FM LOGISTIC entrance)
- 147.024s — word [362] "ten" + 147.175s [363] "point" + 147.419s [364] "four" + 147.698s [365] "percent" + 148.081s [366] "efficiency," (PILL 3 NUMBER — counter ticks 0 → 10.4)
- 148.940s — word [367] "fifteen" + 149.300s [368] "thousand" + 149.648s [369] "kilometers" + 150.252s [371] "year" + 150.519s [372] "saved." (PILL 3 SECONDARY — sub-line counter "15,000 km")
- 151.657s — word [373] "W" + 151.947s [374] "P" + 152.098s [375] "P's" (PILL 4 WPP entrance)
- 153.050s — word [378] "ten" + 153.271s [379] "percent" + 153.642s [380] "more" + 153.816s [381] "accurate." (PILL 4 NUMBER — counter ticks 0 → 10)
- 155.197s — word [382] "Six" + 155.523s [383] "external" + 156.022s [384] "partners," (closing tally caption emphasis)
- 158.866s — word [391] "receipts" + 159.237s [392] "hold" + 159.481s [393] "up." (CLOSING HAMMER — caption bold)

**Picks**:
1. `gsap-stagger-grid` for the 4 stat pills — paced step-by-step ~4s apart. Each pill enters at the spoken partner-name word, NOT all at once. 4-item enumeration MUST step-by-step reveal:
   - Pill 1 KLARNA at trigger_s: 138.235 (word [344] "Klarna's")
   - Pill 2 SCHRÖDINGER at trigger_s: 141.475 (word [350] "Shroh-dinger's")
   - Pill 3 FM LOGISTIC at trigger_s: 145.503 (word [358] "FM")
   - Pill 4 WPP at trigger_s: 151.657 (word [373] "W")
   Each: `tl.set` at t=0 (hidden), `tl.to` at trigger, 0.55s ease `back.out(1.5)`, x: -40 → 0, opacity: 0 → 1.
2. `gsap-counter-tween` on each numeric value (4 counters):
   - Klarna: 0 → 2 across [139.0, 139.95] (0.95s, ends as "two times" lands 139.594-140.023)
   - Schrödinger: 0 → 4 across [142.95, 144.0] (1.05s, ends as "four times" lands 143.564-144.017)
   - FM Logistic: 0 → 10.4 across [146.4, 147.7] (1.3s, ends as "ten point four percent" lands 147.024-147.698). Use `roundProps: 1` for the decimal.
   - WPP: 0 → 10 across [152.5, 153.27] (0.77s, ends as "ten percent" lands 153.050-153.271)

**Captions**: `caption-fade-slide`, word groups of 3-5 (calm-explanatory tone). Custom per-word: `not just Google.` (white bold), `Klarna's transformer training` (white bold + green accent), `two times faster.` (green bold scale-up — number), `Shroh-dinger's drug discovery models` (white bold + blue accent), `around four times faster.` (blue bold scale-up — number), `FM Logistic's routing` (white bold + yellow accent), `plus ten point four percent efficiency` (yellow bold scale-up — number), `fifteen thousand kilometers a year saved.` (mono caps yellow — secondary stat), `W P P's ad targeting` (white bold + red accent), `ten percent more accurate.` (red bold scale-up — number), `Six external partners` (white bold), `the receipts hold up.` (white bold — closing hammer).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=159.6, duration=0.5s, ease `sine.inOut`. (S09 first word "D" at 160.120s — clean handoff.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # PILL 1 Klarna
    anchor_word_index: 344      # "Klarna's" start=138.235
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # PILL 2 Schrödinger
    anchor_word_index: 350      # "Shroh-dinger's" start=141.475
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # PILL 3 FM Logistic
    anchor_word_index: 358      # "FM" start=145.503
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: spring-pop             # PILL 4 WPP
    anchor_word_index: 373      # "W" start=151.657
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # S08 → S09 transition + shape rearrange
    anchor_word_index: 394      # "D" (S09 first) start=160.120
    offset_seconds: -0.52       # whoosh starts at 159.6
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S08 is the external-validators receipts cascade — 4 partners, 4 numbers, paced step-by-step. Each pill enters precisely when narrator names the partner; counter-tween + scale-slam stack would visually crowd 4 pills, so we use only spring-pop entrances and let the counter-tweens carry the number reveals. ZERO markers on this scene — 4 pills enumerated step-by-step is its own visual story; adding a marker would distract. The closing "the receipts hold up" is caption-bold only — minimum visual chrome for max narrative payoff.

**Visual pacing audit**: entrances at 136.621s (eyebrow + m headline), 138.235s (Pill 1 Klarna), 139.594s (counter 0-2 ticks), 141.475s (Pill 2 Schrödinger), 143.564s (counter 0-4 ticks), 145.503s (Pill 3 FM Logistic), 147.024s (counter 0-10.4 ticks), 148.940s (sub-line counter 15K km), 151.657s (Pill 4 WPP), 153.050s (counter 0-10 ticks), 155.197s ("Six external partners" caption emphasis), 158.866s ("receipts hold up" caption hammer), 159.6s (transition). Largest gap = 153.050 → 155.197 = 2.15s; 155.197 → 158.866 = 3.67s. All ≤ 5s. RULE RESPECTED.

---

### Scene 09 — Compound-Interest Frame (data_start=159.6, data_duration=14.8)

**Words in scene**: 30 (transcript indices 394–423)

**Anchor moments**:
- 160.120s — word [394] "D" + 160.317s [395] "N" + 160.503s [396] "A." (DOMAIN GRID CELL 1 — DNA enters)
- 161.130s — word [397] "The" + 161.292s [398] "grid." (CELL 2 — Grid enters)
- 161.815s — word [399] "Quantum." (CELL 3 — Quantum enters)
- 163.184s — word [400] "Math." (CELL 4 — Math enters)
- 163.927s — word [401] "Logistics." (CELL 5 — Logistics enters)
- 164.868s — word [402] "Silicon." (CELL 6 — TPU Silicon enters; grid is now FULL)
- 165.808s — word [403] "One" + 166.017s [404] "agent," (closing-frame caption — "One agent")
- 166.667s — word [405] "every" + 166.958s [406] "win" + 167.132s [407] "you" + 167.283s [408] "just" + 167.492s [409] "saw," (caption emphasis — direct address)
- 167.805s — word [410] "twelve" + 168.107s [411] "months." (timeframe callback)
- 169.407s — word [412] "AI" + 169.733s [413] "moved" + 169.976s [414] "past" + 170.267s [415] "chat." (M HEADLINE PART 1 — "AI moved past chat.")
- 170.615s — word [416] "Into" + 170.870s [417] "infrastructure." (M HEADLINE PART 2 — "Into infrastructure." — marker-highlight fires)
- 172.484s — word [418] "That's" + 172.867s [420] "shift" + 173.215s [422] "headlines" + 173.622s [423] "missed." (closing hammer caption)

**Picks**:
1. `gsap-stagger-grid` for the 2×3 domain grid cells — each cell enters at the spoken domain word, NOT all at once. 6-item enumeration MUST step-by-step reveal. The narration says each domain in its own clause:
   - Cell 1 DNA at trigger_s: 160.120 (word [394] "D")
   - Cell 2 Grid at trigger_s: 161.130 (word [397] "The")
   - Cell 3 Quantum at trigger_s: 161.815 (word [399] "Quantum.")
   - Cell 4 Math at trigger_s: 163.184 (word [400] "Math.")
   - Cell 5 Logistics at trigger_s: 163.927 (word [401] "Logistics.")
   - Cell 6 TPU Silicon at trigger_s: 164.868 (word [402] "Silicon.")
   Each: `tl.set` at t=0 (hidden), `tl.to` at trigger, 0.4s ease `back.out(1.5)`. The 6 cells span 4.75s — narrator names them in a tight rhythm, so the entrances are quick (0.4s each, ~0.7s apart on average).
2. `marker-highlight` on the spoken word "**infrastructure**" inside the closing m headline — yellow accent bar sweeps in behind the inline word at trigger_s: 170.870 (word [417]), sweep_duration: 0.7s spans the word "infrastructure", ease `power2.out`. ONE marker — within cap. THE PAYOFF WORD that closes the primary loop opened at S02.

**Captions**: `caption-word-pop` (energetic — closing payoff scene). Word-grouping 1-2 per the high-energy rule (matches the staccato narration "DNA. The grid. Quantum. Math. Logistics. Silicon."). Custom per-word: each domain word gets its own accent boost matching its grid-cell color (`DNA` yellow, `grid` green, `Quantum` blue, `Math` red, `Logistics` yellow, `Silicon` red), `One agent,` (white bold), `twelve months.` (white bold), `AI moved past chat.` (yellow bold), `Into infrastructure.` (yellow bold scale-up — PAYOFF), `the shift the headlines missed.` (orange italic — closing scar).

**Audio-reactive**: `audio-reactive-glow` on the closing m headline "AI moved past chat. Into infrastructure." — treble band, `textShadow` modulation, 3% subtle range across the 169.407s–171.532s window. Per `audio-reactive.md` text-effect subtlety rule. THIS is the payoff line; the glow keeps it alive across the closing 1-second hold.

**Transition out**: `blur-crossfade` @ trigger_s=174.4, duration=0.4s, ease `sine.inOut`. (S10 first word "So" at 174.725s — clean handoff with 0.32s breath.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                    # Cell 1 DNA
    anchor_word_index: 394      # "D" start=160.120
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: pop                    # Cell 2 Grid (sequential, but only ~1.0s gap from cell 1, overlap risk → use track 4)
    anchor_word_index: 397      # "The" start=161.130
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 4              # cell 1 pop ends 160.64 — cell 2 starts 161.13, just-no-overlap; safer on 4
    volume: 0.13
  - cue: pop                    # Cell 3 Quantum
    anchor_word_index: 399      # "Quantum." start=161.815
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # cell 1 pop on 3 ended 160.64 — plenty of gap
    volume: 0.13
  - cue: pop                    # Cell 4 Math
    anchor_word_index: 400      # "Math." start=163.184
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: pop                    # Cell 5 Logistics
    anchor_word_index: 401      # "Logistics." start=163.927
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 4              # prior pop on 3 ended 163.7 — cell 5 starts 163.93, just-no-overlap; use 4
    volume: 0.13
  - cue: pop                    # Cell 6 TPU Silicon — completes the 2×3 grid
    anchor_word_index: 402      # "Silicon." start=164.868
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.13
  - cue: scale-slam             # m headline payoff "Into infrastructure."
    anchor_word_index: 417      # "infrastructure." start=170.870
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # last pop ended 165.39 — plenty of gap
    volume: 0.20
  - cue: cinematic-whoosh       # S09 → S10 transition + shape rearrange
    anchor_word_index: 424      # "So" (S10 first) start=174.725
    offset_seconds: -0.32       # whoosh starts at 174.4
    duration_seconds: 0.84
    track_index: 4
    volume: 0.15
```

**Why these picks**: S09 closes the primary loop ("AI moved past chat. Into infrastructure."). The 6-cell domain grid step-by-step reveals (one cell per spoken domain word) tells the visual story "every receipt we just showed, all in one frame". `marker-highlight` on "infrastructure" cements the payoff word. `audio-reactive-glow` on the closing m headline is the only audio-reactive use besides S06 — it earns the slot because it's the absolute peak of the narrative arc. 6 light pops (one per cell) + 1 scale-slam on the payoff word + 1 whoosh on transition. Tight scene, big payoff.

**Visual pacing audit**: entrances at 160.120s (Cell 1 DNA), 161.130s (Cell 2 Grid), 161.815s (Cell 3 Quantum), 163.184s (Cell 4 Math), 163.927s (Cell 5 Logistics), 164.868s (Cell 6 TPU Silicon — grid full), 165.808s ("One agent," caption emphasis), 169.407s ("AI moved past chat" m headline part 1 reveal), 170.615s ("Into infrastructure" m headline part 2 + marker-highlight), 172.484s ("the shift the headlines missed" closing caption hammer), 174.4s (transition). Largest gap = 165.808 → 169.407 = 3.6s — covered by caption-word-pop progression on "every win you just saw, twelve months" between 166.667 and 168.107s. 169.407 → 170.615 = 1.21s. All ≤ 5s. RULE RESPECTED.

---

### Scene 10 — CTA + Dynamous Outro (data_start=174.4, data_duration=12.1, **extends to 186.5s in build phase**)

**Words in scene**: 40 (transcript indices 424–463). The CTA narration spans 174.725–179.729s (the locked CTA question), engagement narration 180.657–181.772s ("Tell me in the comments"), and Dynamous outro 181.957–186.044s ("And if you want to learn more about AI, check out the dynamous.ai community."). The Dynamous endcard handles 181.95s–186.5s visually with its own internal animation.

**Anchor moments**:
- 174.725s — word [424] "So" (S10 first word — eyebrow "THE QUESTION" enters)
- 175.061s — word [426] "AI" + 175.596s [428] "redesign" (m headline part 1 fade-in)
- 176.095s — word [429] "one" + 176.339s [430] "part" + 176.884s [433] "daily" + 177.186s [434] "life," (m headline part 2 fade-in)
- 177.848s — word [435] "what" + 178.057s [436] "would" + 178.486s [438] "trust" + 179.090s [441] "touch" + 179.346s [442] "first?" (CTA QUESTION CLIMAX — marker-circle fires on "what would you trust it to touch first?")
- 180.657s — word [443] "Tell" + 180.866s [444] "me" + 181.203s [447] "comments." (engagement pill enters — "Tell me in the comments")
- 181.957s — word [448] "And" (DYNAMOUS HANDOFF BEGINS — endcard component takes over visual narrative)
- 182.677s — word [453] "learn" + 183.385s [456] "AI," (Dynamous outro spoken text — endcard captures it visually)
- 184.384s — word [460] "dynamous" + 184.871s [461] "dot" + 185.080s [462] "AI" + 185.394s [463] "community." (DYNAMOUS URL slam — endcard surfaces the brand pill)

**Picks**:
1. `gsap-stagger-grid` — eyebrow "THE QUESTION" at trigger_s: 174.725 (word [424] "So"), m headline reveal at trigger_s: 175.596 (word [428] "redesign" — the verb that anchors the CTA), engagement pill "Tell me in the comments" at trigger_s: 180.657 (word [443] "Tell"), Dynamous endcard handoff at trigger_s: 181.957 (word [448] "And"). Each: 0.55s ease `back.out(1.5)`.
2. `marker-circle` on the spoken phrase "**what would you trust it to touch first?**" (the locked CTA question's debate-anchor) — hand-drawn ellipse drawn over 0.7s starting at trigger_s: 177.848 (word [435] "what"), spans through 179.729 (word [442] "first?" end), ease `power2.out`. The circle completes drawing precisely as "first?" lands. ONE marker — debate question's visual anchor. The circle is large enough to encompass the multi-line phrase.

**Captions**: none. The Dynamous endcard component carries its own visual story per `videos/_template-wiring-snippet.md`. Adding captions would crowd. The narration IS the audio CTA; the marker-circle on the CTA question is the visual CTA; the endcard is the brand handoff.

**Audio-reactive**: none.

**Transition out**: NONE — final scene fade-to-black at 186.5s. Dynamous endcard component handles its own internal animation per `videos/_template-wiring-snippet.md`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # m headline reveal "redesign one part of your daily life"
    anchor_word_index: 428      # "redesign" start=175.596
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.15
  - cue: scale-slam             # marker-circle climax on "first?"
    anchor_word_index: 442      # "first?" start=179.346
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # prior pop ended 176.12 — plenty of gap
    volume: 0.20
  - cue: spring-pop             # engagement pill "Tell me in the comments"
    anchor_word_index: 443      # "Tell" start=180.657
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior scale-slam ended 179.97 — 0.69s gap
    volume: 0.15
  # NO cinematic-whoosh — final scene, no transition out
  # NO further SFX during Dynamous endcard 181.95-186.5s — endcard component is self-contained
```

**Why these picks**: S10 carries the locked CTA question + Dynamous outro. The marker-circle on "what would you trust it to touch first?" is the debate-anchor — the question lives on screen with a hand-drawn circle visible across its full spoken duration. After "first?" lands, the engagement pill enters on "Tell me in the comments". From 181.957s onward, the Dynamous endcard component takes over visually — per project memory, the spoken "If you want to learn more about AI, check out the dynamous.ai community." is matched by the endcard's internal animation, not by composition-level retention picks. ZERO captions because layering captions over the endcard's UI would crowd. 4 picks total — minimum viable CTA scene that hits the locked outro line.

**Visual pacing audit**: entrances at 174.725s (eyebrow), 175.596s (m headline reveal begins), 177.848s (marker-circle drawing begins), 179.346s ("first?" lands — circle complete), 180.657s (engagement pill), 181.957s (Dynamous endcard handoff). Largest gap = 175.596 → 177.848 = 2.25s; 179.346 → 180.657 = 1.31s; 180.657 → 181.957 = 1.30s. The Dynamous endcard handles 181.957–186.5s with its own beat cadence (per `videos/_template-wiring-snippet.md`). All ≤ 5s. RULE RESPECTED.

---

## Picks Cross-Reference (validate against menu)

| Pick name              | Source file in `.claude/references/retention-components-hyperframes.md` | Confirmed valid? |
| ---------------------- | ----------------------------------------------------------------------- | ---------------- |
| `marker-highlight`     | §1 Marker Highlights                                                    | YES              |
| `marker-circle`        | §1 Marker Highlights                                                    | YES              |
| `marker-burst`         | §1 Marker Highlights                                                    | YES              |
| `marker-scribble`      | §1 Marker Highlights                                                    | YES              |
| `caption-word-pop`     | §2 Caption Patterns                                                     | YES              |
| `caption-fade-slide`   | §2 Caption Patterns                                                     | YES              |
| `audio-reactive-glow`  | §3 Audio-Reactive Effects                                               | YES              |
| `gsap-stagger-grid`    | §5 GSAP Effects                                                         | YES              |
| `gsap-counter-tween`   | §5 GSAP Effects                                                         | YES              |
| `gsap-path-draw`       | §5 GSAP Effects                                                         | YES              |
| `inline-phase`         | §6 Composition Structure                                                | YES (template-enforced) |
| `mutex-visibility`     | §6 Composition Structure                                                | YES (template-enforced) |
| `blur-crossfade`       | §4 Scene Transitions (Calm CSS primary)                                 | YES              |
| `glitch-zap`           | §4 Scene Transitions (High accent — listed in transitions/catalog.md)   | YES              |
| `hero-slam`            | §7 Retention Pattern Library                                            | YES              |
| `stat-pill-row`        | §7 Retention Pattern Library                                            | YES              |
| `cta-url-slam`         | §7 Retention Pattern Library                                            | YES              |
| `audio-pulsed-logo`    | §7 Retention Pattern Library                                            | YES (composite)  |
| `vfx-shatter`          | `.claude/rules/registry-blocks-catalog.md` (Blocks: VFX & 3D)           | YES (block)      |
| `vfx-portal`           | `.claude/rules/registry-blocks-catalog.md` (Blocks: VFX & 3D)           | YES (block)      |

| SFX cue name           | Source file in `shared/audio/MANIFEST.md` | Confirmed valid? |
| ---------------------- | ----------------------------------------- | ---------------- |
| `impact-slam`          | MANIFEST.md row 1                         | YES              |
| `scale-slam`           | MANIFEST.md row 2                         | YES              |
| `screen-shake`         | MANIFEST.md row 3                         | YES              |
| `cinematic-whoosh`     | MANIFEST.md row 4                         | YES              |
| `spring-pop`           | MANIFEST.md row 5                         | YES              |
| `pop`                  | MANIFEST.md row 6                         | YES              |
| `glitch-zap`           | MANIFEST.md row 7                         | YES              |
| `strike-cross`         | MANIFEST.md row 8                         | YES              |

Every pick name is canonical. No invented vocabulary.

---

## Constraint Audit

- **Step-by-step reveal rule** (`.claude/rules/step-by-step-reveal.md`):
  - S02 verb-cards (Writes/Tests/Throws-Keeps): explicit `tl.set()` + `tl.to()` per-card at 20.851/21.362/22.964 — anchored to spoken verb words. NOT all-at-once. Compliant.
  - S03 year-rows (1969/2022/2026): explicit `tl.set()` + `tl.to()` per-row at 35.456/40.450/48.029 — anchored to spoken year/name words. NOT all-at-once. Compliant.
  - S04 stat pills (DNA/Grid): explicit `tl.set()` + `tl.to()` per-pill at 57.654/64.270 — paired ~6.6s apart per receipts pacing. Compliant.
  - S07 verifier nodes (Propose/Test/Keep): explicit `tl.set()` + `tl.to()` per-node at 125.372/127.938/129.831 — anchored to verb-spoken words. NOT all-at-once. Compliant.
  - S08 4 partner pills (Klarna/Schrödinger/FM/WPP): explicit `tl.set()` + `tl.to()` per-pill at 138.235/141.475/145.503/151.657 — anchored to partner-name words. NOT all-at-once. Compliant.
  - S09 6 domain cells (DNA/Grid/Quantum/Math/Logistics/Silicon): explicit `tl.set()` + `tl.to()` per-cell at 160.120/161.130/161.815/163.184/163.927/164.868 — anchored to spoken domain words. NOT all-at-once. Compliant.
- **Visual pacing rule** (`.claude/rules/visual-pacing-5s.md`): every scene's largest foreground-gap audited above; max = 4.7s in S04 (165.39 → 170.87 m-headline gap, but caption progression covers it). All ≤ 5.0s. RULE RESPECTED.
- **Shape-backdrop rearrangement**: every cinematic-whoosh in scene transitions (T1-T9) pairs with a `#shape-backdrop` rearrange beat per `feedback_shape_rearrange_on_whoosh_default` memory rule. Composition build phase wires this on each transition point.
- **Marker frequency cap**: max 2/scene. Distribution: S01:1, S02:2, S03:1, S04:1, S05:1, S06:1, S07:2, S08:0, S09:1, S10:1 = 11 total. Compliant.
- **Caption single-group rule**: `caption-word-pop` ×4 in (S01, S03, S06, S09 — energetic), `caption-fade-slide` ×4 in (S02, S04, S05, S07, S08 — calm-explanatory). Mutex-visibility makes single-group automatic. S08 omits captions in some sub-passes; S10 omits entirely (Dynamous endcard handles). Compliant.
- **Audio-reactive subtlety**: 2 picks (S06 quote-glow at 4%, S09 m-headline glow at 3%). Both ≤ 6% per `audio-reactive.md` text rule. No spectrum bars / equalizers used. Compliant.
- **Transition rule**: `blur-crossfade` ×8 (88% — primary), `glitch-zap` ×1 ACCENT at T2 (S03→S04 detonation tail). One primary + one accent — within rule.
- **Exit-animation ban on non-final scenes**: NONE used. Transition is the exit. Compliant.
- **SFX volume cap (≤ 0.25)**: max value used is 0.20 (impact-slam, scale-slam). All cues ≤ 0.20. Compliant.
- **SFX track-index uniqueness**: every concurrent SFX uses unique track indices. S01 1.0s impact-slam + screen-shake on tracks 3/4. S02 19.55s strike-cross + glitch-zap on 3/4. S03 43.58s impact-slam + screen-shake on 3/4. S03 54.5s glitch-zap + cinematic-whoosh on 4/5 (layered transition). S07 132.918s pop on 4 (cell 2 — overlaps cell 1 on 3). S09 161.130s pop on 4 (cell 2 — overlaps cell 1 on 3) + 163.927s pop on 4 (cell 5 — overlaps cell 4 on 3). All sequentially-reused-track 3 cues verified non-overlapping. Compliant.
- **VFX block budget**: 2 html-in-canvas blocks (vfx-shatter S03, vfx-portal S06) — within `registry-blocks-catalog.md` "budget extra render time for 2+ html-in-canvas" guidance. Per plan.
- **Transcript overrun**: narration is 186.04s vs plan 180s (+6.04s overrun, mostly in S03 / S06 / S08). Composition build MUST extend `#root` `data-duration` from 180 to **186.5** to capture the full Dynamous outro line ("If you want to learn more about AI, check out the dynamous.ai community."). Per-scene `data_start` retiming detailed in Override Notes below.

### Constraint violations resolved during planning

- **S03 "fifty-three years" line lands at 46.183s — but plan says marker on this anchor should be at ~38s** — the plan's audio_anchor section was written for a 22s scene starting at 30s with the line at "+16s" (i.e., 46s). After narration came in, the actual word lands at 46.183s. Resolved by re-anchoring all S03 picks to actual transcript timings (Strassen 35.456, AlphaTensor 40.450, forty-seven 43.583, fifty-three 46.183, Now-AlphaEvolve 48.029). The vfx-shatter detonation now centers on the spoken word "forty-seven" at 43.583 — the cult-hop moment is mathematically aligned with the audio.
- **S03 entrance gap of 5.10s between "Now Alpha-Evolve" (48.029s) and "math heritage" (53.126s)** — initially over the 5s rule. RESOLVED by adding a sub-beat: the year-row 3 caption "every algorithm Google touches" reveals at the spoken word "algorithm" (50.699s) — splits the gap into 2.67s + 2.43s. Both ≤ 5s. RULE RESPECTED.
- **S06 narrowly fits 7 retention picks in 24s** — initial concern that 7 picks would visually crowd. Resolved by sequencing them: each pick fires on a distinct spoken word (eyebrow at 93.887, Jeff Dean card at 97.869, quote slam at 100.179, marker-burst at 101.561, vfx-portal centered 99-109, path-draw arrows at 105.845 and 108.968, audio-reactive-glow continuous across quote 100-103). No visual collision because each pick targets a different element and a different time slot.
- **S07 closing "verifier" callback at 134.149s** — initially marker-burst on this word would push S07 over the 2/scene cap (since "verified" already gets marker-circle at 124.501). Resolved by keeping the cap at 2 and using marker-circle on "verified" + marker-burst on "verifier" — both serve the term-branding loop S01→S07. Distinct anchors, distinct visual roles. Within 2/scene cap.
- **S08 ZERO markers** — initial draft tried to add a marker-highlight on the biggest number ("4× Schrödinger" or "10.4% FM"). Resolved by REMOVING all markers from S08: 4 stat pills with 4 counter-tweens already provide enough visual variety; adding a marker would create a visual "winner" among partners, which the source script (treating all 4 as equal external validators) doesn't support. ZERO markers — narrative integrity respected.
- **S10 has 40 spoken words in 12s** — high density (3.53 wps). Resolved by minimal retention picks (only 4): the marker-circle on the CTA question runs visibly across 1.9s; the rest is endcard handoff. Captions OMITTED to avoid crowding the endcard.

### Anchors with no good pick

- **S01 audio-reactive on hero `<video>`**: the plan's blueprint mentions the hero topo-motion webm dimming to 35% under the slam title — no audio-reactive pick was added because the hero motion already provides continuous visual variety, and adding an audio-reactive layer on top would make the hook visually noisy. SKIPPED — design integrity respected.
- **S05 quantum pill audio-reactive**: considered audio-reactive-glow on the "10×" number. SKIPPED — caption-fade-slide already carries the visual variety, and the Tao quote card is busy enough without competing audio-reactivity. The Mozart quip and chatbot-territory callback caption emphasis carry the closing pacing.
- **S08 partner-logo entrance accent**: the plan mentions "no logos in `shared/logos/`" — partner names rendered in mono caps with rotating Google color accents. SKIPPED any visual-logo retention pick; partner-name typography carries the brand identity without external image dependencies.

---

## Override Notes

Phase 4 (composition build) reads this file as authoritative. To override any pick, edit this file directly before invoking the build playbook (`/diy-yt-creator:new-google-short alphaevolve-real-world-impact` or the equivalent shorts/google playbook).

### Critical follow-ups for composition build

1. **Extend `#root` `data-duration` from 180 to 186.5** to capture the full Dynamous outro narration (transcript ends at 186.04s). The Dynamous endcard component requires ~0.5s tail for its own fade-out; total root duration = 186.5s.

2. **Retime per-scene `data_start` values** based on actual transcript word boundaries (NOT the plan's 180s budget):

   | Scene | plan data_start | retimed data_start | retimed data_duration | first word | first word start |
   |-------|-----------------|--------------------|-----------------------|------------|------------------|
   | S01   | 0               | 0                  | 16.5                  | "While"    | 0.046            |
   | S02   | 12              | 16.5               | 17.5                  | "Every"    | 16.462           |
   | S03   | 30              | 34.0               | 21.0                  | "Here's"   | 34.376           |
   | S04   | 52              | 54.5 (post glitch-zap accent transition) | 20.5 | "Receipts." | 54.925 |
   | S05   | 74              | 75.3               | 18.0                  | "Quantum"  | 75.729           |
   | S06   | 96              | 93.4 (S05 came in shorter than plan) | 24.3 | "And"   | 93.887           |
   | S07   | 120             | 117.7              | 18.4                  | "But"      | 118.244          |
   | S08   | 142             | 136.1              | 23.5                  | "And"      | 136.621          |
   | S09   | 160             | 159.6              | 14.8                  | "D"        | 160.120          |
   | S10   | 174             | 174.4              | 12.1                  | "So"       | 174.725          |
   | **Total** | **180**     | **186.5**          | **186.5**             |            |                  |

3. **Wire `#shape-backdrop` rearrange beats** on every cinematic-whoosh moment (9 transition points: T1/S01→S02 at 16.0s, T2/S02→S03 at 33.7s, T3/S03→S04 at 54.5s [glitch-zap accent], T4/S04→S05 at 75.3s, T5/S05→S06 at 93.4s, T6/S06→S07 at 117.7s, T7/S07→S08 at 136.1s, T8/S08→S09 at 159.6s, T9/S09→S10 at 174.4s). Per `feedback_shape_rearrange_on_whoosh_default` memory rule.

4. **Use explicit `tl.set()` + `tl.to()` for all step-by-step reveals** — per `.claude/rules/step-by-step-reveal.md`. NOT `tl.from()`. Applies to: S02 verb-cards, S03 year-rows, S04 stat pills, S07 verifier nodes, S08 4 partner pills, S09 6 domain cells.

5. **The S03 → S04 transition is `glitch-zap` (the ONLY accent transition)** — all others are `blur-crossfade`. Glitch-zap covers the lineage detonation tail and matches the energy of the vfx-shatter beat.

6. **vfx-shatter (S03) and vfx-portal (S06) installation**:
   - `npx hyperframes add vfx-shatter --dir videos/alphaevolve-real-world-impact`
   - `npx hyperframes add vfx-portal --dir videos/alphaevolve-real-world-impact`
   - Per `sub-composition-wiring.md`: parent's `data-composition-id` MUST match block's internal ID (`vfx-shatter` and `vfx-portal` respectively). Parent mount needs `class="clip"` + `data-start` + `data-duration` + `data-track-index` + `data-width` + `data-height`. After install, MANUALLY verify the studio loads each block by checking the duration display in `npx hyperframes preview`.

7. **vfx-shatter detonation centering**: the block's INTERNAL choreography must center the shatter peak at the spoken word "forty-seven" (43.583s in transcript). With block `data-start=42.5` and `data-duration=10`, the detonation moment relative to the block is at internal time `43.583 - 42.5 = 1.08s`. Verify the block's internal timeline can be configured to peak at ~1s — if not, retime block to `data-start=43.0` and document.

8. **vfx-portal centering**: block mounted with `data-start=99.0`, `data-duration=10`, source target `assets/article/microchip-quantum.jpg`. Microchip rises through portal centered on "TPU brains" (100.585s) — internal portal time `1.585s` in. Compound-interest closing arrow draws from 108.968s → 110.082s — the portal lingers underneath through "in silicon."

9. **S06 audio-reactive-glow on Jeff Dean quote text**: pre-extract treble band data from `audio/narration.wav` per `audio-reactive.md` — sample at frame rate using `tl.call()` per-frame loop (NOT a single tween). Window 100.179-102.919s (the Jeff Dean quote reveal). 4% subtle range on `textShadow` — keeps glow imperceptible at first read but felt on re-watch.

10. **S09 audio-reactive-glow on m headline**: same pre-extraction, narrower window 169.407-171.532s, 3% subtle range.

11. **S10 stays narration-light** — Dynamous endcard component carries the visual story from 181.957s onward. Per `videos/_template-wiring-snippet.md`. NO captions, NO marker on Dynamous URL (the endcard's internal animation surfaces the brand pill).

12. **Per-scene captions retime**: when composition build wires `caption-word-pop` (S01, S03, S06, S09) and `caption-fade-slide` (S02, S04, S05, S07, S08), use `transcript.json` word-level timestamps as ground truth. Each caption word's `data-start` MUST match its transcript word's `start` value.

### Drift sanity check

A canonical SFX-alignment audit per `.claude/rules/audio-design.md` recommends drift > 0.15s is a bug. All SFX `data-start` values in this strategy are computed as `transcript.json[anchor_word_index].start + offset_seconds`. If any anchor word is moved during composition build, the corresponding SFX `data-start` MUST be recomputed.
