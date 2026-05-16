# DESIGN — Long-Form Standard (Dark Navy + 4-Accent Rotation)

Visual system for **horizontal long-form videos** (1920x1080, 30fps, typically 4-15 minutes) in the channel's most-used aesthetic. Synthesized from three Remotion reference projects (`GoogleCloudNext2026V2`, `ClaudeSkillsVsAll`, `Gemma4Models`) and translated to HyperFrames (HTML + GSAP).

## Style Prompt

A dark navy stage built for horizontal long-form. Off-white type sits on a deep navy canvas. A 4-tier accent rotation (blue → cyan → purple → green, with orange + yellow held back for warnings and hero stats) drives chrome — borders, badges, glows, single accent words, per-scene tinting. Layout is sub-composition-based: each scene is its own paused GSAP timeline, the root only orchestrates ambient background + crossfades. Motion is restrained but percussive — back.out springs on cards/pills, expo.out on hero reveals, sine.inOut on ambient breath. Reads like a premium engineering documentary, not an influencer upload.

## Canvas

- Resolution: **1920 x 1080** (horizontal, full HD)
- Frame rate: **30fps**
- Duration target: **4-15 minutes** (template demo is 120s)
- Background: solid `#0B0F1A` near-black navy. Radial highlights only — full-screen linear gradients band under H.264.

## Colors

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0B0F1A` | Page canvas — near-black with a deep navy bias |
| Card surface (default) | `--bg-card` | `rgba(255,255,255,0.04)` | Default panel fill |
| Card surface (raised) | `--bg-surface` | `rgba(255,255,255,0.08)` | Pills, raised UI chrome |
| Border (default) | `--border` | `rgba(255,255,255,0.10)` | Card and panel strokes |
| Border (bright) | `--border-bright` | `rgba(255,255,255,0.18)` | Active or featured strokes |
| Primary text | `--text` | `#F1F3F4` | Headlines, body — warm off-white |
| Secondary text | `--text-secondary` | `#9AA0A6` | Captions, sub-lines, metadata (4.7:1 on bg) |
| Muted text | `--text-muted` | `#64748B` | Use only on small chrome that does NOT need AA — large text only |
| Accent — blue | `--accent-1` | `#3B82F6` | Primary lead, source-card #1, side-by-side A |
| Accent — cyan | `--accent-2` | `#06B6D4` | Secondary, source-card #2, video-embed overline |
| Accent — purple | `--accent-3` | `#8B5CF6` | Tertiary, source-card #3, side-by-side B, architecture overline |
| Accent — green | `--accent-4` | `#22C55E` | Success, "fixed", positive reversal |
| Warn — orange | `--accent-warn` | `#F97316` | Hook overline, stat-pill #1, CTA subscribe pulse |
| Stat — yellow | `--accent-stat` | `#FBBC04` | Hero stat slam digits only |

**Contrast verified (WCAG, body text on `#0B0F1A`):**

- Primary text (`--text`): 14.5:1 (AAA)
- Secondary text (`--text-secondary`): 4.7:1 (AA normal)
- `--text-muted` (`#64748B`): ~3.6:1 — **large text only**, never body
- Accent text on dark bg passes AA at ≥18.5px / 700 weight; below that, use brighter shades or `--text` instead

**Accent rotation rule:** within one video, no two adjacent scenes share the same lead accent. Blue, cyan, purple, green rotate; orange leads warnings; yellow is reserved for hero stats only.

## Typography

Pairing rationale: **Inter** for everything visual; **JetBrains Mono** for overlines, dates, code references. Two families, no exceptions.

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

**Safe zones:** A persistent brand wordmark sits at `top: 30px` (60px tall). A 6px progress bar runs along the bottom. Scene padding clears both:

```
PHASE_PAD_TOP    = 80px   (clears wordmark + breathing room)
PHASE_PAD_X      = 100px  (default side padding)
PHASE_PAD_BOTTOM = 80px   (clears progress bar + reading room)
```

