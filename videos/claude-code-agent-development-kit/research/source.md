---
title: "Source Research — The Agent Development Kit"
topic: "Claude Code as the Agent Development Kit (ADK) — 5-layer architecture big picture"
target_duration_min: 8
target_duration_max: 10
created: 2026-05-10
status: research-complete
---

# Source — The Agent Development Kit (Big Picture)

> All facts below are extracted from `code.claude.com/docs` (canonical Anthropic Claude Code docs as of May 2026). Every claim cites a source URL at the bottom.

## The angle (why this video, why now)

Brij Kishore Pandey's Instagram post (April 25, 2026) reframed Claude Code from "coding assistant" to **"the Agent Development Kit"** — a 5-layer architecture where most engineers only touch Layer 1 (CLAUDE.md). The post collected ~50 comments / lots of engagement because it gave one mental model to an otherwise-fragmented set of features (CLAUDE.md, Skills, Hooks, Subagents, Plugins, MCP). This video gives the same one-screen mental model with the official docs facts behind it.

**The promise**: in 8–10 minutes, you understand all 5 layers, when to use each, and where each one sits in the request lifecycle. You leave knowing whether the thing you want to build is a skill, a hook, a subagent, a plugin, or just a line in CLAUDE.md.

---

## Layer 1 — CLAUDE.md (The Memory / Constitution)

**One-paragraph definition**: CLAUDE.md is a markdown file injected into context as a user message at session start. It's persistent project knowledge — Claude reads it but is not strictly bound by it (it's instruction, not enforcement). Multiple files combine: managed (org policy) > user (`~/.claude/CLAUDE.md`) > project (`./CLAUDE.md`) > local (`./CLAUDE.local.md`, gitignored). All discovered files concatenate; subdirectory CLAUDE.md files load on demand when Claude opens files there.

**Where it lives**:
| Scope | Path |
|---|---|
| Managed (org) | `/Library/Application Support/ClaudeCode/CLAUDE.md` (mac), `/etc/claude-code/CLAUDE.md` (linux) |
| User | `~/.claude/CLAUDE.md` |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` |
| Local | `./CLAUDE.local.md` (gitignored) |

**The 200-line rule**: Anthropic recommends keeping each CLAUDE.md under 200 lines. Beyond that, adherence degrades — Claude starts to skim. Auto-memory's `MEMORY.md` index hard-truncates at 200 lines / 25 KB.

**Token cost**: Full content of every CLAUDE.md is loaded **every session, every request**. That's the price of being "always on."

**Best for**: Always-on facts, never-do-X rules, build commands, naming conventions, repo layout, team coding standards.

**Worst for**: Multi-step procedures (use a skill), path-specific rules (use `.claude/rules/` with `paths:` glob), things that must run deterministically at lifecycle points (use a hook).

**Concrete one-liner**: `Always use pnpm, not npm. Run \`pnpm test\` before committing. Handlers live in src/api/handlers/.`

**v2.x changes (May 2026)**:
- `claudeMdExcludes` skips irrelevant monorepo CLAUDE.md files (glob)
- `CLAUDE_CODE_NEW_INIT=1` enables multi-phase `/init`
- `InstructionsLoaded` hook event for debugging which files actually loaded
- Auto-memory writes its own `MEMORY.md` to `~/.claude/projects/<project>/memory/`

---

## Layer 2 — Skills (The Knowledge / Workflows)

**One-paragraph definition**: A skill is a directory containing `SKILL.md` (YAML frontmatter + markdown instructions) plus optional supporting files (scripts/, references/, examples/). Only skill **descriptions** load at session start; full body loads on demand when Claude auto-matches the description to a request, or when the user invokes `/skill-name`. Skills follow the open Agent Skills standard (agentskills.io) — same skills work across multiple AI tools, not just Claude.

**Where it lives**:
| Scope | Path |
|---|---|
| User | `~/.claude/skills/<name>/SKILL.md` |
| Project | `.claude/skills/<name>/SKILL.md` |
| Plugin | `<plugin>/skills/<name>/SKILL.md` (auto-namespaced as `/plugin-name:skill-name`) |

