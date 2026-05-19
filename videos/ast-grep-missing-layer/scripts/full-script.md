# Script — ast-grep-missing-layer

# Target: ~440s @ 150 WPM = ~1100 words total
# Voice profile: news-explainer (tech-influencer-edgy, receipt-driven)
# Audience: beginners/intermediates using AI coding agents (Claude Code, Cursor, Copilot) — not CLI power-users
# Total: ~1100 words / 12 scenes (Scene 06 Hostinger is the locked midroll)

## Scene 01 — Hook (14s, target ~42 words)

Your AI agent is bleeding tokens. Right now. Here's the proof: it just flagged a string of text as a real bug, in quotes, inside a test fixture. Then it billed you to investigate. There's a smarter search. Your agent doesn't have it yet.

<!-- Receipt: archon-head-to-head.md Query 1 — dag-executor.test.ts:2813 string literal misread as a call. Framing: agent-token-cost first, receipt second. -->

## Scene 02 — Every Agent Has The Same Blind Spot (22s, target ~52 words)

Every AI coding agent has the same blind spot. Claude Code, Cursor, Copilot — they all lean heavily on text search for exact code hunts. But text search can't tell a real call from a string. And that's where ast-grep wins. Watch what that costs you.

<!-- Receipt: research/00-summary.md §4 — all major agents default to text-only search. No taxonomy/Layer terminology in beginner version. -->

## Scene 03 — Meet ast-grep (32s, target ~58 words)

Meet ast-grep. It's a smarter search tool that reads your code as code — not as a wall of text. A regular search sees characters. ast-grep sees structure: functions, calls, try-catch blocks, the real shape of what you wrote. You hand it to your agent in one config line. Now your agent stops getting fooled. And stops billing you for the cleanup.

<!-- Receipt: sources/ast-grep-github-readme.md — ast-grep parses syntax trees, not characters. First mention paired with plain-English definition per audience brief. -->

## Scene 03b — How ast-grep Works (82s, target ~205 words)

But how does it actually work? Three steps. First, your code gets parsed by a library called tree-sitter. It turns every line into a tree of nodes — functions, calls, arguments, strings, comments — each one tagged by what it actually is. That tree is called an AST. Second, ast-grep matches patterns against the tree, not against the text. You write a pattern that looks like real code, with a meta-variable for the parts that change. Dollar-sign-VAR matches any single node. Three dollar signs, BODY, matches any list of nodes. So if you ask for console-dot-log of dollar-sign-VAR, ast-grep finds every real call — and skips every string that just looks like one. A console-dot-log written inside a comment, or inside quoted text, isn't a call node. It can't match a call pattern. Third, it runs in Rust on every CPU core, so a full codebase scan is fast. That's it. Tree-sitter for the shape. Pattern matching on nodes. Multi-core in Rust. Now your agent doesn't get fooled.

<!-- Receipt: https://ast-grep.github.io/advanced/how-ast-grep-works.html — written in Rust, multi-thread, tree-sitter-based parser, AST pattern matching. -->

## Scene 04 — The String-Literal Lie (38s, target ~78 words)

Watch your agent waste your money. You ask it to clean up dee-bug logs. With the dumb text search, the agent finds 164 matches across 22 files. It opens every one. But here's what's hiding inside dag-executor dot test dot ts: a test fixture passes the literal string console-dot-log-hi. It's not a real call. It's just quoted text. The agent reads the whole file, triages it, and bills you. ast-grep skips it instantly. Twelve files, not twenty-two.

<!-- Receipt: examples/archon-head-to-head.md Query 1 + dag-executor.test.ts:2813. Framed as agent-cost, not developer-CLI-output. -->

## Scene 05 — The Numbers Wall (32s, target ~62 words)

