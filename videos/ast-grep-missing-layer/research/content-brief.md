# Content Brief — ast-grep-missing-layer

> **Format:** long-form, 1920×1080, ~4.5min target (~270s)
> **Template:** `templates/long-form/standard/`
> **Audience:** developers using AI coding agents (Claude Code, Cursor, Copilot)
> **Tone:** tech-influencer-edgy but source-grounded — every number traces to receipts
> **Includes:** Hostinger midroll (~10–15s) + Dynamous outro CTA
> **Synthesis date:** 2026-05-16
> **Source notes (second brain):**
> - `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\brief.md`
> - `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\research\00-summary.md`
> - `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\examples\setup-and-live-test.md`
> - `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\examples\archon-head-to-head.md`
> - `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\sources\ast-grep-github-readme.md`

---

## 1. Topic + angle (thesis)

**Thesis:** `ast-grep` is the missing **Layer 2** in the AI-coding search stack. Every agent — Claude Code, Cursor, Copilot — ships with Layer 1 (ripgrep / ugrep) wired up by default. Almost nobody bolts on Layer 2 (structural / AST-based). The result: agents over-count results by 28–122% on real refactor intents, burn tokens reading false-positive files, and silently fail at refactors that grep+regex literally cannot express (bracket-matched `try…catch`, variadic argument capture, multi-line structural rewrites).