**Frontmatter that matters**:
- `description` — used for auto-trigger; first 1,536 chars matter most
- `disable-model-invocation: true` — user-invoked only; description hidden from Claude (zero token cost)
- `context: fork` + `agent: Explore` — runs the skill in an isolated subagent
- `allowed-tools` — pre-approved tools while skill is active
- `paths:` — glob patterns; auto-activates only when working in matching files

**Token economics**: Description-only at session start (capped at 1,536 chars per skill, ~1% of context budget total). Full SKILL.md only when invoked. Once invoked, skill content stays in conversation; after `/compact`, the most recent invocation re-attaches (5 KB per skill, 25 KB total).

**Progressive disclosure**: Keep SKILL.md under 500 lines. Detail goes in `references/<topic>.md` — Claude reads on demand.

**Auto-trigger**: Claude reads the description, compares to your request, fires the matching skill. This is why descriptions need clear trigger conditions ("Use when reviewing PRs", not "PR review skill").

**Best for**: Reference docs Claude needs sometimes, multi-step procedures, invocable workflows, anything too long for CLAUDE.md.

**Recent (2026) changes**:
- Custom commands (`.claude/commands/<name>.md`) merged into the skill system — same trigger semantics, same frontmatter
- `paths:` glob field for file-pattern auto-activation
- `${CLAUDE_SKILL_DIR}` for self-referencing bundled scripts
- Live reload — edit SKILL.md and Claude picks it up without restart

---

## Layer 3 — Hooks (The Guardrail / Deterministic Layer)

**One-paragraph definition**: Hooks are deterministic handlers that execute at specific lifecycle events in the agentic loop. They are NOT AI — they are shell commands, HTTP calls, MCP tool calls, prompt calls, or subagent invocations triggered by events. A hook returning exit code 2 hard-blocks the action being attempted. Configured in `settings.json` under the `hooks` key; hierarchy mirrors all other settings.

**The 31 events (Claude Code v2.x)**:
- **Session**: SessionStart, Setup, SessionEnd
- **Per-turn**: UserPromptSubmit, UserPromptExpansion, Stop, StopFailure
- **Tool calls**: PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied
- **Subagent/task**: SubagentStart, SubagentStop, TaskCreated, TaskCompleted, TeammateIdle
- **File/context**: FileChanged, CwdChanged, InstructionsLoaded, ConfigChange
- **Compaction**: PreCompact, PostCompact
- **Notifications**: Notification, Elicitation, ElicitationResult
- **Worktree**: WorktreeCreate, WorktreeRemove

**5 hook handler types**:
```json
{ "type": "command", "command": "./scripts/lint.sh" }
{ "type": "http", "url": "http://localhost:8080/hooks" }
{ "type": "mcp_tool", "server": "my_server", "tool": "validate" }
{ "type": "prompt", "prompt": "Is this safe? $ARGUMENTS", "model": "fast" }
{ "type": "agent", "prompt": "Verify the command: $ARGUMENTS" }
```

**Exit code semantics (command hooks)**:
- 0 = success (stdout JSON parsed for decisions)
- 2 = blocking (action blocked; stderr fed to Claude as error)
- 1, 3+ = non-blocking error (continue)

**Best for**: Lint after every Edit. Block `rm -rf`. Auto-format. Notify Slack on Stop. Log every Bash command. Anything that must hold **every time, regardless of what Claude decides**.

**Key insight**: "Never edit `.env`" in CLAUDE.md is a *request*. A `PreToolUse` hook on Edit/Write that exits 2 when the path matches `.env` is *enforcement*.

**Worst for**: Multi-step workflows requiring reasoning (use a skill). Annotation (use CLAUDE.md). Anything where Claude's judgment should determine the outcome.

---

## Layer 4 — Subagents (The Delegation Layer)

**One-paragraph definition**: A subagent is a markdown file at `.claude/agents/<name>.md` with YAML frontmatter and a custom system prompt. Claude delegates matching tasks to it; the subagent runs in its own isolated context window, with its own model, tools, and permissions, and returns only a summary to the main conversation. Context pollution from large searches and file reads stays contained. **No recursion** — subagents cannot spawn other subagents.

**File format**:
```markdown
---
name: code-reviewer
description: Reviews code for quality. Use after code changes.
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. Analyze code and provide specific, actionable feedback...
```

**Built-in subagents**:
- `Explore` — Haiku, read-only, fast codebase search
- `Plan` — inherits model, read-only, used in plan mode
- `general-purpose` — inherits model, all tools

