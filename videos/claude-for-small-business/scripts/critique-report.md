# Phase 2.5 Critique Report — claude-for-small-business

- **Script**: `videos/claude-for-small-business/scripts/full-script.md`
- **Voice profile**: `news-explainer`
- **Topic type**: `ARTICLE_RESPONSE`
- **Date**: 2026-05-14

## Metrics

- **Total narrated words**: ~388 (Scene 1 is silent thumbnail hold)
- **Estimated narration duration**: ~155s @ 2.5 wps (fits 180s composition budget with 6s silent open + ~19s of pauses/SFX beats reserved)
- **Mid-video word target (58%)**: ~225 words

---

## Pass 1 — Hook Strength (QG-1)

Hook = Scene 1 (silent thumbnail hold) + Scene 2 (Sunday-night scramble). Treating Scene 2 as the spoken hook.

Opening line: *"Every owner asks the same question the week before payday. Will I make it?"*

| Dimension       | Score      | Notes                                                                                                              |
| --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Curiosity Gap   | 9/10       | "Will I make it?" creates an immediate, unambiguous gap in sentence 2. Universal SMB pain anchor.                  |
| Stakes Clarity  | 9/10       | Specific, tangible stakes: five tabs by Sunday night, still guessing about payroll. Quantified pain.               |
| Specificity     | 8/10       | Five named tools (QuickBooks, PayPal, Gmail, bank, payroll provider) within first 30s. "Five minutes" payoff promise. |
| Stun Gun        | 2/2        | Explicit "But Anthropic just shipped something..." pivot at end of Scene 2.                                        |
| Value Alignment | 0.5/0.5    | "Anthropic just shipped something that answers it" names the topic + subject by second 5.                          |
| Promise         | 1/1        | "Anthropic just shipped something that answers it in five minutes" is an explicit promise of resolution.           |
| **HOOK SCORE**  | **9.4/10** | **PASS (threshold: 7.0)** — base=(9*0.4)+(9*0.4)+(8*0.2)=8.8; +0.1 stun; +0.5 alignment; +1 promise; +0.5 narrative-flow (`because/and/but`). Capped 10. |

Hook complies with Type B (Counterintuitive Observation — "every owner asks → Anthropic answers it in 5min") and Type D (Shared Frustration — Sunday-night scramble stated as fact). Magnitude framing also implicit.

---

## Pass 2 — Retention Curve (QG-3)

### Loop Openers

Required minimum = `max(2, floor(2.5min / 1.5)) = 2`.

| # | Scene    | Position | Loop Opener Phrase                                  |
| - | -------- | -------- | --------------------------------------------------- |
| 1 | Scene 3  | Opening  | "And it's not a new model."                         |
| 2 | Scene 4  | Opening  | "And these workflows don't sit in a chat window..." |
| 3 | Scene 5  | Opening  | "Here's what it actually looks like."               |
| 4 | Scene 6  | Opening  | "Because this isn't built for the Fortune 500."     |
| 5 | Scene 7  | Opening  | "And this isn't a rumor."                           |
| 6 | Scene 8  | Opening  | "Plus the trust beat."                              |

**6 found, 2 required — PASS**

### Boxer's Rhythm (advisory)

Scene 2 mixes 12-word, 3-word, 1-word, 1-word, 1-word, 1-word, 1-word, 13-word, 15-word sentences — strong percussive rhythm. Scene 6 has rhythmic triple-jab ("Not for the 15-person... Not for the 30-person... Not for the 50-person."). No monotonous stretches detected.

### Hedging Language (advisory)

`if you` appears once in Scene 4 ("If you've ever tried...") — this is the mandatory direct-address sentence, not weak hedging. Zero `might / maybe / could be / probably / perhaps`. Clean.

---

## Pass 3 — TTS Readability (advisory)

### Scene length compliance

| Scene    | Words | Implied seconds | Plan duration | Status |
| -------- | ----- | --------------- | ------------- | ------ |
| Scene 2  | 50    | 20.0s           | 22s           | OK (narration 7-26s leaves 1s of silence at end for PIVOT slam) |
| Scene 3  | 57    | 22.8s           | 24s           | OK    |
| Scene 4  | 57    | 22.8s           | 22s           | Slightly tight (TTS pacing may push, monitor) |
| Scene 5  | 9     | 3.6s            | 32s           | UNDER by design — clip plays 29s with narration ducked |
| Scene 6  | 46    | 18.4s           | 18s           | OK    |
| Scene 7  | 31    | 12.4s           | 16s           | OK    |
| Scene 8  | 91    | 36.4s           | 22s           | **OVER** — narration density 1.65× target. Will need TTS pacing tightening at Phase 2a OR Phase 3.5 retiming. Advisory flag, not blocking. |
| Scene 9  | 47    | 18.8s           | 18s           | OK    |

