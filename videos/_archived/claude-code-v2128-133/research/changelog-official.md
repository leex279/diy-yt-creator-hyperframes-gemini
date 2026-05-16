# Official Claude Code Changelog — v2.1.128 → v2.1.133

Source: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

> Note: v2.1.127 and v2.1.130 are not present in the upstream CHANGELOG (skipped releases).

## 2.1.133

- Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
- Added `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) to specify custom bubblewrap and socat binary locations
- Added `parentSettingsBehavior` admin-tier key (`'first-wins' | 'merge'`) to let admins opt SDK `managedSettings` (parent tier) into the policy merge
- Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read `$CLAUDE_EFFORT`
- Improved focus mode behavior
- Improved memory usage by releasing warm-spare background workers under memory pressure
- Fixed parallel sessions all dead-ending at 401 after a refresh-token race wiped shared credentials
- Fixed `Edit`/`Write` allow rules scoped to a drive root (`C:\`) or POSIX `/` matching incorrectly and always prompting
- Fixed an unhandled rejection (`ECOMPROMISED`) when a history or session-log file lock is compromised by clock skew or slow disk
- Fixed pressing Esc during conversation compaction showing a spurious "Error compacting conversation" notification
- Fixed `HTTP(S)_PROXY` / `NO_PROXY` / mTLS not being respected for the full MCP OAuth flow including discovery, dynamic client registration, token exchange, and token refresh
- Fixed Read/Write/Edit being denied on mapped network drives passed via `--add-dir` / SDK `additionalDirectories`
- Fixed Remote Control stop/interrupt from claude.ai not fully canceling the CLI session the same way local Esc does, causing queued messages to never advance after interrupting a stuck tool or prompt
- Fixed `/effort` in one session unexpectedly changing the effort level of other concurrent sessions, and a related issue where an IDE effort change could be silently dropped
- Fixed subagents not discovering project, user, or plugin skills via the Skill tool
- `claude --help` now lists `--remote-control` alongside `--remote-control-session-name-prefix`
- [VSCode] Fixed `claudeCode.claudeProcessWrapper` failing with "Unsupported platform" when the extension build doesn't bundle a Claude binary

## 2.1.132

- Added `CLAUDE_CODE_SESSION_ID` environment variable to the Bash tool subprocess environment, matching the `session_id` passed to hooks
- Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscreen alternate-screen renderer and keep the conversation in the terminal's native scrollback
- Added a "Pasting…" footer hint while a Ctrl+V image paste is being read from the clipboard
- Fixed external SIGINT (e.g. IDE stop button, `kill -INT`) not running graceful shutdown — terminal modes are now restored and the `--resume` hint is printed instead of an abrupt exit
- Fixed an uncaught exception when the terminal is closed or SSH disconnects mid-session under the native build
- Fixed `--resume` failing with `no low surrogate in string` when a tool error truncation split an emoji; pre-corrupted sessions are sanitized on load
- Fixed `--permission-mode` flag being ignored when resuming a plan-mode session with `-p --continue`/`--resume`, and plan mode not being re-applied after `ExitPlanMode` within the same session
- Fixed fullscreen mode showing a blank screen after laptop sleep/wake or Ctrl+Z/`fg` until the next keystroke or stream output
- Fixed cursor landing mid-grapheme on Ctrl+E/A/K/U/arrow keys when an Indic conjunct or ZWJ emoji wraps across lines
- Fixed vim operators corrupting text containing decomposed (NFD) accented characters
- Fixed pasting text starting with `/` silently swallowing the input or triggering an unknown-command reply
- Fixed pasting dumping stray escape sequences into the prompt when focus events or mouse-tracking reports interleave with the bracketed paste
- Fixed mouse wheel scrolling being too fast in Cursor and VS Code 1.92–1.104 due to an upstream xterm.js bug
- Fixed scroll-wheel handling in JetBrains IDE 2025.2 terminals (spurious arrow keys, wrong-direction events, runaway acceleration)
- Fixed `/usage` Ctrl+S hanging when copying the stats screenshot to the clipboard on Linux/X11
- Fixed `/terminal-setup` showing a contradictory error in Windows Terminal — Shift+Enter is natively supported there
- Fixed `/effort` picker not reflecting the `CLAUDE_CODE_EFFORT_LEVEL` env var override
- Fixed `/status` showing the wrong default model for some users
- Fixed slash command autocomplete popup being capped at ~3–5 visible commands instead of scaling with terminal height
- Fixed statusline `context_window` token counts reflecting cumulative session totals instead of current context usage
- Fixed Alt+T (thinking toggle) not working on macOS terminals without "Option as Meta" enabled (iTerm2, Terminal.app defaults)
- Fixed dead keyboard input on Windows after re-opening a background session from `claude agents`
- Fixed unbounded memory growth (10GB+ RSS) when a stdio MCP server writes non-protocol data to stdout
- Fixed MCP servers that connect but fail `tools/list` silently showing 0 tools — they now retry once and show "connected · tools fetch failed" in `/mcp`
- Fixed unauthorized claude.ai MCP connectors showing as "failed" instead of "needs auth", and headless `-p` mode retrying non-transient 4xx connection failures
- Improved visual consistency in slash command dialogs and `/login`, `/upgrade`, `/extra-usage` dialog spacing
- Updated the `/tui fullscreen` startup banner to describe additional renderer benefits (lower memory usage, mouse support, auto-copy on select)
- Fixed Bedrock and Vertex 400 errors when `ENABLE_PROMPT_CACHING_1H` is set

## 2.1.131

- Fixed VS Code extension failing to activate on Windows due to a hardcoded build path in the bundled SDK (`createRequire` polyfill bug)
- Fixed Mantle endpoint authentication failing with missing `x-api-key` header

## 2.1.129

- Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for the current session
- Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized output on terminals that auto-detection misses (e.g. Emacs `eat`)
- Added `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: when set on Homebrew or WinGet installations, Claude Code runs the upgrade command in the background and prompts to restart
- Plugin manifests: `themes` and `monitors` should now be declared under `"experimental": { ... }`. Top-level declarations still work but `claude plugin validate` will warn
- Gateway `/v1/models` discovery for the `/model` picker is now opt-in via `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (was automatic in 2.1.126–2.1.128)
- Ctrl+R history picker now defaults to searching all prompts across all projects, matching pre-2.1.124 behavior. Press Ctrl+S to narrow to the current project or session
- Third-party deployments (Bedrock, Vertex, Foundry, or `ANTHROPIC_BASE_URL` gateway) no longer see spinner tips pointing at first-party Anthropic surfaces
- `skillOverrides` setting now works: `off` hides from model and `/`, `user-invocable-only` hides from model only, `name-only` collapses description
- The `claude_code.pull_request.count` OTel metric now counts PRs/MRs created via MCP tools, not just shell commands
- Policy refusal error messages now include the API Request ID for easier support debugging
- Fixed API errors with unrecognized 400 status codes showing raw JSON instead of the underlying error message
- Fixed `/clear` not resetting the terminal tab title after a conversation
- Fixed session title chip from `/rename` disappearing while a permission or other dialog is active
- Fixed agent panel below the prompt being hidden when subagents are running (regression in 2.1.122)
- Fixed external-editor handoff (Ctrl+G) blanking the conversation history above the prompt
- Fixed `/context` dumping its rendered ASCII visualization grid into the conversation, wasting ~1.6k tokens per call
- Fixed `/agents` Library list arrow-key navigation: the highlighted agent now stays visible when the list exceeds the viewport
- Fixed `/branch` success message not including the new branch's session id for `/resume`
- Fixed bold headers with keycap/ZWJ/skin-tone emoji losing trailing characters in fullscreen mode
- Fixed server-managed settings policy not applying for enterprise/team users whose stored OAuth credentials lacked the `user:inference` scope
- Fixed OAuth refresh race after wake-from-sleep that could log out all running sessions
- Fixed 1-hour prompt cache TTL being silently downgraded to 5 minutes
- Fixed cache-miss warning appearing spuriously after `/clear` or compaction when changing `/effort` or `/model`
- Fixed `Bash(mkdir *)`, `Bash(touch *)` and similar allow rules not being honored for in-project paths
- Fixed `deniedMcpServers` patterns with a `*://` scheme wildcard not matching mixed-case hostnames
- Fixed harmless WebSocket warning being logged as an error in `--debug` during voice mode
- [VSCode] Fixed `/clear` not clearing the conversation context and displayed transcript

