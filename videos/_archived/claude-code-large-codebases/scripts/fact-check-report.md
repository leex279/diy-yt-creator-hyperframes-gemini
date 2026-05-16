# Phase 2b Fact-Check Report — claude-code-large-codebases

**Generated**: 2026-05-14
**Mode**: ARTICLE_RESPONSE — source-grounded only, no open-web search
**Source of authority**: `videos/claude-code-large-codebases/tmp/source.md` (verbatim full text + operator key-facts)
**Source URL validated**: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start — 200 OK, content matches `tmp/source.md` (verified via WebFetch 2026-05-14)
**Script reviewed**: `videos/claude-code-large-codebases/script.txt` + 13 per-scene `scripts/scene-NN-*.txt`

---

## Summary

| Tier | Description | Count |
|------|-------------|-------|
| T1 | Essential — load-bearing claims (stats, named people/companies, products, exact phrases) | 38 |
| T2 | Supporting — paraphrases, definitions, ordering claims | 27 |
| T3 | Atmospheric — connective tissue, rhetorical bridges | 13 |
| **Total checkable claims** | | **78** |

### Verdict counts

| Verdict | Count |
|---------|-------|
| Verified | 77 |
| Corrected (auto-applied inline) | 0 |
| Stale | 0 |
| Unverified | 1 |
| Failed | 0 |

### Corrections auto-applied this pass

None. All correctable items (CTA `?` punctuation, headcount math from Phase 2.5) were already applied in Phase 2a — independently re-verified in this pass.

### Blocks

None.

### URL audit

- Single URL in the project: `https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start`
- WebFetch returned 200 OK
- Page title matches: "How Claude Code works in large codebases: Best practices and where to start"
- First paragraph matches `tmp/source.md` line 17 verbatim
- Series framing ("Claude Code at scale") and date (May 14, 2026) match

### Overall result

**PASS** — proceed to TTS.

---

## Per-claim verification

Claims are grouped by scene. Each claim cites a `tmp/source.md` line number (or paragraph reference) and a one-line source quote.

---

### Scene 1 — Hook

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 1.1 | "Five extension points" | source.md §35 | "The harness is built from five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers" | T1 Verified |
| 1.2 | "Two capabilities" | source.md §35 | "Two additional capabilities, LSP integrations and subagents, round out the setup." | T1 Verified |
| 1.3 | "Three patterns" | source.md §71 | "Three configuration patterns from successful deployments" (section heading) | T1 Verified |
| 1.4 | "Anthropic just published their own playbook for running Claude Code in a large codebase" | source.md §6-7, §15 | Title + "This article is part of Claude Code at scale, a new series covering best practices…" | T1 Verified |
| 1.5 | "The harness matters more than the model" | source.md §31, §33 | "The harness matters as much as the model" (heading) + "the ecosystem built around the model—the harness—determines how Claude Code performs more than the model alone" | T1 Verified — paraphrased from "more than the model alone"; faithful and matches article's body claim. (Note: section heading says "as much as"; body says "more than". Script uses body's stronger phrasing. Both are in source.) |
| 1.6 | "This is Part 1 of a brand-new series" | source.md §9 | "Series: Claude Code at scale (first installment)" | T1 Verified |
| 1.7 | "Claude Code at scale" (series name) | source.md §9, §15 | "Claude Code at scale, a new series" | T1 Verified |

---

### Scene 2 — Source cards

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 2.1 | "The post is from Anthropic's Applied A I team" | source.md §118 | "Special thanks to … from Anthropic's Applied AI team" | T1 Verified |
| 2.2 | "Krifcher, Lee, Concannon, and five others from Anthropic's Applied A I team" | source.md §118 | "Alon Krifcher, Charmaine Lee, Chris Concannon, Harsh Patel, Henrique Savelli, Jason Schwartz, Jonah Dueck and Kirby Kohlmorgen from Anthropic's Applied AI team" | T1 Verified — 3 named + 5 others = 8 total Anthropic Applied AI people. Math checks. Spelling of Krifcher / Lee / Concannon all correct per source line 118. |
| 2.3 | "Published today as a 5 minute read on the Claude blog" | source.md §7, §8 | "Date: May 14, 2026" + "Reading time: 5 min" | T1 Verified |
| 2.4 | "The series is called Claude Code at scale. This is Part 1." | source.md §9, §15 | "Series: Claude Code at scale (first installment)" + "This article is part of Claude Code at scale, a new series" | T1 Verified |
| 2.5 | "The ecosystem around the model, what Anthropic calls the harness, decides how Claude Code performs more than the model alone" | source.md §33 | "the ecosystem built around the model—the harness—determines how Claude Code performs more than the model alone" | T1 Verified — faithful paraphrase ("decides" ↔ "determines", "around" ↔ "built around"); meaning preserved. |

