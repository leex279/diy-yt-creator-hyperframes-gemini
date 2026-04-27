# Retention Components — HyperFrames Vocabulary

**Purpose**: Authoritative list of HyperFrames-native retention components for Phase 1 (composition planning) and Phase 3.5 (per-scene retention strategy). When a phase prescribes a "retention component" it MUST come from this document — the HyperFrames framework only recognizes the patterns enumerated here.

**Why this doc exists**: HyperFrames retention is built from HTML + GSAP + `data-*` attributes + sub-compositions. This file enumerates every pattern the framework recognizes by name, so phases that prescribe "use a marker on this word" or "audio-reactive glow on the number" are using vocabulary the composition build phase can actually implement.

**How to cite a pick**: Use the canonical name in `monospace`, e.g. `marker-highlight`, `audio-reactive-pulse`, `caption-word-pop`. Phase 1 lists these in its `retention_component_picks:` block per scene; Phase 3.5 expands them with per-scene timing in seconds.

---

## 1. Marker Highlights (Word-Level Emphasis)

Pure CSS + GSAP marker effects on inline text. Source: `.agents/skills/hyperframes/references/css-patterns.md`.

| Canonical name      | What it does                                 | Use for                                                | When to skip                                              |
| ------------------- | -------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| `marker-highlight`  | Yellow/accent bar sweeps in behind text      | Stat callouts, key terms, term-branded concepts        | When the surrounding text is already heavily styled       |
| `marker-circle`     | Hand-drawn ellipse around text               | One-off emphasis on a noun (product name, person)      | Multi-line phrases — circle distorts                      |
| `marker-burst`      | Radiating lines from text                    | Surprise reveals, "boom" moments, viewer reactions     | Calm/measured tones — too loud                            |
| `marker-scribble`   | Chaotic scribble over text                   | Crossing out a wrong claim before stating the right one| When you need the original text to stay readable          |
| `marker-sketchout`  | Rough rectangle outline                      | Containing a quote or stat block                       | When a real `<blockquote>` / pill is already used         |

**Wiring pattern**: `<span class="mh-highlight-wrap"><span class="mh-highlight-bar" id="hl-1"></span><span class="mh-highlight-text">…</span></span>`. CSS + GSAP code at `css-patterns.md:14-46` for `marker-highlight`; same file enumerates the other four.

**Frequency cap**: max 2 marker highlights per scene. More than that and the eye stops noticing them.

---

## 2. Caption Patterns (Narration-Synced Word Flow)

Word-level captions driven by `transcript.json` (whisper output). Source: `.agents/skills/hyperframes/references/captions.md`.

| Canonical name           | What it does                                     | Use for                                            | Tone fit                          |
| ------------------------ | ------------------------------------------------ | -------------------------------------------------- | --------------------------------- |
| `caption-word-pop`       | Each word scale-pops on its `start` timestamp    | Hype/launch, Shorts hooks                          | Energetic                         |
| `caption-fade-slide`     | Word group fades + slides in                     | Corporate, SaaS explainer                          | Measured                          |
| `caption-typewriter`     | Char-by-char per word group                      | Tutorial, code walkthrough                         | Technical                         |
| `caption-elegant-fade`   | Slow fade per word group, serif preferred        | Storytelling, brand video                          | Calm                              |
| `caption-bounce-bubble`  | Elastic-ease per word, optional rounded pill BG  | Social, playful, viral Shorts                      | Playful                           |

**Style mapping table**: `captions.md:51-58`. Word-grouping rules: high energy = 2-3 words/group, conversational = 3-5, calm = 4-6.

**Per-word call-outs**: ANY caption pattern can apply per-word styling (color, scale boost) to brand names, ALL CAPS words, numbers/stats, emotional keywords, CTA verbs. See `captions.md:39-47`.

**Positioning**: portrait (1080x1920) → bottom 600-700px from bottom; landscape → bottom 80-120px. Use `position: absolute`, never relative. One caption group visible at a time.

---

## 3. Audio-Reactive Effects (Pulse on Beat / Voice)

Drive any GSAP-tweenable property from pre-extracted audio bands. Source: `.agents/skills/hyperframes/references/audio-reactive.md`.

| Canonical name             | Audio band         | Visual property         | Use for                                         |
| -------------------------- | ------------------ | ----------------------- | ----------------------------------------------- |
| `audio-reactive-pulse`     | Bass (band 0)      | `scale`                 | Whole-element beat pulse (logo, hero card)      |
| `audio-reactive-glow`      | Treble (bands 12+) | `textShadow`/`boxShadow`| Letter glow under speech, halo on numbers       |
| `audio-reactive-breathe`   | Overall amplitude  | `opacity`/`y`           | Background ambient layers                       |
| `audio-reactive-morph`     | Mid (bands 4-8)    | `borderRadius`/`width`  | Shape morphing on shapes/cards                  |
| `audio-reactive-color-shift`| Overall amplitude | CSS custom property      | Background hue shifts driven by narration energy|

