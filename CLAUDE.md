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
npx hyperframes render  videos/<slug> -o out/<slug>.mp4                # render to MP4 — output goes to repo-root out/, named after the slug
npx hyperframes lint    videos/<slug>           # validate compositions (errors + warnings)
npx hyperframes inspect videos/<slug>           # check rendered layout for overflow
npx hyperframes validate videos/<slug>          # lint + WCAG contrast audit
npx hyperframes lint --verbose videos/<slug>    # include info-level findings
npx hyperframes lint --json    videos/<slug>    # machine-readable output for CI
npx hyperframes docs <topic>                    # reference docs in terminal (no project needed)
```

### Per-creator env configs (TTS scripts)

The Python TTS scripts (`scripts/elevenlabs-tts.py`, `scripts/generate-sfx-library.py`) default to `<repo-root>/.env` but accept `--env-file PATH` to point at a per-creator config (e.g. `.env.cole`). Relative paths resolve against the repo root.

```bash
python scripts/elevenlabs-tts.py videos/<slug> --shorts --env-file .env.cole
python scripts/generate-sfx-library.py --env-file .env.cole
```

`.env.*` is gitignored (with `.env.example` carved out) so per-creator configs stay local. This does NOT affect `npx hyperframes tts` — that path still reads `.env` only; the diy-yt-creator playbooks all invoke the Python scripts directly, so the flag is the supported route for per-video voice switching.

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

**For the registry catalog** (every block + component installable via `hyperframes add`), see [`.claude/rules/registry-blocks-catalog.md`](./.claude/rules/registry-blocks-catalog.md). Read it before picking visuals for a new video — it lists the full VFX / html-in-canvas family (`vfx-iphone-device`, `vfx-shatter`, `vfx-portal`, …), shader transitions, social-media overlays, and animation blocks so you don't hand-roll something the registry already provides.

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
├── shared/                                       ← repo-shared assets
│   ├── logos/                                    ← brand wordmarks (84 files)
│   ├── audio/                                    ← shared SFX library — copy-from
│   └── lib/                                      ← reusable cards, components, effects, palettes — copy-from
├── templates/                                    ← copyable starter projects
│   ├── shorts/                                   ← vertical 1080x1920 (Shorts)
│   │   ├── anthropic/                            ← dark-stage Anthropic aesthetic
│   │   └── archon/                               ← dark-blue / cyan-magenta Archon aesthetic
│   └── long-form/                                ← horizontal 1920x1080 (long-form)
│       └── standard/                             ← canonical baseline (dark navy + 4-accent rotation)
└── scripts/                                      ← repo helpers (sync-shared-* hooks)
```

The shared library at `shared/lib/` is **copy-from**, not reference-from. HyperFrames' bundler/preview server rejects paths outside the project directory — see [`shared/lib/README.md`](shared/lib/README.md) for the consumption rules and [`shared/lib/MANIFEST.md`](shared/lib/MANIFEST.md) for the catalog.

## Adding a new video

1. Pick a template by format and aesthetic:
   - **Shorts (vertical, 1080x1920, 24-60s)**: `templates/shorts/anthropic/` or `templates/shorts/archon/`
   - **Long-form (horizontal, 1920x1080, 4-15min)**: `templates/long-form/standard/`
2. Copy it: `cp -r templates/<format>/<style> videos/<slug>` (PowerShell: `Copy-Item -Recurse templates/<format>/<style> videos/<slug>`).
3. Update `videos/<slug>/meta.json` with the real `id` and `name`.
4. Edit `videos/<slug>/index.html` (and any `compositions/scene-*.html` for long-form) per the template's README.
5. Drop narration at `videos/<slug>/audio/narration.wav`, wire up the `<audio>` element.
6. Lint, preview, render — always pass the directory: `npx hyperframes lint videos/<slug>`.

