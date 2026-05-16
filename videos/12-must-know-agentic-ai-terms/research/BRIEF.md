---
title: "12 Must-Know Agentic AI Terms — Long-form (8–10 min)"
slug: 12-must-know-agentic-ai-terms
format: long-form (1920x1080)
target_duration: 9 min (≈ 1620–1680 spoken words at ~180 wpm)
template: templates/long-form/standard
created: 2026-05-11
status: brief-ready
seed_source: "Brij Kishore Pandey, Instagram (May 2026)"
---

# Video Brief — 12 Must-Know Agentic AI Terms

## 1. Thesis (one sentence)

**The agent stack has twelve words. Most teams use three of them wrong — and that's why their demos look the same but their production systems don't.**

The 12 terms aren't a vocabulary list. They're a mental model with four roles (CONTEXT / REASONING / TEAM / CONTROL), a cycle (PERCEIVE → PLAN → ACT → OBSERVE) that anchors each one, and a decision tree that maps real production bugs to the term that names the fix.

## 2. Audience + Promise

- **Audience**: Mid-to-senior engineers shipping agentic features in 2026. People who have wired one MCP server or shipped tool use but can't yet explain to their PM *why* their agent hallucinates *and* why "more context" isn't the fix.
- **Promise (in 9 min)**: A canonical, citable definition for each of the 12 terms. A 4-quadrant mental model. A loop diagram that places every term where it fires. A decision tree that maps "my agent did X bad thing" to the right concept. After this video, you can read any 2026 agent paper, doc, or RFP and translate vendor-speak without ambiguity.
- **What this is NOT**: A "what is AI?" explainer. A code tutorial. A framework comparison. A hot take. This is **vocabulary unification** — backed by Anthropic engineering posts, the ReAct paper, the MCP spec, NVIDIA NeMo docs, Lost-in-the-Middle, AutoGen, MemGPT/Mem0, Constitutional AI.

## 3. Hook (3 candidates — pick winner in Phase 2)

**A. Receipt-first (recommended — Triple-Threat compliant)**
> "Twelve words run the entire agent stack. Get three of them wrong and your demo ships but your production agent burns money, leaks secrets, and confidently lies. Here's the right map."
>
> Visual: 4×3 terms-landscape diagram slams onto screen, all 12 cards highlight at once in their quadrant colors. Triple-threat: visual = grid, spoken = "twelve words", text = the count "12".

**B. Contrarian**
> "Stop calling everything 'tool use.' Tool use is one of twelve concepts in the agent stack — and confusing it with MCP, function calling, or grounding is why your agent ships but doesn't scale."

**C. Question-loop**
> "Your agent hallucinated. Is the fix more context, better grounding, smarter memory, or a different prompt? If you can't answer in 5 seconds, you're missing the vocabulary that decides."

→ **Use A** for the slam. **Sub-question hook** from C can land in scene 1 to open the loop: "Could you, in 5 seconds, name which of the 12 to reach for when your agent hallucinates?"

## 4. Scene-by-scene outline (10 scenes — grouped by quadrant)