`#scene-*-content` MUST use `width:100%; height:100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display:flex; flex-direction:column; box-sizing:border-box`. Padding positions content inward — NEVER `position: absolute; top: Npx`. Absolute-positioned content overflows on dynamic text.

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

- **Cards:** 20-28px radius, `linear-gradient(135deg, <accent>26, <accent>0c)`, `border: 1.5px solid <accent>8c`, `box-shadow: 0 24px 60px rgba(0,0,0,0.55)`. Inner padding 32-40px.
- **Stat pill (hero):** 56px vertical padding, accent gradient bg, accent border, accent glow on the digit (`text-shadow: 0 0 60px <accent>80`).
- **Source card (photo + meta):** 20px radius, photo at 62% height (object-fit cover), meta block padding 24px 28px, mono overline at 18px in a brighter accent variant (`#93C5FD`, `#67E8F9`, `#C4B5FD`) for AA at small sizes.
- **Architecture layer:** 14px radius, 8px accent left-strip, 90px tall, padding 0 32px 0 56px, label (mono 18px) → name (sans 32px) → meta (sans 18px secondary).
- **CTA subscribe pill:** rounded (`border-radius: 999px`), orange gradient, finite yoyo-pulse glow (`box-shadow: 0 0 0 6px rgba(249,115,22,0.35)`, repeat ≤ 4).
- **Embedded video frame:** 24px radius, 2px bright border, 32px×80px black drop-shadow, wrapper-only animation (NEVER animate `<video>` directly).
- **Ambient:** 3-radial wash (blue + purple + cyan), 30s sine yoyo, 14 deterministic shapes drift across full duration.
- **Noise overlay:** SVG fractal turbulence at 3.5% opacity, mix-blend-mode overlay — breaks up gradient banding.

## Audio Bed (Long-form-specific)

Long-form uses a 3-segment bg-music bed under narration (Shorts forbid bg-music). Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

| Segment | data-start | data-volume | When |
|---|---|---|---|
| Narration | `0` | `1.0` | Full-composition single stem on track 2 |
| `bg-music-hook` | `0` | `0.12` | First 8-12s — energy under the hook |
| `bg-music-body` | `12` | `0.07` | Body — ducked under explanation |
| `bg-music-cta` | last 12-15s | `0.12` | Closing CTA — energy back up |

All bg-music sits on track 3 (sequential, no overlap). SFX go on tracks 4+. **Never** lyrical music under narration. Audio elements get `data-start/duration/track-index` but **NEVER** `class="clip"`.

## What NOT to Do

1. **No light canvas.** This is dark navy stage only.
2. **No more than one lead accent per scene.** Each scene picks one of blue/cyan/purple/green for its chrome — don't paint a rainbow.
3. **No serif headlines.** Inter only.
4. **No `repeat: -1` anywhere.** All loops must be deterministic — calculate finite repeat counts (e.g. `Math.floor(duration / cycle)`).
5. **No `tl.from()` at position > 5 without `immediateRender: false`.** Long-form-specific gotcha — without the flag, GSAP applies the `from` state at `t=0` of preview and the element flashes invisible.
6. **No `data-duration` on sub-composition wrapper divs.** The sub-comp's internal timeline owns its length.
7. **No `class="clip"` on `<audio>` or `<video>`.** Wrapper div takes the clip role for video; audio takes data-start/duration/track-index without class.
8. **No `position: absolute; top: Npx` on `#scene-*-content`.** Use padding.
9. **No `Math.random()`, `Date.now()`, or network fetches.** Composition logic must be deterministic for the renderer.
10. **No `<br>` in content text.** Use `max-width` for natural wrapping — `<br>` causes overlap when fonts render slightly wider than estimated.
11. **No phase mutex (`#phase1`/`#phase2`/`z-index`) for long-form.** Use sub-composition split instead — each scene in its own external file.
