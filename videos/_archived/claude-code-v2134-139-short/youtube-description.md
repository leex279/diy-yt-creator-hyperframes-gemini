You can check out Dynamous AI here: https://dynamous.ai/?code=646a60. 10% off applies automatically when you join through this link! 👇

Claude Code v2.1.134 – v2.1.139 just shipped: agent view (Research Preview), /goal command, autoMode hard_deny, transcript keyboard navigation, claude plugin details, MCP OAuth concurrent-refresh fix, smarter compaction, claude auth deadlock fix, and /mcp hot reload. 9 new features, 73 bug fixes, 14 improvements — across six Claude Code updates in one short.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Key Changes in This Release:
- **Agent view (v2.1.139)** — `claude agents` lists every Claude Code session running, blocked, or done. First-ever multi-session dashboard.
- **`/goal` command (v2.1.139)** — set a completion condition; Claude keeps working across turns with live elapsed time, turn count, and tokens until it's met.
- **`autoMode.hard_deny` (v2.1.136)** — unconditional block rules that the classifier cannot override. Hard safety lever for auto mode.
- **Transcript view navigation (v2.1.139)** — `?` for keyboard shortcuts, `{` / `}` to jump between user prompts, `v` to toggle the shortcut panel.
- **`claude plugin details <name>` (v2.1.139)** — see a plugin's component inventory AND projected per-session token cost before installing.
- **MCP OAuth refresh fix (v2.1.136)** — concurrent refreshes across multiple MCP servers no longer drop tokens; multi-server setups stop forcing a daily re-auth.
- **Smarter compaction (v2.1.139)** — compaction prompt now asks the model to preserve sensitive user instructions. Long sessions stop losing intent on trim.
- **`claude auth` deadlock fixed (v2.1.139)** — expired credentials no longer block `claude auth login`, `logout`, and `status`.
- **`/mcp` hot reload (v2.1.139)** — `/mcp` Reconnect now picks up `.mcp.json` edits without a CLI restart.
- **Hook `args: string[]` exec form (v2.1.139)** — spawn the command directly without a shell.
- **Hook `continueOnBlock` config (v2.1.139)** — feed rejection reasons back to Claude on `PostToolUse`.
- **MCP `CLAUDE_PROJECT_DIR` env (v2.1.139)** — stdio MCP servers now receive the project directory automatically.
- **VS Code Windows activation fixed (v2.1.137)** — extension startup restored on Windows.

Chapters
0:00 9 Features / 73 Fixes / 14 Improvements (v2.1.134 – v2.1.139)
0:09 Top 9 Changes: Agent View, /goal, hard_deny + 6 More
1:44 Dynamous AI Mastery Community

Resources:
- Claude Code Releases (v2.1.134 – v2.1.139): https://github.com/anthropics/claude-code/releases
- Anthropic Claude Code CHANGELOG.md: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- Claude Code v2.1.139 curated highlights (marckrenn): https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.139
- Claude Code v2.1.136 curated highlights (marckrenn): https://github.com/marckrenn/claude-code-changelog/releases/tag/v2.1.136

To pull every fix in this video:
$ claude update

Which patch matters most — agent view, /goal, or hard_deny? Drop a comment below.

#ClaudeCode #ClaudeCodeUpdate #ClaudeCodeAgents #ClaudeCodeSubagents #Anthropic #AICoding #AICodingAgent #AIAgents #AgenticAI #MCP #ClaudeAI #AIAutomation #DevTools #VSCode #AIShorts #Shorts
