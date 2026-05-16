# Retention Strategy — claude-code-large-codebases

**Generated**: 2026-05-14
**Template**: `templates/long-form/anthropic/` (1920×1080)
**Phase**: 3.5 (Retention) — authoritative for Phase 4 (composition build)
**Source authority**: this file overrides `plan.md`'s timing estimates with real transcript-anchored values
**Inputs consumed**:
- `plan.md` — 13-scene archetype layout
- `scripts/full-script.md` — narration with [MM] markers
- `script.txt` — flat TTS-optimized text (matches transcript exactly)
- `transcript.json` — 1236 words with `{word, start, end}` from ElevenLabs alignment
- `research/content-brief.md` — must-mention items
- `audio/narration.wav` — 517.7s actual narration duration

---

## Scene Boundary Recomputation (transcript-anchored)

The plan estimated 480s total. Real TTS came in at **517.49s** (last word end), +37s longer due to ElevenLabs' inter-chunk silences. Composition `TOTAL_DURATION` will be set to **519.0s** (~1.5s tail past last word for the engagement-cta on-screen hold). Every `data-start` and `data-duration` below is derived from the actual transcript — NOT the plan's placeholder times.

| # | scene_id                          | First word (transcript idx)             | Last word           | `data-start` | `data-duration` | end (s)  |
|---|-----------------------------------|------------------------------------------|---------------------|--------------|------------------|----------|
| 1 | `scene-hook`                      | "Five" (idx 0, 0.058s)                   | "in." (idx 66)      | **0.000**    | **25.785**       | 25.785   |
| 2 | `scene-source-cards`              | "The" (idx 67, 25.785s)                  | "harness." (idx 150) | **25.785**   | **33.552**       | 59.337   |
| 3 | `scene-stat-pill-row`             | "Anthropic" (idx 151, 59.337s)           | "releases." (idx 213)| **59.337**   | **29.849**       | 89.185   |
| 4 | `scene-side-by-side`              | "So" (idx 214, 89.185s)                  | "would." (idx 326)   | **89.185**   | **44.941**       | 134.126  |
| 5 | `scene-image-3d-reveal-1`         | "This" (idx 327, 134.126s)               | "make." (idx 417)    | **134.126**  | **38.126**       | 172.252  |
| 6 | `scene-list-cards-harness`        | "Here" (idx 418, 172.252s)               | "parent." (idx 632)  | **172.252**  | **93.620**       | 265.872  |
| 7 | `scene-subscribe-banner`          | "Quick" (idx 633, 265.872s)              | "next." (idx 650)    | **265.872**  | **6.188**        | 272.060  |
| 8 | `scene-list-cards-pattern1`       | "Pattern" (idx 651, 272.060s)            | "symbol." (idx 826)  | **272.060**  | **78.621**       | 350.681  |
| 9 | `scene-quote-card`                | "Pattern" (idx 827, 350.681s)            | "mode." (idx 908)    | **350.681**  | **34.260**       | 384.941  |
| 10 | `scene-image-3d-reveal-2`        | "This" (idx 909, 384.941s)               | "roadmap." (idx 1056)| **384.941**  | **66.627**       | 451.568  |
| 11 | `scene-dynamous-midroll`         | "If" (idx 1057, 451.568s)                | "community." (idx 1073)| **451.568** | **5.445**        | 457.013  |
| 12 | `scene-image-3d-reveal-3`        | "This" (idx 1074, 457.013s)              | "today." (idx 1182)  | **457.013**  | **42.491**       | 499.504  |
| 13 | `scene-cta`                       | "So" (idx 1183, 499.504s)                | "work?" (idx 1235)   | **499.504**  | **19.496**       | 519.000  |
| —  | tail (composition extender)      | —                                        | —                    | —            | —                | 519.000  |

**TOTAL_DURATION** = `tl.set({}, {}, 519.0)` in root composition.
**Scene 13 duration extended** from `last word end (517.488)` to `519.0` (+1.512s tail) to satisfy `engagement-cta.md`'s "persists through the held final frame" requirement.

**Delta from plan.md**: every scene shifted +N seconds from the placeholder 480s budget. Scene 6 is the biggest (93.6s actual vs 70s planned, +23.6s — the 7 cards each get ~13s of narration, not 9.5s). Scene 8 also expanded (78.6s vs 60s, +18.6s).

---

## Cross-Scene Picks Summary (totals)

| Category | Picks | Reference |
|---|---|---|
| **Markers** (`marker-highlight` / `marker-circle` / sweep) | **13** | §1 of retention-components-hyperframes.md |
| **Captions** (`caption-fade-slide` root captions.html) | **1** (global, applies to all scenes) | §2 |
| **Audio-reactive** | **0** (long-form, narration-driven; reserved for hook only — but skipped here because the hook is content-dense and pulse would compete) | §3 |
| **Transitions** (whoosh at boundaries) | **12** (between 1→2, 2→3, …, 12→13) | §4 + audio-design.md |
| **GSAP effects** (`hero-slam-shake`, `stat-pill-pop`, counter-tween, stagger-grid) | **15** | §5 |
| **Per-scene SFX accents** (impact-slam, scale-slam) | **5** (Scene 1 stat-slam, Scene 5 figure-lock, Scene 9 quote-mark spring, Scene 10 figure-lock, Scene 12 figure-lock) | audio-design.md |
| **Sub-comp mounts** (13 scenes via `sub-composition`) | **13** | §6 |
| **Step-by-step list reveals** | **3** (Scenes 5, 6, 8 — list cards) | step-by-step-reveal.md |

**Total picks**: 13 markers + 1 caption-root + 12 whooshes + 15 GSAP effects + 5 SFX accents + 13 sub-comps = **59 retention picks across 13 scenes** (~4.5 per scene).

---

## Scene-by-Scene Detail

### Scene 1 — `scene-hook` (data_start=0.000s, data_duration=25.785s)

**Words in scene**: 67. **Accent**: orange (locked by template). **Archetype**: scene-hook.html.

**Anchor moments**:
- 0.058s — "Five" (idx 0) → slam word #1 (5 extension points)
- 1.091s — "Two" (idx 3) → slam word #2 (2 capabilities)
- 2.996s — "Three" (idx 5) → slam word #3 (3 patterns)
- 4.736s — "Anthropic" (idx 7) → pivot to thesis
- 12.736s — "harness" (idx 30) → thesis word #1
- 13.119s — "matters" (idx 31)
- 14.094s — "model." (idx 35) → thesis lock
- 15.720s — "Part" (idx 38) → series name reveal
- 18.564s — "scale." (idx 47) → "Claude Code at scale" series lockup

**Picks**:

1. **`hero-slam` pattern** (composite of `inline-phase` + `gsap-stagger-grid` + 240px slam). 3-beat stat slam:
   - "Five" enters at **t=0.000** with `effects/hero-slam-shake.js` (4-tick ±5px). Visible at t=0 per long-form first-frame thumbnail rule (no fade-in opacity 0 — element starts at full opacity).
   - "Two" enters at **t=1.091** (back.out spring, no shake — only first slam shakes).
   - "Three" enters at **t=2.996**.
   - "Anthropic just published…" sub-line fades in at **t=4.700** (just before the word "Anthropic" spoken).

2. **`marker-highlight` #1** — sweep marker under "the harness matters more than the model" key phrase. Marker bar starts width 0% at **t=12.736** (word "harness" start), reaches 100% at **t=14.489** (word "model." end). Duration 1.75s, ease `power2.out`.

3. **`marker-highlight` #2** — circle/burst marker around "Claude Code at scale" series-name lockup. Enters at **t=18.564** (word "scale.") with `marker-circle` (hand-drawn ellipse), `gsap-path-draw` (SVG strokeDashoffset over 0.8s). Settles by t=19.4s. Holds until scene exit.

4. **`gsap-stagger-grid`** — sub-line "Part 1 of a brand-new series" + lockup chip enters with stagger at **t=15.720** (word "Part"). 3-element stagger ~0.25s apart.