**Angle:** Not "another search tool." Not "ast-grep is faster than grep" (it isn't — both finish sub-second on 400+ files). The angle is **precision-per-token**. For an LLM agent piping search results into Edit operations, every false positive costs a Read call. ast-grep eliminates the triage step.

**One-line video promise:** *"The CLI your AI agent is missing — and the receipts proving it."*

---

## 2. Verified facts (with provenance)

Every load-bearing claim in the script must trace to one of these. If a number isn't here, drop it.

### Tool identity & capability
- ast-grep is a Rust CLI doing structural search/replace via tree-sitter ASTs, with `$VAR` meta-variables in pattern syntax. [source: GitHub README — `D:\...\sources\ast-grep-github-readme.md`]
- 20+ supported languages out of the box (JS/TS/Py/Rust/Go/Java/C/C#/Kotlin/Swift/Ruby/…). [source: ast-grep.github.io homepage, captured in `research/00-summary.md` §1]
- Supports dynamic loading of custom tree-sitter parsers. [source: ast-grep.github.io, `research/00-summary.md` §1]
- `--rewrite` does structural find-and-replace `sed` cannot safely express. [source: `examples/setup-and-live-test.md` §5]
- `--json[=compact|stream|pretty]` outputs structured records with byte ranges + captured meta-variables. [source: live test, `examples/setup-and-live-test.md` §4]
- Install command: `pnpm add -g @ast-grep/cli` → ast-grep `0.42.2`, **5.8s wall-clock** on Windows 11. [source: `examples/setup-and-live-test.md` §1]

### Real codebase head-to-head (the killer proof — Archon repo, 406 TS/TSX files, 11 packages)

| # | Query intent | grep | ast-grep | Over-count | Latency |
|---|---|---|---|---|---|
| 1 | `console.log()` in `.ts` | **164 hits / 22 files** | **130 / 12 files** | +26%, +10 files | 158ms |
| 2 | `useState()` in `.tsx` | **138 / 30 files** | **62 / 26 files** | +122%, +4 files | 102ms |
| 3 | `setTimeout()` in `.ts` | **57 / 23 files** | **48 / 22 files** | +19%, +1 file | 161ms |
| 4 | `.then()` chains in `.ts` | **13 / 9 files** | **10 / 8 files** | +30%, +1 file | 147ms |
| 5 | `try…catch` blocks in `.ts` (structural) | grep **cannot bracket-match** | **415 / 71 files** | ∞ | ~250ms |

[source: `examples/archon-head-to-head.md` — every number traceable to an exact PowerShell command in that doc]

### Repo-internal proof (diy-yt-creator-hyperframes itself)
- `tl.from` baseline: **65 grep hits across 10 files**, of which ~13 are `.md` prose, ~51 are real `<script>` blocks in `.html`, ~1 is real `.js` — agent has to triage manually. [source: `examples/setup-and-live-test.md` §3]
- ast-grep with `--lang js` finds **2,198 real call expressions across 300 files**, zero prose noise — it parses JS inside `<script>` blocks in `.html` automatically. [source: same]
- Real anti-pattern hit: `videos\_test-dynamous\index.html:190` → `tl.from("#dynamous-badge", {...}, 3.0)` — exactly what the repo's `step-by-step-reveal` rule forbids. ast-grep can audit AND rewrite this in one pass. [source: `examples/setup-and-live-test.md` §3b sample]

### The three-layer model
- "AI coding agents largely rely on **ripgrep** as their internal search engine. GitHub Copilot CLI and OpenAI Codex both use it. Claude Code diverged in April 2026, switching to **ugrep + bfs**." [source: ceaksan.com — "grep, ripgrep, and AI-Powered Text Search," captured in `research/00-summary.md` §4]
- Three-layer search stack: Layer 1 exact (ripgrep / ugrep) → Layer 2 structural (ast-grep / grep-ast) → Layer 3 semantic (mgrep / vector). [source: ceaksan.com, `research/00-summary.md` §4]

### Claude Code integration paths
1. **Official Claude Code skill**: `github.com/ast-grep/claude-skill`. [source: ast-grep.github.io/advanced/prompting.html, `research/00-summary.md` §3]
2. **System-prompt directive**: *"For any code search requiring syntax/structure understanding, default to `ast-grep --lang [language] -p '<pattern>'`."* [source: same page, originating @kieranklaussen tweet]
3. **MCP server** (experimental): `github.com/ast-grep/ast-grep-mcp` — flagged as experimental by the project. Don't oversell. [source: same]

---

## 3. The killer proof (lead with this in the script)

The Archon head-to-head is the single strongest receipt in the entire research pack. **One specific demonstration carries the whole video:**

**Setup:** Query `console.log()` across `dynamous/Archon/packages` (406 TS files, 11 packages).
- grep: **164 hits / 22 files**
- ast-grep `--lang ts`: **130 hits / 12 files**

**Where the 10 extra files came from:** grep matched `console.log` inside **string literals used as test fixtures**. Receipts:

```ts
// workflows/src/dag-executor.test.ts:2813
{ script: 'console.log("hi")' }

// workflows/src/dag-executor.test.ts:6043
script: 'console.log("hello from bun")',

// workflows/src/dag-executor.test.ts:6082
{ id: 'compute', script: 'console.log("42")', runtime: 'bun' },
```

Archon's workflow engine *executes* user-supplied JS scripts, so its tests literally pass `'console.log("hi")'` as **data**. grep can't tell a call from a string. ast-grep skipped them all because the AST classifies them as `string_literal`, not `call_expression`.

[source: `examples/archon-head-to-head.md` Query 1 — every receipt traceable to that doc]

**Why it lands:** It's visual (open the file, highlight the line), specific (file path + line number + raw content), and the user can reproduce it in 30 seconds on their own Archon clone.

---

## 4. The three-layer framing (video structure backbone)

Use this as the narrative spine. The viewer leaves the video with a mental model, not just a tool recommendation.

- **Layer 1 — Exact (`ripgrep` / `ugrep`)** — what every agent uses today. Universal. Dumb-fast. Doesn't understand code.
- **Layer 2 — Structural (`ast-grep`)** — the missing middle. Knows what's a call vs. a comment vs. a string. Captures meta-variables. Can rewrite.
- **Layer 3 — Semantic (`mgrep` / vector search)** — "find code like this" by meaning. Heavier, less mature.

[source: ceaksan.com, captured in `research/00-summary.md` §4]

**Visual treatment for this scene:** a 3-tier diagram. Each tier gets a label, a tool logo, and one example query showing what it answers. Reveal Layer 1 first (already familiar), then Layer 2 with a "this is where the gap is" emphasis, then Layer 3 as future-state.

> **Care note:** the article's "mgrep ~2× fewer tokens" claim is single-anecdotal — flagged in `research/00-summary.md` §5. If used in script, attribute as *"some authors report"* — don't state as fact.

---

## 5. Claude Code angle — token economics

The receipt for "why this matters for AI agents":

**With grep alone, an agent auditing Archon for stale `console.log` calls:**
1. Runs grep → 164 matches / 22 files
2. Reads every file to triage (22 Read calls × ~500 tokens ≈ **~11K tokens of file context**)
3. Identifies 34 false positives in 10 test/generated files
4. Edits the remaining 130 real call sites

**With ast-grep, same task:**
1. Runs `ast-grep -p 'console.log($$$A)' -l ts --json=compact` → structured list of 130 calls in 12 files, with byte ranges + captured args
2. Pipes JSON directly into batch Edits using byte ranges
3. Skips the triage entirely

**Conservative receipt:** ~**10K tokens saved per medium refactor**. [source: `examples/archon-head-to-head.md` §"agent-coding angle"]

This is the single most defensible "why now" beat in the video.

---

## 6. Counter-arguments (steelman the skeptic — REQUIRED scene)

The "wait, but…" beat. Cover these three explicitly so the comments section doesn't.

1. **"My codebase is too small."** — Fair. On 5 files, grep is fine. The precision win compounds with size — at 400+ files (Archon), grep over-counts by 26–122%. [source: `research/00-summary.md` §7, `examples/archon-head-to-head.md` table]
2. **"My IDE / LSP already does this."** — Partially true *within a single language*. LSP refactors don't span multiple langs in one repo, don't ship as a pipeable CLI, and don't expose structured JSON for an agent to consume. ast-grep does all three. [source: `research/00-summary.md` §7]
3. **"semgrep does more."** — True: semgrep adds taint analysis, dataflow, security rules. It's also heavier, has its own DSL, and is framed for security work. For everyday refactor and search, ast-grep's pattern syntax is closer to "writing the code I want to find." [source: `research/00-summary.md` §7]

A fourth, lighter one: **"This is just a refactor tool."** — Actually three jobs in one binary: structural search, structural rewrite, lint engine (via `scan` + YAML rules). [source: `research/00-summary.md` §7]

**Honest limit to disclose:** ast-grep is **syntactic only** — no types, no dataflow, no taint. For semantic refactors (rename across a typed API), still need an LSP-aware tool. Don't oversell. [source: `research/00-summary.md` §1]

---

## 7. Hook candidates (pick one in Phase 2)

Each is built around a single verified receipt. The script writer picks the one that fits the chosen energy.

**H1 — The over-count slam (RECOMMENDED).**
> *"Your AI agent just searched 22 files. Only 12 of them had what it was looking for. The other 10? grep lied. Here's the CLI that doesn't."*
Anchor: Archon `console.log` Query 1 (164 / 22 vs 130 / 12). [source: `examples/archon-head-to-head.md` Query 1]

**H2 — The impossible-query slam.**
> *"This — `try { … } catch (err) { … }` — is one grep can't write. ast-grep finds 415 of them in 250 milliseconds. Here's why every agent is missing a layer."*
Anchor: Archon Query 5 — grep cannot bracket-match. [source: `examples/archon-head-to-head.md` Query 5]

**H3 — The three-layer reveal.**
> *"Every AI coding agent has Layer 1. Almost none have Layer 2. The gap is costing you 10,000 tokens per refactor."*
Anchor: token economics math + three-layer model. [source: `research/00-summary.md` §4, `examples/archon-head-to-head.md` §agent-coding angle]

**H4 — The string-literal gotcha.**
> *"This line — `script: 'console.log("hi")'` — is a string. Not a call. grep counts it anyway. Your agent reads the whole file to figure that out. Here's the fix."*
Anchor: dag-executor.test.ts:2813 receipt. [source: `examples/archon-head-to-head.md` Query 1]

---

## 8. Banned phrases (AI-slop closers — auto-fail in Phase 2.5)

Do NOT ship the script with any of these:
- "game-changer" / "game-changing"
- "revolutionary"
- "you won't believe"
- "level up your workflow"
- "blazing fast" (used by upstream marketing — fine in a quoted source attribution, banned as the script's own voice)
- "supercharge"
- "in this video, we'll explore…"
- "let me know in the comments" (without an actual debate question — see §9)
- "what do you think?"
- "drop your thoughts below"
- "how would you build this differently?" (banned per `.claude/rules/engagement-cta.md`)

Per `.claude/rules/engagement-cta.md` anti-patterns list — these all flunk QG-2b.

---

## 9. Engagement CTA candidates (pick one in Phase 2)

Per `.claude/rules/engagement-cta.md`: must be binary/short-list answerable, polarizing, reference a specific claim from the video, low-cost to answer in 5 seconds.

**CTA-1 (RECOMMENDED) — Pick-a-side, references receipts:**
> *"grep over-counted by 122% on a real refactor. Are you giving ast-grep to your coding agent today — or still pretending Layer 1 is enough?"*
Triggers: tool-tribalism + specific receipt (the 122% useState number).

**CTA-2 — Adoption deadline:**
> *"Three months from now — will your agent still be searching code as plain text, or will it finally understand the AST?"*
Triggers: forces a prediction the viewer wants to defend.

**CTA-3 — Hot-take confirm:**
> *"ast-grep as a default tool in every coding agent — overdue, or overkill?"*
Triggers: binary, polarizing, restates the video's thesis directly.

The visual element (per `engagement-cta.md` §"the visual element") goes in the final phase of `index.html` as `id="cta-question"`, ≥36px for long-form, persists through the thumbnail-grade final frame.

---

## 10. Visual proof candidates (scenes that earn screen-shareable visuals)

Map of which research artifacts get screen time. Phase 1 (plan) picks the actual scenes; this is the candidate menu.

| Scene candidate | Visual asset | Source |
|---|---|---|
| Cold open / hook | Animated counter slamming `164 → 130` with file-count `22 → 12` below | Archon Query 1 numbers |
| Layer model reveal | 3-tier diagram (Exact / Structural / Semantic) with tool logos | ceaksan.com framing |
| The killer false-positive | Screenshot of `workflows/src/dag-executor.test.ts:2813` with the string literal highlighted in red | Archon Query 1 receipt |
| Numbers wall | The 5-query head-to-head table animated row-by-row | Archon head-to-head table |
| Impossible-query beat | Live terminal capture of `ast-grep run --pattern 'try { $$$BODY } catch ($ERR) { $$$CBODY }' --lang ts` returning 415 matches in ~250ms | Archon Query 5 |
| Rewrite preview | Live diff from `--rewrite` on `stat-pill-pop.js` (this repo) — show the diff, then the honest caveat (first-draft, not production-ready) | setup-and-live-test §5 |
| Token economics | Side-by-side flow: "agent w/ grep: 22 Reads ≈ 11K tokens" vs "agent w/ ast-grep: 0 Reads, JSON pipe" | Archon §agent-coding angle |
| Hostinger midroll slot | (template-provided banner; placement TBD by Phase 1) | n/a — sponsor cut |
| Three integration paths | Cards: Skill / System-prompt / MCP (experimental) | research/00-summary.md §3 |
| Counter-args steelman | Three skeptic-cards: "too small," "my IDE," "semgrep does more" | research/00-summary.md §7 |
| CTA / final frame | `cta-question` element + Dynamous endcard | engagement-cta + dynamous outro rule |

---

## 11. Hostinger midroll (placement guidance for Phase 1)

The standard long-form template's midroll slot. Per CLAUDE.md memory: **"Hostinger is affiliate-only, NOT sponsored"** — banner headline says "Try Hostinger" not "Sponsored by." Werbung badge stays for DE law.

Tonal note: the midroll cuts in around the natural break between "here's the problem (numbers)" and "here's the solution (live demo)." Don't drop it inside the Archon receipts beat — that's the highest-tension moment. Put it AFTER the receipts land but BEFORE the live rewrite demo.

---

## 12. Dynamous outro (locked spoken line)

Per `.claude/rules/...` and memory feedback: spoken outro = SHORT pointer line, locked to:

> *"If you want to learn more about AI, check out the dynamous.ai community."*

Endcard carries the rest visually. Long outsider AND insider variants are deprecated. Don't deviate.

---

## 13. Hard rules recap (Phase 2 enforcement checklist)

- Every script line, on-screen text, command, and stat traces to one of the five second-brain files above. [HARD RULE — source-grounded only, no fabrication]
- No web research — research is done. Phase 2 pulls receipts from the brief, not from search.
- The Archon head-to-head numbers are the spine. Don't trade them for vaguer claims.
- Don't claim ast-grep is "faster than grep." It isn't (both sub-second). The pitch is **precision**, not speed.
- Don't claim "Claude Code switched to ugrep + bfs" as fact without re-verifying — `research/00-summary.md` §5 flags this as plausible-but-unconfirmed. Either re-verify or attribute as *"per one independent author."*
- Don't claim "mgrep is 2× more token-efficient" as fact — single anecdotal source, attribute or drop.
- Disclose the honest limit: ast-grep is syntactic only — no types, no dataflow.
- Engagement CTA exists in all three places (spoken + on-screen `#cta-question` + youtube-description.md) and they agree.

---

## 14. Gaps requiring user input

None blocking for Phase 1. Two soft items the script writer may flag back:

1. **Hostinger banner copy** — does this video use the standard "Try Hostinger" treatment or a topic-specific tagline ("the host built for shipping side projects"-style)? Default to standard if unclear.
2. **Final-frame topic slam wording** — `"AST-GREP IS THE MISSING LAYER"` vs `"YOUR AGENT IS MISSING LAYER 2"` vs `"AGENTS NEED MORE THAN GREP"`. Phase 1 picks; brief recommends "YOUR AGENT IS MISSING LAYER 2" for thumbnail-test recognizability.

---

## Reference paths (Phase 2 receipts)

- `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\brief.md`
- `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\research\00-summary.md`
- `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\examples\setup-and-live-test.md`
- `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\examples\archon-head-to-head.md`
- `D:\Nextcloud\Obsidian\sync\smartcode\Videos\ast-grep\sources\ast-grep-github-readme.md`