**Frontmatter highlights**:
- `model` — sonnet/opus/haiku/full ID/inherit (route by cost)
- `tools` / `disallowedTools` — capability scope
- `permissionMode` — default/acceptEdits/auto/dontAsk/bypassPermissions/plan
- `skills:` — preload full skill content into subagent context at startup
- `mcpServers` — MCP servers available to this subagent
- `isolation: worktree` — runs in a temporary git worktree (isolated repo copy)
- `background: true` — always runs as background task
- `memory: project` — cross-session auto-memory for this subagent

**Best for**: Context isolation (50-file searches, log analysis), parallel independent work, cost routing (Haiku scout for big reads, Opus for main thread), specialized workers (security-audit, doc-writer, test-runner).

**Worst for**: Knowledge or workflow Claude needs in main context (use a skill instead). Lifecycle enforcement (use a hook).

**Plugin subagents** drop `hooks` / `mcpServers` / `permissionMode` for security — copy to `.claude/agents/` to use those.

---

## Layer 5 — Plugins (The Distribution Layer)

**One-paragraph definition**: A plugin is a self-contained directory bundling skills + agents + hooks + commands + MCP servers + LSP servers + monitors, distributed via marketplaces (official `anthropics/claude-code` GitHub repo, or private team marketplaces via private git). One install command and the entire team gets identical behavior — agent capabilities as distributable, versioned packages.

**Manifest** at `.claude-plugin/plugin.json`:
```json
{
  "name": "my-plugin",
  "description": "What this plugin does",
  "version": "1.0.0",
  "author": { "name": "Author Name" }
}
```

**Directory structure**:
```
my-plugin/
├── .claude-plugin/plugin.json   # Manifest only
├── skills/<name>/SKILL.md       # Auto-namespaced as /my-plugin:name
├── agents/<name>.md             # Subagents
├── hooks/hooks.json             # Hook definitions
├── .mcp.json                    # MCP servers (start when plugin enabled)
├── .lsp.json                    # LSP servers
├── monitors/monitors.json       # Background monitors (stdout → notifications)
├── bin/                         # Executables added to PATH
└── settings.json                # Only `agent` + `subagentStatusLine` keys
```

**Runtime variables**:
- `${CLAUDE_PLUGIN_ROOT}` — plugin install dir (use in hooks/MCP configs)
- `${CLAUDE_PLUGIN_DATA}` — persistent data dir (survives plugin updates)

**Standalone vs Plugin decision**:
- Standalone (`.claude/`) → personal workflows, single project, short skill names
- Plugin → sharing with team or community, multi-project, versioned, marketplace

**Best for**: When the same configuration of skills + agents + hooks + MCP must travel with the team. One install, whole team gets the behavior.

---

## Sidebar — MCP Servers (External Integration, NOT a layer of the ADK)

