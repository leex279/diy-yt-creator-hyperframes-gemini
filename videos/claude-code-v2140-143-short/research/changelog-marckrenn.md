# marckrenn — Claude Code Changelog (Highlights) — v2.1.140 → v2.1.143

Source pages:
- https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.140
- https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.141
- https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.142
- https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.143

Captured 2026-05-16.

---

## v2.1.140 — May 12

**Highlights:**

1. "Agent tool now accepts case- and separator-insensitive subagent type values, reducing tool-match failures"
2. "/goal no longer hangs when disableAllHooks/allowManagedHooksOnly is set; displays a message not a spinner"
3. "Edit workflow keeps indentation with line-number prefixes; JSON schema requires URL to avoid bad formatting"

---

## v2.1.141 — May 13, 23:29

**Highlights:**

1. "Hook JSON adds terminalSequence so hooks can emit notifications, window titles and bells without a TTY"
2. "Auto-mode permission dialogs indicate when a permissions.ask rule triggered them, clarifying why it appeared"
3. "Rewind menu adds 'Summarize up to here' to compress earlier context, preserving recent turns"

---

## v2.1.142 — May 14

**Highlights:**

1. "New 'claude agents' flags configure dirs, permissions, model, effort and plugin/MCP settings for finer control"
2. "grep now uses ripgrep as the default search tool for faster, more accurate results"
3. "Background daemon detects clock jumps after macOS sleep/wake, preventing session loss and reconnect failures"

---

## v2.1.143 — May 15

**Highlights:**

1. "Plugin disable refuses if enabled plugins depend on it, showing a disable-chain hint to avoid broken setups"
2. "Plugin marketplace shows per-turn and per-invocation token estimates, making token usage & costs visible"
3. "Background sessions now preserve model and effort level after waking, preventing unexpected model resets"
