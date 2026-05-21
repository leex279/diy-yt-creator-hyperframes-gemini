# DESIGN — Long-Form Google (Cinematic Brand Stage)

Visual system for **horizontal Google-branded long-form videos** (1920x1080, 30fps, typically 4-15 minutes). Translated from the [`src/GoogleCloudNext2026V2`](../../../) Remotion reference project into HyperFrames-native (HTML + GSAP), forked from `templates/long-form/standard/` and re-painted with the canonical Google brand four-hue rotation.

## Style Prompt

A cinematic dark stage tuned for Google content on a horizontal canvas. Off-white type sits on a near-black `#0C0C0E` deep stage, washed by four soft-corner brand glows (blue NW, red NE, yellow SE, green SW). The Google wordmark (full-color PNG, 180×180) anchors the top-right of every scene; a thin Google-blue → cyan progress bar tracks the bottom. Four canonical Google brand hues — blue `#4285F4`, red `#EA4335`, yellow `#FBBC04`, green `#34A853` — rotate through the accent slots. The Google Cloud accent cyan `#00BCD4` is reserved for the architecture-stack's 5th layer and the bottom progress-bar gradient end-stop; it is NOT a 5th rotation color. Motion is restrained but percussive — `back.out` springs on cards/pills, `expo.out` on hero reveals, `sine.inOut` on ambient breath. Reads like a premium Google product reel, not a creator upload.

## Canvas

- Resolution: **1920 x 1080** (horizontal, full HD)
- Frame rate: **30fps**
- Duration target: **4-15 minutes** (template demo is 120s)
- Background: solid `#0C0C0E` near-black. Four Google-color corner radials at low alpha (0.07-0.10) provide the brand wash. Full-screen linear gradients banding under H.264 is avoided — corner radials only.

## Colors

The accent triad is the four Google brand hues. Surface, text, and spacing tokens live in `tokens/long-form.css`. Override per video by re-declaring any var in a tighter scope.

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0C0C0E` | Page canvas — near-black with a subtle warm bias (matches V2 reference's `COLORS.background`) |
| Card surface (default) | `--bg-card` | `rgba(255,255,255,0.04)` | Default panel fill |
| Card surface (raised) | `--bg-surface` | `rgba(255,255,255,0.08)` | Pills, raised UI chrome |
| Border (default) | `--border` | `rgba(255,255,255,0.10)` | Card and panel strokes |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | Active or featured strokes |
| Primary text | `--text` | `#F1F3F4` | Headlines, body — warm off-white (matches V2) |
| Secondary text | `--text-secondary` | `#9AA0A6` | Captions, sub-lines, metadata (4.7:1 on bg) |
| Muted text | `--text-muted` | `#64748B` | Use only on small chrome that does NOT need AA — large text only |
| **Brand — blue** | `--g-blue` / `--accent-1` | `#4285F4` | Primary lead, source-card #1, side-by-side A, image-hero overline, architecture-stack l1 |
| **Brand — red** | `--g-red` / `--accent-2` / `--accent-warn` | `#EA4335` | Source-card #2, stat-pill #1, architecture-stack l2, hook overline, CTA subscribe pulse |
| **Brand — yellow** | `--g-yellow` / `--accent-3` / `--accent-stat` | `#FBBC04` | Hero stat slam digits, source-card #3, side-by-side B, stat-pill #2, architecture-stack l3 |
| **Brand — green** | `--g-green` / `--accent-4` | `#34A853` | Architecture-stack l4, success / "fixed" / positive reversal |
| Google Cloud cyan | `--g-cyan` | `#00BCD4` | Architecture-stack l5 ONLY, progress-bar gradient end-stop, CTA comment-pill icon |
| Google Blue (deep) | `--g-blue-deep` | `#1A73E8` | V2 reference's `accentStart`/`overline` — available but unused in default scenes |

**Contrast verified (WCAG, body text on `#0C0C0E`):**

- Primary text (`--text` = `#F1F3F4`): ~16.7:1 (AAA)
- Secondary text (`--text-secondary` = `#9AA0A6`): ~5.0:1 (AA)
- Google Blue `#4285F4` on bg: ~5.4:1 (AA safe at 18px+)
- Google Yellow `#FBBC04` on bg: ~12.5:1 (AAA — stat digits + small overlines both pass)
- Google Green `#34A853` on bg: ~6.7:1 (AAA — large text legible)
- Google Red `#EA4335` on bg: ~4.8:1 (AA — chip labels + small captions pass at 18.5px+ / 700)

**For source-card overlines at 18px on translucent backgrounds**, the dim accents fail AA — the template ships lightened variants: `#8AB4F8` (Google blue light) for card-A, `#F6AEA8` (red-text mix) for card-B; card-C uses yellow directly which is AAA at 18px.

