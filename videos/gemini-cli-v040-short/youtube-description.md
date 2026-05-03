Gemini CLI v0.40.0 ships local Gemma 3 — a 1B-parameter, GPU-custom model running on LiteRT-LM that powers intelligent model routing on your hardware today. Plus tiered memory across 4 layers, auto-extracted skills, compact tool output, topic narrations, and a persistent task tracker. Over 150 improvements with full local AI execution on the public roadmap.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Key Changes in This Release:
- Local Gemma 3 support (experimental) — `gemini gemma setup` to install, `/gemma` to check status; LiteRT-LM runtime + ~1 GB Gemma 3 model (`gemma3-1b-gpu-custom`) bundled
- Gemma 3: 1B parameters, GPU-accelerated build, runs on your hardware via LiteRT-LM; today powers intelligent model routing (decides which model handles each prompt locally); full local model execution on the public roadmap
- Enable via `/settings` UI ("Enable Gemma Model Router" toggle) or set `experimental.gemma: true` in `settings.json`
- Tiered memory system across 4 layers: Project (`./GEMINI.md`, committed), Subdirectory (`./src/GEMINI.md`), Private (`MEMORY.md`, not committed), Global (`~/.gemini/GEMINI.md`)
- Auto Memory (experimental) — background agent combs idle session transcripts (10+ messages) and drafts reusable `SKILL.md` files; review with `/memory inbox`; enable via `experimental.autoMemory: true`
- Task Tracker (experimental) — internal persistent task list to monitor progress on complex objectives; enable via `experimental.taskTracker: true`
- Compact Tool Output — file reads, search results, directory listings render in a structured format (no more tool-call boxes spamming the output)
- Topic Narrations — descriptive section headers replace agent chatter across all agents (e.g. "Researching Memory System: explain how it works")
- MCP Resource Support finalized for Model Context Protocol resources
- Real-time `@` Suggestions — file watcher detects + suggests files the moment they're created
- New Commands — `/new` quick-alias for fresh sessions; better accessibility with colorblind-friendly themes (GitHub-inspired); native OSC 777 desktop notifications
- Security & Trust — stricter shell command validation, core tools allowlist, secure workspace loading (headless + IDE), enhanced sandboxing for Docker / macOS Seatbelt, credential keychain fallback hardening
- Performance — bundled `ripgrep` binaries enable lightning-fast offline search; significant memory reductions for DevTools and large output streams; JSONL-based session persistence

Chapters
0:00 Gemini CLI v0.40 Ships Local Gemma 3 — @googlegemma Confirms
0:23 Local Gemma Setup: gemini gemma setup + LiteRT-LM + /settings Toggle
0:53 What Gemma 3 Does: 1B Params + GPU-Custom + Intelligent Model Routing
1:16 Five Big Upgrades: Tiered Memory + Auto Memory (4 Layers, /memory inbox)
1:53 Compact Output, Topic Narrations + Task Tracker (Persistent Objectives)
2:13 Performance + Security: Ripgrep, Sandboxing, Shell Validation, /new, A11y
2:42 Tried Gemini CLI Yet — Or Sticking With Claude Code or Codex?
2:52 Join the Dynamous Community

Resources:
- Gemini CLI on GitHub: https://github.com/google-gemini/gemini-cli
- Gemini CLI Releases: https://github.com/google-gemini/gemini-cli/releases
- Gemma Terms of Use: https://ai.google.dev/gemma/terms
- @googlegemma launch tweet (cited in this video — published 2026-04-30)
- Reddit discussion: https://www.reddit.com/r/GeminiCLI/comments/1t0589f/gemini_cli_v0400_tiered_memory_gemma_and/

To pull every change in this video:
$ gemini update    # then run `gemini gemma setup` to enable local Gemma 3

Tried Gemini CLI already, or sticking with Claude Code or Codex? Drop your tool of choice in the comments — and tell me whether local Gemma routing is the killer feature or just a nice-to-have.

#GeminiCLI #Gemma #Gemma3 #GoogleAI #LocalAI #LocalLLM #GeminiCLITutorial #GeminiCLISetup #Gemini #GoogleGemma #AICoding #AICodingTools #AICodingAssistant #AgenticAI #AIAgent #LLM #OpenSourceAI #AIDeveloperTools #RunLLMLocally #LocalAIModel #AINews #DevTools #ClaudeCodeAlternative #CursorAlternative #GoogleDevelopers