One example isn't a pattern. So we tested five common searches on the same codebase. The dumb search over-counted by twenty-six percent on dee-bug logs. Nineteen percent on setTimeout. Thirty percent on promise chains. One-hundred-and-twenty-two percent on useState hooks. That's pure billed waste. Every false hit is a file your agent has to open, scan, and pay for. ast-grep cuts it in half.

<!-- Receipt: examples/archon-head-to-head.md full 5-query table. Translated to billed-waste language for beginner audience. -->

## Scene 06 — Hostinger Midroll (20s, ~37 words spoken — UNCHANGED)

Quick word from our affiliate, Hostinger. If you're spinning up your own AI agents or coding sandboxes, Hostinger gives you 10 percent off with the code DIYSMARTCODE in the description. Now, back to ast-grep.

## Scene 07 — Token Economics (34s, target ~78 words)

Let's translate that into money. To audit those 22 files, your agent has to open 22 files. That's roughly eleven thousand tokens of context — call it a cent for a single refactor. Now scale it up. Fifty refactors a day. Thirty days a month. That cent becomes fifteen dollars of pure waste, every month, per developer, just on bad search. ast-grep does the same job in one structured query. Ten times cheaper. Your agent stops re-reading files it shouldn't have opened.

<!-- Receipt: examples/archon-head-to-head.md §agent-coding angle + 11K tokens / cent-per-refactor math expanded to monthly developer cost. -->

## Scene 07b — vs Other Tools (66s, target ~165 words)

But isn't this just semgrep? Or comby? Or the structural search in my IDE? No. Here's why. Semgrep is heavier. It does taint analysis, dataflow, security rules — powerful, but slow as a CLI, and overkill for everyday refactors. Comby is generic and syntax-aware, but it doesn't give you ast-grep's language-specific AST node precision. GritQL is a multi-paradigm DSL with logic-programming clauses — a real learning curve before you write your first rule. IntelliJ's structural search is powerful, but it's tied to the JetBrains IDE ecosystem. ast-grep is the lightweight middle. A pipeable command-line tool. Twenty-plus languages out of the box. Easy patterns that look like real code. Fast enough to run inside an agent loop every few seconds. That's the point. Not the deepest analyzer. Not the broadest text tool. Your agent's daily search hammer.

<!-- Receipt: https://ast-grep.github.io/advanced/tool-comparison.html — semgrep heavier/slow CLI, comby no language-awareness/no Python indentation, GritQL multi-paradigm DSL learning curve, IntelliJ locked to one IDE. -->

## Scene 08 — The Steelman (30s, target ~74 words)

But my agent already has search. Yes — and it's the dumb one. But Claude Code has Read and Glob. Different jobs. Read opens a file you point at. Glob lists files by name. Neither one understands code structure. That's what ast-grep adds. But this sounds technical. It isn't. You don't run anything yourself. You add one line to your agent's config, and your agent gains the new search. The terminal stays untouched.

<!-- Receipt: research/00-summary.md §7 counter-arguments — reframed from developer steelmen to agent-user steelmen. -->

## Scene 09 — Give It To Your Agent (38s, target ~95 words)

Giving your agent ast-grep takes two commands. One — install the command-line tool: N P M install dash-G at-ast-grep slash C L I. Two — install the agent skill: N P X skills add ast-grep slash agent-skill. Then restart Claude Code and tell it explicitly: use ast-grep to find. That last part matters — as of today, you have to name the tool out loud, or the agent will fall back to its old text search. Your agent now has the smart search it should have had from day one.

<!-- Receipt: https://github.com/ast-grep/agent-skill — two install steps + explicit-prompting gotcha as of Nov 2025. -->

## Scene 10 — The Debate + Dynamous Outro (26s, target ~62 words)

So here's the question. Your AI agent burns money on every refactor — one-hundred-and-twenty-two percent more work than it needs, on real code. Are you fixing that today with one config line? Or accepting the waste? Drop your pick in the comments. Subscribe for more AI coding deep-dives. If you want to learn more about AI, check out the dynamous dot AI community.