**One-paragraph definition**: MCP (Model Context Protocol) is the open standard for connecting Claude Code to external tools and data — Postgres, Slack, Jira, GitHub, Figma, browsers, hundreds more. MCP is the wire (the connection); skills are the knowledge (how to use what's on the wire). They compose — you almost always want both.

**Three transports** (HTTP recommended; SSE deprecated; stdio for local processes).

**When to pick MCP vs Skills**:
- Need to **reach** an external system → MCP
- Need to **teach** Claude how to use that system effectively → skill
- Both → both

---

## Comparison Table — One Screen

| Layer | Always loaded? | Token cost | Trigger | Best for | Lives in |
|---|---|---|---|---|---|
| **CLAUDE.md** | Yes | Full content every request | Session start | Always-on facts, project conventions | `CLAUDE.md`, `~/.claude/CLAUDE.md` |
| **Skills** | Description only; body on demand | Low (descriptions) | Description match OR `/skill-name` | Reference docs, repeatable procedures | `.claude/skills/<n>/SKILL.md` |
| **Hooks** | No (event-driven) | Zero unless output | Lifecycle events (31 of them) | Deterministic enforcement, lint, block, log | `hooks` key in `settings.json` |
| **Subagents** | No (spawned on demand) | Isolated context | Auto-delegate via description OR explicit | Context isolation, parallel work, cost routing | `.claude/agents/<n>.md` |
| **Plugins** | When enabled | Same as standalone components | Install + enable | Team-wide bundle distribution | `.claude-plugin/plugin.json` + dirs |
| **MCP** *(sidebar)* | Tool names at start; schemas deferred | Low (Tool Search defers) | Claude picks tool when relevant | External system connectivity | `.mcp.json`, `~/.claude.json` |

---

## The Five Confusions (the deep-dive content of the video)

### 1. CLAUDE.md vs Skills

**Heuristic**: "Claude makes the same mistake twice → CLAUDE.md. You keep pasting the same prompt → skill." If CLAUDE.md is over 200 lines, move reference content to skills.

| Use CLAUDE.md when… | Use a Skill when… |
|---|---|
| Fact applies every session | Content is reference Claude needs sometimes |
| Under 200 lines total | Multi-step procedure with reasoning |
| "Never do X" / "Always do Y" | You want to invoke it explicitly with `/name` |
| Project layout, build commands | Detail too long for CLAUDE.md |

### 2. MCP vs Skills

**They're not alternatives.** MCP is connectivity. Skills are knowledge. You compose them: MCP server connects Claude to your Postgres → skill teaches Claude your data model.

### 3. Skills vs Subagents

| Skill (inline) | Subagent (forked) |
|---|---|
| Knowledge enters main context | Work happens in isolated context |
| Reasoning visible in conversation | Only summary returns |
| Small intermediate output | Large output you won't reference |
| One model | Can route to cheaper/faster model |
| One thread | Multiple parallel subagents |

Skills can fork via `context: fork`. Subagents can preload skills via `skills:`. They compose both directions.

### 4. Hooks vs Skills

| Hook (deterministic) | Skill (reasoning) |
|---|---|
| Same outcome every time | Claude decides how to apply |
| Triggered by lifecycle event | Triggered by request |
| Cannot be reasoned around | Can be skipped if not relevant |
| Enforcement | Guidance |

The combo: PostToolUse hook runs lint → output feeds back as error context → `/fix-lint` skill tells Claude how to remediate.

### 5. Standalone vs Plugin

| Standalone `.claude/` | Plugin |
|---|---|
| Personal or single-project | Team-wide or community |
| Short skill names (`/deploy`) | Namespaced (`/my-plugin:deploy`) |
| Versionless | Versioned releases |
| Local edit + reload | Marketplace install |

---

## Stats / Receipts to use in the video

- Brij's Instagram post (Apr 25, 2026): "5-layer agent architecture — most engineers only touch Layer 1"
- 31 distinct hook events in Claude Code v2.x
- 5 hook handler types: command, http, mcp_tool, prompt, agent
- CLAUDE.md target: under 200 lines (per Anthropic docs)
- Skill description budget: 1,536 chars per skill, ~1% of context window total
- Skills follow the open Agent Skills standard (agentskills.io) — cross-tool portability
- Custom commands now merged into the skill system (one mental model, not two)
- MCP HTTP transport now primary; SSE deprecated
- Built-in subagents: Explore (Haiku, read-only), Plan, general-purpose
- Plugin subagents drop hooks/mcpServers/permissionMode for security

---

## Previous coverage in this channel (avoid repeating verbatim)

Three shorts (committed in `e8c7fcd`, May 3 2026) already covered slices:
- `claude-customization-5-features-short` — 95s overview of the 5 features
- `claudemd-vs-skills-short` — when each wins
- `claude-skills-autotrigger-short` — how description-match works
- `claude-mcp-vs-skills-short` — MCP vs Skills decision
- `claude-skills-vs-commands-short` (likely)

The shorts give the **what**. This long-form gives the **architecture** — the *why* behind the 5 layers, the request lifecycle showing how they interact, and the decision-tree across all 5+1.

---

## Sources

- [How Claude remembers your project (CLAUDE.md)](https://code.claude.com/docs/en/memory)
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Hooks reference](https://code.claude.com/docs/en/hooks)
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [Create plugins](https://code.claude.com/docs/en/plugins)
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference)
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [Extend Claude Code (decision framework)](https://code.claude.com/docs/en/features-overview)
- [Claude Code docs index](https://code.claude.com/docs/llms.txt)
- [Brij Kishore Pandey, Instagram post — "5-layer agent architecture"](https://www.instagram.com/codewithbrij/), Apr 25, 2026