**Constraint**: `audio-reactive.md:38-57` — sampling MUST use a `for` loop with `tl.call()` per frame, NOT a single tween. Without per-frame sampling, the composition does not actually react.

**Subtlety rules**: text → 3-6% scale variation; non-text → 10-30% swings.

**Banned visual vocab** (per `audio-reactive.md:32-35`): equalizer bars, spectrum analyzers, waveform displays, generic particle systems, rainbow color cycling, strobing white on beats. Always pick a visual that comes from the *content*, not a stock "music visualization."

---

## 4. Scene Transitions (Between-Scene Handoff)

CSS or shader transitions between sub-compositions. Source: `.agents/skills/hyperframes/references/transitions.md` and the per-category files in `transitions/`.

**Energy → primary transition** (per `transitions.md:14-20`):

| Energy  | CSS primary                  | Shader primary                  | Duration  | Easing                |
| ------- | ---------------------------- | ------------------------------- | --------- | --------------------- |
| Calm    | `blur-crossfade`, `focus-pull` | `cross-warp-morph`              | 0.5-0.8s  | `sine.inOut`, `power1`|
| Medium  | `push-slide`, `staggered-blocks`| `whip-pan`, `cinematic-zoom` | 0.3-0.5s  | `power2`, `power3`    |
| High    | `zoom-through`, `overexposure` | `glitch`, `chromatic-split`     | 0.15-0.3s | `power4`, `expo`      |

**Selection rule**: Pick ONE primary (60-70% of scene changes) + 1-2 accents. Never use a different transition for every scene.

**Anti-rule** (per `transitions.md:11`): exit animations are BANNED except on the final scene. The transition IS the exit. Outgoing scene content stays fully visible until the transition fires.

**Full transition catalog**: `transitions/catalog.md` enumerates GSAP code + hard rules for every named transition. Phase 1 picks names from there; Phase 3.5 may refine the choice based on adjacent scene content.

---

## 5. GSAP Effects (Content-Layer Animations)

Drop-in animation patterns. Source: `.agents/skills/gsap/references/effects.md`.

| Canonical name        | What it does                                           | Use for                                          |
| --------------------- | ------------------------------------------------------ | ------------------------------------------------ |
| `gsap-typewriter`     | Char-by-char text reveal via TextPlugin                | Code blocks, CLI prompts, "what they typed"     |
| `gsap-counter-tween`  | Number tweens from 0 → target via `roundProps`         | Stat reveals ("0 → 42 services")                 |
| `gsap-stagger-grid`   | `gsap.from()` with `stagger:` over a grid              | Logo grids, feature pills, timeline cards        |
| `gsap-path-draw`      | SVG `strokeDashoffset` animation                       | Hand-drawn underlines, arrows, flow diagrams     |
| `gsap-flip-reveal`    | FLIP technique for layout transitions                  | Card expands → fullscreen, list collapses → row  |

**Required plugin imports** vary by effect. Always load from `https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/...` per HyperFrames CDN convention.

**Determinism rule**: every effect must be deterministic — no `Date.now()`, no `Math.random()`, no runtime web fetch. Pre-compute any random-looking offsets at script-write time.

---

## 6. Composition Structure (Sub-Comp Layout Picks)

Not animations — *structural* retention picks that shape how a scene is composed. Source: HyperFrames CLAUDE.md "Key Rules" + `templates/shorts/anthropic/README.md`.

| Canonical name              | What it does                                                | Use for                                               |
| --------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| `inline-phase`              | Scene lives inside `index.html` as a `.phase` div           | Anthropic Shorts (template enforces 4 inline phases)  |
| `sub-composition`           | Scene is its own HTML file under `compositions/`, parent loads via `data-composition-src` | Long-form, when scene is genuinely self-contained or reusable |
| `mutex-visibility`          | Only one phase visible at a time; transitions handle handoff | Multi-phase shorts (Hero/Stat/Timeline/CTA pattern) |
| `progress-track`            | Persistent thin progress bar across the whole composition   | Long-form, when you want a visible runtime indicator  |

**Anthropic Shorts constraint**: `templates/shorts/anthropic/README.md:11-18` — for the Anthropic Shorts template, scenes MUST use `inline-phase` + `mutex-visibility`. To go beyond the four shipped phases, follow the "Adding more phases" section in that README — bump `data-duration`, add a new `<div class="phase">` with a unique id and z-index, and follow the `P1, T1, P2, T2…` naming convention.

