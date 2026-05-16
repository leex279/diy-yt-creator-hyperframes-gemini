---
title: "Source Research — 12 Must-Know Agentic AI Terms"
topic: "The shared vocabulary of agentic AI: MCP, Agent Loop, Tool Use, Orchestrator, Subagent, Memory, Grounding, Guardrails, Sandboxing, Human-in-the-Loop, Context Window, Multi-Agent"
target_duration_min: 8
target_duration_max: 10
created: 2026-05-11
status: research-complete
seed_source: "Brij Kishore Pandey, Instagram (May 2026) — '12 Must-Know Agentic AI Terms' carousel"
---

# Source — 12 Must-Know Agentic AI Terms

> Every claim below is traced to a canonical source: Anthropic docs, OpenAI announcements, peer-reviewed papers (arXiv / TACL / NeurIPS), official protocol specs, NVIDIA / Google official docs, or recognized industry analysts (Simon Willison). Citations appear inline and consolidated at the bottom.

## The angle (why this video, why now)

The seed is Brij Kishore Pandey's Instagram carousel (May 2026) — a 12-card visual glossary that compressed the agent-stack into a single mental model. The post landed because the 2026 agent ecosystem is still arguing about words: the same idea ships as "tool use" at Anthropic, "function calling" at OpenAI, "actions" at Google, and "skills" at OpenAI again. Engineers can't compare designs across vendors when the vocabulary keeps shifting.

This video gives the official, citable definition for each of the 12 terms — plus *where each one fires in the agent loop*, *what it gets confused with*, and *the concrete signal that tells you you need it*. By the end, you can read any 2026 agent paper, doc, or RFP and map every term to a position in the loop without translation.

**The promise**: in 8–10 minutes, you walk away with a 4-quadrant mental model (CONTEXT / REASONING / TEAM / CONTROL), a decision tree for picking the right term when something breaks, and the canonical citation for each definition. Not a vocabulary list — a system.

---

## The 4-quadrant mental model

The 12 terms fall cleanly into four roles:

| Quadrant | What the role does | Terms |
|---|---|---|
| **CONTEXT** | What the agent can REACH | MCP · Tool Use · Memory |
| **REASONING** | How the agent THINKS | Agent Loop · Grounding · Context Window |
| **TEAM** | Agents working TOGETHER | Orchestrator · Subagent · Multi-Agent |
| **CONTROL** | What STOPS bad actions | Guardrails · Sandboxing · Human-in-the-Loop |

This grouping is the spine of Diagram 1 (`diagrams/01-terms-landscape.excalidraw`) and the scene structure of the video.

---

## 1. MCP — Model Context Protocol

**Definition**: An open standard, released by Anthropic on **November 25, 2024**, that provides a unified JSON-RPC 2.0 protocol for AI applications to securely connect to external data sources, tools, and services through a host–client–server architecture.

**Why it exists**: Before MCP, every AI tool integration required custom code per source — "every new data source requires its own custom implementation." MCP replaces that fragmentation with a single stateful session protocol. The three-party model — **Host** (the LLM app, e.g. Claude Desktop), **Client** (connector within the host), **Server** (capability provider) — separates concerns and enforces security boundaries: "Servers should not be able to read the whole conversation, nor 'see into' other servers."

**Three primitive types a server exposes**:
- **Resources** — contextual data the model can read
- **Prompts** — templated workflows
- **Tools** — functions the model can invoke

**Transport**: stdio (local inter-process; default for Claude Desktop and Claude Code) and **Streamable HTTP** (introduced November 2025 spec, replaces legacy SSE for remote services).

**Ecosystem (as of early 2026)**: PulseMCP listed 5,500+ public servers in Oct 2025. By April 2026, published estimates cite 10,000+ servers with 97M monthly SDK downloads (search-index proxies, not official telemetry). OpenAI and Google DeepMind formally adopted the protocol in March–April 2025. Governance moved to the Linux Foundation's Agentic AI Foundation (AAIF) in December 2025.

**Real example**: Claude Desktop connects to GitHub via MCP to read/write code without bespoke integration code.

**Common confusion** — MCP vs OpenAPI vs function-calling vs LSP:
- **OpenAPI** describes a single REST endpoint's schema.
- **Function-calling** describes a single tool's input shape.
- **LSP** does the same transport trick MCP does, but for language intelligence in editors.
- **MCP** is a *session-level transport and capability-negotiation protocol* — defines *how* tools are discovered and invoked across a persistent connection, not the schema of any one function.

**When-to-use signal**: *If you find yourself writing a bespoke integration layer every time the agent needs to touch a new data source, you need MCP.*