## 2.1.128

- Bare `/color` (no args) now picks a random session color
- `/mcp` now shows the tool count for connected servers and flags servers that connected with 0 tools
- `--plugin-dir` now accepts `.zip` plugin archives in addition to directories
- `--channels` now works with console (API key) authentication — console orgs with managed settings must set `channelsEnabled: true` to enable
- Updated `/model` picker: collapsed duplicate Opus 4.7 entries, and current Opus now shows as "Opus" instead of "Opus 4.7"
- Subprocesses (Bash, hooks, MCP, LSP) no longer inherit `OTEL_*` environment variables, so OTEL-instrumented apps run via the Bash tool no longer pick up the CLI's own OTLP endpoint
- MCP: `workspace` is now a reserved server name — existing servers with that name will be skipped with a warning
- Reconnecting MCP servers no longer flood the conversation with full tool-name lists on every reconnect — re-announced tools are summarized by server prefix
- SDK hosts now receive a persistent `localSettings` suggestion for Bash permission prompts, so "Always allow" writes to `.claude/settings.local.json`
- `EnterWorktree` now creates the new branch from local HEAD as documented, instead of `origin/<default-branch>` — unpushed commits are no longer dropped
- Auto mode: when the classifier can't evaluate an action, the error now includes a hint (retry, `/compact`, or run with `--debug`)
- Fixed focus mode briefly dimming the previous response when submitting a new prompt
- Fixed stray "4;0;" desktop notification on every `/exit` in Kitty and other terminals that interpret OSC 9 as a notification
- Fixed Remote Control showing an empty "Opening your options…" message on rate limit instead of actionable upsell options
- Fixed drag-and-drop image upload hanging on "Pasting text…" when the image read fails
- Fixed crash loop when piping very large input (>10 MB) to `claude -p` via stdin
- Fixed long URLs not being individually clickable on every wrapped row in fullscreen mode
- Fixed `/plugin` Components panel showing "Marketplace 'inline' not found" for plugins loaded via `--plugin-dir`
- Fixed MCP tool results dropping images when the server returns both structured content and content blocks
- Fixed fenced code blocks inside list items carrying leading whitespace into the clipboard on copy-paste
- Fixed tab navigation in `/config` stranding focus — the tab header now stays focused so arrows and Esc keep working
- Fixed markdown link labels being lost on terminals without OSC 8 hyperlink support — links now render as `label (url)` instead of just the URL
- Fixed sessions on 1M-context models with a smaller autocompact window being falsely blocked with "Prompt is too long" before reaching the actual API limit
- Fixed parallel shell tool calls: a failing read-only command (grep, git diff, ls) no longer cancels sibling calls
- Fixed banner showing "with X effort" on models that don't support effort
- Fixed `/fast` on 3P providers fuzzy-matching to an unrelated skill instead of showing "not available"
- Fixed Bedrock default model resolving to `global.*` instead of the region-appropriate prefix
- Fixed vim mode: `Space` in NORMAL mode now moves the cursor right, matching standard vi/vim behavior
- Fixed terminal progress indicator (OSC 9;4) flickering off between tool calls — stays visible across the full turn
- Fixed `/rename` without args failing on resumed sessions whose last entry is a compact boundary
- Fixed stale "remote-control is active" status lines from prior sessions appearing after `--resume`/`--continue`
- Fixed stale `installed_plugins.json` entries pointing at deleted cache directories polluting PATH
- Fixed MCP stdio servers receiving corrupted arguments when `CLAUDE_CODE_SHELL_PREFIX` is set and an argument contains spaces or shell metacharacters
- Fixed sub-agent progress summaries missing the prompt cache (~3× `cache_creation` reduction)
- Fixed `/plugin update` never detecting new versions of npm-sourced plugins
- Fixed sub-agent summaries firing repeatedly while a sub-agent's transcript is static, capping worst-case token cost on idle sub-agents
- Headless `--output-format stream-json`: `init.plugin_errors` now includes `--plugin-dir` load failures in addition to dependency demotions
