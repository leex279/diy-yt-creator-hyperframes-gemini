---
description: "Phase 2 — Write narration script for user review (raw, no TTS markup)"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

<objective>
Execute Phase 2 of the HyperFrames pipeline.
Write a high-retention narration script using the Kallaway Formula and present it for user review.

**Goal**: Write viral-quality narration using proven hook techniques and linguistic precision, then STOP for user review before any TTS optimization.

**Input**: `videos/<slug>/plan.md` (from Phase 1)
**Output**: `videos/<slug>/scripts/full-script.md`
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

If invoked as part of the orchestrator:
- **DO NOT STOP for user review** — proceed directly to Phase 2.5
- Use plan's `tone` for writing style
- Use brief's `Technical Terms` for pronunciation planning
- Use brief's `Must-Mention Points` to ensure required points are covered

The script review checkpoint is skipped in autonomous mode.
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.
- **Prerequisites**: Verify `1 - Plan` is `done`.
  - If not: STOP and report "Phase 1 (Plan) has not run. Run `/diy-yt-creator:phase1-plan <slug>` first."
- **Re-run check**: If `2 - Script` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

## Step 1 — Read the Plan & Research

Read `videos/<slug>/plan.md` and `videos/<slug>/research/content-brief.md`.

Extract: scene list, durations, key messaging, tone, visual beats, hook architecture, cult-hopping references, must-mention points, technical terms.

### Selected Hook Variant

Confirm which hook variant was selected in Phase 1:
- Read `plan.md` → `## Hook Variants` section → look for `recommended:` field
- In **interactive mode**: if not selected, show all three variants and ask the user to pick before proceeding
- In **autonomous mode**: use the highest-scoring variant automatically

The selected hook variant's opening line becomes the **mandatory first sentence** of Scene 01. Do NOT improvise a different hook — the variant was scored and selected for a reason.

## Step 2 — Calculate Word Targets

For each scene, calculate target word count at ~2.5 words/second:

| Scene duration | Target words |
| -------------- | ------------ |
| 10s            | ~25          |
| 15s            | ~37          |
| 20s            | ~50          |
| 25s            | ~62          |
| 30s            | ~75          |

Leave ~2-3s of silence buffer per scene (audio starts after scene transition).

## Step 3 — Write the Hook (Kallaway Formula)

The hook is the most critical part. Apply the Three-Step Hook Formula:

### 3a: Context Lean-In (first 4 seconds)

Establish topic clarity immediately. The viewer must self-select.
- For feature/tutorial videos: **name the feature and its benefit immediately**
- For problem/analysis videos: use a **mind-blowing fact** OR a **shared pain point**
- DO NOT default to shame framing ("Most developers don't know...") — your audience already uses the tool
- Example (Tech): "You're juggling scattered websites and messy documents."
- Example (General): "Finding a fact in a PDF feels like finding one grain of sand on a beach."

### 3b: Scroll-Stop Interjection (the Stun Gun)

Insert a contrasting transition word to halt momentum mid-thought:
- **Primary Stun Guns**: "But," "However," "Yet," "Although"
- This is a stop sign in the middle of a sentence
- Example: "...scattered documents. **But** imagine if..."

### 3c: Contrarian Snapback (the Uno Reverse)

Snap the viewer onto an unexpected path:
- If you started praising something, reveal it's actually the least impressive part
- Create the "Hook, Line, and Sinker" effect
- Example: "...But this isn't just another search engine — it's an automated knowledge base that reads everything for you."

## Step 3.5 — Write the Preview Hook (60s+ videos)

For videos 60s+, write a Scene 00 preview that increases watch time by ~32%.

For sub-30s Shorts, the hook variant IS the preview — skip this step.

### Preview Hook Formula

- **Duration**: 10-15 seconds (~25-37 words at 2.5 wps)
- **Pacing**: 1.15× normal speed (use `--preview` flag for TTS)
- **Energy**: HIGH — this is the attention grab

### Structure