**Sources**:
- [Introducing the Model Context Protocol — Anthropic (Nov 25, 2024)](https://www.anthropic.com/news/model-context-protocol)
- [MCP Specification v2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Adoption Statistics — MCP Manager (Apr 2026)](https://mcpmanager.ai/blog/mcp-adoption-statistics/)

---

## 2. Agent Loop — PERCEIVE → PLAN → ACT → OBSERVE

**Definition**: The iterative perceive-plan-act-observe cycle in which a language model autonomously selects and executes actions, observes their results, and uses those results to inform the next action — repeating until the task is complete or a stopping condition is met.

**Canonical origin**: The **ReAct paper** by Yao et al., submitted **October 6, 2022** (arXiv:2210.03629, published ICLR 2023). The paper proposed "generating both reasoning traces and task-specific actions in an interleaved manner," producing the trace-action-observation cadence that became the default mental model for agentic systems.

**ReAct's headline result**: "On ALFWorld and WebShop, two or even one-shot ReAct prompting is able to outperform imitation or reinforcement learning methods trained with 10³ – 10⁵ task instances, with an absolute improvement of 34% and 10% in success rates."

**Named variants worth knowing**:
- **ReAct** — reason-act-observe per step (the canonical loop).
- **Reflexion** (Shinn et al., March 2023, arXiv:2303.11366) — agents verbally reflect on feedback into an episodic memory buffer. Achieved **91% pass@1 on HumanEval** vs. GPT-4's prior 80% SOTA.
- **ReWOO** — Reasoning Without Observation; decouples planning from execution into Planner / Worker / Solver. Reduces token cost 5–10×.
- **Plan-and-Execute** — commits to a multi-step plan upfront, then executes linearly.

**Anthropic's framing**: agents "plan and operate independently" while "gaining ground truth from the environment at each step (such as tool call results or code execution)" — contrasted with workflows that execute "predefined code paths."

**Real example**: Claude Code's main loop. AutoGPT's task cycle. Anthropic's research orchestrator.

**Common confusion** — pipeline / workflow vs agent loop:
- A **pipeline** has predetermined steps hardcoded by the developer.
- An **agent loop** has steps determined at runtime by the model based on tool results.
- A pipeline is a *for-loop*; an agent loop is a *while-loop with the exit condition owned by the model*.

**When-to-use signal**: *If you find yourself writing `if tool_result contains X then call Y else call Z` to handle branching tool logic, you need an agent loop — let the model decide.*

**Sources**:
- [ReAct: Synergizing Reasoning and Acting — arXiv:2210.03629 (Oct 2022)](https://arxiv.org/abs/2210.03629)
- [Reflexion — arXiv:2303.11366 (Mar 2023)](https://arxiv.org/abs/2303.11366)
- [Building Effective Agents — Anthropic Research](https://www.anthropic.com/research/building-effective-agents)

---

## 3. Tool Use (Function Calling)

**Definition**: The capability by which a language model returns a structured, schema-validated invocation request for a developer-defined function rather than a prose response — enabling the model to trigger external code and incorporate the result into subsequent reasoning.

**Names by vendor**: **OpenAI** says "function calling" — shipped **June 13, 2023**, for `gpt-4-0613` and `gpt-3.5-turbo-0613`. **Anthropic** says "tool use" — functionally synonymous, different wire format. **Google** uses "function calling" too. The terms are interchangeable in technical conversation but follow vendor docs when writing integration code.

**Simon Willison's launch-day analysis (June 13, 2023)**: "You can now send JSON schema defining one or more functions to GPT 3.5 and GPT-4 — those models will then return a blob of JSON describing a function they want you to call... which is effectively an implementation of the ReAct pattern, with models that have been fine-tuned to execute it."

**Anthropic's protocol**:
- Claude returns `stop_reason: "tool_use"` plus one or more `tool_use` content blocks.
- Developer executes the call.
- Developer submits a `tool_result` back.
- Parallel tool use is the **default** (disable via `disable_parallel_tool_use: true`).
- Claude 4+ models include token-efficient tool use by default.

**Two execution tiers**:
- **Client tools** — developer-executed (developer's code runs the function).
- **Server tools** — Anthropic-hosted (e.g. `web_search_20260209`); results arrive without developer handling.

**Tool definition shape**: JSON Schema — `name`, `description`, `input_schema`. The `strict: true` flag enforces exact schema conformance.

**Anthropic benchmark claim**: "On benchmarks like LAB-Bench FigQA and SWE-bench, adding even basic tools produces outsized capability gains, often surpassing human expert baselines."

**Real example**: An agent calling a weather API mid-conversation to answer "should I fly to NYC tomorrow?".

**Common confusion** — tool use vs MCP:
- **Function calling** defines the schema and handshake for *one tool in one API call*.
- **MCP** is the persistent session-level protocol that lets a host discover and route *many tools across many servers*.
- You can use function calling without MCP (raw API). MCP servers expose their tools to hosts, which then invoke them via function-calling mechanics.

**When-to-use signal**: *If you find yourself asking the model to respond with JSON and regex-parsing its output to extract action parameters, you need tool use — define a proper schema.*

**Sources**:
- [Function calling and other API updates — OpenAI (Jun 13, 2023)](https://openai.com/index/function-calling-and-other-api-updates/)
- [Simon Willison — Function calling analysis (Jun 13, 2023)](https://simonwillison.net/2023/Jun/13/function-calling/)
- [Tool use with Claude — Anthropic Docs](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use)

---

## 4. Orchestrator

**Definition**: A central agent (or LLM) that receives a high-level task, decomposes it into subtasks at runtime, delegates those subtasks to one or more worker agents (subagents) with isolated context windows, and synthesizes their results — exercising dynamic control flow rather than following a predetermined script.

**Canonical reference**: Anthropic's engineering blog "How we built our multi-agent research system" (June 13, 2025) — the lead agent (Claude Opus 4) orchestrates, Claude Sonnet 4 subagents work in parallel.

**Headline performance gain**: *"A multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by **90.2%** on our internal research eval."*

**Effort scaling — from the same source**:
- 1 subagent for simple fact-finding.
- 2–4 subagents for direct comparisons.
- 10+ subagents for complex research.

Each subagent contract includes "an objective, an output format, guidance on which tools and sources to use, and clear task boundaries."

**Tiered model cost allocation**: The orchestrator runs on the most capable model (Opus) for planning and synthesis; workers run on faster/cheaper models (Sonnet/Haiku) for execution. The multi-agent system uses ~15× more tokens than chat — only economical when task value justifies it.

**Anthropic's "Building Effective Agents" definition**: In the orchestrator-workers workflow, "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results" — different from fixed parallelization because subtasks "aren't predetermined — they emerge based on the specific input."

**Real example**: A coding orchestrator dispatches a test agent, a lint agent, and a deploy agent in parallel and synthesizes their results.

**Common confusion** — orchestrator vs router vs swarm:
- **Router** classifies an input and sends it to one pre-defined handler — no decomposition, no synthesis.
- **Swarm** (OpenAI's Swarm framing) has agents handing off to each other peer-to-peer — a mesh, not a hub.
- **Orchestrator** is always the hub: it holds task state, decides what to spawn next, owns the final output.

**When-to-use signal**: *If you find yourself hard-coding `step 1: search`, `step 2: summarize`, `step 3: rank`, and that sequence would change based on what step 1 returns, you need an orchestrator.*

**Sources**:
- [How we built our multi-agent research system — Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Building Effective Agents — Anthropic Research](https://www.anthropic.com/research/building-effective-agents)

---

## 5. Subagent

**Definition**: A specialized AI assistant spawned by an orchestrating agent to handle a discrete task in its own isolated context window, returning only a summary of results to the parent rather than flooding the main conversation with intermediate data.

**Canonical reference**: Anthropic's "Create custom subagents" doc — [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents).

**Three things a subagent gets that the parent doesn't share**:
1. **Own system prompt**.
2. **Own tool access list**.
3. **Own independent permissions**.

The parent uses the subagent's **description** string to decide when to delegate. The subagent works independently and returns only the result.

**Three goals isolation serves**:
- **Context preservation** — raw file contents, grep output, test logs never pollute the main context.
- **Cost control** — the built-in Explore subagent runs on **Haiku** (faster, cheaper) for read-only codebase searches.
- **Constraint enforcement** — a read-only code-reviewer subagent literally cannot be granted Write or Edit tools.

**Hard constraint**: Subagents **cannot spawn their own subagents** — prevents unbounded nesting.

**From the docs**: *"Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary."*

**Real example**: A "summarizer" subagent condenses 50 research papers before the main agent synthesizes insights. The built-in Explore agent uses Haiku to grep across a 200K-line codebase without polluting the parent's 1M context.

**Common confusion** — subagent vs multi-agent vs orchestrator:
- A **subagent** is a worker inside *one session*. Cannot talk to other agents directly.
- **Multi-agent / agent teams** = multiple sessions coordinating across a network.
- **Orchestrator** is the parent that decides *when* to spawn workers.
- Three different layers.

**When-to-use signal**: *If you find yourself noticing that codebase exploration results consume most of your context and the parent agent never references the raw intermediate output again, you need a subagent.*

**Sources**:
- [Create custom subagents — Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [Choose a permission mode — Claude Code Docs](https://code.claude.com/docs/en/permission-modes)

---

## 6. Memory — short-term and long-term

**Definition**: The mechanism by which an AI system stores, retrieves, and updates information across the boundary of a single context window — enabling persistent knowledge of user preferences, past decisions, and accumulated facts that would otherwise be lost between sessions.

**The OS-analogy framing**: The **MemGPT** paper (Packer et al., UC Berkeley; arXiv:2310.08560, October 2023) proposed treating LLM context like virtual memory in an operating system, with a three-tier hierarchy:
- **Core memory** — in-context (like RAM).
- **Recall memory** — searchable conversation history outside context (like a disk cache).
- **Archival memory** — cold long-term storage queried via tool calls.

This architecture was commercialized as **Letta** (formerly MemGPT).

**The passive-extraction approach**: **Mem0** (Chhikara et al., arXiv:2504.19413, ECAI 2025). Every message pair is analyzed; salient facts are distilled into compact natural language and stored in a vector or graph database with four operations — **ADD, UPDATE, DELETE, NOOP** — so the memory store stays coherent rather than growing unboundedly.

**LOCOMO benchmark headline numbers (Mem0 v full-context, 2026)**:
- **Accuracy**: Mem0 66.9% vs. full-context 72.9%.
- **p95 latency**: 1.44s vs. 17.12s — **91% faster**.
- **Tokens per conversation**: ~1,800 vs. ~26,000 — **90% fewer**.
- Selective memory pays back massively on cost/latency at modest accuracy loss.

**Three-type taxonomy (2026 consensus)**:
- **Episodic memory** — what happened.
- **Semantic memory** — what is known (facts, preferences, entities).
- **Procedural memory** — how to do things (learned workflows, tool-use patterns).

**Real example**: Agent recalls your coding style from a previous session stored in a vector database.

**Common confusion** — memory vs context window vs RAG:
- **Context window** = agent's immediate working memory for one session; disappears after.
- **RAG** = retrieval technique that fetches documents at query time.
- **Memory** = persistent layer that survives session boundaries; RAG can be one implementation, but memory is the broader architectural concept covering storage, update, and deletion over time.

**When-to-use signal**: *If you find yourself re-pasting the same user preferences, coding style rules, or past decisions into every new session's system prompt, you need an agent memory layer.*

**Sources**:
- [MemGPT: Towards LLMs as Operating Systems — arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- [Mem0 — arXiv:2504.19413](https://arxiv.org/abs/2504.19413)
- [State of AI Agent Memory 2026 — Mem0 Blog](https://mem0.ai/blog/state-of-ai-agent-memory-2026)

---

## 7. Grounding — reality tethering

**Definition**: The practice of anchoring a language model's generated output to specific, verifiable external information sources — so every claim in the response can be traced to a retrievable document, live data feed, or structured knowledge base, rather than the model's parametric weights alone.

**Cleanest platform definition**: Google Vertex AI: *"Grounding is the ability to connect model output to verifiable sources of information."*

**Implementation flavors**:
- **RAG** (Retrieval-Augmented Generation) — retrieve docs first, then condition generation on them. The dominant implementation.
- **Search-grounding** — Google's Gemini grounded responses via the Search API.
- **Vertex AI Search**, Elasticsearch indexes, custom APIs, Maps data — same idea, different stores.
- **Native Citations** — Anthropic's Citations API (launched June 23, 2025): the API processes source documents natively and generates **precise sentence-level references automatically**, instead of prompting Claude to include sources (which produced inconsistent results).

**Hard receipts**:
- **Endex** (post-Citations-API adoption): "Source hallucinations and formatting issues reduced from **10% to 0%**, with a 20% increase in references per response."
- **Thomson Reuters CoCounsel** quote: "For CoCounsel to be trustworthy and immediately useful for practicing attorneys, it needs to cite its work."
- Google's claim for grounding-with-Search: "reduces hallucinations by **40%** compared to ungrounded models."

**Real example**: Agent cites live stock price from Bloomberg API instead of generating numbers from training data.

**Common confusion** — grounding vs RAG vs citations vs tool use:
- **Grounding** is the parent concept — the requirement that outputs be traceable to verifiable sources.
- **RAG** is one retrieval strategy that implements grounding.
- **Citations** are the output artifact that proves grounding was applied.
- **Tool use** (e.g. calling Bloomberg API) is another grounding implementation that bypasses retrieval entirely.

**When-to-use signal**: *If you need to trust a model response enough to act on it in a legal, financial, or medical context — or share it with someone who will ask "where did this come from?" — you need grounding.*

**Sources**:
- [Grounding overview — Google Cloud Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)
- [Introducing Citations on the Anthropic API (Jun 23, 2025)](https://claude.com/blog/introducing-citations-api)
- [Citations API Docs — Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/citations)

---

## 8. Guardrails — safety layer

**Definition**: Programmatic controls applied at inference time — as input filters, output filters, or runtime policy enforcers — that constrain what an AI system can accept, generate, or execute, independently of the model's trained behavior.

**Canonical open-source toolkit**: **NVIDIA NeMo Guardrails** (github.com/NVIDIA-NeMo/Guardrails). Defines five rail types:
- **Input rails** — filter or modify user queries before they reach the LLM.
- **Dialog rails** — influence prompting behavior mid-conversation.
- **Retrieval rails** — process retrieved document chunks in RAG pipelines.
- **Execution rails** — manage tool/action inputs and outputs.
- **Output rails** — filter or alter LLM responses before delivery.

The DSL for authoring rails is **Colang** — "a modeling language specifically created for designing flexible, yet controllable, dialogue flows."

**The critical architectural distinction**: system-prompt-based vs runtime-enforced.
- A system prompt saying "never discuss competitors" is **trivially jailbroken**.
- A runtime output rail that scans every response for competitor mentions before it reaches the user **cannot be bypassed by the model's own reasoning**.

**Training-time variant — Constitutional AI** (Anthropic, December 2022): a set of natural-language principles — a "constitution" — guides the model to critique and revise its own outputs during both supervised and RL training. Bakes the guardrail into the weights rather than enforcing it externally. Sample principle: *"Please choose the response that is the most helpful, honest, and harmless."*

**Claude Code's runtime guardrail**: the auto mode classifier runs on a separate server-side model, inspects pending tool calls before execution, and **blocks**:
- Downloading and executing code (e.g. `curl | bash`).
- Sending sensitive data to external endpoints.
- Production deploys and migrations.
- Force push, or pushing directly to `main`.

"A separate server-side probe scans incoming tool results and flags suspicious content before Claude reads it."

**Real example**: Agent is blocked from deleting production databases even if instructed to "clean everything up."

**Common confusion** — guardrails vs sandboxing vs RLHF:
- **Sandboxing** isolates the *execution environment* — process can't reach network/filesystem outside defined boundaries. System-level control.
- **RLHF** bakes preferences into the model *weights at training time*.
- **Guardrails** sit at *inference time*, between model and outside world, enforcing policies the model itself cannot override.

**When-to-use signal**: *If you find yourself running an agent with tool-use access to production systems and relying solely on the system prompt to prevent destructive actions, you need runtime guardrails.*

**Sources**:
- [NeMo Guardrails — NVIDIA GitHub](https://github.com/NVIDIA-NeMo/Guardrails)
- [Constitutional AI: Harmlessness from AI Feedback — Anthropic (Dec 2022)](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
- [Permission modes — Claude Code Docs](https://code.claude.com/docs/en/permission-modes)

---

## 9. Sandboxing — safe execution

**Definition**: A hardware- or kernel-isolated execution environment in which an agent runs untrusted code or takes side-effectful actions, with the guarantee that a compromise or misbehavior inside the sandbox cannot propagate to the host system or production data outside it.

**Key insight**: Sandboxing is an **infrastructure-level control**, not a policy control. Even if the agent is fully compromised by prompt injection and instructed to `rm -rf /` or exfiltrate secrets, the blast radius is bounded to the sandbox instance.

**Three technologies dominate 2026**:

| Tech | Isolation | Boot time | Notes |
|---|---|---|---|
| **Firecracker microVMs** (AWS, open-sourced Nov 2018) | Hardware-level via KVM; independent Linux kernel per VM | ~125 ms | <5 MiB RAM per VM. Used by E2B, Modal, Fly.io, AWS Lambda/Fargate. |
| **gVisor** (Google) | User-space syscall interception | Fast | Used in production by Modal Labs. No full VM. |
| **Docker / runc containers** | Shared host kernel | Fastest | **Weakest** option — container-escape CVE = root on host. |

**2026 consensus (MIT AI Agent Index)**: Docker alone is "**explicitly insufficient for untrusted agent code execution**." [Source](https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf)

**E2B (e2b.dev) — the dominant AI sandbox-as-a-service**: "Companies like E2B use Firecracker to run AI-generated code securely in the cloud." Each sandbox gets its own kernel. Pre-warmed VM snapshots → ~150 ms cold-start. Usage grew from 40,000 sandbox sessions/month (March 2024) to ~15M/month (March 2025).

**Claude Code**: Anthropic ships a Docker integration (`docker/sandbox-templates:claude-code`) with `--dangerously-skip-permissions`; "sandboxes don't pick up user-level configuration from your host, such as `~/.claude`" — OAuth credentials proxied externally so "credentials aren't stored inside the sandbox."

**OpenAI Codex**: Uses Landlock + seccomp at the syscall layer. As of early 2026, the "only major agent with sandboxing enabled by default."

**Real example**: Claude Code runs user scripts in a Docker container before applying changes to the actual repo.

**Common confusion** — sandboxing vs guardrails vs permissions. From the MIT AI Agent Index:
> *"Application-level guardrails, prompt filtering, and semantic monitoring operate after the agent has been handed execution authority. Sandboxing constrains what the agent can do with that authority regardless of what it has been instructed to do."*

- **Guardrails** = rules.
- **Permissions** = allow/deny lists.
- **Sandboxing** = the environment that physically contains the blast radius when both fail.

**When-to-use signal**: *If you find yourself running an agent that executes shell commands, writes to disk, or calls arbitrary code on behalf of user input, you need a sandbox — not just a system prompt saying "be careful."*

**Sources**:
- [Firecracker — AWS Open-Source Announcement (Nov 2018)](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/)
- [Firecracker vs QEMU — E2B Blog](https://e2b.dev/blog/firecracker-vs-qemu)
- [2025 AI Agent Index — MIT](https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf)
- [Claude Code in Docker — Docker Docs](https://docs.docker.com/ai/sandboxes/agents/claude-code/)

---

## 10. Human-in-the-Loop (HITL) — approval gate

**Definition**: An architectural pattern in which a human is inserted as a required decision-maker at one or more checkpoints in an automated pipeline, preventing autonomous progression until explicit approval, correction, or confirmation is received.

**Origins**: The phrase appears in cybernetics literature from the 1960s. Modern ML meaning was codified in **Christiano et al., "Deep Reinforcement Learning from Human Preferences," NeurIPS 2017** (arXiv:1706.03741). Popularized in OpenAI's InstructGPT / RLHF (2022).

**In agentic AI**, HITL is repurposed from labeling to **approval gates** — checkpoints where the agent pauses before executing a dangerous or irreversible tool call.

**Claude Code's `permission_mode` parameter** — the canonical HITL spectrum (6 modes):
- `"default"` — callback on ungated tools.
- `"acceptEdits"` — file ops auto-approved; Bash still gates.
- `"plan"` — read-only exploration; no edits.
- `"dontAsk"` — deny ungated.
- `"auto"` — classifier-based (TypeScript SDK only); 17% miss rate, 0.4% false-positive vs rubber-stamp human approval.
- `"bypassPermissions"` — no gates; "Reserve for CI, containers, or other isolated environments."

**The approval-fatigue finding**: Anthropic's production data shows users approve **93%** of permission prompts — indicating fatigue, which is why the model-based `auto` classifier exists.

**LangGraph's primitive**: ships a first-class `interrupt()` call. The graph pauses execution and surfaces a `HumanMessage`-compatible node, blocking until a human response is injected.

**GitHub Copilot Workspace (2025)**: every proposed multi-file change requires explicit developer approval before execution.

**Real example**: Agent drafts a client email but waits for your approval before hitting send.

**Common confusion** — HITL vs guardrails:
- **Guardrails** = automated checks (classifier, output filter rules). Fire without a human in the path.
- **HITL** = actual human in the decision. A guardrail can block a tool call automatically; HITL pauses and waits.
- **Emerging variant**: **Human-on-the-Loop (HOTL)** — humans supervise an autonomously running agent and can intervene, but are not a required gate.

**When-to-use signal**: *If you find yourself deploying an agent that can send emails, commit code, move money, or delete records — and a wrong decision cannot be trivially undone — you need HITL approval gates on those specific tool calls.*

**Sources**:
- [Deep RL from Human Preferences — arXiv:1706.03741 (Christiano et al., 2017)](https://arxiv.org/abs/1706.03741)
- [Claude Code Agent SDK — Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)
- [Human-in-the-loop — LangChain Docs](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)

---

## 11. Context Window — working memory limit

**Definition**: The fixed maximum number of tokens — comprising system prompt, conversation history, tool definitions, tool outputs, and any injected documents — that a language model can attend to in a single inference call.

**Key property**: The context window is the model's entire working memory **for one inference**. Ephemeral. Wiped after the call. Attention is computed over all tokens simultaneously (transformer architecture).

**The 2026 frontier (as of May 2026)**:

| Model | Context window | Input / Output price (USD/MTok) |
|---|---|---|
| Claude Opus 4.7 | 1M | $5 / $25 |
| Claude Sonnet 4.6 | 1M | $3 / $15 |
| Claude Opus 4.6 | 1M | (legacy) |
| Gemini 3.1 Pro | 1M | — |
| Llama 4 (experimental) | 10M | — |
| GPT-5 | 200K | — |

**The "Lost in the Middle" finding — landmark paper**:
- Liu et al., Stanford / Meta, TACL 2024, arXiv:2307.03172 (Jul 2023).
- Abstract: *"Performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts — even for explicitly long-context models."*
- Implication: large context windows don't eliminate the placement problem — front-load and back-load critical content.

**The "needle in a haystack" benchmark family** measures retrieval quality across context positions. Anthropic's internal MRCR v2 benchmark reports Claude Opus 4.6 at **76%** and Sonnet 4.6 at **68.4%** at 1M tokens.

**Cost reality**: A full 200K-token request using Claude Sonnet 4.6 costs ~$0.60 input alone. A 1M-token request: ~$3 input. Long context isn't free.

**Anthropic's exact framing** (Agent SDK docs): *"The context window is the total amount of information available to Claude during a session. It does not reset between turns within a session. Everything accumulates: the system prompt, tool definitions, conversation history, tool inputs, and tool outputs."*

**Real example**: A 200K token window lets an agent read an entire codebase before writing a single line.

**Common confusion** — context window vs memory vs RAG:
- **Context window** = active token budget for one call. Ephemeral.
- **Memory** = external persistent store across sessions. Stateful, personalized.
- **RAG** = pipeline that queries a static vector store and injects matching document chunks into the context window.
- RAG feeds the context window. Memory persists across calls. The context window itself is the live compute buffer.
- A 1M context does not eliminate the need for RAG (cost) or memory (the window wipes after each call).

**When-to-use signal**: *If you find yourself needing the model to reason coherently across an entire codebase, contract, or research corpus in a single pass — without chunking or retrieval — you need a large context window. Position the most critical content at start and end (per Liu et al. 2023).*

**Sources**:
- [Lost in the Middle — arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- [Anthropic Pricing — platform.claude.com](https://platform.claude.com/docs/en/about-claude/pricing)
- [Context Window Race 2026 — claude5.com](https://claude5.com/news/context-window-race-2026-how-claude-gemini-gpt-transform-lon)

---

## 12. Multi-Agent Systems — collaborative intelligence

**Definition**: A computational architecture in which multiple LLM-backed agents operate concurrently or in coordinated sequence, each with specialized roles, tools, or knowledge, collaborating to complete tasks that exceed the capacity or performance of a single agent.

**The core value prop**: **parallelism and specialization**. One agent is serial — reason, act, wait, reason. A multi-agent system spawns several specialized subagents simultaneously: one searches ten sources while another runs benchmarks while a third summarizes prior findings.

**Canonical reference**: Anthropic's "How we built our multi-agent research system" (June 13, 2025). Production architecture:
- Lead orchestrator: **Claude Opus 4**.
- Workers: **Claude Sonnet 4** subagents in parallel.
- 3–5 subagents spawned concurrently; each capable of parallel tool calls.

**The numbers** (same Anthropic post):
- **+90.2%** improvement over single-agent Claude Opus 4 on Anthropic's internal research eval.
- **~15× token cost** vs chat.
- "Token usage by itself explains 80% of the variance" in performance. Upgrading models > doubling token budgets.

**Academic foundation**: **AutoGen** (Wu et al., Microsoft Research, arXiv:2308.08155, Aug 2023). "An open-source framework that allows developers to build LLM applications via multiple agents that can converse with each other to accomplish tasks." Domains tested: math, coding, QA, operations research, online decision-making.

**Other production frameworks**:
- **CrewAI** — reports 100,000+ agent executions per day, 150+ enterprise customers; $18M Series A.
- **LangGraph** — running in production at LinkedIn, Uber, 400+ companies.
- **MetaGPT** — software-team simulation pattern.

**Real example**: One agent researches, one writes, one fact-checks — all coordinated by an orchestrator. (This video itself was researched by three parallel agents — meta example.)

**Common confusion** — multi-step / orchestrator / multi-agent:
- **Multi-step** — one agent, sequential reasoning over many turns. NOT multi-agent.
- **Orchestrator** — one *component* inside a multi-agent system that coordinates others. Not the system itself.
- **Multi-agent system** — the full architecture property: multiple distinct agents, each with own context and tools, operating in parallel or coordinated sequence.
- An orchestrator is one agent. Multi-agent is the property of the system it inhabits. Chain-of-thought is multi-step, not multi-agent.

**When-to-use signal**: *If you find yourself needing to search across more sources, run more evals, or process more information than a single agent can handle within one context window and one serial reasoning chain — and the task value justifies 15× the token cost — you need a multi-agent system.*

**Sources**:
- [How we built our multi-agent research system — Anthropic Engineering (Jun 13, 2025)](https://www.anthropic.com/engineering/multi-agent-research-system)
- [AutoGen — arXiv:2308.08155 (Aug 2023)](https://arxiv.org/abs/2308.08155)
- [Best Multi-Agent Frameworks 2026 — gurusup.com](https://gurusup.com/blog/best-multi-agent-frameworks-2026)

---

## Cross-cutting clarifications

These are the four confusions viewers will leave with if we don't explicitly address them:

### 1. MCP vs Tool Use vs Function Calling

**Tool use / function calling** define *one tool's schema for one API call*. **MCP** is the persistent session-level protocol that lets a host discover and route *many tools across many servers*. You can use function calling without MCP. MCP servers expose tools to hosts; hosts then invoke them via function-calling mechanics.

### 2. Context Window vs Memory vs RAG

| | What | Persistence |
|---|---|---|
| **Context window** | Active token budget for one inference | Ephemeral |
| **RAG** | Retrieval pipeline that feeds the window | Stateless |
| **Memory** | External store across sessions | Persistent |

### 3. Guardrails vs Sandboxing vs HITL vs Permissions

| | Layer | Actor |
|---|---|---|
| **Guardrails** | Inference-time policy enforcement | Automated (classifier / filter) |
| **Sandboxing** | Execution environment isolation | Infrastructure |
| **HITL** | Decision-gate checkpoint | Human |
| **Permissions** | Allow/deny lists | Configuration |

### 4. Subagent vs Orchestrator vs Multi-Agent

| | Scope |
|---|---|
| **Subagent** | Worker inside one session; can't talk to other agents |
| **Orchestrator** | Coordinator agent that spawns subagents/workers |
| **Multi-Agent** | The system property — multiple distinct agents collaborating, may span sessions |

---

## All sources (consolidated)

### Anthropic
- [Introducing the Model Context Protocol (Nov 25, 2024)](https://www.anthropic.com/news/model-context-protocol)
- [How we built our multi-agent research system (Jun 13, 2025)](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Constitutional AI: Harmlessness from AI Feedback (Dec 2022)](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
- [Introducing Citations on the Anthropic API (Jun 23, 2025)](https://claude.com/blog/introducing-citations-api)
- [Tool use with Claude — Docs](https://platform.claude.com/docs/en/docs/build-with-claude/tool-use)
- [Citations — Anthropic API Docs](https://docs.anthropic.com/en/docs/build-with-claude/citations)
- [Create custom subagents — Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [Permission modes — Claude Code Docs](https://code.claude.com/docs/en/permission-modes)
- [Agent SDK — Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)
- [Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing)

### Specifications / Protocols
- [MCP Specification v2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture)

### Papers (arXiv)
- [ReAct (Yao et al., Oct 2022) — arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- [Reflexion (Shinn et al., Mar 2023) — arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- [MemGPT (Packer et al., Oct 2023) — arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- [Mem0 (Chhikara et al., 2025) — arXiv:2504.19413](https://arxiv.org/abs/2504.19413)
- [Lost in the Middle (Liu et al., Jul 2023) — arXiv:2307.03172](https://arxiv.org/abs/2307.03172)
- [Deep RL from Human Preferences (Christiano et al., 2017) — arXiv:1706.03741](https://arxiv.org/abs/1706.03741)
- [AutoGen (Wu et al., Aug 2023) — arXiv:2308.08155](https://arxiv.org/abs/2308.08155)
- [Attention Is All You Need (Vaswani et al., 2017) — arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

### Vendors & Platforms
- [OpenAI — Function calling (Jun 13, 2023)](https://openai.com/index/function-calling-and-other-api-updates/)
- [Simon Willison — Function calling analysis](https://simonwillison.net/2023/Jun/13/function-calling/)
- [Google Vertex AI — Grounding overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)
- [NVIDIA NeMo Guardrails — GitHub](https://github.com/NVIDIA-NeMo/Guardrails)
- [AWS — Firecracker open-source (Nov 2018)](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/)
- [E2B — Firecracker vs QEMU](https://e2b.dev/blog/firecracker-vs-qemu)
- [Claude Code in Docker — Docker Docs](https://docs.docker.com/ai/sandboxes/agents/claude-code/)
- [LangChain — Human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)

### Industry analyses
- [MCP Adoption Statistics (Apr 2026) — MCP Manager](https://mcpmanager.ai/blog/mcp-adoption-statistics/)
- [State of AI Agent Memory 2026 — Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [2025 AI Agent Index — MIT](https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf)
- [Best Multi-Agent Frameworks 2026 — gurusup.com](https://gurusup.com/blog/best-multi-agent-frameworks-2026)
- [Context Window Race 2026 — claude5.com](https://claude5.com/news/context-window-race-2026-how-claude-gemini-gpt-transform-lon)
