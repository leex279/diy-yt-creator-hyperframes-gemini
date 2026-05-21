# Long-Form Google Template

Horizontal YouTube long-form (1920x1080, 30fps, 4-15 minutes) in the **Google brand cinematic** aesthetic — near-black `#0C0C0E` canvas with four canonical Google brand hues (blue `#4285F4` / red `#EA4335` / yellow `#FBBC04` / green `#34A853`) rotating through the accent slots, Google wordmark top-right watermark (mirrors the V2 Remotion reference), and four soft Google-color corner glows washing the stage.

The full design system (colors, type, motion, anti-patterns) lives in [DESIGN.md](./DESIGN.md). Read it before editing.

## What this template ships

A self-contained ~120-second demo composition (`index.html`) showcasing **8 reusable scene archetypes** + a captions sub-composition. Each scene is its own external HTML file with its own paused GSAP timeline — same architecture as `templates/long-form/standard/`, only re-painted.

| File | Pattern | Use for |
|---|---|---|
| `compositions/scene-hook.html` | red overline + 100px headline + 130px yellow stat slam + sub-line | Scroll-stop opener (yellow stat reads as the hero number) |
| `compositions/scene-image-hero.html` | full-bleed photo backdrop + dark gradient overlay + left-aligned blue overline | Photo-led setup; product / event / location reveals |
| `compositions/scene-side-by-side.html` | two glass panels (blue "Before" vs yellow "After") entering from opposite sides | A vs B comparison; "before / after" stat pairs |
| `compositions/scene-stat-pill-row.html` | two huge stats (red + yellow) with mono labels | Receipts; "X bugs / Y weeks" hero numbers |
| `compositions/scene-source-cards.html` | three photo + overline + title cards (blue / red / yellow rotation) | "Where this came from"; source citations |
| `compositions/scene-video-embed.html` | animated wrapper around `<video>` with blue overline + caption | Embedded clips, demo footage |
| `compositions/scene-architecture-stack.html` | 5 accent-striped horizontal layers (blue / red / yellow / green / Google cyan) + synth headline | "How it all fits together" |
| `compositions/scene-cta.html` | debate question + comment pill + red subscribe pulse + next-video card | Closing CTA with finite-pulse glow |
| `compositions/captions.html` | empty captions sub-composition with `data-caption-root="true"` | Word-level captions populated by `npx hyperframes transcribe` |

The root composition (`index.html`) only orchestrates: ambient background (four Google-color corner glows + 14 drifting shapes + noise overlay), narration `<audio>`, optional 3-segment bg-music, the **Google wordmark watermark** anchored top-right (180×180, `top:-20, right:30` mirroring the V2 Remotion reference), and 8 `data-composition-src` wrappers that pull in each scene file. The root timeline holds only ambient breath + shape drift + scene crossfades — every scene-internal animation lives in its own paused timeline. This caps the root timeline at ~30 tweens regardless of total video length.

## When to use this template

Pick `templates/long-form/google/` over `templates/long-form/standard/` when the video's editorial subject is the Google brand or one of its products:

- Google Cloud Next / I/O recaps and deep dives
- Gemini, Gemini 3, Gemini App, Gemma model launches
- Google Workspace AI feature explainers
- Android, ChromeOS, Pixel software releases
- TPU / DeepMind / Google AI research walkthroughs
- Any "article response" or "what they announced" coverage of a `google.com` / `cloud.google.com` / `deepmind.google` post

For brand-neutral or non-Google long-form content, use `templates/long-form/standard/` instead — the four-color rotation in this template is explicitly the Google brand, not a generic palette.

## Spawn a new video from this template

From the repo root:

