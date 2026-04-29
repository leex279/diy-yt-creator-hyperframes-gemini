# Shorts Templates

Reusable HyperFrames project templates for **vertical YouTube Shorts** (1080x1920, 30fps, typically 24-180s).

> **Status:** 3 templates available — [`standard/`](./standard/) is the canonical brand-neutral baseline; [`anthropic/`](./anthropic/) and [`archon/`](./archon/) are brand-specific variants.

## Available templates

| Folder | Aesthetic | Best for |
|---|---|---|
| [`standard/`](./standard/) | Dark navy + 4-accent rotation (blue/cyan/purple/green) | **Default pick for any topic.** Brand-neutral, topic-agnostic baseline. 4 phase archetypes (hero hook + stat row + numbered step cards + CTA). Use this for general explainers, how-tos, news, opinion, comparisons, tips. |
| [`anthropic/`](./anthropic/) | Dark stage + Claude orange + warm off-white | Anthropic / Claude product launches, postmortems, dev-tool reveals. Ships with the Anthropic shape backdrop and dated timeline cards (Mar 4 / Mar 26 / Apr 16). |
| [`archon/`](./archon/) | Dark blue + cyan-magenta gradient | Archon workflow showcases. Ships with the Archon brand gradient (cyan→magenta shield). |

## What a shorts template looks like

Each template is a fully self-contained HyperFrames project that can be copied into `videos/<slug>/` and edited per video. Layout:

```
templates/shorts/<style-name>/
├── README.md             # spawn-a-new-video instructions
├── DESIGN.md             # color, type, motion system spec
├── meta.json
├── hyperframes.json
├── sfx-cues.txt          # default SFX cue list for sync-video-sfx.sh
├── index.html            # root composition (1080x1920) — phase-mutex inline
├── tokens/               # CSS variable system on :root (palette + spacing + type)
│   └── <name>.css
├── compositions/         # usually empty for shorts (phase mutex lives in index.html)
├── audio/.gitkeep        # narration drops here
└── assets/
    ├── shapes/           # background drift shapes (3 SVGs)
    ├── sfx/.gitkeep      # SFX synced via scripts/sync-video-sfx.sh
    └── <brand>-logo.*    # optional — only on brand-specific templates
```

## How shorts differ from long-form

| Dimension | Shorts (this folder) | Long-form (`templates/long-form/`) |
|---|---|---|
| Resolution | 1080x1920 vertical | 1920x1080 horizontal |
| Duration | 24-180s | 4-15+ minutes |
| Top safe zone | 240px (mobile UI overlay) | 80-120px (no mobile chrome) |
| Background music | None (narration + SFX only) | Yes — low-volume bed under narration |
| Sub-compositions | Usually inline in one `index.html` (phase mutex) | Multiple sub-comps for intro / outro / midroll / chapter cards |
| Captions | Optional | Recommended (use `/hyperframes` captions reference) |
| End screen | Single CTA pill | Subscribe banner + next-video card slot |
| Transitions | Hard cuts + blur crossfades | Add wipes, shader transitions, chapter beats |

## Adding a new shorts template

When the user asks for a new shorts variant:

1. Pick a folder name based on the brand or use case (e.g. `templates/shorts/news-explainer/`, `templates/shorts/tutorial/`).
2. Fork the canonical baseline: `cp -r templates/shorts/standard templates/shorts/<variant>`.
3. Swap the palette in `tokens/<name>.css` to the variant's brand colors.
4. Replace, remove, or add phase archetypes in `index.html` to fit the variant's needs.
5. Update the variant's `README.md` and `DESIGN.md` to document its specifics.
6. Add a row to the "Available templates" table above.
7. Add the matching playbook at `.claude/skills/diy-yt-creator/new-<variant>-short.md` and register it in `.claude/skills/diy-yt-creator/SKILL.md`.
8. Author with `/hyperframes` and `/gsap` skills active.
9. Lint, validate, and inspect: `npx hyperframes lint templates/shorts/<variant>` (must be 0 errors, 0 warnings).

The full new-template checklist (including the spawn dry-run + draft-render gates and shared/lib/ catalog updates) is in the project's [CLAUDE.md](../../CLAUDE.md) under "Building New Templates — Consistent Workflow".
