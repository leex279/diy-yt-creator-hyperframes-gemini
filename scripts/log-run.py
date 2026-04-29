"""Log diy-yt-creator phase runs to .claude/runs/runs.jsonl

Wired up by hooks in .claude/settings.json. Three events:
  user_prompt    - detect /diy-yt-creator phase commands, open a run record
  post_tool_use  - increment tool-call counters for the active run
  stop           - close out the active run with end time + duration

Designed to be silent and non-blocking: any error swallows and exits 0 so a
broken logger never blocks the user.

Usage (called by Claude Code, not by hand):
  python scripts/log-run.py user_prompt    < hook-payload.json
  python scripts/log-run.py post_tool_use  < hook-payload.json
  python scripts/log-run.py stop           < hook-payload.json
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = REPO_ROOT / ".claude" / "runs"
LOG_FILE = RUNS_DIR / "runs.jsonl"

PHASE_RE = re.compile(r"/diy-yt-creator[:/]([\w.-]+)", re.IGNORECASE)
SLUG_RE = re.compile(r"videos/([a-z0-9][\w-]*)", re.IGNORECASE)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def state_path(session_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "unknown")
    return RUNS_DIR / f".active-{safe}.json"


def load_state(session_id: str) -> dict | None:
    p = state_path(session_id)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_state(session_id: str, state: dict) -> None:
    state_path(session_id).write_text(json.dumps(state), encoding="utf-8")


def clear_state(session_id: str) -> None:
    p = state_path(session_id)
    if p.exists():
        try:
            p.unlink()
        except Exception:
            pass


def append_record(record: dict) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, separators=(",", ":")) + "\n")


def finalize(state: dict, status: str) -> None:
    end = now_utc()
    try:
        start = datetime.fromisoformat(state["start_ts"])
    except Exception:
        start = end
    record = {
        "run_id": state.get("run_id"),
        "session_id": state.get("session_id"),
        "phase": state.get("phase"),
        "video_slug": state.get("video_slug"),
        "start_ts": state.get("start_ts"),
        "end_ts": end.isoformat(),
        "duration_s": round((end - start).total_seconds(), 3),
        "status": status,
        "tool_calls": state.get("tool_calls", {}),
        "tool_call_total": sum(state.get("tool_calls", {}).values()),
        "prompt_excerpt": state.get("prompt_excerpt"),
    }
    append_record(record)


def handle_user_prompt(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    prompt = payload.get("prompt", "") or ""

    # New prompt arriving while a run is open means the previous run's Stop
    # never fired (rare) — close it as superseded so we still get a record.
    existing = load_state(session_id)
    if existing:
        finalize(existing, status="superseded")
        clear_state(session_id)

    match = PHASE_RE.search(prompt)
    if not match:
        return

    phase = match.group(1).lower()
    slug_match = SLUG_RE.search(prompt)
    slug = slug_match.group(1) if slug_match else None

    start = now_utc()
    state = {
        "run_id": f"{session_id[:8]}-{phase}-{int(start.timestamp())}",
        "session_id": session_id,
        "phase": phase,
        "video_slug": slug,
        "start_ts": start.isoformat(),
        "tool_calls": {},
        "prompt_excerpt": prompt[:200],
    }
    save_state(session_id, state)


def handle_post_tool_use(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    state = load_state(session_id)
    if not state:
        return
    tool = payload.get("tool_name") or "unknown"
    state["tool_calls"][tool] = state["tool_calls"].get(tool, 0) + 1
    save_state(session_id, state)


def handle_stop(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    state = load_state(session_id)
    if not state:
        return
    finalize(state, status="ok")
    clear_state(session_id)


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    event = sys.argv[1]
    try:
        RUNS_DIR.mkdir(parents=True, exist_ok=True)
        payload = json.load(sys.stdin)
        if event == "user_prompt":
            handle_user_prompt(payload)
        elif event == "post_tool_use":
            handle_post_tool_use(payload)
        elif event == "stop":
            handle_stop(payload)
    except Exception:
        # Never block the user on monitoring failures.
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
