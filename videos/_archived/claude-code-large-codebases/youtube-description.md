Claude Code in a large codebase — Anthropic just published their own playbook. Five extension points, two capabilities, three patterns: CLAUDE.md, hooks, skills, plugins, MCP servers, LSP, and subagents. The harness matters more than the model. Part 1 of Claude Code at scale.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

What's covered in this video:
- The harness-over-model thesis — why Anthropic says the ecosystem around the model decides Claude Code's performance at scale
- The 7-component harness: 5 extension points (CLAUDE.md, hooks, skills, plugins, MCP servers) + 2 capabilities (LSP integrations, subagents)
- Why Claude Code uses agentic search instead of RAG retrieval — and how RAG embedding pipelines fail in active monorepos (stale renames, deleted modules, index lag)
- The build order Anthropic insists on: CLAUDE.md first, MCP last — and why teams that start with MCP servers are making the most common mistake
- Pattern 1 (Navigability): the 6 sub-patterns from the article — lean + layered CLAUDE.md, subdirectory init, scoped tests/lint, .gitignore + permissions.deny in .claude/settings.json, codebase maps, and LSP for symbol-not-string search
- Pattern 2 (Maintenance): the 3–6 month CLAUDE.md review cadence + the redundant p4 edit hook example
- Pattern 3 (Ownership): the emerging agent-manager role (hybrid PM/engineer), DRI as the minimum viable owner, and the cross-functional working group (engineering + info-sec + governance)
- Customer anecdotes from Anthropic's Applied AI team: a large retail org's internal-analytics plugin, an enterprise software company that deployed LSP org-wide for C / C++, and two day-one rollouts with dedicated tooling teams
- Languages Anthropic explicitly names as working well at scale: C, C++, C#, Java, PHP
- Edge cases the article does NOT cover (hundreds-of-thousands of folders, millions of files, non-git VCS) — promised for future installments of Claude Code at scale

Chapters
0:00 The Harness Playbook: 5 Extension Points, 2 Capabilities, 3 Patterns
0:26 Anthropic's Applied AI Team — Where the Claude Code at Scale Series Came From
0:59 Multi-Million-Line Monorepos & Thousands of Developers (C / C++ / C# / Java / PHP)
1:29 Why Agentic Search Beats RAG Retrieval at Scale (No Embedding Index)
2:14 The 7-Component Harness Diagram — CLAUDE.md First, MCP Last
2:52 Extension Points & Capabilities Explained: CLAUDE.md, Hooks, Skills, Plugins, MCP, LSP, Subagents
4:32 Pattern 1 — Make the Codebase Navigable: 6 Sub-Patterns (.gitignore, permissions.deny, Codebase Maps, LSP)
5:51 Pattern 2 — Maintain CLAUDE.md as Models Evolve (3–6 Month Review Cadence)
6:25 Pattern 3 — Ownership, the Agent Manager Role & Cross-Functional Working Group
7:37 The Getting Started Checklist + Edge Cases Promised for Future Installments
8:20 Harness or Model — Which One Is Doing the Work?

Resources:
- 📝 Source article (Anthropic — Claude Code at Scale, Part 1): https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
- 📚 Claude Code documentation (overview): https://code.claude.com/docs/en/overview
- 🔧 Claude Code Skills documentation: https://code.claude.com/docs/en/skills
- 📖 CLAUDE.md & Memory documentation: https://code.claude.com/docs/en/memory
- 🪝 Claude Code Hooks reference: https://code.claude.com/docs/en/hooks
- 🔌 Model Context Protocol (MCP): https://modelcontextprotocol.io

Key Concepts:
- Harness — the ecosystem of CLAUDE.md files, hooks, skills, plugins, and MCP servers that wraps the Claude model. Per Anthropic: the harness decides how Claude Code performs more than the model itself.
- CLAUDE.md — markdown context files Claude Code reads automatically at the start of every session. Lean + layered: a root file for the big picture, subdirectory files for local conventions.
- Agentic search — Claude Code's codebase navigation pattern: file traversal + grep + reference-following, no embedding index, no central RAG retrieval. Avoids index-lag failures from renames and deletes in active codebases.
- Skills — progressive-disclosure expertise that loads on demand. Path-scopable so a security-review skill only fires when Claude works on relevant code.
- MCP servers — Model Context Protocol integrations that expose structured search, internal docs, and ticketing as tools Claude can call. Anthropic says: build them LAST, not first.
- LSP integrations — Language Server Protocol bindings that give Claude symbol-level navigation. Grep for a common function name returns thousands of matches; LSP returns only the references that point to the same symbol.
- Subagents — isolated Claude instances with their own context that take a task, do the work, and return only the final result to the parent.
- Agent manager — emerging hybrid PM/engineer role dedicated to running the Claude Code ecosystem inside an organization. The minimum viable version is a DRI (Directly Responsible Individual) with authority over settings, permissions, and CLAUDE.md conventions.

Anthropic says the harness matters more than the model. Do you buy it — or is it still mostly Claude doing the heavy lifting? Harness or model — which one is doing the work? Drop your pick below.

#ClaudeCode #Claude #Anthropic #AITools #AIAgents #CLAUDEmd #LargeCodebase #Monorepo #EnterpriseAI #ClaudeMdBestPractices #ClaudeSkills #ClaudePlugins #MCPServers #ModelContextProtocol #LanguageServerProtocol #LSP #Subagents #AgenticCoding #AICoding #ClaudeCodeBestPractices #ClaudeCodeAtScale #DevExperience #SoftwareEngineering
