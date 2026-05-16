# Claude Code Official Changelog — v2.1.134 → v2.1.139

Captured 2026-05-11 from `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`.

## 2.1.139

- Added agent view (Research Preview): a single list of every Claude Code session — running, blocked on you, or done. Run `claude agents` to get started
- Added `/goal` command: set a completion condition and Claude keeps working across turns until it's met
- Added `/scroll-speed` command to tune mouse wheel scroll speed with a live preview
- Added `claude plugin details <name>` to show a plugin's component inventory and projected per-session token cost
- Added transcript view navigation: `?` for keyboard shortcuts, `{`/`}` to jump between user prompts, `v` to toggle shortcut panel
- Added hook `args: string[]` field (exec form) that spawns the command directly without a shell
- Added hook `continueOnBlock` config option for `PostToolUse` — set to `true` to feed rejection reason back to Claude
- MCP stdio servers now receive `CLAUDE_PROJECT_DIR` in their environment
- Compaction prompt now asks the model to preserve sensitive user instructions
- `/mcp` Reconnect now picks up `.mcp.json` edits without a restart
- `/context all` per-skill token estimates now account for the model's tokenizer
- `claude plugin install <name>@<marketplace>` now auto-refreshes the marketplace and retries
- `/plugin` installed-plugin details now show hook event names and MCP server names cleanly
- `/context` now shows the providing plugin's name for plugin-sourced skills
- Remote MCP server reconnect retry on transient failures is now enabled for all users
- API requests from subagents now carry `x-claude-code-agent-id` / `x-claude-code-parent-agent-id` headers
- Remote Control, `/schedule`, claude.ai MCP connectors, and notification preferences disabled when API key is set
- Fixed a deadlock where expired credentials blocked `claude auth login`/`logout`/`status`
- Fixed `autoAllowBashIfSandboxed` not auto-approving commands with shell expansions like `$VAR` and `$(cmd)`
- Fixed a bug where a hook writing to the terminal could corrupt an on-screen interactive prompt
- Fixed unbounded memory growth when an HTTP/SSE MCP server streams non-protocol data
- Fixed `Skill(name *)` permission rules — the wildcard form now works as a prefix match
- Fixed settings hot-reload not detecting edits to symlinked `~/.claude/settings.json`
- Fixed plugin details failing to load when the marketplace key differs from the manifest name
- Fixed `/model` picker "Default" row not reflecting environment variable overrides
- Fixed spurious "stream idle timeout" 5 minutes after a response completed
- Fixed silent `exit 1` when 10+ MCP servers are configured and the cache directory is unwritable
- Fixed a typing cursor blinking on tab names, list pointers, and select rows in dialogs
- Fixed transcript view letter shortcuts not working after mouse click
- Fixed Bash-mode up-arrow history repeating the first entry and clobbering the in-progress draft
- Fixed pasting or dropping multiple images only inserting the last one
- Fixed hyperlinks using unreadable dark navy on dark themes
- Fixed model picker showing a redundant "Current model" row for third-party users
- Fixed legacy Opus picker entry on PAYG 3P providers resolving to the same model as the default entry
- Fixed mouse wheel scrolling speed in Cursor and VS Code 1.92–1.104
- Fixed scroll behavior in Windows Terminal and VS Code when attached to background sessions
- Fixed MCP resources from disconnected servers lingering in `@server:` autocomplete
- Fixed two-file diff snippets over-reporting the number of truncated lines by one
- Fixed Grep results not relativizing Windows drive-letter paths
- Fixed border-embedded text overflowing on CJK/emoji due to visual cell width miscalculation
- Fixed fuzzy-match highlighting splitting emoji and astral-plane characters mid-pair
- Fixed skill argument names containing regex metacharacters breaking argument substitution
- Fixed ProgressBar rendering a full block for an almost-full fractional cell
- Fixed task polling and `fs.watch` being resurrected when the last subscriber leaves
- Fixed plugin dependency resolution leaving a stale count when the manifest name differs
- Fixed Insights Time-of-Day chart skewing when a session has an unparseable timestamp
- Fixed keybindings using only the cmd/super/win modifier being flagged as unparseable
- Fixed `claude_code.active_time.total` OpenTelemetry metric not being emitted in `--print` mode
- Fixed `claude plugin update` not preserving cross-plugin symlinks inside a marketplace
- [VSCode] Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab

## 2.1.138

- Internal fixes

## 2.1.137

- [VSCode] Fixed extension failing to activate on Windows