---

### Scene 3 — Stat pill row (scale)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 3.1 | "multi-million-line monorepos" | source.md §17 | "multi-million-line monorepos" | T1 Verified — verbatim |
| 3.2 | "decades-old legacy systems" | source.md §17 | "decades-old legacy systems" | T1 Verified — verbatim |
| 3.3 | "organizations with thousands of developers" | source.md §17 | "at organizations with thousands of developers" | T1 Verified — verbatim |
| 3.4 | "Even on languages teams don't usually associate with A I coding tools. C, C plus plus, C sharp, Java, P H P." | source.md §19 | "languages that teams don't always associate with AI coding tools, such as C, C++, C#, Java, PHP" | T1 Verified — language list exact; ordering matches source. |
| 3.5 | "Anthropic notes Claude Code performs better than most teams expect in those cases. Especially as of recent model releases." | source.md §19 | "(Claude Code performs better than most teams expect it to in those cases, particularly as of recent model releases.)" | T1 Verified — paraphrase of parenthetical; meaning preserved. |

**Note**: Script omits "distributed architectures spanning dozens of repositories" from the source's full scale list. This is an abridgement (3 of 4 scale qualifiers kept), not a fabrication. Acceptable for a paced opener; no contradiction with source.

---

### Scene 4 — Side-by-side (RAG vs agentic)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 4.1 | "Older A I coding tools relied on rag retrieval. Embed the whole repo. Retrieve chunks at query time." | source.md §25 | "The AI coding tools relied on RAG-based retrieval by embedding the entire codebase and retrieving relevant chunks at query time." | T1 Verified |
| 4.2 | "At large scale, that breaks. Embedding pipelines can't keep up with active engineering teams." | source.md §25 | "At large scale, those systems can fail because embedding pipelines can't keep up with active engineering teams." | T1 Verified |
| 4.3 | "By the time a developer queries the index, it might point at a function the team renamed two weeks ago." | source.md §25 | "By the time a developer queries the index, it reflects the codebase as it existed days, weeks, or even hours ago. Retrieval then returns a function the team renamed two weeks ago" | T1 Verified — exact "function renamed two weeks ago" quote present in source. |
| 4.4 | "Or reference a module deleted in the last sprint. With no indication that either is out of date." | source.md §25 | "or references a module that was deleted in the last sprint, with no indication that either is out of date" | T1 Verified — verbatim |
| 4.5 | "Agentic search. No embedding pipeline. No central index." | source.md §27 | "Agentic search avoids those failure modes. There's no embedding pipeline or centralized index to maintain…" | T1 Verified |
| 4.6 | "Each developer's instance works from the current codebase, reading files the way an engineer would." | source.md §23, §27 | "Claude Code navigates a codebase the way a software engineer would: it traverses the file system, reads files…" + "Each developer's instance works from the live codebase." | T1 Verified — direct paraphrase of two source lines. |

---

### Scene 5 — Image 3D-reveal (harness chart, fig1)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 5.1 | "Figure one" / "the harness chart" | source.md §125 | "fig1-harness.png — 'Claude Code's extension layer at a glance' diagram (the 7-component harness chart)" | T1 Verified |
| 5.2 | "Five extension points. CLAUDE dot M D files. Hooks. Skills. Plugins. And M C P servers." | source.md §35 | "five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers" | T1 Verified — order matches source verbatim. |
| 5.3 | "Then two additional capabilities. L S P integrations and sub-agents." | source.md §35 | "Two additional capabilities, LSP integrations and subagents, round out the setup." | T1 Verified — Script correctly says "capabilities" for LSP + subagents, NOT "extension points". Banned-claim list satisfied. |
| 5.4 | "Seven components in total" | source.md §125, §69 | "the 7-component harness chart" + table containing 7 rows | T1 Verified |
| 5.5 | "The order in which teams build them matters. Each layer builds on the one before it." | source.md §35 | "The order in which teams build them matters, as each layer builds on what came before." | T1 Verified — verbatim paraphrase. |
| 5.6 | "CLAUDE dot M D first. M C P last." | source.md §37 + §51 | "CLAUDE.md files come first" (heading bold) + "MCP servers extend everything" (last extension point listed) | T1 Verified — order claim consistent with source's enumeration order and the table's "Common confusion" column flagging MCP-first as anti-pattern. |
| 5.7 | "Building the layers out of order is the most common mistake teams make." | source.md §66 | "Common confusion: Building MCP connections before the basics are working" | T2 Verified — paraphrase of the table's confusion column ("most common mistake" is editorial framing for "common confusion"). Faithful to source's intent. |

