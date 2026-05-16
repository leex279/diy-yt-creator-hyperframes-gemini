# Phase 2.5 — Critique Report: `claude-code-goal-command`

**Run date**: 2026-05-12
**Voice profile**: `news-explainer`
**Script**: `videos/claude-code-goal-command/scripts/full-script.md`
**Total words**: 351 (incl. headers & receipts) / ~273 narration-only
**Estimated duration**: ~2m 20s (140 sec @ 2.5 wps narration) — plan target 120s
**Mid-video word target (58%)**: ~158 narration words

---

## Pass 1 — Hook Strength (QG-1)

Hook = Scene 1: *"Wait. There's a new slash command in Claude Code — and Haiku judges Sonnet now. It's called slash goal. And it just made typing 'keep going' obsolete."*

| Dimension       | Score   | Notes                                                                                              |
| --------------- | ------- | -------------------------------------------------------------------------------------------------- |
| Curiosity Gap   | 9/10    | "Haiku judges Sonnet" is a sharp, single-sentence architectural reveal. Strong gap.                |
| Stakes Clarity  | 6/10    | Implied ("keep going obsolete"); not quantified.                                                   |
| Specificity     | 8/10    | Names slash goal, Haiku, Sonnet within first 2 sentences.                                          |
| Stun Gun        | 0/2     | "Wait." is a soft-stun curiosity opener, NOT But/However/Yet/Although. By spec → 0.                |
| Value Alignment | 0.5/0.5 | Feature ("slash command" → "slash goal") named directly in sentences 1-2.                          |
| Promise         | 0/1     | No explicit "in the next X minutes you will…" promise.                                             |

```
base = (9*0.4) + (6*0.4) + (8*0.2) = 3.6 + 2.4 + 1.6 = 7.6
stun_bonus = 0; alignment_bonus = 0.5; promise = 0
narrative_flow_bonus = 0  (hook uses coordinator "and"; no explanatory because/so/here's why inside the hook)
hook_score = 7.6 + 0 + 0.5 + 0 + 0 = 8.1
```

**HOOK SCORE: 8.1/10 — PASS (threshold: 7.0)**

Tone match: curious / discovery (user constraint). "Wait." opener and "Haiku judges Sonnet" reveal are pure discovery framing — no pain/shame.

---

## Pass 2 — Retention Curve

### Check 1 — Loop Openers (QG-3)

Estimated duration ≈ 2.34 min. Required ≥ `max(2, floor(2.34/1.5))` = **2**.

| # | Scene | Position | Phrase |
|---|---|---|---|
| 1 | Scene 2 | Opening | "Because here's how it works." |
| 2 | Scene 4 | Opening | "And here's why it's not just another prompt." |

