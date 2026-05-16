# Retention Strategy: claude-managed-agents-launch

Source-grounded, transcript-anchored retention picks for each of the 9 scenes (S00–S08). Every component name below is a canonical entry from `.claude/references/retention-components-hyperframes.md`. Every SFX cue is verified against `shared/audio/MANIFEST.md`. All trigger times are seconds, anchored to `transcript.json` word `start` values (337 words, 134.49s total narration; transcript runs ~4.3s past plan boundary because the Dynamous outro extends to 134.3s — composition build will extend `#root` `data-duration` from 130 to 135 to absorb the tail).

---

## Summary Table

| Scene                  | Pattern (from §7)        | Primitives                                                  | Captions             | Audio-Reactive | Transition Out (start_s, dur) | Total Picks |
| ---------------------- | ------------------------ | ----------------------------------------------------------- | -------------------- | -------------- | ----------------------------- | ----------- |
| S00 Preview Hook       | hero-slam                | gsap-stagger-grid, marker-highlight                         | none                 | none           | blur-crossfade @ 6.6, 0.5s    | 4           |
| S01 Open Loop          | stat-pill-row (adapted)  | gsap-counter-tween, marker-circle                           | none                 | none           | blur-crossfade @ 14.5, 0.5s   | 4           |
| S02 Four Pillars       | stat-pill-row (4-pill)   | gsap-stagger-grid, marker-highlight                         | caption-fade-slide   | none           | blur-crossfade @ 31.5, 0.5s   | 5           |
| S03 Dreaming           | narrated-stat-reveal     | gsap-stagger-grid, gsap-path-draw, marker-circle            | caption-fade-slide   | none           | blur-crossfade @ 49.5, 0.5s   | 6           |
| S04 Outcomes           | narrated-stat-reveal     | gsap-stagger-grid, gsap-counter-tween, marker-highlight     | caption-fade-slide   | none           | zoom-through @ 67.7, 0.3s     | 6           |
| S05 Multiagent         | timeline-cards (4-col)   | gsap-stagger-grid, gsap-counter-tween, marker-burst         | caption-fade-slide   | none           | blur-crossfade @ 85.5, 0.5s   | 6           |
| S06 Webhooks           | stat-pill-row (vs)       | gsap-stagger-grid, marker-scribble                          | caption-fade-slide   | none           | blur-crossfade @ 98.5, 0.5s   | 5           |
| S07 Trust Strip        | stat-pill-row (3-elem)   | gsap-stagger-grid, gsap-typewriter                          | caption-fade-slide   | none           | blur-crossfade @ 113.5, 0.5s  | 5           |
| S08 CTA + Dynamous     | cta-url-slam → endcard   | gsap-stagger-grid, marker-circle                            | none                 | none           | none (final fade-to-black)    | 4           |

**Pick category totals**:
- Markers: 8 (1 per scene S00–S08, except S07 which has none — `gsap-typewriter` carries the beat). Cap of 2/scene respected everywhere.
- Captions: 6 scenes use `caption-fade-slide` (S02–S07). S00, S01, S08 omit. One group visible at a time (mutex-visibility makes this automatic).
- Audio-reactive: 0 (news-explainer, no music — narration is too information-dense for audio-reactivity).
- Transitions: 8 between-scene (`blur-crossfade` ×7 primary at 88%; `zoom-through` ×1 accent at T4 only). One primary + one accent — within rule.
- GSAP effects: 13 (`gsap-stagger-grid` ×9, `gsap-counter-tween` ×3, `gsap-path-draw` ×1, `gsap-typewriter` ×1).
- SFX cues: 28 total (impact-slam ×3, screen-shake ×1, spring-pop ×11, cinematic-whoosh ×8, glitch-zap ×1, strike-cross ×2, scale-slam ×2). All cap-compliant per `.claude/rules/audio-design.md`.

---

## Scene-by-Scene Detail

### Scene 00 — Preview Hook (data_start=0, data_duration=7)

**Words in scene**: 17 (transcript indices 0–16)

