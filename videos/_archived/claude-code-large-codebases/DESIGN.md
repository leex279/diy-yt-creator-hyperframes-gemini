# DESIGN — Long-Form Anthropic (Dark Stage)

Visual system for **horizontal long-form videos** (1920x1080, 30fps, 4-10 minutes) in the Anthropic / Claude dark-stage aesthetic. Adapted from the Anthropic Shorts template (`templates/shorts/anthropic/`) and translated to the long-form sub-composition architecture used by `templates/long-form/standard/`.

## Style Prompt

A dark, confident stage built for horizontal long-form. Warm off-white type (`#F5F1EB`) sits on a near-black canvas (`#0B0F18`) with a barely-perceptible blue bias. Claude orange (`#E97458`) leads the accent rotation — it owns the hero stat, the CTA, the primary overline. Purple, blue, and green rotate through body scenes. Motion is spring-driven and percussive: `back.out(1.7)` slams on hero words, `power3.out` rises on headlines, `sine.inOut` ambient breath. Reads like a premium engineering long-form documentary, not an influencer upload.

## Canvas

- Resolution: **1920 x 1080** (horizontal, full HD)
- Frame rate: **30fps**
- Duration target: **4-10 minutes** (template demo is 135s)
- Background: solid `#0B0F18`. Anthropic warm near-black. No full-screen linear gradients (banding under H.264) — use radial highlights only.

## Colors

| Role | Token | Hex | Usage |
|---|---|---|---|
| Background | `--bg` | `#0B0F18` | Page canvas — near-black with blue bias |
| Card surface | `--bg-card` | `#161B26` | Dense secondary panels |
| Surface fill | `--bg-surface` | `rgba(245,241,235,0.08)` | Pills, chip fills |
| Border | `--border` | `rgba(245,241,235,0.12)` | Card/panel strokes |
| Border bright | `--border-bright` | `rgba(245,241,235,0.18)` | Active/featured strokes |
| Primary accent | `--accent-1` | `#E97458` | Claude orange — primary lead, CTA, hero stat |
| Secondary accent | `--accent-2` | `#A78BFA` | Purple — secondary scenes |
| Tertiary accent | `--accent-3` | `#6B9AEF` | Blue — technical / docs scenes |
| Positive accent | `--accent-4` | `#7DD3A6` | Green — success / confirmation |
| Warning | `--accent-warn` | `#D14343` | Red — warnings only, never decorative |
| Stat digit | `--accent-stat` | `#E97458` | Hero stat digits — same orange |
| Primary text | `--text` | `#F5F1EB` | Headlines, body — warm off-white |
| Secondary text | `--text-secondary` | `#9A958D` | Captions, sub-lines (4.7:1 on bg) |
| Muted text | `--text-muted` | `#6B6862` | Large chrome only — do NOT use on body |

**Contrast verified (WCAG, text on `#0B0F18`):**
- Primary text: 14.6:1 (AAA)
- Secondary text: 4.7:1 (AA normal)
- Orange `#E97458` on bg: 6.2:1 (AA normal — safe for 40px+)
- Purple `#A78BFA`: 8.5:1 (AA)
- Blue `#6B9AEF`: 5.4:1 (AA)
- Green `#7DD3A6`: 9.6:1 (AAA)

**Accent rotation rule:** within one video, no two adjacent scenes share the same lead accent. Orange leads (hook + CTA); purple/blue/green rotate through the middle. Use `--accent-warn` (red) ONLY for genuine warnings — never decorative.

## Typography

Two families only — Inter + JetBrains Mono.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| Hero stat / slam | `--sans` (Inter) | 900 | `letter-spacing: -5px`, glow + drop-shadow |
| Headline | `--sans` (Inter) | 800-900 | `letter-spacing: -2px`, line-height 1.0 |
| Body large | `--sans` (Inter) | 600 | line-height 1.3 |
| Body | `--sans` (Inter) | 500 | line-height 1.4 |
| Section overline | `--mono` (JetBrains Mono) | 700 | UPPERCASE, `letter-spacing: 7px`, accent color |
| Stat number | `--sans` (Inter) | 900 | `font-variant-numeric: tabular-nums lining-nums` |
| URL / code | `--mono` (JetBrains Mono) | 600-700 | `letter-spacing: 2px` |

**Type scale (long-form 1920x1080 — adapted from Anthropic Shorts, proportionally larger):**

| Role | Size |
|---|---|
| Hero slam (scene-hook stat) | 200px |
| Scene headline (hook, hook) | 120px |
| Section headline (most scenes) | 56-72px |
| Card primary label (list-cards) | 36px |
| Card descriptor (list-cards) | 24px |
| Quote text | 56px |
| Body large | 32-40px |
| Body | 26-32px |
| Section overline (mono) | 26-28px |
| Stat pill digits | 200px |
| Side-by-side card stats | 84px |
| Caption (transcribe target) | 38px |

## Layout

**Safe zones:** A persistent Anthropic wordmark sits at `top: 30px` (60px tall). A 6px progress bar at bottom. Scene padding clears both:

```
PHASE_PAD_TOP    = 80px   (clears wordmark + breathing room)
PHASE_PAD_X      = 100px  (side padding — wider than Shorts' 60px mobile gutter)
PHASE_PAD_BOTTOM = 80px   (clears progress bar)
```

`#scene-*-content` MUST use `width:100%; height:100%; padding: var(--pad-top) var(--pad-x) var(--pad-bottom); display:flex; flex-direction:column; box-sizing:border-box`. Use padding for content positioning — **NEVER** `position: absolute; top: Npx`.

