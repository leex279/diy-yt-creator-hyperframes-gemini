---
description: Structured video-brief input format for /diy-yt-creator pipeline phases
---

# Video Brief Template

Use this format when you want full control over the pipeline inputs (instead of just passing a free-form topic to `/diy-yt-creator:full-auto`).

The detection marker is the literal string `**Topic**:` on its own line — both `/diy-yt-creator:phase0-research` and `/diy-yt-creator:full-auto` parse this format when they see it.

Save your brief as a `.md` file anywhere (e.g. `videos/<slug>/brief.md` or `~/scratch/brief.md`) and pass the path as the argument.

---

## Brief Schema

Copy this template, fill in the fields, save as `.md`, and pass the path to `/diy-yt-creator:full-auto`.

```markdown
## Video Brief

**Topic**: [Product name, concept, or feature to explain]

**Slug**: [optional — kebab-case folder name under videos/. If omitted, derived from Topic.]

**Template**: [shorts/anthropic | long-form/* — currently only shorts/anthropic is implemented]

**Duration**: [15s / 30s / 45s / 60s / 90s / 3min]

**Tone**: [tech-influencer-edgy / professional-corporate / friendly-educational / dramatic-cinematic]

**Links**:
- [Primary URL — product page, docs, or announcement]
- [Additional reference URLs]

**Target Audience**: [Who is this for? e.g., developers, product managers, non-technical users]

**Key Angle**: [The single most compelling narrative angle, or leave blank for auto-detection]

**Thesis**: [One sentence. Falsifiable — must be a claim that could be wrong. Forces the script to argue something instead of describing the topic. Example: "Claude Code's plan-first agent mode prevents the codebase damage that direct-edit agents cause — but only when the developer reads the plan before approving." Leave blank in autonomous mode if Phase 0 should derive it from research.]

**Must-Mention Points**:
- [Specific feature, stat, or claim to include]
- [Another key point]

**Technical Terms** (pronunciation notes):
- [e.g., kubectl = cube-C T L, nginx = engine-x]

**Voice/Style Notes**: [Any specific preferences — e.g., "no humor", "include a question hook", "end with GitHub link"]

## Receipts

[At least 3 named, linkable, verifiable items — OR explicitly mark `topic_type: CONCEPT` to override the gate. Each receipt = URL + version/date + one-line summary. Phase 0's Receipt Gate (Step 0H) blocks pipeline if neither condition is met. This prevents the model from inventing "studies show 73%..." stats during script generation.]

1. <URL> — <version or date> — <one-line summary of what this verifies>
2. <URL> — <version or date> — <one-line summary>
3. <URL> — <version or date> — <one-line summary>
```

---

## Field Reference

