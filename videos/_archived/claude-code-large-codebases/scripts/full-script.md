# Full Script — claude-code-large-codebases

**Generated**: 2026-05-14
**Source authority**: `tmp/source.md` (verbatim Anthropic blog post)
**Target**: ~1280 words @ 160 WPM over 478.5s of narration + 1.5s tail = 480s
**Tone**: friendly-educational. Source-grounded language only.

---

## Scene 1: scene-hook

Five extension points. Two capabilities. Three patterns. [MM: 5 extension points + 2 capabilities = 7-component harness] Anthropic just published their own playbook for running Claude Code in a large codebase. And the part most teams miss is this. The harness matters more than the model. This is Part 1 of a brand-new series. Claude Code at scale. [MM: First installment of "Claude Code at scale" series] So here is what is in the playbook. And here is the order Anthropic says to build it in.

## Scene 2: scene-source-cards

The post is from Anthropic's Applied AI team. Krifcher, Lee, Concannon, and six others. Published today as a 5 minute read on the Claude blog. The series is called Claude Code at scale. This is Part 1. And the post lays out one thesis right at the top. The ecosystem around the model, what Anthropic calls the harness, decides how Claude Code performs more than the model alone. Everything that follows is a breakdown of that harness.

## Scene 3: scene-stat-pill-row

Anthropic says Claude Code is now running in production across multi-million-line monorepos, decades-old legacy systems, and at organizations with thousands of developers. [MM: multi-million-line monorepos / thousands of developers] Even on languages teams don't usually associate with A I coding tools. C, C plus plus, C sharp, Java, P H P. [MM: Languages C / C++ / C# / Java / PHP] Anthropic notes Claude Code performs better than most teams expect in those cases. Especially as of recent model releases.

## Scene 4: scene-side-by-side

So how does Claude Code actually navigate a codebase this big? The article explains it. Older A I coding tools relied on R A G retrieval. Embed the whole repo. Retrieve chunks at query time. At large scale, that breaks. Embedding pipelines can't keep up with active engineering teams. [MM: Why RAG fails at scale — index lag] By the time a developer queries the index, it might point at a function the team renamed two weeks ago. Or reference a module deleted in the last sprint. With no indication that either is out of date. Claude Code does it differently. Agentic search. [MM: Claude Code uses agentic search, no embedding index] No embedding pipeline. No central index. Each developer's instance works from the current codebase, reading files the way an engineer would.

## Scene 5: scene-image-3d-reveal (#1) — fig1-harness.png

This is the harness chart from Anthropic's article. Figure one. The playbook in a single table. Five extension points. CLAUDE dot M D files. Hooks. Skills. Plugins. And M C P servers. Then two additional capabilities. L S P integrations and sub-agents. Seven components in total. And Anthropic is explicit about one thing. The order in which teams build them matters. Each layer builds on the one before it. CLAUDE dot M D first. M C P last. [MM: Order matters — CLAUDE.md first, MCP last] Building the layers out of order is the most common mistake teams make.

## Scene 6: scene-list-cards-harness

Here is the breakdown card by card. Card one. CLAUDE dot M D files come first. Context files Claude reads automatically at every session. Card two. Hooks make the setup self-improving. A stop hook can reflect on a session and propose CLAUDE dot M D updates while context is fresh. Card three. Skills keep expertise on-demand through progressive disclosure. A security review skill loads when Claude assesses code for vulnerabilities. Card four. Plugins distribute what works. They bundle skills, hooks, and M C P configurations into one installable package. Anthropic gives a concrete example. A large retail organization built a skill connecting Claude to their internal analytics platform, then distributed it as a plugin before the broad rollout. [MM: Large retail organization with internal-analytics plugin] Card five. L S P integrations. Symbol-level precision. One enterprise software company deployed L S P org-wide before their Claude Code rollout. Specifically to make C and C plus plus navigation reliable at scale. [MM: Enterprise software co. with org-wide LSP for C/C++] Card six. M C P servers extend everything. The most sophisticated teams expose structured search as a tool Claude can call directly. And the article calls out the common confusion here. Teams build M C P first. Don't. It comes last. Card seven. Sub-agents. Isolated Claude instances that take a task, do the work, and return only the final result to the parent.

## Scene 7: scene-subscribe-banner

Quick beat. If this playbook is useful to you, hit subscribe. Part 2 of the series drops next.

## Scene 8: scene-list-cards-pattern1

Pattern one. Make the codebase navigable at scale. Anthropic lays out six sub-patterns. One. Keep CLAUDE dot M D files lean and layered. Root file for the big picture, subdirectory files for local conventions. Everything else drifts into noise. Two. Initialize in subdirectories, not at the repo root. Claude automatically walks up the directory tree and loads every CLAUDE dot M D it finds along the way. Three. Scope test and lint commands per subdirectory. Running the full suite when Claude changed one service wastes context on irrelevant output. Four. Use dot-gitignore plus permissions-dot-deny in dot-claude slash settings-dot-json. Version-controlled exclusions, so every developer gets the same noise reduction. Five. Build codebase maps when the directory structure doesn't do the work. A lightweight markdown file at the repo root listing each top-level folder with a one-line description. Six. Run L S P so Claude searches by symbol, not by string. Grep for a common function name in a large codebase returns thousands of matches. L S P returns only the references that point to the same symbol. [MM: Pattern 1 sub-patterns — 6 items]

