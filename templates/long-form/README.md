# Long-Form Templates

Reusable HyperFrames project templates for **horizontal YouTube videos** (1920x1080, 30fps, typically 4-15 minutes).

> **Status:** 2 templates available — [`standard/`](./standard/) is the canonical generic baseline; [`claude-code-version/`](./claude-code-version/) is the first variant (Claude Code release-update videos).
> Future variants (`dynamous`, `news-explainer`, `tutorial`) build on top of standard.

## Available templates

| Folder | Aesthetic | Best for |
|---|---|---|
| [`standard/`](./standard/) | Dark navy + 4-accent rotation (blue/cyan/purple/green) | Default long-form baseline. 8 scene archetypes (hook, image-hero, side-by-side, stat-pills, source-cards, video-embed, architecture-stack, CTA) + captions sub-comp. Use this for most videos unless a brand-specific variant exists. |
| [`claude-code-version/`](./claude-code-version/) | GitHub-dark + Claude Code accents (cyan-blue/purple/green/orange) | Per-release Claude Code version-update videos. Adds VersionBranding overlay (Anthropic + Claude Code logos top-right + repo URL bottom-right) + scene-stats-opener (3 stat pills + version badge) + scene-feature-cards (configurable 2x2/3x2/stack grid) + scene-terminal (macOS chrome with code block). CTA shows `$ claude update`. Spawn via `/claude-code-version` slash command. |

## What a long-form template looks like

Each template is a fully self-contained HyperFrames project that can be copied into `videos/<slug>/` and edited per video. Layout:

```
templates/long-form/<style-name>/
├── README.md            # spawn-a-new-video instructions
├── DESIGN.md            # color, type, motion system spec
├── meta.json
├── hyperframes.json
├── sfx-cues.txt         # default SFX cue list for sync-video-sfx.sh
├── index.html           # root composition (1920x1080) — orchestrates only
├── tokens/              # CSS variable system on :root (palette + spacing + type)
│   └── long-form.css
├── compositions/        # one external HTML file per scene archetype
│   ├── scene-*.html     # 8 scene archetypes (each its own paused timeline)
│   └── captions.html    # word-level captions root (data-caption-root="true")
├── audio/.gitkeep       # narration + bg-music drop here
└── assets/
    ├── shapes/          # background drift shapes (3 SVGs)
    ├── screenshots/     # placeholder PNGs replaced per video
    ├── clips/           # operator's MP4 clips
    └── sfx/             # SFX synced via scripts/sync-video-sfx.sh
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

When the user asks for a new long-form variant:

1. Pick a folder name based on the brand or use case (e.g. `templates/long-form/dynamous/`, `templates/long-form/claude-code-version/`).
2. Fork the canonical baseline: `cp -r templates/long-form/standard templates/long-form/<variant>`.
3. Swap the palette in `tokens/long-form.css` to the variant's brand colors.
4. Replace, remove, or add scene archetypes in `compositions/` to fit the variant's needs (e.g. a Claude Code release-update template would swap `scene-architecture-stack` for a feature-card grid).
5. Update the variant's `README.md` and `DESIGN.md` to document its specifics.
6. Add a row to the "Available templates" table above.
7. Author with `/hyperframes` and `/gsap` skills active.
8. Lint and validate the variant: `npx hyperframes lint templates/long-form/<variant>`.