| Field                   | Required? | Used by                       | Notes                                                                                  |
| ----------------------- | --------- | ----------------------------- | -------------------------------------------------------------------------------------- |
| **Topic**               | Yes       | Phase 0, all downstream       | Detection marker — must be the literal `**Topic**:` string                             |
| **Slug**                | No        | Orchestrator, all phases      | If omitted, derived as kebab-case from Topic (e.g. "Claude Code Skills" → `claude-code-skills`) |
| **Template**            | No        | `/diy-yt-creator:full-auto` Step 1.5, then Phase 1  | If specified, the orchestrator skips the template-suggestion prompt and uses this verbatim. If omitted, the orchestrator scans `templates/`, recommends one based on the topic/duration, and asks the user to confirm before locking. Long-form templates do not exist yet — see `templates/long-form/README.md` |
| **Duration**            | Yes       | Phase 0 (depth), Phase 1 (scenes), Phase 2 (word count), Phase 2.5 (loop-opener cadence) | Drives nearly every quantitative decision downstream |
| **Tone**                | Yes       | Phase 2, Phase 2.5            | Picked up by the Faceless Tech Scriptwriting Playbook §4 voice rules                   |
| **Links**               | Recommended | Phase 0, Phase 2b           | Phase 0 pre-fetches the primary URL; Phase 2b uses links as Tier-1 source URL audit     |
| **Target Audience**     | Recommended | Phase 0, Phase 2            | Shapes messaging hierarchy and pain-point selection                                    |
| **Key Angle**           | No        | Phase 0                       | Overrides the auto-detected narrative angle from Phase 0's competitive analysis        |
| **Must-Mention Points** | No        | Phase 2 (enforced inclusions) | Treated as hard requirements in script drafting                                        |
| **Thesis**              | No        | Phase 0 (synthesis), Phase 1 (structure), Phase 2.5 (cohesion check) | One-sentence falsifiable claim. If omitted, Phase 0 derives one from research. Forces script to argue, not describe. |
| **Receipts**            | Yes (≥3, OR topic_type=CONCEPT) | Phase 0 gate, Phase 2 (per-scene binding), Phase 2b (cross-check) | Minimum 3 named, linkable items. Phase 0 Step 0H blocks the pipeline otherwise. Override: `topic_type: CONCEPT` for abstract topics with no linkable artifacts. |
| **Technical Terms**     | No        | Phase 2a                      | Fed into ElevenLabs TTS optimization for pronunciation accuracy                        |
| **Voice/Style Notes**   | No        | Phase 2                       | Free-form modifier applied during script writing                                       |

---

## Why no `Resolution` field?

Resolution is template-driven in HyperFrames. The Anthropic Shorts template ships at 1080x1920; future long-form templates will ship at 1920x1080. The choice is made by `Template`, not by a separate `Resolution` field — HyperFrames bakes resolution into `hyperframes.json` per-template.

---

## Example — Minimal Brief

```markdown
## Video Brief

**Topic**: Claude Code Skills launch

**Duration**: 45s

**Tone**: tech-influencer-edgy

**Links**:
- https://www.anthropic.com/news/skills

**Target Audience**: developers building with Claude

## Receipts

1. https://www.anthropic.com/news/skills — 2025-10 — Skills launch announcement, names mechanism + install pattern
2. https://docs.claude.com/en/docs/claude-code/skills — 2025-10 — Skills docs, lists discovery + invocation rules
3. https://github.com/anthropics/claude-code/releases — 2025-10 — Release notes confirming Skills shipped in v1.x.y
```

This is enough to drive the full pipeline. Everything else gets auto-derived.

---

## Example — Full Brief

```markdown
## Video Brief

**Topic**: Claude Code Skills launch

**Slug**: claude-code-skills-launch

**Template**: shorts/anthropic

**Duration**: 60s

**Tone**: tech-influencer-edgy

**Links**:
- https://www.anthropic.com/news/skills
- https://docs.claude.com/en/docs/claude-code/skills

**Target Audience**: developers already using Claude Code, considering writing their first skill

**Key Angle**: Skills compress recurring workflows into one-line invocations — the productivity unlock most CC users haven't installed yet

**Thesis**: Claude Code Skills are not "another extension system" — they're the first install mechanism that lets ChatGPT-grade prompt engineering ship as version-controlled artifacts inside the repo, and most CC users haven't installed one yet because the discovery surface is silent.

**Must-Mention Points**:
- Skills are markdown files that bundle prompts + tools + reference docs
- Discoverable via natural language ("create a slash command")
- Can be project-local (.claude/skills/) or global (~/.claude/skills/)

**Technical Terms**:
- CC = Claude Code
- skill (lowercase) — the artifact

**Voice/Style Notes**: Open with a number. End with the install command as the CTA.

## Receipts

1. https://www.anthropic.com/news/skills — 2025-10 — Launch post, names the mechanism
2. https://docs.claude.com/en/docs/claude-code/skills — 2025-10 — Authoritative docs on discovery + invocation
3. https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md — 2025-10 — Release notes confirming the version Skills shipped in
```