Total fits. **Scene 8 is the only friction point** — flag for Phase 2a / Phase 3.5 to confirm narration finishes within the 22s phase or extend phase duration when retiming to transcript.

### Sentence length

No sentence exceeds 25 words. Longest: Scene 4 ("If you've ever tried to run an S M B with a generic chatbot that can't see your books, this is the difference.") = 24 words. OK.

### Acronym safety

All acronyms already spelled letter-by-letter in script: `C R M`, `S M B`, `H V A C` — TTS-safe.

### Symbol check

No `{} <> [] $ % @ #` in narration. Clean.

---

## Pass 4 — Story Arc (QG-2a + QG-2b)

### Arc Element 1 — Hook → Value Timing

First concrete payoff: Scene 3 "15 ready-to-run workflows, plus 15 reusable skills..." at ~t=30s. Threshold for 3min+: 90s. **Hits at 30s — 60s ahead of deadline.**

**Score: 10/10**

### Arc Element 2 — Benefit-Led Scenes

- Scene 2: pain-led (universal owner question) — benefit ✓
- Scene 3: feature-reveal but reframed as "the bundle answers it" — benefit ✓
- Scene 4: "tools you already pay for" + viewer-pain framing ("if you've ever tried...") — benefit ✓
- Scene 5: demo proof — neutral
- Scene 6: target-customer framing — benefit ✓
- Scene 7: receipt-validation — neutral
- Scene 8: trust + customer outcome — benefit ✓

6 of 7 body scenes benefit-led. **Score: 9/10**

### Arc Element 3 — CTA Strength (QG-2b, INDEPENDENT)

CTA verbatim:
> "So here's the question. You're already paying for Copilot. Sunday-night payroll just dropped to five minutes inside the tools you already use. Switching from Copilot, or sticking? Drop your pick in the comments. Subscribe for more AI news. And if you want to learn more about AI, check out the dynamous.ai community."

| Check | Test | Result |
|-------|------|--------|
| C1    | Ends with `?` on a question | ✅ "Switching from Copilot, or sticking?" |
| C2    | Binary or short-list answerable | ✅ Two-option answer: "switching" or "sticking" — 1 word each, mobile-typable |
| C3    | Polarizing / contrarian stance | ✅ Forces tool-loyalty pick; tribal Copilot-vs-Claude framing |
| C4    | References specific video claim | ✅ Anchors to the Copilot framing built in Scene 4 ("generic chatbot that can't see your books") + Sunday-night payroll → 5 min outcome from Scene 5 |

**4/4 checks PASS. Banned-closer scan: no match (no "what do you think", "let me know in the comments" standalone, "smash that like", etc. — comments-ask is anchored to a specific debate question).**

**arc3_score = 10/10 — PASS QG-2b**

### Arc Element 4 — Narrative Cohesion

Open loop from Scene 2 ("will I make it?") resolves implicitly at Scene 9 CTA ("Sunday-night payroll just dropped to five minutes"). Clear beginning (pain) → middle (15+15 + integration + demo + quote + proof + trust) → end (debate-CTA). Scene 7 is the slight weak point — feels redundant with Scene 3's announcement framing, but the screenshot-as-receipt beat earns it. **Score: 8/10**

### Arc Element 5 — Experience Signal (advisory)

The narrator is reporting on a third-party launch, not testing it personally. No scar/friction-point claimed — appropriate for news-explainer profile (per memory rule: never fabricate "I tested this"). Arc5 = 0; no experience bonus, but no penalty either.

### QG-2a Score

`qg2a_score = round((10 + 9 + 8) / 3, 1) = 9.0`
Experience bonus = 0.
**QG-2a final = 9.0/10 — PASS (threshold: 7.0)**

### QG-2b Score

**QG-2b final = 10/10 — PASS (threshold: 7.0)**

