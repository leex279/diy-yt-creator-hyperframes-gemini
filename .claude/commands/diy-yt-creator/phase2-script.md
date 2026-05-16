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

**Also extract `voice_profile`** from `videos/<slug>/research/content-brief.md` (added in Phase 0 Step 0E). Acceptable values: `tutorial`, `news-explainer`, `comparison`. If the field is missing or unrecognized, default to `news-explainer` (per `brand-voice.md` dispatcher rules). Store this value — it drives Step 3.55, Step 3.6, and Step 4c below.

### Extract Thesis (anti-slop methodology)

Read the brief's `## Thesis` section. This is one falsifiable sentence — a claim that could be wrong. **The script body MUST argue this thesis**, not just describe the topic. If the body never advances the thesis, Phase 2.5 Pass 4 (Arc Element 4 — Narrative Cohesion) will flag it.

**How to argue a thesis in narration**:
1. State the thesis (or its core position) early — the hook can plant it implicitly, the body must commit explicitly.
2. Provide the evidence chain — receipts from the brief's `## Receipts` section.
3. Address the counter-position briefly — what would make the thesis wrong, why the evidence rules that out.
4. Close with the implication — what changes for the viewer if the thesis is true.

If the thesis feels too bold, narrow it; do not soften it into a description. A bold-but-wrong thesis can be revised; a generic description is unfixable.

### Extract Receipts

Read the brief's `## Receipts` section. These are the linkable, verifiable artifacts the script may reference. Two rules:

1. **No new authority claims**: every "according to X" or attribution in the script MUST trace to a Receipts entry OR to a brief Proof Points entry with a source URL. Inventing a new "studies show 73%" line is a Phase 2.5 Pass 5 (QG-4) FAIL.
2. **Per-scene Receipt comments (optional but recommended)**: when a scene makes a factual claim that comes from a specific receipt, append a `<!-- Receipt: <url> -->` HTML comment after the scene's narration in `full-script.md`. Phase 2b cross-checks these against the brief's Receipts list.

If the brief was waived under `topic_type: CONCEPT`, the Receipts list will be empty — but the authority-without-evidence ban (Phase 2.5 Pass 5) still applies. Script must not invent stats.

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

## Step 3.55 — Read the Script Library (gold-standard examples)

Before applying any voice rules, read the matching profile section in `.claude/references/script-library.md`. The library quotes verbatim scripts that worked, with per-paragraph annotations showing exactly which moves earned the click.

Look up the section by `voice_profile` (extracted in Step 1):

- `news-explainer` → read the **Profile: news-explainer** section (Anthropic / AWS deal annotated example)
- `tutorial` → read the **Profile: tutorial** section (placeholder if no winners shipped yet)
- `comparison` → fall back to news-explainer (deferred — no comparison-specific examples yet)

Note the rhythm: **claim → explanation → stake → direct address → CTA**. Aim for the same shape, NOT the same words. Each annotated example calls out "what to learn" (rhythm targets) and "what NOT to copy" (specific phrases that are now burned).

The library is the single source of truth for "what good looks like." Voice rules are the single source of truth for "what bad looks like." Read the library first; voice rules are the fence, not the goal.

## Step 3.6 — Consult the Scriptwriting References

Before writing, read BOTH reference docs in this order — brand-voice is more specific and overrides the generic playbook where they differ:

### A. The matching brand-voice profile (CHANNEL-SPECIFIC — read first)

Look up the active brand-voice profile by the `voice_profile` field (from Step 1):

- `tutorial` → read `.claude/references/brand-voice-tutorial.md`
- `news-explainer` → read `.claude/references/brand-voice-news-explainer.md`
- `comparison` → currently falls back to `.claude/references/brand-voice-news-explainer.md` (deferred — no comparison-specific profile yet)
- missing or unrecognized → read `.claude/references/brand-voice-news-explainer.md` (default per `brand-voice.md` dispatcher)