1. **Attention Grab** (2-3 words, ~1s):
   - For feature/tutorial videos: **name the feature** — "Skills system.", "Print mode."
   - For analysis/problem videos: bold stat or shocking statement — "85% of developers..."
   - DO NOT default to stats for feature videos — your audience clicked for the feature, show it.

2. **Teaser Phrases** (3-4 phrases, 4-6 words each, ~6-8s):
   - Quick mentions of key features/outcomes from upcoming scenes
   - NO explanation, just intrigue — create "open loops"
   - Each teaser should reference a specific visual that will appear later
   - Example: "Automated testing. Real-time suggestions. Zero config."

3. **Promise Statement** (8-12 words, ~3s):
   - "In this video, I'll show you exactly how..."
   - "Let me show you the [X] that changed everything..."
   - Specific value proposition that ties the teasers together

### Preview script template

```markdown
## Scene 00 Preview

[Bold stat or statement — 2-4 words]
[Teaser 1 — 4-6 words referencing Scene 03-04 visual]
[Teaser 2 — 4-6 words referencing Scene 05-06 visual]
[Teaser 3 — 4-6 words referencing final feature visual]
[Promise statement — 8-12 words]
```

## Step 3.6 — Consult the Scriptwriting References

Before writing, read BOTH reference docs in this order — brand-voice is more specific and overrides the generic playbook where they differ:

### A. `.claude/references/brand-voice.md` (CHANNEL-SPECIFIC — read first)

This is the narrator's voice spec — it tells you exactly how the script should sound when read aloud. Apply ALL rules:

- **Voice profile**: Enthusiastic. Practical. Honest. (3 core adjectives — every line should fit at least one)
- **The 4 acceptable hook types** (only these — narrower than the generic catalog):
  - Type A — The Honest Result: *"I ran [X] for [time]. Here's what actually happened."*
  - Type B — The Counterintuitive Observation: *"[Common assumption]. [One sentence that breaks it]."*
  - Type C — The Specific Number: *"[Precise number] [thing]. [Why that matters in one sentence]."*
  - Type D — The Shared Frustration: *"[Specific problem stated as a fact, not a question]."*
- **First-person singular only**: "I tried", "I was wrong" — never "we", never "one should"
- **Short → Longer → Short → Opinion** rhythm pattern (per §"Sentence Rhythm Rules")
- **No false research claims**: banned to imply original benchmarks/long-term tests that didn't happen ("I tested X for 30 days" → BANNED unless explicitly true and brief). Curate, don't invent.
- **Always attribute third-party claims to a source** — never present someone else's claim as personal validation
- **Per-scene structure**: Observation → Implication → Action/Example
- **The 10 hard rules** ("What Claude Must NOT Do"): no greeting, no preview summary, no motivational frame, no manufactured stakes, no em dashes in narration, no bullet narration, no attributed emotions to viewer, no vague promise endings, no false research claims, always attribute claims
- **Banned word lists** (§"The 50-Word Banned List"): generic AI phrases (delve, leverage, paradigm, seamless, …), hype phrases (changed everything, smash that like button, mind-blowing, …), over-hedging phrases (some might argue, arguably, …)

The Phase 2.5 critique will enforce ALL of these.

### B. `.claude/references/faceless-tech-scriptwriting-playbook.md` (GENERIC — broader context)

Use these sections:
- **§4 (Writing Voice for TTS)**: Gary Provost rhythm, Golf Buddy tone, TTS-specific rules
- **§5 (Transitions)**: Use these instead of defaulting to "But here's the thing" or "Let me show you"
- **§11 (Banned Patterns)**: Critical/High phrases that compound with brand-voice's banned list
- **§2 (Script Structure)**: Use But/Therefore chains, not "And then" sequences

Where brand-voice.md and the playbook conflict, **brand-voice.md wins** — it's the narrator-specific spec.

Do NOT use any phrase from EITHER banned list. Phase 2.5 will block the script if found.

## Step 3.7 — Scars Mining (Credibility Signal)

Identify **1-2 experience signals** for this topic — specific friction points, failure modes, or time traps that a practitioner would know but ChatGPT cannot replicate.

