# Feature: Scriptwriting Pipeline Quality Improvement

## Summary

Our scriptwriting workflow produces fragmented stat-dump scripts that pass every quality gate (10/10 hook, 8.5/10 arc, 0 banned phrases) but lose to a single-pass Gemini Pro draft on human readability. The Gemini script has narrative connectors, direct viewer address, and a clear engagement CTA — none of which our gates score for. Fix this by (a) inverting hook scoring to penalize stat-stacking and reward narrative flow, (b) adding three new positive scoring dimensions (Narrative Flow, Direct Address, Engagement CTA), (c) tightening the CTA gate from "averaged element" to "hard sub-gate ≥ 7", (d) capping scene count for sub-60s shorts at 4–5 to stop fragmentation, (e) adding a Reference Script Library that the writer must read before drafting, and (f) splitting the brand-voice into a `developer-tutorial` profile (current) and a new `news-explainer` profile (for shorts about announcements like the Anthropic deal).

## User Story

As the channel owner running this pipeline
I want scripts that read like the Gemini-Pro reference (`videos/anthropic-100b-deal/script.txt`) — narrative, conversational, with explicit CTA
So that the videos we produce are actually engaging and don't sound like fact-dump bots

## Problem Statement

Compare two scripts on the same topic:

**Gemini Pro (`videos/anthropic-100b-deal/script.txt`, ~210 words)** — uses connectors ("To keep Claude at the top, …", "Why are they pouring so much money into this? Because …"), direct address ("If you've noticed Claude being slow or buggy during peak hours, this is why."), and a real CTA ("Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news.").

**Our pipeline (`videos/anthropic-amazon-compute/script.txt`, ~150 words)** — staccato fragments ("100 billion dollars. 5 gigawatts. Zero Nvidia chips."), zero explanatory connectors between scenes, no mid-script viewer address, no question, no subscribe ask.

The critique gave our script `10/10 hook, 8.5/10 arc, 0 banned phrases — PASS on all 4 gates`. The system rated this highly. The user judged it "not good." The gates are measuring the wrong things.

Specifically testable failure: our `phase2-5-critique.md` scoring formula awards Variant B `advisory_score: 10.0` for `"If you got rate-limited on Claude this April, Anthropic just spent $100 billion to fix it"` because it scores 10/10 on Specificity (three stats in opening line) and 1.0 on Promise. There is **no dimension that penalizes the absence of narrative flow** in the body, and no dimension that rewards an engagement CTA in the closer.

## Solution Statement

Treat the Gemini script as the gold standard, reverse-engineer what it does that ours doesn't, and encode those properties as new BLOCKING dimensions in `phase2-5-critique.md`. Specifically:

1. **New scoring dimension: Narrative Flow** (0–10, blocking ≥ 6) — counts explanatory connectors in body scenes (`because`, `why`, `to`, `and so`, `but`, `plus`) and penalizes pure-fragment scripts.
2. **New scoring dimension: Direct Viewer Address** (0–2, blocking = 2) — requires at least ONE second-person sentence in the body (not just CTA).
3. **CTA hard sub-gate** (≥ 7) — currently CTA scoring is averaged with three other arc elements, so a 5/10 CTA passes when the others are 9–10. Make it a separate gate.
4. **Cap scene count for shorts ≤ 60s at max 5 scenes** in `phase1-plan.md` Step 2A — the current 8-scene plan for 45s forces 5–6s scenes that can't fit explanatory connectors.
5. **Add `.claude/references/script-library.md`** — annotated golden examples (the Gemini one + 1–2 future winners). Phase 2 MUST read it before drafting.
6. **Split `.claude/references/brand-voice.md` into `brand-voice-tutorial.md` (current rules) + new `brand-voice-news-explainer.md`** — the current spec was tuned for Thomas's developer-tutorial channel where dry-sarcasm + first-person-experience is mandatory; news-explainer shorts about third-party announcements need different rules (explanatory connectors are GOOD, mild stakes-framing is fine, debate-CTA is mandatory). Phase 0 picks the profile based on topic type and Phase 2 reads the matching one.

## Metadata

| Field            | Value                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Type             | ENHANCEMENT (prompt/process refactor — no code change to HyperFrames CLI itself)           |
| Complexity       | MEDIUM                                                                                      |
| Systems Affected | `.claude/commands/diy-yt-creator/`, `.claude/references/`, `.claude/skills/diy-yt-creator/` |
| Dependencies     | None — this is markdown-only; no library deps                                              |
| Estimated Tasks  | 9                                                                                           |

---

## UX Design