Strong loop openers found: **2**. (Scene 3's "So here's what it looks like in your terminal" is a procedural transition, not a curiosity bridge; Scene 5's "So — next time…" is the CTA opener.)

**Result: 2 found, 2 required — PASS**

### Check 2 — Boxer's Rhythm (Advisory)

Sentence lengths vary well in each body scene. No monotonous 5-sentence stretches detected. **PASS (advisory)**.

### Check 3 — Hedging Language (Advisory)

Zero hedging hits ("might", "maybe", "probably", "perhaps"). Clean. **PASS (advisory)**.

---

## Pass 3 — TTS Readability (Advisory)

### Scene length compliance (target = duration × 2.5 wps)

| Scene | Words | Target (plan duration) | Status |
|---|---|---|---|
| S1 | ~31 | 30 (12s × 2.5) | OK |
| S2 | ~52 | 50 (20s × 2.5) | OK |
| S3 | ~86 | 82.5 (33s × 2.5) | OK |
| S4 | ~57 | 62.5 (25s × 2.5) | OK |
| S5 | ~52 | 75 (30s × 2.5) | UNDER — narration light vs plan, but ≥ Dynamous outro + URL hold |

### Sentence length

No sentence > 25 words detected.

### Acronym safety

"AI" appears in Dynamous outro — known-safe. No other unsafe acronyms.

### Symbol check

`/` slashes will be normalized by Phase 2a ("slash goal" already spelled out — good). Em dashes `—` present but Phase 2a/TTS will strip; see QG-4 finding below.

### 800-char estimate

S3 word count × 5.5 ≈ 473 chars — well under 800.

**Pass 3: Advisory PASS (no blocking issues)**

---

## Pass 4 — Story Arc (QG-2a + QG-2b)

| Element                    | Score      | Notes |
|----------------------------|------------|-------|
| Arc 1 — Hook to Value      | 8/10       | First payoff (mechanism) lands at ~12s; well within the 45s medium-form window. |
| Arc 2 — Benefit-Led        | 7/10       | S2 opens with mechanism ("Because here's how it works"); S3 with demo lead-in; S4 explicitly benefit-led ("If you've ever typed 'keep going' eight times…"). Mostly OK. |
| Arc 3 — CTA Strength       | **3/10**   | **No rhetorical/debate question. No comments-ask. No subscribe-ask.** Dynamous pointer ("If you want to learn more about AI, check out the dynamous.ai community") is the entire closer. Fails all 3 news-explainer CTA criteria. |
| Arc 4 — Narrative Cohesion | 8/10       | Hook → mechanism → demo → differentiation → CTA. Primary open loop ("how Haiku judging Sonnet works") resolves in S3. |
| Arc 5 — Experience Signal  | 0          | No scar / no first-person friction point. Acceptable for news-explainer (third-party reporting). |

```
qg2a_score = (8 + 7 + 8) / 3 = 7.67  → round to 7.7
experience_bonus = 0
QG-2a final = 7.7/10
qg2b_score = 3/10
```

**QG-2a (Arc1+Arc2+Arc4): 7.7/10 — PASS (threshold: 7.0)**
**QG-2b (CTA standalone): 3.0/10 — FAIL (threshold: 7.0)**

### On QG-2b FAIL — proposed fix

Current closer (S5): *"State the finish line once. The docs are at claude dot com slash docs slash en slash goal. Shipped in version 2.1.139. If you want to learn more about AI, check out the dynamous.ai community."*

Replacement satisfying news-explainer CTA template (`brand-voice-news-explainer.md` §CTA Pattern):

> "State the finish line once. The docs are at claude dot com slash docs slash en slash goal. Shipped in version 2.1.139. So — would you trust a second model to judge your work, or are you sticking with 'keep going'? Let me know in the comments. And subscribe for more Claude Code news. If you want to learn more about AI, check out the dynamous.ai community."

This adds: (1) rhetorical question ending with `?`, (2) comments-ask, (3) subscribe-ask, while preserving the locked Dynamous outro line.

**NOTE on tension**: the locked Dynamous outro rule (`feedback_dynamous_short_outro` memory) and the news-explainer mandatory engagement CTA both exist. The replacement above stacks them — engagement CTA first, Dynamous pointer last — which is the cleanest reconciliation. If the user prefers Dynamous-only closer, the voice_profile should be downgraded to `tutorial` (which skips QG-5/CTA enforcement) — that's a workflow decision, not something this gate can soften.

---

## Pass 5 — Voice & AI-Phrasing (QG-4)

### A. Generic AI-phrasing (playbook §11)

- "But here's the thing" — **absent** ✓
- "Most developers don't know" — **absent** ✓
- "No more [X]" pattern — **absent** ✓
- "[X] changes everything" — **absent** ✓
- "Let me show you" / "walk you through" — **absent** ✓
- "Game changer" — **absent** ✓
- "Under the hood" — **absent** ✓
- "The future of [X]" — **absent** ✓

### B. Brand-voice news-explainer §B.1–B.5

| Check | Result |
|---|---|
| B.1 Generic banned words (delve, leverage, unlock, supercharge, paradigm, …) | **None** ✓ |
| B.1 Hype phrases (changed everything, mind-blowing, …) | **None** ✓ |
| B.1 Over-hedging | **None** ✓ |
| B.2 Hard rule #1 — no greeting open | Pass ✓ |
| B.2 Hard rule #2 — no "in this video I'll show" | Pass ✓ |
| B.2 Hard rule #3 — no motivational frame | Pass ✓ |
| B.2 Hard rule #4 — no manufactured stakes | Pass ✓ |
| **B.2 Hard rule #5 — no em dashes in narration** | **FAIL — 5+ em dashes** |
| B.2 Hard rule #6 — no bullet-pointed narration | Pass ✓ |
| B.2 Hard rule #7 — no attributing emotions to viewer | Pass ✓ |
| B.2 Hard rule #8 — no vague-promise closer | Pass ✓ (no "future of dev is here" type closer) |
| B.2 Hard rule #9 — no implied original research | Pass ✓ |
| B.2 Hard rule #10 — third-party claims attributed | Pass ✓ (docs cited; behavior described in third person) |
| B.3 Hook type compliance | Type B — Counterintuitive ✓ |
| B.4 First-person `we` as narrator | **None** ✓ |
| B.5 Expanded contractions | **None** ✓ — script uses "it's", "there's", "you're", "doesn't" consistently |

### Em-dash count (narration lines only — Scene 1 header excluded)

| # | Line | Quote (em dash shown as —) |
|---|---|---|
| 1 | 5 | "a new slash command in Claude Code **—** and Haiku judges Sonnet now" |
| 2 | 12 | "a small fast model **—** Haiku by default **—** checks the transcript" (×2 — pair) |
| 3 | 18 | "a condition **—** something like…" |
| 4 | 18 | "returns: 'no **—** auth login still broken'" |
| 5 | 18 | "'Yes **—** achieved.'" |
| 6 | 18 | "Wait **—** Haiku just told Sonnet…" |
| 7 | 24 | "Claude answers **—** control returns…" |
| 8 | 24 | "a fresh model **—** not the one doing the work **—** judges…" (×2 pair) |
| 9 | 30 | "So **—** next time you're about to type 'keep going'…" |

**Total em-dash violations in narration: 11**

### C. Medium-tier advisory (playbook §11)

- "It's not just X — it's Y" pattern in S4: *"And here's why it's **not just** another prompt."* — Medium phrase, count = 1 (limit 1/video). Advisory only — does NOT block.

### Scoring

```
banned_count = 11 (all em-dash violations against B.2 hard rule #5)
```

**QG-4: 11 blocking hits — FAIL**

### On QG-4 FAIL — proposed fixes

Replace every em dash in narration with a period or comma. Examples:

- Line 5: "Wait. There's a new slash command in Claude Code, and Haiku judges Sonnet now."
- Line 12: "Then a small fast model, Haiku by default, checks the transcript and returns yes or no with a short reason."
- Line 18: replace each `—` with `.` or `,` (e.g., "Haiku reads the transcript and returns: 'no, auth login still broken.'")
- Line 30: "So next time you're about to type 'keep going' for the eighth time, type slash goal instead."

Phase 2a TTS-script normalization commonly strips em dashes, but the brand-voice spec treats them as a script-level fail; the script source must be clean before progressing.

---

## Pass 6 — Narrative Flow & Direct Address (QG-5, news-explainer profile)

### Check 1 — Connector Density (body = S2, S3, S4)

| Scene | Connectors found | Unique types |
|---|---|---|
| S2 | "Because" (sentence-initial), "and" | 2 |
| S3 | "So" (sentence-initial), "then", "and" | 2 |
| S4 | "And" (sentence-initial), "why" | 2 |

Total: ≥ 6 connector instances across body, ≥ 3 unique types (because, so, and, why). **Score: 9/10**

**QG-5a: PASS (threshold ≥ 6)**

### Check 2 — Direct Address (body, not hook/CTA)

S4: *"If you've ever typed 'keep going' eight times in a row, this replaces all eight."* — matches canonical pattern `"If you ['ve verb-ed] X, [implication]"`.

**QG-5b: 2/2 PASS**

### Check 3 — Engagement CTA Closer

Final scene S5: *"So — next time you're about to type 'keep going' for the eighth time, type slash goal instead. State the finish line once. The docs are at claude dot com slash docs slash en slash goal. Shipped in version 2.1.139. If you want to learn more about AI, check out the dynamous.ai community."*

| Component | Found? |
|---|---|
| Rhetorical/debate question ending in `?` | **NO** |
| Comments-ask ("comments", "let me know", "tell me below") | **NO** |
| Subscribe-ask ("subscribe", "follow for more", "for more X news") | **NO** |

**Score: 0/2 — FAIL**

**QG-5c: FAIL**

```
QG-5 overall: a=PASS, b=PASS, c=FAIL → QG-5 FAIL
```

### Fix (mirrors QG-2b fix above)

Add an engagement closer before the Dynamous pointer line (see proposed S5 rewrite under QG-2b).

---

## Pass 7 — JCRR Line Audit (ADVISORY)

Body scenes (S2, S3, S4 — excluding hook S1 and CTA S5):

| Scene | Sentences | J | C | R-reason | R-receipt | F | Filler % |
|---|---|---|---|---|---|---|---|
| S2 | 6 | 0 | 5 | 1 | 0 | 0 | 0% |
| S3 | 11 | 1 | 7 | 2 | 0 | 1 | 9.1% |
| S4 | 6 | 0 | 4 | 2 | 0 | 0 | 0% |
| **Total** | **23** | **1** | **16** | **5** | **0** | **1** | **4.3%** |

Filler hit (S3): *"That's the loop."* — debatable; reads as thought-narration kicker rather than pure filler. Lenient classification keeps it advisory.

```
overall_filler_pct = 4.3%
overall_jcrr_pct  = 95.7%
```

**Methodology rating: STRONG (≥ 90%)** — every body sentence carries information; no filler runs > 2.

**Pass 7: ADVISORY — does not block. Rating recorded for future calibration.**

---

## Gate Summary

| Gate  | Check                              | Result | Score / Status                                  |
|-------|------------------------------------|--------|------------------------------------------------|
| QG-1  | Hook Strength                      | PASS   | 8.1/10                                          |
| QG-2a | Story Arc (Arc1+Arc2+Arc4 avg)     | PASS   | 7.7/10                                          |
| QG-2b | CTA Strength (Arc3 standalone)     | **FAIL** | 3.0/10 (no debate ?, no comments-ask, no subscribe-ask) |
| QG-3  | Loop Opener Frequency              | PASS   | 2 found / 2 required                            |
| QG-4  | AI-Phrasing Detection              | **FAIL** | 11 em-dash violations (brand-voice §B.2 hard rule #5) |
| QG-5  | Narrative Flow & Direct Address    | **FAIL** | a=PASS, b=PASS, **c=FAIL** (no engagement CTA closer) |
| QG-7  | JCRR Methodology (advisory)        | ADVISORY | 95.7% JCRR (STRONG)                            |

**Overall Verdict: FAIL — QG-2b + QG-4 + QG-5 blocking**

---

## On FAIL — Actionable Fix List (in order of effort)

### Fix #1 — Strip em dashes from narration (QG-4)

Replace all 11 narration em dashes with period or comma. Examples:

- S1 L5: `Claude Code — and Haiku` → `Claude Code, and Haiku`
- S2 L12: `model — Haiku by default — checks` → `model, Haiku by default, checks`
- S3 L18: every `—` → `.` or `,` (5 instances)
- S4 L24: `answers — control returns` → `answers, control returns`; `model — not the one — judges` → `model, not the one doing the work, judges`
- S5 L30: `So — next time` → `So next time` OR `So, next time`

### Fix #2 — Add engagement CTA closer (QG-2b + QG-5c)

Insert before the Dynamous outro line in S5:

> "So, would you trust a second model to judge your work, or are you sticking with 'keep going'? Let me know in the comments. And subscribe for more Claude Code news."

This adds the three required components (rhetorical question + comments-ask + subscribe-ask) while preserving the locked Dynamous outro pointer (per `feedback_dynamous_short_outro` memory rule).

### Heteronym audit

- `live` — not present ✓ (per project constraint)
- `lead` (as noun) — not present ✓ (per project constraint)

### After fixes

Re-run `/diy-yt-creator:phase2-5-critique claude-code-goal-command` to clear the gates.

**STOP — do NOT proceed to Phase 2a until QG-2b, QG-4, and QG-5 all clear.**
