# DESIGN — OpenAI Shorts (Monochrome Editorial + Mint)

Visual system for **vertical OpenAI-branded Shorts** (1080x1920, 30fps, 24-180s). Forked from `templates/shorts/google/` and re-skinned to the OpenAI brand's quieter editorial register. Mutex-phase architecture, sub-slide CSS, Dynamous overlay wiring, and `video.config.js` knobs are unchanged from the Google variant — palette, brand chrome, and accent rotation are what changed.

## Style Prompt

A monochrome editorial stage tuned for OpenAI content on a vertical canvas. Off-white type (`#ECECEC`) sits on an off-black `#0A0A0A` canvas — no corner glows by default, no four-color rotation, no cinematic flourishes. A single mint accent (`#10A37F` — the canonical ChatGPT hue) threads through the eyebrow, the active rail dot, the progress-bar fill, the `@` symbol, and the CTA pill stroke. The ChatGPT spirograph anchors the top of every phase (swap to the OpenAI wordmark for GPT/Sora/DALL·E videos); a small mono `@handle` floats top-right with the mint `@`. A 5-dot progress rail (INTRO → BUILD → SIGNAL → SHIFT → CTA) marches across the bottom — one dot lights mint per phase. A sparse monochrome particle field (40 dots in three off-white tints) drifts behind the content. An inner safe-area frame (rounded hairline border) keeps content off the canvas edges. Phase 4 optionally inverts to a soft warm-white "shift" surface for the closing thought.

The aesthetic anchor: **the surface you'd find on openai.com/research**, not openai.com/sora. Calm, premium, restrained. The video's narrative does the work; the visuals don't compete.

## Canvas

- Resolution: **1080 x 1920** (vertical Shorts)
- Frame rate: **30fps**
- Duration target: **24-180s** (template demo is 24s)
- Background: `theme-quiet` by default — flat `#0A0A0A` → `#060606` linear gradient, no glows. `theme-cinematic` adds a single soft mint top-center glow; `theme-editorial` adds a faint 60px hairline grid. Default is `theme-quiet`.

## Colors

The accent triad is **one** mint hue with three auxiliary tints reserved for explicit override. Surface, text, and spacing tokens live in `tokens/openai-mono.css`. Override per video by re-declaring any var in a tighter scope.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background (deep) | `--bg-deep` / `--bg` | `#0A0A0A` | Default canvas — softer than pure black |
| Background (mid) | `--bg-mid` | `#111111` | Mid-tone wash, terminal panel surround |
| Background (soft) | `--bg-soft` | `#181818` | Card surfaces, raised pills |
| Card surface | `--card` | `rgba(20,20,20,0.55)` | Chip / quote / panel bodies |
| Border | `--border` | `rgba(255,255,255,0.08)` | Default hairline |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | Active / focused border, terminal stroke |
| Primary text | `--text` / `--ink-100` | `#ECECEC` | Headlines, body — off-white, not pure white |
| Secondary text | `--text-secondary` / `--ink-60` | `#A0A0A0` | Subhead, label |
| Muted text | `--text-muted` / `--ink-40` | `#7A7A7A` | Inactive rail labels, prompts, handle base |
| **Primary accent — mint** | `--oai-mint` / `--accent` | `#10A37F` | Default accent: eyebrow, active rail dot, CTA pill stroke, `@` symbol, progress-bar fill |
| Mint (bright) | `--oai-mint-hi` | `#19C37D` | Hover-style emphasis; bigstat gradient endpoint |
| Mint (dark) | `--oai-mint-lo` | `#0E7E61` | Hairlines, dim accents |
| Auxiliary — lavender | `--oai-lavender` | `#A78BFA` | Sora-flavored override; never default |
| Auxiliary — amber | `--oai-amber` | `#F0B86E` | DALL·E-flavored override; terminal flag color |
| Auxiliary — coral | `--oai-coral` | `#FF6E5A` | Warning / regression callout; rare |
| Pill bg | `--pill-bg` | `rgba(20,20,20,0.7)` | CTA pill base |
| Pill border | `--pill-border` | `rgba(255,255,255,0.18)` | Default chip / pill stroke |
| Light surface | `--bg-light` | `#F4F4F2` | "Shift" theme on Phase 4 (`theme-light`) — warm off-white |
| Light ink | `--ink-on-light` | `#0A0A0A` | Headline / quote color on light theme |

