# Long-Form Templates

Reusable HyperFrames project templates for **horizontal YouTube videos** (1920x1080, 30fps, typically 4-15 minutes).

> **Status:** 5 templates available — [`standard/`](./standard/) is the canonical generic baseline; [`anthropic/`](./anthropic/) is the Anthropic dark-stage variant for Claude / Anthropic article-response and deep-dive content; [`claude-code-version/`](./claude-code-version/) is the Claude Code release-update variant; [`hostinger-sponsored/`](./hostinger-sponsored/) is the Hostinger sponsorship cadence (single-file 53.5s tutorial); [`dynamous-slides/`](./dynamous-slides/) is the classic Dynamous deep-navy + blue workshop deck.
> Future variants (`news-explainer`, `tutorial`) build on top of standard.

## Available templates

| Folder | Aesthetic | Best for |
|---|---|---|
| [`standard/`](./standard/) | Dark navy + 4-accent rotation (blue/cyan/purple/green) | Default long-form baseline. 8 scene archetypes (hook, image-hero, side-by-side, stat-pills, source-cards, video-embed, architecture-stack, CTA) + captions sub-comp. Use this for most videos unless a brand-specific variant exists. |
| [`anthropic/`](./anthropic/) | Anthropic dark stage — `#0B0F18` near-black + warm off-white + Claude orange / purple / blue / green rotation | Anthropic / Claude article responses, "how it works" explainers, multi-figure blog-post deep dives. 12 scene archetypes — re-skinned hook / side-by-side / stat-pills / source-cards / video-embed / architecture-stack / CTA + **NEW** `scene-image-3d-reveal` (perspective + rotateY entrance for blog screenshots), `scene-list-cards` (2x2 step-by-step grid), `scene-quote-card` (180px orange quote-mark + marker-sweep underline), `scene-dynamous-midroll` (opt-out community plug), `scene-subscribe-banner` (mid-video pop-in). |
| [`claude-code-version/`](./claude-code-version/) | GitHub-dark + Claude Code accents (cyan-blue/purple/green/orange) | Per-release Claude Code version-update videos. Adds VersionBranding overlay (Anthropic + Claude Code logos top-right + repo URL bottom-right) + scene-stats-opener (3 stat pills + version badge) + scene-feature-cards (configurable 2x2/3x2/stack grid) + scene-terminal (macOS chrome with code block). CTA shows `$ claude update`. Spawn via `/claude-code-version` slash command. |
| [`hostinger-sponsored/`](./hostinger-sponsored/) | Deep navy `#0E0F19` + Hostinger purple `#673DE6` accent (Manrope + JetBrains Mono) | Hostinger sponsorship cadence — tight 53.5s tutorial built around the brief's structure (hook → brand → plan comparison → cart + coupon → setup → workflow → CTA). **Single-file** composition (no sub-compositions), 14 inline scenes, one `cinematic-zoom` shader at the climax (s7→s8). Reusable for any Hostinger-branded creator deal (OpenClaw, Coolify, Plesk add-ons, etc.) — find/replace product name, affiliate URL, coupon code, prices, hero stat. Not a deep tutorial; for that use `standard/`. |
| [`screencap-dubbed/`](./screencap-dubbed/) | Forked from `standard` — same dark navy + 4-accent palette, **corner watermark instead of centered top-banner**, no captions sub-comp | Real screen recording (you on a website, app, or terminal) dubbed with an **AI voice generated from your own transcribed narration**. 3-scene flow: `title` → full-bleed `screencap` (muted `<video>` on track 2) → `cta`. Use when the video centers on real screen interaction AND you don't want your real voice in the published output. Drives a separate workflow (`phase0-ingest-recording` → `phase2-script-from-transcript` → TTS → `phase-sync-check`) — see [`new-long-form-screencap-dubbed.md`](../../.claude/skills/diy-yt-creator/new-long-form-screencap-dubbed.md). |
| [`dynamous-slides/`](./dynamous-slides/) | Classic Dynamous deep-navy `#07090F` + Dynamous Blue `#3B82F6` / Cyan `#0EA5E9` (NO PURPLE) + Montserrat 300/800 weight-contrast + JetBrains Mono mono-bar eyebrows + dual blue/cyan halo backdrop | Dynamous-branded workshops, Cole Medin episodes, AI-coding deep-dives, "scaling X" or "strategies for Y" workshop content. 8 scene archetypes — hook-wordmark (character-stagger hero), headline-accent (Dynamous-Blue sweep), big-stat (counter ramp + gradient text), tension-pivot (300/800 weight contrast), pillars-3 (step-by-step 3-card reveal), list-reveal (6-row enumerated with marker sweeps), quote-card (line-by-line + author chip), cta (logo lockup + debate question). Two opt-in flash transitions (hero pivot + CTA landing). |

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