## 2.1.136

- Added `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` to re-enable session quality survey for enterprises
- Added `settings.autoMode.hard_deny` for auto mode classifier rules that block unconditionally
- Fixed MCP servers silently disappearing after `/clear` in VS Code extension, JetBrains plugin, and Agent SDK
- Fixed a rare login loop where a concurrent credential write could overwrite a freshly-rotated OAuth token
- Fixed MCP OAuth refresh tokens being lost when multiple servers refresh concurrently
- Fixed an API error (400) when extended thinking emitted a redacted thinking block after a tool call
- Fixed `--resume` / `--continue` not finding sessions when the project path contains underscores
- Fixed plan mode not blocking file writes when a matching `Edit(...)` allow rule exists
- WSL2: image paste from Windows clipboard now works via a PowerShell fallback
- Fixed plugin `Stop`/`UserPromptSubmit` hooks failing when cache cleanup deletes a version still in use
- Improved visual consistency across slash command dialogs
- Fixed colors appearing at wrong positions in bash command output and markdown code blocks
- Fixed ReasonML diffs rendering corrupted "undefined" text artifacts at word-diff boundaries
- Fixed worktree exit dialog warning about uncommitted files in the wrong directory
- Fixed `@` file picker not matching files created mid-session in small non-git directories
- Fixed `@`-mention file picker not finding files in directories with more than 100 entries
- Fixed failed tool calls not being click-to-expand in fullscreen mode when their output was truncated
- Fixed Backspace and Ctrl+Backspace getting swapped after using Ctrl+G to open an external editor
- Fixed `/usage` weekly reset showing time of day instead of the calendar date
- Fixed welcome banner ellipsis causing column overflow on CJK terminals
- Fixed `/insights` crash when session history contains tool calls with malformed input fields
- Fixed a renderer crash when a tool's collapsibility classification changes mid-session
- Fixed a `skills` entry in `plugin.json` hiding the plugin's default `skills/` directory
- Fixed IDE shell-integration lock files not respecting `CLAUDE_CONFIG_DIR`
- Fixed trailing whitespace in copied terminal output during streaming
- Fixed plugin uninstall and enable/disable not matching slugs case-insensitively
- Fixed tool error truncation marker showing a negative count for surrogate-pair strings
- Fixed env vars from `CLAUDE_ENV_FILE` SessionStart hooks going stale after `/resume` or `/clear`
- Fixed `/branch` saving a multi-line session title when given a pasted multi-line name
- Fixed a stray leading space on the second line of wrapped text at the column boundary
- Fixed Esc not dismissing dialogs in `/install-github-app`, `/desktop`, `/resume`, and `/web-setup`
- Fixed `/doctor` MCP schema errors not naming the missing field or showing the source file path
- Fixed Bash permission prompts showing an internal parser diagnostic instead of user-readable explanation
- Fixed plugin slash commands with spaces not resolving to their namespaced form
- Fixed `AskUserQuestion` discarding multi-select answers when supplied as an array
- Fixed `/clear <name>` not labeling the cleared session for `/resume`
- Fixed `CronList` output missing qualifiers and the scheduled prompt
- Fixed "Jump to bottom" overlay leaving color artifacts on CJK characters in fullscreen mode
- Fixed wide markdown tables leaving a stale bordered render in terminal scrollback while streaming
- Fixed pasted text being silently dropped when a long prompt with a pasted-text placeholder was auto-truncated
- Fixed `/release-notes` getting stuck on an old version after a failed changelog refresh
- Fixed `/mcp` server list not scrolling when there are more servers than fit in the terminal
- Fixed mid-input slash command autocomplete not working after an initial slash command
- Fixed scrolling to bottom re-engaging auto-follow with `autoScrollEnabled: false`
- Fixed prompt suggestions being auto-submitted by Enter on an empty input
- Fixed keyboard shortcut hints not reflecting rebound keys from `keybindings.json`
- Fixed `/settings` language change being reverted on Escape after confirming
- Fixed `/terminal-setup` only appearing in autocomplete on exact name match
- Fixed "Chat about this" on an `AskUserQuestion` dialog erasing the question text
- Fixed MCP tool results being invisible when the server returns content blocks
- Improved error message when `--worktree` collides with an existing or stale worktree
- Changed plugin marketplace removal key to `d` (matching delete elsewhere) instead of `r`

## 2.1.135

*(No changelog entry found upstream)*

## 2.1.134

*(No changelog entry found upstream)*