**Commodity Test**: "Can a viewer get the core answer from ChatGPT in 10 seconds?" If YES, the script needs repositioning to the experience layer before writing begins.

For each major scene, ask:
- What is the most common mistake a developer makes when first encountering this?
- What does the documentation skip that causes real failures in practice?
- What took days to figure out that can be compressed into one sentence here?

**Scar insert patterns**:
- "The docs skip this — if you [X] before [Y], it silently fails."
- "Took me three weeks to realize: [specific technical gotcha]."
- "Almost every team makes this mistake on first setup: [specific error]."

At least 1 scar must appear somewhere in the final script. Phase 2.5 will check for its presence.

## Step 4 — Write the Full Script

Write the complete narration as one flowing document, applying these techniques:

### Benefit-Led Scripting

Viewers care about their problems, not your features:
- **Mediocre (Feature-led)**: "Magnesium is a core mineral."
- **Viral (Benefit-led)**: "If you want better sleep, you need magnesium."

For each feature scene, ask: "What problem does this solve for the viewer?"

### Cult Hopping Strategy

Wrap unknown ideas in known layers:
- Reference established brands or celebrities for subconscious comfort
- Example: "Like Taylor Swift's financial advisor..." makes tax planning feel familiar
- Draft off existing credibility to accelerate trust

### The Distillation Technique ("Say It Twice")

Maximize comprehension by providing two "cracks" at the point:
1. **The Expert Line**: Use technical language. ("SpaceX caught the Starship in the Mechazilla.")
2. **The 5-Year-Old Line**: Use a metaphor. ("It's like metal chopsticks catching a 23-story building.")

### Linguistic Precision (Rhythm & Cadence)

**The Staccato Rule**: Short, punchy sentences for hooks. High value density per word.

**The Boxer's Rhythm**: Vary your "punches."
- Three "Jabs" (short sentences) → one "Overhand" (longer contextual sentence)
- Example: "It's fast. It's precise. It never forgets. And it integrates with everything you already use."

**Pop-Pop-B Pattern (Three-Item Lists)**:
- Two short "Pops" + one longer contextual "B"
- Example: "The energy you bring, the charisma you show, and the rhythm of how you speak."

**The Jagged Edge Test**:
- Audit visually — if the right margin is a straight line, it's monotonous
- You need variety in sentence length creating a "jagged edge"

**Down-Energy Syllables**:
- End sentences on hard "down" notes to signal completion
- Avoid upspeak patterns that sound uncertain

### Tone Guidelines (from plan)

- **tech-influencer**: Short punchy sentences. Rhetorical questions. Confident swagger.
- **professional-corporate**: Clear, authoritative. No slang. Trust through precision.
- **friendly-educational**: Conversational. "Let me show you..." Warm and approachable.
- **dramatic-cinematic**: Building tension. Strategic pauses. Cinematic reveals.

## Step 4b — Apply Story Locks (Enhancement Pass)

After writing the full script, review it through the lens of the **6 Story Locks** (full reference: `.claude/references/story-locks.md`). This is an enhancement pass — the core script should already be solid.

1. **Term Branding**: Identify 1-2 core concepts → give them a memorable name (short, vivid, 2-3 words).
2. **Embedded Truths**: Search for hedging words (`if`, `maybe`, `might`, `could`, `probably`) → replace with certainty framing (`when`, `the reason`, `once you`, `this is how`).
3. **Thought Narration**: Add 1-2 moments where you narrate the viewer's likely thought at major transition points ("You're probably thinking: *'...'*").
4. **Negative Frames**: Consider negative-framing at least one key point — flip "here's how to do X" into "stop doing X wrong".
5. **Loop Openers**: Add re-engagement phrases between major sections ("But that's not even the most interesting part", "Here's where it gets crazy").
6. **Contrast Words**: Ensure key pivot sentences use A→but→B structure — vary the contrast word (but, actually, instead, turns out, except).

**Note**: Don't force every lock into every script. Short scripts (15-30s) may only use Embedded Truths + Contrast Words. The goal is natural integration, not a checklist quota.

## Step 5 — Save Full Script for Review

