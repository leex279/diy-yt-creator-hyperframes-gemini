Claude Code v2.1.119, v2.1.120, v2.1.121, v2.1.122, v2.1.123 — five Claude Code updates from Anthropic stacked into one release recap. 32 new features, 71 bug fixes, 11 improvements: PowerShell replaces Git for Windows, claude ultrareview runs headless, /config finally persists, MCP alwaysLoad, PostToolUse hook output overrides, /resume by PR URL, Vertex AI X.509 Workload Identity, and the Bedrock service tier env var.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Key Changes in This Release:
- PowerShell replaces Git for Windows — `pwsh` fallback when Git isn't installed (v2.1.120)
- `claude ultrareview` — headless code review CLI, pipe findings to stdout from CI (v2.1.120)
- `/config` finally persists — writes to `~/.claude/settings.json` with project / local / policy precedence (v2.1.119)
- MCP `alwaysLoad: true` — flagged servers skip search-deferral and load immediately (v2.1.121)
- PostToolUse hooks override any tool's output via `hookSpecificOutput.updatedToolOutput` (v2.1.121)
- `/resume` by PR URL — find a session straight from a GitHub PR link (v2.1.122)
- `--from-pr` accepts GitLab, Bitbucket, and GitHub Enterprise URLs (v2.1.119)
- `claude plugin prune` — removes orphaned auto-installed plugin dependencies
- Tool search now finds MCP tools that connect after a session starts
- MCP servers with startup errors auto-retry up to 3 times
- LSP diagnostic summaries expand on click (no more inline dumps)
- Recent Activity panel removed for faster cold start
- Memory leak fixes — image processing, /usage on large transcripts, long-running tools
- Fullscreen scroll-jump fixed; iTerm2 + Ghostty scrollback duplication fixed
- Wrapped URLs in fullscreen now click through to the full URL
- `NO_PROXY` finally respected for all HTTP clients
- MCP+OAuth resilience — invalid responses no longer break the connection; 401 retry loop fixed
- Connector dedup — claude.ai connectors with the same URL deduplicated; `/mcp` flags duplicates
- Vertex AI X.509 Workload Identity Federation + count_tokens behind a proxy
- Bedrock service tier via `ANTHROPIC_BEDROCK_SERVICE_TIER` env var
- Settings stop getting invalidated by legacy enum values or a single malformed hooks entry
- Vim mode no longer pulls queued messages back on Esc
- `dangerously-skip-permissions` stops prompting on `.claude/` directory writes
- Plugins pinned by version constraints auto-update to the highest matching tag
- `mcp authenticate` supports redirect URI for custom-scheme completion

Chapters
0:00 Claude Code v2.1.119–v2.1.123 — 32 Features, 71 Fixes, 11 Improvements
0:30 Six Headline Changes: PowerShell, ultrareview, /config, MCP alwaysLoad, PostToolUse, /resume by PR
0:52 Headless & SDK: claude ultrareview, --from-pr (GitLab/Bitbucket), MCP redirect URI
1:16 Performance: Faster Cold Start, LSP Click-to-Expand, Memory Leak Fixes
1:39 Plugin System: claude plugin prune, MCP Auto-Retry, ToolSearch Finds Late MCP Tools
2:01 Terminal UI: Fullscreen Scroll Fix, iTerm2 + Ghostty Cleanup, Wrapped URL Clicks
2:19 Networking: NO_PROXY, MCP+OAuth Resilience, Vertex AI X.509, Bedrock Service Tier
2:56 $ claude update — Pull Every Fix

Resources:
- Release Notes (v2.1.119): https://github.com/anthropics/claude-code/releases/tag/v2.1.119
- Release Notes (v2.1.120): https://github.com/anthropics/claude-code/releases/tag/v2.1.120
- Release Notes (v2.1.121): https://github.com/anthropics/claude-code/releases/tag/v2.1.121
- Release Notes (v2.1.122): https://github.com/anthropics/claude-code/releases/tag/v2.1.122
- Release Notes (v2.1.123): https://github.com/anthropics/claude-code/releases/tag/v2.1.123
- Official Changelog (full inventory): https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- Curated Highlights (marckrenn): https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.123

To pull every fix in this video:
$ claude update

Which patch made your day — PowerShell-only Windows, the headless `claude ultrareview`, /resume by PR URL, or the MCP+OAuth retry-loop cleanup? Tell me below.

#ClaudeCode #ClaudeCodeUpdate #ClaudeCodeV2 #Anthropic #AICoding #MCP #PluginSystem #ToolSearch #PostToolUse #PowerShell #AIDevTools #AICodingAgent #AgenticAI #HeadlessCodeReview #DeveloperTools #DevTools #CLI #Terminal #ReleaseNotes #CodingAgent #SoftwareEngineering #ClaudeUpdate #AnthropicClaude #VertexAI #Bedrock
