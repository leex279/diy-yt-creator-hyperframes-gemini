# Long-Form Templates

Reusable HyperFrames project templates for **horizontal YouTube videos** (1920x1080, 30fps, typically 4-15 minutes).

> **Status:** No long-form templates yet. The first one will land here as a sibling to `templates/shorts/anthropic/`.

## What a long-form template will look like

Each template is a fully self-contained HyperFrames project that can be copied into `videos/<slug>/` and edited per video. Expected layout:

```
templates/long-form/<style-name>/
├── README.md            # spawn-a-new-video instructions
├── DESIGN.md            # color, type, motion system spec
├── meta.json
├── hyperframes.json
├── index.html           # root composition (1920x1080)
├── audio/.gitkeep       # narration + BG music drop here
├── assets/.gitkeep      # screenshots, logos, SFX
└── compositions/.gitkeep   # sub-composition HTML files (intro, outro, midroll, etc.)
```

## How long-form differs from shorts

| Dimension | Shorts (`templates/shorts/`) | Long-form (this folder) |
|---|---|---|
| Resolution | 1080x1920 vertical | 1920x1080 horizontal |
| Duration | 60-180s | 4-15+ minutes |
| Top safe zone | 240px (mobile UI overlay) | 80-120px (no mobile chrome) |
| Background music | None (narration + SFX only) | Yes — low-volume bed under narration |
| Sub-compositions | Usually inline in one `index.html` | Multiple sub-comps for intro / outro / midroll / chapter cards |
| Captions | Optional | Recommended (use `/hyperframes` captions reference) |
| End screen | Single CTA pill | Subscribe banner + next-video card slot |
| Transitions | Hard cuts + blur crossfades | Add wipes, shader transitions, chapter beats |

## Adding a new long-form template

When the user asks for a long-form template:

1. Pick a folder name based on aesthetic (e.g. `templates/long-form/anthropic/`, `templates/long-form/swiss-pulse/`).
2. Mirror the structure of `templates/shorts/anthropic/`.
3. Set `data-width="1920" data-height="1080"` on the root composition.
4. Author with `/hyperframes` and `/gsap` skills active.
5. Wire in chapter sub-compositions via `data-composition-src` so episode-style videos can swap chapters per video.
