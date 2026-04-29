# Marckrenn curated highlights — v2.1.119 / v2.1.120 / v2.1.121

Source: `https://github.com/marckrenn/claude-code-changelog/releases/tag/<v>`
Fetched: 2026-04-28.

## v2.1.121 Highlights

- Added MCP server option `alwaysLoad`: when true, that server's tools skip search deferral and load immediately
- Bash tool drops shell state between runs and adds rerun-footer tokens, so commands don't share prior context
- PostToolUse hooks can replace output for all tools, letting hooks override tool results (was MCP-only)

## v2.1.120 Highlights

- `claude ultrareview` runs `/ultrareview` headless in CI/scripts and prints findings to stdout for CI capture
- Automated rule reviewer evaluates classifier rules for clarity, catching ambiguous rules before deployment
- Fixed `DISABLE_TELEMETRY` so it suppresses usage metrics for API and enterprise, restoring opt-out

## v2.1.119 Highlights

- CLI `/config` now persists to `~/.claude/settings.json` and obeys project/local/policy override precedence
- Edits must be submitted via Edit tool as one parallel msg, keeping section headers and italic templates intact
- Memory-synthesis extracts code-query facts with fact/sent caps to limit context and bound tokens