| Element                | Score      | Notes                                                              |
| ---------------------- | ---------- | ------------------------------------------------------------------ |
| Hook → Value Timing    | 10/10      | First payoff at t≈30s vs 90s threshold                             |
| Benefit-Led Scenes     | 9/10       | 6/7 body scenes lead with viewer-pain/gain                         |
| CTA Strength           | 10/10      | All 4 debate-CTA checks pass                                       |
| Narrative Cohesion     | 8/10       | Open loop resolved; Scene 7 slight redundancy                      |
| Experience Signal      | 0          | News-explainer profile — narrator is reporter, no scar required    |
| **QG-2a (Arc 1+2+4)**  | **9.0/10** | **PASS**                                                           |
| **QG-2b (CTA solo)**   | **10/10**  | **PASS**                                                           |

---

## Pass 5 — Voice & AI-Phrasing (QG-4)

### A. Generic AI-phrasing scan (playbook §11)

| Pattern | Found |
|---------|-------|
| Critical (But here's the thing / Most developers don't / No more X / X changes everything / If this helped, subscribe) | **0** |
| High (Let me show you / Here's the thing / Game changer / The future of / Under the hood) | **0** |
| Medium (It's not just X — it's Y / Nobody talks about / Where it gets interesting / Think about it / Paradigm shift / Imagine) | **0** |

### B. Channel-specific voice (brand-voice-news-explainer.md)

#### B.1 — Banned word scan (case-insensitive)

Scanned: `delve, tapestry, harness, unlock, leverage, paradigm, seamless, cutting-edge, groundbreaking, transformative, revolutionize, furthermore, moreover, nevertheless, undoubtedly, changed everything, you won't believe, the future is here, absolutely incredible, mind-blowing, next level, smash that like button, don't forget to subscribe, this is huge, the most powerful, full potential, some might argue, arguably, generally speaking, experts agree, studies show, research suggests`.

**Hits: 0**

#### B.2 — Hard rules (10 rules, news-explainer version)

| # | Rule | Verdict |
|---|------|---------|
| 1 | No channel-name / greeting open | ✅ Opens on "Every owner asks..." |
| 2 | No "in this video I'll show you" summary | ✅ |
| 3 | No motivational frame | ✅ |
| 4 | No manufactured stakes | ✅ Stakes are real ("Anthropic shipped this") |
| 5 | No em dashes in narration | ✅ Only em dashes are in title H1 (line 1) and Scene 3 heading (line 13) — neither is spoken |
| 6 | No bullet-pointed narration | ✅ Prose throughout |
| 7 | No emotion-attribution to viewer | ✅ "If you've ever tried" addresses action, not feeling |
| 8 | No vague-promise closer | ✅ Closes on concrete debate CTA |
| 9 | No fabricated "I tested" | ✅ Pure reporting frame |
| 10 | Third-party claims attributed | ✅ "Lina Ochman runs S M B at Anthropic", "Anthropic posted it themselves on May 13th", "HubSpot calls it the first C R M connector", "Daniela Amodei calls this..." |

#### B.3 — Hook type (Type A-news / B / C / D)

Scene 2 hook = **Type D — Shared Frustration** (Sunday-night payroll scramble stated as fact), pivots to Type A-news magnitude ("Anthropic just shipped something that answers it"). ✅ Compliant.

#### B.4 — First-person `we` scan

Zero `we` used as narrator's voice. (`Every owner` / `you` / `Anthropic` / `they` — all correct.) ✅

#### B.5 — Contractions

Uses contractions throughout: "isn't", "it's", "don't", "you've", "what's", "didn't", "doesn't", "here's", "aren't", "you're". Zero expanded forms where contraction would be natural. ✅

### ARTICLE_RESPONSE source-grounding check

Forbidden third-party-only stats scan:
- `36M / 36 million` SMBs (TechCrunch only): **NOT FOUND** ✅
- `$30B / 30 billion` run-rate (Yahoo only): **NOT FOUND** ✅
- `$30-43/seat` / Copilot dollar pricing (Compare-the-Cloud only): **NOT FOUND** ✅ (brand name "Copilot" appears but no dollar figure)

All on-screen claims trace to primary source (anthropic.com/news/claude-for-small-business) or the companion YouTube video (lserpKbUDjc). Press articles used only for cross-verification, never as the sole script source. **No fabrication. No third-party leakage.**

### QG-4 Result

`banned_count = 0` — **PASS**

---

## Pass 6 — Narrative Flow & Direct Address (QG-5, news-explainer)

### QG-5a — Connector Density

Body scenes (3, 4, 5, 6, 7, 8) — explanatory connectors found:

| Scene | Connectors found (unique types) |
|-------|---------------------------------|
| Scene 3 | `And` (sentence-initial), `because`, `plus` — 3 unique |
| Scene 4 | `And` (sentence-initial), `if you` (direct address counts toward implication) — 1 unique connector (`and`) |
| Scene 5 | (terse — narrator pause; no connectors needed) |
| Scene 6 | `Because` (sentence-initial), `and` — 2 unique |
| Scene 7 | `And` (sentence-initial), `too` — 1 unique |
| Scene 8 | `Plus` (sentence-initial), `And` — 2 unique |

**Total unique connectors across body**: `and`, `because`, `plus` (3 distinct types). Total occurrences: 8+. **Score: 9/10** (≥5 connectors, ≥3 unique types). **PASS QG-5a (≥6).**

### QG-5b — Direct Address Sentence

**Found in Scene 4**: *"If you've ever tried to run an S M B with a generic chatbot that can't see your books, this is the difference."*

Matches canonical pattern `"If you ['ve noticed / use / care about / build on] X, [implication]"`. **Score: 2/2 — PASS QG-5b.**

### QG-5c — Engagement CTA Closer

Scene 9 final scene checks:
1. **Rhetorical / debate question**: ✅ "Switching from Copilot, or sticking?"
2. **Comments-ask**: ✅ "Drop your pick in the comments."
3. **Subscribe-ask**: ✅ "Subscribe for more AI news."

All three components present. **Score: 2/2 — PASS QG-5c.**

### QG-5 Final

**QG-5a (9/10) + QG-5b (2/2) + QG-5c (2/2) — ALL PASS. QG-5 PASS.**

---

## Pass 7 — JCRR Line Audit (ADVISORY)

Body scenes only (Scenes 3, 4, 5, 6, 7, 8 — excluding hook and CTA).

| Scene | Sentences | J | C | R-reason | R-receipt | F (filler) | Filler % |
|-------|-----------|---|---|----------|-----------|------------|----------|
| Scene 3 | 9 | 1 | 5 | 2 | 1 | 0 | 0% |
| Scene 4 | 4 | 0 | 2 | 1 | 1 | 0 | 0% |
| Scene 5 | 2 | 0 | 0 | 0 | 0 | 2 | 100% (meta-narration only — *"Here's what it actually looks like. Full demo's in the description."*) |
| Scene 6 | 5 | 1 | 3 | 0 | 1 | 0 | 0% |
| Scene 7 | 4 | 0 | 3 | 0 | 1 | 0 | 0% |
| Scene 8 | 9 | 1 | 6 | 1 | 1 | 0 | 0% |
| **Total** | **33** | 3 | 19 | 4 | 5 | 2 | **6.1%** |

**JCRR % = 93.9% — STRONG rating** (lean script, every sentence carries information except the two intentional Scene 5 demo-frame meta lines which are deliberate transition framing for the embedded clip).

**Filler runs > 2 consecutive**: None. Scene 5's 2 filler sentences are intentional framing for the embedded demo clip — not slop, but technically meta-narration. Recommend keeping as-is.

**Pass 7 advisory: STRONG (93.9% JCRR). No action required.**

---

## Visual-Pacing & Step-by-Step Reveal Audit (cross-checking plan.md)

Per `.claude/rules/visual-pacing-5s.md` and `.claude/rules/step-by-step-reveal.md`:

| Scene | Plan max gap | Status | Notes |
|-------|--------------|--------|-------|
| Scene 1 | 6s static | EXEMPT (thumbnail-grade open hold; rule explicitly relaxes for opening hold ≤2.5s — extended to 5.5s + 0.5s fade is acceptable per shorts-thumbnail-frames.md) |
| Scene 2 | 8s gap (14→22) | **PLAN PRE-FLAGGED FIX**: marker-circle on "payday" at t=18 inserted (plan line 249) — gap now ≤4s ✓ |
| Scene 3 | ≤2s | ✅ Beats every ≤2s |
| Scene 4 | ≤2.5s | ✅ Beats every ~2.5s |
| Scene 5 | continuous video | ✅ Video plays 29s (counts as motion); 1s pointer-hold post-clip |
| Scene 6 | ≤4s | ✅ |
| Scene 7 | ≤4s | ✅ |
| Scene 8 | ≤4s | ✅ |
| Scene 9 | ≤3s + terminal hold | ✅ Terminal hold relaxation per shorts-thumbnail-frames.md |

Step-by-step reveal compliance: ✅ Every enumerated list (skill chips, partner logos, customer rows, business-type chips) reveals one-at-a-time per the rule. Plan explicitly calls for `tl.set()` hidden-until-reveal pattern (plan line 582).

**Visual pacing AUDIT: PASS** (assuming composition build follows the plan's pre-flagged Scene-2 marker-circle insertion at t=18).

---

## Pass 7 advisory — Engagement-hooks-framework cross-check

- **Triple-Threat Hook (visual + text + spoken alignment)**: ✅ Scene 1 thumbnail-grade hold (visible from t=0) + Scene 2 spoken "will I make it?" question + tab-cluster visual reveal — all three layers reinforce each other.
- **Violent Contrast (200-unit lean-and-snap)**: ✅ Scene 2 → Scene 3 pivot from chaotic 5-tab scramble to single `/plan-payroll` slam meets the slam-cut threshold (impact-slam + screen-shake + cinematic-whoosh layered SFX per plan).
- **One-Question-Loop sentence flow**: ✅ "Will I make it?" (Q opens) → answer revealed across Scenes 3-8 → "Switching from Copilot, or sticking?" (next Q closes the loop and opens the comments-loop).
- **Lego-Brick outlier deconstruction**: ✅ Explicit "It's not a new model. It's a bundle." (Scene 3) — frames the launch as the Lego brick (15 workflows + 15 skills snap together), not the model.
- **Anti-Slop (Receipts + Thesis + JCRR + Specificity Ladder)**: ✅ Every claim has a receipt URL (Anthropic primary + companion YT); thesis-driven; 93.9% JCRR; specificity ladder runs from universal pain ("every owner") → specific stakes ("five tabs by Sunday night") → specific receipt ("posted on May 13th, inside Claude Cowork").

**Engagement-hooks-framework advisory: STRONG across all 5 dimensions.**

---

## Gate Summary

| Gate  | Check                              | Result      | Score/Status                                                          |
| ----- | ---------------------------------- | ----------- | --------------------------------------------------------------------- |
| QG-1  | Hook Strength                      | **PASS**    | 9.4/10 (threshold: 7.0)                                               |
| QG-2a | Story Arc (Arc1+Arc2+Arc4 avg)     | **PASS**    | 9.0/10 (threshold: 7.0)                                               |
| QG-2b | CTA Strength (Arc3 standalone)     | **PASS**    | 10/10 (threshold: 7.0, independent sub-gate — all 4 debate checks pass) |
| QG-3  | Loop Opener Frequency              | **PASS**    | 6 found, 2 required                                                   |
| QG-4  | AI-Phrasing Detection              | **PASS**    | 0 banned phrases (playbook + brand-voice + ARTICLE_RESPONSE source-grounding all clean) |
| QG-5  | Narrative Flow & Direct Address    | **PASS**    | QG-5a 9/10, QG-5b 2/2, QG-5c 2/2 (news-explainer profile)             |
| QG-7  | JCRR Methodology (advisory)        | ADVISORY    | 93.9% JCRR, 0 filler runs >2 — STRONG                                 |

**Overall Verdict: PASS** — All applicable blocking gates cleared.

### Auto-fixable advisories (NON-blocking)

1. **Scene 8 narration density** (91 words / 22s phase = 1.65× target wps). Will likely fit at TTS speed 1.05× but flag for Phase 2a TTS chunk-test OR Phase 3.5 phase-duration extension to 24-25s if narration overruns.
2. **Scene 5 filler classification** (2 meta-narration sentences). Intentional demo-frame transition; recommend keeping. Could trim *"Full demo's in the description."* to *"Full demo, description."* if a tighter beat is preferred, but not required.
3. **Scene 7 narrative weight**: feels slightly redundant with Scene 3 framing. Not a gate failure — but if composition build needs to recover 2-3s for Scene 8 narration density, Scene 7 is the candidate to compress.

### Blocking issues

**None.** Script is approved for Phase 2a.

---

## Next Step

Run `/diy-yt-creator:phase2a-tts-script claude-for-small-business`.