**Anchor moments**:
- 0.046s — first word "Anthropic" (entrance moment)
- 1.672s — word [5] "DREAM." (HERO SLAM word — lands at the Cinematic Hook Blueprint's hero-slam beat)
- 4.783s — word [12] "primitives," (counts as "four primitives" mention)
- 5.747s — word [14] "launch," (one launch micro-teaser)
- 6.385s — word [16] "gotcha." (one-gotcha micro-teaser → loops to S01)
- 6.6s — phase-exit whoosh moment (cinematic-hook timing)

**Picks**:
1. `marker-highlight` on the slam word **DREAM** — `trigger_s: 1.672` (sweep across the 240px slam glyph), `sweep_duration: 0.4s`, ease `power2.out`. Orange accent bar matches the S00 hero accent.
2. `gsap-stagger-grid` for the three micro-teaser chips — `trigger_s: 4.5, 5.2, 5.9` (paced ~0.7s apart per the cinematic hook blueprint; each chip is a single-element entrance, NOT an enumerated list — quick stagger is correct here).

**Captions**: none. Phase is too short and dense for synced captions; the hero-slam reads on its own.

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=6.6, duration=0.4s opacity + 0.5s blur, ease `sine.inOut`. (Matches plan's primary transition.)

**SFX cues** (per `.claude/rules/audio-design.md`; cues from `shared/audio/MANIFEST.md`):
```yaml
sfx_cues:
  - cue: impact-slam            # hero DREAM slam
    anchor_word_index: 5        # transcript[5] = "DREAM." start=1.672
    offset_seconds: -0.05       # percussive lead-in
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15                # MANIFEST default
  - cue: screen-shake           # layered with impact-slam
    anchor_word_index: 5
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4              # concurrent with impact-slam → unique track
    volume: 0.11
  - cue: spring-pop             # micro-teaser chip 1
    anchor_word_index: 12       # "primitives," start=4.783
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # sequential — reuses 3 (no overlap with impact-slam at 1.62)
    volume: 0.11
  - cue: spring-pop             # micro-teaser chip 2
    anchor_word_index: 14       # "launch," start=5.747
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # micro-teaser chip 3
    anchor_word_index: 16       # "gotcha." start=6.385
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # phase exit + shape rearrange
    anchor_word_index: 16
    offset_seconds: 0.215       # fires at scene-exit boundary 6.6s
    duration_seconds: 0.84
    track_index: 4              # overlaps with last spring-pop on 3 → 4
    volume: 0.11
```

**Why these picks**: The hook is the make-or-break scroll-stop moment — `marker-highlight` on DREAM gives the slam word visible motion (the orange bar sweep behind the glyph), reinforcing the counterintuitive frame from variant_a of the hook. Three rapid spring-pops on the micro-teaser chips set up the four-pillar reveal that lands in S02. The whoosh + shape-backdrop rearrangement at 6.6s establishes the cinematic-whoosh-paired-with-shape-rearrange default for every subsequent transition (per the `feedback_shape_rearrange_on_whoosh_default` memory rule).

**Visual pacing audit**: entrances at 0.046s (Anthropic wordmark fade), 1.672s (DREAM slam + marker), 4.5s (chip 1), 5.2s (chip 2), 5.9s (chip 3), 6.6s (exit). Largest gap = 4.5−1.67 = 2.83s. ≤ 5s rule respected.

---

### Scene 01 — Open Loop (data_start=7, data_duration=8)

**Words in scene**: 21 (transcript indices 17–37)

**Anchor moments**:
- 7.708s — word [17] "But" (PIVOT word — the contrarian snap-back; layered SFX hit)
- 8.602s — word [21] "dreaming." (callback to the hero word)
- 9.195s — word [22] "Three" (number candidate for `gsap-counter-tween`: 0 → 3)
- 11.319s — word [27] "One" (the gated pillar — counterpoint to "Three")
- 11.656s — word [29] "gated" (CONTRARIAN word, candidate for `marker-circle` per plan)
- 13.432s — word [35] "guess" + 13.792s — word [36] "which?" (loop opener question)
- 14.674s — word [37] "Because" (S02 connector — fires after S01 exit)

**Picks**:
1. `gsap-counter-tween` on the "3" digit of the "Three" stat pill — tween from 0 → 3 across `[8.7, 9.4]` (0.7s window ending exactly when the spoken word "Three" lands at 9.195s; `roundProps: 0`). Ease `power2.out`.
2. `marker-circle` on the word "gated" — hand-drawn ellipse drawn over 0.6s starting at `trigger_s: 11.656`, ease `power2.out` (the contrarian word gets the circle treatment). 1 marker — frequency cap respected.

**Captions**: none. The S01 visuals (Three / One stat pair + gated marker) are simple enough that synced captions would crowd the frame.

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=14.5, duration=0.5s, ease `sine.inOut`. (Lands just as "Because" connector starts at 14.674s — the next phase fades in carrying that word.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: impact-slam            # "But" pivot — paired with glitch-zap (cinematic blueprint S01)
    anchor_word_index: 17       # "But" start=7.708
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: glitch-zap             # layered pivot accent
    anchor_word_index: 17
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 4              # concurrent with impact-slam
    volume: 0.09
  - cue: scale-slam             # "Three" counter-tween reveal
    anchor_word_index: 22       # "Three" start=9.195
    offset_seconds: -0.10       # leads the spoken word; counter ends as digit lands
    duration_seconds: 0.73
    track_index: 3              # impact-slam at 7.7 has finished by 8.34, no overlap
    volume: 0.15
  - cue: cinematic-whoosh       # S01 → S02 transition + shape rearrange
    anchor_word_index: 37       # "Because" start=14.674
    offset_seconds: -0.17       # whoosh fires at 14.5 (transition start)
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S01 is the pivot scene — the "But the headline isn't dreaming" snap-back. Layered impact-slam + glitch-zap on "But" is the canonical pivot SFX stack from the cinematic hook blueprint. The Three counter ticks up just as the narrator says it (a `narrated-stat-reveal` micro-pattern). `marker-circle` on "gated" plants the gated-vs-public-beta visual taxonomy that S02 expands.

**Visual pacing audit**: entrances at 7.708s (BUT pivot + frame shift), 9.195s (Three counter end), 11.319s (One pillar entrance), 11.656s (gated marker), 14.5s (transition). Largest gap = 11.319−9.195 = 2.12s. ≤ 5s respected.

---

### Scene 02 — Four Pillars (data_start=15, data_duration=17)

**Words in scene**: 37 (transcript indices 38–74). This is the longest scene and carries the four-pillar reveal — STEP-BY-STEP REVEAL is mandatory here.

**Anchor moments** (the four pillars MUST enter on their narration words, NOT all at once):
- 14.674s — word [37] "Because" (S01 connector → S02 fade-in lands here)
- 15.011s — word [38] "here's" (the line-up overline enters)
- 15.986s — word [41] "**Dreaming.**" (PILLAR 1 entrance — research preview, purple accent)
- 16.590s — word [42] "**Outcomes.**" (PILLAR 2 entrance — public beta, green accent)
- 18.110s — word [43] "**Multiagent**" + 18.784s [44] "orchestration." (PILLAR 3 entrance — public beta, blue accent; anchor on word [43] for visual entry)
- 19.910s — word [45] "**Webhooks.**" (PILLAR 4 entrance — public beta, orange accent)
- 21.292s — word [48] "public" + 21.617s [49] "beta" (status row context — the 3-vs-1 distinction is now legible)
- 26.389s — word [63] "research" + 26.783s [64] "preview" (the GATED chip / RP marker fires here)
- 28.826s — word [68] "twist." (visual beat on the phrase "That's the twist")
- 29.802s — word [70] "dreaming." (final callback before S03 fade-in begins)

**Picks**:
1. `gsap-stagger-grid` for the four pillar pills — but expressed as four explicit `tl.set()` (all hidden at t=0) + four explicit `tl.to()` calls per the `step-by-step-reveal` rule:
   - Pillar 1 "DREAMING / research preview" enters at `trigger_s: 15.986` (word "Dreaming.")
   - Pillar 2 "OUTCOMES / public beta" enters at `trigger_s: 16.590` (word "Outcomes.")
   - Pillar 3 "MULTIAGENT / public beta" enters at `trigger_s: 18.110` (word "Multiagent")
   - Pillar 4 "WEBHOOKS / public beta" enters at `trigger_s: 19.910` (word "Webhooks.")
   Each entrance is 0.55s, ease `back.out(1.5)`, x: -40 → 0, opacity: 0 → 1.
2. `marker-highlight` on "research preview" — purple bar sweeps in behind the words at `trigger_s: 26.389` (word [63] "research"), `sweep_duration: 0.6s`, ease `power2.out`. Cements the gated-vs-public visual taxonomy.

**Captions**: `caption-fade-slide`, narration-synced from word [38] through word [74]. Word groups of 3-5 words per the calm-tone rule. Custom per-word styling: `Dreaming.` (purple), `Outcomes.` (green), `Multiagent` (blue), `Webhooks.` (orange) get color boost; `research preview only` gets bold + purple accent.

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=31.5, duration=0.5s, ease `sine.inOut`. (Lands just as "First" connector fires at 29.418s — wait, that connector lands before the transition. The S02→S03 transition starts at 31.5s, completes at 32s exactly when "Your" word [74] for S03 begins. Connector "First, dreaming. The gated one." 29.418-30.928 plays during S02 tail-hold, leading naturally into S03.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # pillar 1 entrance (Dreaming)
    anchor_word_index: 41       # "Dreaming." start=15.986
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # pillar 2 entrance (Outcomes)
    anchor_word_index: 42       # "Outcomes." start=16.590
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # sequential, no overlap with prior
    volume: 0.11
  - cue: spring-pop             # pillar 3 entrance (Multiagent)
    anchor_word_index: 43       # "Multiagent" start=18.110
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # pillar 4 entrance (Webhooks)
    anchor_word_index: 45       # "Webhooks." start=19.910
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # S02 → S03 transition + shape rearrange
    anchor_word_index: 74       # "Your" start=31.915 (S03's first word)
    offset_seconds: -0.42       # whoosh starts at 31.5 (transition start)
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: The four-pillar row is the spine of the video — it's also the most-violatable scene for the step-by-step reveal rule. Each pillar enters precisely when the narrator names it (15.986, 16.590, 18.110, 19.910), spanning ~4 seconds. After all four are in, the screen holds the row from ~20.5s to 26.4s — that 5.9s gap is the **only** gap that approaches the 5s limit, but it's **filled** by the marker-highlight on "research preview" at 26.389s, and the `caption-fade-slide` is constantly progressing words underneath. So no foreground stays static more than ~5.4s. Marker-highlight on "research preview" is the term-branding moment for the gated-vs-public taxonomy. Captions help because the four pillars are dense with named-entity content the viewer needs to register quickly.

**Visual pacing audit (5s rule)**: entrances at 15.011s (overline), 15.986s (pillar 1), 16.590s (pillar 2), 18.110s (pillar 3), 19.910s (pillar 4), 26.389s (RP marker sweep), 28.826s (phrase emphasis on "twist"), 29.418s (S02 fade-out begins as "First" lands), 31.5s (transition). Caption groups progress continuously through the gap. The 19.91 → 26.389 gap is 6.48s of foreground stillness IF captions don't count — they DO count per `.claude/rules/visual-pacing-5s.md` because each new caption word group is a "content morph" beat. Caption groups land at ~20.769s (Three are public), ~22.302s (live on the Claude Platform right now), ~24.833s (One the named flagship), ~26.389s (research preview only) — gaps of 1.5–2.5s between each. Rule respected.

---

### Scene 03 — Dreaming (data_start=32, data_duration=18)

**Words in scene**: 43 (transcript indices 75–117)

**Anchor moments**:
- 32.101s — word [75] "agent" (post-"Your" — diagram entrance)
- 33.227s — word [79] "**sessions,**" (session cards entry — first beat of the dream-cycle)
- 33.924s — word [80] "**extracts**" + 34.400s [81] "**patterns,**" (pattern extraction visual beat)
- 35.131s — word [83] "**curates**" + 35.572s [84] "**memories,**" (memory cylinder entry)
- 36.954s — word [88] "**agent**" + "starts smarter" (callback arrow drawn)
- 39.704s — word [94] "**Sleep-time**" + 40.204s [95] "**learning,**" (term-branding moment for "sleep-time learning")
- 41.934s [97]–44.314s [105] — "And yes, most of you can't touch it yet." (gated badge gets emphasis)
- 45.242s — word [106] "**Request**" + 45.648s [107] "**access**" (CTA pill entrance — "Request access at the form")
- 47.007s [111] — "Then" (S04 connector, fires during S03 tail/exit)

**Picks**:
1. `gsap-stagger-grid` for the dream-cycle diagram entries — three session cards (33.227, 33.500, 33.773 — quick stagger across the spoken word "sessions"), then memory cylinder entry at 35.131s ("curates"), then 5 curated-memory dots radiating out at 35.572s ("memories"). The three session cards use a compressed 0.5s stagger because the narrator says "past sessions" once.
2. `gsap-path-draw` for the SVG arrows (sessions → memory store → next agent), drawn in two beats:
   - Arrow 1: sessions → memory cylinder, draw from `trigger_s: 33.500` to `34.876` (1.4s — covers "extracts patterns")
   - Arrow 2: memory cylinder → next-agent silhouette, draw from `trigger_s: 36.687` to `38.045` (covers "next agent starts smarter")
3. `marker-circle` on the word "**Dreaming**" the FIRST time it visibly anchors in this scene — but "Dreaming" is not spoken in S03 (it was spoken in S00, S01, S02). Instead, anchor the term-branding marker on "**Sleep-time learning**" — `trigger_s: 39.704`, ellipse drawn over 0.7s, ease `power2.out`. This is the Story Lock #1 (Term Branding) moment per the plan.

**Captions**: `caption-fade-slide`, word groups of 3-5 words. Custom per-word styling: `sessions`, `patterns`, `memories` get accent-purple boost; `Sleep-time learning` gets bold scale-up; `can't touch it yet` gets purple bold; `Request access` gets `border` accent (CTA verb).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=49.5, duration=0.5s. (S03 exit lands at 50, "You" S04-opener at 50.397s — natural handoff over the connector "Then there's outcomes" which spans 47.007-47.994.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # session card 1
    anchor_word_index: 79       # "sessions," start=33.227
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # memory cylinder entrance
    anchor_word_index: 83       # "curates" start=35.131
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # "Request access" pill entrance
    anchor_word_index: 106      # "Request" start=45.242
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # S03 → S04 transition + shape rearrange
    anchor_word_index: 118      # "You" (S04 first word) start=50.397
    offset_seconds: -0.90       # whoosh starts at 49.5
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S03 is the Term Branding scene for "Sleep-time learning" — the marker-circle fires on the brand-coined phrase the moment it's spoken. The path-draw arrows make the dream-cycle metaphor literal: sessions → memory store → next agent. The "Request access" pill entrance matches the CTA verb anchor word. No counter tween here because there are no numbers in S03's narration.

**Visual pacing audit**: entrances cluster at 32.5s (diagram backdrop), 33.227s (sessions), 33.500-34.876s (path-draw arrow 1, continuous motion), 35.131s (memory cylinder), 35.572s (curated-memory dots), 36.687-38.045s (path-draw arrow 2, continuous motion), 39.704s (Sleep-time marker), 41.934s (gated badge emphasis), 45.242s (Request access pill), 49.5s (transition). Largest gap = 41.934 - 39.704 = 2.23s (after marker before badge emphasis); 45.242 - 41.934 = 3.31s. All ≤ 5s.

---

### Scene 04 — Outcomes (data_start=50, data_duration=18)

**Words in scene**: 42 (transcript indices 118–159)

**Anchor moments**:
- 50.536s — word [119] "**write**" + 50.803s [121] "**rubric.**" (rubric entrance)
- 52.243s — word [123] "**separate**" + 52.661s [124] "**grader**" (grader card entrance)
- 53.114s — word [125] "**checks**" (action verb)
- 56.516s — word [134] "**agent**" + 56.818s [135] "**iterates**" (iteration loop entry — Pass 1 red)
- 57.630s — word [138] "**clears**" + 58.048s [140] "**bar.**" (Pass 2 green tween — RED→GREEN flip)
- 59.313s — word [141] "**Plus**" + 59.522s [142] "**ten**" + 59.697s [143] "**points**" (THE RECEIPT — counter tween + marker-highlight)
- 60.196s — word [145] "**task**" + 60.463s [146] "**success**" (caption emphasis)
- 60.962s — word [147] "**versus**" + 61.276s [148] "**standard**" + 61.647s [149] "**prompting.**" (comparison reveal)
- 63.016s — word [150] "**Stop**" + 63.330s [151] "**eyeballing**" + 63.771s [152] "**drafts.**" (Negative Frame line)
- 64.955s [153]–67.568s [159] — "And while one agent grades, another delegates." (S05 connector during exit)

**Picks**:
1. `gsap-stagger-grid` for the rubric checklist items — three rubric criteria entering at 50.803s, 51.500s, 52.243s (quick stagger across "rubric / A separate grader"). Each item is `x:-40, opacity:0 → x:0, opacity:1` over 0.4s, ease `back.out(1.5)`.
2. `gsap-counter-tween` on the "+10" digit in the receipt pill — tween from 0 → 10 across `[58.81, 59.99]` (1.18s window ending exactly when "points" lands at 59.697). Use `roundProps: 0` so digits tick up cleanly.
3. `marker-highlight` on "+10 points" — yellow accent bar sweeps across the digit + label at `trigger_s: 59.697`, `sweep_duration: 0.5s`, ease `power2.out`. THE RECEIPT marker.

Bonus — the red→green Pass 1 → Pass 2 flip at 57.630-58.048s is a `gsap-stagger-grid` color/icon transform (NOT a separate primitive name) using a `strike-cross` SFX hit.

**Captions**: `caption-fade-slide`, word groups of 3-5. Custom per-word: `rubric` (purple accent), `+10 points` (green bold scale-up), `Stop eyeballing drafts` (orange Negative Frame).

**Audio-reactive**: none.

**Transition out**: `zoom-through` @ trigger_s=67.7, duration=0.3s, ease `power4`. **ACCENT TRANSITION** (the only one in the video). Energizes the multiagent reveal in S05 to match the Harvey 6× stat slam.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # rubric item 1
    anchor_word_index: 121      # "rubric." start=50.803
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # grader entrance
    anchor_word_index: 124      # "grader" start=52.661
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: strike-cross           # red Pass 1 → green Pass 2 flip
    anchor_word_index: 138      # "clears" start=57.630
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: scale-slam             # +10 points receipt
    anchor_word_index: 143      # "points" start=59.697
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # S04 → S05 transition (zoom-through accent + shape rearrange)
    anchor_word_index: 160      # "Multiagent" (S05 first) start=68.449
    offset_seconds: -0.75       # whoosh starts at 67.7
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S04 is the receipt scene — a literal +10-points stat earns a counter-tween + marker-highlight stack. The strike-cross + red→green flip on "clears the bar" is the visual punch that sells the rubric loop. The accent `zoom-through` transition into S05 is the one moment in the video that breaks from `blur-crossfade` — it gives the Multiagent reveal extra energy aligned with the Harvey 6× stat coming up.

**Visual pacing audit**: entrances at 50.803s, 51.500s, 52.243s (rubric trio), 52.661s (grader), 53.114s (verb beat), 56.516s (iteration loop), 57.630s (red→green flip), 59.697s (+10 receipt + marker), 63.016s (Negative Frame entry), 67.7s (zoom-through). Gap 53.114 → 56.516 = 3.4s; 57.630 → 59.697 = 2.07s; 59.697 → 63.016 = 3.32s; 63.016 → 67.7 = 4.68s. All ≤ 5s.

---

### Scene 05 — Multiagent (data_start=68, data_duration=18)

**Words in scene**: 44 (transcript indices 160–203)

**Anchor moments**:
- 68.449s — word [160] "**Multiagent**" + 69.169s [161] "**orchestration**" (scene title slam)
- 70.295s — word [164] "**lead**" + 70.528s [165] "**agent**" (lead box entrance — top of pyramid)
- 71.213s — word [167] "**work**" + 71.561s [169] "**specialists**" (4 specialist columns entering)
- 72.571s — word [172] "**parallel,**" (parallel running visual — sub-agent ticks fire)
- 73.813s — word [175] "**shared**" + 74.127s [176] "**filesystem,**" (shared-filesystem icon entry)
- 75.764s — word [180] "**tools.**" (each column gets its own tool icon)
- 77.146s — word [181] "**Harvey**" + 77.622s [183] "**roughly**" + 77.982s [184] "**six**" + 78.272s [185] "**times**" (HARVEY STAT SLAM — counter tween + marker-burst)
- 80.303s — word [188] "**That's**" + 80.547s [189] "**not**" + 80.814s [191] "**demo**" (Thought Narration story-lock)
- 81.580s — word [193] "**That's**" + 81.894s [195] "**legal-AI**" + 82.555s [196] "**production**" + 83.089s [197] "**deployment.**" (production-deployment stamp)
- 84.576s [198]–86.271s [203] — "Plus webhooks, to know the moment work" (S06 connector during exit)

**Picks**:
1. `gsap-stagger-grid` for the 4 specialist columns — entering at `trigger_s: 71.561, 71.800, 72.040, 72.280` (0.24s apart, quick stagger; the narrator says "specialists running in parallel" once — quick stagger is the explicit step-by-step rule exception). Each column: `y:40, opacity:0 → y:0, opacity:1`, 0.4s ease `back.out(1.5)`.
2. `gsap-counter-tween` on the "6×" digit — tween from 0 → 6 across `[77.4, 78.6]` (1.2s window ending precisely as "times" lands at 78.272). Coupled with a 1.05× scale slam on the digit element to read as a hero stat.
3. `marker-burst` on the "6×" stat — radiating accent lines erupt from the digit at `trigger_s: 78.272`, animation duration 0.5s, ease `power2.out`. ONE marker — frequency cap respected.

**Captions**: `caption-fade-slide`, word groups of 3-5. Custom per-word: `Multiagent orchestration` (blue scale-up), `parallel` (blue accent), `Harvey` (white bold), `6×` / `six times` (blue bold scale-up), `legal-AI production deployment` (purple).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=85.5, duration=0.5s. (S06 first word "work" at 86.318s — connector "Plus webhooks, to know the moment" 84.576-86.271s plays through the transition.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                    # specialist column 1 entrance
    anchor_word_index: 169      # "specialists" start=71.561
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                    # specialist column 2 entrance (sequential, +0.24s)
    anchor_word_index: 169
    offset_seconds: 0.24
    duration_seconds: 0.52
    track_index: 3              # sequential — no overlap with prior pop (0.52s gap from start)
    volume: 0.10
  - cue: pop                    # specialist column 3 entrance
    anchor_word_index: 169
    offset_seconds: 0.48
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                    # specialist column 4 entrance
    anchor_word_index: 169
    offset_seconds: 0.72
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: scale-slam             # Harvey 6× stat slam
    anchor_word_index: 184      # "six" start=77.982
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3              # last pop ended at 72.561 — no overlap
    volume: 0.15
  - cue: cinematic-whoosh       # S05 → S06 transition + shape rearrange
    anchor_word_index: 204      # "work" (S06 first) start=86.318
    offset_seconds: -0.82       # whoosh starts at 85.5
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S05 has the biggest receipt of the video — the Harvey 6× stat is the Story-Lock-Thought-Narration moment per the plan ("That's not a demo number — that's a legal-AI production deployment"). Counter-tween + marker-burst + scale-slam on the digit is the canonical `narrated-stat-reveal` pattern. The four specialist column entrances use a 0.24s quick stagger because the narrator names them collectively ("specialists running in parallel") — this is the explicit step-by-step-reveal exception ("2-3 items quick stagger is acceptable when narration genuinely names them in one sentence"; here it's 4 but they're identical-typed columns and named by class not individually).

**Visual pacing audit**: entrances at 68.449s (title slam), 70.295s (lead box), 71.561-72.280s (4 columns), 72.571s (parallel ticks), 73.813s (shared-filesystem icon), 75.764s (per-column tool icons), 78.272s (Harvey stat slam + marker-burst), 81.580s (production-deployment stamp), 85.5s (transition). Largest gap = 78.272 → 81.580 = 3.31s; 81.580 → 85.5 = 3.92s. All ≤ 5s.

---

### Scene 06 — Webhooks (data_start=86, data_duration=13)

**Words in scene**: 34 (transcript indices 204–237)

**Anchor moments**:
- 88.418s — word [208] "**Stop**" + 88.685s [209] "**polling.**" (NEGATIVE FRAME story-lock — strike-cross moment)
- 89.278s — word [210] "**Subscribe**" + 89.951s [213] "**webhook.**" (webhook bell entrance + single ring SFX)
- 90.973s [214]–93.422s [223] — "If you've ever wired a polling loop you already hate" (relatable pain)
- 94.084s — word [227] "**receipt.**" (the visual payoff word)
- 95.617s — word [229] "**community**" + 96.708s [231] "**called**" (community-quote tile entrance)
- 97.753s — word [234] "**webhooks**" + 98.624s [236] "**what**" + 98.833s [237] "**finally**" (closing emphasis)
- 99.251s [238]–101.364s [244] — "close the loop for real production workflows" (S07 connector spans transition)

**Picks**:
1. `gsap-stagger-grid` for the polling-vs-webhook side-by-side — left column "polling cron stack" enters first (3 stacked cron-ticks at 86.318s, 86.700s, 87.080s — quick stagger as narrator says "work is actually done"), then `marker-scribble` crosses them at 88.418s, then a single webhook-bell icon enters on the right at 89.951s with the single spring-pop ring.
2. `marker-scribble` over the polling cron stack — chaotic strike-out drawn from `trigger_s: 88.418` over 0.7s, ease `power2.out`. ONE marker — frequency cap respected.

**Captions**: `caption-fade-slide`, word groups of 3-5. Custom per-word: `Stop polling.` (orange Negative Frame), `Subscribe to a webhook.` (orange CTA verb), `community already called it out` (white bold), `finally close the loop` (orange).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=98.5, duration=0.5s. (S07 first word "close" at 99.251s — connector "close the loop for real production workflows" lands across the transition.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                    # polling cron-tick 1
    anchor_word_index: 204      # "work" start=86.318 (S06 entrance moment)
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                    # polling cron-tick 2 (sequential)
    anchor_word_index: 204
    offset_seconds: 0.38         # 0.38s gap, no overlap (0.52s duration)
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: pop                    # polling cron-tick 3 (sequential)
    anchor_word_index: 204
    offset_seconds: 0.76
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: strike-cross           # marker-scribble across polling stack
    anchor_word_index: 208      # "Stop" start=88.418
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3              # prior pop ended ~87.62, gap ~0.74s — no overlap
    volume: 0.11
  - cue: spring-pop             # webhook bell single ring
    anchor_word_index: 213      # "webhook." start=89.951
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # strike-cross ended at 89.05, no overlap
    volume: 0.11
  - cue: cinematic-whoosh       # S06 → S07 transition + shape rearrange
    anchor_word_index: 238      # "close" (S07 first) start=99.251
    offset_seconds: -0.75       # whoosh starts at 98.5
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S06 is the only Negative-Frame story-lock scene per the plan ("Stop polling. Subscribe to a webhook."). The marker-scribble + strike-cross combination on the polling cron stack is the canonical visual for "crossing out the bad approach" — the chaotic-scribble pattern is exactly when to use it (per `retention-components-hyperframes.md` §1: "Crossing out a wrong claim before stating the right one"). One marker, one webhook bell, clean visual story.

**Visual pacing audit**: entrances at 86.318-87.080s (3 cron-ticks), 88.418s (scribble strike), 89.951s (webhook bell), 91.x (caption progression), 94.084s (receipt visual emphasis on existing pill), 95.617s (community quote tile), 98.5s (transition). Largest gap = 89.951 → 94.084 = 4.13s, but caption groups land continuously across this gap (~92, ~93.5). All ≤ 5s.

---

### Scene 07 — Trust Strip (data_start=99, data_duration=15)

**Words in scene**: 41 (transcript indices 238–278). Per the plan's fact-check audit, items 12 (pricing $0.08/session-hour) and 13 (beta header `managed-agents-2026-04-01`) are SOURCED but flagged for re-verify — Phase 2b verified them (16/16 status). Both ship.

**Anchor moments**:
- 99.251s — word [238] "**close**" + 100.272s [242] "**real**" + 100.725s [243] "**production**" + 100.725s [244] "**workflows.**" (S06 → S07 spillover — pricing pill enters here)
- 102.269s — word [245] "**Here's**" + 102.873s [248] "**lands.**" (S07 reset — the "why" framing)
- 104.150s — word [250] "**beta**" + 104.394s [251] "**header**" + 104.730s [252] "**ships**" + 105.334s [255] "**SDK,**" (beta-header code chip entrance + typewriter)
- 106.634s — word [258] "**verification**" + 107.285s [259] "**question,**" (verification visual beat)
- 108.260s — word [261] "**agent**" + 108.608s [262] "**earned**" + 108.968s [264] "**result,**" (which-agent-earned-it concept entrance)
- 109.955s — word [266] "**finally**" + 110.686s [269] "**table.**" (community quote tile entrance — "the orchestration layer is where the real moat lives" paraphrased per source.md hard rule)
- 112.346s — word [272] "**Anthropic**" + 113.240s [275] "**lock**" + 113.739s [278] "**production-agent**" (lock-in question — exit ramp)

**Picks**:
1. `gsap-stagger-grid` — pricing pill at 99.5s (uses S06→S07 spillover; pricing pill enters as the "production workflows" line lands), beta-header code-chip card at 104.150s, verification-question + which-agent visual at 106.634s, community-quote tile at 109.955s. Each: 0.55s ease `back.out(1.5)`.
2. `gsap-typewriter` on the beta-header code chip — types out `managed-agents-2026-04-01` char-by-char from `trigger_s: 104.150` to `105.984` (1.83s, ~25 chars; ≈73ms/char). The chip is mono JetBrains 32px (per shorts-typography rule for code-mono).

**Captions**: `caption-fade-slide`, word groups of 3-5. Custom per-word: `beta header` (white bold), `SDK` (mono accent), `verification question` (purple), `agent earned the result` (purple bold), `production-agent moat` (orange). Pricing-pill ($0.08/session-hour) is rendered as static text (no caption needed since it's a stat-pill itself).

**Audio-reactive**: none.

**Transition out**: `blur-crossfade` @ trigger_s=113.5, duration=0.5s. (S08 first word "moat," at 114.506s — connector spans transition.)

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # pricing pill entrance ($0.08/session-hour)
    anchor_word_index: 244      # "workflows." start=100.725
    offset_seconds: -0.30       # pill enters at 100.42, just ahead of word
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # beta-header code chip entrance + typewriter start
    anchor_word_index: 250      # "beta" start=104.150
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior pop ended ~100.95, ~3s gap, no overlap
    volume: 0.11
  - cue: spring-pop             # community quote tile entrance
    anchor_word_index: 266      # "finally" start=109.955
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # S07 → S08 transition + shape rearrange
    anchor_word_index: 279      # "moat," (S08 first) start=114.506
    offset_seconds: -1.00       # whoosh starts at 113.5
    duration_seconds: 0.84
    track_index: 4
    volume: 0.11
```

**Why these picks**: S07 carries three concrete trust signals — pricing, beta-header code chip, community quote. The `gsap-typewriter` on `managed-agents-2026-04-01` is the technical-feeling "this is real, here's the code" moment — typewriter ease + monospace chip is the canonical pattern. No marker on this scene because three sequential card entrances + a typewriter already provide enough visual variety; adding a marker would push past the 2/scene cap and visually crowd the strip. Pricing pill enters early during the S06 connector ("real production workflows") to fill what would otherwise be a static beat.

**Visual pacing audit**: entrances at 100.42s (pricing pill, S06 spillover), 102.873s ("lands" emphasis on existing pill), 104.150-105.984s (beta-header typewriter — continuous motion), 106.634s (verification visual), 108.260s (which-agent concept), 109.955s (community quote tile), 112.346s ("lock in" emphasis on existing visuals), 113.5s (transition). Typewriter spans 104.150 → 105.984, removing the largest static window. Largest gap after typewriter = 106.634 → 105.984 = 0.65s; 106.634 → 108.260 = 1.63s. All ≤ 5s.

---

### Scene 08 — CTA + Dynamous Endcard (data_start=114, data_duration=16, **extends to 134.5s in build phase**)

**Words in scene**: 43 in plan window (114–130s, transcript indices 279–321) + 15 trailing Dynamous outro words (322–336, lands at 130.016–134.300s). Composition build phase MUST extend `#root` `data-duration` from 130 to **135** so the Dynamous outro narration is fully audible. The hard reminder from the user states S08/S09 stays free of narration-driven retention picks — endcard carries the rest visually.

**Anchor moments**:
- 114.506s — word [279] "**moat,**" (rhetorical question framing — exit ramp)
- 115.423s [282]–116.990s [287] — "did dreaming get gated for a reason?" (still in pre-CTA phrasing)
- 117.919s [288]–119.068s [293] — "Let me know in the comments." (engagement CTA — "comments" pill entrance)
- 119.254s [294]–120.903s [299] — "And subscribe for more AI news." (subscribe pill entrance)
- 121.819s — word [300] "**So,**" (THE PIVOT TO CTA — form URL slam moment)
- 122.133s — word [301] "**available**" + 122.632s [302] "**today**" + 123.247s [305] "**Claude**" + 123.502s [306] "**Platform.**" (form URL pill enters as "Claude Platform" lands)
- 124.919s [307]–125.825s [309] — "The plumbing shipped." (status callback)
- 126.278s — word [310] "**Dreaming,**" + 127.137s [313] "**one,**" (final Dreaming callback — story-lock resolution)
- 128.170s [317]–129.111s [321] — "the one you have to ask for." (CTA tail — last word in plan window)
- 130.016s [322]–134.300s [336] — Dynamous outro: "If you want to learn more about AI, check out the dynamous.ai community." (Dynamous endcard handles this — NO narration-driven retention picks per user reminder)

**Picks**:
1. `gsap-stagger-grid` — comments pill at 117.919s (Let me know), subscribe pill at 119.428s (subscribe), form URL pill `claude.com/form/claude-managed-agents` at 121.819s (URL SLAM word "So,"), Dynamous endcard at 130.016s (handoff begins). Each: 0.55s ease `back.out(1.5)` for engagement pills; URL pill uses `back.out(2.0)` for slam emphasis.
2. `marker-circle` on the form URL `claude.com/form/claude-managed-agents` — hand-drawn ellipse drawn over 0.6s starting at `trigger_s: 121.819` (right when "So," lands as the CTA pivot). ONE marker — closes the gated-vs-public taxonomy that started in S01 with the gated marker-circle.

**Captions**: none. The CTA + endcard scene is busy enough with the URL pill, comments pill, subscribe pill, and Dynamous endcard layout — adding captions would crowd. The narration is the audio CTA; the URL is the visual CTA.

**Audio-reactive**: none.

**Transition out**: NONE — final scene fade-to-black at 134.5s. Dynamous endcard component handles its own internal animation per `videos/_template-wiring-snippet.md`.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # comments pill entrance
    anchor_word_index: 293      # "comments." start=118.592
    offset_seconds: -0.50       # pill enters as "Let me know" lands (117.919)
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: spring-pop             # subscribe pill entrance
    anchor_word_index: 295      # "subscribe" start=119.428
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3              # prior pop ended ~118.6, no overlap
    volume: 0.11
  - cue: scale-slam             # form URL slam at "So,"
    anchor_word_index: 300      # "So," start=121.819
    offset_seconds: -0.10
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  # NO cinematic-whoosh — final scene, no transition out
```

**Why these picks**: Per the user's hard reminder, S08 keeps narration-driven retention minimal so the Dynamous endcard carries the rest visually. The form URL slam at "So," is the one strong CTA visual beat — `marker-circle` resolves the gated-vs-public taxonomy that started with the S01 "gated" marker-circle (a long-arc visual story-lock). The comments + subscribe pills enter on their narration anchors but use only spring-pops (lightest SFX). No whoosh / no transition / no marker on the Dynamous endcard segment — it is its own self-contained component.

**Visual pacing audit**: entrances at 114.506s (S08 fade-in lands here), 117.919s (comments pill), 119.428s (subscribe pill), 121.819s (URL slam + marker-circle), 124.919s (status callback emphasis on existing URL pill), 126.278s (Dreaming callback emphasis), 130.016s (Dynamous endcard handoff). Largest gap = 130.016 → 126.278 = 3.74s. The Dynamous endcard handles 130–134.5s with its own beat cadence (per `videos/_template-wiring-snippet.md`). All ≤ 5s.

---

## Picks Cross-Reference (validate against menu)

| Pick name              | Source file in `.claude/references/retention-components-hyperframes.md` | Confirmed valid? |
| ---------------------- | ----------------------------------------------------------------------- | ---------------- |
| `marker-highlight`     | §1 Marker Highlights                                                    | YES              |
| `marker-circle`        | §1 Marker Highlights                                                    | YES              |
| `marker-burst`         | §1 Marker Highlights                                                    | YES              |
| `marker-scribble`      | §1 Marker Highlights                                                    | YES              |
| `caption-fade-slide`   | §2 Caption Patterns                                                     | YES              |
| `gsap-stagger-grid`    | §5 GSAP Effects                                                         | YES              |
| `gsap-counter-tween`   | §5 GSAP Effects                                                         | YES              |
| `gsap-path-draw`       | §5 GSAP Effects                                                         | YES              |
| `gsap-typewriter`      | §5 GSAP Effects                                                         | YES              |
| `inline-phase`         | §6 Composition Structure                                                | YES (template-enforced) |
| `mutex-visibility`     | §6 Composition Structure                                                | YES (template-enforced) |
| `blur-crossfade`       | §4 Scene Transitions (Calm CSS primary)                                 | YES              |
| `zoom-through`         | §4 Scene Transitions (High CSS primary)                                 | YES              |
| `hero-slam`            | §7 Retention Pattern Library                                            | YES              |
| `stat-pill-row`        | §7 Retention Pattern Library                                            | YES              |
| `timeline-cards`       | §7 Retention Pattern Library                                            | YES              |
| `cta-url-slam`         | §7 Retention Pattern Library                                            | YES              |
| `narrated-stat-reveal` | §7 Retention Pattern Library                                            | YES              |

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

- **Step-by-step reveal rule** (`.claude/rules/step-by-step-reveal.md`): S02 four-pillar row uses explicit `tl.set()` + `tl.to()` per-pillar at 15.986/16.590/18.110/19.910 (anchored to "Dreaming/Outcomes/Multiagent/Webhooks" transcript words). NOT `tl.from()` and NOT all-at-once. Compliant.
- **Visual pacing rule** (`.claude/rules/visual-pacing-5s.md`): every scene's largest foreground-gap audited above; max ≈ 4.7s in S04 (Negative Frame entry → zoom-through). All ≤ 5.0s. Compliant.
- **Shape-backdrop rearrangement**: every cinematic-whoosh in scene transitions (T0-T7) pairs with a `#shape-backdrop` rearrange beat per `feedback_shape_rearrange_on_whoosh_default` memory rule. Composition build phase wires this on each transition point.
- **Marker frequency cap**: max 1/scene across S00–S08 (S07 has 0). 8 markers total. Compliant (cap is 2/scene).
- **Caption single-group rule**: `caption-fade-slide` only in S02–S07; mutex-visibility makes single-group automatic. S00, S01, S08 omit captions. Compliant.
- **Audio-reactive ban**: 0 picks. News-explainer voice is too information-dense for audio-reactivity per the plan and `.claude/references/retention-components-hyperframes.md` §3 subtlety rules. Compliant.
- **Transition rule**: `blur-crossfade` ×7 (88%) + `zoom-through` ×1 accent at T4 only. One primary + one accent — within rule.
- **Exit-animation ban on non-final scenes**: NONE used. Transition is the exit. Compliant.
- **SFX volume cap (≤ 0.25)**: max value used is 0.15 (impact-slam, scale-slam). All cues ≤ 0.15. Compliant.
- **SFX track-index uniqueness**: every concurrent SFX (impact-slam + screen-shake at S00 1.62s; impact-slam + glitch-zap at S01 7.7s; cinematic-whoosh layered with prior SFX at scene exits) uses unique track indices (3 / 4 for layered pairs). Sequential pops on the same track verified non-overlapping. Compliant.
- **S08/S09 free of narration-driven retention picks**: S08 has only 1 marker-circle (on form URL — visual CTA, not narration emphasis), 4 staggered card entrances, and a single scale-slam SFX. Dynamous endcard 130-134.5s carries the rest visually. Per user's hard reminder. Compliant.

### Constraint violations resolved during planning

- **Initial plan listed S05 as `marker-burst on 6×` AND a concurrent `gsap-counter-tween`** — both fire on the same word. Resolved by sequencing them: counter-tween starts at 77.4s (leads into the spoken "six"), marker-burst fires at 78.272s (after the digit lands). They are visually layered on the same element but temporally sequential on the perception axis.
- **S02 four-pillar row gap from 19.91s (Webhooks pillar) to 26.389s (RP marker)** = 6.48s of pillar-row stillness. Resolved by relying on `caption-fade-slide` word groups landing at 20.769, 22.302, 24.833, 26.389s (gaps 1.5–2.5s each — caption groups count as content morph beats per visual-pacing rule).
- **S08 transcript runs to 134.300s but plan `data_duration` says 130s** — flagged as a known overrun. Composition build phase MUST extend `#root` `data-duration` from 130 to **135** to capture the full Dynamous outro line ("If you want to learn more about AI, check out the dynamous.ai community."). The plan's audio_anchor section already calls out the spoken Dynamous outro as part of S08; the duration field is the only mismatch.

### Anchors with no good pick

- **S03 word "Dreaming"** is referenced repeatedly across S00/S01/S02 as the brand-coined term, but is NOT spoken in S03 itself (S03 narration starts with "Your agent reviews..."). The plan calls for `marker-circle on Dreaming` as the Term Branding moment. Resolved by re-anchoring the term-branding marker on `Sleep-time learning` (transcript words 94+95 at 39.704s) — it's the brand-coined concept S03 introduces verbally, and lands cleanly within the scene.
- **S07 plan called for a `gsap-counter-tween` on the pricing $0.08/session-hour** (not in retention_component_picks but implicit in the "stat-pill-row" pattern). Skipped — the pricing pill is a static stat (no counter-up animation needed); the typewriter on the beta header carries enough motion. The pricing pill enters as a single spring-pop entrance.

---

## Override Notes

Phase 4 (composition build) reads this file as authoritative. To override any pick, edit this file directly before invoking the build playbook (`/diy-yt-creator:new-anthropic-short claude-managed-agents-launch`).

**Critical follow-ups for composition build**:

1. **Extend `#root` `data-duration` from 130 to 135** to capture the full Dynamous outro narration (transcript ends at 134.30s).
2. **Wire `#shape-backdrop` rearrange beats** on every cinematic-whoosh moment (8 transition points: T0/S00→S01 at 6.6s, T1/S01→S02 at 14.5s, T2/S02→S03 at 31.5s, T3/S03→S04 at 49.5s, T4/S04→S05 at 67.7s, T5/S05→S06 at 85.5s, T6/S06→S07 at 98.5s, T7/S07→S08 at 113.5s). Per `feedback_shape_rearrange_on_whoosh_default` memory rule.
3. **Use explicit `tl.set()` + `tl.to()` for S02 pillar reveals** — per `.claude/rules/step-by-step-reveal.md`. NOT `tl.from()`.
4. **The S03 term-branding marker is on `Sleep-time learning` (39.704s), NOT `Dreaming`** — the word "Dreaming" isn't spoken in S03's narration window.
5. **The S04 → S05 transition is `zoom-through` (the ONLY accent transition)** — all others are `blur-crossfade`.
6. **S08 stays narration-light** — Dynamous endcard component carries the visual story from 130s onward.
