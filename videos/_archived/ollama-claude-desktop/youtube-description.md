Ollama just shipped Claude Desktop support. Every Ollama Cloud model — Kimi K2.6, GPT-OSS 120b, Qwen3-VL 235b, Devstral, Ministral, GLM, Minimax — now runs natively inside Claude Cowork and Claude Code. Two-command setup: `ollama launch claude-desktop`. The launch tweet hit 139K views in hours. Here's what just unlocked, the full lineup, and the limits.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Key Changes in This Release:
- Ollama Cloud models discovered automatically inside Claude Desktop's model picker — no manual provider config
- `ollama launch claude-desktop` swaps the Anthropic profile for an Ollama-Cloud-backed bridge in one command (revert with `--restore`)
- Works in both Claude Cowork (agentic file/app organization) and Claude Code (the launch demo runs the snake-game-graphics-upgrade plan on Kimi K2.6 Thinking)
- Subagents inherit the parent agent's model — pick Qwen once, every spawned subagent runs Qwen
- Lineup: Kimi K2.6 Thinking, GPT-OSS 120b, Qwen3-VL 235b, Devstral, Ministral, GLM, Minimax
- Web search and Extensions are NOT supported yet — roadmap items, not in the v1 bridge
- Same `OLLAMA_API_KEY` you already use locally — no separate Anthropic-side credential swap

Chapters
0:00 Ollama × Claude Desktop Launch — 139K Views in Hours
0:18 Two-Command Setup: ollama launch claude-desktop
0:28 Claude Cowork on Ollama Cloud — Agentic File Organization
0:40 Claude Code on Ollama Cloud — Snake Game Demo Running on Kimi K2.6
0:50 Ollama Cloud Lineup: Kimi, GPT-OSS, Qwen, Devstral, Ministral, GLM, Minimax
1:00 Limits + Setup Docs — No Web Search, No Extensions, Subagent Model Inheritance

Resources:
- Official setup guide: https://docs.ollama.com/integrations/claude-desktop
- Ollama Cloud overview: https://docs.ollama.com/cloud
- Claude Desktop download: https://claude.com/download
- Ollama on GitHub: https://github.com/ollama/ollama

To launch the bridge yourself:
$ ollama launch claude-desktop

Key Concepts:
- **Ollama Cloud** — Ollama's hosted inference layer for frontier-scale open-weight models (Kimi K2.6 Thinking, GPT-OSS 120b, Qwen3-VL 235b). Same `OLLAMA_API_KEY`, same SDK surface as local Ollama, but the heavy parameter counts run on Ollama's hardware.
- **Claude Cowork** — Anthropic's agentic mode that handles real desktop work autonomously (organizing files, talking to local apps). Now driveable by any Ollama Cloud model via the bridge.
- **Subagent model inheritance** — when a Claude agent spawns subagents (sub-task workers), they use the parent's currently-selected model. Pick Kimi at the top, every subagent runs Kimi too — no per-subagent model override yet.
- **`ollama launch claude-desktop` bridge** — this CLI command rewrites Claude Desktop's provider configuration to route through Ollama Cloud instead of api.anthropic.com. Completely reversible with `ollama launch claude-desktop --restore`.

Are you ditching Anthropic's Sonnet for Kimi K2.6 inside Claude Code, or sticking with the native Anthropic stack? Drop your pick below.

#OllamaCloud #ClaudeDesktop #ClaudeCode #ClaudeCowork #Ollama #KimiK2 #GPTOSS #Qwen3 #Devstral #Anthropic #AICoding #AgenticAI #AIAgents #LLM #OpenSourceLLM #AICodingAgent #AICodingAssistant #DevTools #AIAutomation #LocalLLM #OllamaSetup #AITutorial #ClaudeAI #ModelRouting #AIDeveloperTools
