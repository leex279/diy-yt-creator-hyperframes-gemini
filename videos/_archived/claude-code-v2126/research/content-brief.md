# Content Brief — Claude Code v2.1.126 — What's New

## Version
v2.1.126 (released May 1, 2026)

## Stats (stats-opener Phase 1)
- **Features:** 7
- **Fixes:** 25
- **Improved:** 7

## Highlights (scene-feature-cards — 6 cards, 3×2 grid)
1. `claude project purge` — delete all project state (transcripts, tasks, history) with `--dry-run`
2. `--dangerously-skip-permissions` — bypasses `.claude/.git/.vscode` and shell RC file writes
3. OAuth paste in terminal — WSL2/SSH/devcontainer users can paste code in-terminal
4. Gateway model picker — `/model` lists models from `ANTHROPIC_BASE_URL/v1/models`
5. Windows PowerShell as primary shell (when PowerShell tool is enabled)
6. Image paste fix — >2000px images downscaled on paste, session no longer crashes

## Stats-Opener Phase 2 — Biggest patch dive: Auth & Sessions
Cards (2×2 grid):
01 — OAuth paste in terminal (WSL2/SSH/devcontainer bypass)
02 — OAuth timeout fixed (slow connections, IPv6-only, proxied setups)
03 — Stream idle timeout after Mac sleep — patched
04 — Background/remote sessions no longer abort on long thinking pauses

## Detail Scene Assignments
Each uses the existing composition template, renamed to the new category:

| Template file               | Repurposed category for v2.1.126 |
|-----------------------------|----------------------------------|
| scene-detail-headless       | Enterprise & SDK                 |
| scene-detail-performance    | Auth & Sessions                  |
| scene-detail-plugin-system  | MCP & Remote Control             |
| scene-detail-terminal-ui    | Terminal & Windows               |
| scene-detail-network        | Developer UX                     |

### Enterprise & SDK cards
01 — Gateway model picker reads `/v1/models` from `ANTHROPIC_BASE_URL` automatically
02 — Host-managed Bedrock/Vertex/Foundry: analytics no longer auto-disabled
03 — `allowManagedDomainsOnly` security policy now enforces correctly across settings layers
04 — Agent SDK: no more hang on malformed tool name in parallel tool call batch

### Auth & Sessions cards
01 — OAuth credential race condition: concurrent writes no longer clear valid refresh token
02 — Org OAuth error: login screen replaced with "contact your admin" guidance
03 — Deferred tools (WebSearch/WebFetch) now load on first turn for `context: fork` subagents
04 — API retry countdown no longer sticks at "0s" between retries

### MCP & Remote Control cards
01 — claude.ai MCP connectors no longer suppressed by manual servers stuck in needs-auth state
02 — Remote control retries show result on each attempt (no more frozen "connecting…")
03 — Remote control failure notification now shows the actual error reason
04 — Plan-mode tools now available in `--channels` interactive sessions

### Terminal & Windows cards
01 — Trackpad scrolling speed fixed in Cursor and VS Code 1.92–1.104
02 — Japanese/Korean/Chinese text no longer garbled on Windows in no-flicker mode
03 — `Ctrl+L` redraws screen instead of clearing prompt (readline behavior restored)
04 — Windows clipboard: content no longer exposed in process args to EDR/SIEM; >22KB selections work

### Developer UX cards
01 — Spinner turns red in auto mode when a permission check stalls
02 — File-modified reminders bounded when linter touches many files at once
03 — `/plugin` Uninstall now reports "Uninstalled" (was "Enabled")
04 — PowerShell tool: bare `--` no longer mis-flagged as `--%` stop-parsing token

## Terminal Scene Pick
`$ claude update` — the CTA close (default)

## Hook Angle
Auth and sessions dominate: 4 coordinated fixes ship together — OAuth paste in terminal, timeout resilience, Mac sleep stability, remote session stability.

## WatchNext
Skipped (user choice).
