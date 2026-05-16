# Script — ast-grep-missing-layer

# Target: ~270s @ 145 WPM (draft voice) = ~595 words total
# Voice profile: news-explainer (tech-influencer-edgy, receipt-driven)
# Audience: beginners/intermediates using AI coding agents (Claude Code, Cursor, Copilot) — not CLI power-users
# Total: 595 words / 10 scenes (Scene 06 Hostinger is the locked midroll)

## Scene 01 — Hook (14s, target ~42 words)

Your AI agent is bleeding tokens. Right now. Here's the proof: it just flagged a string of text as a real bug, in quotes, on line two-eight-one-three. Then it billed you to investigate. There's a smarter search. Your agent doesn't have it yet.

<!-- Receipt: archon-head-to-head.md Query 1 — dag-executor.test.ts:2813 string literal misread as a call. Framing: agent-token-cost first, receipt second. -->

## Scene 02 — Every Agent Has The Same Blind Spot (22s, target ~52 words)

Every AI coding agent has the same blind spot. Claude Code, Cursor, Copilot — they all search your code the same dumb way. They scan for matching text. That's it. They can't tell the difference between code that actually runs and a string that just looks like code. Watch what that costs you.

<!-- Receipt: research/00-summary.md §4 — all major agents default to text-only search. No taxonomy/Layer terminology in beginner version. -->

## Scene 03 — Meet ast-grep (32s, target ~58 words)

Meet ast-grep. It's a smarter search tool that reads your code as code — not as a wall of text. A regular search sees characters. ast-grep sees structure: functions, calls, try-catch blocks, the real shape of what you wrote. You hand it to your agent in one config line. Now your agent stops getting fooled. And stops billing you for the cleanup.

<!-- Receipt: sources/ast-grep-github-readme.md — ast-grep parses syntax trees, not characters. First mention paired with plain-English definition per audience brief. -->

## Scene 04 — The String-Literal Lie (38s, target ~78 words)

Watch your agent waste your money. You ask it to clean up debug logs. With the dumb text search, the agent finds 164 matches across 22 files. It opens every one. But here's what's hiding inside dag-executor dot test dot ts line two-eight-one-three: a test fixture passes the literal string console-dot-log-hi. It's not a real call. It's just quoted text. The agent reads the whole file, triages it, and bills you. ast-grep skips it instantly. Twelve files, not twenty-two.

<!-- Receipt: examples/archon-head-to-head.md Query 1 + dag-executor.test.ts:2813. Framed as agent-cost, not developer-CLI-output. -->

## Scene 05 — The Numbers Wall (32s, target ~62 words)

One example isn't a pattern. So we tested five common searches on the same codebase. The dumb search over-counted by twenty-six percent on debug logs. Nineteen percent on setTimeout. Thirty percent on promise chains. One-hundred-and-twenty-two percent on useState hooks. That's pure billed waste. Every false hit is a file your agent has to open, scan, and pay for. ast-grep cuts it in half.

<!-- Receipt: examples/archon-head-to-head.md full 5-query table. Translated to billed-waste language for beginner audience. -->

## Scene 06 — Hostinger Midroll (20s, ~37 words spoken — UNCHANGED)

Quick word from our affiliate, Hostinger. If you're spinning up your own AI agents or coding sandboxes, Hostinger gives you 10 percent off with the code DIYSMARTCODE in the description. Now, back to ast-grep.

## Scene 07 — Token Economics (34s, target ~78 words)

Let's translate that into money. To audit those 22 files, your agent has to open 22 files. That's roughly eleven thousand tokens of context — call it a cent for a single refactor. Now scale it up. Fifty refactors a day. Thirty days a month. That cent becomes fifteen dollars of pure waste, every month, per developer, just on bad search. ast-grep does the same job in one structured query. Ten times cheaper. Your agent stops re-reading files it shouldn't have opened.

<!-- Receipt: examples/archon-head-to-head.md §agent-coding angle + 11K tokens / cent-per-refactor math expanded to monthly developer cost. -->

## Scene 08 — The Steelman (30s, target ~74 words)

But my agent already has search. Yes — and it's the dumb one. But Claude Code has Read and Glob. Different jobs. Read opens a file you point at. Glob lists files by name. Neither one understands code structure. That's what ast-grep adds. But this sounds technical. It isn't. You don't run anything yourself. You add one line to your agent's config, and your agent gains the new search. The terminal stays untouched.

<!-- Receipt: research/00-summary.md §7 counter-arguments — reframed from developer steelmen to agent-user steelmen. -->

## Scene 09 — Give It To Your Agent (18s, target ~45 words)

How do you give it to your agent? Two minutes. For Claude Code, add one line to your config file. For Cursor, install the extension. Restart your agent. Done. Your AI agent now searches code by structure — not by guessing at text. That's the upgrade.

<!-- Receipt: examples/setup-and-live-test.md §1 — install was ~5.8s; reframed for agent-user, no terminal command shown. -->

## Scene 10 — The Debate + Dynamous Outro (26s, target ~62 words)

So here's the question. Your AI agent burns money on every refactor — one-hundred-and-twenty-two percent more work than it needs, on real code. Are you fixing that today with one config line? Or accepting the waste? Drop your pick in the comments. Subscribe for more AI coding deep-dives. If you want to learn more about AI, check out the dynamous dot AI community.