The active profile is the narrator's voice spec — it tells you exactly how the script should sound when read aloud. Apply ALL rules from the matching file. Each profile defines its own:

- 3 core adjectives (e.g., tutorial: "Enthusiastic. Practical. Honest." / news-explainer: "Clear. Contextual. Direct.")
- Sentence rhythm pattern (e.g., tutorial: Short → Longer → Short → Opinion / news-explainer: Claim → Explanation → Stake → Implication)
- Acceptable hook types (some shared across profiles, some profile-specific — e.g., news-explainer adds Type A-news Magnitude framing, tutorial keeps Type A Honest Result)
- Per-scene structure
- Hard rules (the "what Claude must NOT do" list)
- Banned word lists (Universal Bans shared across profiles + profile-specific additions/relaxations)
- For news-explainer specifically: mandatory connectors (≥3 in body), mandatory direct-address sentence (≥1 in body), mandatory engagement CTA (question + comments-ask + subscribe-ask). Phase 2.5 Pass 6 enforces these.

The Phase 2.5 critique will enforce ALL of the active profile's rules. Pass 6 (Narrative Flow / Direct Address / CTA) skips for `voice_profile == tutorial`.

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

## Step 4c — Apply Narrative Flow (news-explainer profile only)

**Skip if `voice_profile == tutorial`.** Tutorial scripts are allowed terse and fragment-heavy because the narrator is the practitioner — they don't need to bridge scenes with explanatory connectors.

**For `news-explainer` and `comparison` profiles**, the script MUST include at least:

1. **3 explanatory connectors across the body** (across all scenes between the hook and the CTA), with **at least 2 unique** types from this list:
   `because` / `why` / `to <verb>` / `and` / `but` / `plus` / `so` / `here's why` / `the reason`

   Pure-fragment scripts ("$100B. 5GW. Zero Nvidia. Compute crunch is over.") have zero connectors and FAIL Phase 2.5 Pass 6 Check 1. Aim for 5+ connectors (the gold-standard target — see `script-library.md`).

2. **1 direct-address sentence in the body** (NOT in the hook, NOT only in the CTA). Canonical patterns:
   - `"If you ['re building on / 've noticed / use / care about] X, [implication]"`
   - `"You ['re probably / might be] [verb]ing X — [implication]"`
   - `"Your [thing] just got [Y]."`

   The Gemini gold-standard line is: `"If you've noticed Claude being slow or buggy during peak hours, this is why."` Aim for the same texture, not the same words.

**Note**: The engagement-CTA closer is enforced separately in Step 4d below and applies to ALL voice profiles (including tutorial). Step 4c's connector + direct-address checks remain news-explainer/comparison only.

**Audit pass (do this BEFORE saving the script in Step 5)**:

- [ ] Count connectors. Are there ≥ 3 in body scenes, with ≥ 2 unique types?
- [ ] Find the direct-address sentence. Is there ≥ 1 in the body, in second person?

If any of these are missing, REWRITE before saving. Phase 2.5 Pass 6 will FAIL the script and block TTS otherwise.

## Step 4d — Apply Engagement CTA (ALL voice profiles, MANDATORY)

**Applies to every video, every voice_profile, every template — no exceptions.** See [`.claude/rules/engagement-cta.md`](../../rules/engagement-cta.md) for the canonical rule.

The final 3-5 seconds of the script MUST close on a **debate-sparking question** that satisfies all four HARD criteria:

1. **Binary or short-list answer** — answerable in 1-5 words. `"Team A or team B?"` / `"Yes or no?"` / `"Which one are you switching to?"`. NOT `"How would you architect this differently?"` (too high-effort).
2. **Polarizing / contrarian stance baked in** — the question takes a side, dares disagreement, OR forces side-picking. Pure-neutral `"What do you think?"` is BANNED.
3. **References a specific claim from the video** — must build on a concrete stat, comparison, hot take, deprecation, or winner-takes-all framing the viewer just watched.
4. **Low cost to answer** — 5 seconds from any viewer, expert or beginner.

