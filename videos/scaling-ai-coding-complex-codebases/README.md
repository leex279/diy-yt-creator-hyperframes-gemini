# templates/long-form/dynamous-slides/

Long-form (1920×1080) HyperFrames template built around the **Dynamous
brand system**: deep-navy stage with Dynamous Blue (`#3B82F6`),
Montserrat for display, JetBrains Mono for data, 300/800 weight
contrast as the signature move.

Adapted from the original **Dynamous Slides** deck (8 scenes / 22 seconds)
into the long-form sub-composition architecture: each scene archetype is
its own paused-timeline file under `compositions/`, and the root
`index.html` orchestrates crossfades, persistent chrome, and ambient
backdrop.

Default total duration: **120 seconds (2 minutes)** with 8 scene
archetypes. Operator extends per video by adding more sub-comp
instances, copying existing scene files, or extending scene durations.

## What's in the box

- **8 scene archetypes** (paused-timeline sub-compositions):
  1. `scene-hook-wordmark` — Character-stagger wordmark hero with flame mark.
  2. `scene-headline-accent` — Two-line headline with Dynamous-Blue sweep.
  3. `scene-big-stat` — Counter ramp with gradient text + receipt label.
  4. `scene-tension-pivot` — 300/800 weight-contrast headline with flash entry.
  5. `scene-pillars-3` — Three-pillar grid, step-by-step paced reveal.
  6. `scene-list-reveal` — 6-row enumerated list with marker sweeps.
  7. `scene-quote-card` — Line-by-line quote reveal with author chip.
  8. `scene-cta` — Logo lockup + debate question + comment/subscribe pills.
- **Persistent background stack**: ambient radial breath, hairline grid,
  shape backdrop with deterministic drift, two blue/cyan halos with
  separate yoyo cadences, SVG film-grain noise, vignette.
- **Crossfade orchestration** between scenes with optional Dynamous-Blue
  flash overlay on flagged boundaries (default: hero pivot + CTA landing).
- **All brand tokens** in `tokens/dynamous.css`.

See [`DESIGN.md`](./DESIGN.md) for the full scene catalog, type scale,
and transition rules.

## Spawn a new video from this template

```bash
# 1. Pick a slug, copy the template
cp -r templates/long-form/dynamous-slides videos/<slug>

# 2. Replace metadata placeholders
#    (PowerShell on Windows; Linux/macOS use sed -i)
$txt = (Get-Content videos/<slug>/meta.json -Raw) `
  -replace 'REPLACE_WITH_VIDEO_SLUG','<slug>' `
  -replace 'REPLACE_WITH_VIDEO_NAME','<Video Title>'
Set-Content videos/<slug>/meta.json $txt

# 3. Drop narration audio
#    videos/<slug>/audio/narration.wav
#    Edit index.html — uncomment the audio bed block, set data-duration.

# 4. Edit each scene's REPLACE: copy + (where relevant) scene timing in
#    videos/<slug>/index.html.
#    The CTA scene's #cta-debate text MUST match the final spoken line
#    of script.txt and the closing paragraph of youtube-description.md
#    (see .claude/rules/engagement-cta.md).

# 5. Validate
npx hyperframes lint    videos/<slug>
npx hyperframes inspect videos/<slug>
npx hyperframes validate videos/<slug>

# 6. Render
npx hyperframes render  videos/<slug> -o videos/<slug>/out/<slug>.mp4
```

Or use the `diy-yt-creator` skill to drive the whole pipeline from a
topic + source materials in one command — see
[`.claude/skills/diy-yt-creator/new-long-form-dynamous-slides.md`](../../../.claude/skills/diy-yt-creator/new-long-form-dynamous-slides.md).

## Wiring the narration audio

Uncomment the audio bed comment block in `index.html` and replace with:

```html
<audio id="narration"
       src="audio/narration.wav"
       data-start="0"
       data-duration="120"
       data-track-index="2"
       data-volume="1"></audio>
```

NEVER add `class="clip"` on `<audio>` elements. Volume cap per
[`.claude/rules/audio-design.md`](../../../.claude/rules/audio-design.md).

## Wiring background music (optional, long-form only)

3-segment bg-music bed keyed by section mood. See the audio block
comments in `index.html` for canonical wiring (hook ≈ first 12s,
body ≈ middle, cta ≈ final 15s). Volume caps per the audio rule.

Shorts (1080×1920) MUST NOT use BG music — this template is long-form
only.

## Adding a scene

1. Pick the archetype from `compositions/` that matches.
2. Either duplicate-and-rename, or just point a new wrapper at the
   existing file with a different `data-composition-id`.
3. Add the wrapper to `index.html` with a unique `id`, the matching
   `data-composition-id`, `data-composition-src`, a `data-start`, and
   `data-track-index="1"`.
4. Add a label and a `crossfadeScenes()` call in the root timeline
   script. Choose `flash: true` only for hero pivots or CTA landings.
5. Lint. Preview. Iterate.

## Lint expectations

Bare template lints clean (0 errors, 0 warnings) and renders a playable
draft MP4. See [`CLAUDE.md` § Building New Templates](../../../CLAUDE.md)
for the full template acceptance checklist.

## Brand provenance

This template was migrated from the **Dynamous brand system** (original
`Dynamous Slides.zip` from `c:\Users\Leex279\Downloads\`). Palette,
type scale, weight-contrast move, and the flame mark all come from
that source. The companion shared-lib visual-style spec lives at
[`shared/lib/visual-styles/dynamous-deep-navy.md`](../../../shared/lib/visual-styles/dynamous-deep-navy.md).
