# Shorts Templates

Reusable HyperFrames project templates for **vertical YouTube Shorts** (1080x1920, 30fps, typically 24-180s).

> **Status:** 8 templates available — [`standard/`](./standard/) is the canonical brand-neutral baseline; [`editorial/`](./editorial/) is the single-accent editorial variant; [`anthropic/`](./anthropic/), [`archon/`](./archon/), [`claude-code-version/`](./claude-code-version/), [`google/`](./google/), and [`openai/`](./openai/) are brand-specific variants. [`game-map/`](./game-map/) is a **structural variant** (camera-driven hub-and-spoke) that reuses the Anthropic-dark palette.

## Available templates

| Folder | Aesthetic | Best for |
|---|---|---|
| [`standard/`](./standard/) | Dark navy + 4-accent rotation (blue/cyan/purple/green) | **Default pick for any topic.** Brand-neutral, topic-agnostic baseline. 4 phase archetypes (hero hook + stat row + numbered step cards + CTA). Use this for general explainers, how-tos, news, opinion, comparisons, tips. |
| [`editorial/`](./editorial/) | Warm cream `#F4F1EA` + Source Serif 4 italic + single terracotta `#C75A3F` accent | **Editorial-light variant of `standard`** for topics that deserve the mood of a long-form publication — deep-explainer overviews of a spec / standard / open protocol, essay-style "what is X and why" deep-dives, cross-tool comparisons, companion Shorts to long-form on the same topic. Same sub-composition architecture as `standard` (15 scene archetypes), opposite philosophy: one lead accent per scene, no rainbow. Ships a centered mono wordmark + thin rule (chapter heading feel) and a persistent bottom-right source-URL chip. |
| [`dynamous-slides/`](./dynamous-slides/) | Deep-navy `#07090F` + Dynamous Blue `#3B82F6` + Cyan `#0EA5E9` + Montserrat 300/800 + JetBrains Mono | **Vertical companion to `templates/long-form/dynamous-slides/`.** Same Dynamous brand system (deep navy + Dynamous Blue, Montserrat 300/800 weight-contrast signature, JetBrains Mono data, scattered Dynamous-icon shape backdrop, dual blue/cyan halo orbs, flash-flagged crossfade rhythm) restaged for 1080×1920. 7 scene archetypes: `hook-wordmark` → `headline-accent` → `big-stat` → `tension-pivot` → `list-reveal` (6 rows) → `quote-card` → `cta`. Sister template for community drops, workshop recaps, six-strategy explainers — any Short paired with a long-form filmed in the same deck. **Dynamous endcard built in** (flame + 4 community offerings + Link in Description + 10% OFF + dynamous.ai URL + `#cta-question` debate slot). |
| [`anthropic/`](./anthropic/) | Dark stage + Claude orange + warm off-white | Anthropic / Claude product launches, postmortems, dev-tool reveals. Ships with the Anthropic shape backdrop and dated timeline cards (Mar 4 / Mar 26 / Apr 16). |
| [`archon/`](./archon/) | Dark blue + cyan-magenta gradient | Archon workflow showcases. Ships with the Archon brand gradient (cyan→magenta shield). |
| [`claude-code-version/`](./claude-code-version/) | GitHub-dark `#0D1117` + Claude Code accent triad (cyan-blue / purple / green) + orange Subscribe pulse | **Claude Code release-update Shorts** (≤3 min — target 70-130s). Ships with VersionBranding overlay (Anthropic + Claude Code logos top-right + bottom-center URL line), version-slam hero, 3-pill stats opener (features / fixes / improved), numbered highlight cards (`01/02/03`), and a `$ claude update` macOS terminal CTA. Sister of the long-form variant at [`templates/long-form/claude-code-version/`](../long-form/claude-code-version/). |
| [`google/`](./google/) | Cinematic deep-navy + canonical Google four-color rotation (blue/red/yellow/green) + Plus Jakarta Sans + JetBrains Mono | **Google-branded content** (Gemini, Workspace, Cloud, Android, Chrome, Google AI). Ships with the Google logo top-center, accent-tinted `@handle` top-right, 5-dot SETUP→PUBLISH progress rail, and three theme variants (`cinematic` / `spotlight` / `editorial`). Phase archetypes: hero (xl headline) → terminal (CLI moment) → 2x2 chip grid (4-color signals) → optional light "shift" surface + accent-bordered quote + CTA pill. **Dynamous promotion ON by default** — badge + module interstitial + 10% OFF discount bubble all enabled in `video.config.js`. |
| [`openai/`](./openai/) | Monochrome editorial off-black `#0A0A0A` + single ChatGPT-mint `#10A37F` accent + Inter + JetBrains Mono | **OpenAI-branded content** (ChatGPT, GPT, Sora, DALL·E, Codex, research releases). Ships with the ChatGPT spirograph top-center (swap-in OpenAI wordmark included for cross-sub-brand), mint-tinted `@handle` top-right, 5-dot INTRO→CTA single-accent progress rail, and three theme variants (`quiet` / `cinematic` / `editorial`). Aux tints (lavender for Sora / amber for DALL·E / coral for warnings) reserved for whole-video override only. Phase archetypes: hero (xl headline) → terminal (CLI moment) → 2x2 single-accent chip grid → accent-bordered quote + CTA pill. **Dynamous promotion ON by default** (badge + 10% OFF discount bubble + endcard). Forked from the Google variant; reads as `openai.com/research`, not cinematic-launch. |
| [`game-map/`](./game-map/) | Anthropic dark palette + hub-and-spoke world canvas (1 hub + 6 hex spokes) + GSAP camera pan/zoom transitions | **Structural variant — replaces phase-mutex crossfades with a camera that travels across a single giant world canvas.** The viewer first sees a zoomed-out map of the journey (connection lines drawing in 1-by-1), then the camera dives into the hub for the hook and pans node-to-node. Two moves are "chapter breaks" — camera pulls fully out to map view and dives into the next node. Final pull-back becomes the thumbnail-grade completion screen (every node lit with a green ✓). Default 38s, 30-60s typical. Use for any short where the metaphor of a "tour" or "journey through six things" fits the topic — list videos, feature roundups, "X things you missed" formats. |

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