### CTA question patterns (use as templates, never copy verbatim)

| Pattern | Example | When to use |
|---|---|---|
| Tool-vs-tool | `"Claude or Cursor — which one are you shipping with in 2026?"` | Comparison videos, ecosystem shifts |
| Dead-or-alive | `"Is the browser-tab era actually over, or is this just hype?"` | Trend-claim videos, "X is dying" hot takes |
| Pick-the-winner | `"Of the 15 new connectors — which one ships first to your workflow?"` | Feature-rollout videos, multi-item lists |
| Hot-take confirm | `"Claude reading your emails — useful or terrifying?"` | Privacy/UX-controversial features |
| Adoption deadline | `"Three months from now, will you still open tabs for these tools?"` | Predictive / forecast-style closers |
| Stop-doing-X | `"What's the first browser tab you'd close if Claude could do that job?"` | Workflow-shift videos |
| Hill to die on | `"Which Claude feature is the one you'd quit your job to keep?"` | Identity-tied feature highlights |

Best CTAs combine TWO patterns — e.g., dead-or-alive + pick-a-side: `"Browser tabs are dying — or is this just another integration fad? Which side are you on?"`

### Banned closers (zero tolerance — rewrite if found)

These are AUTOMATIC FAIL on Phase 2.5 QG-2b regardless of the rest of the script:

- `"What do you think?"` / `"What are your thoughts?"`
- `"Let me know in the comments"` (without an anchoring question)
- `"Like and subscribe if you enjoyed"`
- `"Drop your thoughts below"`
- `"How would you build this differently?"` (too high-effort to answer)
- `"Did this help you?"` (yes/no with no debate value)
- `"Anything I missed?"`
- `"Link below."` as the sole closer
- Any CTA that requires watching the video twice to answer

### For news-explainer / comparison profiles only — keep the comments + subscribe asks

When `voice_profile == news-explainer` or `comparison`, the CTA closer should ALSO include:
- Comments-ask phrase (`comments`, `let me know`, `tell me below`, `drop your pick below`)
- Subscribe-ask phrase (`subscribe`, `for more <topic>`, `follow for more`)

These wrap around the debate question, they do NOT replace it. Phase 2.5 Pass 6 (QG-5c) enforces the comments+subscribe pair for those profiles. The debate-question itself is enforced by QG-2b (Arc 3 CTA Strength) for all profiles.

### Audit pass (do this BEFORE saving the script in Step 5)

- [ ] Read the final 1-2 sentences of the script. Does it ask a question (ends with `?`)?
- [ ] Does the question satisfy all four HARD criteria (binary/short-list, polarizing, specific to video, low-cost to answer)?
- [ ] Is the closer NOT in the banned list above?
- [ ] If `voice_profile == news-explainer` / `comparison`: are comments-ask AND subscribe-ask also present after the question?
- [ ] Does the question fit in ~3-5s of speech (8-14 words at 160 WPM for Shorts)?

If any check fails, REWRITE before saving. Phase 2.5 QG-2b and QG-5c both backstop this gate but the cheapest place to fix a weak CTA is BEFORE TTS.

## Step 5 — Save Full Script for Review

Save the complete script to `videos/<slug>/scripts/full-script.md` as **plain narration text only**.

```markdown
# [Video Title]

## Scene 1: [Name]

[Plain narration text for this scene. No word counts, no annotations, no TTS markup. Just the words the narrator will speak.]

<!-- Receipt: https://example.com/source — only when this scene makes a factual claim sourced from a brief Receipt -->

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
- **Per-scene Receipt comments are HTML comments** (`<!-- Receipt: ... -->`) — TTS, captions, and the user-facing review render strip them. Add ONE per factual scene whose claim comes from a brief Receipts entry. Skip on hook/CTA/transition scenes that aren't making sourced claims. Phase 2b cross-checks every Receipt URL against the brief.

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
