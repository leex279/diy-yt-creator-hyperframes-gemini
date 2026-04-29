# Claude Code official CHANGELOG — v2.1.119, v2.1.120, v2.1.121

Source: `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md`
Fetched: 2026-04-28.

## v2.1.121

- Added `alwaysLoad` option to MCP server config for tools that skip deferral
- Added `claude plugin prune` to remove orphaned auto-installed dependencies
- Added type-to-filter search box to `/skills` for easier discovery
- PostToolUse hooks can now replace tool output via `hookSpecificOutput.updatedToolOutput`
- Fullscreen mode: typing no longer jumps scroll after scrolling up
- Dialogs that overflow terminal are now scrollable with arrow keys and mouse wheel
- Clicking wrapped URLs in fullscreen mode now opens the full URL
- SDK and `claude -p`: `CLAUDE_CODE_FORK_SUBAGENT=1` works in non-interactive sessions
- `--dangerously-skip-permissions` no longer prompts for `.claude/` directory writes
- `/terminal-setup` enables iTerm2 clipboard access for `/copy`
- MCP servers with startup errors now auto-retry up to 3 times
- Terminal tab session title generated in configured language setting
- Claude.ai connectors with same URL are deduplicated
- Vertex AI supports X.509 certificate-based Workload Identity Federation
- Faster startup after upgrading by removing Recent Activity panel
- LSP diagnostic summaries expand on click with hint display
- SDK: `mcp_authenticate` supports `redirectUri` for custom scheme completion
- OpenTelemetry: added `stop_reason` and related fields to LLM request spans
- VSCode: voice dictation respects `accessibility.voice.speechLanguage` setting
- VSCode: `/context` opens native token usage dialog
- Fixed unbounded memory growth when processing many images
- Fixed `/usage` memory leak on machines with large transcript histories
- Fixed memory leak when long-running tools fail to emit progress
- Fixed Bash tool becoming unusable when working directory is deleted
- Fixed `--resume` crashing on startup in external builds
- Fixed `--resume` failing on large sessions with corrupted transcript lines
- Fixed thinking type error when using Bedrock inference profiles
- Fixed Microsoft 365 MCP OAuth duplicate parameter error
- Fixed scrollback duplication in non-fullscreen mode on various terminals
- Fixed claude.ai MCP connectors disappearing on transient auth errors
- Fixed "Always allow" rules not surviving worker restarts in remote sessions
- Fixed `NO_PROXY` not being respected for all HTTP clients
- Fixed managed settings approval prompt exiting session
- Fixed `/usage` rate limit errors with stale OAuth tokens
- Fixed invalid legacy enum values invalidating entire settings file
- Fixed `/usage` dialog clipping in no-flicker mode
- Fixed `/focus` showing unknown command error
- Fixed embedded grep/find/rg wrappers failing when binary is deleted
- Reduced peak file descriptor usage during `find` on large directories

## v2.1.120

- Windows: Git for Windows no longer required; PowerShell used as fallback
- Added `claude ultrareview [target]` for non-interactive code review from CI/scripts
- Skills reference effort level with `${CLAUDE_EFFORT}` variable
- Set `AI_AGENT` environment variable for subprocesses attribution
- Spinner tips hidden when desktop app or skills/agents already installed
- Added "use PgUp/PgDn to scroll" hint for arrow-key scroll events
- Faster session start with many claude.ai connectors
- Auto mode denial message links to configuration docs
- `claude plugin validate` accepts top-level schema and version fields
- Auto-compact displays `auto` instead of misleading token value
- Fixed MCP stdio tool call closing entire connection on Esc
- Fixed `/rewind` overlay keyboard input regression
- Fixed terminal scrollback duplication in non-fullscreen mode
- Fixed `DISABLE_TELEMETRY` not suppressing usage metrics
- Fixed false-positive "Dangerous rm" prompts in auto mode
- Fixed long selection menus clipping below terminal in fullscreen
- Fixed Write tool output collapsing instead of expanding
- Fixed slash command picker jumping and highlight matching
- Fixed `/plugin` marketplace failing when entry uses unrecognized format
- VSCode: `/usage` opens native Account & Usage dialog
- VSCode: voice dictation respects language setting
- Fixed `find` exhausting file descriptors on large trees

## v2.1.119

- `/config` settings now persist to `~/.claude/settings.json` with precedence
- Added `prUrlTemplate` setting for custom code-review URLs
- Added `CLAUDE_CODE_HIDE_CWD` to hide working directory in startup logo
- `--from-pr` accepts GitLab, Bitbucket, and GitHub Enterprise URLs
- `--print` mode honors agent `tools:` and `disallowedTools:` frontmatter
- `--agent <name>` honors agent's `permissionMode` setting
- PowerShell tool commands can be auto-approved in permission mode
- Hooks include `duration_ms` for tool execution time
- Subagent MCP server reconfiguration connects servers in parallel
- Plugins pinned by constraints auto-update to highest satisfying tag
- Vim mode: Esc in INSERT no longer pulls queued message back
- Slash command suggestions highlight matched characters
- Slash command picker wraps long descriptions to second line
- `owner/repo#N` links use git remote's host instead of github.com
- `blockedMarketplaces` correctly enforces `hostPattern` and `pathPattern`
- OpenTelemetry: `tool_result` and `tool_decision` include `tool_use_id`
- Status line: stdin JSON includes `effort.level` and `thinking.enabled`
- Fixed CRLF paste inserting extra blank lines
- Fixed multi-line paste losing newlines with kitty keyboard protocol
- Fixed Glob and Grep tools disappearing when Bash tool denied
- Fixed scrolling up snapping back to bottom in fullscreen
- Fixed MCP HTTP connections failing with invalid OAuth responses
- Fixed Rewind showing "(no prompt)" for image attachments
- Fixed auto mode overriding plan mode instructions
- Fixed async PostToolUse hooks with no response writing empty entries
- Tool search disabled by default on Vertex AI
- Fixed `@`-file Tab completion replacing entire prompt
- Fixed stray `p` character appearing at prompt on macOS via Docker
- Fixed `${ENV_VAR}` placeholders in MCP server headers
- Fixed MCP OAuth client secret not sent during token exchange
- Fixed `/skills` Enter key opening dialog instead of pre-filling
- Fixed `/agents` detail view mislabeling unavailable tools
- Fixed MCP servers not spawning when plugin cache incomplete
- Fixed `/export` showing current default model instead of actual
- Fixed verbose output setting not persisting
- Fixed `/usage` progress bar overlapping labels
- Fixed plugin MCP servers failing with `${user_config.*}` references
- Fixed list items wrapping final numbers onto separate line
- Fixed `/plan` not acting on existing plan in plan mode
- Fixed skills re-executed against next message after auto-compaction
- Fixed `/reload-plugins` and `/doctor` reporting disabled plugin errors
- Fixed Agent tool worktree reuse from prior sessions
- Fixed disabled MCP servers appearing as "failed"
- Fixed `TaskList` returning tasks in arbitrary order
- Fixed spurious "GitHub API rate limit exceeded" hints
- Fixed SDK `read_file` not enforcing size cap correctly
- Fixed PR not linked when working in git worktree
- Fixed `/doctor` warning about MCP overrides
- Windows: removed false-positive MCP config warning
- VSCode: fixed voice dictation producing nothing on macOS