```bash
# 1. Pick a slug (kebab-case, descriptive)
SLUG="google-cloud-next-2026"

# 2. Copy the template
cp -r templates/long-form/google videos/$SLUG

# 3. Update meta.json
#    {
#      "id": "google-cloud-next-2026",
#      "name": "Google Cloud Next 2026 — What Actually Shipped"
#    }

# 4. Drop narration audio (TTS or recorded) at:
#      videos/$SLUG/audio/narration.wav
#    Then UNCOMMENT the <audio id="narration"> block in index.html
#    (and tune data-duration to your narration's actual length).

# 5. Drop your media:
#      videos/$SLUG/assets/screenshots/hero-shot.png            (1920x1080 — keynote frame, product shot)
#      videos/$SLUG/assets/screenshots/source-1.png             (16:9 — Google blog screenshot)
#      videos/$SLUG/assets/screenshots/source-2.png             (16:9 — keynote frame)
#      videos/$SLUG/assets/screenshots/source-3.png             (16:9 — DeepMind paper, TPU diagram, etc.)
#      videos/$SLUG/assets/screenshots/next-video-thumbnail.png (16:9)
#      videos/$SLUG/assets/clips/demo.mp4                       (optional demo clip)
#
#    The default top-right watermark is assets/google-logo.png (full multi-color
#    wordmark). For sub-brand videos drop a different wordmark in assets/ and
#    update <img id="top-banner-logo"> in index.html — see "Sub-brand wordmark
#    swaps" below.

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
npx hyperframes render videos/$SLUG --quality high --workers 4 -o out/$SLUG.mp4
```

PowerShell equivalent for step 2: `Copy-Item -Recurse templates/long-form/google videos/$SLUG`.

## Lib provenance

This template is the **Google-brand variant** of `templates/long-form/standard/`. Forked structure, swapped palette + logo:

- Tokens: forked from `standard/tokens/long-form.css`; `--bg` swapped to `#0C0C0E`, `--accent-1..4` re-mapped to the four Google brand hues, `--accent-warn` re-pointed at Google red.
- Logo: replaced `assets/anthropic-logo-light.svg` with `assets/google-logo.png` (180×180 PNG) + `assets/google-g-logo.png` (alternate). Pulled from `shared/logos/`.
- Scene archetypes: every scene's hardcoded inline-CSS `rgba()` swapped to the Google equivalent (purple → yellow, orange → red, cyan → red, blue → Google blue, dark-bg overlays from `#0B0F1A` → `#0C0C0E`).
- Architecture-stack: 5th layer now uses `--g-cyan` (`#00BCD4`) instead of repeating `--accent-warn` (red), so all 5 layers stay color-distinct.

The named-style fragment for this aesthetic is at [`shared/lib/visual-styles/google-cinematic-long-form.md`](../../../shared/lib/visual-styles/google-cinematic-long-form.md). The library token copy is at [`shared/lib/tokens/google-cinematic-long-form.css`](../../../shared/lib/tokens/google-cinematic-long-form.css). Future Google-family variants (Gemini-only, Workspace-only, Pixel) should fork this template, not the standard.

## Customizing per video

Most styling is driven by CSS variables on `:root` (in `tokens/long-form.css`). Override per video by re-declaring any var in a tighter scope:

```css
/* In videos/<slug>/tokens/long-form.css OR inline in index.html.
   Stay within the four canonical Google brand hues — don't introduce a
   fifth color (the brand reads cleanly only with the four-color rotation). */
:root {
  --accent-1:    #4285F4;   /* swap rotation order per video if needed */
  --accent-2:    #34A853;
  --accent-3:    #FBBC04;
  --accent-4:    #EA4335;
}
```

Per-scene accent rotation: change which `--accent-*` a scene uses by editing the scene's CSS. The default mapping in this template:

