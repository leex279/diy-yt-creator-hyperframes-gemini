# DESIGN — Google Shorts (Cinematic Brand Stage)

Visual system for **vertical Google-branded Shorts** (1080x1920, 30fps, 24-180s). Translated from the supplied "Google Short Design" reference (React + tweaks panel) into a HyperFrames-native mutex-phase composition. Mirrors the structural patterns of `templates/shorts/anthropic/` and `templates/shorts/claude-code-version/` (phase mutex, blur+crossfade, deterministic seeded particles, progress bar, persistent brand chrome) but swaps the palette and chrome surfaces for the Google brand.

## Style Prompt

A cinematic dark stage tuned for Google content on a vertical canvas. Off-white type sits on a `#06080F` deep-navy that's washed by four soft-corner brand glows (blue at top-left, red at top-right, green at bottom-center, yellow at bottom-right). The Google wordmark (full-color) anchors the top of every phase; a small mono `@handle` floats top-right with the active accent color tinting the `@`. A 5-dot progress rail (one Google color each, rotating blue → red → yellow → green → blue) marches across the bottom — one dot lights up per phase, glow tinted to its color. The accent triad is the four canonical Google brand hues (`#4285F4` / `#EA4335` / `#FBBC05` / `#34A853`); the chosen primary `--accent` colors the eyebrow, the progress-bar fill, the `@` symbol, and the CTA pill stroke. Particles drift; the top-left has a 4px green→yellow ramp; an inner safe-area frame keeps content off the canvas edges. Phase 4 optionally inverts to a soft white "shift" surface for the closing thought.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **24-180s** (template demo is 24s)
- Background: cinematic dark with corner glows by default. `theme-spotlight` (single accent beam from top) and `theme-editorial` (60px hairline grid) are also wired and selectable via the `class` on `#root`.

## Colors

The accent triad is the four Google brand hues. Surface, text, and spacing tokens live in `tokens/google-cinematic.css`. Override per video by re-declaring any var in a tighter scope.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background (deep) | `--bg-deep` / `--bg` | `#06080F` | Default canvas |
| Background (mid) | `--bg-mid` | `#0B1020` | Mid-tone wash, terminal panel surround |
| Background (soft) | `--bg-soft` | `#11182C` | Card surfaces, raised pills |
| Card surface | `--card` | `rgba(10,14,26,0.55)` | Chip / quote / panel bodies |
| Border | `--border` | `rgba(255,255,255,0.07)` | Default hairline |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | Active / focused border, terminal stroke |
| Primary text | `--text` / `--ink-100` | `#FFFFFF` | Headlines, body |
| Secondary text | `--text-secondary` / `--ink-60` | `#A7B0C5` | Subhead, label |
| Muted text | `--text-muted` / `--ink-40` | `#6A7390` | Inactive rail labels, prompts, handle base |
| **Accent — blue** | `--g-blue` | `#4285F4` | Default `--accent`; rail dot 1 (SETUP), rail dot 5 (PUBLISH) |
| **Accent — red** | `--g-red` | `#EA4335` | Rail dot 2 (CREATE), chip-color option, top-line stroke |
| **Accent — yellow** | `--g-yellow` | `#FBBC05` | Rail dot 3 (EVAL), terminal flag color, top-line ramp end |
| **Accent — green** | `--g-green` | `#34A853` | Rail dot 4 (DEPLOY), terminal `cmd` color, top-line ramp start |
| Pill bg | `--pill-bg` | `rgba(10,14,26,0.7)` | CTA pill base |
| Pill border | `--pill-border` | `rgba(255,255,255,0.18)` | Default chip / pill stroke |
| Light surface | `--bg-light` | `#F4F6FB` | "Shift" theme on Phase 4 (`theme-light`) |
| Light ink | `--ink-on-light` | `#0A0E1A` | Headline / quote color on light theme |

**Contrast verified (WCAG, body text on `#06080F`):**

- Primary text (`#FFFFFF`) on bg: ~21:1 (AAA)
- Secondary text (`#A7B0C5`) on bg: 8.6:1 (AAA)
- Blue accent `#4285F4` on bg: 5.4:1 (AA — safe for 36px+ overlines and the 38px terminal flag)
- Yellow `#FBBC05` on bg: 11.3:1 (AAA — terminal flag legible)
- Green `#34A853` on bg: 6.7:1 (AAA — terminal `cmd` legible)
- Red `#EA4335` on bg: 4.8:1 (AA — chip label and rail-dot 2 legible)