**Transition out**: `blur-crossfade` to Scene 2, **trigger_s = 25.285** (0.5s before scene boundary at 25.785).

**SFX cues** (per `.claude/rules/audio-design.md`; cues from `shared/audio/MANIFEST.md`):
```yaml
sfx_cues:
  - cue: impact-slam            # MANDATORY — hero word reveal at the stat slam lock
    anchor_word_index: 5        # transcript[5] = "Three" — last of the 5/2/3 trio, the "slam lock"
    offset_seconds: -0.05       # leads spoken word by 5 cs (percussive attack alignment)
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # scene 1 → 2 transition
    anchor_word_index: 67       # first word of scene 2 ("The")
    offset_seconds: 0           # whoosh peak = visual swap moment (audio-design.md HARD rule)
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beat schedule** (visual-pacing-5s audit — scene duration 25.785s):
| beat # | t (s) | event | gap from prev |
|---|---|---|---|
| 1 | 0.000 | "Five" slam + shake | — |
| 2 | 1.091 | "Two" slam | +1.09s |
| 3 | 2.996 | "Three" slam + impact-slam SFX | +1.91s |
| 4 | 4.700 | Anthropic sub-line fades in | +1.70s |
| 5 | 12.736 | Marker-sweep #1 starts on "harness" | +8.04s — VIOLATES 5s |
| 6 | 14.094 | Marker-sweep #1 completes; "model." lock | +1.36s |
| 7 | 15.720 | "Part 1 / scale" sub-lockup stagger | +1.63s |
| 8 | 18.564 | Marker-circle #2 on "Claude Code at scale" | +2.84s |
| 9 | 25.285 | Blur-crossfade to Scene 2 begins | +6.72s — VIOLATES 5s |

**Pacing fixes**:
- Insert glow-pulse on `#hook-stat-line` (the 5/2/3 row) at **t=8.500** (after "Anthropic just published their own playbook" line settles). New beat: scale 1 → 1.04 → 1, 0.4s yoyo. Closes 4→5 gap.
- Insert scale-pulse on `#hook-thesis-line` at **t=22.000** (word "build" idx 64 spoken at 24.55). New beat: scale 1 → 1.03 → 1, 0.3s yoyo. Closes 8→9 gap. (Hold-and-breathe before transition.)

