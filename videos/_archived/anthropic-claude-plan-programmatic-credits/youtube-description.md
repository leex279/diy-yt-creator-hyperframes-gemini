Claude Agent SDK programmatic credit splits your Claude plan in two: interactive Claude Code (IDE/CLI/desktop) usage stays in your existing plan budget, and a new $20–$200 monthly programmatic credit covers Agent SDK calls, `claude -p`, Claude Code GitHub Actions, and third-party SDK apps like OpenClaw and Archon. Starting June 15, every paid Claude plan (Pro $20, Max 5× $100, Max 20× $200, Team, Enterprise) gets the new credit. Plus Claude Code weekly limits jumped +50% through July 13. Net upside for most builders — but the $20 Pro cap matters if you're running heavy Agent SDK loops.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

What this Anthropic change actually does:
- Before June 15: third-party autonomous Claude agents like OpenClaw were BANNED from authenticating through your Claude subscription — they required a separate Anthropic API setup, separately billed. Dev harnesses like Archon (which wrap your Claude Code workflow rather than acting as autonomous agents) sat in a gray zone, operating through your Claude Code session. Your own Agent SDK scripts and `claude -p` calls counted against the same usage limit as your interactive IDE/CLI Claude Code work — heavy overnight scripts ate your next-day Claude Code budget.
- Starting June 15, Anthropic clears the rules. Programmatic usage moves off your Claude plan's interactive budget into a new dedicated credit pool. The monthly programmatic credit is completely separate from your IDE budget.
- Third-party Agent SDK tools — including the previously-banned autonomous-agent class (OpenClaw and others like it) — can now officially authenticate through your Claude plan and draw from this credit pool. This is the bigger headline than the budget split: Anthropic is opening the gates to third-party agents that were locked out.
- Plan credit amounts (verified from Anthropic's support article): Pro $20, Max 5× $100, Max 20× $200, Team $20 or $100, Enterprise $20 or $200. Free plan: not eligible.
- The catch: the Pro cap is small. $20 burns in a few hundred Agent SDK calls. Hit the ceiling with "extra usage" opted in, you flow to standard API rates per token. Without extra usage, every SDK request hard-stops until the next month.
- Rollout timeline: nothing changes today. June 8, every paid Claude user gets an email with the claim link. June 15, the new programmatic credit goes into effect across every Agent SDK surface.
- Separately, Claude Code weekly limits +50% boost through July 13 — already applied across CLI, IDE extensions, desktop, and web. No opt-in. Unrelated to the programmatic credit, but a parallel update.
- Community reaction split three ways — HAPPY (interactive and programmatic finally separate, no more SDK scripts eating IDE budget), SKEPTICAL (the $20 Pro cap matters more than the split if you're running heavy Agent SDK loops), CONFUSED (what counts as programmatic vs interactive — Hooks? Sub-agents? The line isn't clear).

Chapters
0:00 Claude Plan Just Split In Two: Programmatic Credit + IDE Budget Now Separate
0:17 How Claude Agent SDK Used to Eat Your Claude Code Budget (And Why That's Over)
1:02 Plan Credit Amounts: Pro $20 / Max 5× $100 / Max 20× $200 / Team / Enterprise
1:15 Programmatic Credit Rollout Timeline (Today / June 8 Email / June 15 In Effect)
1:30 The $20 Pro Cap Catch: Extra Usage API Rates vs Hard-Stop Until Next Month
1:49 Builders Are Split: Happy, Skeptical, Confused — Community Reactions
2:11 Net Upside for Most: Two Budgets Beats One, But Is the Ceiling Tall Enough?
2:25 Generous Anthropic Move, or Just Enough Rope to Hang Yourself? — Drop Your Pick

Resources:
Anthropic Agent SDK programmatic credit support article: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
Claude Code product page: https://claude.com/claude-code
Anthropic newsroom: https://www.anthropic.com/news
ClaudeDevs on X (source thread): https://x.com/ClaudeDevs
Archon (open-source agent OS built on the Claude Agent SDK): https://github.com/coleam00/Archon
OpenClaw (open-source Agent SDK wrapper): https://github.com/openclaw/openclaw

Key Concepts:
- Claude Agent SDK programmatic credit — a new dedicated monthly credit attached to paid Claude AI plans (Pro $20, Max 5× $100, Max 20× $200, Team, seat-based Enterprise) that covers Claude Agent SDK usage, the `claude -p` command, Claude Code GitHub Actions, and third-party apps built on the Agent SDK that authenticate through your Claude subscription. Goes into effect June 15. Free plan: not eligible.
- Two-budget separation — before June 15 every Agent SDK call counted against the same plan budget as interactive Claude Code IDE/CLI/desktop work. After June 15 they are completely separate buckets. Interactive Claude Code usage is unchanged; programmatic gets its own pool. Net user-favorable for most builders who run any SDK scripts.
- Cap-size trade-off — $20 of programmatic credit on Pro burns in a few hundred Agent SDK calls. With "extra usage" opted in, overage flows to standard Anthropic API rates per token. With extra usage off, every SDK request hard-stops until the next monthly refresh. There's no middle ground — the cap size decides whether the split is genuinely useful for your workflow.
- Third-party Agent SDK tools (OpenClaw, Archon) — two different shapes of "agent on Claude". OpenClaw was an autonomous-agent class previously BANNED from authenticating through your Claude subscription pre-June-15. Archon is a dev harness wrapping Claude Code workflows — it operated through your Claude Code session in a gray zone. Starting June 15 both classes can officially authenticate through your Claude plan and draw from your programmatic credit pool the same way your own Python scripts do.
- Claude Code weekly limits +50% — already applied to all Pro, Max, Team, and seat-based Enterprise accounts, running through July 13 at 6PM PDT across CLI, IDE extensions, desktop, and web. Nothing to opt into. A parallel update — not part of the programmatic credit rollout, but landing in the same week.

Twenty bucks of programmatic credit on Pro — generous Anthropic move, or just enough rope to hang yourself? Drop your pick below.

#ClaudeAgentSDK #AgentSDK #ProgrammaticCredit #OpenClaw #Archon #ClaudeCode #ClaudeAI #Anthropic #ClaudePricing #ClaudeUsageLimits #ClaudeCodeLimits #ClaudePro #ClaudeMax #ClaudeCodeUpdate #ClaudeCodeTutorial #AIAgent #AIAgents #AgenticAI #ClaudeSubagents #AICoding #DevTools #AI #Programming
