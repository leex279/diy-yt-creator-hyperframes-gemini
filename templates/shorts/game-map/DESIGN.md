# DESIGN — Game-Map Shorts (Camera-Driven Hub-and-Spoke)

Visual system for **YouTube Shorts** (1080x1920, 30fps, 30-60s) using a **camera-driven hub-and-spoke** structure: instead of phase-mutex crossfades, a single GSAP-tweened camera pans + zooms across one giant world canvas containing 7 sections (1 hub + 6 spokes in a hexagonal ring). The metaphor is a video-game world map — viewer "travels" between rooms instead of cutting between scenes.

This template **inherits the Anthropic-dark palette + typography + motion easing** verbatim — only the **structural pattern** is new. Pair this DESIGN.md with [`shared/lib/visual-styles/anthropic-dark.md`](../../../shared/lib/visual-styles/anthropic-dark.md) for the palette / type / easing tables.

## Style Prompt

A dark-stage Anthropic short rebuilt as a navigable map. The viewer first sees a zoomed-out map of the journey — six labeled nodes connected to a central hub by hand-drawn lines that draw in one at a time. The camera dives into the hub (impact-slam) for the hook, then pans node-to-node along the ring. Each node holds one beat of the story; every visited node lights up with a green check. Two of the moves are bigger "chapter breaks" — the camera pulls all the way out to the map view and dives into the next node, paired with a heavier whoosh. After the sixth node, the camera pulls back to the completion screen — every check lit, the headline returns, a CTA pill subordinate to the map. That last frame is the thumbnail.

## Canvas