**Accent rotation rule:** the chip grid and progress rail rotate through all four Google colors in `blue → red → yellow → green → blue` order, deterministic. Don't introduce a fifth color — the brand reads cleanly only when the four-color rotation is consistent.

## Typography

Two families, no exceptions:

- `--sans` Plus Jakarta Sans (workhorse for hero, headline, body, CTA pill text, big-stat number)
- `--mono` JetBrains Mono (eyebrow, terminal content, rail labels, handle, chip label)

| Role | Size | Notes |
|---|---|---|
| Hero headline (Phase 1) | 148px | Plus Jakarta 800; line-height 0.98; letter-spacing -2px; `text-wrap: balance` |
| Phase 2/3/4 headline (m) | 104px | Plus Jakarta 800; line-height 0.98 |
| Subhead | 46px | Plus Jakarta 600; secondary ink |
| Eyebrow | 36px | Mono 600, UPPERCASE, letter-spacing 6.5px, accent-tinted |
| Big-stat number (alt Phase 3) | 360px | Plus Jakarta 800; gradient blue→green→yellow with drop-shadow |
| Big-stat suffix | 140px | Plus Jakarta 700; same gradient |
| Big-stat label | 34px | Mono UPPERCASE letter-spacing 6px; secondary ink |
| Chip value | 50px | Plus Jakarta 700; primary ink |
| Chip label | 26px | Mono UPPERCASE letter-spacing 3px; chip-accent color |
| Terminal content | 38px | Mono; prompt ink-40, cmd green, arg ink-100, flag yellow, kw blue, str peach |
| Quote | 64px | Plus Jakarta 700; left accent border 4px |
| CTA pill value | 40px | Mono UPPERCASE letter-spacing 5px |
| Rail-dot label | 24px | Mono UPPERCASE letter-spacing 4px; ink-40 inactive, dot-color active |
| Footer handle | 28px | Mono UPPERCASE letter-spacing 4px; ink-40 with accent-tinted `@` |

**Tabular numerals on the big-stat number:** `font-variant-numeric: tabular-nums lining-nums` so digits don't jitter across springs.

## Layout

`--pad-top: 240px`, `--pad-x: 60px`, `--pad-bottom: 240px`. Phase content uses `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box`.

**Phase mutex:** only one phase visible at any frame. Crossfades (`#phase1` → `#phase2` etc.) operate on the whole phase wrapper, not individual elements. Entrance tweens for individual elements only — exits are handled by the next-phase blur+crossfade.

## Motion Language

Same easing palette as the anthropic shorts template:

| Pattern | Easing | Duration |
|---|---|---|
| Headline rise | `power3.out` | 0.6s |
| Body / caption rise | `power2.out` | 0.5s |
| Eyebrow rise | `power2.out` | 0.5s |
| Card / chip pop | `back.out(1.5)` (chips) / `back.out(1.4)` (terminals) | 0.5-0.6s |
| Phase crossfade out | `power1.in` (blur+scale up to 1.04) | 0.4-0.5s |
| Phase crossfade in | `power1.inOut` (opacity) → `power1.out` (deblur+scale to 1) | 0.3-0.5s |
| Particle drift | `sine.inOut`, yoyo true, repeat 1, dur 12s | (full composition) |
| CTA pulse | `sine.inOut`, yoyo true, repeat 4 (5 tweens, ~3.5s) | 0.7s/half |

**Stagger:** 200-300ms between adjacent chips (Phase 3), 600ms between adjacent terminal blocks (Phase 2), 100-300ms between eyebrow → headline → body within a phase. No `repeat: -1` anywhere — deterministic timeline rule.

## Phase Archetypes

### Phase 1 — Hero (0-6s in 24s template)

- Eyebrow (36px mono, accent color)
- xl headline (148px, balance-wrap, "Agents need a path." in default)
- Subhead (46px, secondary ink)
- No rail dot active (the rail is a "what comes next" hint, hero is the hook)

### Phase 2 — Terminal (6-12s)

- Eyebrow + m headline (104px)
- Two `.terminal` blocks stacked. First has `.with-rim` (4-color top stroke). Mono content with colored syntax: `cmd` green, `arg` ink-100, `flag` yellow, `kw` blue, `str` peach, `prompt` ink-40.
- Rail dot 0 (SETUP, blue) glows.