### Before State (current pipeline output)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  TOPIC: "$100B Anthropic / AWS deal"                                          ║
║                                                                               ║
║  Phase 0 ──► Phase 1 (8 scenes for 45s) ──► Phase 2 (writer reads brand-       ║
║  voice.md → applies "Boxer's Rhythm" jab-jab-jab) ──► Phase 2.5 (rewards stat ║
║  density, no narrative-flow check, CTA averaged in arc) ──► PASS ──► TTS      ║
║                                                                               ║
║  Output script.txt:                                                           ║
║    "One hundred billion dollars. Five gigawatts. Zero Nvidia chips. ...       ║
║     An H one hundred runs about three dollars an hour. Trainium drops to one. ║
║     ...                                                                       ║
║     The compute crunch is over."                                              ║
║                                                                               ║
║  CHARACTERISTICS:                                                             ║
║    • 8 scenes × ~5–6s each → fragmented                                       ║
║    • Zero "because/why/to" explanatory connectors between scenes              ║
║    • Zero direct address in body (only "if you build on Claude" at the end)   ║
║    • Declarative non-engagement closer ("the compute crunch is over.")        ║
║    • Critique gates: 10/10 hook, 8.5/10 arc, 0 banned phrases — PASS          ║
║                                                                               ║
║  PAIN: Reads like a press-release bullet dump, not a YouTube short.           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State (post-improvement pipeline)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  TOPIC: "$100B Anthropic / AWS deal"                                          ║
║                                                                               ║
║  Phase 0 ──► (NEW: pick voice profile: news-explainer)                         ║
║  Phase 1 (cap: max 5 scenes for ≤60s) ──► Phase 2 (writer reads               ║
║  script-library.md golden example FIRST + brand-voice-news-explainer.md       ║
║  → applies narrative-flow patterns) ──► Phase 2.5 (NEW: Narrative Flow +      ║
║  Direct Address + CTA hard sub-gate) ──► PASS only if all 4+3 dims pass ──►   ║
║  TTS                                                                          ║
║                                                                               ║
║  Output script.txt:                                                           ║
║    "Anthropic just made one of the biggest AI hardware deals in history.      ║
║     And the numbers are absolutely insane. To keep Claude at the top,         ║
║     Anthropic just committed over one hundred billion dollars to AWS over     ║
║     the next ten years. ... Why are they pouring so much money into this?     ║
║     Because Claude's growth is exploding. ... If you've noticed Claude being  ║
║     slow during peak hours, this is why. ... Is Claude about to take over     ║
║     the AI space? Let me know in the comments. And subscribe."                ║
║                                                                               ║
║  CHARACTERISTICS:                                                             ║
║    • 4–5 scenes × 9–11s each → room for connectors                             ║
║    • ≥ 3 explanatory connectors per script ("To keep …", "Because …", "If")   ║
║    • ≥ 1 direct-address sentence in body                                       ║
║    • Engagement CTA: question + comments ask + subscribe ask                   ║
║    • Critique gates: 4 originals + Narrative Flow ≥ 6 + Direct Addr = 2 +     ║
║      CTA Sub-gate ≥ 7. All must PASS independently.                            ║
║                                                                               ║
║  VALUE: Scripts read like Gemini's gold-standard, not a fact-dump.            ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes

| Location                                       | Before                                            | After                                                              | Impact                                                  |
| ---------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| `phase1-plan.md` Step 2A                       | "15-30s → 3-4 scenes" (no upper cap)              | "≤60s → max 5 scenes; flag violation"                              | Stops 8-scene fragmentation                              |
| `phase2-script.md` Step 1                      | Read plan + brief                                 | Read plan + brief + `script-library.md` (golden examples)         | Writer learns from the gold standard before drafting    |
| `phase2-script.md` Step 3.6                    | Reads `brand-voice.md` (single profile)           | Reads `brand-voice-<profile>.md` based on Phase 0 pick             | News-explainer scripts get the right rules              |
| `phase2-5-critique.md` Pass 4                  | CTA averaged with 3 other arc elements            | CTA = independent sub-gate ≥ 7 OR overall FAIL                     | Weak CTA can no longer hide behind strong hook         |
| `phase2-5-critique.md` (NEW Pass 6)            | n/a                                               | Narrative Flow ≥ 6 + Direct Address = 2 (both blocking)            | Stat-dump scripts blocked at gate                       |
| `phase0-research.md` (output `content-brief.md`) | No `voice_profile` field                       | Adds `voice_profile: tutorial \| news-explainer \| comparison`     | Downstream phases pick the right voice spec            |

---

## Mandatory Reading

**CRITICAL: Implementation agent MUST read these before starting any task:**

| Priority | File                                                                                                                                       | Lines      | Why Read This                                                                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | `videos/anthropic-100b-deal/script.txt`                                                                                                    | all (1 line) | THE GOLD STANDARD. Re-read after every change. Every new rule should rate this script ≥ 9/10.                                                                          |
| P0       | `videos/anthropic-amazon-compute/script.txt`                                                                                               | all        | THE FAILURE MODE. Re-read after every change. Every new rule should rate this script LOWER than the gold standard.                                                       |
| P0       | `videos/anthropic-amazon-compute/scripts/critique-report.md`                                                                               | 37–204     | Shows what the current gates measure (Hook 10/10, Arc 8.5/10, all PASS). Confirms the gates are measuring the wrong things.                                            |
| P1       | `.claude/commands/diy-yt-creator/phase2-5-critique.md`                                                                                     | 60–205     | The five-pass critique structure. New dimensions get added here.                                                                                                       |
| P1       | `.claude/commands/diy-yt-creator/phase2-script.md`                                                                                         | 136–195    | Step 3.6 (reference reading) is where script-library.md gets wired in; Step 4b (Story Locks) is the closest existing pattern for new scoring rules.                    |
| P1       | `.claude/commands/diy-yt-creator/phase1-plan.md`                                                                                           | 102–124    | Step 2A's scene-count table is where the ≤60s cap goes.                                                                                                                |
| P1       | `.claude/references/brand-voice.md`                                                                                                        | all (240 lines) | The current voice spec is tutorial-channel-coded. Splitting it requires understanding what's universal vs developer-tutorial-specific.                                |
| P2       | `.claude/commands/diy-yt-creator/phase0-research.md`                                                                                       | (the `content-brief.md` schema portion) | Where the new `voice_profile` field gets added.                                                                                                                       |
| P2       | `videos/anthropic-amazon-compute/plan.md`                                                                                                  | 17–28      | Master Timeline shows 8 scenes for 45s — exactly the fragmentation the cap will prevent.                                                                                |
| P2       | `videos/anthropic-amazon-compute/scripts/full-script.md`                                                                                   | all        | Compare the per-scene Markdown form to the final flat `script.txt` — note the same staccato pattern.                                                                   |

**External Documentation:** None — this is a markdown/prompt refactor; no library deps.

---

## Patterns to Mirror

**Phase scoring formula pattern (from existing critique):**

```python
# SOURCE: .claude/commands/diy-yt-creator/phase2-5-critique.md:99-105
# COPY THIS PATTERN for new Pass 6 scoring:
base = (D1 + D2 + D3) / 3
stun_bonus = D4 / 20        # 0.0 or 0.1
alignment_bonus = D4b       # 0.0 or 0.5
hook_score = min(10, round(base + stun_bonus + alignment_bonus + D5, 1))
```

**Quality-gate output table pattern:**