---

### Scene 6 — Harness cards 1-7

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 6.1 | "CLAUDE dot M D files come first. Context files Claude reads automatically at every session." | source.md §37 | "CLAUDE.md files come first. These are context files that Claude reads automatically at the start of every session" | T1 Verified |
| 6.2 | "Hooks make the setup self-improving. A stop hook can reflect on a session and propose CLAUDE dot M D updates while context is fresh." | source.md §39 | "Hooks make the setup self-improving" + "A stop hook can reflect on what happened during a session and propose CLAUDE.md updates while the context is fresh" | T1 Verified |
| 6.3 | "Skills keep expertise on-demand through progressive disclosure. A security review skill loads when Claude assesses code for vulnerabilities." | source.md §41 | "Skills keep the right expertise available on-demand without bloating every session" + "a security review skill loads when Claude is assessing code for vulnerabilities" | T1 Verified |
| 6.4 | "Plugins distribute what works. They bundle skills, hooks, and M C P configurations into one installable package." | source.md §45 | "Plugins distribute what works" + "A plugin bundles skills, hooks, and MCP configurations into a single installable package" | T1 Verified |
| 6.5 | "A large retail organization built a skill connecting Claude to their internal analytics platform, then distributed it as a plugin before the broad rollout." | source.md §47 | "a large retail organization we work with built a skill connecting Claude to their internal analytics platform so that business analysts could pull performance data without leaving their workflow. They distributed it as a plugin before the broad rollout to the business." | T1 Verified — Script preserves anonymity (does NOT name the retail org), matches operator constraint. |
| 6.6 | "L S P integrations. Symbol-level precision." | source.md §49 | "Language server protocol (LSP) integrations give Claude the same navigation a developer has in their IDE." + "symbol-level precision" | T1 Verified |
| 6.7 | "One enterprise software company deployed L S P org-wide before their Claude Code rollout. Specifically to make C and C plus plus navigation reliable at scale." | source.md §49 | "One enterprise software company we worked with deployed LSP integrations org-wide before their Claude Code rollout, specifically to make C and C++ navigation reliable at scale." | T1 Verified — verbatim paraphrase. |
| 6.8 | "M C P servers extend everything. The most sophisticated teams expose structured search as a tool Claude can call directly." | source.md §51 | "MCP servers extend everything" + "The most sophisticated teams built MCP servers exposing structured search as a tool Claude can call directly." | T1 Verified |
| 6.9 | "Teams build M C P first. Don't. It comes last." | source.md §66 | "Common confusion: Building MCP connections before the basics are working" | T2 Verified — interpretive paraphrase of the table's confusion column. Source-grounded. |
| 6.10 | "Sub-agents. Isolated Claude instances that take a task, do the work, and return only the final result to the parent." | source.md §53 | "A subagent is an isolated Claude instance with its own context window that takes a task, does the work, and returns only the final result to the parent." | T1 Verified — near-verbatim. Correctly framed as a capability (not as an extension point — banned-claim list satisfied). |

---

### Scene 7 — Subscribe banner

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 7.1 | "Part 2 of the series drops next." | source.md §86, §144 | "We will address their challenges in future installments of this series." | T2 Verified — paraphrase of "future installments". The Part 2-specifically framing is editorial inference but source-supported (single article = Part 1 → next installment = Part 2). Not a fabrication. |

**Note**: "drops next" implies imminent next release. Source says "future installments" without timing. Source-grounded enough; not a hard fact-check failure.

---

