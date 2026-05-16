# marckrenn highlights — Claude Code v2.1.128 → v2.1.133

Curated, narrative-friendly highlights from https://github.com/marckrenn/claude-code-changelog

## v2.1.133

- Risky-action confirmations removed; approved actions now auto-run; speeds automation; drops per-action checks
- worktree.baseRef picks --worktree/agent-isolation base: origin/ vs local HEAD; affects local commits
- Hooks and Bash tools get active effort via effort.level and $CLAUDE_EFFORT so they can adapt behavior/logging

## v2.1.132

- Bash subprocesses now get CLAUDE_CODE_SESSION_ID matching hook session_id, enabling tool-level session tracing
- Added CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 to disable fullscreen alternate screen and keep native scrollback
- Risky-action confirmation policy moved to top of system prompt; checks now run before other instructions

## v2.1.131

- VS Code extension activates on Windows after fixing hardcoded build path in the bundled SDK
- Fixed Mantle endpoint failing authentication when x-api-key header was missing, restoring API requests

## v2.1.129

- Added --plugin-url flag to fetch a plugin .zip from a URL for quick session-only installs
- Policy refusal error messages now include the API Request ID, enabling faster tracing and support debugging
- Spinner tips in third-party deployments no longer point at Anthropic surfaces, avoiding first-party UI cues

## v2.1.128

- EnterWorktree creates branches from local HEAD instead of origin/, preserving unpushed commits
- Subprocesses no longer inherit OTEL_* vars, so OTEL-instrumented apps won't send traces to CLI OTLP endpoint
- MCP reconnects now summarize re-announced tools by server prefix to avoid flooding chats with full tool lists