## Scene 9: scene-quote-card

Pattern two. Actively maintain CLAUDE dot M D files as models evolve. Anthropic says instructions written for your current model can work against a future one. Teams should expect a meaningful configuration review every three to six months. [MM: 3-6 month review cadence] Or whenever performance feels like it's plateaued after a major model release. The article gives one concrete example. A hook that intercepted file writes to enforce P four edit in a Perforce codebase. It became redundant the moment Claude Code added native Perforce mode.

## Scene 10: scene-image-3d-reveal (#2) — fig2-rollout-phases.png

This is the rollout-phases diagram from Anthropic's article. Figure two. Pattern three. Assign ownership. Technical configuration alone doesn't drive adoption. The rollouts that spread fastest had a dedicated infrastructure investment before broad access. Anthropic names two concrete examples. At one company, a couple of engineers built a suite of plugins and M C Ps that were available on day one. [MM: Plugin+MCP suite available day one] At another, an entire team focused on managing A I coding tools had the infrastructure in place before the rollout began. [MM: Dedicated AI-coding-tools team] Anthropic calls the emerging role the agent manager. A hybrid P M slash engineer dedicated to managing the Claude Code ecosystem. [MM: Agent manager is hybrid PM/engineer] The minimum viable version is a D R I. One person with authority over settings, permissions, and CLAUDE dot M D conventions. And the smoothest deployments establish a cross-functional working group early. Engineering, information security, and governance representatives. Defining requirements together and building the rollout roadmap. [MM: Cross-functional working group = engineering + info-sec + governance]

## Scene 11: scene-dynamous-midroll

If you want to learn more about A I, check out the dynamous dot A I community.

## Scene 12: scene-image-3d-reveal (#3) — fig3-getting-started-checklist.png

This is the getting-started checklist from Anthropic's article. Figure three. The action items at the end of the post. CLAUDE dot M D first. Then hooks, skills, plugins. Then L S P and M C P. In that order. And one caveat from Anthropic. There are edge cases this article does not cover. Codebases with hundreds of thousands of folders. Millions of files. Or legacy systems on non-Git version control. [MM: Edge cases not covered — hundreds-of-thousands of folders / non-Git VCS] The article says those will be addressed in future installments of the series. So if your environment is in that bucket, Part 2 is the one to watch for. The rest of us can start applying the playbook today.

## Scene 13: scene-cta

So that is Anthropic's playbook. The harness, the three patterns, and the order to build them in. Anthropic says the harness matters more than the model. Do you buy it. Or is it still mostly Claude doing the work. Drop your pick below. Harness or model. Which one is doing the work.

---

## Phase 2a Optimizations Applied

**Generated**: 2026-05-14
**Output**: 13 per-scene `.txt` files in `scripts/scene-NN-*.txt` + flat `script.txt` at video root.
**Total narration words after optimization**: 1235 (was 1266 in raw script — delta from `[MM: ...]` annotation strip + the changes below).
**Flat `script.txt` character count**: 7454 chars.

### 1. Phase 2.5 action items applied

- **`?` restored on Scene 13 debate questions** (3 occurrences):
  - `Do you buy it.` → `Do you buy it?`
  - `Or is it still mostly Claude doing the work.` → `Or is it still mostly Claude doing the work?`
  - `Which one is doing the work.` → `Which one is doing the work?`
  - Total `?` restorations: **3**. No other rhetorical questions in the script needed restoration — Scene 4's "So how does Claude Code actually navigate a codebase this big?" already had `?`.

- **Anthropic team headcount fix** (Scene 2): recommended option applied (cleaner, Anthropic-only attribution).
  - Before: `"Krifcher, Lee, Concannon, and six others."`
  - After: `"Krifcher, Lee, Concannon, and five others from Anthropic's Applied A I team."`
  - This matches the 8 Anthropic Applied-AI members in `tmp/source.md` acknowledgements (3 named + 5 unnamed = 8 total). Drops Amit Navindgi from the spoken byline (he is from Zoox / external reviewer, not Applied AI team).

### 2. Tech-term replacements (heteronym + acronym TTS optimization)

- **`R A G` → `rag`** (Scene 4, 1 occurrence): per the brief's TTS table, `RAG` reads cleaner as the one-word `rag` than spelled-out letters. Replaced `"R A G retrieval"` → `"rag retrieval"`.
- All other tech-term replacements were already applied in Phase 2 / `full-script.md`:
  - `CLAUDE.md` → `CLAUDE dot M D` (10+ occurrences across Scenes 5, 6, 8, 9, 10, 12)
  - `MCP` → `M C P` (Scenes 5, 6, 10, 12) — and `M C Ps` plural (Scene 10)
  - `LSP` → `L S P` (Scenes 5, 6, 8, 10, 12)
  - `DRI` → `D R I` (Scene 10)
  - `PHP` → `P H P` (Scene 3)
  - `AI` → `A I` (multiple scenes — consistent throughout)
  - `p4 edit` → `P four edit` (Scene 9)
  - `.gitignore` → `dot-gitignore` (Scene 8)
  - `permissions.deny` → `permissions-dot-deny` (Scene 8)
  - `.claude/settings.json` → `dot-claude slash settings-dot-json` (Scene 8)
  - `PM/engineer` → `P M slash engineer` (Scene 10)
  - `C++` → `C plus plus` (Scenes 3, 6)
  - `C#` → `C sharp` (Scene 3)