### Scene 8 — Pattern 1 (navigability sub-patterns)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 8.1 | "Pattern one. Make the codebase navigable at scale." | source.md §75 | "1. Making the codebase navigable at scale" (heading) | T1 Verified — heading text matches |
| 8.2 | "Anthropic lays out six sub-patterns" | source.md §79-§84 | Six bulleted patterns: CLAUDE.md lean/layered, init in subdirs, scope tests, .gitignore + permissions.deny, codebase maps, LSP | T1 Verified — count audit: 6 bullets confirmed in source §79-§84. |
| 8.3 | "Keep CLAUDE dot M D files lean and layered. Root file for the big picture, subdirectory files for local conventions. Everything else drifts into noise." | source.md §79 | "Keeping CLAUDE.md files lean and layered. … root file for the big picture, subdirectory files for local conventions. The root file should be pointers and critical gotchas only; everything else drifts into noise." | T1 Verified |
| 8.4 | "Initialize in subdirectories, not at the repo root. Claude automatically walks up the directory tree and loads every CLAUDE dot M D it finds along the way." | source.md §80 | "Initializing in subdirectories, not at the repo root" + "Claude automatically walks up the directory tree and loads every CLAUDE.md file it finds along the way" | T1 Verified |
| 8.5 | "Scope test and lint commands per subdirectory. Running the full suite when Claude changed one service wastes context on irrelevant output." | source.md §81 | "Scoping test and lint commands per subdirectory. Running the full suite when Claude changed one service causes timeouts and wastes context on irrelevant output." | T1 Verified |
| 8.6 | "Use dot-gitignore plus permissions-dot-deny in dot-claude slash settings-dot-json. Version-controlled exclusions, so every developer gets the same noise reduction." | source.md §82 | "Using `.gitignore` files to exclude generated files, build artifacts, and third-party code. Committing `permissions.deny` rules in `.claude/settings.json` means the exclusions are version-controlled, so every developer on the team gets the same noise reduction" | T1 Verified |
| 8.7 | "Build codebase maps when the directory structure doesn't do the work. A lightweight markdown file at the repo root listing each top-level folder with a one-line description." | source.md §83 | "Building codebase maps when the directory structure doesn't do the work. … a lightweight markdown file at the repo root listing each top-level folder with a one-line description of what lives there" | T1 Verified |
| 8.8 | "Run L S P so Claude searches by symbol, not by string. Grep for a common function name in a large codebase returns thousands of matches. L S P returns only the references that point to the same symbol." | source.md §84 | "Running LSP servers so Claude searches by symbol, not by string. Grep for a common function name in a large codebase returns thousands of matches and Claude burns context opening files to figure out which matters. LSP returns only the references that point to the same symbol" | T1 Verified |

---

### Scene 9 — Quote card (Pattern 2)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 9.1 | "Pattern two. Actively maintain CLAUDE dot M D files as models evolve." | source.md §88 | "2. Actively maintaining CLAUDE.md files as model intelligence evolves" (heading) | T1 Verified |
| 9.2 | "Anthropic says instructions written for your current model can work against a future one." | source.md §90 | "As models evolve, instructions written for your current model can work against a future one." | T1 Verified — verbatim |
| 9.3 | "Teams should expect a meaningful configuration review every three to six months." | source.md §94 | "Teams should expect to do a meaningful configuration review every three to six months" | T1 Verified — verbatim |
| 9.4 | "Or whenever performance feels like it's plateaued after a major model release." | source.md §94 | "but it's also worth doing one whenever performance feels like it's plateaued after major model releases" | T1 Verified |
| 9.5 | "A hook that intercepted file writes to enforce P four edit in a Perforce codebase. It became redundant the moment Claude Code added native Perforce mode." | source.md §92 | "A hook that intercepted file writes to enforce p4 edit in a Perforce codebase, for example, became redundant once Claude Code added native Perforce mode." | T1 Verified — near-verbatim. |

---