**Contrast verified (WCAG, body text on `#0A0A0A`):**

- Primary text (`#ECECEC`) on bg: ~17:1 (AAA)
- Secondary text (`#A0A0A0`) on bg: 7.8:1 (AAA)
- Muted text (`#7A7A7A`) on bg: 4.6:1 (AA — safe for ≥18px UI text)
- Mint accent `#10A37F` on bg: 6.2:1 (AAA — safe for the 36px eyebrow and the 38px terminal `cmd`)
- Lavender `#A78BFA` on bg: 7.6:1 (AAA — safe for any size)
- Amber `#F0B86E` on bg: 10.4:1 (AAA — terminal flag legible)
- Coral `#FF6E5A` on bg: 5.4:1 (AAA — warning callout legible)

**Single-accent rule:** the chip grid, progress rail, terminal `cmd`, and CTA pill all share the **same** `--accent` (mint by default). Don't introduce a fifth color, and don't rotate accents across chips inside one phase — the OpenAI brand reads cleanly when the surface stays quiet. The auxiliary tints (lavender / amber / coral) exist for **explicit per-video override** (e.g. a Sora launch Short can swap `--accent` to lavender for the whole composition), never for per-element rotation within one video.

## Typography

Two families, no exceptions:

- `--sans` Inter (best free Söhne-substitute — OpenAI uses Söhne internally; Inter is the closest open-source pairing). Workhorse for hero, headline, body, CTA pill value.
- `--mono` JetBrains Mono (Söhne Mono substitute) — eyebrow, terminal content, rail labels, handle, chip label.

| Role | Size | Notes |
|---|---|---|
| Hero headline (Phase 1) | 148px | Inter 800; line-height 0.98; letter-spacing -2px; `text-wrap: balance` |
| Phase 2/3/4 headline (m) | 104px | Inter 800; line-height 0.98 |
| Subhead | 46px | Inter 500; secondary ink |
| Eyebrow | 36px | Mono 600, UPPERCASE, letter-spacing 6.5px, mint |
| Big-stat number (alt Phase 3) | 360px | Inter 800; gradient mint → bright-mint with drop-shadow |
| Big-stat suffix | 140px | Inter 700; same gradient |
| Big-stat label | 34px | Mono UPPERCASE letter-spacing 6px; secondary ink |
| Chip value | 50px | Inter 700; primary ink |
| Chip label | 26px | Mono UPPERCASE letter-spacing 3px; mint (default) or chip-accent |
| Terminal content | 38px | Mono; prompt ink-40, cmd mint, arg ink-100, flag amber, kw lavender, str ink-80 |
| Quote | 64px | Inter 700; left accent border 4px |
| CTA pill value | 40px | Mono UPPERCASE letter-spacing 5px |
| Rail-dot label | 24px | Mono UPPERCASE letter-spacing 4px; ink-40 inactive, mint active |
| Footer handle | 28px | Mono UPPERCASE letter-spacing 4px; ink-40 with mint `@` |

**Tabular numerals on the big-stat number:** `font-variant-numeric: tabular-nums lining-nums` so digits don't jitter across springs.

## Layout

`--pad-top: 240px`, `--pad-x: 60px`, `--pad-bottom: 240px`. Phase content uses `width: 100%; height: 100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box`.

**Phase mutex:** only one phase visible at any frame. Crossfades (`#phase1` → `#phase2` etc.) operate on the whole phase wrapper, not individual elements. Entrance tweens for individual elements only — exits are handled by the next-phase blur+crossfade.

## Motion Language

Same easing palette as the Google + Anthropic shorts templates:

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

**Stagger:** 200ms between adjacent chips (Phase 3), 600ms between adjacent terminal blocks (Phase 2), 100-300ms between eyebrow → headline → body within a phase. No `repeat: -1` anywhere — deterministic timeline rule.

