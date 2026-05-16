# Agent Skills — 3-minute editorial Short

Source-grounded against `tmp/source.md` (agentskills.io home / spec / quickstart).
Target: ~180s @ ~155 WPM ≈ 460 words.

Per `.claude/rules/engagement-cta.md`: closes on a binary debate question that the on-screen `#cta-question` and YouTube description will mirror.

---

## Scene 1 — title (~16s)

Every AI agent has the same problem.

They're smart. They're capable. But they don't know *your* stack.

So you write the same setup prompt. Every time. In every tool.

That ends with Agent Skills.

## Scene 2 — typewriter (~18s)

A skill is one folder.

Inside lives one file. SKILL.md.

That file holds two fields. A *name*. A *description*. Plus the instructions an agent follows to do the work.

That is the whole spec.

## Scene 3 — bullets (~22s)

A skill is more than just SKILL.md though.

Drop scripts into a `scripts/` folder — and the agent runs them.

Drop reference docs into a `references/` folder — and the agent reads them on demand.

Drop templates into `assets/` — and the agent uses them.

## Scene 4 — process-flow (~22s)

Here's the part that makes it actually work. *Progressive disclosure*.

Stage one — discovery. At startup, the agent loads only each skill's name and description. About a hundred tokens each.

Stage two — activation. When your task matches the description, the full SKILL.md loads into context.

Stage three — execution. Bundled scripts and reference files only load when the work demands them.

Skills stay small until you need them.

## Scene 5 — code-block (~22s)

This is what a real SKILL.md looks like.

Three dashes. A name. A description that says what the skill does and when to use it. Three dashes again. Then Markdown.

No DSL. No SDK. Just a file you can commit to a Git repo.

## Scene 6 — stat (~17s)

Here's the receipt.

A *hundred* tokens to advertise a skill. *Five thousand* tokens to run it. *Zero* tokens until activation.

Many skills. Tiny context footprint.

## Scene 7 — badges (~22s)

So where can you use a skill you write today?

Claude Code. VS Code. Cursor. GitHub Copilot. Gemini CLI. OpenAI Codex. Goose. Letta. Roo Code. Kiro.

*Thirty-seven* products and growing. Same file. Same format. Zero rewrites.

## Scene 8 — quote (~17s)

The format was originally developed by *Anthropic*.

Then released as an open standard.

Open to contributions from anyone in the ecosystem.

## Scene 9 — cta + thumbnail-grade final frame (~24s)

So one question.

Skills, or MCP — which one earns the spot in your stack first?

Drop your pick in the comments.

Full spec at agentskills dot io.

---

## Engagement CTA — locked

**Question (spoken + on-screen + description, identical wording):**
> Skills, or MCP — which one earns the spot in your stack first?

Properties (per engagement-cta.md):
- Binary/short-list answer: ✅ "Skills" or "MCP"
- Polarizing stance: ✅ forces a stack-pick, hot-take territory
- References specific claim: ✅ the video's core thesis (skills as the new extension format)
- Low cost: ✅ anyone with an AI tool can answer in 2 words

## Heteronym audit (pre-TTS)

- "live" / "lives" — only "lives" appears (3rd-person verb /lɪvz/), unambiguous. ✅
- "read" / "reads" — present tense /riːdz/ in "the agent reads them on demand". Engine reads it correctly in context. ✅
- "lead" — not used. ✅
- "record" — not used. ✅
- "close" — not used. ✅
- "Cursor" — proper noun, pronounced normally. ✅
- "SKILL.md" — TTS-script will spell as "skill dot M D". Action: applied in `scene-XX-*.txt`.
- "agentskills.io" — TTS-script will spell as "agentskills dot io". Action: applied in scene-09.
- "MCP" → "M C P" (TTS-spelled).
- "SDK" → "S D K" (TTS-spelled).
- "DSL" → "D S L" (TTS-spelled).
- "VS Code" → "V S Code" (TTS-spelled to avoid "vs" being read as "versus").
- "CLI" → "C L I" (TTS-spelled).

## Word count target

| Scene | Words | Est duration @ 155 WPM × 1.05 speed |
|---|---|---|
| 1 title | 32 | ~12s narration + 4s breath |
| 2 typewriter | 36 | ~14s + 4s breath |
| 3 bullets | 41 | ~16s + 6s breath |
| 4 process-flow | 76 | ~29s + ... | (over budget — trim or extend scene) |
| 5 code-block | 35 | ~14s + 8s breath |
| 6 stat | 28 | ~11s + 6s breath |
| 7 badges | 36 | ~14s + 8s breath |
| 8 quote | 22 | ~9s + 8s breath |
| 9 cta | 28 | ~11s + 12s breath |

Total spoken: ~334 words / ~130s. Plus inter-scene silence ≈ ~50s. Total ≈ 180s. ✅

Scene 4 (process-flow) is the long one. We'll allocate ~30s for that scene specifically.
