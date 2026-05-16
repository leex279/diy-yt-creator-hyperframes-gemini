# Game-Map Shorts Template

Vertical YouTube Short (1080x1920, 30fps, 30-60s) with a **camera-driven hub-and-spoke** structure: instead of phase-mutex crossfades between scenes, a single GSAP timeline pans + zooms a camera across one giant world canvas containing 7 sections (1 hub + 6 spokes in a hex ring). The metaphor is a video-game world map — the viewer "travels" between rooms instead of cutting between scenes.

The full design system (camera mechanics, hex geometry, motion, audio, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained 38-second demo composition (`index.html`) that demonstrates the full camera choreography:

| Beat                        | Time      | What's happening                                                                          |
| --------------------------- | --------- | ----------------------------------------------------------------------------------------- |
| Establishing shot           | 0.0-2.5s  | Map view — connection lines draw in 1-by-1 around the hub. Map-overlay headline holds.    |
| Dive into HUB               | 2.5-3.0s  | Camera scale 0.26 → 1.0, lands on the hero hook section (impact-slam pairs with whoosh).  |
| HUB content (00 START)      | 3.0-7.5s  | Hero-slam + overline + accent pill enter. Badge ✓ lights up.                              |
| Direct pan to S1, S2        | 7.5-16.5s | Two adjacent-spoke pans — short whooshes, content fades in/out as camera moves.           |
| **Chapter break** to S3     | 16.5-18s  | Camera zooms OUT to map, holds 0.6s, dives INTO S3. The structural pacing reset.          |
| S3 → S4 → S5 → S6           | 18-34.5s  | Four more sections, four more direct pans. Each section's badge ✓ lights up after visit.  |
| **Pull-back to map**        | 34.5-36s  | Camera retreats to map view (whoosh + scale-slam). Every node has a ✓ now.                |
| Completion screen (held)    | 36-38s    | Map-overlay copy switches to "Six covered. Follow for more." CTA pill fades in. **Frozen.** |

Every camera move is paired with a `cinematic-whoosh`. The dive-in adds `impact-slam`; the pull-back adds `scale-slam`. Per-section content uses the standard Anthropic-dark patterns (overline + headline + body OR hero-slam + accent pill).

## Add Dynamous promotion? (opt-in, ask each new video)

Before you wire content, decide:

> **"Add Dynamous promotion to this Short? (y/N — default no)"**

- **No** (default) — skip this section. Proceed to "Spawn a new video" below.
- **Yes** — open [`videos/_template-wiring-snippet.md`](../../../videos/_template-wiring-snippet.md) and follow Step 0 onward. Wires the persistent badge (artifact 1) + endcard (artifact 2). Optionally also the module interstitial (artifact 3) when the topic matches a curriculum module, and the discount bubble (artifact 4) when the platform is visibly on screen.

Existing videos are NOT retroactively touched. The decision is per video. Record the choice in `videos/<slug>/meta.json` as `"dynamousPromotion": true|false` for later audit.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-game-map-short"

# 2. Copy the template
cp -r templates/shorts/game-map videos/$SLUG
# PowerShell: Copy-Item -Recurse templates/shorts/game-map videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-game-map-short",
#      "name": "My Game Map Short",
#      "dynamousPromotion": false
#    }

# 4. Edit videos/$SLUG/index.html — see "Per-section editing" below

# 5. Drop narration at videos/$SLUG/audio/narration.wav
#    Sync SFX:
bash scripts/sync-video-sfx.sh videos/$SLUG cinematic-whoosh impact-slam scale-slam pop

# 6. Validate
npx hyperframes lint     videos/$SLUG
npx hyperframes validate videos/$SLUG     # WCAG contrast audit
npx hyperframes inspect  videos/$SLUG     # layout overflow check

# 7. Preview
npx hyperframes preview videos/$SLUG

# 8. Render
npx hyperframes render videos/$SLUG -o videos/$SLUG/out/$SLUG.mp4
```

## Per-section editing

Each of the 7 sections is a `<div class="section">` inside `#camera`. To replace placeholder content per video:

| Slot               | Selector                       | What to swap                                          |
| ------------------ | ------------------------------ | ----------------------------------------------------- |
| HUB hero hook      | `#sec-hub .hero-slam`          | The scroll-stop word (160px Inter 900). 6-10 chars max — bigger overflows the 920px content box. |
| HUB overline       | `#sec-hub .overline`           | Mono context line above the hero (e.g., "The Game Map", "What Changed", "Six Updates"). |
| HUB pill           | `#sec-hub .accent-pill`        | Sub-line in mono (e.g., "in 30 seconds", "Claude Code 2.0"). |
| HUB badge          | `#sec-hub .node-num` + `.node-label` | Default `00` / `START`. Usually leave as-is — the badge is structural anchor, not content. |
| Spoke headline     | `#sec-N .headline`             | The section's main beat (72px Inter 800). One sentence, no `<br>`. |
| Spoke overline     | `#sec-N .overline`             | Mono category for that section (e.g., "Discovery", "Mechanism", "Pivot"). |
| Spoke body         | `#sec-N .body`                 | Optional 1-2 sentence receipt below the headline (36px dim). Skip if narration carries everything. |
| Spoke badge        | `#sec-N .node-num` + `.node-label` | `01-06` numbers stay. Replace label with a 1-word topic chip ("HOOK", "STAT", "CTA", etc.). |

**Do NOT** move section coordinates (`top` / `left` on `#sec-*`). The camera transforms in the script tag (`VIEWS.s1`, `VIEWS.s2`, …) are pre-computed from those positions; moving a section without recomputing the matching `VIEWS` entry will silently point the camera at empty space. See [DESIGN.md § Hub-and-Spoke Geometry](./DESIGN.md) for the formula if you need to.

## Camera-move timeline (where to retime per video)

The 8 camera moves live in the `<script>` block. Each is a single `tl.to('#camera', { ...VIEWS.X, duration: D, ease: E }, T)` call. To retime to your narration:

1. Run `npx hyperframes transcribe videos/<slug>` to get word-level timestamps.
2. For each section, find the word in `transcript.json` where the camera should arrive.
3. Replace the hard-coded `T` value (the last argument of `tl.to`) with that word's `start` value.
4. Update each section's micro-beat times (`overline +0.7`, `headline +1.0`, `body +2.0`) to also reference word starts where possible.
5. Update SFX `data-start` attributes in the audio block to match the new camera-move start times.

The default 38s budget is a starting point; trim or expand based on script length. Keep the structure (1 dive-in + 5 direct pans + 1 chapter break + 1 pull-back) regardless of duration.

## Adding more sections

The default is hub + 6 spokes (hexagonal). To go to hub + 8 spokes (octagon):

1. In the CSS, add `#sec-7`, `#sec-8` with positions at angles 22.5° offset (octagon: 22.5°, 67.5°, 112.5°, …). Compute `top` / `left` per section centre.
2. Add `<line>` entries inside `#connections` for hub→S7 and hub→S8.
3. Add S7 / S8 `.section` divs with badges + content (mirror existing structure).
4. Add `VIEWS.s7`, `VIEWS.s8` entries — `tx = 540 - Lx`, `ty = 960 - Ly` at scale 1.
5. Add the camera-move timeline blocks for S7 / S8 (mirror existing pattern).
6. Bump `#root` `data-duration` to cover the longer total, plus add SFX whooshes for the new moves.
7. Update `data-layout-allow-overflow="true"` on the new sections.

To go to hub + 4 spokes (cardinal cross), do the inverse — delete S5 + S6 and adjust the path. Keep the chapter break though; it's the structural rhythm of the template.

## Lib provenance

This template's CSS originates in [`shared/lib/tokens/anthropic-dark.css`](../../../shared/lib/tokens/anthropic-dark.css) (palette + spacing + type — byte-for-byte copy at `tokens/anthropic-dark.css`). The visual style fragment is [`shared/lib/visual-styles/anthropic-dark.md`](../../../shared/lib/visual-styles/anthropic-dark.md) — the game-map template adds a structural pattern on top of that, not a new aesthetic.

Components and effects reused from the lib catalog (annotated in `index.html`):

- `shared/lib/components/ambient-radial/` — viewport-fixed warm wash
- `shared/lib/components/top-banner-wordmark/` — persistent Anthropic mark
- `shared/lib/components/progress-bar/` — slim 6px bottom progress fill

The hub-and-spoke world, camera transform, connection-line draw-in, and per-section badge are NOT in the lib catalog — they're structural to this template. If a future template wants a different camera topology (linear path, 3x3 grid), fork this template rather than promoting parts to the lib (the camera math is geometry-specific).

## Logos — always use real ones

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks). The template's top banner points at the local copy `assets/anthropic-logo-light.svg` (HyperFrames' bundler rejects paths outside the project dir). To swap brand:

```bash
cp shared/logos/<brand>-logo-light.svg videos/<slug>/assets/
```

Then edit the `<img id="top-banner-logo" src="assets/<brand>-logo-light.svg">` line. Use `*-light.svg` variants on this dark-stage template — `*-dark` will be near-invisible. Run `ls shared/logos | grep -i <brand>` to find a logo. **Never** swap the img back to a styled text div when a real logo exists.

## Don'ts

See [`DESIGN.md` § "What NOT to Do"](./DESIGN.md) for the full list. The big ones:

- **No phase-mutex crossfades.** The camera replaces them.
- **No CSS `transform:` on `#camera`.** GSAP owns it.
- **No moving sections without recomputing VIEWS.** Silently breaks the camera.
- **No silent camera moves.** Every tween needs a paired whoosh.
- **No background music on Shorts.** Narration + SFX only.
- **No `<br>` in content text.** Use `max-width`.
- **No more than 8 camera moves per 38-45s short.** Each move costs transit time.
- **No more than 2 chapter-break moves per Short.** They're load-bearing pacing resets, not casual transitions.