## Phase Archetypes

### Phase 1 — Hero (0-6s in 24s template)

- Eyebrow (36px mono, mint)
- xl headline (148px, balance-wrap)
- Subhead (46px, secondary ink)
- Rail dot 0 (INTRO) glows mint — the rail is visible from frame 1 to give the viewer a "5 beats" wayfinding hint.

### Phase 2 — Terminal (6-12s)

- Eyebrow + m headline (104px)
- Two `.terminal` blocks stacked. First has `.with-rim` (mint hairline top stroke — replaces the Google template's four-color stroke). Mono content with colored syntax: `cmd` mint, `arg` ink-100, `flag` amber, `kw` lavender, `str` ink-80, `prompt` ink-40.
- Rail dot 1 (BUILD) glows mint.

### Phase 3 — Info Grid (12-18s)

- Eyebrow + m headline.
- 2x2 chip grid (920px wide). Each chip has a 4px left bar in mint (default), a mono UPPERCASE label, and a 50px sans value. The `data-color="mint|lavender|amber|coral"` attribute lets one chip lead with an auxiliary hue if the topic demands it — but the default in the demo is all-mint.
- Rail dot 2 (SIGNAL) glows mint.

**Alternate archetype — Big stat:** swap the `.chip-grid` for a `.bigstat`:

```html
<div class="bigstat">
  <div class="num">3<span class="num-suffix">x</span></div>
  <div class="label">From prototype to production</div>
</div>
```

The `.num` uses a 360px gradient (mint → bright mint) with a drop-shadow.

**Alternate archetype — Compare:** before → after rows are wired as `.compare` markup (same pattern as the Google template). Ship two `.compare-side` cards split by a `→` arrow. Use coral for `.before`, mint for `.after`.

### Phase 4 — Shift / CTA (18-24s)

- Eyebrow ("THE SHIFT") + m headline ("Models become a quiet utility.")
- Quote block (`.quote`) with 4px left accent border, optional 200px transparent quote-mark glyph
- CTA pill — 999px-rounded pill with accent border, mono UPPERCASE label + value, accent-glow box-shadow
- Rail dot 3 (SHIFT) glows mint at headline beat → rail dot 4 (CTA) glows as the pill appears 1.4s later
- CTA pulse: `boxShadow` glow yoyo with `repeat: 4`

**Light "shift" variant:** add `class="theme-light"` to `#phase4` to flip the surface to a warm `#F4F4F2` → `#EAEAE6` gradient. Headline + quote text auto-switch to `--ink-on-light` (`#0A0A0A`).

## Variant-specific Surfaces

### Persistent chrome (all phases)

- **`#brand-mark`** — ChatGPT spirograph (`assets/chatgpt-mark.svg`), 110px tall, top-center at `top: 80px`. No `class="clip"`. Operators can swap for `assets/openai-wordmark.png` per video (see README — drop height to 80-90px for the wordmark).
- **`#footer-handle`** — top-right at `top: 56px; right: 64px`. Mono UPPERCASE 28px. The `@` glyph carries `--accent` (mint by default); the handle text uses `--ink-40`.
- **`#particles`** — 40-dot deterministic SVG scatter (xmur3-seeded), 3 off-white tints (236/160/107 luminance), opacity 0.15-0.60 each. Slow sine drift (yoyo) over 12s. Sparser than the Google template (60 dots / 4 colors) to preserve the editorial feel.
- **`#slide-frame`** — 32px-inset rounded hairline (28px border-radius), `--border` color.
- **`#progress-rail`** — 5 dots, mono labels (INTRO / BUILD / SIGNAL / SHIFT / CTA), all dots use the same mint accent when active (no per-dot color rotation, unlike the Google template). Active dot scales 24→32px and gains mint glow. Labels are absolutely positioned below the dots and carry `data-layout-allow-overflow="true"` so HyperFrames inspect doesn't flag the intentional overhang.
- **`#progress-track`** — 6px slim bar at `bottom: 0`, fills linearly 0% → 100% across composition duration with `--accent` (mint) color.

### `tokens/openai-mono.css` (token file)

Single `:root` block. Re-declarable per video. Variables: `--oai-mint/mint-hi/mint-lo/lavender/amber/coral` (brand triad), `--bg-deep/mid/soft`, `--ink-100/80/60/40/20`, `--accent`, `--accent-glow`, `--pad-top/x/bottom`, `--sans` (Inter), `--mono` (JetBrains Mono).

**Legacy aliases:** `--orange / --purple / --blue / --green / --red / --yellow` and `--g-blue / --g-red / --g-yellow / --g-green` are all mapped onto the closest OpenAI hue so blocks pulled from `shared/lib/` (which reference legacy names) render correctly without rewrite. Every legacy color → mint or auxiliary tint, never a Google-style four-color rotation.

## VIDEO_CONFIG opt-in overlays (Dynamous promotion)

Mirrors the Google variant. Three independent overlays + the endcard — enable any combination via `video.config.js`. The wiring (badge, discount-bubble, module-interstitial sub-comp, endcard sub-comp, guard script) is byte-identical to the Google variant. See [`templates/shorts/google/DESIGN.md`](../google/DESIGN.md) "VIDEO_CONFIG opt-in overlays" for the full mechanics — they apply here unchanged.

**Critical CSS rule (carried over):** the module-interstitial sub-comp uses **class-only** selectors (`.dmi-card`, `.dmi-row`, etc.) — never ID-prefixed. HyperFrames' sub-comp scoping rewrites the inner ID, breaking ID-prefixed selectors.

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

1. **Do NOT introduce a 5th accent color.** Mint is the brand. Lavender / amber / coral are reserved for explicit per-video overrides (Sora-flavored / DALL·E-flavored / warning). Adding cyan / pink / neon-green breaks the OpenAI editorial register.
2. **Do NOT rotate accents across chips inside one phase.** The chip grid is single-accent by design — every chip mint, or every chip lavender if the whole video is Sora-flavored. Per-chip color rotation is the Google pattern, not OpenAI.
3. **Do NOT reference `../../shared/...` paths at runtime.** The bundler / preview server rejects paths outside the project directory. Logos must be local copies inside `assets/`.
4. **Do NOT add `class="clip"` to persistent chrome.** `#brand-mark`, `#footer-handle`, `#progress-rail`, `#dynamous-badge`, `#dynamous-module-interstitial-wrap`, `#slide-frame`, `#particles` are all unclipped (full-duration). Only timed media (audio/video) gets `class="clip"`.
5. **Do NOT use `repeat: -1`.** Deterministic timeline rule. Use `repeat: <finite-number>` with `yoyo: true` for pulses.
6. **Do NOT use `Math.random()` / `Date.now()` / network fetches.** The particle field uses xmur3-style hashing for deterministic placement.
7. **Do NOT add background music to Shorts.** Narration + SFX + (optional) sonic-logo only.
8. **Do NOT use `<br>` for line breaks in the headline.** Rely on `text-wrap: balance` and font-size to drive natural wrapping.
9. **Do NOT scope the module interstitial CSS with the `#dynamous-module-interstitial` ID prefix.** Use class-only selectors so the rules survive sub-comp ID rewriting.
10. **Do NOT animate the `<audio>` `volume` property.** HyperFrames reads `data-volume` once at render time. Bake fades into the source SFX with the audio gen tool.
11. **Do NOT enable the `discountBubble` without the matching CTA phase.** The bubble is auto-wired to `Phase 4` start; if you remove or retime Phase 4, override `discountBubbleStart` in `video.config.js`.
12. **Do NOT use pure `#000000` for the background.** Stays at `#0A0A0A` (the deep bg token). Pure black reads as "missing rendered surface" on OLED screens; the off-black sits more comfortably as an editorial canvas.
13. **Do NOT use pure `#FFFFFF` for body text.** Stays at `#ECECEC` (off-white). Pure white on near-black is harsh on OLED; the off-white preserves the calm, premium register.