- **Viewport**: 1080 x 1920 (vertical Shorts).
- **World** (the camera's canvas): 4080 x 4518. Sections are placed absolute inside `#camera`.
- **Section size**: 1080 x 1920 each (matches viewport so a section view is 1:1 with the canvas).
- **Frame rate**: 30 fps.
- **Duration target**: 30-60s. Default in this template is **38s** (2.5s establishing + 4-4.5s per section + 1.5s pull-back + 2s final hold).
- **Background**: solid `#0B0F18` per `tokens/anthropic-dark.css`.

## Hub-and-Spoke Geometry (HARD: do not move sections)

The 7 sections sit at fixed coordinates in `#camera`-local pixels. Spokes are at hex angles 60°, 120°, 180°, 240°, 300°, 0° around hub at world origin, radius **R = 1500**:

| Section | Camera-local centre (Lx, Ly) | Section `top, left`     |
| ------- | ---------------------------- | ----------------------- |
| HUB     | (2040, 2259)                 | top: 1299, left: 1500   |
| S1 NW   | (1290,  960)                 | top:    0, left:  750   |
| S2 NE   | (2790,  960)                 | top:    0, left: 2250   |
| S3 E    | (3540, 2259)                 | top: 1299, left: 3000   |
| S4 SE   | (2790, 3558)                 | top: 2598, left: 2250   |
| S5 SW   | (1290, 3558)                 | top: 2598, left:  750   |
| S6 W    | ( 540, 2259)                 | top: 1299, left:    0   |

**Why this matters:** every camera transform in the script tag is derived from these centres via the rule below. Moving a section without recomputing its `VIEWS` entry will desync the camera so a "look at S3" tween points at the wrong spot. If you change R or section count, **regenerate VIEWS** by hand from the formula:

```
tx = 540 - Lx * scale
ty = 960 - Ly * scale
```

For section view (`scale = 1`), `tx = 540 - Lx`, `ty = 960 - Ly`. For map view (`scale = 0.26` centred on world middle 2040,2259), `tx = 10`, `ty = 373`.

## Camera Choreography (the structural signature of this template)

Replaces phase-crossfade transitions with a single GSAP timeline that animates `#camera`'s `x`, `y`, and `scale`. Three camera-move types, each with its own duration + easing + audio cue:

| Move type            | Duration | Easing            | SFX cue                          | Volume | Used for                                      |
| -------------------- | -------- | ----------------- | -------------------------------- | ------ | --------------------------------------------- |
| **Dive-in**          | 0.5s     | `power2.inOut`    | `cinematic-whoosh` + `impact-slam` | 0.13 + 0.15 | Map → first section (after establishing shot) |
| **Direct pan**       | 0.5s     | `power2.inOut`    | `cinematic-whoosh` (soft)        | 0.08   | Adjacent section to adjacent (5x in default)  |
| **Chapter break**    | 1.5s total (0.6s out + 0.9s in) | `power2.in` then `power2.out` | `cinematic-whoosh` (long) | 0.13   | Mid-video pacing reset (1x in default)        |
| **Pull-back**        | 1.5s     | `power2.inOut`    | `cinematic-whoosh` + `scale-slam`  | 0.13 + 0.13 | Final frame — completion screen                |

The default 38s short uses: **1 dive-in + 5 direct pans + 1 chapter break + 1 pull-back = 8 camera moves**. Each is paired with audio. Without the audio, camera moves feel ungrounded — keep the cues in sync (`audio-design.md` "SFX must be aligned to their visual triggers": `data-start` of every whoosh equals the camera tween's `at` time).

## What the viewer sees per beat

| Time      | Camera state            | What's visible                                                                          |
| --------- | ----------------------- | --------------------------------------------------------------------------------------- |
| 0.0-2.5s  | Map view (scale 0.26)   | Full map. Connection lines draw in 1-by-1 (0.25s apart). Map-overlay headline holds.    |
| 2.5-3.0s  | Diving to HUB           | Camera transition. Map overlay fades out.                                               |
| 3.0-7.5s  | HUB section view        | Hero-slam + overline + accent pill enter (anthropic motion).                            |
| 7.5-12.5s | S1 → S2 (direct pans)   | Each section shows overline / headline / body. Visited node lights up with a ✓.        |
| 16.5-18s  | Chapter pull-out + dive | Camera retreats to map, holds 0.6s, dives into S3.                                      |
| 18-31.5s  | S3 → S6 (direct pans)   | Continues per-section beats. ✓ accumulates after each visit.                            |
| 34.5-36s  | Pull-back to map        | Camera retreats to map view. Every node now has a ✓.                                    |
| 36-38s    | Completion screen       | Map-overlay copy switches to "Six covered. Follow for more." CTA pill fades in. **Held still.** |

## Per-section content layout (every section uses the same anchor structure)

```
y=  0-240px   : top safe-zone (top banner sits here at viewport level)
y=280-580px   : SECTION NODE BADGE (300x300 round badge with 01-06 + label)
                — always visible at all camera depths
                — connects to hub via SVG line in map view
y=620-1680px  : SECTION CONTENT (overline + headline + body OR hero-slam + pill)
                — opacity 0 at default; fades in when camera arrives
y=1680-1920px : bottom safe-zone (progress bar lives at viewport level)
```

The badge is the **anchor of the section** — it's what the viewer sees in map view (where content is too small to read) and the chapter-chip at section view. **Do not remove the badge** when authoring per video; it's load-bearing for the map metaphor.

The content area uses the standard anthropic patterns:

- **HUB**: hero-slam (160px) + overline + accent pill — the scroll-stop hook
- **Spokes (S1-S6)**: overline (36px mono) + headline (72px Inter 800) + body (36px Inter 500, dim)

Per-video editing replaces the placeholder copy. The structure is fixed.

## Colors

Inherits [`shared/lib/tokens/anthropic-dark.css`](../../../shared/lib/tokens/anthropic-dark.css). Key role mapping for this template:

| Element                        | Token         | Notes                                                  |
| ------------------------------ | ------------- | ------------------------------------------------------ |
| HUB badge ring + glow          | `--orange`    | One-of-one — only orange node, signals "start"        |
| S1, S4 badge ring              | `--purple`    | Spoke colour rotation 1                                |
| S2, S5 badge ring              | `--blue`      | Spoke colour rotation 2                                |
| S3, S6 badge ring              | `--green`     | Spoke colour rotation 3 (also the "chapter" colour)    |
| Connection lines               | `rgba(245,241,235,0.18)` | Soft white at low alpha; reads as map ink |
| Visited check (✓)              | `--green` on `#0B0F18` | Always green regardless of node colour     |
| Map-overlay headline           | `--text` + `--orange` overline | Same hierarchy as section overlines    |
| Final-frame CTA arrow          | `--orange`    | Single Anthropic-orange tick                           |

**Accent rotation rule:** within the spokes, no two adjacent (in path order) share the same accent. Default order Hub→S1→S2→S3→S4→S5→S6 = orange / purple / blue / green / purple / blue / green — passes the rule.

## Typography

Inherits Anthropic-dark type scale, with one structural addition:

| New role               | Family    | Weight | Size  | Treatment                          |
| ---------------------- | --------- | ------ | ----- | ---------------------------------- |
| Section node number    | Inter     | 900    | 110px | letter-spacing -3px (130px on HUB) |
| Section node label     | JetBrains | 700    | 28px  | UPPERCASE, letter-spacing 4px      |
| Map-overlay headline   | Inter     | 900    | 88px  | letter-spacing -2px, line-height 0.95 |
| Map-overlay sub        | Inter     | 500    | 36px  | dim text, line-height 1.25         |

All other type roles (hero-slam, headline, body, overline, accent-pill) use the standard Anthropic-dark sizes — see [`shared/lib/visual-styles/anthropic-dark.md`](../../../shared/lib/visual-styles/anthropic-dark.md).

## Motion Language

Inherits Anthropic-dark easing palette (`back.out(1.7)`, `power2.out`, `power3.out`, `expo.out`, `sine.inOut`). Adds the **camera-tween easing**:

- `power2.inOut` for direct pans + pull-back (smooth deceleration both ends)
- `power2.in` then `power2.out` chained for chapter breaks (accelerate out, decelerate in)
- Connection-line draw-in: `power2.inOut`, 0.5s per line, 0.25s stagger

**Per-section beats** still follow the visual-pacing-5s rule:

- HUB: hero-slam at +0.4s, accent-pill at +1.6s, badge-check at +3.8s — three beats inside 4.5s
- Spokes: overline +0.2, headline +0.5, body +1.5, badge-check +3.4 — four beats inside 4s

**Avoid:**

- Any tween on `#camera`'s rotation. Rotation breaks the "the world is fixed; you're moving the lens" metaphor.
- Camera scale extremes (< 0.2 or > 1.0). 0.26 is the lowest readable map view; 1.0 is section-fit. Going further introduces glyph aliasing and viewer-sickness.
- More than 8 camera moves in a 38s short. Each move costs ~0.5-1.5s of "transit time" that doesn't carry information; budget accordingly.

## Surface Detail

- **Section node badge**: 300x300 (HUB: 380x380), `border-radius: 50%`, `border: 4px solid <accent>`, `background: rgba(11,15,24,0.78)` with `backdrop-filter: blur(6px)`, glow shadow `0 0 60px <accent>33` (HUB: 80px / 0.45 alpha).
- **Section tile**: `inset: 60px; border-radius: 60px;` filled with `radial-gradient(circle at 50% 40%, <accent>14-16, transparent 60%)` — the soft accent wash that reads as "you're inside this room" at section view.
- **Connection lines**: `stroke-width: 6`, `stroke-linecap: round`, `pathLength=1` + `stroke-dasharray=1` + `stroke-dashoffset=1` so GSAP can animate `strokeDashoffset` from 1 to 0 to draw any line regardless of length.
- **Visited check**: 56x56 circle, `background: #0B0F18`, `color: var(--green)`, `border: 3px solid var(--green)`, top-right inside the badge (NOT overlapping the ring — that breaks WCAG AA contrast).
- **Map overlay**: viewport-fixed div under the top banner; copy swaps from "Tap → to start" (establishing shot) to "Six covered. Follow for more." (completion screen) via `tl.set('#map-overlay-sub', { innerText: ... })`.
- **Final-frame CTA pill**: viewport-fixed near bottom; subordinate to the map (per [`shorts-thumbnail-frames.md`](../../../.claude/rules/shorts-thumbnail-frames.md) — topic dominates, CTA is small).
- **Shape backdrop**: per-section, 8 shapes scattered inside each `.section-shapes` container (NOT spanning the full world). Total 56 shapes ambient. No drift / yoyo on shapes — at this resolution, a still field reads as ambient texture; movement competes with the camera.

## Audio / SFX Cues

Canonical rules: [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Cue files live in [`shared/audio/sfx/`](../../../shared/audio/) (sync into a video via [`scripts/sync-video-sfx.sh`](../../../scripts/sync-video-sfx.sh)).

Narration is one stem. SFX layer as separate `<audio>` elements at low volume.

**DEFAULT — every camera move gets a whoosh.** This is intentional and **differs from the anthropic template's "transition whooshes only" default**: the game-map metaphor depends on camera moves *feeling like* physical journey beats, and a silent camera move reads as ungrounded sliding. The default short has 8 whooshes over 38s — one per ~4.7s — calibrated by move size:

| Cue                | Use on                                         | Default `data-volume` | Default state |
| ------------------ | ---------------------------------------------- | --------------------- | ------------- |
| `cinematic-whoosh` | Direct pan (5x in default)                     | 0.08                  | **ON**        |
| `cinematic-whoosh` | Chapter break (1x) + dive-in (1x) + pullback (1x) | 0.13              | **ON**        |
| `impact-slam`      | Dive-in landing (paired with whoosh)           | 0.15                  | **ON**        |
| `scale-slam`       | Pull-back landing (paired with whoosh)         | 0.13                  | **ON**        |
| `pop`              | Optional badge-check pop on each `.node-check` reveal | 0.08            | OFF — opt-in  |
| `sonic-logo`       | Composition start (optional brand stinger)     | 0.45                  | OFF — opt-in  |

**Whoosh-to-camera-move alignment rule (HARD).** Every whoosh's `data-start` MUST equal the camera tween's `at` time (NOT `at - 0.4` like the anthropic shape-reposition rule — this template doesn't reposition shapes, so the offset doesn't apply). Drift > 0.15s is a defect per `audio-design.md`.

**Hard cap:** never exceed `0.25` on a single per-cue SFX (sonic-logo at `0.45` is the only exception).

## What NOT to Do

1. **No phase-mutex crossfades.** The whole point of this template is that the camera replaces the crossfade. Adding a `phase-crossfade` block back in defeats the metaphor.
2. **No camera rotation.** The world is fixed; rotation breaks the "moving the lens" feel.
3. **No CSS `transform` on `#camera`.** GSAP's `x`/`y`/`scale` and CSS `transform` conflict (HyperFrames lint flags it). Use `tl.set('#camera', { x, y, scale }, 0)` for the initial state.
4. **No moving sections without recomputing `VIEWS`.** The camera transforms are derived from section centres; desyncing them silently points the camera at the wrong spot.
5. **No silent camera moves.** Every camera tween needs a paired audio cue. A move without sound reads as a glitch.
6. **No overlapping content during a camera tween.** Fade outgoing section's content out BEFORE the move (or during the first ~30% of the move). Stale content surviving into the new section creates double-vision artifacts.
7. **No background music on Shorts.** Inherited from the anthropic template — narration + SFX only.
8. **No more than 8 camera moves in a 38-45s short.** Each move costs transit time. Budget moves like you'd budget cuts.
9. **No drift on shape backdrop.** Camera motion is the foreground motion budget; ambient drift competes for attention.
10. **No `<br>` in content text.** Use `max-width` for wrapping (Anthropic rule, applies here too).
11. **No accent below 40px.** Anthropic rule, applies here too — orange/purple/blue/green don't carry contrast for body text.
12. **No tweening of the connection lines after they've drawn in.** They are stable map infrastructure. Once drawn, they hold position until the composition ends.
13. **No `position: absolute; top: Npx` on `.section-content`.** Use the existing flex column layout — absolute positioning overflows when content text re-wraps.
14. **No more than 2 chapter-break (zoom-out-zoom-in) moves per Short.** Each is a strong pacing reset; using them more frequently makes the camera feel chaotic instead of intentional.

## Final-frame guarantee

Per [`shorts-thumbnail-frames.md`](../../../.claude/rules/shorts-thumbnail-frames.md), the last 1.5-2.0s MUST hold a thumbnail-grade still. This template ships that out of the box: at t=36-38s the camera is parked at map view, every node has a green ✓, the map-overlay returns with completion copy, and the CTA pill is in. The viewer pausing at the final frame sees:

1. **Topic** (map-overlay headline, 88px) — dominant, what the video was about
2. **Visual anchor** (the lit-up map with all 6 nodes + hub) — the journey completed
3. **Brand chrome** (top banner: Anthropic wordmark) — channel attribution
4. **Outcome receipt** (map-overlay sub: "Six covered.") — what they got
5. **CTA pill** (subordinate, lower) — Follow for more →

All five required elements per the rule. Do NOT remove the pull-back move when authoring per video; without it, the Short loses its loop-grade thumbnail.
