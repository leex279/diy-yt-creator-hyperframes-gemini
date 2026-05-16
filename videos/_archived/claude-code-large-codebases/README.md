# Long-Form Anthropic Template

Horizontal YouTube long-form (1920x1080, 30fps, 4-15 minutes) in the **Anthropic dark-stage** aesthetic. Claude orange primary (`#E97458`), warm off-white text (`#F5F1EB`), near-black canvas (`#0B0F18`). Built on top of the long-form sub-composition architecture used by `templates/long-form/standard/`.

The full design system (colors, type, motion, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained ~135-second demo composition (`index.html`) showcasing **11 reusable scene archetypes** + a captions sub-composition. Each scene is its own external HTML file with its own paused GSAP timeline.

| File | Pattern | Use for |
|---|---|---|
| `compositions/scene-hook.html` | overline + 120px headline + 200px stat slam + inline shake + sub-line | Scroll-stop opener |
| `compositions/scene-image-3d-reveal.html` | 3D `rotationY` entrance on a framed still image + overline + caption | NEW — cinematic product/screenshot reveals |
| `compositions/scene-list-cards.html` | 4-card 2×2 grid, step-by-step reveal ~5s apart | NEW — feature lists, comparison grids |
| `compositions/scene-quote-card.html` | 180px orange opening quote-mark, 56px italic quote, mono attribution, marker-sweep | NEW — expert quotes, pull-quotes, testimonials |
| `compositions/scene-side-by-side.html` | two accent-striped panels entering from opposite sides | Before vs after; A vs B compare |
| `compositions/scene-stat-pill-row.html` | 3 huge color-rotated stats with mono labels (200px digits) | Receipts; hero numbers |
| `compositions/scene-architecture-stack.html` | 5 accent-striped horizontal layers stacked top-down + headline | "How it all fits together" |
| `compositions/scene-dynamous-midroll.html` | DYNAMOUS wordmark + tagline + URL pill with finite pulse | NEW — mid-video community plug (opt-out per video) |
| `compositions/scene-subscribe-banner.html` | subscribe + Dynamous join banner rows | NEW — 7s CTA banner |
| `compositions/scene-source-cards.html` | 3 photo + overline + title cards in a row, accent-rotated | Source citations |
| `compositions/scene-video-embed.html` | animated wrapper with operator placeholder | Embedded clips, demo footage |
| `compositions/scene-cta.html` | debate question + comment pill + subscribe pulse + next-video card | Closing CTA with finite-pulse glow |
| `compositions/captions.html` | `data-caption-root="true"` — empty until `npx hyperframes transcribe` | Word-level captions |

The root composition (`index.html`) only orchestrates: ambient background (dual-radial orange+purple wash + 14 drifting shapes + noise overlay), narration `<audio>`, optional 3-segment bg-music, and `data-composition-src` wrappers for each scene. Every scene-internal animation lives in its own paused timeline.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-anthropic-longform"

# 2. Copy the template
cp -r templates/long-form/anthropic videos/$SLUG
# PowerShell: Copy-Item -Recurse templates/long-form/anthropic videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-anthropic-longform",
#      "name": "My Anthropic Long-Form Video"
#    }

# 4. Copy your brand logo from the shared library into assets/
cp shared/logos/anthropic-logo-light.svg videos/$SLUG/assets/
# Use *-light variants on this dark-stage template

# 5. Drop narration audio at:
#      videos/$SLUG/audio/narration.wav
#    Then UNCOMMENT the <audio id="narration"> block in index.html
#    and tune data-duration to your narration's actual length.

# 6. Drop your media:
#      videos/$SLUG/assets/screenshots/hero-shot.png          (1920x1080)
#      videos/$SLUG/assets/screenshots/image-reveal.png       (for scene-image-3d-reveal)
#      videos/$SLUG/assets/screenshots/source-1.png           (16:9)
#      videos/$SLUG/assets/screenshots/source-2.png           (16:9)
#      videos/$SLUG/assets/screenshots/source-3.png           (16:9)
#      videos/$SLUG/assets/screenshots/next-video-thumbnail.png
#      videos/$SLUG/assets/clips/demo.mp4                     (optional)

# 7. Edit videos/$SLUG/index.html:
#    - Tune data-start values on each scene wrapper to match your narration
#    - Bump TOTAL_DURATION and #root data-duration to your real total length
#    - Remove scenes you don't need (e.g. scene-dynamous-midroll if not applicable)

# 8. Edit each compositions/scene-*.html with your real copy

# 9. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG
npx hyperframes inspect videos/$SLUG

# 10. Preview
npx hyperframes preview videos/$SLUG

# 11. Render
npx hyperframes render videos/$SLUG --quality high --workers 4 -o videos/$SLUG/out/$SLUG.mp4
```

## Logos — always use local copies

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks). The template's top banner points at `assets/anthropic-logo-light.svg`. When you spawn a video, swap for the matching brand:

```bash
cp shared/logos/<brand>-logo-light.svg videos/<slug>/assets/
# Then edit index.html: <img id="top-banner-logo" src="assets/<brand>-logo-light.svg" ...>
```

**HyperFrames rejects out-of-project paths** — always copy logos into `assets/` rather than referencing `../../shared/logos/...`. Use `*-light.svg` or `*-light.png` variants on this dark-stage template.

## Opt-out of mid-video scenes

`scene-dynamous-midroll.html` and `scene-subscribe-banner.html` are community-plug scenes — remove them from `index.html` when they are not appropriate for the video. Delete the wrapper div and crossfade calls from `index.html`, then retime the remaining scene `data-start` values. Adjust `TOTAL_DURATION` accordingly.

## Customizing per video

CSS variables live in `tokens/anthropic-dark.css`. Override per video by re-declaring in a tighter scope:

```css
/* In videos/<slug>/index.html or a per-video CSS file */
:root {
  --accent-1:    #E97458;   /* Claude orange — swap for a different lead */
  --accent-2:    #A78BFA;   /* purple */
  --accent-3:    #6B9AEF;   /* blue */
  --accent-4:    #7DD3A6;   /* green */
}
```

Per the accent-rotation rule: no two adjacent scenes share the same lead accent. Orange leads hook + CTA; purple/blue/green rotate through the middle.

## Adding more scenes

1. Duplicate a sub-comp file: `cp compositions/scene-source-cards.html compositions/scene-my-new.html`.
2. Change `data-composition-id`, `<template id>`, and `window.__timelines["..."]` key to `scene-my-new`.
3. Edit the GSAP timeline tweens.
4. In `index.html`, add a wrapper div:
   ```html
   <div id="scene-my-new-wrap" class="scene-wrapper"
        data-composition-id="scene-my-new"
        data-composition-src="compositions/scene-my-new.html"
        data-start="<your_time>"
        data-track-index="1"
        data-width="1920"
        data-height="1080"
        style="position:absolute; inset:0; opacity:0; visibility:hidden; z-index:1;"></div>
   ```
5. Add `tl.addLabel("my-new", <your_time>)` and a `crossfadeScenes()` call.
6. Bump `TOTAL_DURATION` and `#root data-duration` if needed.
7. Re-run `npx hyperframes lint videos/<slug>`.

## Adding narration

1. Drop TTS audio at `audio/narration.wav`.
2. Uncomment the `<audio id="narration">` block in `index.html`.
3. Tune `data-start` and `data-duration` to match the file.
4. Sync each scene wrapper's `data-start` to spoken-word landmarks via `npx hyperframes transcribe videos/<slug>`.

## Adding background music

Long-form supports a 3-segment bg-music bed (Shorts forbid it). Pattern in `index.html`'s commented audio block:

| Segment | When | `data-volume` |
|---|---|---|
| `bg-music-hook.mp3` | First 8s — energy under the hook | `0.12` |
| `bg-music-body.mp3` | Body — ducked under narration | `0.07` |
| `bg-music-cta.mp3` | Final ~17s — energy back up for CTA | `0.12` |

All on track 3. Drop files at `audio/bg-music-{hook,body,cta}.mp3` and uncomment their `<audio>` blocks.

**Volume caps are non-negotiable.** Never lyrical music under narration. Full rules at [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## Adding SFX

Sync SFX files first:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

This reads `videos/<slug>/sfx-cues.txt` and copies matching files from `shared/audio/sfx/`. Default cues: `cinematic-whoosh, impact-slam, scale-slam, spring-pop, pop`.

Wire `<audio>` elements in `index.html` (after the bg-music block), track-index 4+, volume cap `0.25`. Full table in [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## Embedded video

`compositions/scene-video-embed.html` ships a placeholder div (no `<video>` element) — the bare template is render-safe. Wire real media per video:

1. Replace the placeholder div with a `<video>` element pointing at `assets/clips/demo.mp4`.
2. Extract the audio separately:
   ```bash
   ffmpeg -i videos/<slug>/assets/clips/demo.mp4 \
     -vn -acodec libmp3lame videos/<slug>/assets/clips/demo-audio.mp3
   ```
3. Add a sibling `<audio>` element (different filename avoids `duplicate_media_discovery_risk`).

See the operator comment inside `scene-video-embed.html` for the exact snippet.

## CTA — engagement question is mandatory

`compositions/scene-cta.html` ships with a placeholder `<REPLACE: debate-sparking question here>` in `#cta-question`. This MUST be replaced per video with a polarizing, binary-answerable question that references a specific claim. See [`.claude/rules/engagement-cta.md`](../../../.claude/rules/engagement-cta.md) for the full rule.

The question MUST agree in all three places: spoken (final line of script), on-screen (`#cta-question`), and in `youtube-description.md`.

## Expected lint state on bare template

The bare template lints **0 errors, 0 warnings**. After wiring real media you may see:

- `audio_src_not_found` — until you uncomment + drop narration/bg-music.
- WCAG contrast warnings — only if you swap to a brighter palette.

## Lib provenance

This template forks `templates/long-form/standard/` and re-skins it with the Anthropic dark-stage aesthetic from `templates/shorts/anthropic/`. The named-style fragment is at [`shared/lib/visual-styles/anthropic-long-form-dark.md`](../../../shared/lib/visual-styles/anthropic-long-form-dark.md). The library token copy is at [`shared/lib/tokens/anthropic-dark-lf.css`](../../../shared/lib/tokens/anthropic-dark-lf.css).

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No light canvas — dark stage only (`#0B0F18`).
- No more than one lead accent per scene.
- No `repeat: -1` anywhere — calculate finite repeats.
- No `tl.from()` at position > 5 without `immediateRender: false` (long-form gotcha).
- No `data-duration` on sub-composition wrapper divs.
- No `class="clip"` on `<audio>` or `<video>` elements.
- No `position: absolute; top: Npx` on scene content — use `padding`.
- No phase mutex — use sub-composition split.