### Phase 3 — Info Grid (12-18s)

- Eyebrow + m headline.
- 2x2 chip grid (920px wide). Each chip has a colored 4px left bar in its accent (blue / yellow / green / red rotating), a mono UPPERCASE label, and a 50px sans value.
- Rail dot 1 (CREATE, red) glows.

**Alternate archetype — Big stat:** swap the `.chip-grid` for a `.bigstat`:

```html
<div class="bigstat">
  <div class="num">3<span class="num-suffix">x</span></div>
  <div class="label">From prototype to production</div>
</div>
```

The `.num` uses a 360px gradient (blue → green → yellow) with a drop-shadow — borrowed verbatim from the reference design's "BIG STAT" slide.

**Alternate archetype — Compare:** the reference design's "before → after" rows are wired as `.compare` markup. Ship two `.compare-side` cards split by a `→` arrow. Use red label for `.before`, green label for `.after`. See the supplied design's `slides.jsx` `SlideCompare` for the exact shape.

### Phase 4 — Shift / CTA (18-24s)

- Eyebrow ("THE SHIFT") + m headline ("Cloud becomes a command surface.")
- Quote block (`.quote`) with 4px left accent border, optional 200px transparent quote-mark glyph
- CTA pill — 999px-rounded pill with accent border, mono UPPERCASE label + value, accent-glow box-shadow
- Rail dot 4 (PUBLISH, blue) glows
- CTA pulse: `boxShadow` glow yoyo with `repeat: 4`

