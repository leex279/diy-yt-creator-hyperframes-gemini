# Long-Form Standard Template

Horizontal YouTube long-form (1920x1080, 30fps, 4-15 minutes) in the **dark navy + 4-accent rotation** aesthetic. The first generic long-form template — the canonical baseline that future variants (`dynamous`, `news-explainer`, `tutorial`, `claude-code-version`) build on top of.

The full design system (colors, type, motion, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained ~120-second demo composition (`index.html`) showcasing **8 reusable scene archetypes** + a captions sub-composition. Each scene is its own external HTML file with its own paused GSAP timeline.

| File | Pattern | Use for |
|---|---|---|
| `compositions/scene-hook.html` | overline + 100px headline + 130px stat slam + sub-line | Scroll-stop opener |
| `compositions/scene-image-hero.html` | full-bleed photo backdrop + dark gradient overlay + left-aligned content | Photo-led setup; product or location reveals |
| `compositions/scene-side-by-side.html` | two LiquidGlassCard panels (blue vs purple), entering from opposite sides | Before vs after; A vs B compare |
| `compositions/scene-stat-pill-row.html` | 2 huge color-rotated stats (orange + purple) with mono labels | Receipts; "X bugs / Y weeks" hero numbers |
| `compositions/scene-source-cards.html` | 3 photo + overline + title cards in a row, accent-rotated | "Where this came from"; source citations |
| `compositions/scene-video-embed.html` | animated wrapper around `<video>` with mono overline + caption | Embedded clips, demo footage |
| `compositions/scene-architecture-stack.html` | 5 accent-striped horizontal layers stacked top-down + synth headline | "How it all fits together" |
| `compositions/scene-cta.html` | debate question + comment pill + subscribe pulse + next-video card | Closing CTA with finite-pulse glow |
| `compositions/captions.html` | empty captions sub-composition with `data-caption-root="true"` | Word-level captions populated by `npx hyperframes transcribe` |

The root composition (`index.html`) only orchestrates: ambient background (radial wash + 14 drifting shapes + noise overlay), narration `<audio>`, optional 3-segment bg-music, and 8 `data-composition-src` wrappers that pull in each scene file. The root timeline holds only ambient breath + shape drift + scene crossfades — every scene-internal animation lives in its own paused timeline. This caps the root timeline at ~30 tweens regardless of total video length.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="my-new-long-form"

# 2. Copy the template
cp -r templates/long-form/standard videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "my-new-long-form",
#      "name": "My New Long-Form Video"
#    }

# 4. Drop narration audio (TTS or recorded) at:
#      videos/$SLUG/audio/narration.wav
#    Then UNCOMMENT the <audio id="narration"> block in index.html
#    (and tune data-duration to your narration's actual length).

# 5. Drop your media:
#      videos/$SLUG/assets/screenshots/hero-shot.png         (1920x1080)
#      videos/$SLUG/assets/screenshots/source-1.png          (16:9)
#      videos/$SLUG/assets/screenshots/source-2.png          (16:9)
#      videos/$SLUG/assets/screenshots/source-3.png          (16:9)
#      videos/$SLUG/assets/screenshots/next-video-thumbnail.png (16:9)
#      videos/$SLUG/assets/clips/demo.mp4                    (optional)

# 6. Edit videos/$SLUG/index.html:
#    - Tune data-start values on each scene wrapper to match your script's
#      scene boundaries (the 0/12/32/55/70/90/105/115 defaults are demo timing)
#    - Bump #root data-duration to your real total length
#    - Update tl.set({}, {}, TOTAL_DURATION) at the bottom of <script>

# 7. Edit each compositions/scene-*.html with your real copy
#    (the templates ship placeholder text — "YOUR HOOK HEADLINE", etc.)

# 8. Validate
npx hyperframes lint videos/$SLUG
npx hyperframes validate videos/$SLUG     # WCAG contrast audit
npx hyperframes inspect videos/$SLUG      # layout overflow check

# 9. Preview
npx hyperframes preview videos/$SLUG

# 10. Render
npx hyperframes render videos/$SLUG --quality high --workers 4 -o videos/$SLUG/out/long-form.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/long-form/standard videos/$SLUG`.

## Lib provenance

This template is the canonical generic baseline for `templates/long-form/`. Other long-form variants (`dynamous`, `news-explainer`, `tutorial`, `claude-code-version`) should be authored by:

1. Forking this folder (`cp -r templates/long-form/standard templates/long-form/<variant>`).
2. Swapping the palette in `tokens/long-form.css` to the variant's brand colors.
3. Replacing scene archetypes that don't fit the variant (e.g. `claude-code-version` would swap `scene-architecture-stack` for a feature-card grid).

The named-style fragment for this aesthetic is at [`shared/lib/visual-styles/long-form-standard.md`](../../../shared/lib/visual-styles/long-form-standard.md). The library token copy is at [`shared/lib/tokens/long-form-standard.css`](../../../shared/lib/tokens/long-form-standard.css). Future variants pick from these via copy-from per the [`shared/lib/`](../../../shared/lib/) consumption rules.

## Customizing per video

Most styling is driven by CSS variables on `:root` (in `tokens/long-form.css`). Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/long-form.css OR inline in index.html */
:root {
  --accent-1:    #FF6B6B;   /* swap for a different brand primary  */
  --accent-2:    #4ECDC4;
  --accent-3:    #FFE66D;
  --accent-4:    #95E1D3;
  --accent-warn: #F38181;
  --accent-stat: #FCE38A;
}
```

Per-scene accent rotation: change which `--accent-*` a scene uses by editing the scene's CSS — most scenes pin one lead color (`scene-hook` uses `--accent-warn` + `--accent-stat`; `scene-image-hero` uses `--accent-1`; `scene-stat-pill-row` uses `--accent-warn` + `--accent-3`; `scene-architecture-stack` rotates through all four).

## Logos — always use real ones

The repo ships a shared logo library at `shared/logos/` (84 brand wordmarks and icons — see `shared/README.md`). The template's top banner points at the local copy at `assets/anthropic-logo-light.svg` (60px tall). When you spawn a video, swap it for the matching brand:

```bash
# In videos/<slug>/, copy a logo from shared/logos/ into the local assets:
cp shared/logos/<brand>-logo-light.svg videos/<slug>/assets/

# Then edit videos/<slug>/index.html:
#   <img id="top-banner-logo" src="assets/<brand>-logo-light.svg" alt="<Brand>" />
```

Use `*-light.svg` or `*-light.png` variants on this dark-stage template — `*-dark` variants will be near-invisible. Run `ls shared/logos | grep -i <brand>` to find a logo. **HyperFrames rejects out-of-project paths** — always copy logos into `assets/` rather than referencing `../../shared/logos/...`.

## Adding more scenes

The 8 archetypes are starting points — any video can add, remove, or reorder scenes:

1. Duplicate one of the 9 sub-comp files: `cp compositions/scene-source-cards.html compositions/scene-my-new.html`.
2. Inside the new file, change `data-composition-id` (e.g. `scene-my-new`), the inner `<template id="...">` id, and the `window.__timelines["..."]` key.
3. Edit the GSAP timeline tweens for the new scene's content.
4. In `index.html`, add a new wrapper div pointing at the file:
   ```html
   <div id="scene-my-new-wrap" class="scene-wrapper"
        data-composition-id="scene-my-new"
        data-composition-src="compositions/scene-my-new.html"
        data-start="<your_time>"
        data-track-index="1"></div>
   ```
5. Add a CSS rule for `#scene-my-new-wrap` with `z-index: 1; opacity: 0; visibility: hidden;` so the crossfade can fade it in.
6. Add a `tl.addLabel("my-new", <your_time>)` and a `crossfadeScenes()` call to bring it on screen.
7. Bump `TOTAL_DURATION` and `#root data-duration` if needed.
8. Re-run `npx hyperframes lint videos/<slug>` after every change.

## Adding narration

1. Generate or drop your TTS audio at `audio/narration.wav` (or `.mp3`).
2. Uncomment the `<audio id="narration">` block in `index.html` (the audio bed comment block).
3. Tune `data-start` (when narration begins relative to composition 0) and `data-duration` (clip length) to match the file.
4. Sync each scene wrapper's `data-start` to spoken-word landmarks. Use `npx hyperframes transcribe videos/<slug>` for word-level timestamps.

## Adding background music

Long-form supports a 3-segment bg-music bed (Shorts forbid it). The pattern is in `index.html`'s commented audio bed block:

| Segment | When | `data-volume` |
|---|---|---|
| `bg-music-hook.mp3` | First 8-12s, before narration kicks in | `0.12` |
| `bg-music-body.mp3` | Body of the video, under narration | `0.07` |
| `bg-music-cta.mp3` | Final 10-15s, energy back up for CTA | `0.12` |

All on track 3 (sequential, no overlap). Drop the three files at `audio/bg-music-{hook,body,cta}.mp3` and uncomment their `<audio>` blocks in `index.html`.

**Volume caps are non-negotiable** — see [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md). Never lyrical music under narration.

## Adding SFX

Each SFX is a separate `<audio>` element on its own track index, gated by `data-start` / `data-duration`. Sync the files into `assets/sfx/` first:

```bash
bash scripts/sync-video-sfx.sh videos/<slug>
```

This reads `videos/<slug>/sfx-cues.txt` (one cue name per line) and copies the matching files from `shared/audio/sfx/`. The default `sfx-cues.txt` shipped here lists `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop` — edit it to match your needs before running the sync.

Then wire the `<audio>` elements at the bottom of `index.html` (after the bg-music block):

```html
<audio id="sfx-slam"
       src="assets/sfx/scale-slam.mp3"
       data-start="3.20"
       data-duration="0.6"
       data-track-index="4"
       data-volume="0.20"></audio>
```

Hard volume cap: `0.25` per cue (sonic-logo at `0.60` is the only documented exception). Track-index 4+ for SFX (track 2 = narration, track 3 = bg-music). Volume caps and the full per-cue table live in [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## Embedded video — bringing the audio in

`compositions/scene-video-embed.html` ships a `<video>` element pointing at `assets/clips/demo.mp4`. The `<video>` is `muted` (HTML autoplay requirement) — to bring the clip's audio in, extract the audio to a separate file with a different name and add a sibling `<audio>`:

```bash
# Extract the audio from your MP4 (ffmpeg)
ffmpeg -i videos/<slug>/assets/clips/demo.mp4 \
  -vn -acodec libmp3lame videos/<slug>/assets/clips/demo-audio.mp3
```

Then in `compositions/scene-video-embed.html`, after the `<video>` element:

```html
<audio id="vembed-audio"
       src="assets/clips/demo-audio.mp3"
       data-start="0"
       data-duration="14"
       data-track-index="6"
       data-volume="0.6"></audio>
```

Different filename matters: pointing both `<video>` and `<audio>` at the same `.mp4` triggers the `duplicate_media_discovery_risk` lint warning.

## Expected lint warnings on the bare template

Before you wire your media, the bare template lints **0 errors, 0 warnings**. After you spawn a video and start dropping screenshots, you may see:

- `audio_src_not_found` — until you uncomment + drop narration/bg-music files.
- `404 loading assets/clips/demo.mp4` — until you drop a clip (or remove `compositions/scene-video-embed.html` from the wiring if you don't need it).
- WCAG contrast warnings — if you swap to a brighter palette, re-check by running `npx hyperframes validate`.

## Don'ts

See `DESIGN.md` "What NOT to Do" for the full list. The big ones:

- No light canvas — this is dark navy only.
- No `repeat: -1` anywhere (deterministic-only).
- No `tl.from()` at position > 5 without `immediateRender: false` (long-form gotcha).
- No `data-duration` on sub-composition wrapper divs.
- No `class="clip"` on `<audio>` or `<video>` elements.
- No `position: absolute; top: Npx` on scene content — use padding.
- No phase mutex (`#phase1` / `z-index` escalation) — use sub-composition split.
