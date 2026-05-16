---
description: "Comprehensive video-production review — 5 specialized agents in parallel (timing, render, layout, content, metadata)"
argument-hint: <slug> [--mode pre-render|pre-publish|perfect] [--fix off|safe|aggressive] [--visual] [--severity blocker|high|medium|low]
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Task, WebFetch, Agent
---

Invoke the `video-review` skill with the user's arguments.

```
slug + flags = $ARGUMENTS
```

If `$ARGUMENTS` is empty or just the word `help`, print:

```
Usage: /video-review <slug> [--mode <mode>] [--fix <policy>] [--visual] [--severity <floor>]

Examples:
  /video-review claude-code-v2-launch
  /video-review claude-code-v2-launch --mode pre-render
  /video-review claude-code-v2-launch --mode perfect --visual
  /video-review claude-code-v2-launch --fix safe
  /video-review claude-code-v2-launch --fix off --severity high

Modes:
  pre-render     Only BLOCKER findings count. Use right before npx hyperframes render.
  pre-publish    (default) BLOCKER + HIGH gate publish.
  perfect        Everything reported (BLOCKER + HIGH + MEDIUM + LOW).

Auto-fix:
  off            Report only.
  safe           (default) Apply mechanical fixes (font-var, missing description scaffold,
                 banned-phrase swap, chapter-timestamp recompute). Ask before script edits.
  aggressive     Also apply heteronym swaps + banned-CTA rewrites.

--visual         Add screenshot pass via agent-browser (requires hyperframes preview running).

Falls through to the `video-review` skill — see .claude/skills/video-review/SKILL.md for the full process.
```

Otherwise: invoke the `video-review` skill with $ARGUMENTS passed verbatim. The skill orchestrator parses flags, dispatches the 5 specialized agents in parallel (`video-timing-pacer`, `video-render-validator`, `video-layout-typography`, `video-script-content`, `video-metadata-publish`), aggregates findings by severity, optionally applies safe auto-fixes, and prints a Markdown report + saves JSON to `videos/<slug>/qa/review-report.json`.