| # | Scene | Archetype | Dur | What's on screen | Narration beat |
|---|---|---|---|---|---|
| 1 | **Hook + thesis** | scene-hook | 0:00–0:35 | Brij Instagram cite tile, then D1 (4×3 landscape) slams in | "12 words run the stack. Most teams use 3 wrong." |
| 2 | **The map — 12 terms in 4 quadrants** | scene-diagram (D1 full-screen) | 0:35–1:10 | D1 holds; quadrant headers highlight in sequence (orange / blue / purple / red) | "Four roles. Twelve words. Read each one once. CONTEXT reaches. REASONING thinks. TEAM coordinates. CONTROL stops." |
| 3 | **CONTEXT: 1·MCP, 3·Tool Use, 6·Memory** | scene-side-by-side + stat-pill | 1:10–2:35 | Left: MCP host-client-server diagram (Nov 25 2024 stamp). Right: Anthropic tool_use → tool_result loop. Bottom: MemGPT 3-tier (RAM/disk/archival) | "MCP is USB-C for AI — open standard, Nov 2024. Tool use shipped June 2023 at OpenAI. Memory is the OS analogy: scratchpad now, vector store later." |
| 4 | **REASONING: 2·Agent Loop, 7·Grounding, 11·Context Window** | scene-diagram (D2 partial) | 2:35–4:00 | D2 (cycle) appears; PERCEIVE quadrant highlights; ReAct paper cite (arXiv:2210.03629) on screen; pill: "Citations API: 10% → 0% hallucinations (Endex)"; pill: "1M tokens · Lost in the Middle" | "ReAct, 2022 — perceive, plan, act, observe. Grounding ties output to source. 1M context isn't enough — Liu et al. proved info in the middle gets lost." |
| 5 | **TEAM: 4·Orchestrator, 5·Subagent, 12·Multi-Agent** | scene-stat-pill-row + animation | 4:00–5:30 | Animated fork: Opus orchestrator → 3 Sonnet subagents in parallel → results synthesize. Pull stat: "+90.2% perf · 15× tokens" (Anthropic, Jun 2025) | "Orchestrator splits the goal. Subagent owns one task with its own context. Multi-agent is the system property. Anthropic's number: ninety point two percent better than solo. Cost: fifteen times the tokens." |
| 6 | **CONTROL: 8·Guardrails, 9·Sandboxing, 10·HITL** | scene-side-by-side | 5:30–6:45 | Left: NeMo 5-rail diagram. Center: Firecracker microVM stamp ("AWS, Nov 2018 · 125ms boot"). Right: Claude Code permission_mode picker showing 6 modes | "Three control layers — not one. Guardrails are rules. Sandboxing is the environment. Human-in-the-loop is the gate. Confuse them and your agent will eventually find the gap." |
| 7 | **The 4 cross-cutting confusions** | scene-side-by-side (4 tables) | 6:45–7:45 | 4 mini-tables flash up: MCP vs Tool Use · Context vs Memory vs RAG · Guardrails vs Sandboxing vs HITL · Subagent vs Orchestrator vs Multi-Agent | "These are the four arguments your team will have. Here's the resolution for each." |
| 8 | **The decision tree (D3) — which concept is your bug?** | scene-diagram (D3 full-screen) | 7:45–8:30 | D3 cascades onto screen, one question at a time. Highlight current question, dim others. Branch arrows light up. | "5 symptoms. Pick the first YES. Q1 covers most production hallucinations. Q3 covers most security incidents." |
| 9 | **The agent loop with every term anchored (D2 hero pose)** | scene-diagram (D2 full-screen) | 8:30–8:55 | D2 (loop with all 12 anchored) plays in motion — phase labels pulse in clockwise sequence, terms scale up at their phase | "That's the stack. Twelve words. One cycle. Four roles." |
| 10 | **Outro + Dynamous endcard** | scene-outro | 8:55–9:00 | Dynamous CTA card | "If you want to learn more about AI, check out the dynamous.ai community." |

## 5. Visual library picks (per scene)

- **D1 — terms-landscape (4×3 grid)**: scenes 1, 2 (hero pose); referenced again in 3, 4, 5, 6 as overlay (quadrant in focus)
- **D2 — agent-loop-anchors**: scenes 4 (partial — PERCEIVE quadrant only), 9 (hero pose, full cycle in motion)
- **D3 — decision-tree**: scene 8 (full-screen sequential reveal)
- **stat-pill-row** (registry block): scenes 3, 5 — pull receipts: "Nov 2024 · 10,000+ servers", "Jun 2023 · OpenAI", "+90.2% / 15× tokens", "1M tokens · $3/$15 MTok"
- **vfx-text-cursor** (registry): scene 1 hook word "12" slam
- **cinematic-zoom** shader transition: scene 7 → 8 (the gear shift from confusions to decision tree)
- **flowchart** block: optionally for D3 if registry version is cleaner than our excalidraw
- **dynamous-endcard** block: scene 10

## 6. Receipts to use (cite source in metadata)

The numbers / direct quotes the video must land precisely. Every one of these is in `source.md` with a URL.