Each template's `README.md` has the full spawn instructions specific to that format. The `/diy-yt-creator` skill family (`new-anthropic-short`, `new-archon-short`, `new-long-form-standard`) automates the whole flow from a topic prompt — see `.claude/skills/diy-yt-creator/SKILL.md`.

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
5. Sub-compositions use `data-composition-src="compositions/file.html"` to reference other HTML files. **Wiring rules are strict — see [`.claude/rules/sub-composition-wiring.md`](.claude/rules/sub-composition-wiring.md).** The parent's `data-composition-id` MUST equal the child file's internal `data-composition-id`, AND the parent mount needs `class="clip"` + `data-start` + `data-duration` + `data-track-index` + `data-width` + `data-height`. Missing any of these makes the studio silently load nothing (canvas: "Drop media here…", duration `0:00/0:00`) — and lint passes anyway. Always preview-check the duration in the studio before declaring done.
6. Only deterministic logic — no `Date.now()`, no `Math.random()`, no network fetches
7. **Speedup is always ffmpeg post-process on the rendered MP4** — see [`.claude/rules/video-speedup.md`](.claude/rules/video-speedup.md). Never edit `ELEVENLABS_SPEED` in `.env`, never regenerate narration, never re-render to change pacing.
8. **YouTube descriptions follow [`.claude/rules/youtube-metadata.md`](.claude/rules/youtube-metadata.md)** — every video MUST ship a `videos/<slug>/youtube-description.md`. Mandatory: vidIQ keyword research before drafting, keyword-front-loaded first 200 chars, SEO chapter titles, the Dynamous CTA block in `----` separators, validated URLs, a debate-sparking engagement question, 15-25 hashtags. Chapter timestamps are `data-start ÷ speed_factor` when the MP4 was ffmpeg-sped.
9. **Enumerated lists reveal step-by-step — never all bullets at once** — see [`.claude/rules/step-by-step-reveal.md`](.claude/rules/step-by-step-reveal.md). Each card / row / item in a list enters on its own beat, paced to when narration would name it (~5s apart in a 30s+ phase). Quick `+0.7s` staggers belong on hero "cast" reveals, not on enumerated explanations. Without TTS yet, use placeholder spacing — retime to transcript word-anchors when narration lands. **Hidden-until-reveal pattern is REQUIRED**: use explicit `tl.set()` at `t=0` + `tl.to()` at the reveal time, NOT `tl.from()` (which leaves elements visible until the tween fires).
10. **Shorts typography minimums** — see [`.claude/rules/shorts-typography.md`](.claude/rules/shorts-typography.md). On 1080×1920 canvas, body text < 32px renders at ≤11px on phone (unreadable). Min sizes: list-item primary 48px, descriptor 30px, decision-matrix question 36px, answer 42px, hero slam 140px+, CTA pill 44px+. Long-form (1920×1080) is NOT covered.
11. **Visual pacing — never static more than 5 seconds** — see [`.claude/rules/visual-pacing-5s.md`](.claude/rules/visual-pacing-5s.md). In every phase, no gap between visual changes (entrances, marker sweeps, scale pulses, glow pulses) may exceed 5 seconds — including the gap from the last entrance to the phase's exit. Persistent backgrounds (ambient, shape drift, progress bar) do NOT count. Audit every phase before lint.
12. **TTS heteronym audit before generating narration** — see [`.claude/rules/tts-pronunciation.md`](.claude/rules/tts-pronunciation.md). The `eleven_multilingual_v2` model has no per-word semantic disambiguation and its pronunciation dictionaries don't support phoneme rules. Heteronyms like `live` (laɪv adj vs. lɪv verb), `lead` (liːd vs. lɛd), `read`, `close`, `record` MUST be checked at the script level before TTS. Default fixes: `live today` → `available today`; `live on the platform` → `shipping on the platform`; `lead agent` → `primary agent` / `coordinator agent`. Phase 2a enforces the audit; the rule lists every known failure mode and grows when new ones are discovered.
13. **Shorts MUST open AND close on thumbnail-grade frames** — see [`.claude/rules/shorts-thumbnail-frames.md`](.claude/rules/shorts-thumbnail-frames.md). **First frame** (t=0): YouTube auto-picks this as the entry thumbnail when none is uploaded — it must already show topic + brand + receipt (open-topic-then-pivot pattern). **Last frame**: held still (≥1.5s after entrance settles) that with no audio and no prior frames communicates the topic in under one second. Both frames require: dominant topic statement (≥120px), visual anchor, brand chrome, outcome receipt line. Forbidden on either: solo CTA on empty background, fade-to-black, brand-only stills. Explicitly relaxes [`visual-pacing-5s`](.claude/rules/visual-pacing-5s.md) for both the opening hold (≤2.5s) and the terminal hold (≤2.5s).
14. **HyperFrames pitfalls cheat sheet** — see [`.claude/rules/hyperframes-pitfalls.md`](.claude/rules/hyperframes-pitfalls.md). Covers the upstream [Common Mistakes](https://hyperframes.mintlify.app/guides/common-mistakes) and [Troubleshooting](https://hyperframes.mintlify.app/guides/troubleshooting) items the linter does NOT catch and that aren't already in other rules: composition duration shorter than narration (`tl.set({}, {}, TOTAL_DURATION)` extender), oversized source images (decoded-bitmap cost — keep ≤2× canvas), heavy `backdrop-filter` stacks (≤2-3 layers, none > 64px radius), HDR vs SDR output decisions, render-vs-preview determinism via `--docker`, preview-stutter debug path, and render-speed knobs (`benchmark`, `--workers`, `--gpu`). Check before final render. Upstream doc index: `https://hyperframes.mintlify.app/llms.txt`.
15. **Every video MUST end on a debate-sparking CTA** — see [`.claude/rules/engagement-cta.md`](.claude/rules/engagement-cta.md). A polarizing, easy-to-answer question in THREE places that all agree: (1) the final 3–5s of narration, (2) an on-screen `#cta-question` element in the final phase of `index.html` (persists through the thumbnail-grade final frame), (3) the closing paragraph of `youtube-description.md`. The question MUST be binary-or-short-list answerable, take a polarizing stance, reference a specific claim from the video, and answerable in 5 seconds by both senior and beginner viewers. BANNED closers: "What do you think?", "Let me know in the comments", "Drop your thoughts below", "How would you build this differently?", "Link below". Applies to ALL videos including tutorials — voice_profile does NOT exempt this rule.

## Building New Templates — Consistent Workflow

When the user asks for a **new template** (a new variant under `templates/shorts/<style>/` or `templates/long-form/<style>/`), follow this checklist exactly. Every shipped template MUST satisfy every requirement below — this keeps the catalog coherent and ensures `diy-yt-creator` can drive the new template the same way it drives the existing ones.

### Decision: which family?

| Family | Canvas | Duration | Architecture | Bg-music | Captions |
|---|---|---|---|---|---|
| `templates/shorts/<style>/` | 1080x1920 vertical | 24-180s | Phase mutex inside one `index.html` (`#phase1` / `#phase2` z-index escalation) | Forbidden (narration + SFX only) | Optional |
| `templates/long-form/<style>/` | 1920x1080 horizontal | 4-15+ min | Sub-composition split — each scene is `compositions/scene-*.html` with its own paused timeline; root only orchestrates | 3-segment bed (hook/body/cta on track 3) | Recommended (`compositions/captions.html` with `data-caption-root="true"`) |

For a new **variant** of an existing family, fork the closest existing template (e.g. `cp -r templates/long-form/standard templates/long-form/<variant>`). Don't author from scratch.

### Required template files (every template, both families)

```
templates/<format>/<style>/
├── meta.json              ← { "id": "REPLACE_WITH_VIDEO_SLUG", "name": "REPLACE_WITH_VIDEO_NAME" }
├── hyperframes.json       ← byte-identical copy from another template (schema/registry/paths config)
├── sfx-cues.txt           ← default cue list (one per line), seeds scripts/sync-video-sfx.sh
├── README.md              ← spawn-a-new-video workflow (mirror an existing template's structure)
├── DESIGN.md              ← color/type/motion spec (mirror an existing template's structure)
├── index.html             ← root composition; for long-form, only orchestrates (ambient + crossfades)
├── tokens/<name>.css      ← CSS variable system on :root (palette + spacing + type)
├── compositions/          ← long-form: one HTML file per scene archetype + captions.html
│                            shorts: usually empty (phase mutex lives in index.html)
├── audio/.gitkeep         ← operator drops narration + (long-form) bg-music here
└── assets/
    ├── shapes/            ← background drift shapes (3 SVGs typical)
    ├── sfx/.gitkeep       ← scripts/sync-video-sfx.sh populates per video
    ├── screenshots/       ← long-form only: placeholder PNGs operators replace per video
    ├── clips/.gitkeep     ← long-form only: operator drops embedded video clips
    └── <brand>-logo-light.svg|png  ← copied from shared/logos/ (NEVER reference shared/ at runtime)
```

### Step-by-step: shipping a new template

1. **Pick the slug.** Kebab-case, descriptive of the aesthetic (e.g. `dynamous`, `news-explainer`, `tutorial`, `claude-code-version`). Reserve `standard` / `default` / `base` for the canonical baseline only.

2. **Fork the closest existing template.** `cp -r templates/<format>/<closest-existing-style> templates/<format>/<new-style>`.

3. **Swap the palette** in `tokens/<name>.css`. Re-declare `--bg`, accent vars, and any spacing tokens that need to change. Keep the variable names identical to the parent template — operators rely on those names being stable.

4. **Replace, remove, or add scene/phase archetypes.** For long-form, edit `compositions/scene-*.html` (each is independent). For shorts, edit the phase mutex inside `index.html`. Don't duplicate scene archetypes that already exist — the goal is a meaningful variant, not a re-skinned twin.

5. **Update `meta.json`** if the placeholders need format hints (most templates leave the placeholders alone — operators replace them per video).

6. **Update `README.md`** to describe what's unique about this variant (palette, scene archetypes, intended use cases). Use the existing `README.md` as the structural template.

7. **Update `DESIGN.md`** with the variant's color/type/motion spec. Same structural mirror.

8. **Pair the template with shared-lib catalog entries** (only if the variant introduces a new visual style). Two files + one MANIFEST update:
   - `shared/lib/visual-styles/<name>.md` — named-style fragment (palette, type, motion signature, suggested lib picks, anti-patterns). Mirror an existing visual-style file.
   - `shared/lib/tokens/<name>.css` — byte-identical copy of `templates/<format>/<style>/tokens/<name>.css`. Future variants pick this up via copy-from per the lib consumption rules.
   - Append entries to `shared/lib/MANIFEST.md` under the **Tokens** and **Visual Styles** tables (between the `<!-- LIB:TOKENS:BEGIN -->` / `<!-- LIB:VISUAL-STYLES:BEGIN -->` sentinels).

9. **Create the diy-yt-creator playbook.** Every template MUST have a matching playbook at `.claude/skills/diy-yt-creator/new-<style>.md` (for shorts) or `new-long-form-<style>.md` (for long-form). Mirror an existing playbook (e.g. [`new-archon-short.md`](.claude/skills/diy-yt-creator/new-archon-short.md) is a tight delta-from-`new-anthropic-short.md`). Include:
   - Inputs (topic / facts / pre-written script)
   - Outputs (the per-video artifacts)
   - 12-step workflow with deltas from the parent template called out
   - Quality bar checklist
   - Don'ts (template-specific)

10. **Register the playbook** by adding a row to the table in [`.claude/skills/diy-yt-creator/SKILL.md`](.claude/skills/diy-yt-creator/SKILL.md) and a trigger phrase to the "When to invoke" list. Without this registration, `/diy-yt-creator` won't route to the new playbook.

11. **Update the parent format README** (`templates/shorts/README.md` or `templates/long-form/README.md`) — add a row to the "Available templates" table. Without this, the variant is invisible.

### Required validation gates (before declaring template done)

Run all of these. The bare template (no operator media) MUST pass them all:

```bash
npx hyperframes lint templates/<format>/<style>          # 0 errors, 0 warnings
npx hyperframes validate templates/<format>/<style>      # WCAG AA on all text; no contrast warnings
npx hyperframes inspect templates/<format>/<style>       # 0 layout overflow at the canvas size
```

Then **spawn dry-run** to verify the template is copy-friendly:

```bash
cp -r templates/<format>/<style> /tmp/test-spawn
sed -i 's/REPLACE_WITH_VIDEO_SLUG/test-spawn/' /tmp/test-spawn/meta.json
sed -i 's/REPLACE_WITH_VIDEO_NAME/Test Spawn/' /tmp/test-spawn/meta.json
npx hyperframes lint /tmp/test-spawn                     # must stay 0 errors, 0 warnings
rm -rf /tmp/test-spawn
```

Finally, **draft render** the bare template to confirm the renderer can complete:

```bash
npx hyperframes render templates/<format>/<style> --quality draft -o /tmp/<style>-smoke.mp4
```

If render hard-blocks on missing operator media (most often a `<video>` pointing at a missing `.mp4`), replace the live element with a placeholder slate / commented-out snippet. The bare template MUST be render-able — operators wire real media when they spawn a video from it.

### Recurring gotchas to design around

These hit every new template — bake them in from day one:

- **Lint parses HTML comments for media references.** Don't include literal `src="..."` attributes inside `<!-- ... -->` blocks (lint reports `duplicate_media_discovery_risk`). Use prose like "operator wires the video element" instead of pasting a sample tag.
- **`audio_src_not_found` is a lint error, not a warning.** If the template has live `<audio>` elements pointing at missing files, lint fails. Comment out the audio block with an "uncomment when ready" note (mirror the existing templates).
- **`<video>` missing source hard-blocks the renderer.** Unlike audio, missing video files cause `[FrameCapture] video metadata not ready after 45000ms`. Ship a placeholder slate; operators replace with the live `<video>` snippet from the template's README.
- **All sub-composition root divs need `data-start="0"`.** Long-form `compositions/scene-*.html` files lint-warn without it.
- **Sub-composition wrapper divs in the root MUST NOT have `data-duration`.** The sub-comp's internal timeline owns its length.
- **`tl.from()` at timeline position > 5 needs `immediateRender: false`.** Without the flag, GSAP applies the from-state at t=0 and the element flashes invisible at scrub time. Long-form-specific (Shorts at 24s rarely hit this).
- **`<audio>` and `<video>` NEVER take `class="clip"`.** Wrapper div gets the clip role for video; audio uses `data-start`/`data-duration`/`data-track-index` directly.
- **Logos must be local copies inside `assets/`.** HyperFrames' bundler/preview server rejects `../../shared/logos/...` paths. Copy first, reference local.
- **Deterministic-only.** No `Math.random()`, `Date.now()`, network fetches, or `repeat: -1`. Calculate finite repeats (e.g. `Math.floor(duration / cycle)`).

### Acceptance checklist (template ships only when ALL pass)

- [ ] Template directory exists with all required files (meta.json, hyperframes.json, sfx-cues.txt, README.md, DESIGN.md, index.html, tokens/*.css, optional compositions/, audio/.gitkeep, assets/{shapes,sfx,screenshots,clips})
- [ ] `npx hyperframes lint templates/<format>/<style>` → 0 errors, 0 warnings
- [ ] `npx hyperframes validate templates/<format>/<style>` → no AAA contrast failures, no AA failures on headlines
- [ ] `npx hyperframes inspect templates/<format>/<style>` → 0 layout overflow
- [ ] Spawn dry-run lints clean after copying to a fresh slug
- [ ] Bare-template draft render produces a playable MP4
- [ ] `shared/lib/visual-styles/<name>.md` exists and mirrors the structure of `anthropic-dark.md`
- [ ] `shared/lib/tokens/<name>.css` exists as a byte-identical copy of `templates/<format>/<style>/tokens/<name>.css`
- [ ] `shared/lib/MANIFEST.md` has new rows under Tokens and Visual Styles
- [ ] `.claude/skills/diy-yt-creator/new-<style>.md` (or `new-long-form-<style>.md`) playbook exists
- [ ] `.claude/skills/diy-yt-creator/SKILL.md` lists the new playbook in its table AND adds a trigger phrase to the "When to invoke" list
- [ ] `templates/<format>/README.md` "Available templates" table has a row for the new variant

If any item fails, the template is not ready to ship. Don't claim completion on a half-built template — operators downstream will hit the gap and lose trust in the catalog.