### 3. Heteronym audit results

Scanned per `.claude/rules/tts-pronunciation.md` heteronym table. Results:

- **`live`** — 0 occurrences in problematic adjective sense. (No "live codebase", "live today", "live on the platform" anywhere. Scene 4's narration uses `"current codebase"` — was already corrected in Phase 2.)
- **`lead`** — 0 occurrences (no noun-sense "lead agent" / "lead engineer" anywhere).
- **`read`** — 3 occurrences, all in correct senses:
  - Scene 2: `"a 5 minute read"` (noun, /riːd/, ElevenLabs reads correctly)
  - Scene 5: `"Claude reads automatically"` (verb, present-tense, correct)
  - Scene 6: `"Claude reads automatically"` (same, correct)
- **`close`** / **`record`** / **`object`** / **`present`** — 0 occurrences in problematic senses.
- **No heteronym swaps required** in this script.

### 4. Annotation strip

- All `[MM: ...]` must-mention annotations from Phase 2 stripped before per-scene files were written. Every must-mention is still present in narration (15/15 per Phase 2.5 QG-6 — verified preserved):
  - 7-component harness (5+2), Claude Code at scale series, multi-million-line monorepos, thousands of developers, C/C++/C#/Java/PHP languages, RAG-fails-at-scale (index lag), agentic search (no embedding index), order matters (CLAUDE.md first / MCP last), large retail org analytics plugin, enterprise software co. org-wide LSP, Pattern 1 sub-patterns (6 items), 3-6 month review cadence, plugin+MCP suite available day one, dedicated AI-coding-tools team, agent manager (hybrid PM/engineer), cross-functional working group, edge cases not covered.

- All `## Scene N:` markdown headers stripped from per-scene `.txt` files (the optimizer reads narration-only files).

### 5. Per-scene character count audit

| Scene | File | Chars | Words | >800 char risk? |
| ----- | ---- | ----- | ----- | --------------- |
| 1 | `scene-01-hook.txt` | 374 | 67 | OK |
| 2 | `scene-02-source-cards.txt` | 471 | 84 | OK |
| 3 | `scene-03-stat-pill-row.txt` | 404 | 63 | OK |
| 4 | `scene-04-side-by-side.txt` | 674 | 113 | OK |
| 5 | `scene-05-image-3d-reveal-harness.txt` | 514 | 91 | OK |
| 6 | `scene-06-list-cards-harness.txt` | **1326** | 215 | **YES — chunk-boundary risk** |
| 7 | `scene-07-subscribe-banner.txt` | 95 | 18 | OK |
| 8 | `scene-08-list-cards-pattern1.txt` | **1109** | 176 | **YES — chunk-boundary risk** |
| 9 | `scene-09-quote-card.txt` | 514 | 82 | OK |
| 10 | `scene-10-image-3d-reveal-rollout.txt` | **990** | 148 | **YES — chunk-boundary risk** |
| 11 | `scene-11-dynamous-midroll.txt` | 79 | 17 | OK |
| 12 | `scene-12-image-3d-reveal-checklist.txt` | 609 | 109 | OK |
| 13 | `scene-13-cta.txt` | 283 | 52 | OK |
| — | **Flat `script.txt`** | **7454** | **1235** | — |

Scenes 6, 8, 10 each exceed 800 chars — these are the dense card-enumeration / pattern-3 scenes flagged in Phase 2.5 Pass 3 as +20–26% over per-scene word targets. The flat `script.txt` is what `npx hyperframes tts` reads, and ElevenLabs chunks by paragraph (blank-line separated) — so each paragraph corresponds to one scene chunk. The 1326-char Scene 6 paragraph may trigger an internal sub-chunk split inside ElevenLabs; if a pronunciation seam appears at TTS time, it likely lands inside Scene 6's card 4 or 5 narration. **Action if seam detected post-TTS**: split Scene 6's paragraph at "Card four." or "Card five." with a manual blank line in `script.txt` for re-generation.

### 6. Items NOT applied (intentional)

- **Contractions optimization** (Phase 2.5 advised: optional convert "Here is" → "Here's"): NOT applied. Phase 2.5 marked this advisory-only; the deliberate "Here is" weighting reads with friendly-educational pacing. Operator can manually convert in scenes 1 + 6 if rhythm seems off after first TTS preview.
- **No SSML tags / `<break>` / `[PAUSE]` markers** added — `eleven_multilingual_v2` doesn't honor SSML per `.claude/rules/tts-pronunciation.md`, and the flat `script.txt` is what TTS reads (per-scene `.txt` files mirror the same content with no SSML).
