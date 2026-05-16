Agent Skills explained in under 3 minutes — the open standard for AI agent capabilities, originally developed by Anthropic and now supported by 37+ tools including Claude Code, VS Code, Cursor, GitHub Copilot, Gemini CLI, OpenAI Codex, and more.

A skill is one folder. Inside lives one file: SKILL.md. That file holds two fields — a name and a description — plus the instructions an agent follows to do the work. Optional sub-folders (scripts/, references/, assets/) let you bundle executable code, reference docs, and templates the agent loads only when the task demands them.

The magic is **progressive disclosure**: agents load only the name + description (~100 tokens) at startup. When your task matches the description, the full SKILL.md (under 5,000 tokens) loads into context. Bundled scripts and reference files load only when the work demands them. Many skills. Tiny context footprint.

This is what makes Agent Skills different from a custom plugin or an SDK: no DSL, no SDK, just a Markdown file you commit to your Git repo. Build it once. Use it in every skills-compatible agent. Zero rewrites.

📚 The spec: https://agentskills.io
📖 Full format reference: https://agentskills.io/specification
🚀 Quickstart (VS Code + GitHub Copilot): https://agentskills.io/skill-creation/quickstart
🛠 Best practices: https://agentskills.io/skill-creation/best-practices
👥 Client showcase (37+ tools): https://agentskills.io/clients

⚙️ Build a real skill that runs in Claude Code, OpenAI Codex, Cursor, VS Code Copilot, Gemini CLI, and more — all from the same `SKILL.md`.

▼ CHAPTERS

0:00 Agent Skills — the open standard, built by Anthropic
0:11 A skill is one folder, one file
0:25 Three optional directories: scripts/ · references/ · assets/
0:41 Progressive disclosure — the three stages
1:11 What a real SKILL.md looks like (with all the optional fields)
1:30 Token budget — 100 / 5,000 / 0
1:41 Where you can use it — Claude Code, Cursor, VS Code, OpenAI Codex + 31 more
1:52 Originally developed by Anthropic, released as an open standard
2:01 The debate

▼ TIMESTAMPS RELATIVE TO 1.0× — RENDERED AT 1.0× (no ffmpeg speedup)

----

🎓 New to building with Claude Code, Cursor, OpenAI Codex, and the rest? Learn the workflow inside the Dynamous AI community — agentic coding curriculum, weekly office hours, and a builder-first Discord.

→ https://dynamous.ai (10% off in the link)

----

▼ ABOUT THIS VIDEO

This is a 2-minute deep-explainer Short on the Agent Skills open standard — what it is, how progressive disclosure works, the SKILL.md format, the token economics, and the 37+ tools that already adopt it. Sourced verbatim from agentskills.io (home, specification, quickstart).

If you build with AI agents — Claude Code, OpenAI Codex, Cursor, VS Code Copilot, Gemini CLI, GitHub Copilot, Goose, Letta, Kiro, or any other skills-compatible client — this is the format you'll keep reaching for.

▼ THE DEBATE — drop your pick below

Skills, or MCP — which one earns the spot in your stack first?

It's a real question. MCP is a protocol for agents to call tools. Skills are a format for agents to load procedural knowledge on demand. Both are open, both shipped from Anthropic. Some teams will ship skills first because they need procedural context. Some will reach for MCP first because they need tool connectivity. Most will end up running both — but which one earns the slot in your stack FIRST?

Tell me below. Skills or MCP. One word. Go.

#AgentSkills #ClaudeCode #MCP #AICoding #Anthropic #OpenAI #Cursor #VSCode #GitHubCopilot #GeminiCLI #AIAgents #LLM #AIWorkflow #DevTools #OpenStandard #AIProductivity #SoftwareEngineering #CodingAgent #PromptEngineering #Programming #AICoding2026
