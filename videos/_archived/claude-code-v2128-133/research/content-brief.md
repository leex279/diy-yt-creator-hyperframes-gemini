# Content Brief — Claude Code v2.1.128 → v2.1.133 — What's New

## Version Range
v2.1.128, v2.1.129, v2.1.131, v2.1.132, v2.1.133
(v2.1.127 + v2.1.130 are absent from the upstream changelog — skipped releases.)

Slug: `claude-code-v2128-133`
Render target: 1920x1080 30fps, ~3.5–4 minutes, MP4 with VersionBranding overlay.

## Stats (stats-opener Phase 1)

Counted from the official changelog above (Added/Changed → features; Improved → improved; Fixed → fixes).

- **Features:** 28
- **Fixes:** 78
- **Improved:** 4

## Highlights (scene-feature-cards — 6 cards, 3×2 grid)

User-confirmed pre-selection (strongest 6 across the range):

1. `worktree.baseRef` setting (v133) — choose `fresh` (origin/default) vs `head` (local HEAD) for new worktrees
2. `--plugin-url <url>` flag (v129) — fetch plugin `.zip` archive from URL for current session
3. `$CLAUDE_EFFORT` in hooks + Bash (v133) — hooks adapt to active effort level
4. `CLAUDE_CODE_SESSION_ID` env var (v132) — Bash subprocess gets matching hook session ID for tool tracing
5. `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` (v132) — keep conversation in native terminal scrollback
6. Subagent skills discovery fix (v133) — subagents now find project, user, and plugin skills via Skill tool

## Stats-Opener Phase 2 — Biggest patch dive: MCP got a stability pass

Cards (2×2 grid):
01 — Tool list reconnect floods gone — re-announced tools summarized by server prefix (v128)
02 — Servers that connect but fail tools-list now retry once + show "fetch failed" status in `/mcp` (v132)
03 — Stdio MCP servers writing non-protocol stdout were leaking 10 GB+ RSS — patched (v132)
04 — MCP OAuth now respects `HTTP(S)_PROXY` / `NO_PROXY` / mTLS across discovery + token refresh (v133)

## Detail Scene Assignments

| Template file               | Repurposed category for v2.1.128–v2.1.133 |
|-----------------------------|--------------------------------------------|
| scene-detail-headless       | Hooks & Power-User APIs                    |
| scene-detail-performance    | Auth, OAuth & Sessions                     |
| scene-detail-plugin-system  | Plugins, MCP & Skills                      |
| scene-detail-terminal-ui    | Terminal UI & Editor Integration           |
| scene-detail-network        | Network, Proxy & API Compatibility         |

### Hooks & Power-User APIs (detail-headless)

01 — `$CLAUDE_EFFORT` env var flows into hooks + Bash subprocesses (v133)
02 — `CLAUDE_CODE_SESSION_ID` matches hook session ID — every Bash run can write to a session-scoped log (v132)
03 — `worktree.baseRef` setting — `fresh` (origin/default) vs `head` (local HEAD) for new worktree base branch (v133)
04 — `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) — custom bubblewrap and socat binaries (v133)

### Auth, OAuth & Sessions (detail-performance)

01 — Refresh-token race: parallel sessions all dead-ending at 401 after a refresh wiped shared credentials — patched (v133)
02 — OAuth refresh race after wake-from-sleep was logging out all running sessions — fixed (v129)
03 — 1-hour prompt cache TTL was being silently downgraded to 5 minutes — now honored (v129)
04 — `/effort` in one session no longer leaks into other concurrent sessions (v133)

### Plugins, MCP & Skills (detail-plugin-system)

01 — `--plugin-url <url>` fetches plugin `.zip` archive from any URL — session-scoped install (v129)
02 — Subagents now discover project, user, and plugin skills via the Skill tool (v133)
03 — MCP server reconnects no longer flood chat with full tool-name lists — re-announced tools summarized by server prefix (v128)
04 — Stdio MCP servers writing non-protocol stdout were leaking 10 GB+ RSS — fixed (v132)

### Terminal UI & Editor Integration (detail-terminal-ui)

01 — `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` keeps the conversation in native terminal scrollback (v132)
02 — Mouse wheel scrolling speed in Cursor + VS Code 1.92–1.104 — upstream xterm.js bug patched (v132)
03 — Fullscreen mode going blank after laptop sleep/wake or `Ctrl+Z`/`fg` — fixed (v132)
04 — `/terminal-setup` no longer shows a contradictory error in Windows Terminal — Shift+Enter is natively supported (v132)

### Network, Proxy & API Compatibility (detail-network)

01 — `HTTP(S)_PROXY` / `NO_PROXY` / mTLS now honored across full MCP OAuth flow — discovery, dynamic client registration, token exchange, refresh (v133)
02 — Bedrock + Vertex 400 errors when `ENABLE_PROMPT_CACHING_1H` is set — patched (v132)
03 — VS Code extension activation on Windows — hardcoded build path fixed (v131)
04 — Mantle endpoint authentication failure with missing `x-api-key` header — restored (v131)

## Terminal Scene Pick

`$ claude update` — the CTA close (default; no command demo specifically called out by this range).

## Hook Angle

"Six Claude Code releases shipped this week. The biggest pass: MCP got a stability win, and your hooks just got smarter — they now know which effort level is running."

The unifying theme across this range is **automation getting smarter**: hooks see effort level, sessions are traceable, plugins install from URLs, subagents finally find skills.

## WatchNext

Skipped (user choice).
