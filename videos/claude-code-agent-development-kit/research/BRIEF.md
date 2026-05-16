---
title: "The Agent Development Kit — Big Picture (8–10 min)"
slug: claude-code-agent-development-kit
format: long-form (1920x1080)
target_duration: 9 min (≈ 1620–1680 spoken words at ~180 wpm)
template: templates/long-form/standard
created: 2026-05-10
status: brief-ready
---

# Video Brief — The Agent Development Kit

## 1. Thesis (one sentence)

**Claude Code isn't a coding assistant. It's a 5-layer Agent Development Kit — and the gap between a demo agent and a production agent is which layers you actually use.**

The shortcut framing comes from Brij Kishore Pandey's viral Instagram post (Apr 25, 2026) — "most engineers only touch Layer 1." This video makes the case with the official Anthropic docs underneath every claim.

## 2. Audience + Promise

- **Audience**: Senior devs who know `CLAUDE.md` exists, maybe wired one MCP server, but haven't built skills/hooks/subagents/plugins. Channel demographic = mid-to-senior eng working with Claude Code daily.
- **Promise (in 9 min)**: You leave with a one-screen mental model of all 5 layers, a decision tree to pick the right layer for any extension, and concrete examples for each. You can immediately go answer "is this a skill, a hook, or just a CLAUDE.md line?" for your own project.
- **What this is NOT**: A getting-started tutorial. We don't install Claude Code, we don't show prompts, we don't demo a chat. This is architecture-level mental modelling for people already using the tool.

## 3. Hook (3 candidates — pick winner in Phase 2)

**A. Receipt-first (recommended — Triple-Threat compliant)**
> "Claude Code has 5 customization layers. Most devs touch one. Here's what the other four unlock — and how to know which one you actually need."
> Visual: 5-layer-stack diagram slams onto screen, four layers grayed out, Layer 1 highlighted.

**B. Contrarian**
> "Stop putting everything in CLAUDE.md. Past 200 lines, Claude starts skimming it. Here's the 5-layer architecture that solves it."

**C. Question-loop**
> "Should this rule live in CLAUDE.md, a skill, a hook, or a subagent? If you can't answer in 5 seconds, you're missing 4 layers of Claude Code."

→ **Use A.** It opens the loop ("the other four"), makes a falsifiable claim ("most devs only touch one"), and the visual matches the words exactly.

## 4. Scene-by-scene outline (8 scenes)

| # | Scene | Archetype | Dur | What's on screen | Narration beat |
|---|---|---|---|---|---|
| 1 | **Hook + thesis** | scene-hook | 0:00–0:35 | Brij Instagram cite + 5-layer stack diagram (D1) entering | "5 layers. Most devs touch one. Here's the other four." |
| 2 | **The 5 layers in 60s** | scene-stat-pill-row + diagram (D1) | 0:35–1:35 | Diagram 1 fills screen; each layer highlights as it's named | One sentence per layer: "CLAUDE.md = always-on facts. Skills = on-demand knowledge. Hooks = deterministic guards. Subagents = isolated workers. Plugins = team distribution." |
| 3 | **Layer 1 deep — CLAUDE.md** | scene-side-by-side | 1:35–3:00 | Left: file tree showing `CLAUDE.md`, `~/.claude/CLAUDE.md`, `.claude/rules/`. Right: live token-cost meter "loaded every request" | "It's a constitution, not a config. Always loaded. Keep under 200 lines or Claude starts skimming. Project facts, not procedures." |
| 4 | **Layer 2 + 3 in tension — Skills vs Hooks** | scene-side-by-side | 3:00–4:30 | Left: Skill card "/lint" with description match. Right: PreToolUse hook firing red. The same goal — different mechanism. | "Skills are guidance. Hooks are enforcement. 'Never edit `.env`' in a skill is a request. A `PreToolUse` hook that exits 2 is a guarantee. 31 hook events. 5 handler types." |
| 5 | **Layer 4 — Subagents and the context isolation play** | scene-terminal + animation | 4:30–6:00 | Animated fork: main thread spawns `Explore` (Haiku), `code-reviewer` (Sonnet), `test-runner` — three parallel boxes returning summaries | "When the side task would flood your main context, fork a subagent. Own model. Own tools. Own permissions. Returns only the summary. This is also where you cost-route — Haiku reads 50 files, Opus stays on main thread." |
| 6 | **Layer 5 — Plugins, the distribution wrapper** | scene-stat-pill-row | 6:00–7:00 | Marketplace install command on screen; plugin.json directory tree; one install → 4 capabilities appear | "Wrap skills + agents + hooks + MCP into one bundle. `/plugin install`. Whole team gets the same behavior. Versioned. Namespaced. This is how 'agent capabilities' become a deliverable." |
| 7 | **The decision tree (D3) — which layer for what?** | scene-side-by-side (full-screen diagram) | 7:00–8:15 | Diagram 3 cascades onto screen, one question at a time. Highlight current question, dim others. | "5 questions. 5 answers. Pick the first YES." (read each Q + answer) |
| 8 | **Lifecycle (D2) + close** | scene-video-embed + outro | 8:15–9:00 | Diagram 2 (request lifecycle) plays as the "system in motion." Then channel CTA + Dynamous endcard. | "Here's how all 5 fire on a single request. CLAUDE.md is always there. Hooks gate the transitions. Skills load on description-match. Subagents fork off. Plugins wrap the whole thing for distribution. That's the kit." |

## 5. Visual library picks (per scene)