---

## 7. Retention Pattern Library (Composite Picks)

Higher-level "named patterns" that combine 2-3 components above. Phase 3.5 may pick these instead of individual primitives when a scene's archetype is well-understood.

| Pattern name           | Composition                                                                                       | Use for                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `hero-slam`            | `inline-phase` + 240px slam word + `gsap-stagger-grid` (overline → slam → caption pill)           | Scroll-stop hook (Anthropic Phase 1)     |
| `stat-pill-row`        | `inline-phase` + 2 huge stat pills + `gsap-counter-tween` per number + `marker-highlight` on units| Receipts ("X bugs / Y weeks", Phase 2)   |
| `timeline-cards`       | `inline-phase` + 3 dated cards + `gsap-stagger-grid` entrance + per-card accent rotation          | Dated event sequence (Phase 3)           |
| `cta-url-slam`         | `inline-phase` + URL pill + subscribe pill + optional `marker-circle` on URL                      | Closing CTA (Anthropic Phase 4)          |
| `code-walkthrough`     | `sub-composition` + `gsap-typewriter` + per-line `caption-fade-slide` synced to narration          | Tutorial scenes, command demos           |
| `audio-pulsed-logo`    | `inline-phase` + brand logo + `audio-reactive-pulse` on bass + `audio-reactive-glow` on treble    | Brand reveal under narration emphasis    |
| `narrated-stat-reveal` | Number element + `gsap-counter-tween` driven by narration timing + `caption-word-pop` for the digit| Stat scenes where the narrator says the number aloud |

These compose primitives — they are not new framework features. A `hero-slam` pick expands to "use `inline-phase` structure, choose `gsap-stagger-grid` for entrance, no audio-reactivity on text".

---

## 8. Anti-Patterns (Banned Picks)

Things Phase 1 / Phase 3.5 must NOT prescribe:

- **Anything Remotion**: `SyncedAnimatedText`, `SyncedCodeBlock`, `TypeWriter` (Remotion bits), `TransitionSeries`, `Composition.tsx`, frame-counted spring configs from `hookSprings.ts`. None exist in HyperFrames.
- **Any spectrum/equalizer visual** (per `audio-reactive.md:32-35`).
- **Exit animations on non-final scenes** (per `transitions.md:11`).
- **More than 2 markers per scene** — viewer eye stops registering them.
- **Caption groups overlapping in time** — only one group visible at any moment.
- **Mixing `inline-phase` and `sub-composition` arbitrarily** — pick one structural model per video. Sub-comps are for genuine reuse or scene isolation; otherwise stay inline.
- **Different transition for every scene** — pick one primary + 1-2 accents.

---

## 9. Quick Lookup — "How do I render X in HyperFrames?"

| The script wants to…                          | Pick this                                                         |
| --------------------------------------------- | ----------------------------------------------------------------- |
| Highlight a single key term                   | `marker-highlight` (max 2/scene)                                  |
| Reveal text char-by-char                      | `gsap-typewriter`                                                 |
| Show numbers ticking up                       | `gsap-counter-tween`                                              |
| Flash captions in sync with narration         | `caption-word-pop` (energetic) or `caption-fade-slide` (calm)     |
| Pulse the logo on the beat                    | `audio-reactive-pulse` on the logo's `scale`                      |
| Soft glow under spoken emphasis               | `audio-reactive-glow` on `textShadow` of the active word          |
| Soft handoff between two scenes               | `blur-crossfade` (calm) or `crossfade` (medium)                   |
| Punchy handoff between two scenes             | `zoom-through` or `staggered-blocks`                              |
| 4-phase Anthropic Short                       | `hero-slam` → `stat-pill-row` → `timeline-cards` → `cta-url-slam` |

---

## Appendix: Source File Index

For deep dives, read these files in `.agents/skills/`:

- `hyperframes/references/css-patterns.md` — all 5 marker highlight modes (HTML + CSS + GSAP)
- `hyperframes/references/captions.md` — per-word styling, transcript shape, style detection
- `hyperframes/references/audio-reactive.md` — band → property mapping, sampling pattern, banned vocab
- `hyperframes/references/transitions.md` + `transitions/catalog.md` — full transition library with code
- `hyperframes/references/transcript-guide.md` — the `transcript.json` shape Phase 3.5 reads
- `hyperframes/references/typography.md`, `motion-principles.md`, `dynamic-techniques.md` — supporting refs
- `gsap/references/effects.md` — typewriter + audio visualizer patterns

Phase 1 and Phase 3.5 should treat this file as the *menu* and the linked references as the *recipes*.