- `scene-hook` — `--accent-warn` (red) overline + `--accent-stat` (yellow) hero number
- `scene-image-hero` — `--accent-1` (blue) overline
- `scene-side-by-side` — `.a` blue, `.b` yellow (operator can swap to red/green for "before/after" if the video's semantics need it)
- `scene-stat-pill-row` — `.warn` red + `.gold` yellow
- `scene-source-cards` — `.a` blue, `.b` red, `.c` yellow
- `scene-architecture-stack` — l1 blue / l2 red / l3 yellow / l4 green / l5 Google cyan
- `scene-cta` — red subscribe pulse, cyan comment-pill icon

## Sub-brand wordmark swaps

The default top-right watermark is the **full multi-color Google wordmark**. For sub-brand videos:

| Topic | Recommended top-right logo | Where to find it |
|---|---|---|
| Gemini app / API / Pro / Advanced | Drop a Gemini-only wordmark into `assets/` and point `#top-banner-logo` at it | `shared/logos/` (check `ls shared/logos/ \| grep -i gemini`) |
| Google Cloud / Vertex AI / TPU | Use `assets/google-logo.png` (the full wordmark — Cloud is a sub-brand of Google) | Default |
| Workspace (Docs, Sheets, Gmail) | Same as Cloud — full Google wordmark | Default |
| DeepMind | `shared/logos/deepmind-logo.svg` if available | Check `shared/logos/` |
| Just the **G** mark (cleaner with a busy hero image) | `assets/google-g-logo.png` (already shipped) | Already in template |

When you swap, also bump the alt text on `<img id="top-banner-logo">` to match the sub-brand for accessibility.

## Logos — use the real ones

HyperFrames' bundler / preview server rejects out-of-project paths — never reference `../../shared/logos/...` at runtime. Always copy logos into `videos/<slug>/assets/`:

```bash
# Find the right wordmark
ls shared/logos | grep -i google

# Copy into the per-video assets
cp shared/logos/google-logo.png videos/<slug>/assets/

# Point #top-banner-logo at the local copy
# <img id="top-banner-logo" src="assets/google-logo.png" alt="Google" />
```

The Google wordmark PNG already has its own transparent margin, which is why `top: -20` in the index.html visually docks it to the top edge of the canvas. Don't add more padding — it'll look like the logo is floating away from the frame edge.

## Adding more scenes

The 8 archetypes are starting points — any video can add, remove, or reorder scenes. Follow the same pattern as `templates/long-form/standard/`:

1. Duplicate one of the 9 sub-comp files: `cp compositions/scene-source-cards.html compositions/scene-my-new.html`.
2. Inside the new file, change `data-composition-id` (e.g. `scene-my-new`), the inner `<template id="...">` id, and the `window.__timelines["..."]` key.
3. Edit the GSAP timeline tweens for the new scene's content. Stay within the four Google brand hues.
4. In `index.html`, add a new wrapper div pointing at the file (mirror the existing `#scene-*-wrap` blocks).
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
       data-volume="0.15"></audio>
```

Hard volume cap: `0.25` per cue. Track-index 4+ for SFX (track 2 = narration, track 3 = bg-music). Volume caps and the full per-cue table live in [`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## Expected lint warnings on the bare template

Before you wire your media, the bare template lints **0 errors, 2 warnings** (both inherited from `standard/` — `composition_file_too_large` on `index.html` and `studio_missing_editable_id` on `compositions/captions.html`). Both are informational, not blockers.

After you spawn a video and start dropping screenshots, you may see:

- `audio_src_not_found` — until you uncomment + drop narration/bg-music files.
- `404 loading assets/clips/demo.mp4` — until you drop a clip (or remove `compositions/scene-video-embed.html` from the wiring if you don't need it).
- WCAG contrast warnings — if you swap to a brighter palette or use accent text below the AA threshold size.

## Don'ts (Google-specific)

See `DESIGN.md` "What NOT to Do" for the full list. The Google-template-specific ones:

- **Do NOT introduce a 5th accent color.** The four Google hues are the brand. Adding purple / orange / cyan-as-primary breaks the visual identity. The Google Cloud cyan (`--g-cyan`) is an explicit exception ONLY for the 5th architecture-stack layer; don't use it elsewhere as a lead accent.
- **Do NOT replace the Google wordmark with an off-brand alternative.** If the video is Google-adjacent (e.g., "Anthropic vs Google" comparison), use `templates/long-form/standard/` and a Google-Anthropic side-by-side scene instead.
- **Do NOT swap to Plus Jakarta Sans / Geist / any non-Inter sans.** The V2 reference uses Inter; we match. Plus Jakarta is documented in the **Shorts** Google template for the cinematic-vertical look, but long-form stays on Inter.
- **Do NOT rebuild the Google logo from primitives.** Always use the canonical wordmark PNG from `shared/logos/`. Recoloring or hand-redrawing the wordmark is a brand-guidelines violation.
- All the `standard/` template's don'ts still apply: no light canvas, no `repeat: -1`, no `tl.from()` at position > 5 without `immediateRender: false`, no `data-duration` on sub-composition wrapper divs, no `class="clip"` on `<audio>` or `<video>`, no `position: absolute; top: Npx` on scene content (use padding), no phase mutex.