Save the complete script to `videos/<slug>/scripts/full-script.md` as **plain narration text only**.

```markdown
# [Video Title]

## Scene 1: [Name]

[Plain narration text for this scene. No word counts, no annotations, no TTS markup. Just the words the narrator will speak.]

## Scene 2: [Name]

[Plain narration text...]

## Scene 3: [Name]

[Plain narration text...]
```

**IMPORTANT**:
- Write ONLY the narration text — no metadata, no word counts, no checklists
- Plain, human-readable form — no TTS optimizations yet (no pronunciation fixes, no break tags)
- Keep scene headers simple: just `## Scene N: [Name]`
- This is what the user will review and edit directly

</process>

<output>
**File created**: `videos/<slug>/scripts/full-script.md`

**STOP HERE — User Review Required (interactive mode only)**

Tell the user:
> "Script created: `videos/<slug>/scripts/full-script.md`
>
> Please review and edit the script directly in that file. When you are satisfied with the content, run the quality gate:
> `/diy-yt-creator:phase2-5-critique <slug>`
>
> Phase 2.5 runs a four-pass LLM critique (Hook Strength, Retention Curve, TTS Readability, Story Arc, AI-Phrasing) and gates access to Phase 2a. Only scripts that score ≥ 7/10 on Hook Strength and Story Arc, with zero banned phrases, will proceed to TTS optimization."

Do NOT (in interactive mode):
- Proceed to TTS optimization
- Create scene files
- Present detailed quality assessments or checklists

Just create the plain script file and stop.

In autonomous mode (called from `/diy-yt-creator:full-auto`), the orchestrator dispatches Phase 2.5 immediately — do not present the user prompt.

### Update Phase Status

Update `videos/<slug>/phase-status.md` — set the `2 - Script` row to `done <YYYY-MM-DD>` (today's date).
</output>

<quality-checklist>
## Built-in Author Checklist

Before declaring the script written, verify:

0a. [ ] **Hook Variant Used**: Did I use the selected hook variant's opening line as written in the plan?
0b. [ ] **Open Loop Established**: Is the primary open loop (from plan's `open_loop_architecture` section) raised within the first 60 seconds?
0c. [ ] **Value Alignment**: Does the hook name the video's main feature/concept within the first sentence?
1. [ ] **Benefit First**: Did I lead with a pain point solve?
2. [ ] **Cult Hop**: Did I anchor the niche in a known reference?
3. [ ] **Value Compression**: Is there a unique "value hit" before the 4-second mark?
4. [ ] **Clarity Check**: Is the message distilled to its atomic unit?
5. [ ] **Stun Gun**: Does the hook contain a "But/However/Yet" interjection?
6. [ ] **Uno Reverse**: Does the hook snap to an unexpected path?
7. [ ] **Jagged Edge**: Do sentence lengths vary visibly?
8. [ ] **Say It Twice**: Are complex concepts explained both technically and simply?
9. [ ] **Term Branded**: Did I coin at least 1 named framework/concept?
10. [ ] **No Hedging**: Are "if/maybe/might/could" replaced with "when/the reason/once you"?
11. [ ] **Thought Narration**: Did I narrate the viewer's likely thought at least once?
12. [ ] **Negative Frame**: Is at least one point framed as a warning/mistake to avoid?
13. [ ] **Loop Openers**: Are there re-engagement phrases between major sections?
14. [ ] **Contrast Words**: Do key points use A→but→B structure?

These are author checks — formal gate enforcement happens in Phase 2.5.
</quality-checklist>

### Retention Structure Requirements (MANDATORY)

Every script must satisfy all of the following before proceeding to Phase 2a (Phase 2.5 enforces them):

1. **Open Loop per Scene**: Each scene (except final CTA) ends with an open loop phrase
2. **Chapter Names as Curiosity Gaps**: Scene headers in `full-script.md` are curiosity gaps, not topic labels
3. **WPM in Range**: Each scene's word count ÷ duration = 150-165 WPM (mark deviations in header comments)
4. **Silence Cues**: High-impact reveal words preceded by `[PAUSE]` on its own line (Phase 2a will preserve these)