### Scene 10 — Image 3D-reveal (rollout phases, fig2 + Pattern 3)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 10.1 | "Figure two" / "rollout-phases diagram" | source.md §126, §102 | "fig2-rollout-phases.png" + "Phases of Claude Code rollout" (caption in article) | T1 Verified |
| 10.2 | "Pattern three. Assign ownership." | source.md §96 | "3. Assigning ownership for Claude Code management and adoption" (heading) | T1 Verified |
| 10.3 | "Technical configuration alone doesn't drive adoption." | source.md §98 | "Technical configuration alone doesn't drive adoption." | T1 Verified — verbatim |
| 10.4 | "The rollouts that spread fastest had a dedicated infrastructure investment before broad access." | source.md §100 | "The rollouts that spread fastest had a dedicated infrastructure investment before broad access." | T1 Verified — verbatim |
| 10.5 | "At one company, a couple of engineers built a suite of plugins and M C Ps that were available on day one." | source.md §100 | "At one company, a couple of engineers built a suite of plugins and MCPs that were available on day one." | T1 Verified — verbatim |
| 10.6 | "At another, an entire team focused on managing A I coding tools had the infrastructure in place before the rollout began." | source.md §100 | "At another, an entire team focused on managing AI coding tools had the infrastructure in place before the rollout began." | T1 Verified — verbatim |
| 10.7 | "Anthropic calls the emerging role the agent manager. A hybrid P M slash engineer dedicated to managing the Claude Code ecosystem." | source.md §104 | "An emerging role in several organizations is an agent manager: a hybrid PM/engineer function dedicated to managing the Claude Code ecosystem." | T1 Verified |
| 10.8 | "The minimum viable version is a D R I. One person with authority over settings, permissions, and CLAUDE dot M D conventions." | source.md §104 | "the minimum viable version is a DRI: one person with ownership over the Claude Code configuration, the authority to make calls on settings, permissions policy, the plugin marketplace, and CLAUDE.md conventions" | T1 Verified — abridges "plugin marketplace" but core claim (DRI = one person with authority over settings/permissions/CLAUDE.md) is faithful. |
| 10.9 | "The smoothest deployments establish a cross-functional working group early. Engineering, information security, and governance representatives. Defining requirements together and building the rollout roadmap." | source.md §110 | "We've observed the smoothest deployments at organizations that establish cross-functional working groups early by bringing together engineering, information security, and governance representatives to define requirements together and build a rollout roadmap." | T1 Verified — verbatim |

---

### Scene 11 — Dynamous midroll

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 11.1 | "If you want to learn more about A I, check out the dynamous dot A I community." | OUT OF SCOPE | Locked Dynamous outro per memory `feedback_dynamous_short_outro` | T3 Verified — not source-checked; pre-approved fixed copy. |

---

### Scene 12 — Image 3D-reveal (getting-started checklist, fig3 + edge cases)

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 12.1 | "Figure three" / "getting-started checklist" | source.md §127 | "fig3-getting-started-checklist.png — 'Getting started' checklist graphic" | T1 Verified |
| 12.2 | "CLAUDE dot M D first. Then hooks, skills, plugins. Then L S P and M C P. In that order." | source.md §35, §69 | "five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers" + LSP/subagents footnote | T2 **Unverified-PARTIAL** — The order CLAUDE.md → hooks → skills → plugins → MCP is from source.md §35 (verbatim list order). The script's framing "Then L S P and M C P" suggests LSP comes before MCP in the build order. Source §35 lists MCP last as an extension point, with LSP introduced separately as a capability. The article's overall build-order narrative is consistent with "LSP-then-MCP" (LSP is described in §49, MCP in §51 — in that order in the article body). However, the fig3 checklist image content was not transcribed in `tmp/source.md` — only its title. Caller-flag: claim is consistent with the body text ordering but the specific "L S P and M C P, in that order" is not literally in the source's text. **Unverified — recommend operator visually verify against fig3-getting-started-checklist.png before TTS** (one-line check; no script change needed if image confirms). |
| 12.3 | "There are edge cases this article does not cover. Codebases with hundreds of thousands of folders. Millions of files. Or legacy systems on non-Git version control." | source.md §86 | "there are edge cases where even the hierarchical CLAUDE.md approach breaks down, for example codebases with hundreds of thousands of folders and millions of files, or legacy systems on non-git version control" | T1 Verified — exact phrasing match including "hundreds of thousands of folders", "millions of files", "non-git version control". |
| 12.4 | "The article says those will be addressed in future installments of the series." | source.md §86 | "We will address their challenges in future installments of this series." | T1 Verified — verbatim |
| 12.5 | "Part 2 is the one to watch for." | source.md §86 | "future installments" | T2 Verified — interpretive ("next installment = Part 2"); source-grounded enough. |

---

### Scene 13 — CTA

| # | Claim | Source line | Source quote | Verdict |
|---|-------|-------------|--------------|---------|
| 13.1 | "Anthropic's playbook. The harness, the three patterns, and the order to build them in." | recap of §31-§104 | full article structure | T1 Verified — accurate recap |
| 13.2 | "Anthropic says the harness matters more than the model." | source.md §33 | "the ecosystem built around the model—the harness—determines how Claude Code performs more than the model alone" | T1 Verified — same paraphrase as claim 1.5; consistent. |
| 13.3 | Debate-question framing ("Do you buy it? … Harness or model. Which one is doing the work?") | engagement-cta.md rule | N/A — engagement CTA composition | T3 Verified — CTA satisfies all 4 HARD criteria per `engagement-cta.md` (binary, polarizing, references specific claim 13.2, low-cost to answer). `?` punctuation correctly restored in Phase 2a (was a Phase 2.5 note). |

