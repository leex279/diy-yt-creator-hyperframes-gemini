"""Summarize diy-yt-creator phase runs from .claude/runs/runs.jsonl

Usage:
  python scripts/analyze-runs.py                  # summary table
  python scripts/analyze-runs.py --slug <slug>    # filter to one video
  python scripts/analyze-runs.py --phase <name>   # filter to one phase
  python scripts/analyze-runs.py --recent 20      # only the last N runs
  python scripts/analyze-runs.py --json           # machine-readable output
  python scripts/analyze-runs.py --raw            # dump every record
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = REPO_ROOT / ".claude" / "runs" / "runs.jsonl"


def load_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def fmt_seconds(s: float) -> str:
    if s >= 60:
        return f"{s / 60:.1f}m"
    return f"{s:.1f}s"


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    if len(values) == 1:
        return values[0]
    ordered = sorted(values)
    k = (len(ordered) - 1) * pct
    lo = int(k)
    hi = min(lo + 1, len(ordered) - 1)
    frac = k - lo
    return ordered[lo] + (ordered[hi] - ordered[lo]) * frac


def summarize(records: list[dict]) -> dict:
    by_phase: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_phase[r.get("phase") or "unknown"].append(r)

    rows = []
    for phase, items in sorted(by_phase.items()):
        durations = [r.get("duration_s", 0.0) or 0.0 for r in items]
        failures = sum(1 for r in items if r.get("status") not in ("ok", None))
        tool_totals: Counter = Counter()
        for r in items:
            tool_totals.update(r.get("tool_calls") or {})
        top_tools = ", ".join(f"{t}:{n}" for t, n in tool_totals.most_common(4))
        rows.append(
            {
                "phase": phase,
                "runs": len(items),
                "median_s": round(statistics.median(durations), 1) if durations else 0.0,
                "p95_s": round(percentile(durations, 0.95), 1) if durations else 0.0,
                "avg_s": round(sum(durations) / len(durations), 1) if durations else 0.0,
                "min_s": round(min(durations), 1) if durations else 0.0,
                "max_s": round(max(durations), 1) if durations else 0.0,
                "failures": failures,
                "top_tools": top_tools,
            }
        )
    return {"total_runs": len(records), "rows": rows}


def print_table(summary: dict) -> None:
    rows = summary["rows"]
    if not rows:
        print("No runs recorded yet. Trigger a /diy-yt-creator:* command to start logging.")
        return

    headers = ["Phase", "Runs", "Median", "p95", "Avg", "Min", "Max", "Fail", "Top tools"]
    table = [
        [
            r["phase"],
            str(r["runs"]),
            fmt_seconds(r["median_s"]),
            fmt_seconds(r["p95_s"]),
            fmt_seconds(r["avg_s"]),
            fmt_seconds(r["min_s"]),
            fmt_seconds(r["max_s"]),
            str(r["failures"]),
            r["top_tools"][:60],
        ]
        for r in rows
    ]
    widths = [
        max(len(h), max((len(row[i]) for row in table), default=0))
        for i, h in enumerate(headers)
    ]

    def fmt(row):
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row))

    print(fmt(headers))
    print(fmt(["-" * w for w in widths]))
    for row in table:
        print(fmt(row))
    print()
    print(f"Total runs logged: {summary['total_runs']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", help="filter to one video slug")
    parser.add_argument("--phase", help="filter to one phase name")
    parser.add_argument("--recent", type=int, help="only the last N runs")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--raw", action="store_true", help="dump every record")
    args = parser.parse_args()

    records = load_records(LOG_FILE)
    if args.slug:
        records = [r for r in records if r.get("video_slug") == args.slug]
    if args.phase:
        records = [r for r in records if r.get("phase") == args.phase]
    if args.recent:
        records = records[-args.recent :]

    if args.raw:
        for r in records:
            print(json.dumps(r))
        return 0

    summary = summarize(records)

    if args.json:
        print(json.dumps(summary, indent=2))
        return 0

    print_table(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
