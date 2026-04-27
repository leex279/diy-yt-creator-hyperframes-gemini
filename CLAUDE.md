# HyperFrames Composition Project

## Skills — USE THESE FIRST

**Always invoke the relevant skill before writing or modifying compositions.** Skills encode framework-specific patterns (e.g., `window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS rules) that are NOT in generic web docs. Skipping them produces broken compositions.

| Skill                      | Command                   | When to use                                                                                       |
| -------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| **hyperframes**            | `/hyperframes`            | Creating or editing HTML compositions, captions, TTS, audio-reactive animation, marker highlights |
| **hyperframes-cli**        | `/hyperframes-cli`        | CLI commands: init, lint, preview, render, transcribe, tts                                        |
| **hyperframes-registry**   | `/hyperframes-registry`   | Installing blocks and components via `hyperframes add`                                            |
| **website-to-hyperframes** | `/website-to-hyperframes` | Capturing a URL and turning it into a video — full website-to-video pipeline                      |
| **gsap**                   | `/gsap`                   | GSAP animations for HyperFrames — tweens, timelines, easing, performance                          |
| **agent-browser**          | `/agent-browser`          | Real Chromium browser — open URL, snapshot DOM, click, fill, screenshot, scrape, QA. Use directly or as a building block inside other skills. |

> **Skills not available?** Ask the user to run `npx hyperframes skills` and restart their
> agent session, or install manually: `npx skills add heygen-com/hyperframes`.

## Commands

This repo holds **multiple videos**. Every CLI command takes a project directory argument — point it at the specific video you're working on (or a template):

```bash
npx hyperframes preview videos/<slug>           # preview in browser (studio editor)
npx hyperframes render  videos/<slug>           # render to MP4
npx hyperframes lint    videos/<slug>           # validate compositions (errors + warnings)
npx hyperframes inspect videos/<slug>           # check rendered layout for overflow
npx hyperframes validate videos/<slug>          # lint + WCAG contrast audit
npx hyperframes lint --verbose videos/<slug>    # include info-level findings
npx hyperframes lint --json    videos/<slug>    # machine-readable output for CI
npx hyperframes docs <topic>                    # reference docs in terminal (no project needed)
```

## Documentation

**For quick reference**, use the local CLI docs command (no network required):

```bash
npx hyperframes docs <topic>
```

Topics: `data-attributes`, `gsap`, `compositions`, `rendering`, `examples`, `troubleshooting`

**For full documentation**, discover pages via the machine-readable index — do NOT guess URLs:

```
https://hyperframes.heygen.com/llms.txt
```

## Project Structure

This is a **multi-video repo**. The root holds shared docs and config; each video is a self-contained HyperFrames project under `videos/`:

```
diy-yt-creator-hyperframes/
├── CLAUDE.md, AGENTS.md, README.md, .gitignore   ← repo-level only
├── skills-lock.json
├── videos/                                       ← one folder per video
│   └── <slug>/                                   ← e.g. claude-connectors-everyday-life
│       ├── index.html                            ← root composition (root timeline)
│       ├── compositions/                         ← sub-compositions via data-composition-src
│       ├── meta.json                             ← { id, name }
│       ├── hyperframes.json                      ← schema/registry/paths
│       ├── DESIGN.md                             ← per-video design system
│       ├── script.txt                            ← narration script
│       ├── audio/                                ← narration.wav, sfx
│       ├── assets/                               ← screenshots, logos
│       └── out/                                  ← rendered MP4 (gitignored)
└── templates/                                    ← copyable starter projects
    ├── shorts/
    │   └── anthropic/                            ← dark-stage Anthropic Shorts (1080x1920)
    └── long-form/                                ← horizontal templates (1920x1080) — TBD
```

## Adding a new video

1. Pick a template (currently `templates/shorts/anthropic/`).
2. Copy it: `cp -r templates/shorts/<style> videos/<slug>` (PowerShell: `Copy-Item -Recurse templates/shorts/<style> videos/<slug>`).
3. Update `videos/<slug>/meta.json` with the real `id` and `name`.
4. Edit `videos/<slug>/index.html` and `DESIGN.md` per the template's README.
5. Drop narration at `videos/<slug>/audio/narration.wav`, wire up the `<audio>` element.
6. Lint, preview, render — always pass the directory: `npx hyperframes lint videos/<slug>`.

Each template's `README.md` has the full spawn instructions specific to that format.

## Linting — ALWAYS RUN AFTER CHANGES

After creating or editing any `.html` composition, **always** run the linter scoped to that video before considering the task complete:

```bash
npx hyperframes lint videos/<slug>
```

Fix all errors before presenting the result. Warnings are informational and usually safe to ignore — but check them: a `duplicate_media_discovery_risk` warning on a template often means a literal `<img …>` syntax was placed inside an HTML comment or a markdown file the linter is scanning.

## Key Rules

1. Every timed element needs `data-start`, `data-duration`, and `data-track-index`
2. Elements with timing **MUST** have `class="clip"` — the framework uses this for visibility control
3. Timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. Videos use `muted` with a separate `<audio>` element for the audio track
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches
