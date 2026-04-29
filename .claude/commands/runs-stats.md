---
description: "Summarize logged diy-yt-creator phase runs (duration, failures, tool usage)"
argument-hint: "[--slug <slug>] [--phase <name>] [--recent N] [--json] [--raw]"
allowed-tools: Bash
---

Run the analysis script and present the result to the user verbatim. Pass `$ARGUMENTS` straight through.

```bash
python scripts/analyze-runs.py $ARGUMENTS
```

If the table is empty, tell the user no runs are logged yet — the hooks in `.claude/settings.json` will start populating `.claude/runs/runs.jsonl` once they invoke a `/diy-yt-creator:*` phase command.

Useful flags to remind the user about:
- `--slug <slug>` — filter to one video
- `--phase <name>` — drill into one phase across all videos
- `--recent 20` — only the last N runs (handy after a pipeline tweak)
- `--raw` — dump every JSONL record (when looking for one specific outlier)

After printing, if any phase shows a high p95 / median ratio (slow tail) or non-zero failures, point that out as a candidate for investigation or a smaller-model swap.
