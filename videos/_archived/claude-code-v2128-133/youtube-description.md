Claude Code v2.1.128 → v2.1.133 ships 110 changes in six releases — 28 new features, 78 bug fixes, and 4 improvements. Here's every change in under 5 minutes: MCP got a stability pass, hooks now read $CLAUDE_EFFORT, --plugin-url installs plugins from URLs, and subagents finally find skills again.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Key Changes in This Release:
- worktree.baseRef setting — choose `fresh` (origin/default) or `head` (local HEAD) for new --worktree, EnterWorktree, and agent-isolation worktree base branches
- --plugin-url <url> flag — fetch a plugin .zip archive from any URL for the current session, no install required
- $CLAUDE_EFFORT in hooks + Bash — hooks now receive the active effort level via effort.level JSON input and Bash subprocesses can read $CLAUDE_EFFORT
- CLAUDE_CODE_SESSION_ID env var — Bash tool subprocesses get a session ID matching the hook session_id, enabling tool-level session tracing
- CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 — keep the conversation in your terminal's native scrollback instead of fullscreen alternate screen
- Subagent skill discovery — regression patched, subagents now find project, user, and plugin skills through the Skill tool
- MCP stability pass — re-announced tools summarized by server prefix, failed tools/list servers retry once, 10 GB+ stdio RSS leak fixed, MCP OAuth honors HTTP(S)_PROXY / NO_PROXY / mTLS
- OAuth refresh-token race — parallel sessions all dead-ending at 401 after refresh wiped shared credentials — patched
- 1-hour prompt cache TTL was being silently downgraded to 5 minutes — now honored
- Bedrock + Vertex 400 errors with ENABLE_PROMPT_CACHING_1H — patched
- VS Code extension activation on Windows — hardcoded build path fixed (v2.1.131)
- Mantle endpoint authentication missing x-api-key header — restored (v2.1.131)

Chapters
0:00 Claude Code v2.1.128–v2.1.133: 6 Releases, 28 Features, 78 Fixes — MCP Stability Pass
0:44 Six Headline Changes — worktree.baseRef, --plugin-url, CLAUDE_EFFORT, Subagent Skills
1:38 Hooks & Power-User APIs — $CLAUDE_EFFORT in Hooks + Bash + CLAUDE_CODE_SESSION_ID
2:18 Auth, OAuth & Sessions — 401 Refresh-Token Race + Wake-from-Sleep Logout Patched
2:49 Plugins, MCP & Skills — --plugin-url Flag + 10 GB stdio Memory Leak Fixed
3:28 Terminal UI & Editors — CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN + Cursor/VS Code Wheel
4:07 Network, Proxy & API — MCP OAuth Honors HTTP(S)_PROXY + mTLS, Bedrock + Vertex
4:42 Run claude update — That's All It Takes

Resources:
Release Notes (v2.1.133 — official): https://github.com/anthropics/claude-code/releases/tag/v2.1.133
Curated Changelog (marckrenn — v2.1.133 highlights): https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.133
Full Claude Code CHANGELOG.md: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
Claude Code Docs (how to use Claude Code): https://code.claude.com/docs/en/overview
Claude Code MCP Setup Guide: https://code.claude.com/docs/en/mcp

To pull every change in this video:
$ claude update

Which patch made your day — the hooks effort variable, the subagent skill fix, or the 10 GB MCP memory leak?

#ClaudeCode #ClaudeCodeUpdate #ClaudeCode21 #AnthropicClaude #ClaudeCodeMCP #ClaudeCodeSubagents #ClaudeCodeAPI #ClaudeCodeTutorial #ClaudeCodeHooks #ClaudeCodePlugins #MCPServers #ModelContextProtocol #ClaudeAI #AnthropicAI #AICoding #AICodingAgent #AICodingAssistant #CodingWithAI #ClaudeCodeSkills #ClaudeUpdate #ClaudeCodeChangelog #ClaudeCodeReleaseNotes #DevTools2026 #AIDeveloperTools #ClaudeCodeFixes