**Accent rotation rule:** the Google brand reads cleanly only with the canonical four-color rotation (blue → red → yellow → green). Don't introduce a fifth lead color. Within one video, no two adjacent scenes should share the same lead accent — vary which of the four leads each scene.

## Typography

Pairing rationale: **Inter** for everything visual (matches the V2 Remotion reference's `FONTS.primary`); **JetBrains Mono** for overlines, dates, code references. Two families, no exceptions.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero stat / slam | `--sans` (Inter) | 900 | `letter-spacing: -4px`, glow + drop-shadow |
| Headline | `--sans` (Inter) | 800-900 | `letter-spacing: -1px`, line-height 1.05 |
| Body large | `--sans` (Inter) | 600 | line-height 1.3 |
| Body | `--sans` (Inter) | 500 | line-height 1.4 |
| Section overline | `--mono` (JetBrains Mono) | 700 | UPPERCASE, `letter-spacing: 5-7px`, accent color |
| Stat number | `--sans` (Inter) | 900 | `font-variant-numeric: tabular-nums lining-nums` |
| URL / code | `--mono` (JetBrains Mono) | 600-700 | `letter-spacing: 2px` |

**Type scale (long-form 1920x1080):**

| Role | Size |
|---|---|
| Hero stat (`scene-hook`) | 130px |
| Hero headline (`scene-hook`) | 100px |
| Section headline (image-hero) | 64px |
| Comparison headline (side-by-side, stat-pills) | 56px |
| Synth headline (architecture-stack) | 56px |
| Body large | 26px |
| Body | 22px |
| Section overline (mono) | 26-28px |
| Card title | 28-32px |
| Caption (stable transcribe target) | 38px |
| Stat pill digits | 130px |
| Side-by-side card stats | 84px |

## Layout

**Safe zones:** A persistent Google wordmark watermark sits at `top: -20px; right: 30px` (180×180, the PNG's built-in transparent margin docks it visually to the top edge). A 6px progress bar runs along the bottom in a Google-blue → cyan gradient. Scene padding clears both:

```
PHASE_PAD_TOP    = 80px   (clears wordmark + breathing room)
PHASE_PAD_X      = 100px  (default side padding)
PHASE_PAD_BOTTOM = 80px   (clears progress bar + reading room)
```

`#scene-*-content` MUST use `width:100%; height:100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display:flex; flex-direction:column; box-sizing:border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`. Absolute-positioned content overflows on dynamic text.

**Watermark right-edge offset:** the V2 Remotion reference uses `right: 30, top: -20`. We match exactly so screenshots from this template are visually indistinguishable from V2 frames (apart from the scene art).

**Sub-composition split:** unlike Shorts (which use phase mutex inside one root), long-form splits each scene into its own external HTML file. The root timeline only orchestrates ambient + crossfades — every scene-internal animation lives in its own paused timeline registered on `window.__timelines["scene-<name>"]`. This caps the root timeline at ~30 tweens regardless of total video length.

## Motion Language

| Easing | Use for |
|---|---|
| `expo.out` | Hero word reveal, URL slam, single-element impact |
| `back.out(1.4)` | Card / chip / pill entrances (signature spring) |
| `back.out(1.6)` | Stat pill pop |
| `power3.out` | Headlines and primary text rises |
| `power2.out` | Body / secondary text entrances |
| `power1.in` | Outgoing scene blur+fade (root crossfade) |
| `sine.inOut` | Ambient background breath ONLY |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Stagger:** 80-140ms on body lists; 120ms on multi-card rows; 150ms on architecture-stack layers; 500ms between adjacent stat pills.

**Duration:**
- Hero / slam: 0.6-0.8s
- Headline: 0.5-0.7s
- Card / pill: 0.5-0.6s
- Scene crossfade: 0.4s opacity + 0.5s blur, 1.1s total span

**Direction:** Vertical y-rises dominate (`y: +30 → 0`). Hero slams use `scale: 0.85 → 1.0`. Side-by-side cards use horizontal slides (`x: ±80 → 0`). No rotation. No scale-pop above 1.06. Inline shake is reserved for Shorts-style hero slams; long-form is steadier.

## Surface Detail

- **Cards:** 20-28px radius, `linear-gradient(135deg, <accent>21, <accent>0a)`, `border: 1.5px solid <accent>8c`, `box-shadow: 0 24px 60px rgba(0,0,0,0.55)`. Inner padding 32-40px.
- **Stat pill (hero):** 56px vertical padding, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>80`). Red pill + yellow pill is the default pair (red for problem / count, yellow for hero stat).
- **Source card (photo + meta):** 20px radius, photo at 62% height (object-fit cover), meta block padding 24px 28px, mono overline at 18px in a brighter accent variant (`#8AB4F8` blue-light, `#F6AEA8` red-light, `#FBBC04` yellow direct) for AA at small sizes.
- **Architecture layer:** 14px radius, 8px accent left-strip, 90px tall, padding 0 32px 0 56px, label (mono 18px) → name (sans 32px) → meta (sans 18px secondary). Five layers rotate blue → red → yellow → green → Google cyan (l5).
- **CTA subscribe pill:** rounded (`border-radius: 999px`), Google-red gradient, finite yoyo-pulse glow (`box-shadow: 0 0 0 6px rgba(234,67,53,0.35)`, repeat ≤ 4).
- **Embedded video frame:** 24px radius, 2px bright border, 32px×80px black drop-shadow, wrapper-only animation (NEVER animate `<video>` directly). The placeholder slate inside the wrapper uses a Google-blue → cyan gradient as a brand "loading" cue.
- **Ambient:** 4-radial wash (blue NW + red NE + yellow SE + green SW), 30s sine yoyo, 14 deterministic shapes drift across full duration.
- **Noise overlay:** SVG fractal turbulence at 3.5% opacity, mix-blend-mode overlay — breaks up gradient banding.
- **Top-right watermark:** 180×180 Google wordmark PNG with built-in transparent margin, `top: -20, right: 30`. Drop shadow `0 4px 12px rgba(0,0,0,0.5)` so the multi-color wordmark stays legible on any backdrop.
- **Bottom progress bar:** 6px tall, full-width, `linear-gradient(90deg, var(--g-blue) 0%, var(--g-cyan) 100%)`, glow shadow `0 0 12px rgba(66, 133, 244, 0.55)`.

## Audio Bed (Long-form-specific)

Long-form uses a 3-segment bg-music bed under narration (Shorts forbid bg-music). Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

| Segment | data-start | data-volume | When |
|---|---|---|---|
| Narration | `0` | `1.0` | Full-composition single stem on track 2 |
| `bg-music-hook` | `0` | `0.12` | First 8-12s — energy under the hook |
| `bg-music-body` | `12` | `0.07` | Body — ducked under explanation |
| `bg-music-cta` | last 12-15s | `0.12` | Closing CTA — energy back up |

All bg-music sits on track 3 (sequential, no overlap). SFX go on tracks 4+. **Never** lyrical music under narration. Audio elements get `data-start/duration/track-index` but **NEVER** `class="clip"`.

The V2 reference also uses `bg-music-hook.mp3` / `bg-music-body.mp3` / `bg-music-cta.mp3` as separate stems — we mirror that pattern for parity.

## What NOT to Do

1. **No 5th accent color.** The four Google hues are the brand. Adding cyan / pink / orange as a lead accent breaks the visual identity. The Google Cloud cyan (`--g-cyan`) is an explicit exception reserved for the architecture-stack's 5th layer and the bottom progress-bar gradient end-stop; never use it as a lead accent on scene content.
2. **No light canvas.** This is Google brand cinematic dark stage only. Light "shift" themes (like the Shorts variant's Phase-4 inversion) are NOT part of the long-form variant — the long-form canvas stays `#0C0C0E` end-to-end.
3. **No more than one lead accent per scene.** Each scene picks one of blue/red/yellow/green for its chrome — don't paint a Google-color rainbow within a single scene (except in the architecture-stack and source-cards archetypes, which are explicitly the rotation showcase).
4. **No serif headlines.** Inter only.
5. **No `repeat: -1` anywhere.** All loops must be deterministic — calculate finite repeat counts (e.g. `Math.floor(duration / cycle)`).
6. **No `tl.from()` at position > 5 without `immediateRender: false`.** Long-form-specific gotcha — without the flag, GSAP applies the `from` state at `t=0` of preview and the element flashes invisible.
7. **No `data-duration` on sub-composition wrapper divs.** The sub-comp's internal timeline owns its length.
8. **No `class="clip"` on `<audio>` or `<video>`.** Wrapper div takes the clip role for video; audio takes data-start/duration/track-index without class.
9. **No `position: absolute; top: Npx` on `#scene-*-content`.** Use padding.
10. **No `Math.random()`, `Date.now()`, or network fetches.** Composition logic must be deterministic for the renderer.
11. **No `<br>` in content text.** Use `max-width` for natural wrapping.
12. **No phase mutex (`#phase1`/`#phase2`/`z-index`).** Use sub-composition split — each scene in its own external file.
13. **No hand-redrawn Google logo.** Always use the canonical wordmark PNG from `shared/logos/google-logo.png`. Recoloring or rebuilding the wordmark from primitives is a brand-guidelines violation.
14. **No off-brand top-right watermark.** If the video is comparing Google to a competitor, switch to `templates/long-form/standard/` and put both brands inside scene content — don't paint a non-Google logo into the top-right slot that's reserved for the Google watermark.
