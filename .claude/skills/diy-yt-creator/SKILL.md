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

## Available commands

| Command | Template used | Use when |
|---|---|---|
| [new-anthropic-short.md](./new-anthropic-short.md) | `templates/shorts/anthropic/` | User wants a vertical YouTube Short (1080x1920, 30fps, ~24-60s) in the Anthropic dark-stage aesthetic |

> **Long-form templates do not exist yet.** If the user asks for a long-form video, point them at `templates/long-form/README.md` and offer to build a long-form template first.

## Hard rules across every command

1. **Never auto-render.** Every workflow ends at `npx hyperframes preview videos/<slug>`. The user always triggers `npx hyperframes render` manually.
2. **Never fabricate facts.** Stats, dates, URLs, quotes must come from a source the user provides or that exists on the open web. If the topic has no source, ASK before drafting.
3. **Never modify the template itself.** Only edit the copy under `videos/<slug>/`.
4. **Never bundle multiple videos in one run.** One slug = one invocation.
5. **Always lint + inspect before reporting done.** Both must pass cleanly.
6. **Always invoke the `/hyperframes` skill** before editing any composition HTML — it has framework-specific rules (timeline registration, phase mutex, `data-*` semantics) that this skill assumes.

Open the relevant command file for the full playbook.
