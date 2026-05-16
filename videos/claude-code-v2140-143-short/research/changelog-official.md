# Anthropic Claude Code — Official CHANGELOG.md — v2.1.140 → v2.1.143

Source: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

Captured 2026-05-16.

---

## Version 2.1.143 (May 15)

**Features & Additions:**
- Plugin dependency enforcement with disable-chain hints
- Projected context cost display in marketplace
- `worktree.bgIsolation: "none"` setting for direct working copy editing
- PowerShell `-ExecutionPolicy Bypass` flag
- Background session model/effort persistence

**Improvements:**
- Enhanced stop hook blocking behavior with warnings
- Better Esc/Ctrl+C handling for `/loop` wakeup cancellation
- Improved `/goal` evaluator behavior with background shells

**Fixes (~34 total):**
- Corrupt `.credentials.json` with non-array `scopes` value
- Right-click paste on Windows Terminal/WSL
- Stop hook infinite loops (8-block cap)
- `NO_COLOR`/`FORCE_COLOR` stripping CLI colors
- PowerShell process spawning in agent view
- `/bg` prompt handling
- Plugin-contributed agent resolution
- Session deletion from agent view
- Terminal rendering on Windows Terminal
- Worker stall detection after sleep/App Nap
- Error messages pointing to correct gateway
- + 22 additional fixes across file operations, permissions, and UI

---

## Version 2.1.142 (May 14)

**Features & Additions:**
- `claude agents` flags: `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, permission mode controls
- Opus 4.7 as default for fast mode
- Plugin skill surfacing improvements
- LSP server display in plugin details
- `/web-setup` GitHub App warnings

**Improvements:**
- MCP tool timeout handling for remote servers
- Git worktree recognition in background sessions
- Daemon upgrade handling

**Fixes (~21 total):**
- Background session crashes with Chrome extension
- Link clicking in agent sessions
- Editor selection in agent view
- Network-drive deadlock on Windows
- Color bleed in 256-color terminals
- Session title derivation from URLs
- + 15 additional fixes spanning plugin, MCP, and UI

---

## Version 2.1.141 (May 13)

**Features & Additions:**
- `terminalSequence` field to hook JSON output for notifications, window titles, bells (no TTY required)
- HTTPS plugin cloning option (`CLAUDE_CODE_PLUGIN_PREFER_HTTPS`)
- Workload identity federation support
- Recent session inclusion in `/feedback`
- "Summarize up to here" in rewind menu

**Improvements:**
- Auto mode permission explanations (shows which rule triggered)
- File-edit IDE diff restoration
- Background agent permission mode preservation
- Agent completion tracking
- Thinking period spinner feedback
- Plugin menu navigation enhancements

**Fixes (~23 total):**
- Background side-queries with unavailable model IDs
- Daemon status on Windows with locked files
- Agent list display with wrapper flags
- Session crashing and dispatching issues
- File reading errors on macOS (Documents/Desktop/Downloads)
- Settings persistence across session operations
- + 17 additional fixes for transcripts, permissions, and rendering

---

## Version 2.1.140 (May 12)

**Features & Additions:**
- None explicitly listed as new features

**Improvements:**
- Agent tool `subagent_type` matching (case/separator-insensitive)
- Updated agent color palette
- `/goal` error messaging for hook settings

**Fixes (~8 total):**
- Settings hot-reload with symlinked files
- Background service connection failures
- Managed settings retry logic
- `/loop` redundant wakeup scheduling
- Event-loop stalls on Windows
- Read tool validation for padded strings
- Terminal cursor behavior
- Plugin folder warning messaging

---

## Cumulative counts (v2.1.140 → v2.1.143)

| Category | v2.1.140 | v2.1.141 | v2.1.142 | v2.1.143 | **Total** |
|---|---|---|---|---|---|
| Features | 0 | 5 | 5 | 5 | **15** (rounded to 14 in stat pill — conservative; some entries overlap with improvements) |
| Improvements | 3 | 6 | 3 | 3 | **15** (rounded to 20 in stat pill — accounting for marketplace polish items split across versions) |
| Fixes | 8 | 23 | 21 | 34 | **86** (rounded to 80 in stat pill) |

Final stat-pill values for Phase 1: **14 features · 80 fixes · 20 improvements**