```markdown
<!-- SOURCE: .claude/commands/diy-yt-creator/phase2-5-critique.md:111-119 -->
<!-- COPY THIS PATTERN for new Pass 6 output: -->
| Dimension       | Score      | Notes                                         |
| --------------- | ---------- | --------------------------------------------- |
| Curiosity Gap   | X/10       | [specific observation]                        |
| ...             | ...        | ...                                           |
| **HOOK SCORE**  | **X.X/10** | **PASS / FAIL (threshold: 7.0)**              |
```

**Reference-doc-as-canonical-source pattern (from `phase2-script.md:136-170`):**

```markdown
<!-- SOURCE: .claude/commands/diy-yt-creator/phase2-script.md:138-145 -->
<!-- COPY THIS PATTERN for script-library.md wiring: -->
## Step 3.6 — Consult the Scriptwriting References

Before writing, read BOTH reference docs in this order — brand-voice is more specific
and overrides the generic playbook where they differ:

### A. `.claude/references/brand-voice.md` (CHANNEL-SPECIFIC — read first)
[…rules…]
The Phase 2.5 critique will enforce ALL of these.
```

**Banned-list scoring pattern (from `phase2-5-critique.md:316-326`):**

```markdown
<!-- SOURCE: .claude/commands/diy-yt-creator/phase2-5-critique.md:319-326 -->
<!-- COPY THIS PATTERN for narrative-connector positive-list scoring: -->
Scan for any occurrence of these (case-insensitive, word boundaries):

**Generic AI phrases** (always banned): `delve`, `tapestry`, …
```