- D1 (5-layer stack): scenes 1, 2 (hero)
- D2 (request lifecycle): scene 8 (in motion)
- D3 (decision tree): scene 7 (full-screen reveal)
- `vfx-text-cursor` block (registry): hook word "5" slam in scene 1
- `stat-pill-row` block: scenes 2, 6 (pull receipts: "200 lines", "31 events", "5 handler types")
- `cinematic-zoom` shader transition between scene 3 → 4 (the gear-shift from passive to active enforcement)
- `dynamous-endcard` block (already wired in long-form template): scene 8 outro

## 6. Receipts to use (cite source in metadata)

- "Most engineers only touch Layer 1" — Brij Kishore Pandey, Instagram, Apr 25 2026
- "31 distinct hook events" — code.claude.com/docs/en/hooks
- "5 hook handler types: command, http, mcp_tool, prompt, agent" — same
- "Keep CLAUDE.md under 200 lines" — code.claude.com/docs/en/memory
- "Skill descriptions cap at 1,536 chars; ~1% of context window total" — code.claude.com/docs/en/skills
- "Claude makes the same mistake twice → CLAUDE.md. You keep pasting the same prompt → skill." — features-overview decision heuristic
- "Plugin subagents drop hooks/mcpServers/permissionMode for security" — code.claude.com/docs/en/sub-agents
- Custom commands merged into the skill system in v2.x — code.claude.com/docs/en/skills

## 7. Engagement tactics

- **Open loop in scene 1** ("most devs touch one — here's what the other four unlock") closes in scene 2 (all five visible at once).
- **JCRR (just-curious-rationale-receipt)** in scene 4: "Why does enforcement need a different layer? Because instructions are reasoned around — hooks aren't. The exit code 2 is the receipt."
- **Contrarian beat** in scene 3: "Past 200 lines, CLAUDE.md adherence degrades — Claude skims it. The fix isn't more lines, it's the next layer."
- **Specificity ladder** when describing each layer — name → what it does → where it lives → one concrete example. Never abstract for two consecutive sentences.
- **Visual counter on screen** during scene 2: "Layer 1 of 5 → Layer 2 of 5 → …" — gives the viewer a progress bar through the architecture.
- **Sub-question hook** between scenes 4 and 5: "OK so what about parallel work? Different problem. Different layer."

## 8. CTA / endcard

- Spoken outro (locked, per channel rule): "If you want to learn more about AI, check out the dynamous.ai community."
- Endcard visuals (handled by `dynamous-endcard` block default): channel subscribe + Dynamous logo + URL pill
- Optional pinned-comment hook: "Which layer do you use most? CLAUDE.md, Skills, Hooks, Subagents, or Plugins? 1–5 in the comments."

## 9. SEO / metadata starter

- **Working title**: "Claude Code is the Agent Development Kit — All 5 Layers Explained"
- **Alt titles** (vidIQ-test before publish):
  - "The 5-Layer Architecture Behind Claude Code (Most Devs Only Use 1)"
  - "Stop Using Claude Code Wrong — The Agent Development Kit"
  - "Skills vs Hooks vs Subagents — Which Layer Do You Need?"
- **Front-load chapter titles** with searched terms: "Claude.md", "Skills", "Hooks", "Subagents", "Plugins", "MCP"
- **Hashtags** (15–25): #ClaudeCode #Anthropic #AgentSDK #AI #LLM #DevTools #PromptEngineering #MCP #ClaudeMD #AISkills #AgenticCoding #AIIDE …
- **Description boilerplate**: per `.claude/rules/youtube-metadata.md` (Dynamous CTA block, chapter timestamps, debate question, sources block)

## 10. Don'ts (template-specific)

- ❌ **Don't show prompts or chat transcripts.** This is architecture, not "how to use Claude." If the screen reads like a chat, cut it.
- ❌ **Don't claim Layer 5 (Plugins) is "advanced."** It's *distribution*. The complexity is in Layers 2–4. Plugins are the wrapper.
- ❌ **Don't conflate MCP with the 5 layers.** MCP is a sidebar. It's a sixth thing — connectivity — not an ADK layer. Diagrams 1 and 2 explicitly mark it that way.
- ❌ **Don't drift past 9:30.** The promise is 8–10 min; over-running on Layer 4 (subagents) is the most likely failure mode. Hard cap scene 5 at 1:30.
- ❌ **Don't use the word "powerful."** Anti-slop rule.

## 11. Speed factor decision

- TTS speed in `.env` stays at default (`ELEVENLABS_SPEED=1.05` for long-form). If post-render feels slow, ffmpeg-speedup to 1.08× or 1.10× per `.claude/rules/video-speedup.md`. **Never re-TTS / re-render to change pacing.**

## 12. Sources (must appear in YouTube description)

- code.claude.com/docs/en/memory
- code.claude.com/docs/en/skills
- code.claude.com/docs/en/hooks
- code.claude.com/docs/en/sub-agents
- code.claude.com/docs/en/plugins
- code.claude.com/docs/en/mcp
- code.claude.com/docs/en/features-overview (the official decision framework — this video extends it visually)
- Brij Kishore Pandey, Instagram, Apr 25 2026 (the framing inspiration)

## 13. Pipeline handoff (for /diy-yt-creator)

When ready to spawn the project:

```
/diy-yt-creator
  topic: "The Agent Development Kit — 5-layer Claude Code architecture, big picture"
  template: templates/long-form/standard
  slug: claude-code-agent-development-kit
  brief: D:\Nextcloud\Obsidian\sync\smartcode\Videos\The Agent Development Kit\BRIEF.md
  source: D:\Nextcloud\Obsidian\sync\smartcode\Videos\The Agent Development Kit\source.md
  diagrams: D:\Nextcloud\Obsidian\sync\smartcode\Videos\The Agent Development Kit\diagrams\
```

Then run phases in order: phase0-research → phase1-plan → phase2-script → phase2-5-critique → phase2a-tts-script → phase2b-factcheck → TTS → phase3-5-retention → composition handoff.
