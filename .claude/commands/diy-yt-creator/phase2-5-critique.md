---
description: "Phase 2.5 — LLM script critique loop: five-pass quality gate before TTS"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

<objective>
Execute Phase 2.5 of the HyperFrames pipeline.

**Goal**: Catch structural problems in the script before TTS generation. Run a five-pass automated critique that gates progress to Phase 2a.

**Input**: `videos/<slug>/scripts/full-script.md` (from Phase 2)
**Output**: `videos/<slug>/scripts/critique-report.md`
**Gate condition**: Hook Score ≥ 7.0 AND Story Arc Score ≥ 7.0 AND Loop Opener count ≥ required minimum AND banned phrase count == 0

If ANY gate fails, the script is BLOCKED from Phase 2a until the issue is fixed and Phase 2.5 is re-run.
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

Run all five passes automatically. If all gates pass, proceed to Phase 2a immediately. If any gate fails, STOP orchestration and report which gate(s) failed with specific actionable issues. Do not ask questions.
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.
- **Prerequisites**: Verify `2 - Script` is `done`.
  - If not: STOP and report "Phase 2 (Script) has not run. Run `/diy-yt-creator:phase2-script <slug>` first."
- **Re-run check**: If `2.5 - Critique` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

## Step 1 — Read the Script

Read the following files:
- `videos/<slug>/scripts/full-script.md` — the script to critique
- `videos/<slug>/plan.md` — the video plan (for open loop references and hook variants)
- `.claude/references/story-locks.md` — reference for Loop Opener definitions
- `.claude/references/faceless-tech-scriptwriting-playbook.md` — generic banned phrase list (§11)
- `.claude/references/brand-voice.md` — channel-specific voice spec (banned word lists, 10 hard rules, 4 acceptable hook types, voice QA checklist)

Calculate metrics from the script:
- `total_word_count` — sum of all scene word counts
- `estimated_duration_seconds` = total_word_count / 2.5
- `estimated_duration_minutes` = estimated_duration_seconds / 60
- `mid_video_word_target` = total_word_count × 0.58

Report:
```
Script: videos/<slug>/scripts/full-script.md
Total words: N
Estimated duration: Xm Ys (N seconds)
Mid-video word target (58%): N words
```

---

## Pass 1: Hook Strength Scoring (Quality Gate 1)

Analyze the hook scenes (Scene 00 Preview if present + Scene 01 Hook). Score five dimensions:

### Dimension 1 — Curiosity Gap Strength (1-10)
- 9-10: Single sentence creates immediate, unambiguous curiosity gap
- 7-8: Curiosity gap present but takes 2-3 sentences to establish
- 5-6: Some curiosity but could be dismissed
- 3-4: Informational opening, no gap created
- 1-2: Generic introduction, no hook

### Dimension 2 — Stakes Clarity (1-10)
- 9-10: Specific, quantified stakes ("you will waste 6 months rebuilding")
- 7-8: Stakes are clear but general ("this will save you significant time")
- 5-6: Implied stakes, viewer must infer
- 3-4: Benefits mentioned but stakes not established
- 1-2: No stakes established

### Dimension 3 — Specificity (1-10)
- 9-10: Specific stat or number in opening line ("73% of devs...")
- 7-8: Named tools or specific examples within first 30 seconds
- 5-6: Some specificity but could be more concrete
- 3-4: Generic language throughout hook
- 1-2: Completely abstract

### Dimension 4 — Scroll-Stop Interjection (0 or 2)

Presence of But/However/Yet/Although pivot within the hook.

### Dimension 4b — Value Alignment (0 or 0.5)

Does the hook name the video's main topic/feature within the first 2 sentences?
- 0.5: Feature/concept named directly — viewer knows what they'll learn by second 4
- 0: Hook creates tension/curiosity without naming the subject

### Dimension 5 — Promise Statement (0 or 1)

Explicit promise of resolution ("In the next X minutes, you will...").

### Scoring Formula