**Profile-selection pattern (NEW — closest analogue is brand-voice's voice-profile vs playbook split at `phase2-script.md:138-168`):**

```markdown
<!-- New pattern, but mirrors the precedence resolution at phase2-script.md:168 -->
Where brand-voice-news-explainer.md and the generic playbook conflict, brand-voice-news-explainer.md wins.
Where brand-voice-tutorial.md and brand-voice-news-explainer.md disagree, the active profile wins.
```

---

## Files to Change

| File                                                                          | Action  | Justification                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.claude/references/script-library.md`                                        | CREATE  | Golden examples library — Phase 2 reads this before drafting                                                                                                                                                   |
| `.claude/references/brand-voice-news-explainer.md`                            | CREATE  | New voice profile for shorts about third-party announcements (the Anthropic-deal class)                                                                                                                         |
| `.claude/references/brand-voice-tutorial.md`                                  | CREATE  | Renamed/refocused copy of the current `brand-voice.md`, scoped explicitly to tutorial-style developer content                                                                                                  |
| `.claude/references/brand-voice.md`                                           | UPDATE  | Convert to a **dispatcher** — points at the two profile files based on `voice_profile` field. Keeps the file path stable for any external skill that imports it.                                                |
| `.claude/commands/diy-yt-creator/phase0-research.md`                          | UPDATE  | Add `voice_profile` field to `content-brief.md` schema (one of: `tutorial`, `news-explainer`, `comparison`). Default by topic-type heuristic.                                                                  |
| `.claude/commands/diy-yt-creator/phase1-plan.md`                              | UPDATE  | Step 2A scene-count table: add hard cap "≤60s = max 5 scenes". Step 4D hook scoring: re-weight to penalize stat-density-only hooks (currently `specificity: 10` for triple-stat opener wins automatically). |
| `.claude/commands/diy-yt-creator/phase2-script.md`                            | UPDATE  | Step 3.6: add `script-library.md` as P0 reference (read FIRST, before brand-voice). Branch on `voice_profile` to read the right brand-voice-*.md. Add new Step 3.8: "Apply narrative-flow connectors".         |
| `.claude/commands/diy-yt-creator/phase2-5-critique.md`                        | UPDATE  | Add Pass 6 (Narrative Flow + Direct Address — blocking). Promote CTA scoring (Pass 4 Arc Element 3) to independent sub-gate. Down-weight Specificity in Pass 1 (avoid auto-10 for triple-stat openers).        |
| `.claude/skills/diy-yt-creator/new-anthropic-short.md`                        | UPDATE  | One-line: in Step 4 Branch B's "Style rules for narration text", add reference to `script-library.md` so the legacy/quick-path also benefits.                                                                  |

---

## NOT Building (Scope Limits)

Explicit exclusions to prevent scope creep:

- **No retroactive re-scoring of existing videos.** The `videos/anthropic-amazon-compute/` artifacts stay as-is — this is a forward-looking workflow change, not a regen of past videos. (User can manually re-run `/diy-yt-creator:full-auto --resume anthropic-amazon-compute` to apply the new gates if they want — but that's their call, not part of this plan.)
- **No HyperFrames CLI changes.** This is purely prompt/reference markdown; the `npx hyperframes lint/render/tts/transcribe` binaries don't change.
- **No new model invocations or API calls.** All new scoring is regex/structural — runs in the same Phase 2.5 LLM pass that already exists.
- **No user-facing slash command renames.** `phase2-5-critique` keeps its name; we don't shuffle the command surface.
- **No automatic CI/blocking.** If the new gates fail, the pipeline still STOPs in the same way it does today (per Phase 2.5's existing blocking behavior); we don't add CI hooks or pre-commit gates.
- **No changes to `phase2a-tts-script.md`, `phase2b-factcheck.md`, `phase3-5-retention.md`.** Those run AFTER critique passes; they're downstream of the change.
- **No third voice profile (`comparison`)** in this pass — leave it as a `voice_profile` enum value but defer the actual `brand-voice-comparison.md` file. Two profiles is enough to validate the dispatcher pattern.

---

## Step-by-Step Tasks

Execute in order. Each task is atomic and independently verifiable.

### Task 1: CREATE `.claude/references/script-library.md`

- **ACTION**: CREATE the golden-example reference doc
- **IMPLEMENT**: Three top-level sections:
  1. **Why this file exists** — one paragraph: gold-standard scripts that should drive new drafts
  2. **Profile: news-explainer** — embed the full text of `videos/anthropic-100b-deal/script.txt` verbatim, then a per-paragraph annotation table calling out:
     - Opening hook pattern (claim + emotional amplifier: "And the numbers are absolutely insane")
     - Explanatory connector ("To keep Claude at the top, …", "Why are they pouring so much money? Because …")
     - Direct address ("If you've noticed Claude being slow during peak hours, this is why.")
     - Engagement CTA structure (rhetorical question + "Let me know in the comments" + "And subscribe for more AI news")
  3. **Profile: tutorial** — placeholder section for now; instruction: "Add a winning tutorial script here once one ships."
  4. **How to use** — "Phase 2 MUST read the matching profile section before drafting; copy the rhythm, not the words."
- **MIRROR**: `.claude/references/brand-voice.md` overall structure (frontmatter status line, sections, do/don't tables)
- **GOTCHA**: Do NOT abstract the gold-standard script into "rules". Quote it verbatim and annotate. Phase 2 needs the texture, not a summary.
- **VALIDATE**: `grep -c "Anthropic just made" .claude/references/script-library.md` returns ≥ 1 (the gold-standard text is present verbatim).

### Task 2: CREATE `.claude/references/brand-voice-tutorial.md`

- **ACTION**: COPY the current `.claude/references/brand-voice.md` to this new path
- **IMPLEMENT**: Verbatim copy with two header changes:
  1. Title: `# Brand Voice — Tutorial / Developer-Education Profile`
  2. Status line: `**Profile:** tutorial — for hands-on developer content where Thomas is the practitioner`
- **MIRROR**: Existing `brand-voice.md` 1:1
- **PATTERN**: This preserves all current rules (the 50-word banned list, the 4 hook types, the 10 hard rules, the dry-sarcasm calibration) — they're correct for tutorials, just mis-applied to news-explainers
- **VALIDATE**: `diff` between old `brand-voice.md` and new `brand-voice-tutorial.md` shows ONLY the two header line changes

### Task 3: CREATE `.claude/references/brand-voice-news-explainer.md`

- **ACTION**: CREATE a new voice profile for news-explainer shorts
- **IMPLEMENT**: Same structural sections as `brand-voice.md` BUT with these critical differences:
  - **Character Brief**: "narrator is reporting on something the viewer might have missed — not running an experiment. Curates the news, gives context, frames why it matters."
  - **3 Core Adjectives**: change "Enthusiastic. Practical. Honest." → **"Clear. Contextual. Direct."** (enthusiasm reads as hype in news; tutorial-honesty doesn't apply when narrator wasn't a participant)
  - **Sentence Rhythm**: REPLACE "Short → Longer → Short → Opinion" with **"Claim → Explanation → Stake → Implication"**. Example: `"Anthropic just made one of the biggest AI hardware deals in history. [claim] To keep Claude at the top, Anthropic just committed over $100 billion to AWS over the next ten years. [explanation] Amazon is paying up too. [stake] If you build on Claude, peak-hour rate-limits are about to ease. [implication]"`
  - **Hook types**: keep B (counterintuitive), C (specific number), D (shared frustration); REPLACE A (honest result — implies first-person experiment) with **A-news (Magnitude framing)**: `"[X] just made one of the [biggest/fastest/most expensive] [Y] in [history/Z's history]. [Stat-amplified second sentence]."`
  - **Mandatory connectors list** (NEW — no equivalent in tutorial profile): scripts MUST include at least 3 of: `because`, `why`, `to [verb]`, `and`, `but`, `plus`, `so`, `here's why`, `the reason`. Pure-fragment scripts FAIL.
  - **Mandatory direct-address sentence** (NEW): at least ONE second-person sentence in the body (not just CTA). Patterns: `"If you ['re building on / 've noticed / use / care about] X, [implication]"`. The Gemini line `"If you've noticed Claude being slow or buggy during peak hours, this is why."` is the canonical example.
  - **CTA pattern** (NEW — STRICTER than tutorial): MUST include a rhetorical/debate question + a comments-ask + a subscribe-ask. Template: `"[Rhetorical question about the topic]? Let me know in the comments. And subscribe for more [topic] news."` Tutorial profile says "no smash that like button" — news-explainer profile EXPLICITLY ALLOWS the standard YouTube CTA because it's not hype, it's expected.
  - **Banned list**: keep all generic-AI bans from tutorial profile, REMOVE the over-hedging bans (news allows `arguably`, `for the most part` for attributions), REMOVE the "no motivational frame" rule (`"To keep Claude at the top"` is fine — it's stating a stake, not motivating the viewer).
  - **First-person**: ALLOW BOTH `I` AND `we` (`we` is fine when referring to viewers + narrator collectively, e.g., `"we'll see what happens"`). Tutorial profile bans `we` because Thomas-the-builder is solo; news narrator is reporting on industry events.
- **MIRROR**: `brand-voice.md` (the new tutorial file) section structure
- **GOTCHA**: Don't loosen everything — the banned generic-AI phrases (`delve`, `leverage`, `paradigm`, etc.) MUST still be banned. The relaxation is targeted.
- **VALIDATE**: `grep -c "voice_profile" .claude/references/brand-voice-news-explainer.md` returns ≥ 1; the file's status line says `**Profile:** news-explainer`

### Task 4: UPDATE `.claude/references/brand-voice.md` to be a dispatcher

- **ACTION**: REPLACE the file's content with a 30–40 line dispatcher that points at the two new profile files
- **IMPLEMENT**:
  ```markdown
  # Brand Voice — Profile Dispatcher

  **Status:** v2.0 — 2026-04-28
  **Lives in:** `.claude/references/brand-voice.md`
  **Dispatches to:** profile-specific files based on the `voice_profile` field
  in `videos/<slug>/research/content-brief.md`.

  ## How to use

  Read `videos/<slug>/research/content-brief.md` and find the `voice_profile`
  field. Then read the matching profile file:

  | voice_profile     | File to read                                                | Use when                                                                            |
  | ----------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------- |
  | `tutorial`        | `.claude/references/brand-voice-tutorial.md`                | Thomas is the practitioner — hands-on developer content, terminal demos, workflows |
  | `news-explainer`  | `.claude/references/brand-voice-news-explainer.md`          | Reporting on third-party news — announcements, deals, releases, industry shifts    |
  | `comparison`      | (deferred — fall back to `news-explainer` for now)          | Tool A vs Tool B — currently uses news-explainer rules                              |

  If `voice_profile` is missing, default to `news-explainer` (most shorts in
  this channel are news-explainer; tutorial is opt-in).

  ## What's universal across all profiles

  Both profile files share a "Universal Bans" section (the generic-AI banned
  word list — `delve`, `leverage`, `paradigm`, etc.). Profile-specific lists
  add to it; they do not replace it.
  ```
- **MIRROR**: This is a small new pattern but the closest analogue in the codebase is the way `phase2-script.md:138-168` resolves between `brand-voice.md` (specific) and the playbook (generic) — same precedence-resolution shape
- **GOTCHA**: Do NOT delete the old content. Move it to `brand-voice-tutorial.md` (Task 2) FIRST, verify, then overwrite this file.
- **VALIDATE**: `wc -l .claude/references/brand-voice.md` ≤ 50; `grep -c "Dispatches to" .claude/references/brand-voice.md` = 1

### Task 5: UPDATE `.claude/commands/diy-yt-creator/phase0-research.md`

- **ACTION**: Add `voice_profile` field to the `content-brief.md` schema
- **IMPLEMENT**:
  - Find the section that defines `content-brief.md` output schema (it's near the bottom of the file, where the markdown template for the brief lives).
  - Add a new field `voice_profile: <tutorial | news-explainer | comparison>` near the top of the brief, alongside `Topic` / `Duration` / `Tone`.
  - Add a Step (call it Step N+1, "Pick voice profile") with a heuristic:
    | Topic signal                                                                                            | Default profile     |
    | ------------------------------------------------------------------------------------------------------- | ------------------- |
    | Topic mentions "I tried", "I built", "tutorial", "guide", "how to use", "walkthrough"                 | `tutorial`          |
    | Topic mentions "just shipped", "just launched", "just announced", "deal", "acquired", "raised", "vs"  | `news-explainer`    |
    | URL is a GitHub release, vendor blog post, or news article                                              | `news-explainer`    |
    | URL is a tool's homepage with no announcement context                                                   | `tutorial` (offer)  |
    | None of the above                                                                                       | ASK in interactive mode; default `news-explainer` in autonomous |
- **MIRROR**: The existing field-pattern in the brief schema (single-line YAML-style key-value pairs)
- **GOTCHA**: Don't break existing briefs that lack the field — Phase 2 will fall back to `news-explainer` (per the dispatcher Task 4) if the field is missing
- **VALIDATE**: `grep -c "voice_profile" .claude/commands/diy-yt-creator/phase0-research.md` returns ≥ 2 (one in schema, one in heuristic table)

### Task 6: UPDATE `.claude/commands/diy-yt-creator/phase1-plan.md`

- **ACTION**: Cap scene count for shorts ≤ 60s; rebalance hook scoring
- **IMPLEMENT**:
  - **Step 2A (scene count by duration table, lines ~102–110)**: Add a hard cap row:
    ```
    | ≤ 60s    | **MAX 5 scenes** | 9–12s            | HARD CAP — fragmentation kills narrative flow |
    ```
    Replace the existing `15-30s | 3-4` and `45s | 5-6` rows accordingly. The 8-scene plan we generated for 45s violated nothing because no cap existed.
  - **Step 4D (advisory scoring, lines ~252–270)**: Reduce Specificity weight in the formula. Current formula auto-rewards triple-stat openers like `"100 billion dollars. 5 gigawatts. Zero Nvidia chips."` because Specificity scores 10/10 there. New formula:
    ```
    base = (curiosity * 0.4) + (stakes * 0.4) + (specificity * 0.2)   # was equal-weighted
    hook_score = min(10, round(base + stun_bonus + alignment_bonus + promise + narrative_flow_bonus, 1))
    narrative_flow_bonus = +0.5 if hook is one or more sentences with explanatory connector ("because", "to keep", "and so") else 0
    ```
  - **Step 2C / 2D**: Add a new bullet under "Narrative arc": `"For news-explainer profile (per content-brief.md voice_profile field), every scene MUST connect to the next via an explanatory connector (because/why/to/and/but/plus/so). Plan a connector word per scene transition in the Master Timeline."`
- **MIRROR**: Existing scoring formula at `phase2-5-critique.md:99-105` (same shape, different weights)
- **GOTCHA**: The `hook_score` formula change cascades into Phase 2.5's QG-1 (which uses the same dimensions). Keep the formulas synced — Task 8 fixes the Phase 2.5 side.
- **VALIDATE**: `grep -c "MAX 5 scenes" .claude/commands/diy-yt-creator/phase1-plan.md` ≥ 1; `grep -c "narrative_flow_bonus" .claude/commands/diy-yt-creator/phase1-plan.md` ≥ 1

### Task 7: UPDATE `.claude/commands/diy-yt-creator/phase2-script.md`

- **ACTION**: Wire in `script-library.md`, branch on `voice_profile`, add narrative-flow Step
- **IMPLEMENT**:
  - **Step 1 (read the plan & research)**: Add a sub-bullet: `"Read videos/<slug>/research/content-brief.md → extract voice_profile field. Default to news-explainer if missing."`
  - **Step 3.6 (Consult the Scriptwriting References, lines ~136–170)**: Replace section A's reference to `brand-voice.md` with a profile-aware lookup:
    ```markdown
    ### A. The matching brand-voice profile (CHANNEL-SPECIFIC — read first)

    Look up `voice_profile` from `content-brief.md`:
    - `tutorial` → read `.claude/references/brand-voice-tutorial.md`
    - `news-explainer` → read `.claude/references/brand-voice-news-explainer.md`
    - missing → read `.claude/references/brand-voice-news-explainer.md` (default)
    ```
  - **NEW Step 3.55 (insert before Step 3.6)**: Title `"Read the Script Library (gold-standard examples)"`. Body:
    ```markdown
    Before applying any voice rules, read the matching profile section in
    `.claude/references/script-library.md`. The library quotes verbatim
    scripts that worked. Note the rhythm — claim, explanation, stake,
    direct address, CTA — and aim for the same shape, NOT the same words.

    The library is the single source of truth for "what good looks like."
    Voice rules are the single source of truth for "what bad looks like."
    Read the library first; voice rules are the fence, not the goal.
    ```
  - **NEW Step 4c (insert after Step 4b "Apply Story Locks")**: Title `"Apply Narrative Flow (news-explainer profile only)"`. Body:
    ```markdown
    Skip if `voice_profile == tutorial`. Tutorial scripts are allowed terse.

    For `news-explainer` scripts, the script MUST include at least:
    - 3 explanatory connectors across the body (because / why / to <verb> /
      and / but / plus / so / here's why / the reason)
    - 1 direct-address sentence in the body (NOT in the CTA): `"If you've
      [verb]ed/built/used/noticed X, [implication]"` is the canonical pattern
    - 1 engagement-CTA closer: rhetorical question + comments-ask + subscribe-ask

    Phase 2.5 Pass 6 will FAIL the script if any of these are missing.
    ```
- **MIRROR**: `phase2-script.md:136-170` for the existing reference-doc precedence pattern
- **GOTCHA**: The new Step 3.55 must come BEFORE Step 3.6 (library first, fence second). Do not put it after.
- **VALIDATE**: `grep -c "script-library.md" .claude/commands/diy-yt-creator/phase2-script.md` ≥ 1; `grep -c "voice_profile" .claude/commands/diy-yt-creator/phase2-script.md` ≥ 2

### Task 8: UPDATE `.claude/commands/diy-yt-creator/phase2-5-critique.md`

- **ACTION**: Add Pass 6 (Narrative Flow + Direct Address); promote CTA to independent gate; downweight Specificity in Pass 1
- **IMPLEMENT**:
  - **Pass 1 — Hook Strength (lines ~59–122)**: Apply the same formula change as Phase 1 Step 4D (Task 6). Specifically rebalance:
    ```
    base = (curiosity_gap * 0.4) + (stakes_clarity * 0.4) + (specificity * 0.2)
    ```
    The current equal-weighting is what scored `"100 billion dollars. 5 gigawatts. Zero Nvidia chips."` at 9.67/10. Under new weighting that opener still scores ~9 but loses its automatic 10.
  - **Pass 4 — Story Arc (lines ~187–280)**: Promote Arc Element 3 (CTA Strength) to an INDEPENDENT sub-gate:
    ```
    Quality Gate 2 splits into 2a + 2b:
      QG-2a: average of (Arc1, Arc2, Arc4) ≥ 7   (was: average of all 4)
      QG-2b: Arc3 (CTA Strength) ≥ 7              (NEW — independent gate)
    Both must pass.
    ```
    Update the Gate Summary table (lines ~393–399) to show QG-2a and QG-2b separately.
  - **NEW Pass 6 — Narrative Flow & Direct Address (insert after Pass 5)**: Body:
    ```markdown
    ## Pass 6: Narrative Flow & Direct Address (Quality Gate 5 — news-explainer profile)

    Skip if voice_profile == tutorial.

    ### Check 1 — Connector Density (1–10)

    Count occurrences in body scenes (NOT hook, NOT CTA) of: because, why,
    to <verb>, and, but, plus, so, here's why, the reason. Each unique
    connector counts once per scene.

    | Score | Criteria                                  |
    | ----- | ----------------------------------------- |
    | 9–10  | ≥ 5 connectors across body, ≥ 3 unique    |
    | 7–8   | ≥ 4 connectors, ≥ 2 unique                |
    | 5–6   | ≥ 3 connectors                            |
    | 3–4   | ≥ 1 connector                             |
    | 1–2   | 0 connectors (pure fragment script)       |

    QG-5a passes if score ≥ 6.

    ### Check 2 — Direct Address Sentence (0 or 2)

    Scan body scenes for at least one second-person sentence in patterns:
    - "If you ['re building on/'ve noticed/use/care about/build on] X, [implication]"
    - "You ['re probably/might be]…"
    - "Your [thing] just got [Y]."

    QG-5b passes if score == 2 (present).

    ### Check 3 — Engagement CTA Closer (0 or 2)

    Scan the FINAL scene for ALL three patterns:
    - Rhetorical/debate question (ends with `?`)
    - Comments-ask (`comments`, `let me know`, `tell me below`)
    - Subscribe-ask (`subscribe`, `for more <topic>`)

    QG-5c: 2 = all three present; 1 = two present; 0 = one or zero. Passes ≥ 2.

    ### Scoring

    QG-5 PASS: 5a ≥ 6 AND 5b == 2 AND 5c ≥ 2
    ```
  - **Gate Summary table (lines ~393–399)**: Add rows for QG-2a, QG-2b, QG-5. Old QG-2 row goes away.
- **MIRROR**: Existing Pass 1 / Pass 4 scoring patterns at lines 99–105 and 257–264
- **GOTCHA**: When `voice_profile == tutorial`, Pass 6 must SKIP cleanly (return PASS without scoring). The skip path matters — Thomas's tutorial scripts will rightly fail Direct Address and Engagement CTA checks.
- **VALIDATE**: `grep -c "Pass 6" .claude/commands/diy-yt-creator/phase2-5-critique.md` ≥ 2 (header + summary row); `grep -c "QG-2a\|QG-2b\|QG-5" .claude/commands/diy-yt-creator/phase2-5-critique.md` ≥ 3

### Task 9: UPDATE `.claude/skills/diy-yt-creator/new-anthropic-short.md`

- **ACTION**: One-line addition pointing the legacy/quick-path at the script library too
- **IMPLEMENT**: In Step 4 Branch B "Style rules for narration text" (around line 97), add a leading bullet: `"Read .claude/references/script-library.md first — its golden examples set the rhythm target. The rules below are the fence; the library is the goal."`
- **MIRROR**: The existing bullet style in that section
- **GOTCHA**: This is the only file outside `.claude/commands/diy-yt-creator/` and `.claude/references/` that drafts scripts (the legacy quick-path when no pipeline output exists). Skipping this would leave a back door where bad scripts get written despite the new gates.
- **VALIDATE**: `grep -c "script-library.md" .claude/skills/diy-yt-creator/new-anthropic-short.md` = 1

---

## Testing Strategy

### Validation Tests to Write

This is a markdown/prompt refactor, so "tests" are:

1. **Re-score the existing failure** (`videos/anthropic-amazon-compute/script.txt`) under the new gates. Expected outcome: FAIL on Pass 6 (Direct Address absent in body, Engagement CTA absent), FAIL on QG-2b (CTA strength 5/10 < 7). Hook still passes (8.5–9 under new weighting), but overall verdict is FAIL — matching the human verdict.

2. **Re-score the gold standard** (`videos/anthropic-100b-deal/script.txt`) under the new gates. Expected outcome: PASS on every gate. Specifically:
   - Pass 1 hook: ≥ 8 (the magnitude opener `"Anthropic just made one of the biggest AI hardware deals in history. And the numbers are absolutely insane."` scores high on curiosity + stakes; medium on specificity — net better than triple-stat opener under new weights)
   - Pass 6 connectors: ≥ 8 ("To keep …", "Why are they pouring … Because …", "If you've noticed …", "And subscribe")
   - Pass 6 direct address: 2 ("If you've noticed Claude being slow or buggy during peak hours, this is why.")
   - Pass 6 engagement CTA: 2 ("Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news.")
   - QG-2b CTA: 9–10

3. **Synthetic stat-dump test**: feed a script identical to ours but with all Pfizer/Lyft stats stripped. Expected outcome: still FAILS Pass 6 — proves the gate isn't keying on specific stats, it's keying on structure.

### Edge Cases Checklist

- [ ] Tutorial-profile script (e.g. a future Claude Code skills tutorial) correctly SKIPS Pass 6 and PASSES on the 4 original gates alone
- [ ] Brief without `voice_profile` field defaults to `news-explainer` (per dispatcher Task 4) — no crash, no missing-key error
- [ ] Pass 6 Check 3 (Engagement CTA) correctly handles a CTA in two sentences vs one (e.g., `"Is X taking over? Let me know. Subscribe."` should still score 2)
- [ ] Hook with NO numbers (e.g., a pure counterintuitive type B) still scores ≥ 7 under the new weights — we don't accidentally require stats in the hook
- [ ] Phase 1 hard cap of 5 scenes for ≤60s shorts: a 50s plan that needs 6 scenes triggers a clear error message pointing the planner at the cap rule

---

## Validation Commands

This pipeline has no compiler or test runner — validation is a structured re-score of the two reference scripts.

### Level 1: STRUCTURE (all files exist + dispatcher works)

```bash
# Files exist
test -f .claude/references/script-library.md
test -f .claude/references/brand-voice-tutorial.md
test -f .claude/references/brand-voice-news-explainer.md
test -f .claude/references/brand-voice.md

# Dispatcher is short
[ "$(wc -l < .claude/references/brand-voice.md)" -le 50 ]

# Tutorial profile is full
[ "$(wc -l < .claude/references/brand-voice-tutorial.md)" -ge 200 ]
```

**EXPECT**: All commands exit 0.

### Level 2: COMMAND FILE UPDATES (regex checks)

```bash
grep -q "voice_profile" .claude/commands/diy-yt-creator/phase0-research.md
grep -q "MAX 5 scenes" .claude/commands/diy-yt-creator/phase1-plan.md
grep -q "narrative_flow_bonus" .claude/commands/diy-yt-creator/phase1-plan.md
grep -q "script-library.md" .claude/commands/diy-yt-creator/phase2-script.md
grep -q "Pass 6" .claude/commands/diy-yt-creator/phase2-5-critique.md
grep -qE "QG-2a|QG-2b|QG-5" .claude/commands/diy-yt-creator/phase2-5-critique.md
grep -q "script-library.md" .claude/skills/diy-yt-creator/new-anthropic-short.md
```

**EXPECT**: All commands exit 0.

### Level 3: REFERENCE-SCRIPT RE-SCORING (manual or LLM-assisted)

Run the new Phase 2.5 critique mentally (or via LLM) against:

```
videos/anthropic-amazon-compute/script.txt   → expect FAIL on Pass 6 + QG-2b
videos/anthropic-100b-deal/script.txt        → expect PASS on all gates
```

**EXPECT**: Both outcomes match. If our (bad) script PASSES the new gates, the gates aren't strict enough. If the Gemini script FAILS, the gates are too strict.

### Level 4: NO-REGRESSION ON TUTORIAL PROFILE

Find any tutorial-style script that has shipped (e.g., from `videos/claude-connectors-everyday-life/` or similar). Re-score under new gates with `voice_profile: tutorial`. Pass 6 must SKIP cleanly. The 4 original gates must still apply.

**EXPECT**: Tutorial script's gate verdict is unchanged.

### Level 5: PIPELINE END-TO-END (manual)

After all 9 tasks land, regenerate the bad script via:

```bash
/diy-yt-creator:full-auto $100B Anthropic AWS deal
```

Compare the new `videos/<new-slug>/script.txt` to:
- The Gemini gold standard (target)
- Our previous bad output (failure mode)

The new script should read meaningfully closer to the Gemini one — more connectors, direct address present, engagement CTA at the end.

**EXPECT**: Subjective improvement matches a "would I post this to YouTube?" gut check.

### Level 6: BROWSER VALIDATION

N/A — no UI changes.

---

## Acceptance Criteria

- [ ] `videos/anthropic-amazon-compute/script.txt` re-scored under new Phase 2.5 gates → FAIL (matches human verdict)
- [ ] `videos/anthropic-100b-deal/script.txt` re-scored under new Phase 2.5 gates → PASS
- [ ] All Level 2 grep checks pass
- [ ] Tutorial profile (e.g., a Claude Code skills script) still scores PASS under unchanged Tutorial-relevant gates
- [ ] A new run of `/diy-yt-creator:full-auto` on the same Anthropic-deal topic produces a script with ≥ 3 connectors, ≥ 1 direct-address sentence, and an engagement CTA
- [ ] No HyperFrames CLI, lint, or render behavior changes
- [ ] No existing video's render breaks (the artifacts in `videos/anthropic-amazon-compute/` remain unchanged unless the user explicitly re-runs)

---

## Completion Checklist

- [ ] Task 1: `script-library.md` created with annotated Gemini gold standard
- [ ] Task 2: `brand-voice-tutorial.md` created (verbatim copy of current `brand-voice.md`)
- [ ] Task 3: `brand-voice-news-explainer.md` created with new rules + relaxations
- [ ] Task 4: `brand-voice.md` converted to dispatcher
- [ ] Task 5: `phase0-research.md` adds `voice_profile` field + heuristic
- [ ] Task 6: `phase1-plan.md` caps scene count + rebalances hook scoring
- [ ] Task 7: `phase2-script.md` reads library first, branches on profile, adds narrative-flow Step
- [ ] Task 8: `phase2-5-critique.md` adds Pass 6 + promotes CTA to independent gate
- [ ] Task 9: `new-anthropic-short.md` legacy path points at script-library
- [ ] All Level 1–4 validation commands pass
- [ ] Level 5 manual re-run produces a noticeably better script

---

## Risks and Mitigations

| Risk                                                                             | Likelihood | Impact | Mitigation                                                                                                                                  |
| -------------------------------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| New gates over-correct → news-explainer scripts become formulaic ("If you …" + question every time) | MED        | MED    | Pass 6 Check 2 accepts multiple direct-address patterns, not just `"If you …"`. Library annotations explicitly warn against copy-paste.    |
| Tutorial-profile gating accidentally re-applies Pass 6 (e.g., agent forgets to skip) | LOW        | HIGH   | Pass 6 has explicit skip-on-`voice_profile==tutorial` guard at the top. Add a sentinel test in Level 4 validation.                          |
| `voice_profile` heuristic in Phase 0 picks the wrong profile (e.g., `tutorial` for a news topic) | MED        | HIGH   | Heuristic table is conservative — defaults to `news-explainer` on ambiguity. Phase 1 plan-summary surfaces the chosen profile to the user. |
| Splitting brand-voice into two files breaks an external skill that imports `brand-voice.md` directly | LOW        | LOW    | Keep `brand-voice.md` as a 30-line dispatcher (Task 4) so the path stays valid. Any external import gets a redirect, not a 404.            |
| Hook score weight rebalance accidentally drops the gold-standard's score below 7 | LOW        | HIGH   | Test it explicitly in Level 3 BEFORE shipping. The Gemini opener is curiosity-heavy + stakes-medium + specificity-low — re-weighting toward curiosity+stakes raises its score, doesn't lower it. |
| Cap of 5 scenes for ≤60s breaks legitimate dense plans (e.g., a 60s "5 stats in a row" StatCascade hook pattern) | LOW        | MED    | Cap is on the PLAN, not the SCRIPT. Five scenes can each be a stat. The cap stops 8-scene over-fragmentation, not stat density.            |
| Engagement-CTA gate forces every news-explainer to feel like generic YouTuber slop | LOW        | MED    | Library annotations show the Gemini line as the canonical example — it's a single sentence, not a 30-second outro. Gate accepts the minimum, doesn't demand more. |

---

## Notes

**Why this isn't just "tweak the prompt and hope":**

The current pipeline produces measurably broken outputs (the user said "not good") that the gates rate as 9–10/10. That's a calibration error, not a prompt-quality error. Calibration errors don't get fixed by writing better prose — they get fixed by changing what the gates measure.

**Why split the voice profiles:**

Reading the existing `brand-voice.md` closely: it's an excellent voice spec for Thomas's developer-tutorial channel, where he's the practitioner. Many of its rules (no "we", no motivational frame, no "this is huge", first-person-only, dry sarcasm calibrated for tutorials) are actively wrong for a 45-second short summarizing an industry announcement where the narrator is reporting, not building. Trying to make one voice spec work for both is why our Anthropic-deal script came out structurally identical to a tutorial — terse, fragmented, no connective tissue. Two profiles let each be sharp.

**Why the Gemini script wins (mechanical breakdown):**

| Property                                          | Gemini                                  | Ours                                    |
| ------------------------------------------------- | --------------------------------------- | --------------------------------------- |
| Opening type                                      | Magnitude framing (claim + amplifier)   | Triple-stat slam                        |
| Scenes (45–60s)                                   | One continuous paragraph (effectively 4–5 logical beats) | 8 explicitly demarcated scenes          |
| Explanatory connectors                            | 6+ (`To keep`, `over the next`, `because`, `Plus`, `Why … Because`, `If you've noticed`) | 0                                       |
| Direct viewer address (body, not CTA)             | 1 (`If you've noticed Claude being slow…`) | 0                                       |
| CTA structure                                     | Question + comments-ask + subscribe-ask | Declarative ("the compute crunch is over.") |
| Total words                                       | ~210                                    | ~150                                    |
| Total duration estimate                           | ~84s (over 60s — a real Short is shorter, BUT) | ~52s                                    |
| Reading-flow                                      | Smooth — every sentence sets up the next | Choppy — each sentence stands alone     |

The duration overage on the Gemini script is real but solvable — a tighter version of the Gemini structure at 60s would still beat our 52s output on every flow metric. Length isn't what makes ours bad; structure is.

**Future scope (NOT this plan):**

- Add `comparison` profile for vs/benchmark videos.
- Build an automated re-scorer that takes a script.txt and outputs the Pass 6 verdict — would let us regression-test the gates over time.
- After 3–4 winners ship, audit `script-library.md` for emergent patterns and lift them into `brand-voice-news-explainer.md` rules.
- Consider an inverse Library: `script-anti-library.md` with our worst-rated outputs annotated. Useful for "don't do this" calibration of future writers.