## Sub-composition split

Unlike Shorts (which use phase mutex in one index.html), long-form splits each scene into its own external HTML file. The root timeline **only** orchestrates:
- Ambient background (radial wash + shape drift + noise overlay)
- Narration audio element
- 3-segment bg-music (optional, commented out by default)
- Per-scene `data-composition-src` wrapper divs
- Scene crossfades via `crossfadeScenes()`

Every scene-internal animation lives in its own paused timeline registered on `window.__timelines["scene-<name>"]`. This caps the root timeline at ~30 tweens regardless of total video length.

Each scene sub-composition file MUST:
- Have `<div data-composition-id="scene-NAME" data-start="0" data-width="1920" data-height="1080">` as root
- Register: `window.__timelines["scene-NAME"] = gsap.timeline({ paused: true });`
- End with `tl.set({}, {}, SCENE_DURATION);` to pin the timeline
- Use placeholder text operators replace per video

## Motion Language

| Easing | Use for |
|---|---|
| `back.out(1.7)` | Hero slam words (signature Anthropic spring) |
| `back.out(1.6)` | Stat pill pop |
| `back.out(1.4)` | Card / chip entrances (slight overshoot) |
| `power3.out` | Headlines and primary text rises |
| `power2.out` | Body / chip / pill entrances |
| `expo.out` | High-impact one-element reveals (URL slam, CTA question) |
| `power1.in` | Outgoing scene blur+fade (root crossfade) |
| `sine.inOut` | Ambient background breath ONLY |

**Avoid:** `elastic`, `bounce` — read toy-like for this brand.

**Duration:**
- Hero / slam: 0.7-0.9s
- Headline: 0.5-0.7s
- Card / pill: 0.5-0.65s
- Scene crossfade: 0.4s opacity + 0.5s blur, 1.1s total

**Direction:** Vertical y-rises dominate (`y: +24-40 → 0`). Hero slams use `scale: 0.85 → 1.0`. Side-by-side cards use horizontal slides (`x: ±80 → 0`). 3D scene uses `rotationY: -25 → 0`. No rotation elsewhere. No scale-pop above 1.06.

**Inline shake** on the impact frame of a slam word — 4 ticks at ±6px, 40ms each. One shake per scene maximum.

## Surface Detail

- **Cards:** 20-24px radius, `linear-gradient(135deg, <accent>18, <accent>04)`, `border: 1.5-2px solid <accent>40`, `box-shadow: 0 14px 36px rgba(0,0,0,0.35)`. Inner padding 28-36px.
- **Stat pill:** 26px radius, accent gradient bg, accent border, accent glow on digit (`text-shadow: 0 0 60px <accent>45`).
- **Source card:** 20px radius, empty div placeholder until operator wires img; card meta 28px sans.
- **Architecture layer:** 14px radius, 8px accent left-strip, 90px tall, padding 0 32px 0 56px.
- **CTA subscribe pill:** `border-radius: 999px`, orange gradient, finite yoyo-pulse glow (repeat ≤ 4).
- **3D image frame:** 20px radius, `border: 2px solid rgba(233,116,88,0.53)`, warm glow `box-shadow: 0 24px 60px rgba(0,0,0,0.55), 0 0 80px rgba(233,116,88,0.22)`.
- **Ambient:** dual-radial wash (orange + purple), 30s sine yoyo, 14 deterministic shapes drift.
- **Noise overlay:** SVG fractal turbulence at 3.5% opacity, mix-blend-mode overlay.

## Audio Bed (Long-form)

Long-form supports a 3-segment bg-music bed under narration (Shorts forbid bg-music). Ships commented out in the bare template. Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

| Segment | data-start | data-volume | When |
|---|---|---|---|
| Narration | `0` | `1.0` | Full composition single stem on track 2 |
| `bg-music-hook` | `0` | `0.12` | First 8s — energy under the hook |
| `bg-music-body` | `8` | `0.07` | Body — ducked under explanation |
| `bg-music-cta` | `118` | `0.12` | Closing CTA — energy back up |

SFX: whoosh-only default (one `cinematic-whoosh` at each scene boundary, commented out in bare template). Wire per video after syncing via `bash scripts/sync-video-sfx.sh videos/<slug>`.

## What NOT to Do

1. **No light canvas.** Dark stage only — `#0B0F18`.
2. **No more than one lead accent per scene.** Orange OR purple OR blue OR green — not all.
3. **No serif headlines.** Inter only.
4. **No `repeat: -1` anywhere.** All loops must be deterministic — calculate finite repeats.
5. **No `tl.from()` at position > 5 without `immediateRender: false`.** Long-form-specific gotcha.
6. **No `data-duration` on sub-composition wrapper divs.** The sub-comp's internal timeline owns its length.
7. **No `class="clip"` on `<audio>` or `<video>`.** Wrapper div takes clip role for embedded video.
8. **No `position: absolute; top: Npx` on `#scene-*-content`.** Use padding.
9. **No `Math.random()`, `Date.now()`, or network fetches.** Compositions must be deterministic.
10. **No `<br>` in content text.** Use `max-width` for natural wrapping.
11. **No phase mutex** (`#phase1`/`z-index` escalation). Use sub-composition split.
12. **No background music on Shorts** (this is long-form — bg-music IS allowed here).
13. **No accent on text below 40px.** Orange/purple/blue/green on small body is a contrast failure.
