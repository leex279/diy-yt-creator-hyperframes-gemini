# Engagement Audit Checklist

Run this checklist after Phase 2 (script written) and before Phase 2.5 (formal critique). It catches engagement failures that the existing critique gates don't measure: scroll-stop force, sentence pull, hook alignment, dopamine pacing.

**Output format**: a per-check PASS / FAIL with line citations and a one-sentence rewrite suggestion for each FAIL. Do NOT modify the script — return the report only.

---

## Section 1 — Hook (0.0s to 4.0s)

### H1. Triple-Threat Alignment

The first scene must annotate visual + text + spoken hooks (or — if the script doesn't yet — note that the alignment must be designed before composition build).

- [ ] Spoken hook fits inside 3.5s (≤9 words for a single-sentence hook, ≤15 for a chained hook ending mid-sentence at 3.5s)
- [ ] `[VISUAL: ...]` annotation present in Scene 01 OR documented in the Phase 1 plan's `hook_variants` block
- [ ] `[TEXT: ...]` annotation present, text ≤7 words, designed for ≥44px on shorts canvas
- [ ] All three components point at the same topic and angle (no mismatch)

**Failure example**: `[TEXT: Skills system]` paired with spoken `"If you've ever wondered how Claude really thinks..."` — text says "skills", spoken says "thinking", visual would have to pick one. Pick "skills" or "thinking", align all three.

### H2. Violent Contrast

The hook traverses 200 units (`+100 → -100`), not 100 (`0 → -100`).

- [ ] First sentence (or first clause) anchors the common belief in the viewer's voice ("If you've been...", "You probably think...", "Most strategy guides say...")
- [ ] Second sentence (or pivot clause) snaps to the contrarian truth with no hedge
- [ ] The +100 is a real belief the target audience holds (not a strawman)
- [ ] The -100 is fully contrarian (not "kind of less true")

**Failure example**: `"Tags might be less important than they used to be."` — that's `+50 → -50`, only 100 units of distance. Replace with `"You've been stuffing tags hoping for views. They do almost nothing now."` — full 200.

### H3. Hook completes inside 4 seconds

- [ ] By 4.0s, the viewer knows the topic AND the angle
- [ ] No "in this video", no "today we're talking about", no greeting
- [ ] Active voice, second-person specific where appropriate

### H4. Pattern selection is documented

- [ ] Phase 1 plan's `hook_variants` block specifies one of Pattern A/B/C/D/E from `triple-threat-hook.md`
- [ ] Pattern matches topic type (news → C, utility → B, system reveal → A or E, contrarian thesis → A)

---

## Section 2 — Sentence Pull (4s onward)

### S1. Question-chain map exists

- [ ] The plan or script has 5-8 explicit questions for each scene (the `Q1 / Q2 / Q3` chain from `one-question-loop.md`)
- [ ] OR the prose itself flows as Q-driven (verifiable by Eyes-Closed Test below)

### S2. Eyes-Closed Test

Read the first 60 seconds aloud, eyes closed. After each sentence, a question must form naturally in the listener's head, and the next sentence must answer it.

- [ ] Sentences 1-15 (the first 60s) all pull the next sentence in
- [ ] No more than 2 consecutive answer-only sentences before a new question is raised
- [ ] No tangent that doesn't return within 2 sentences

**Failure example**: 
```
"Skills auto-load when relevant. (Q: how detect?) 
They live in .claude/skills. (answer ≠ Q — tangent) 
Each has a SKILL.md. (still tangent) 
Some have references. (still tangent) 
Anyway, the auto-load uses keyword matching. (return — but 3 sentences late)"
```
Fix: tighten to 2 sentences max between question and return, or restructure the chain.

### S3. Two Dopamine Hits before 60s

- [ ] Hit #1 (specific actionable / memorable nugget) lands between 10-25s
- [ ] Hit #2 lands between 40-55s
- [ ] Each nugget is self-contained — extractable as a single sentence the viewer could screenshot

**Failure example**: A 60s script that's all setup with no payoff until second 50. Fix: pull one tactical takeaway into the 15-20s window.

---

## Section 3 — Visual Pacing Cross-Check

This section overlaps with `.claude/rules/visual-pacing-5s.md` but specifically audits the engagement layer of pacing.

### V1. No static frames > 5s

- [ ] Inside the hook (0-4s), at least 2 visual beats (entrance, scale pulse on title, marker sweep, etc.)
- [ ] Inside the first 30s, at least 6 visual beats (one every 5s)
- [ ] Visual beats deliver new content (per `visual-pacing-5s.md`), not pure decoration

### V2. The Mute-Test

Play the first 10s muted. Can a viewer determine the topic from visual + text alone?

- [ ] Title text on screen at 0.5s, large enough to read at phone scale (~16px after 0.36× scaling)
- [ ] Visual shows the subject (logo, screenshot, counter, character) — not a generic gradient
- [ ] By 5s, secondary visual (proof point, second card, a stat) has entered

**Failure example**: A 10s hook with a single gradient background and animated typography. Muted, the viewer reads "[topic]" for 10 seconds with no reinforcement → bounce.

---

## Section 4 — Density & Compression

### D1. Speed-to-Value ≤ 4s

- [ ] First concrete payoff (a stat, a feature name, a tool name, a specific outcome) by 4s
- [ ] No throat-clearing ("Hi guys", "In this video", "Today we're going to discuss")

### D2. Sentence length variance

- [ ] No 3+ consecutive sentences within ±3 words of each other (Boxer's Rhythm)
- [ ] Average sentence length 12-18 words for news-explainer; 6-10 for tutorial
- [ ] At least one short punch (≤7 words) per scene as a rhythm reset

### D3. Substance layer

- [ ] At least one **contrarian take or non-obvious insight** in the body — not just facts
- [ ] At least one piece of **evidence** for that take (case study, A vs B, metaphor, specific stat)

**Failure example**: A script that lists 5 features without taking a position on which one matters most. Fix: add a contrarian rank ("the third one is the only one that actually changes your workflow") with evidence.

---

## Section 5 — Cross-Compatibility With Existing Pipeline

These checks ensure this skill's output flows cleanly into Phase 2.5 and Phase 2a.

### X1. Brand-voice compliance

- [ ] No banned phrases from `.claude/references/brand-voice-news-explainer.md` (or the active profile)
- [ ] No em dashes in narration (Phase 2.5 hard rule #5 for news-explainer)
- [ ] First-person rule respected per profile (`I` only for tutorial; `I` + audience-`we` allowed for news-explainer)
- [ ] No "Most developers don't" frame, no "It's not just X — it's Y", no "But here's the thing" (banned across all profiles)

### X2. Phase 2.5 gate compatibility

If this audit's recommendations are applied, the script should still pass:

- [ ] QG-1 Hook Score ≥ 7.0 (Curiosity Gap + Stakes + Specificity weighted)
- [ ] QG-2a Story Arc avg ≥ 7.0
- [ ] QG-2b CTA Strength ≥ 7.0 (rhetorical Q + comments-ask + subscribe-ask)
- [ ] QG-5 connectors ≥ 3 in body, ≥ 1 direct-address, full CTA closer (news-explainer only)

If this skill's audit recommends changes that would break Phase 2.5, flag the conflict to the user. The user decides which gate to satisfy. Defer to Phase 2.5 by default — it's the blocking authority.

---

## Section 6 — Tone Spot-Check

### T1. The "Coffee" Test

Read each sentence aloud. Does it sound like something the narrator would say to a peer over coffee?

- [ ] No "transformative", no "revolutionize", no "leverage", no "harness" (Universal Bans from `brand-voice-news-explainer.md`)
- [ ] No "absolutely incredible", no "you won't believe", no "this is huge" (hype phrases)
- [ ] Contractions used naturally (`it's`, `don't`, `you're` — not `it is`, `do not`, `you are`)

### T2. Restraint over hype

- [ ] If a stat is included, it has a comparison baseline ("$30B run-rate, up from $9B last year") rather than a hype amplifier ("a STAGGERING $30B")
- [ ] The hook earns the lean-in via specificity, not via superlatives

---

## Final Audit Output Template

Use this format when reporting back to the user / Phase 2 / orchestrator:

```markdown
# Engagement Audit — videos/<slug>

**Audited**: <YYYY-MM-DD>
**Script**: videos/<slug>/scripts/full-script.md
**Mode**: audit (advisory — does not block pipeline)

## Summary

| Section | Pass | Fail | Critical |
|---|---|---|---|
| H — Hook | X/4 | Y | Z |
| S — Sentence Pull | X/3 | Y | Z |
| V — Visual Pacing Cross-Check | X/2 | Y | Z |
| D — Density & Compression | X/3 | Y | Z |
| X — Pipeline Compatibility | X/2 | Y | Z |
| T — Tone | X/2 | Y | Z |
| **TOTAL** | **X/16** | **Y** | **Z** |

## Critical fails (must fix before ship)

### H2 (Violent Contrast) — FAIL
- **Line**: Scene 01, sentence 1
- **Current**: "Tags might be less important than they used to be."
- **Issue**: Hedged contrarian. Travels ~100 units, not 200.
- **Suggested rewrite**: "You've been stuffing tags hoping for views. They do almost nothing now. YouTube reads your transcript instead."

[... one block per critical fail ...]

## Advisory fails (recommend fixing)

[... per-check entries ...]

## Passes worth noting

[Optional: callouts where the script does something especially well — useful for the self-improvement loop]

## Next step

If critical fails > 0: address them, then re-run `/diy-yt-creator:phase2-5-critique`.
If only advisory fails: proceed to Phase 2.5 — the gate may still pass.
```

## How this audit is rated against ship results

When the video ships, log:
- Which audit sections had critical fails at ship time
- Which audit sections had advisory fails at ship time
- The retention curve at 3s, 10s, 30s

Over time, calibrate:
- Audit sections that consistently correlate with low retention → tighten the thresholds
- Audit sections that fire false-positive (FAIL but video still performs) → relax with documented exception
