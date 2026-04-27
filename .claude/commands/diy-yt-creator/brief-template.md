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

**Must-Mention Points**:
- [Specific feature, stat, or claim to include]
- [Another key point]

**Technical Terms** (pronunciation notes):
- [e.g., kubectl = cube-C T L, nginx = engine-x]

**Voice/Style Notes**: [Any specific preferences — e.g., "no humor", "include a question hook", "end with GitHub link"]
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

**Must-Mention Points**:
- Skills are markdown files that bundle prompts + tools + reference docs
- Discoverable via natural language ("create a slash command")
- Can be project-local (.claude/skills/) or global (~/.claude/skills/)

**Technical Terms**:
- CC = Claude Code
- skill (lowercase) — the artifact

**Voice/Style Notes**: Open with a number. End with the install command as the CTA.
```
