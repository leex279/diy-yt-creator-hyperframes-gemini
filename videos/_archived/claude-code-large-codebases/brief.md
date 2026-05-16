## Video Brief

**Topic**: How Claude Code works in large codebases — Anthropic's playbook (ARTICLE_RESPONSE to the official Claude blog post in the new "Claude Code at scale" series)

**Slug**: claude-code-large-codebases

**Template**: long-form/anthropic

**Duration**: 8min

**Tone**: friendly-educational

**Links**:
- https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

**Target Audience**: Engineering leaders, platform / DX teams, senior developers at companies running Claude Code in monorepos / legacy systems / large multi-repo environments. Secondary: individual developers who want to set up their own large codebase well.

**Key Angle**: Anthropic is publishing their own playbook for Claude Code at scale — the 5 extension points (CLAUDE.md, hooks, skills, plugins, MCP servers) + 2 capabilities (LSP, subagents) that actually drive successful deployments, plus 3 configuration patterns observed across thousands-of-developer rollouts. Frame as "Anthropic shows" — not opinion, not commentary, fully grounded in the source.

**Thesis**: According to Anthropic, what makes Claude Code work in a large codebase isn't the model — it's the harness (CLAUDE.md + hooks + skills + plugins + MCP + LSP + subagents) and the org structure (dedicated DRI / agent manager owning the configuration). Teams that invest in this layer see successful adoption; teams that bet only on model quality plateau.

**Must-Mention Points**:
- Claude Code uses agentic search (no embedding index), not RAG retrieval — and the article explains why RAG fails at scale
- The 5 extension points + 2 additional capabilities are the harness — order matters (CLAUDE.md first, MCP last)
- 3 configuration patterns: (1) navigability — lean layered CLAUDE.md files, subdirectory init, scoped tests/lint, .gitignore + permissions.deny, codebase maps, LSP for symbol-not-string search; (2) actively maintaining CLAUDE.md as models evolve (review every 3–6 months); (3) assigning ownership — agent-manager / DRI / cross-functional working group
- Languages explicitly called out: C, C++, C#, Java, PHP (Claude Code performs better than most teams expect)
- Customer anecdotes: large retail org's internal-analytics plugin; enterprise software co's org-wide LSP for C/C++; day-one plugin+MCP suite at one company; dedicated AI-tooling team at another
- Edge cases NOT covered: codebases with hundreds of thousands of folders / millions of files, legacy non-git VCS — promised for future installments
- The article is the first in a new "Claude Code at scale" series

**Technical Terms** (pronunciation notes):
- CLAUDE.md = "claude dot M D" (read as a filename, not a sentence)
- MCP = "M C P" (spell out)
- LSP = "L S P" (spell out)
- RAG = "rag" (one word) — verify against TTS audit
- DRI = "D R I" (spell out)
- monorepo = "mono-repo" (compound)
- subagent = "sub-agent" (compound)
- p4 edit = "P 4 edit" (the Perforce command — only relevant to one anecdote)

**Voice/Style Notes**: Frame every claim with source-grounded language — "Anthropic explains", "the article lays out", "Anthropic's Applied AI team observed", "the post notes". NEVER "I think" or "in my opinion". The video is a faithful response to Anthropic's own playbook, not commentary on it. Open with a number or punchline from the article (e.g., "5 extension points. 2 capabilities. 3 patterns."). End with a debate-sparking CTA that ties to the harness-vs-model tension.

## Receipts

1. https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start — 2026-05-14 — Anthropic's "Claude Code at scale" series, Part 1: harness + 3 configuration patterns + ownership / DRI / agent-manager pattern + customer anecdotes
2. file://./tmp/source.md — 2026-05-14 — Verbatim full-text local copy of the article with operator-curated key facts / stats / quotes for fact-check
3. file://./assets/blog/ — 2026-05-14 — 4 downloaded source figures: header-icon.svg, fig1-harness.png (the 7-component harness table), fig2-rollout-phases.png (rollout phases diagram), fig3-getting-started-checklist.png (action items)

## Topic Type Override

**topic_type**: ARTICLE_RESPONSE

For ARTICLE_RESPONSE videos:
- Phase 0 research: SKIP vidiQ + open-web search; the source article is the authority. Optionally run vidiQ keyword_research for the YouTube description's keyword optimization, but DON'T let it shape script content.
- Phase 2b fact-check: cross-check every claim in the script against `tmp/source.md` only. Skip WebSearch entirely. A claim that doesn't appear in the source (or isn't a faithful paraphrase) MUST be removed or reworded.
- Engagement CTA: tie to the article's central tension. Strong candidates:
  - "Anthropic says the harness matters more than the model. Do you buy it — or is this still mostly Sonnet 4.6 doing the heavy lifting?"
  - "Three to six months between configuration reviews. Too long? Too short? When was YOUR last CLAUDE.md cleanup?"
  - "Anthropic's calling the role 'agent manager'. Real job, or rebranded DevEx?"

## Composition direction

- Mid-video subscribe-banner around the 50% mark (`scene-subscribe-banner.html`)
- Dynamous midroll around the 60–70% mark (`scene-dynamous-midroll.html`) — locked spoken line per memory: "If you want to learn more about AI, check out the dynamous.ai community."
- The 4 source figures anchor 3–4 distinct `scene-image-3d-reveal.html` scenes per `tmp/image-map.md`. Each enters with the signature 3D-reveal motion, holds for narration, and exits via crossfade.
- The hook scene must satisfy the thumbnail-grade-first-frame rule (per `.claude/rules/shorts-thumbnail-frames.md`) — even though this is long-form, opening on topic+brand+receipt is best practice.
- The CTA scene must satisfy `.claude/rules/engagement-cta.md` — debate-sparking question on screen + matching spoken close + matching YouTube description close, all referencing the same article claim.

## Output requirements (recap)

- Total duration target: ~480s (8 min)
- Composition build via `new-long-form-anthropic` playbook
- `youtube-description.md` mandatory (per `.claude/rules/youtube-metadata.md`) with source URL credited in Resources section
- Engagement CTA mandatory (per `.claude/rules/engagement-cta.md`)
- Never auto-render — pipeline ends at `npx hyperframes preview videos/claude-code-large-codebases`