| Receipt | Source |
|---|---|
| MCP released Nov 25, 2024 | anthropic.com/news/model-context-protocol |
| 5,500+ MCP servers (Oct 2025) → 10,000+ (early 2026) | mcpmanager.ai (PulseMCP-derived) |
| ReAct paper Oct 6, 2022, arXiv:2210.03629 | arxiv.org/abs/2210.03629 |
| ReAct: 34% / 10% absolute improvement on ALFWorld / WebShop | same |
| Reflexion: 91% pass@1 HumanEval (vs GPT-4's 80%) | arxiv.org/abs/2303.11366 |
| OpenAI function calling shipped Jun 13, 2023 | openai.com/index/function-calling-and-other-api-updates |
| "JSON schema defining one or more functions" (Simon Willison) | simonwillison.net/2023/Jun/13/function-calling |
| Multi-agent: +90.2% over single-agent on Anthropic's internal eval | anthropic.com/engineering/multi-agent-research-system |
| Multi-agent: ~15× more tokens than chat | same |
| Anthropic spawn rules: 1 / 2–4 / 10+ subagents | same |
| MemGPT three-tier (core / recall / archival), arXiv:2310.08560 | arxiv.org/abs/2310.08560 |
| Mem0 LOCOMO: 91% lower p95 latency, 90% fewer tokens | mem0.ai/blog/state-of-ai-agent-memory-2026 |
| Citations API: Endex 10% → 0% hallucinations | claude.com/blog/introducing-citations-api |
| Citations API launched Jun 23, 2025 | same |
| NeMo Guardrails 5 rail types + Colang | github.com/NVIDIA-NeMo/Guardrails |
| Constitutional AI, Anthropic Dec 2022 | anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback |
| Claude Code permission_mode: 6 discrete modes | code.claude.com/docs/en/agent-sdk/agent-loop |
| Approval-fatigue stat: 93% of permission prompts approved | same |
| Firecracker AWS-open-sourced Nov 2018, ~125ms boot, <5 MiB RAM | aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization… |
| MIT AI Agent Index: Docker "insufficient for untrusted agent code" | aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf |
| E2B: 40K → 15M sandbox sessions/mo (Mar 2024 → Mar 2025) | e2b.dev (industry analyses) |
| Lost in the Middle, Liu et al. 2023, arXiv:2307.03172 | arxiv.org/abs/2307.03172 |
| Claude Sonnet 4.6 / Opus 4.7 — 1M context, $3/$15 and $5/$25 MTok | platform.claude.com/docs/en/about-claude/pricing |
| AutoGen, Wu et al. Microsoft, Aug 2023, arXiv:2308.08155 | arxiv.org/abs/2308.08155 |

## 7. Engagement tactics

- **Open loop in scene 1**: "Three of these you use wrong. Watch for which." — closes implicitly in scene 7 (the cross-cutting confusions resolve which 3 are most often misused).
- **Specificity ladder** in every term reveal: vendor name → release date → one-line definition → one real example → one stat. Never abstract for two sentences in a row.
- **JCRR (just-curious-rationale-receipt)** in scene 6: "Why three control layers? Because each fails differently. Guardrails fail when the rule isn't written. Sandboxes fail when the escape exists. HITL fails when the human rubber-stamps. 93% of permission prompts get approved (Anthropic data) — that's the receipt."
- **Triple-threat alignment** on every scene transition: spoken word + on-screen text + visual change in the same beat (per `.claude/skills/engagement-hooks-framework/`).
- **Visual counter** during scene 2: "Term 1 of 12 → Term 2 of 12 → …" — viewer's progress through the stack.
- **Sub-question hook** between scenes 5 and 6: "OK, multi-agent gets you parallelism. But what stops it from doing damage in parallel? Different problem. Different layer."
- **Lego-brick deconstruction** in scene 7: take the most-confused pairs (MCP vs Tool Use, Context vs Memory) and snap them apart on screen.

## 8. SEO starter (vidIQ pass before publish — per `.claude/rules/youtube-metadata.md`)

- **Working title options** (vidIQ-score before commit; refine in Phase 5):
  - "12 Agentic AI Terms Every Dev Must Know (2026)"
  - "The Agent Stack: 12 Words You're Using Wrong"
  - "MCP, Tool Use, Agent Loop — 12 Terms That Run Every AI Agent in 2026"
- **Primary keyword**: "agentic AI terms"
- **Secondary**: "MCP", "agent loop", "tool use", "function calling", "multi-agent system", "context window 2026"
- **Description**: chapter timestamps come from `data-start ÷ speed_factor` after ffmpeg speedup. Front-load keywords in first 200 chars. Engagement question at the end ("Which of the 12 do you think is most over-hyped?"). Dynamous CTA between `----`. 15-25 hashtags.

## 9. Chapter timestamps (pre-speedup; recompute after ffmpeg)

| # | Chapter | Start |
|---|---|---|
| 1 | Intro: 12 words run the agent stack | 0:00 |
| 2 | The 4-quadrant map (Context / Reasoning / Team / Control) | 0:35 |
| 3 | CONTEXT — MCP, Tool Use, Memory | 1:10 |
| 4 | REASONING — Agent Loop, Grounding, Context Window | 2:35 |
| 5 | TEAM — Orchestrator, Subagent, Multi-Agent | 4:00 |
| 6 | CONTROL — Guardrails, Sandboxing, Human-in-the-Loop | 5:30 |
| 7 | The 4 confusions that ship bad agents | 6:45 |
| 8 | Decision tree — which concept is your bug? | 7:45 |
| 9 | The full agent loop with every term placed | 8:30 |
| 10 | Outro | 8:55 |

## 10. Don'ts (template-specific)

- **Don't** use "function calling" and "tool use" interchangeably in scene 3 — say "OpenAI's term" / "Anthropic's term" once, then pick one and stick.
- **Don't** use the words "live", "lead" without checking [`tts-pronunciation.md`](../../diy-yt-creator-hyperframes/.claude/rules/tts-pronunciation.md) — both are heteronyms. Default fixes: "available", "primary".
- **Don't** put marker overlays on the diagram bars (per [`screenshot-anchor-markers.md`](../../diy-yt-creator-hyperframes/.claude/rules/screenshot-anchor-markers.md)) — these excalidraws are synthetic charts, not source screenshots, so technically allowed, but still keep emphasis subtle.
- **Don't** drop the citations. The video's whole credibility ride is "every stat has a URL behind it." If a stat is on screen, the source must be on screen or in description.
- **Don't** abstract for two consecutive sentences. Every other sentence needs a concrete name, date, or number.

## 11. Quality bar checklist

- [ ] Every term has: definition + one example + one citation
- [ ] All 12 terms appear visually in D1 by 0:45
- [ ] All 12 terms appear visually in D2 by 9:00 (loop close)
- [ ] D3 reveals 5 questions sequentially in scene 8 — never all at once
- [ ] Engagement-hooks rules apply (`.claude/skills/engagement-hooks-framework`)
- [ ] Anti-slop pass (`/engagement-hooks-framework` references/anti-slop.md)
- [ ] Heteronym audit on script before TTS (per `.claude/rules/tts-pronunciation.md`)
- [ ] No 5s static gaps (per `.claude/rules/visual-pacing-5s.md`)
- [ ] All sub-comp wirings validate (per `.claude/rules/sub-composition-wiring.md`)

## 12. diy-yt-creator handoff

Spawn from `templates/long-form/standard/` and feed this BRIEF + `source.md` to Phase 1.

```bash
# Copy template → videos/<slug>
Copy-Item -Recurse templates/long-form/standard videos/12-must-know-agentic-ai-terms

# Edit meta.json
# { "id": "12-must-know-agentic-ai-terms", "name": "12 Must-Know Agentic AI Terms" }

# Run the phase pipeline (full-auto or per-phase per `.claude/skills/diy-yt-creator/SKILL.md`)
# Inputs Phase 0 has already covered (this BRIEF + source.md).
# Phase 1 → composition plan
# Phase 2 → script
# Phase 2.5 → critique
# Phase 2a → TTS script (heteronym audit)
# Phase 2b → fact-check (cross-check against source.md citations only)
# Phase 3 (TTS handoff) → narration.wav
# Phase 3.5 → retention strategy
# Phase 4 (composition) → wire scenes; copy D1/D2/D3 into assets/ if used as images
```

Phase 2b should **only fact-check against `source.md`** per the user's memory rule (see [`feedback_factcheck_article_response_scope.md`](../../../.claude/projects/.../memory/feedback_factcheck_article_response_scope.md)).