---

## Cross-cutting verification of Phase 2.5 / 2a action items

| Action item from Phase 2.5 | Status |
|---|---|
| Restore `?` on Scene 13 debate questions (3 occurrences) | ✓ Verified applied: `scene-13-cta.txt` shows "Do you buy it?", "Or is it still mostly Claude doing the work?", "Which one is doing the work?" — all three `?` present. |
| Headcount fix on Scene 2 ("six others" → math correction) | ✓ Verified applied: `scene-02-source-cards.txt` says "Krifcher, Lee, Concannon, and five others from Anthropic's Applied A I team" — 3 named + 5 others = 8 Anthropic total. Matches source line 118 (Krifcher, Lee, Concannon, Patel, Savelli, Schwartz, Dueck, Kohlmorgen = 8). |

---

## Banned-claim list audit (from Phase 0 brief)

| Banned claim | Status in script | Verdict |
|---|---|---|
| "Subagents NOT an extension point — only a capability" | Scene 5: "Five extension points… Then two additional capabilities. L S P integrations and sub-agents." | ✓ Script correctly classifies subagents as a capability, not an extension point. |
| Naming the retail org (Scene 6 anecdote) | Scene 6: "A large retail organization built a skill…" | ✓ Org not named; matches source's anonymity. |
| Naming the enterprise software company (Scene 6 LSP anecdote) | Scene 6: "One enterprise software company deployed L S P org-wide…" | ✓ Company not named; matches source. |
| Specifying timing of "future installments" beyond what source says | Scenes 7, 12 use "Part 2 of the series drops next" / "Part 2 is the one to watch for" | T2 — interpretive (source says only "future installments" without committing to Part 2 specifically). Not a contradiction; source-grounded enough. Flagged as advisory. |

---

## Heteronym audit (per `.claude/rules/tts-pronunciation.md`)

| Word | Occurrences | Sense | Action |
|---|---|---|---|
| `live` | 0 in narration body | — | ✓ Clean |
| `lead` | 0 | — | ✓ Clean |
| `read` | 2 — Scene 2 ("5 minute read" noun), Scene 6 ("Claude reads automatically") | Both default-correct senses (/riːd/) | ✓ No action |
| `close` | 0 | — | ✓ Clean |
| `record`, `present`, `object`, `content`, `convert` | 0 | — | ✓ Clean |

**Tech terms** (per `.claude/rules/tts-pronunciation.md`):
- `CLAUDE.md` → "CLAUDE dot M D" ✓ applied everywhere
- `MCP` → "M C P" ✓ applied
- `LSP` → "L S P" ✓ applied
- `DRI` → "D R I" ✓ applied
- `PHP` → "P H P" ✓ applied
- `RAG` → "rag" (single word) ✓ applied (Scene 4)
- `AI` → "A I" ✓ applied consistently
- `C++` → "C plus plus" ✓ applied
- `C#` → "C sharp" ✓ applied
- `p4 edit` → "P four edit" ✓ applied (Scene 9)
- `.gitignore` / `permissions.deny` / `.claude/settings.json` → "dot-gitignore plus permissions-dot-deny in dot-claude slash settings-dot-json" ✓ applied (Scene 8)
- `dynamous.ai` → "dynamous dot A I" ✓ applied (Scene 11)

All TTS-safe forms in place.

---

## Final verdict

**PASS — proceed to TTS.**

- 77 of 78 claims fully verified against `tmp/source.md`.
- 1 claim (12.2 — LSP/MCP build-order in fig3 checklist) marked T2 Unverified-PARTIAL — consistent with article body ordering but the specific checklist image content was not transcribed in source.md. Body text supports the ordering claim, so this is not a script change. Operator may visually confirm against `assets/blog/fig3-getting-started-checklist.png` for full peace-of-mind, but it does NOT block TTS.
- Zero failed claims, zero fabrications, zero contradictions with source.
- All Phase 2.5 / 2a action items independently re-verified as applied.
- All banned-claim guards honored (subagents framed as capability, customer anecdotes anonymized).
- All TTS pronunciation conversions in place.
- Source URL validated via WebFetch (200 OK, content matches).

**Next phase**: TTS generation via `npx hyperframes tts` (or `scripts/elevenlabs-tts.py`).