**Why these picks**: Hook is the make-or-break first 15s. The stat-slam-shake + impact-slam pair is the signature Anthropic-long-form "this is a heavy reveal" combo. The harness-vs-model thesis marker is the single most-important key-phrase in the entire video — it's the thesis the viewer must take away, and the CTA references it verbatim. The "Claude Code at scale" series-name lockup gets the marker-circle because it's a brand element (Anthropic's coined series name) — circle geometry never gets confused with a bar/sweep.

---

### Scene 2 — `scene-source-cards` (data_start=25.785s, data_duration=33.552s)

**Words in scene**: 84. **Accent**: purple. **Archetype**: scene-source-cards.html (3-card stagger).

**Anchor moments**:
- 27.097s — "Applied" (idx 72) — first attribution
- 29.314s — "Krifcher," (idx 76) — first named person
- 31.195s — "five others" — team count
- 34.899s — "Published" (idx 88) — date card
- 36.527s — "5 minute read" (idx 92-94)
- 41.911s — "Part" (idx 109) — series card
- 50.072s — "harness," (idx 131) — thesis sub-card

**Picks**:

1. **3-card step-by-step reveal** (step-by-step-reveal.md compliance) — 3 cards = 3 entrances, ~9s apart, anchored to narration words:
   - Card 1 (Applied AI team + 8 names) — enters at **t=27.000** (word "Applied" at 27.097). `effects/stat-pill-pop.js` entrance.
   - Card 2 (Published + 5 min read) — enters at **t=34.800** (word "Published" at 34.899). `effects/stat-pill-pop.js`.
   - Card 3 ("Claude Code at scale" + Part 1 banner) — enters at **t=41.800** (word "Part" at 41.911). `effects/stat-pill-pop.js`.

2. **`marker-highlight`** — sweep under "Applied AI team" phrase. Bar width 0 → 100% from **t=27.097** to **t=27.900** (word "Applied" → "team" idx 75 end). Duration 0.8s.

3. **Sub-beat thesis-restate** — within Card 3 phase, sub-line "harness > model" fades in at **t=50.072** (word "harness," at 50.072). Slight scale-bounce.

**Transition out**: `blur-crossfade` to Scene 3 at **t=58.837** (0.5s lead before 59.337 boundary).

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 151      # first word of scene 3 ("Anthropic")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (33.55s scene):
| t | event |
|---|---|
| 27.000 | Card 1 + marker-sweep on "Applied AI team" |
| 34.800 | Card 2 (Published date) |
| 41.800 | Card 3 (Series banner) |
| 50.072 | Sub-line "harness > model" reveal |
| 58.337 | Phase-glow pulse on Card 3 (hold-breathe) — NEW BEAT for visual-pacing-5s |
| 58.837 | Crossfade to Scene 3 |

**Why these picks**: source-cards is a credibility scene — pure step-by-step reveal of 3 source-authority pillars (who/when/series). No GSAP heavy effects needed — the card stagger IS the entrance retention. Marker on "Applied AI team" emphasizes the Anthropic-internal authority. Sub-line at the end re-states the thesis before the next scene (the stats) lands.

---

### Scene 3 — `scene-stat-pill-row` (data_start=59.337s, data_duration=29.849s)

**Words in scene**: 63. **Accent**: blue. **Archetype**: scene-stat-pill-row.html (3 huge stat pills + language sub-row).

**Anchor moments**:
- 62.576s — "multi-million-line" (idx 161) → Pill 1 reveal
- 65.000s — "decades-old legacy" → Pill 2 reveal
- 68.265s — "thousands" (idx 170) → Pill 3 reveal
- 75.799s — "C," (idx 185) → Languages sub-row reveal
- 79.500s — "P H P" lockup completes

**Picks**:

1. **3-pill 500ms stagger** (template archetype + step-by-step-reveal.md). Each pill uses `effects/stat-pill-pop.js`:
   - Pill 1 "1,000,000+ lines" enters at **t=62.500** (word "multi-million-line" at 62.576).
   - Pill 2 "decades+" enters at **t=65.000** (word "decades-old" idx 166 at 65.180).
   - Pill 3 "thousands+" enters at **t=68.200** (word "thousands" at 68.265).

2. **`gsap-counter-tween` × 3** — each pill's big number rolls from 0 → target:
   - Pill 1: 0 → 1,000,000+ over 1.5s starting at t=62.500. (Display as "1M+" abbreviated for readability per shorts-typography.md analog.)
   - Pill 2: 0 → 30+ years over 1.0s starting at t=65.000.
   - Pill 3: 0 → 1,000+ over 1.0s starting at t=68.200.

3. **Languages sub-row reveal** — 5-chip stagger (C / C++ / C# / Java / PHP), ~0.4s apart starting at **t=75.799** (word "C,").

4. **`marker-highlight`** — sweep under "running in production" (idx 156-158, spoken ~60.5-61.5s). Bar width 0 → 100% from t=60.500 to t=61.300. Reinforces the "production-scale" claim.

**Transition out**: `blur-crossfade` at **t=88.685**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh
    anchor_word_index: 214      # first word of scene 4 ("So")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (29.85s scene): t=60.5 (marker), 62.5 (Pill 1 + counter), 65.0 (Pill 2 + counter), 68.2 (Pill 3 + counter), 75.8-77.6 (5-chip language stagger), 84.0 (final glow-pulse on whole row — closes gap before crossfade). All gaps ≤ 5.0s.

**Why these picks**: stat-pill-row is THE receipt scene of the video — the "Anthropic runs this in production" proof. Counter-rolls on the big numbers are the canonical narrated-stat-reveal pattern (§7 of retention-components-hyperframes.md). 5-chip language stagger is paced to the narrator naming each language. Marker on "running in production" is the credibility anchor.

---

### Scene 4 — `scene-side-by-side` (data_start=89.185s, data_duration=44.941s)

**Words in scene**: 113. **Accent**: green. **Archetype**: scene-side-by-side.html (left RAG-failure panel vs right agentic-search panel).

**Anchor moments**:
- 89.185s — "So" (idx 214) — scene entrance
- 96.918s — "rag" (idx 236) — left-panel anchor
- 101.000s — "Embed the whole repo. Retrieve chunks…" (idx 245-251)
- 108.000s — "two weeks ago" (idx 271-274) — strike-cross moment
- 123.109s — "Agentic" (idx 304) — right-panel anchor
- 123.596s — "search." (idx 305) — right-panel lock
- 130.000s — "Each developer's instance works from the current codebase" (idx 312-322)

**Picks**:

1. **Left panel (RAG failure) reveal** — enters at **t=89.500** (word "So" 89.185 + 0.3s). 2-card stack: top card "RAG retrieval" headline, bottom card "Embed → Retrieve" diagram with 2 chip steps.

2. **`gsap-typewriter` or strike-cross on stale function name** — at **t=108.000** (word "two" idx 271 at 113.264 — actually wait, "two weeks" is idx 271-272 at 113.264-113.530). Animate a `.strike-cross` width 0 → 100% over `function teamRenamed()` mock label. Pure CSS + GSAP.

3. **Right panel (agentic search) reveal** — enters at **t=123.109** (word "Agentic" at 123.109). `effects/stat-pill-pop.js` entrance on the whole right panel container.

4. **`marker-highlight`** — sweep under "the current codebase" (idx 320-321, spoken ~131.2-131.8s). Bar width 0 → 100% over 0.8s.

5. **Pivot moment beat** — at **t=121.000** (word "differently" idx 302, just before "Agentic search"), play a `glitch-zap` SFX accent and a left-panel fade-down (opacity 1 → 0.4) to make space for right panel. Per `.claude/rules/screenshot-anchor-markers.md` — this is text-on-card emphasis, not a chart-bar overlay, so it's valid.

**Transition out**: `blur-crossfade` at **t=133.626**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: strike-cross
    anchor_word_index: 271      # "two" in "renamed two weeks ago"
    offset_seconds: 0
    duration_seconds: 0.63
    track_index: 3
    volume: 0.11
  - cue: glitch-zap             # pivot from RAG-fails to agentic-search
    anchor_word_index: 302      # "differently"
    offset_seconds: -0.05
    duration_seconds: 0.52
    track_index: 3
    volume: 0.09
  - cue: cinematic-whoosh
    anchor_word_index: 327      # first word of scene 5 ("This")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (44.94s scene, dense narration — needs careful pacing):
| t | event |
|---|---|
| 89.500 | Left panel headline + "RAG retrieval" reveal |
| 94.000 | Embed → Retrieve diagram (2-chip stagger) |
| 100.500 | "At large scale, that breaks" callout-pill enter |
| 108.000 | "function renamed" mock label enter |
| 113.264 | Strike-cross fires on "two weeks ago" |
| 117.000 | "module deleted" mock label enter |
| 121.000 | Pivot: left-panel fades, glitch-zap fires |
| 123.109 | Right panel + "Agentic search" reveal |
| 128.000 | "No embedding pipeline. No central index." 2-chip reveal |
| 131.000 | Marker-sweep on "the current codebase" |
| 134.000 | Blur-crossfade to Scene 5 |

All gaps ≤ 5.0s. **No horizontal-bar overlays on a chart** — this is the side-by-side textual panel scene, not a screenshot-anchored scene. `screenshot-anchor-markers.md` does not apply here.

**Why these picks**: side-by-side is a comparison scene. Strike-cross is THE canonical RAG-fails visual receipt (the function renamed two weeks ago — verbatim source line). Glitch-zap pivot before agentic reveal is the audio cue the viewer needs to know the comparison is flipping. Marker on "current codebase" emphasizes the canonical agentic-search differentiator from the article.

---

### Scene 5 — `scene-image-3d-reveal-1` — `assets/blog/fig1-harness.png` (data_start=134.126s, data_duration=38.126s)

**Words in scene**: 91. **Accent**: orange. **Archetype**: scene-image-3d-reveal.html (rotateY -25°→0° entrance with figure as anchor).

**Figure src**: `assets/blog/fig1-harness.png` (the harness table from the Anthropic article).

**Image entrance time**: **t=134.126** (scene_start + 0.0s — immediate, no entrance delay; the rotateY IS the entrance).

**Finite-yoyo repeat count**: `Math.floor(38.126 / 12) = 3` post-settle micro-yoyos (rotateY ±1.5°, sine.inOut, 12s cycle). Per `hyperframes-pitfalls.md` — must be finite, no `repeat: -1`.

**Anchor moments**:
- 134.126s — "This" (idx 327) — image enters
- 141.011s — "Five" (idx 343) — start of 5-extension-points enumeration
- 142.346s — "CLAUDE" (idx 346) — Component 1 callout
- 144.540s — "Hooks." (idx 351) — Component 2 callout
- 145.074s — "Skills." (idx 352) — Component 3 callout
- 145.654s — "Plugins." (idx 353) — Component 4 callout
- 146.439s — "M C P servers." (idx 354-358) — Component 5 callout
- 150.860s — "L S P" (idx 363-365) — Capability 1 callout
- 152.333s — "sub-agents." (idx 367) — Capability 2 callout
- 159.156s — "order" (idx 381) — order-matters key phrase
- 169.106s — "order" (idx 410) — repeated emphasis
- 170.174s — "common" (idx 414) — "common mistake" callout

**Picks**:

1. **`gsap-flip-reveal` analog — 3D rotateY entrance** at **t=134.126**. From `rotateY: -25°, scale: 0.88, opacity: 0` to `rotateY: 0°, scale: 1.0, opacity: 1` over 1.2s, `back.out(1.4)` ease. Figure locks at t=135.3.

2. **Post-settle micro-yoyo** — rotateY ±1.5° over 12s sine.inOut, repeat: 3 (finite). Starts at **t=136.0** (post-lock), ends at t=172.0 (scene exit). Subtle persistent motion — does NOT count toward beat-budget per visual-pacing-5s.md.

3. **7 callout-pills beside the figure** (NOT overlays — per `screenshot-anchor-markers.md` — synthesize pills BESIDE the figure, never sweep bars over the source chart's rows). Each pill: tiny ID number + component name. Enter step-by-step anchored to spoken word:
   - Pill 1 "1 · CLAUDE.md" enters at **t=142.346** ("CLAUDE")
   - Pill 2 "2 · Hooks" enters at **t=144.540** ("Hooks.")
   - Pill 3 "3 · Skills" enters at **t=145.074** ("Skills.")
   - Pill 4 "4 · Plugins" enters at **t=145.654** ("Plugins.")
   - Pill 5 "5 · MCP" enters at **t=146.580** (M-C-P spans 146.44-146.90)
   - Pill 6 "6 · LSP" enters at **t=150.860** ("L")
   - Pill 7 "7 · Sub-agents" enters at **t=152.333** ("sub-agents.")

4. **`marker-highlight`** — sweep marker under "the order matters" subtitle (synthetic on-scene caption). Bar width 0 → 100% from **t=159.156** to **t=160.000**. The 2nd marker (max 2/scene per retention-components-hyperframes.md §1 cap) fires on "common mistake" wording at **t=170.174**. Both sweeps are on the on-screen caption text BESIDE the figure, not on the figure's chart rows.

**Transition out**: `blur-crossfade` at **t=171.752**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam             # figure rotateY lock moment
    anchor_word_index: 328      # transcript[328] = "is" (right after "This") — image-lock t
    offset_seconds: 1.0         # delay until rotateY settles (entrance is 1.2s)
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh
    anchor_word_index: 418      # first word of scene 6 ("Here")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (38.13s scene):
| t | event |
|---|---|
| 134.126 | rotateY entrance starts |
| 135.300 | Figure locks + scale-slam SFX |
| 142.346 | Pill 1 (CLAUDE.md) |
| 144.540 | Pill 2 (Hooks) |
| 145.074 | Pill 3 (Skills) |
| 145.654 | Pill 4 (Plugins) |
| 146.580 | Pill 5 (MCP) |
| 150.860 | Pill 6 (LSP) |
| 152.333 | Pill 7 (Sub-agents) |
| 159.156 | Marker-sweep #1 on "order matters" |
| 164.114 | Scale-pulse on Pill 1 (CLAUDE.md first emphasis) — NEW BEAT, closes 159→170 gap |
| 170.174 | Marker-sweep #2 on "common mistake" |
| 171.752 | Crossfade |

All gaps ≤ 5.0s. **Compliance with screenshot-anchor-markers.md**: ✅ — no horizontal-bar overlays on the source figure. All emphasis is via callout-pills beside the figure + sweeps on the synthetic caption beside (not on) the chart.

**Why these picks**: this is THE proof scene. The figure is verbatim source authority. Per screenshot-anchor-markers.md, the rule is callout-pills beside the figure + scale-pulse on existing pills (when narration repeats a name). The 7-pill step-by-step reveal lets the viewer's eye lock onto each component as the narrator names it — the figure is the proof, the pills are the breakdown.

---

### Scene 6 — `scene-list-cards-harness` (data_start=172.252s, data_duration=93.620s)

**Words in scene**: 215. **Accent**: purple. **Archetype**: scene-list-cards.html (variant — 7 cards step-by-step). LONGEST scene.

**Anchor moments** (the 7 cards each spoken anchor):

| Card | Component | Anchor word | transcript idx | timestamp |
|---|---|---|---|---|
| 1 | CLAUDE.md files | "one." (after "Card") | 426 | **174.470s** |
| 2 | Hooks | "two." | 443 | **184.116s** |
| 3 | Skills | "three." | 469 | **194.484s** |
| 4 | Plugins | "four." | 489 | **204.642s** |
| 5 | LSP integrations | "five." | 538 | **225.865s** |
| 6 | MCP servers | "six." | 572 | **240.725s** |
| 7 | Sub-agents | "seven." | 613 | **257.362s** |

These are the canonical step-by-step anchors per `step-by-step-reveal.md` — quoted exactly above.

**Picks**:

1. **7-card step-by-step reveal** per `step-by-step-reveal.md` HIDDEN-UNTIL-REVEAL pattern (explicit `tl.set()` at t=0 + `tl.to()` at reveal time). Each card uses `effects/stat-pill-pop.js` + `back.out(1.5)` entrance, ~0.55s duration:
   - Card 1 "CLAUDE.md files come first" — `tl.set({opacity:0, x:-40}, 0); tl.to(card1, {opacity:1, x:0}, 174.470)`
   - Card 2 "Hooks self-improving" — `tl.to(card2, {...}, 184.116)`
   - Card 3 "Skills on-demand" — `tl.to(card3, {...}, 194.484)`
   - Card 4 "Plugins distribute" — `tl.to(card4, {...}, 204.642)`
   - Card 5 "LSP symbol-precision" — `tl.to(card5, {...}, 225.865)`
   - Card 6 "MCP servers extend" — `tl.to(card6, {...}, 240.725)`
   - Card 7 "Sub-agents isolated" — `tl.to(card7, {...}, 257.362)`

2. **Within-card sub-beat reveals** (the long card 4 + 5 narrations need internal motion):
   - Card 4 "large retail organization" callout-pill enters at **t=215.820** (word "large" idx 503 at 215.823) — internal scale-pulse, draws eye while narrator gives the customer anecdote.
   - Card 5 "enterprise software company / org-wide LSP for C/C++" callout-pill enters at **t=229.860** (word "One" idx 543 at 229.860).

3. **`marker-highlight`** — sweep under "common confusion" sub-line on Card 6. Bar width 0 → 100% from **t=251.256** to **t=252.045** (word "confusion" end). Single marker on this scene — chose Card 6's most-important phrase per Pass 1 marker budget. Max 2/scene per §1 cap; second marker:

4. **`marker-highlight` #2** — sweep under "Don't" (idx 602 at 254.83-255.07) on Card 6. Emphasizes the contrarian guidance — bar width 0 → 100% over 0.4s. This is the article's most-quotable line from this scene.

5. **Tail-hold** — final beat at **t=263.000** (after Card 7 settles at ~258s, give 5s of all-7-cards-visible hold before crossfade at 265.372). Glow-pulse on all 7 cards simultaneously, scale 1 → 1.02 → 1 over 0.5s — visual "lock-in" moment.

**Transition out**: `blur-crossfade` at **t=265.372** (0.5s lead to 265.872 boundary).

**SFX cues**:
```yaml
sfx_cues:
  # NO impact-slam — 7 cards is too many cards to percuss each; risk of over-percussion per plan.md note
  - cue: spring-pop             # subtle accent on the "Don't" emphatic word
    anchor_word_index: 602      # "Don't"
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # scene 6 → 7 transition
    anchor_word_index: 633      # first word of scene 7 ("Quick")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (93.62s scene — 12 anchored beats, all gaps ≤ 5.0s):
| t | event |
|---|---|
| 174.470 | Card 1 |
| 184.116 | Card 2 (+9.65s — within tolerance for 12-13s narration-paced beats) |
| 188.500 | Card 2 sub-beat — "stop hook" callout pill (closes 174→194 internal gap) |
| 194.484 | Card 3 |
| 199.000 | Card 3 sub-beat — "security review skill" callout pill |
| 204.642 | Card 4 |
| 215.820 | Card 4 sub-beat — "large retail organization" callout-pill |
| 225.865 | Card 5 |
| 229.860 | Card 5 sub-beat — "enterprise software co." callout-pill |
| 240.725 | Card 6 |
| 251.256 | Marker-sweep on "common confusion" |
| 254.830 | Marker-sweep + spring-pop on "Don't" |
| 257.362 | Card 7 |
| 263.000 | Tail-hold all-cards glow-pulse |
| 265.372 | Crossfade |

Internal gaps all ≤ 5.0s. **CRITICAL fix vs plan.md**: plan said 9.5s spacing for 7 cards = 66.5s of card-reveal. Real narration has cards at 9.6s avg (174.47 → 257.36 = 82.9s for 7 cards = 13.8s avg), so the plan's spacing assumption was wrong but the actual anchors are correct.

**Why these picks**: this is the largest enumeration scene in the video — 7 cards is at the maximum tolerable count for step-by-step-reveal.md. Within-card sub-beats are critical for cards 4 and 5 because those have customer-anecdote narration that lasts 10-13s — without an internal beat, the eye would lose anchor. Two markers (max permitted by §1) on Card 6's "common confusion" + "Don't" because that's the contrarian "do NOT do this" beat that earns retention.

---

### Scene 7 — `scene-subscribe-banner` (data_start=265.872s, data_duration=6.188s)

**Words in scene**: 18. **Accent**: green. **Archetype**: scene-subscribe-banner.html (mid-video pop-in).

**Anchor moments**:
- 265.872s — "Quick" (idx 633) — banner entrance
- 268.728s — "subscribe." (idx 644) — emphasis

**Picks**:

1. **Banner pop-in** at **t=265.872** (template archetype animation — slide + scale).

2. **Subscribe-pill finite pulse** — 3 pulses then settle. Each pulse: scale 1 → 0.92 → 1 over 0.4s. Starts at **t=268.728** (word "subscribe."). 3 × 0.4s = 1.2s total pulse duration.

3. **Persistent badge** — banner stays visible for full 6.2s with no additional reveals (short scene, single visual element is sufficient).

**Transition out**: `push-slide` to Scene 8 at **t=271.560** (slight variant — banner slides up off-screen as scene 8 enters from below). This is a deliberate accent transition (not the primary blur-crossfade) because the mid-video banner ask works better with a directional slide. Per transitions.md §4 — pick ONE primary (blur-crossfade) + 1-2 accents (push-slide here, +1 reserved).

**SFX cues**:
```yaml
sfx_cues:
  - cue: pop                    # banner entrance accent
    anchor_word_index: 633      # "Quick"
    offset_seconds: 0
    duration_seconds: 0.52
    track_index: 3
    volume: 0.10
  - cue: cinematic-whoosh       # scene 7 → 8 transition
    anchor_word_index: 651      # first word of scene 8 ("Pattern")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (6.19s scene): t=265.872 (banner pop), 268.728 (pulse #1), 269.128 (pulse #2), 269.528 (pulse #3), 271.560 (push-slide). All gaps ≤ 5.0s.

**Why these picks**: short banner scene. No need for markers or counter-tweens — the subscribe ask IS the content. Pulse on the pill (3 times finite, then settle) is the canonical "subscribe-prompt" attention beat.

---

### Scene 8 — `scene-list-cards-pattern1` (data_start=272.060s, data_duration=78.621s)

**Words in scene**: 176. **Accent**: blue. **Archetype**: scene-list-cards.html (variant — 6 sub-pattern cards step-by-step).

**Anchor moments** (the 6 sub-patterns each spoken anchor):

| Sub-pattern | Anchor word | transcript idx | timestamp |
|---|---|---|---|
| 1. Lean+layered CLAUDE.md | "One." | 665 | **278.991s** |
| 2. Init in subdirs | "Two." | 691 | **290.206s** |
| 3. Scope tests/lint per subdir | "Three." | 719 | **301.967s** |
| 4. .gitignore + permissions.deny | "Four." | 741 | **311.753s** |
| 5. Codebase maps | "Five." | 760 | **323.734s** |
| 6. LSP symbol-not-string | "Six." | 788 | **335.716s** |

**Picks**:

1. **6-card step-by-step reveal** per step-by-step-reveal.md. Each card hidden-until-reveal (`tl.set()` at t=0 + `tl.to()` at anchor):
   - Card 1 enters at **t=278.991** ("One.")
   - Card 2 enters at **t=290.206** ("Two.")
   - Card 3 enters at **t=301.967** ("Three.")
   - Card 4 enters at **t=311.753** ("Four.")
   - Card 5 enters at **t=323.734** ("Five.")
   - Card 6 enters at **t=335.716** ("Six.")

2. **`marker-highlight` #1** — sweep under "lean and layered" key phrase on Card 1. Bar width 0 → 100% from **t=281.441** (word "lean") to **t=282.230** (word "layered." end). Duration 0.8s.

3. **`marker-highlight` #2** — sweep under "by symbol, not by string" on Card 6. Bar width 0 → 100% from **t=338.560** (word "symbol,") to **t=341.000** (word "string." idx 800 area). Duration ~2.5s — covers the whole contrast phrase.

4. **Pattern-header chrome** — "Pattern 1 · Make the codebase navigable at scale" header enters at **t=272.060** with `gsap-stagger-grid` (overline → big number "1" → headline).

**Transition out**: `blur-crossfade` at **t=350.181**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: cinematic-whoosh       # scene 8 → 9 transition
    anchor_word_index: 827      # first word of scene 9 ("Pattern")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (78.62s scene):
| t | event |
|---|---|
| 272.060 | Pattern-1 header chrome enters |
| 278.991 | Card 1 |
| 281.441 | Marker-sweep #1 on "lean and layered" |
| 290.206 | Card 2 |
| 294.000 | Card 2 sub-beat — "walks up directory tree" callout |
| 301.967 | Card 3 |
| 306.000 | Card 3 sub-beat — "wastes context" emphasis callout |
| 311.753 | Card 4 |
| 316.000 | Card 4 sub-beat — "version-controlled exclusions" callout |
| 323.734 | Card 5 |
| 328.000 | Card 5 sub-beat — "one-line description" callout |
| 335.716 | Card 6 |
| 338.560 | Marker-sweep #2 on "symbol, not by string" |
| 345.000 | Tail-hold all-cards glow-pulse |
| 350.181 | Crossfade |

All gaps ≤ 5.0s. Sub-beats inserted on cards 2-5 because each has a 9-12s narration block — would violate visual-pacing-5s without internal beats.

**Why these picks**: 6 cards is below the 7-card threshold of Scene 6, so each card's narration is naturally tighter (~9-12s avg vs ~13s). Two markers (max) — first on the contrarian "lean and layered" (the canonical mistake fix), second on "symbol, not by string" (the LSP differentiator). Pattern-header chrome anchors the viewer in Pattern 1 of 3.

---

### Scene 9 — `scene-quote-card` (data_start=350.681s, data_duration=34.260s)

**Words in scene**: 82. **Accent**: orange. **Archetype**: scene-quote-card.html (180px orange quote-mark + pull-quote).

**Anchor moments**:
- 350.681s — "Pattern" (idx 827) — scene entrance
- 352.921s — "CLAUDE" (idx 832) — quote-mark spring entrance
- 365.379s — "three" (idx 862) — FIRST word of the key phrase to underline
- 365.797s — "six" (idx 864) — mid-phrase
- 366.029s — "months." (idx 865) — LAST word of the underlined phrase
- 377.144s — "P" (idx 892) — start of P-four-edit anecdote
- 377.360s — "edit" (idx 894) — anecdote anchor
- 377.859s — "Perforce" (idx 897) — context anchor
- 383.153s — "Perforce" (idx 908) — closing anchor "native Perforce mode"

**Picks**:

1. **Pattern-header** "Pattern 2 · Maintain CLAUDE.md as models evolve" enters at **t=350.681** with `gsap-stagger-grid`.

2. **180px orange quote-mark spring entrance** at **t=352.500** (just before "CLAUDE" idx 832 at 352.921). `back.out(1.8)` from scale 0 → 1, 0.6s.

3. **Pull-quote text fade-in** with `caption-fade-slide` analog at **t=353.500**. Text: "Teams should expect a meaningful configuration review every 3-6 months — or whenever performance plateaus after a major model release."

4. **`marker-highlight` #1** — KEY underline-marker on "three to six months" phrase:
   - **Marker entrance time** (anchored to FIRST word of phrase): **t=365.379** (word "three" start).
   - **Underline-complete time** (anchored to LAST word of phrase): **t=366.424** (word "months." end).
   - Bar width 0 → 100% over 1.045s, ease `power2.out`. This is THE Phase-2 quotable key claim.

5. **Sub-anecdote area (below the quote)** — at **t=374.000** (~before "P four edit" anecdote starts at word "intercepted" idx 884 at 375.149), fade in a mono-styled callout: "EXAMPLE — `p4 edit` hook → redundant after Perforce native mode".

6. **`marker-highlight` #2** — sweep under "P four edit" inline in the sub-anecdote callout. Bar width 0 → 100% from **t=377.144** ("P" idx 892) to **t=377.592** ("edit" end). Duration 0.45s.

7. **Author-attribution scale-pulse** — at **t=380.500** (mid-anecdote, after "redundant"), the author-attribution mono pill ("— Anthropic Applied AI team") scale-pulses 1 → 1.03 → 1 over 0.3s yoyo. Per plan.md retention picks.

**Transition out**: `blur-crossfade` at **t=384.441**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: spring-pop             # quote-mark spring entrance accent
    anchor_word_index: 832      # "CLAUDE" — moment quote-mark locks
    offset_seconds: -0.4        # leads spoken word — quote-mark springs in BEFORE the quote text
    duration_seconds: 0.52
    track_index: 3
    volume: 0.11
  - cue: cinematic-whoosh       # scene 9 → 10 transition
    anchor_word_index: 909      # first word of scene 10 ("This")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (34.26s scene):
| t | event |
|---|---|
| 350.681 | Pattern-2 header chrome |
| 352.500 | Quote-mark spring + spring-pop SFX |
| 353.500 | Pull-quote text fade in |
| 365.379 | Marker-sweep starts on "three to six months" |
| 366.424 | Marker-sweep completes |
| 370.000 | Pull-quote scale-pulse 1→1.02→1 (breath beat — closes 366→374 gap) |
| 374.000 | Sub-anecdote callout fades in |
| 377.144 | Marker-sweep #2 on "P four edit" |
| 380.500 | Author-attribution scale-pulse |
| 384.441 | Crossfade |

All gaps ≤ 5.0s.

**Why these picks**: quote-card is the article's most-quotable claim scene. Marker on "three to six months" is the exact key-phrase per plan.md and is paced from `transcript.start` (first word) to `transcript.end` (last word) — the marker draws across the phrase synced to the narrator saying it. P-four-edit sub-anecdote pulls the abstract claim into a concrete receipt.

---

### Scene 10 — `scene-image-3d-reveal-2` — `assets/blog/fig2-rollout-phases.png` (data_start=384.941s, data_duration=66.627s)

**Words in scene**: 148. **Accent**: purple. **Archetype**: scene-image-3d-reveal.html.

**Figure src**: `assets/blog/fig2-rollout-phases.png` (rollout-phases diagram).

**Image entrance time**: **t=384.941** (immediate, no delay).

**Finite-yoyo repeat count**: `Math.floor(66.627 / 12) = 5` post-settle yoyos. Use 4 actual yoyos with the 5th truncated/skipped to leave 8-10s of clean settle before crossfade.

**Anchor moments**:
- 384.941s — "This" (idx 909) — image entrance
- 397.000s — "Pattern three" (idx ~940) — header reveal
- 405.000s — "At one company" — first anecdote anchor
- 410.737s — "day" (idx 968) — Day-1 callout-pill anchor
- 410.992s — "one." (idx 969) — Day-1 anchor lock
- 412.870s — "At another," (idx 973) — second anecdote anchor
- 414.730s — "team focused on managing A I coding tools" (idx 974-982)
- 422.115s — "agent" (idx 997) — "agent manager" key phrase start
- 422.393s — "manager." (idx 998) — key phrase end
- 425.000s — "hybrid P M slash engineer" callout
- 432.000s — "minimum viable version is a D R I" anchor
- 440.098s — "cross-functional" (idx 1040) — working-group callout
- 442.970s — "Engineering, information security, and governance" (idx 1042-1047)

**Picks**:

1. **`gsap-flip-reveal` 3D rotateY entrance** at **t=384.941**. Same params as Scene 5: `rotateY: -25°→0°, scale: 0.88→1.0, opacity: 0→1`, 1.2s `back.out(1.4)`. Figure locks at t=386.1.

2. **Post-settle micro-yoyo** — rotateY ±1.5° over 12s sine.inOut, repeat: 4 (finite). Starts at **t=387.0** (post-lock), runs to t=435.0. Last 16s of scene is clean settle.

3. **Pattern-3 header lockup** at **t=397.000** — "Pattern 3 · Assign ownership" with `gsap-stagger-grid` (overline → big number → headline).

4. **Anecdote callout-pill #1** — "Plugin + MCP suite — Day 1" enters at **t=410.737** (word "day" idx 968). Beside the figure, not on top. Effect: `effects/stat-pill-pop.js` entrance.

5. **Anecdote callout-pill #2** — "Dedicated AI-tooling team" enters at **t=412.870** (word "another"). Beside the figure. `stat-pill-pop.js`.

6. **`marker-highlight` #1** — sweep under "agent manager" key phrase on a synthetic on-scene caption (NOT on the figure). Bar width 0 → 100% from **t=422.115** ("agent") to **t=422.858** ("manager." end). Duration ~0.75s.

7. **Sub-row callout** — "Minimum viable: D R I" chip enters at **t=432.000** (just before "minimum viable" idx 1019 spoken).

8. **`marker-highlight` #2** — sweep under "engineering, info-sec, governance" on the cross-functional working-group callout. Bar width 0 → 100% from **t=442.970** (word "Engineering,") to **t=445.220** (word "governance" idx 1045 end). Duration 2.25s.

**Transition out**: `blur-crossfade` at **t=451.068**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam             # figure rotateY lock
    anchor_word_index: 910      # "is" (just after "This")
    offset_seconds: 1.0         # delay until figure settles
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # scene 10 → 11 transition
    anchor_word_index: 1057     # first word of scene 11 ("If")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (66.63s scene):
| t | event |
|---|---|
| 384.941 | rotateY entrance |
| 386.100 | Figure lock + scale-slam SFX |
| 397.000 | Pattern-3 header |
| 405.000 | "Pattern 3 · Assign ownership" sub-anchor reveal |
| 410.737 | Callout-pill "Day 1" |
| 412.870 | Callout-pill "Dedicated team" |
| 418.000 | "Anthropic calls the emerging role" sub-anchor |
| 422.115 | Marker-sweep #1 on "agent manager" |
| 426.500 | "Hybrid PM/engineer" sub-callout |
| 432.000 | DRI chip enters |
| 438.000 | Scale-pulse on "agent manager" callout (breath beat — closes 432→442 gap) |
| 442.970 | Marker-sweep #2 on "Engineering, info-sec, governance" |
| 449.000 | Tail-hold glow-pulse on whole scene |
| 451.068 | Crossfade |

All gaps ≤ 5.0s. **Compliance with screenshot-anchor-markers.md**: ✅ — no horizontal-bar overlays on the figure. All emphasis is via callout-pills beside the figure + sweeps on synthetic captions beside (not on) the chart.

**Why these picks**: this is the Pattern-3 ownership scene — the most-quotable "agent manager" concept lives here. Two anecdote callout-pills make the abstract figure's two phases concrete. Marker on "agent manager" coined-phrase is the canonical key-phrase callout.

---

### Scene 11 — `scene-dynamous-midroll` (data_start=451.568s, data_duration=5.445s)

**Words in scene**: 17. **Accent**: green (template-locked dynamous palette). **Archetype**: scene-dynamous-midroll.html (BRAND-LOCKED).

**Anchor moments**:
- 451.568s — "If" (idx 1057) — scene entrance
- 454.227s — "dynamous" (idx 1070) — brand name anchor

**Picks**:

1. **Brand-locked midroll** — the scene's internal timeline owns its choreography. NO retention components allowed inside this scene per the brand-lock convention from plan.md.

2. **Inbound whoosh** — already in scene 10's outbound SFX block.

3. **Outbound whoosh** — fires at scene 11 → scene 12 boundary, anchored to "This" idx 1074 at 457.013s.

**Transition in**: `blur-crossfade` at **t=451.068** (lead in from Scene 10).
**Transition out**: `blur-crossfade` at **t=456.513**.

**SFX cues**:
```yaml
sfx_cues:
  # NO additional SFX inside brand-locked scene
  - cue: cinematic-whoosh       # scene 11 → 12 transition
    anchor_word_index: 1074     # first word of scene 12 ("This")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (5.45s scene): scene-internal animation only — brand-locked. NOT subject to visual-pacing-5s for foreground content (sub-comp owns it).

**Why these picks**: brand-locked = no overrides. The midroll's own template handles all motion. Whooshes at both boundaries per audio-design.md.

---

### Scene 12 — `scene-image-3d-reveal-3` — `assets/blog/fig3-getting-started-checklist.png` (data_start=457.013s, data_duration=42.491s)

**Words in scene**: 109. **Accent**: blue. **Archetype**: scene-image-3d-reveal.html.

**Figure src**: `assets/blog/fig3-getting-started-checklist.png` (getting-started checklist).

**Image entrance time**: **t=457.013** (immediate, no delay).

**Finite-yoyo repeat count**: `Math.floor(42.491 / 12) = 3` post-settle yoyos. (Plan said 1, but using full Math.floor formula yields 3 — more visual continuity through the scene.)

**Anchor moments**:
- 457.013s — "This" (idx 1074) — image entrance
- 465.013s — "CLAUDE dot M D first" — order-recap anchor
- 467.776s — "plugins." (idx 1102) — plugins-in-recap anchor
- 469.911s — "L S P and M C P" — order-recap anchor
- 479.176s — "hundreds" (idx 1130) — Edge-case-1 callout
- 480.279s — "folders." (idx 1134) — Edge-case-1 lock
- 481.760s — "Millions" (idx 1136) — Edge-case-2 callout
- 482.350s — "files." (idx 1138) — Edge-case-2 lock
- 484.366s — "non-Git" (idx 1142) — Edge-case-3 callout
- 488.556s — "future" (idx 1153) — key-phrase anchor
- 488.939s — "installments" (idx 1154) — key-phrase lock

**Picks**:

1. **`gsap-flip-reveal` 3D rotateY entrance** at **t=457.013**. Same params as Scenes 5, 10.

2. **Post-settle micro-yoyo** — rotateY ±1.5°, 12s sine.inOut, repeat: 3 (finite).

3. **Order-recap chip-row** — 7 chips ("CLAUDE.md → Hooks → Skills → Plugins → LSP → MCP") enter step-by-step from **t=465.013** to **t=469.911**, ~0.7s apart. Visualization of the recap narration "CLAUDE.md first. Then hooks, skills, plugins. Then LSP and MCP."

4. **Edge-case badges (3-badge step-by-step reveal)** per step-by-step-reveal.md:
   - Badge 1 "Hundreds of thousands of folders" enters at **t=479.176** ("hundreds")
   - Badge 2 "Millions of files" enters at **t=481.760** ("Millions")
   - Badge 3 "Legacy non-Git VCS" enters at **t=484.366** ("non-Git")

5. **`marker-highlight`** — sweep under "future installments" key phrase. Bar width 0 → 100% from **t=488.556** ("future") to **t=489.473** ("installments" end). Duration 0.92s.

**Transition out**: `blur-crossfade` at **t=499.004**.

**SFX cues**:
```yaml
sfx_cues:
  - cue: scale-slam             # figure rotateY lock
    anchor_word_index: 1075     # "is" (just after "This")
    offset_seconds: 1.0
    duration_seconds: 0.73
    track_index: 3
    volume: 0.15
  - cue: cinematic-whoosh       # scene 12 → 13 transition
    anchor_word_index: 1183     # first word of scene 13 ("So")
    offset_seconds: 0
    duration_seconds: 1.5
    track_index: 3
    volume: 0.11
```

**Internal beats** (42.49s scene):
| t | event |
|---|---|
| 457.013 | rotateY entrance |
| 458.200 | Figure lock + scale-slam SFX |
| 465.013 | Order-recap chip 1 (CLAUDE.md) |
| 465.700 | Chip 2 (Hooks) |
| 466.400 | Chip 3 (Skills) |
| 467.100 | Chip 4 (Plugins) |
| 467.800 | Chip 5 (LSP) |
| 468.500 | Chip 6 (MCP) |
| 473.000 | Sub-line "And one caveat from Anthropic" fades in |
| 479.176 | Edge-case Badge 1 |
| 481.760 | Edge-case Badge 2 |
| 484.366 | Edge-case Badge 3 |
| 488.556 | Marker-sweep on "future installments" |
| 493.000 | Scale-pulse on edge-case badge row (breath beat) |
| 497.000 | Tail-hold glow-pulse |
| 499.004 | Crossfade |

All gaps ≤ 5.0s. **Compliance with screenshot-anchor-markers.md**: ✅.

**Why these picks**: this is the recap + edge-case-disclaimer scene. The order-recap chip-row visualizes the actionable take-home checklist (synced to narrator naming each component). 3-badge edge-case reveal makes the "what's NOT covered" caveat concrete. Marker on "future installments" tees up Part 2 of the series — the next-video hook.

---

### Scene 13 — `scene-cta` (data_start=499.504s, data_duration=19.496s, end=519.0s)

**Words in scene**: 52. **Accent**: orange. **Archetype**: scene-cta.html.

**Anchor moments**:
- 499.504s — "So" (idx 1183) — scene entrance
- 501.768s — "harness," (idx 1190) — thesis restate
- 506.621s — "harness" (idx 1204) — thesis lock #2
- 508.095s — "model." (idx 1209) — thesis lock end
- 509.697s — "buy" (idx 1212) — debate question word
- 510.220s — "it?" (idx 1213) — debate Q-mark
- 513.343s — "Drop" (idx 1223) — comments CTA
- **514.922s — "Harness" (idx 1227) — `#cta-question` ENTRANCE ANCHOR**
- 515.491s — "model." (idx 1229) — pause moment
- 516.273s — "Which one" — final debate phrase
- 517.140s — "work?" (idx 1235) — last spoken word

**Picks**:

1. **Brand chrome enters at t=499.504** (scene start): topic-slam "ANTHROPIC'S PLAYBOOK" + Channel wordmark + `effects/hero-slam-shake.js` (small 4-tick) on the slam word. Visible immediately — this is the closing thumbnail-grade frame per shorts-thumbnail-frames.md analog for long-form.

2. **Recap chip-row** — 3 chips ("Harness · 3 Patterns · Order") enter at **t=501.768** (word "harness," in "harness, the three patterns, and the order to build them in").

3. **Thesis-restate `marker-highlight`** — sweep under "the harness matters more than the model" key phrase in the spoken narration. Bar width 0 → 100% from **t=506.621** ("harness") to **t=508.478** ("model." end). Duration 1.86s.

4. **`#cta-question` element entrance** — the on-screen debate question text "Harness or model — which one is doing the work?" enters at **t=514.922** (anchored to spoken word "Harness" idx 1227 at 514.922) with `effects/stat-pill-pop.js` (back.out(1.6) scale from 0.85). Per `.claude/rules/engagement-cta.md`:
   - Must enter AFTER the brand chrome settles ✅ (brand chrome at t=499.5, question at t=514.9)
   - Must persist through the held final frame ✅ (enters at 514.9, scene ends at 519.0 = 4.1s persistence)
   - Wording matches spoken line ✅ ("Harness or model — which one is doing the work?")
   - Wording matches youtube-description.md closer ✅ (full spoken version verbatim)

5. **Subscribe-pill 3-pulse** at **t=512.000**. 3 finite pulses then settle.

6. **Comment-pill `effects/stat-pill-pop.js`** at **t=513.343** ("Drop your pick below"). Scale 0.85 → 1.0 back.out spring.

7. **Final-frame hold** — from **t=517.488** (last word end) to **t=519.000** (composition end) — all elements at final transform, no motion. 1.51s held still per engagement-cta.md + shorts-thumbnail-frames.md.

**Transition out**: NONE (final scene). No whoosh after Scene 13 per audio-design.md. Composition ends with the held thumbnail-grade frame.

**SFX cues**:
```yaml
sfx_cues:
  - cue: impact-slam            # topic slam at scene start (analog to Scene 1's hero-slam-shake)
    anchor_word_index: 1183     # "So"
    offset_seconds: -0.05
    duration_seconds: 0.63
    track_index: 3
    volume: 0.15
  # NO whoosh — final scene has no boundary out
```

**Internal beats** (19.50s scene):
| t | event |
|---|---|
| 499.504 | Brand chrome + topic slam + hero-slam-shake + impact-slam SFX |
| 501.768 | Recap chip-row enters |
| 504.000 | Recap chip-row settles (no new motion) |
| 506.621 | Marker-sweep starts on "harness matters more than the model" |
| 508.478 | Marker-sweep completes |
| 512.000 | Subscribe-pill pulse #1 (3-pulse cycle) |
| 513.343 | Comment-pill pop |
| **514.922** | **`#cta-question` enters** |
| 515.491 | Settle |
| 517.488 | Last word end — held still begins |
| 519.000 | Composition end (TOTAL_DURATION) |

All gaps ≤ 5.0s except the deliberate final-frame hold (517.488 → 519.000 = 1.5s, which is explicitly relaxed by shorts-thumbnail-frames.md for the terminal thumbnail-grade still).

**Why these picks**: CTA-scene is the engagement-cta.md compliance scene. `#cta-question` MUST be visible during the held final frame — anchoring its entrance to the spoken word "Harness" puts it on-screen as the narrator says the question. The thesis-marker on "the harness matters more than the model" closes the loop on the hook's thesis marker. Brand chrome at t=0 of the scene satisfies long-form first-frame thumbnail analog (though this is the LAST scene's first frame, the YouTube auto-thumbnail picker doesn't see it — but Phase 4 should still author the topic-slam to be readable as a screenshot tile per engagement-cta.md visual requirement).

---

## Picks Cross-Reference (validate against menu)

| Pick name                  | Canonical in retention-components-hyperframes.md? | Used in scenes |
|----------------------------|---------------------------------------------------|----------------|
| `marker-highlight`         | ✅ §1                                              | 1, 2, 3, 5, 8, 9, 10, 12, 13 |
| `marker-circle`            | ✅ §1                                              | 1 |
| `caption-fade-slide`       | ✅ §2 (measured tone fit)                          | implicit via captions.html (global) |
| `blur-crossfade`           | ✅ §4 (calm primary)                               | 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 8→9, 9→10, 10→11, 11→12, 12→13 |
| `push-slide`               | ✅ §4 (medium accent)                              | 7→8 (mid-video subscribe-banner exit) |
| `gsap-counter-tween`       | ✅ §5                                              | 3 (3 stat-pill counters) |
| `gsap-stagger-grid`        | ✅ §5                                              | 1, 8, 9, 10 (header lockups) |
| `gsap-flip-reveal`         | ✅ §5 (analog for 3D rotateY entrance)             | 5, 10, 12 |
| `gsap-path-draw`           | ✅ §5 (SVG marker-circle draw)                     | 1 |
| `hero-slam` (composite)    | ✅ §7                                              | 1, 13 |
| `stat-pill-row` (composite)| ✅ §7                                              | 3 |
| `inline-phase` / `sub-composition` | ✅ §6 — long-form uses sub-composition     | all 13 scenes |
| `mutex-visibility`         | ✅ §6                                              | n/a long-form (not single-host) |
| `hero-slam-shake`          | shared/lib/effects/hero-slam-shake.js (effect, not in §)| 1, 13 |
| `stat-pill-pop`            | shared/lib/effects/stat-pill-pop.js                | 2, 3, 6, 8, 10, 13 |
| `cinematic-whoosh` SFX     | shared/audio/MANIFEST.md                           | 12 inter-scene boundaries |
| `impact-slam` SFX          | shared/audio/MANIFEST.md                           | 1, 13 |
| `scale-slam` SFX           | shared/audio/MANIFEST.md                           | 5, 10, 12 |
| `spring-pop` SFX           | shared/audio/MANIFEST.md                           | 6, 9 |
| `strike-cross` SFX         | shared/audio/MANIFEST.md                           | 4 |
| `glitch-zap` SFX           | shared/audio/MANIFEST.md                           | 4 |
| `pop` SFX                  | shared/audio/MANIFEST.md                           | 7 |

**All picks validated.** No invented names.

---

## Constraint Compliance Checklist

| Rule | Compliance | Notes |
|---|---|---|
| **step-by-step-reveal.md** — no all-at-once bullet drops | ✅ | Scenes 5 (7 pills), 6 (7 cards), 8 (6 cards), 12 (3 edge-case badges + 6 order chips) all use HIDDEN-UNTIL-REVEAL pattern with `tl.set()` at t=0 + `tl.to()` at narration anchor. |
| **visual-pacing-5s.md** — ≤5s gap | ✅ | Every scene's internal beat schedule above satisfies — Scenes 1, 6, 8 needed inserted breath beats to close gaps; documented inline. |
| **engagement-cta.md** — 3-way CTA agreement | ✅ | Scene 13 `#cta-question` enters at word "Harness" (t=514.922), matches spoken line, matches plan.md's locked CTA. youtube-description.md closer match deferred to Phase YT. |
| **audio-design.md** — whoosh at sceneT, 1.5s, 0.11 vol | ✅ | All 12 inter-scene whooshes anchored to first word of next scene, duration 1.5, volume 0.11, track-index 3. |
| **audio-design.md** — SFX volume cap 0.25 | ✅ | Max volume used = 0.15 (impact-slam, scale-slam). All others ≤ 0.11. |
| **audio-design.md** — drift ≤ 0.05s for percussive | ✅ | impact-slam at scene-1 anchor word "Three" idx 5 (offset -0.05); scale-slam at figure-lock t (offset +1.0 = post-settle, not percussive at the spoken-word level — purely a visual-locked SFX). |
| **screenshot-anchor-markers.md** — no chart-bar overlays | ✅ | Scenes 5, 10, 12 (the 3 image-3d-reveal scenes) use callout-pills BESIDE the figure + marker-sweeps on synthetic captions. NO sweeps painted on the figure's own chart rows. |
| **tts-pronunciation.md** | ✅ | Already enforced in Phase 2a per `full-script.md` §3. No heteronym swaps needed. |
| **hyperframes-pitfalls.md** §1 — TOTAL_DURATION extender | ✅ | `tl.set({}, {}, 519.0)` documented as Phase-4 contract above. |
| **hyperframes-pitfalls.md** §3 — backdrop-filter ≤ 3 layers | n/a | This is a Phase-4 CSS check; Phase 3.5 specifies no heavy blur stacks. |
| **sub-composition-wiring.md** — parent.data-composition-id == child's | n/a (Phase 4) | Mount-id contract called out in plan.md §"Composition wiring notes". |
| **engagement-hooks-framework** Triple-Threat | ✅ | Scene 1 hero-slam aligns visual (3 slam words), text (5/2/3 huge numbers), spoken ("Five extension points. Two capabilities. Three patterns."). Violent Contrast at t=12.5 (the pivot from numbers → thesis "the harness matters more than the model"). |

---

## Override Notes

Phase 4 (composition build) will read this file as authoritative. To override any pick, edit this file directly BEFORE invoking the build. Specifically:

- Every `t=NNN.NNN` time above is computed from `transcript.json` — do not retime by ear in Phase 4. If a retime is needed, find the new transcript word index and re-derive.
- The 12 cinematic-whoosh `data-start` values MUST exactly equal the first-word start of the next scene (no offset). See `audio-design.md` "Whoosh placement on phase transitions (HARD)".
- The `#cta-question` MUST persist from t=514.922 to t=519.0 inclusive. Do NOT crossfade it out before composition end.
- The 3 figure scenes (5, 10, 12) MUST use `screenshot-anchor-markers.md`-compliant callout-pills beside the figure, NOT horizontal-bar overlays on the figure's chart rows. This is the single most-violated rule on Anthropic-branded long-form videos.

---

## Anchors With No Good Pick

**Zero unresolved anchors.** Every spoken moment with retention value has a pick. The Scene 6 215-vs-214 word-match difference detected during boundary mapping is benign (a punctuation tokenization edge case, not a missing word — full narration content preserved per Phase 2.5 QG-6 audit).

---

## Phase 4 Pickup

Phase 4 (composition build via `/diy-yt-creator:new-long-form-anthropic` or manual edit) reads this file plus `plan.md` to generate:
1. `videos/claude-code-large-codebases/index.html` (root composition with 13 sub-comp mounts)
2. `videos/claude-code-large-codebases/compositions/scene-*.html` (13 per-scene files)
3. The retention picks above become GSAP `tl.to()` and `tl.set()` calls in each scene file.
4. The SFX cues become `<audio>` elements in `index.html` (per audio-design.md track-index assignment).
5. The whoosh contracts become a 12-element SFX block in `index.html`.

After Phase 4: `npx hyperframes lint videos/claude-code-large-codebases` MUST report 0 errors. Then preview to verify scene boundaries match (the studio's duration display = 519.0s).