```
base = (D1 + D2 + D3) / 3
stun_bonus = D4 / 20        # 0.0 or 0.1
alignment_bonus = D4b       # 0.0 or 0.5
hook_score = min(10, round(base + stun_bonus + alignment_bonus + D5, 1))
```

**Quality Gate 1**: Hook Score MUST be ≥ 7.0 to proceed.

### Output Format

| Dimension       | Score      | Notes                                         |
| --------------- | ---------- | --------------------------------------------- |
| Curiosity Gap   | X/10       | [specific observation]                        |
| Stakes Clarity  | X/10       | [specific observation]                        |
| Specificity     | X/10       | [specific observation]                        |
| Stun Gun        | X/2        | [present/absent + exact phrase if present]    |
| Value Alignment | X/0.5      | [Hook names video's subject in first 2 sentences? Yes/No] |
| Promise         | X/1        | [present/absent]                              |
| **HOOK SCORE**  | **X.X/10** | **PASS / FAIL (threshold: 7.0)**              |

**On FAIL**: Provide 2-3 specific replacement sentences, not general advice. Point to exact lines that need rewriting.

---

## Pass 2: Retention Curve Analysis (Quality Gate 3 + advisories)

### Check 1 — Loop Openers (Quality Gate 3)

Find all loop openers in the script. Transition phrases between scenes that reset the viewer's attention hourglass:
- Curiosity bridges: "But here is what nobody talks about", "And this is where it gets interesting"
- Stakes escalation: "This is where most people go wrong", "Here is the part that changes everything"
- Re-engagement: "Now here is the real question", "But wait — there is more to this"

Required minimum = `max(2, floor(estimated_duration_minutes / 1.5))`

**QG-3 passes** if found ≥ required.

| #   | Scene    | Position   | Loop Opener Phrase                       |
| --- | -------- | ---------- | ---------------------------------------- |
| 1   | Scene 02 | Opening    | "But that is just the beginning."        |
| 2   | Scene 04 | Transition | "Here is where it gets interesting."     |

Result: X found, Y required — **PASS / FAIL**

### Check 2 — Boxer's Rhythm (Advisory)

Audit 3 random body paragraphs. Flag if any 5-sentence stretch has all sentences within ±3 words of each other in length (monotonous rhythm). Advisory — does not block the gate.

### Check 3 — Hedging Language (Advisory)

Search for: "if you", "might", "maybe", "could be", "probably", "perhaps", "you may", "might want to". List occurrences with scene + line. Suggest embedded-truth replacements (e.g., "you might want to try" → "try this"). Advisory — does not block, but high count (5+) indicates weak writing.

---

## Pass 3: TTS Readability Check (Advisory)

Advisory — flags potential TTS issues but does not block the gate.

### Check 1 — Scene Length Compliance

For each scene, calculate `target_words = scene_duration_seconds × 2.5`. Valid range = target ±10%.

| Scene    | Words | Target | Range | Status              |
| -------- | ----- | ------ | ----- | ------------------- |
| Scene 01 | N     | N      | N-N   | OK / OVER / UNDER   |

### Check 2 — Sentence Length

Flag any sentence exceeding 25 words. Long sentences are harder for TTS to deliver naturally.

### Check 3 — Acronym Safety

Known-safe acronyms (do NOT flag): AI, API, UI, CLI, SDK, PDF, HTML, CSS, JS, TS, URL, HTTP, SQL, LLM, GPU, CPU, RAM, SSD, IDE, SSH, DNS, JWT, XSS, CORS, REST, CRUD, YAML, JSON, XML, CSV, TLS, SSL, AWS, GCP.

Flag any other acronym not already spaced or hyphenated for TTS. Suggest spacing (e.g., "GRPC" → "G R P C" or "gee-RPC").

### Check 4 — Symbol Check

Scan for: `{ } < > [ ] $ % @ #` (break tags exempt). These render as silence or gibberish in TTS.

### Check 5 — 800 Character Estimate

If `scene word_count × 5.5 > 800`, flag as likely too long after TTS optimization expands abbreviations.

---

## Pass 4: Story Arc Completeness (Quality Gate 2)

Score four arc elements on a 1-10 scale:

### Arc Element 1 — Hook to Value Delivery Timing

First concrete payoff must arrive before:
- 4 seconds for short-form (< 60s)
- 45 seconds for medium (60s-3min)
- 90 seconds for long-form (3min+)

| Score | Criteria                              |
| ----- | ------------------------------------- |
| 9-10  | On time, high-value hit               |
| 7-8   | Slightly delayed but substantive      |
| 5-6   | Delivers but value is vague           |
| 3-4   | Value hit missing or too late         |
| 1-2   | No clear value hit                    |

### Arc Element 2 — Benefit-Led Feature Scenes

Do scene-opening sentences mention viewer problem or gain BEFORE technical explanation?

| Score | Criteria                          |
| ----- | --------------------------------- |
| 9-10  | Every scene benefit-led           |
| 7-8   | ≥ 75% of scenes benefit-led       |
| 5-6   | Mixed                             |
| 3-4   | Mostly feature-led                |
| 1-2   | All feature-led (information dump)|

### Arc Element 3 — CTA Strength

Must pass all three: debate-sparking question + specific video reference + under 15 words.

| Score | Criteria                          |
| ----- | --------------------------------- |
| 9-10  | All three criteria met            |
| 7-8   | Two criteria met                  |
| 5-6   | One criterion met                 |
| 3-4   | Generic CTA                       |
| 1-2   | No CTA or pure channel plug       |

### Arc Element 4 — Narrative Cohesion

Logical scene flow + primary open loop resolved + clear beginning/middle/end structure.

| Score | Criteria                                  |
| ----- | ----------------------------------------- |
| 9-10  | Tightly structured, clear arc             |
| 7-8   | Mostly coherent with minor gaps           |
| 5-6   | Some structural jumps                     |
| 3-4   | Scenes feel disconnected                  |
| 1-2   | No discernible arc                        |

### Arc Element 5 — Experience Signal (Advisory Bonus)

Does the script contain at least 1 "scar" — a first-person friction point, failure mode, undocumented edge case, or time trap that earns trust because it could not have been generated by AI?

| Score | Criteria                                                                    |
| ----- | --------------------------------------------------------------------------- |
| 1     | Present: specific failure mode / time wasted / undocumented edge case       |
| 0     | Absent: purely informational content with no earned insight signal          |

Advisory — adds 0.5 bonus points to story arc score when present.

**Scar patterns**: "I wasted X hours before...", "The docs don't mention...", "This breaks silently when...", "After running this on N projects I noticed...", "Here's what nobody writes about..."

**Commodity Test**: If the entire script could be reproduced by prompting ChatGPT with the video title, flag it as a credibility risk — not a gate failure, but a note for the writer.

### Scoring Formula

```
story_arc_score = round((Arc1 + Arc2 + Arc3 + Arc4) / 4, 1)
experience_bonus = 0.5 if Arc5 == 1 else 0
story_arc_score = min(10, story_arc_score + experience_bonus)
```

**Quality Gate 2**: Story Arc Score MUST be ≥ 7.0 to proceed.

### Output Format

| Element                | Score        | Notes                                                |
| ---------------------- | ------------ | ---------------------------------------------------- |
| Hook to Value Timing   | X/10         | [observation]                                        |
| Benefit-Led Scenes     | X/10         | [which scenes are feature-led]                       |
| CTA Strength           | X/10         | [debate question present?]                           |
| Narrative Cohesion     | X/10         | [open loop resolved?]                                |
| Experience Signal      | 0 or +0.5    | [scar found / not found — quote if found]            |
| **STORY ARC SCORE**    | **X.X/10**   | **PASS / FAIL (threshold: 7.0)**                     |

**On FAIL**: Provide 2-3 specific structural rewrites pointing to exact scenes that need changes.

---

## Pass 5: Voice & AI-Phrasing Detection (Quality Gate 4)

Combines two scans into one gate:

### A. Generic AI-phrasing (from `.claude/references/faceless-tech-scriptwriting-playbook.md` §11)

#### Critical Phrases (BLOCKING — zero tolerance)

Any exact or near-match of these causes QG-4 FAIL:
- "But here's the thing" / "But here is the thing" / "But here's what" / "But here's where"
- "Most developers don't know" / "Most developers missed" / "Most developers are sleeping on" / "Most people don't realize"
- "No more [X]" (as a benefits bullet pattern)
- "[X] changes everything" / "This changes everything"
- "If this helped, subscribe" / "If this changed how you think" (generic CTA pattern)

#### High Phrases (BLOCKING — zero tolerance)

- "Let me show you" / "Let me walk you through"
- "Here's the thing" (standalone)
- "Game changer" / "game-changing"
- "The future of [X]"
- "Under the hood"

#### Medium Phrases (ADVISORY — max 1 per video)

- "It's not just X — it's Y"
- "Nobody talks about"
- "Where it gets interesting"
- "Think about it" / "Think about that"
- "Paradigm shift"
- "Imagine [generic scenario]"

### B. Channel-specific voice (from `.claude/references/brand-voice.md`)

Brand-voice.md adds a channel-specific layer ON TOP of the generic playbook. ALL of these are BLOCKING for QG-4:

#### B.1 — Banned word lists (§"The 50-Word Banned List")

Scan for any occurrence of these (case-insensitive, word boundaries):

**Generic AI phrases** (always banned): `delve`, `tapestry`, `harness`, `unlock`, `leverage`, `paradigm`, `seamless`, `cutting-edge`, `groundbreaking`, `transformative`, `revolutionize`, `in today's fast-paced world`, `as we navigate`, `it's worth noting`, `needless to say`, `without further ado`, `in conclusion`, `in essence`, `having said that`, `first and foremost`, `last but not least`, `to summarize`, `let's dive in`, `let's explore`, `furthermore`, `moreover`, `nevertheless`, `undoubtedly`, `it goes without saying`

**Hype phrases** (banned for this channel): `changed everything`, `you won't believe`, `the future is here`, `absolutely incredible`, `mind-blowing`, `next level`, `the game has changed`, `smash that like button`, `don't forget to subscribe`, `this is huge`, `the most powerful`, `unlike anything before`, `the only tool you need`, `full potential`, `unlock your potential`

**Over-hedging phrases** (banned — narrator is direct): `some might argue`, `it could be said`, `in many ways`, `to some extent`, `this may or may not`, `generally speaking`, `for the most part`, `one could say`, `arguably`

#### B.2 — Hard rules (§"What Claude Must NOT Do When Writing Scripts" — all 10)

Each script must pass ALL of these. Each violation is a separate QG-4 failure:

1. Does NOT open with the channel name or a greeting (cuts straight to the first scene)
2. Does NOT summarise what's coming at the start (no "In this video, I'll show you…")
3. Does NOT add a motivational frame ("This will help you become a better developer" → BANNED)
4. Does NOT manufacture stakes ("If you're not using this, you're already behind" → BANNED)
5. Does NOT use em dashes (—) in narration (use period or comma — em dashes sound wrong when spoken)
6. Does NOT use bullet-pointed narration (scripts are prose)
7. Does NOT attribute emotions to the viewer ("You've probably felt frustrated when…" → BANNED)
8. Does NOT end on a vague promise ("The future of development is here" → BANNED)
9. Does NOT imply original research that didn't happen ("I tested X for 30 days", "In my experiments", "My tests show" → BANNED unless explicitly true and brief)
10. Always attributes third-party claims to a source (never presents an announcement / benchmark as personal validation)

#### B.3 — Hook type compliance (§"Hook Rules")

Scene 01 hook must match ONE of the 4 acceptable types:
- **Type A — The Honest Result**: "I ran [X] for [time]. Here's what actually happened."
- **Type B — The Counterintuitive Observation**: "[Common assumption]. [One sentence that breaks it]."
- **Type C — The Specific Number**: "[Precise number] [thing]. [Why that matters in one sentence]."
- **Type D — The Shared Frustration**: "[Specific problem stated as a fact, not a question]."

If the hook doesn't fit any of these (e.g. opens with "Have you ever wondered…" or "In this video I'm going to show you…" or "[Tool name] just changed everything") — QG-4 FAIL.

#### B.4 — First-person singular check

Scan for "we" used as the narrator's voice (not in quoted speech / not when referring to the audience as "you and I together"). The channel uses "I", never "we". Each "we" used as the narrator is one QG-4 failure.

#### B.5 — Contractions check

Scan for expanded contractions (it is, do not, you are, I have) where the contraction would be natural. The channel uses contractions always. Flag each occurrence — collectively if there are 3+, that's a QG-4 failure.

### Scoring

```
banned_count = count of (Critical + High playbook phrases) + (B.1 + B.2 + B.3 + B.4 + B.5 hits)
QG-4 PASS: banned_count == 0
QG-4 FAIL: banned_count > 0
```

### Output Format

| #   | Source                          | Hit                          | Severity | Scene    | Fix                                                  |
| --- | ------------------------------- | ---------------------------- | -------- | -------- | ---------------------------------------------------- |
| 1   | playbook §11 Critical           | "But here's the thing"       | Critical | Scene 03 | "One detail changes this." / "Look at what happens when..." |
| 2   | brand-voice §B.1 generic        | "delve into"                 | Critical | Scene 02 | Cut. State the action directly.                      |
| 3   | brand-voice §B.2 hard rule #5   | em dash in narration         | Critical | Scene 04 | Replace `—` with period or comma                      |
| 4   | brand-voice §B.3 hook type      | hook is "Have you ever…"     | Critical | Scene 01 | Rewrite as Type A/B/C/D from brand-voice.md          |
| 5   | brand-voice §B.4 first-person   | "we" as narrator             | Critical | Scene 02 | Rewrite as "I"                                       |

Medium phrases (playbook): list as advisories (not blocking), flag if count > 1 per video.

Result: X blocking hits — **PASS / FAIL**

**On FAIL**: List each hit with scene location and a concrete fix. Writer must address ALL blocking hits before re-running QG-4.

</process>

<output>

## Gate Summary

Produce the final gate summary table:

| Gate | Check                  | Result      | Score/Status                          |
| ---- | ---------------------- | ----------- | ------------------------------------- |
| QG-1 | Hook Strength          | PASS / FAIL | X.X/10 (threshold: 7.0)               |
| QG-2 | Story Arc              | PASS / FAIL | X.X/10 (threshold: 7.0)               |
| QG-3 | Loop Opener Frequency  | PASS / FAIL | X found, Y required                   |
| QG-4 | AI-Phrasing Detection  | PASS / FAIL | X banned phrases found                |

**Overall Verdict**: PASS or FAIL

### On PASS

All four quality gates cleared. The script is approved for TTS optimization.

Next step: Run `/diy-yt-creator:phase2a-tts-script <slug>`

### On FAIL

Numbered list of specific actionable issues per failed gate. Each issue must include:
- Which gate failed
- What specifically is wrong (quote the problematic text)
- A concrete replacement or structural fix

After revisions, re-run: `/diy-yt-creator:phase2-5-critique <slug>`

**STOP** — do NOT proceed to Phase 2a under any circumstance until all four gates are cleared.

## Save Report

Save the full critique report to: `videos/<slug>/scripts/critique-report.md`

The report must include all five passes with their output tables, the gate summary, and the overall verdict.

### Update Phase Status

Update `videos/<slug>/phase-status.md`:
- If all gates **PASS**: set the `2.5 - Critique` row to `done (X.X/10 hook, X.X/10 arc) <YYYY-MM-DD>`.
- If any gate **FAILS**: set the `2.5 - Critique` row to `blocked (<failed gate names>) <YYYY-MM-DD>`.

</output>

### Retention Checklist (Phase 2.5 — BLOCKING)

The following issues block script approval. Each must receive a PASS before Phase 2a proceeds:

- [ ] Does every scene (except final CTA) end with an open loop or chapter hook?
- [ ] Are all chapter/scene names curiosity gaps rather than topic labels?
- [ ] Is the WPM in range (150-165 WPM per segment)?
- [ ] Are high-impact reveal words preceded by `[PAUSE]` in the script?