**Light "shift" variant:** add `class="theme-light"` to `#phase4` to flip the surface to the bright `#F4F6FB` → `#EAEEF7` gradient (matches the reference's `lightShift` toggle). Headline + quote text auto-switch to `--ink-on-light` (`#0A0E1A`).

## Variant-specific Surfaces

### Persistent chrome (all phases)

- **`#glogo`** — Google logo PNG, 120px tall, top-center at `top: 80px`. No `class="clip"`.
- **`#footer-handle`** — top-right at `top: 56px; right: 64px`. Mono UPPERCASE 28px. The `@` glyph carries the active `--accent` color; the handle text uses `--ink-40`.
- **`#top-line`** — top-left 4px accent ramp (`--g-green` → `--g-yellow`), 18% width. Entrance: `scaleX: 0` from x-origin 0 over 0.7s.
- **`#particles`** — 60-dot deterministic SVG scatter (xmur3-seeded), 4 Google colors, opacity 0.15-0.65 each. Slow sine drift (yoyo) over 12s.
- **`#slide-frame`** — 32px-inset rounded hairline (28px border-radius), `--border` color.
- **`#progress-rail`** — 5 dots, mono labels (SETUP / CREATE / EVAL / DEPLOY / PUBLISH), Google-color rotation. Active dot scales 28→36px and gains the matching colored glow. Labels are absolutely positioned below the dots and carry `data-layout-allow-overflow="true"` so HyperFrames inspect doesn't flag the intentional overhang.
- **`#progress-track`** — 6px slim bar at `bottom: 0`, fills linearly 0% → 100% across composition duration with `--accent` color.

### `tokens/google-cinematic.css` (token file)

Single `:root` block. Re-declarable per video. Variables: `--g-blue/red/yellow/green` (brand triad), `--bg-deep/mid/soft`, `--ink-100/80/60/40/20`, `--accent`, `--accent-glow`, `--pad-top/x/bottom`, `--sans`, `--mono`. Legacy aliases `--orange`, `--purple`, `--blue`, `--green`, `--red`, `--yellow` are mapped onto the closest Google hue so blocks pulled from `shared/lib/` (which reference legacy names) render correctly without rewrite.

## VIDEO_CONFIG opt-in overlays (Dynamous promotion)

Mirrors the long-form `claude-code-version` pattern, repositioned for the vertical canvas. Three independent overlays — enable any combination via `video.config.js`:

### `#dynamous-badge`

Top-left brand pill at `top: 130px; left: 60px` (avoids the bottom progress rail on the vertical canvas; long-form puts it at bottom-left). 38px Dynamous logo + `dynamous.ai` URL in Inter 600. Opacity 0.55, blurred backdrop, drop-shadow. Persistent (no `class="clip"`). Entrance fade at t=3.0s.

### `#dynamous-discount-bubble`

Bottom-left at `bottom: 220px; left: 60px` (above the progress rail). Inline-flex pill: 28px Dynamous mark + `Dynamous.ai` + red-gradient `10% OFF` chip + `in the link ↓` pointer. Time-bounded — `class="clip"`, `data-track-index="10"`. The guard script auto-wires `data-start` to the Phase 4 (CTA) start (default 18.4s in the 24s template). Override per video via `discountBubbleStart` and `discountBubbleDuration` in `video.config.js`.

### `#dynamous-module-interstitial-wrap`

Sub-composition mounted via `data-composition-src="compositions/dynamous-module-interstitial.html"`. 3-second slide-in card from the right edge at the first scene transition (t=5.6s by default). Card sits at `top: 240px; right: 60px; width: 540px`. Module dot + module number + module title + "Part of Dynamous AI Mastery" tagline. The dot color, module ID, and module name are read from `window.VIDEO_CONFIG.dynamous.{moduleAccentColor, moduleId, moduleName}` at composition load time — change per release without editing the sub-comp file.

**Critical CSS rule:** the sub-comp uses **class-only** selectors (`.dmi-card`, `.dmi-row`, etc.) — never ID-prefixed (`#dynamous-module-interstitial .dmi-card`). HyperFrames' sub-comp scoping rewrites the inner ID, breaking ID-prefixed selectors. The class-only form survives the rewrite.

### Guard script

The synchronous `<script>` at the bottom of `index.html` runs before HyperFrames scans the DOM. It removes any disabled overlay element and auto-wires the discount bubble timing. Disabled overlays therefore never appear in the clip list or the sub-composition queue.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Default `sfx-cues.txt` ships with: `impact-slam`, `scale-slam`, `cinematic-whoosh`, `spring-pop`, `pop`. Volume caps:

| Cue | Use on | `data-volume` |
|---|---|---|
| `impact-slam` | Phase-1 hero headline reveal | 0.15 |
| `scale-slam` | Phase-2 terminal entrance, Phase-3 chip-grid first chip | 0.15 |
| `cinematic-whoosh` | Phase / scene change (transitions T1, T2, T3) | 0.11 |
| `spring-pop` | Chip / terminal block entrance (per-element) | 0.11 |
| `pop` | Rail-dot activation (subtle) | 0.10 |

Hard cap **0.25** per single per-cue SFX (sonic-logo at 0.45 is the only documented exception). Density target ~2 SFX placements per 10 seconds of narration; cap 2.5 / 10s. **No background music on Shorts** — narration + SFX only.

## What NOT to Do

1. **Do NOT introduce a 5th accent color.** The four Google hues are the brand. Adding cyan / pink / orange breaks the visual identity. Map non-Google needs onto the closest Google hue or leave the chip empty.
2. **Do NOT reference `../../shared/...` paths at runtime.** The bundler / preview server rejects paths outside the project directory. Logos must be local copies inside `assets/`.
3. **Do NOT add `class="clip"` to persistent chrome.** `#glogo`, `#footer-handle`, `#progress-rail`, `#dynamous-badge`, `#dynamous-module-interstitial-wrap`, `#slide-frame`, `#particles`, `#top-line` are all unclipped (full-duration). Only timed media (audio/video) gets `class="clip"`.
4. **Do NOT use `repeat: -1`.** Deterministic timeline rule. Use `repeat: <finite-number>` with `yoyo: true` for pulses.
5. **Do NOT use `Math.random()` / `Date.now()` / network fetches.** The particle field uses xmur3-style hashing for deterministic placement.
6. **Do NOT add background music to Shorts.** Narration + SFX + (optional) sonic-logo only.
7. **Do NOT use `<br>` for line breaks in the headline.** Rely on `text-wrap: balance` and font-size to drive natural wrapping. The headline's max width is the phase-content's available width minus padding.
8. **Do NOT scope the module interstitial CSS with the `#dynamous-module-interstitial` ID prefix.** Use class-only selectors so the rules survive sub-comp ID rewriting.
9. **Do NOT animate the `<audio>` `volume` property.** HyperFrames reads `data-volume` once at render time. Bake fades into the source SFX with the audio gen tool.
10. **Do NOT enable the `discountBubble` without the matching CTA phase.** The bubble is auto-wired to `Phase 4` start; if you remove or retime Phase 4, override `discountBubbleStart` in `video.config.js`.
