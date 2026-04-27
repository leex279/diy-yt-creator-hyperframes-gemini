---
name: diy-yt-creator
description: Use when the user wants to create a new YouTube video using one of the templates in this repo's templates/ folder. Spawns the project folder, drafts the script from a topic, generates TTS, fills the composition with real content sync'd to word-level timestamps, lints + inspects, and opens preview. Never auto-renders.
---

# diy-yt-creator

Zero-manual-step workflows for spawning fully-prepped HyperFrames videos from the templates in `templates/`.

## When to invoke

Trigger when the user says any of:

- "create / make / spawn a new short / video"
- "new anthropic short about X"
- "/diy-yt-creator:new-anthropic-short …"
- Anything that asks to scaffold a video from a template in this repo
- "capture / screenshot <url> for video <slug>" → uses `capture-asset`
- "QA / check / verify the preview for <slug>" → uses `qa-composition`

## Available commands

### Composition-build commands (template-specific HTML edit)

| Command | Template used | Use when |
|---|---|---|
| [new-anthropic-short.md](./new-anthropic-short.md) | `templates/shorts/anthropic/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~24-60s) in the Anthropic dark-stage aesthetic |
| [capture-asset.md](./capture-asset.md) | n/a (uses `agent-browser`) | Per-video screenshot/asset from a public URL into `videos/<slug>/assets/` |
| [qa-composition.md](./qa-composition.md) | n/a (uses `agent-browser`) | Visually QA a running `hyperframes preview` — snapshot each phase, report issues |

> **Long-form templates do not exist yet.** If the user asks for a long-form video, point them at `templates/long-form/README.md` and offer to build a long-form template first.

### Pipeline commands (research + scriptwriting + retention)

These are first-class slash commands under `.claude/commands/diy-yt-creator/`. They produce the research, script, and retention artifacts that feed the composition-build step.

| Command | Use when |
|---|---|
| [/diy-yt-creator:full-auto](../../commands/diy-yt-creator/full-auto.md) | End-to-end pipeline from topic to retention-engineered script + per-scene retention strategy. Stops twice for human review (TTS, composition build). Use this by default. |
| [/diy-yt-creator:phase0-research](../../commands/diy-yt-creator/phase0-research.md) | Topic research only (vidiq + web search + 4 parallel agents → `videos/<slug>/research/content-brief.md`) |
| [/diy-yt-creator:phase1-plan](../../commands/diy-yt-creator/phase1-plan.md) | Composition plan (after Phase 0) — scenes, hook variants, retention component picks, `data-start`/`data-duration` budget |
| [/diy-yt-creator:phase2-script](../../commands/diy-yt-creator/phase2-script.md) | Draft narration script (after Phase 1) |
| [/diy-yt-creator:phase2-5-critique](../../commands/diy-yt-creator/phase2-5-critique.md) | Quality gate on script (after Phase 2) — hook score, story arc, banned phrases |
| [/diy-yt-creator:phase2a-tts-script](../../commands/diy-yt-creator/phase2a-tts-script.md) | TTS-optimize script + write flat `script.txt` (after Phase 2.5) |
| [/diy-yt-creator:phase2b-factcheck](../../commands/diy-yt-creator/phase2b-factcheck.md) | Fact-check claims via WebSearch (after Phase 2a) |
| [/diy-yt-creator:phase3-5-retention](../../commands/diy-yt-creator/phase3-5-retention.md) | Per-scene retention strategy from `transcript.json` (after `npx hyperframes transcribe` runs) |
| [/diy-yt-creator:brief-template](../../commands/diy-yt-creator/brief-template.md) | Reference for the structured-brief input format |

## Pipeline vs direct invocation

- **Use `/diy-yt-creator:full-auto`** when the user gives you a topic and wants a researched, fact-checked, retention-engineered video. This is the default.
- **Use `/diy-yt-creator:new-anthropic-short` directly** when the user already has a finished `script.txt` (or content brief) and just wants the composition built. Skips all research/critique/fact-check steps.
- **Use individual phase commands** when debugging or re-running a single phase after fixes.

The composition-build skill (`new-anthropic-short.md`) reads `videos/<slug>/scripts/full-script.md` and `videos/<slug>/plan.md` if they exist (Branch A in step 4) — so the pipeline output flows naturally into the build.

## Hard rules across every command

1. **Never auto-render.** Every workflow ends at `npx hyperframes preview videos/<slug>`. The user always triggers `npx hyperframes render` manually.
2. **Never fabricate facts.** Stats, dates, URLs, quotes must come from a source the user provides or that exists on the open web. If the topic has no source, ASK before drafting.
3. **Never modify the template itself.** Only edit the copy under `videos/<slug>/`.
4. **Never bundle multiple videos in one run.** One slug = one invocation.
5. **Always lint + inspect before reporting done.** Both must pass cleanly.
6. **Always invoke the `/hyperframes` skill** before editing any composition HTML — it has framework-specific rules (timeline registration, phase mutex, `data-*` semantics) that this skill assumes.

Open the relevant command file for the full playbook.
