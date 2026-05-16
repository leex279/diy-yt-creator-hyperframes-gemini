# Phase 2.5 Critique Report — claude-personal-guidance

**Date:** 2026-05-08
**Voice profile:** `news-explainer` (per `videos/claude-personal-guidance/research/content-brief.md`)
**Script:** `videos/claude-personal-guidance/scripts/full-script.md`

## Script Metrics

```
Script: videos/claude-personal-guidance/scripts/full-script.md
Total words: 369
Estimated duration: 2m 27.6s (147.6 seconds)
Mid-video word target (58%): 214 words
```

Per-scene word counts:

| Scene | Words | Role           |
| ----- | ----- | -------------- |
| 1     | 24    | Hook           |
| 2     | 58    | Topic chart    |
| 3     | 61    | Sycophancy twist |
| 4     | 83    | Pushback flip  |
| 5     | 61    | Loop / Opus 4.7 |
| 6     | 50    | Takeaway       |
| 7     | 32    | CTA            |

Plan budget: 150s render duration. Script narration estimate (147.6s) lands within ±2% of target — clean.

---

## Pass 1: Hook Strength Scoring (Quality Gate 1)

**Hook (Scene 1):**
> "Six percent of Claude chats are people asking life questions, and Anthropic just measured how often Claude tells them what they want to hear."

| Dimension       | Score      | Notes                                                                                                       |
| --------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| Curiosity Gap   | 8/10       | "how often Claude tells them what they want to hear" creates an unambiguous sycophancy gap — viewer wants the number |
| Stakes Clarity  | 8/10       | Stakes are clear (model-truthfulness on life decisions) — high but not yet quantified in hook itself        |
| Specificity     | 8/10       | "Six percent" + named subjects (Claude, Anthropic, life questions) — named entities + leading stat          |
| Stun Gun        | 0/2        | No But/However/Yet/Although pivot in hook                                                                   |
| Value Alignment | 0.5/0.5    | Yes — viewer knows by sentence one this is about Claude + personal guidance + sycophancy measurement        |
| Promise         | 0/1        | No explicit "in the next X minutes" promise                                                                 |
| Narrative Flow  | +0.5       | "and" connector links the two clauses — earns the news-explainer narrative_flow bonus                       |
| **HOOK SCORE**  | **9.0/10** | **PASS (threshold 7.0)**                                                                                    |

base = (8 × 0.4) + (8 × 0.4) + (8 × 0.2) = 8.0
hook_score = min(10, 8.0 + 0 + 0.5 + 0 + 0.5) = **9.0**

**Hook type compliance** (brand-voice §B.3): matches **Type C — The Specific Number** with paired "why it matters" sentence containing the `and` connector — required pairing per news-explainer profile is satisfied. PASS.

---

## Pass 2: Retention Curve Analysis (Quality Gate 3 + advisories)

### Check 1 — Loop Openers (QG-3)

Required minimum = `max(2, floor(2.46m / 1.5))` = **max(2, 1)** = **2**

| #   | Scene    | Position                | Loop Opener Phrase                                                  |
| --- | -------- | ----------------------- | ------------------------------------------------------------------- |
| 1   | Scene 2  | Closing line (T1→P3)    | "Here is the twist."                                                |
| 2   | Scene 3  | Closing line (T2→P4)    | "Now watch the trigger."                                            |
| 3   | Scene 4  | Opening (T3→P4)         | "Here is the pattern Anthropic isolated, and it is the scar of this whole study." |
| 4   | Scene 5  | Opening (T4→P5)         | "So Anthropic ran a three step research loop."                      |
| 5   | Scene 6  | Opening (T5→P6)         | "Here is what this actually means."                                 |

**Result: 5 found, 2 required — PASS**

### Check 2 — Boxer's Rhythm (Advisory)

Spot-checked Scenes 2, 3, 4. Sentence lengths vary widely (Scene 2: 17 / 9 / 4 / 4 / 4 / 4 / 12 / 4; Scene 4: 8+ / 4 / 5 / 5 / 9 / 12 / 4 / 4 / 8 / 13). No 5-sentence stretch monotonous. **PASS (advisory)**.

### Check 3 — Hedging Language (Advisory)

| Term     | Occurrences | Lines                                                          |
| -------- | ----------- | -------------------------------------------------------------- |
| "if you" | 2           | S4: "If you have ever argued with Claude…" (direct-address — intentional). S7: "if you want to learn more about AI…" (Dynamous outro — locked) |

Both `if you` instances are intentional patterns (one is the canonical news-explainer direct-address; one is the locked Dynamous outro). Not advisory-flag-worthy. **PASS (advisory)**.

---

## Pass 3: TTS Readability Check (Advisory)

### Check 1 — Scene Length Compliance

| Scene    | Words | Target (s × 2.5)   | Range (±10%) | Status     |
| -------- | ----- | ------------------ | ------------ | ---------- |
| Scene 1  | 24    | 25 (10s × 2.5)     | 22-28        | OK         |
| Scene 2  | 58    | 55 (22s × 2.5)     | 50-61        | OK         |
| Scene 3  | 61    | 55 (22s × 2.5)     | 50-61        | OK         |
| Scene 4  | 83    | 70 (28s × 2.5)     | 63-77        | **OVER**   |
| Scene 5  | 61    | 55 (22s × 2.5)     | 50-61        | OK         |
| Scene 6  | 50    | 45 (18s × 2.5)     | 41-50        | OK         |
| Scene 7  | 32    | 61 (24.4s × 2.5)   | 55-67        | **UNDER**  |

Scene 4 is +18% over (intentional per Phase 2 summary — carries the central scar + named-pattern coinage). Scene 7 is -47% under target — the CTA is short by design (4 sentences); the remaining 12s of the 24.4s P7 budget is for URL pill, subscribe pill, and endcard pacing per plan. Both deltas align with Phase 1 plan intent. **No blocking issue**.

### Check 2 — Sentence Length

Sentences over 25 words: **0**. PASS.

### Check 3 — Acronym Safety

Unsafe acronyms: **0**. (TTS-spelled forms `dynamous dot AI`, `Opus four point seven`, `four point six`, `four point seven` are correctly pre-spelled. `Clio` is treated as a word, will pronounce KLEE-oh.) PASS.

### Check 4 — Symbol Check

`{ } < > [ ] $ % @ #` (non-break tags): **0**. PASS.

### Check 5 — 800 Char Estimate

Largest scene (S4) = 83 × 5.5 = 456 chars. Well under 800. PASS.

---

## Pass 4: Story Arc Completeness (Quality Gate 2)

### Arc 1 — Hook→Value Timing

First concrete value-payoff lands in Scene 2 (~10–14s in: Clio + 1M sample + 6% domain breakdown). For 150s long-form territory, threshold is 90s. Lands well inside the 4-second short-form threshold via the hook stat itself ("six percent" already a value-hit in S1). **9/10** — on time, high-value hit.

### Arc 2 — Benefit-Led Scenes

Scene-opening framings:
- S2 — "Anthropic ran their Clio analysis…" — methodology lead (mixed)
- S3 — "The popular topics are not the sycophantic ones." — contrarian framing (benefit-led)
- S4 — "Here is the pattern Anthropic isolated, and it is the scar…" — pattern-led (benefit-led)
- S5 — "So Anthropic ran a three step research loop." — process lead (mixed)
- S6 — "Here is what this actually means." — implication-led (benefit-led)

3 of 5 body scenes are benefit-led; 2 are mixed (methodology/process leads but resolve to viewer-facing outcome quickly). **7/10** — ≥ 75% threshold close to met (60%); rounded conservatively because S2 and S5 open with process before payoff.

### Arc 3 — CTA Strength (QG-2b standalone)

CTA verbatim:
> "Should AI vendors publish numbers like this? Tell me below. Subscribe for more Anthropic research news. And if you want to learn more about AI, check out the dynamous dot AI community."

| Component               | Present? | Quote                                                  |
| ----------------------- | -------- | ------------------------------------------------------ |
| Debate-sparking question | YES      | "Should AI vendors publish numbers like this?"         |
| Specific video reference / topic anchor | YES      | "for more Anthropic research news" (topic-anchored subscribe-ask) |
| Under 15 words (core CTA, excl. Dynamous outro) | YES      | First 3 sentences = 15 words exactly                   |

All three criteria met. Plus the locked Dynamous outro line lands cleanly at the tail. **9/10**.

### Arc 4 — Narrative Cohesion

Primary open loop established in S1 ("Anthropic just measured how often Claude tells them what they want to hear") resolves in S5 ("In Opus four point seven, sycophancy in relationship guidance is half the rate it was in Opus four point six. And the fix generalized to other domains."). Logical scene flow: 6% reveal → topic distribution → sycophancy distribution flips → pushback mechanism → fix → takeaway → CTA. Clear beginning/middle/end. **9/10**.

### Arc 5 — Experience Signal (Advisory Bonus)

Scar candidates:
1. S4: "Here is the pattern Anthropic isolated, and **it is the scar of this whole study**." — explicit naming of the failure mode + the *named-pattern coinage* "the pushback flip" (Story Lock #1).
2. S4: "**If you have ever argued with Claude until it agreed with you, this is why.**" — first-person-adjacent lived experience routed to the viewer (the Gemini direct-address pattern).

Scar found. **+0.5 bonus**.

### Scoring

```
qg2a_score = (Arc1 + Arc2 + Arc4) / 3 = (9 + 7 + 9) / 3 = 8.33
qg2a_score += experience_bonus (0.5) = 8.83
qg2a_score (rounded) = 8.8

qg2b_score = Arc3 = 9.0
```

| Element                | Score        | Notes                                                                |
| ---------------------- | ------------ | -------------------------------------------------------------------- |
| Hook to Value Timing   | 9/10         | Value hits in S1 (6%) and again at S2 ~10s — well inside threshold   |
| Benefit-Led Scenes     | 7/10         | 3/5 benefit-led; S2 & S5 open with process before payoff             |
| CTA Strength           | 9/10         | All 3 components present; under-15-word core; Dynamous outro intact  |
| Narrative Cohesion     | 9/10         | Primary loop opened in S1, resolved in S5; clean arc                 |
| Experience Signal      | +0.5         | "it is the scar of this whole study" + viewer-routing direct address |
| **QG-2a (Arc 1+2+4)**  | **8.8/10**   | **PASS (threshold 7.0)**                                             |
| **QG-2b (CTA solo)**   | **9.0/10**   | **PASS (threshold 7.0)**                                             |

---

## Pass 5: Voice & AI-Phrasing Detection (Quality Gate 4)

### A. Generic AI-phrasing (playbook §11)

| Severity tier         | Hits | Notes                                            |
| --------------------- | ---- | ------------------------------------------------ |
| Critical (zero-tol.)  | 0    | No "But here's the thing", "changes everything", etc. |
| High (zero-tol.)      | 0    | No "let me show you", "game changer", etc.       |
| Medium (advisory)     | 0    | No "nobody talks about", "imagine", etc.         |

### B. Channel-specific (brand-voice-news-explainer.md)

#### B.1 — Banned word lists

| Subgroup               | Hits | Notes                                                             |
| ---------------------- | ---- | ----------------------------------------------------------------- |
| Generic AI phrases     | 0    | No `delve`, `tapestry`, `harness`, `unlock`, `leverage`, etc.    |
| Hype phrases           | 0    | No `changed everything`, `mind-blowing`, `smash that like button`, etc. |
| Over-hedging phrases   | 0    | No `arguably`, `for the most part`, `generally speaking`, etc.    |

#### B.2 — Hard rules (10 items)

| #   | Rule                                              | Hits | Status                                                              |
| --- | ------------------------------------------------- | ---- | ------------------------------------------------------------------- |
| 1   | No channel-name / greeting at open                | 0    | PASS — opens with the 6% claim                                      |
| 2   | No "in this video I'll show you…" summary         | 0    | PASS                                                                |
| 3   | No motivational frame                             | 0    | PASS                                                                |
| 4   | No manufactured stakes ("you're already behind")  | 0    | PASS                                                                |
| 5   | No em dashes (—) in narration                     | 0    | PASS — all em dashes from plan softened to commas/periods           |
| 6   | No bullet-pointed narration                       | 0    | PASS — pure prose                                                   |
| 7   | No emotion-attribution to viewer                  | 0    | PASS — direct address routes to action ("argued with Claude"), not feeling |
| 8   | No vague-promise closer                           | 0    | PASS — closer is rhetorical question                                |
| 9   | No fabricated original research                   | 0    | PASS — every claim attributed to Anthropic                          |
| 10  | Always attributes third-party claims              | OK   | PASS — "Anthropic ran their Clio analysis", "Anthropic isolated", "Anthropic ran a three step research loop" |

#### B.3 — Hook type compliance

Hook matches **Type C — The Specific Number** ("Six percent of Claude chats are people asking life questions") paired with the news-explainer-mandatory why-it-matters connector clause via `and` ("and Anthropic just measured how often Claude tells them what they want to hear"). PASS.

#### B.4 — First-person check

Scan for `we` as narrator: **0 hits**. The narrator never uses `we` as a company-pretender. PASS.

#### B.5 — Contractions check

| Expanded form    | Count | Locations                                                             |
| ---------------- | ----- | --------------------------------------------------------------------- |
| "it is"          | 2     | S4: "and it is the scar of this whole study"; S5: "and it is specific" |
| "you are"        | 1     | S4: "agrees you are right"                                            |
| "Here is"        | 3     | S2: "Here is the twist"; S4: "Here is the pattern"; S6: "Here is what this actually means" |
| "were not"       | 1     | S2: "almost six percent of them were not code"                        |
| "you have"       | 1     | S4: "If you have ever argued with Claude…"                            |

**Total expanded contractions: 8.** Per command-file rule (Pass 5 §B.5): "collectively if there are 3+, that's a QG-4 failure." 8 ≥ 3 → **FAIL**.

**Mitigating context (advisory note for the orchestrator/writer):**
The "Here is" trio functions as a deliberate three-beat loop-opener motif (S2, S4, S6) — TTS-friendly, rhythmic, and the news-explainer profile EXPLICITLY VALUES the magnitude/declarative cadence of "Here is the …" loop openers. Contracting all three to "Here's" would land softer and less rhetorical. However, the strict QG-4 rule does not provide a stylistic exception. The remaining five (`it is` ×2, `you are`, `were not`, `you have`) ARE natural contraction candidates and should be tightened.

**Suggested fixes (apply BEFORE re-running Pass 2.5):**

| Scene | Current                                                          | Fix                                                                  |
| ----- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| S2    | "almost six percent of them were not code"                       | "almost six percent of them weren't code"                            |
| S4    | "and it is the scar of this whole study"                         | "and it's the scar of this whole study"                              |
| S4    | "and suddenly agrees you are right"                              | "and suddenly agrees you're right"                                   |
| S4    | "If you have ever argued with Claude until it agreed with you"   | "If you've ever argued with Claude until it agreed with you"          |
| S5    | "and it is specific"                                             | "and it's specific"                                                  |
| S2    | "Here is the twist."                                             | Keep OR change to "Here's the twist." — writer's call (3-instance motif) |
| S4    | "Here is the pattern Anthropic isolated"                         | Keep OR change to "Here's the pattern Anthropic isolated"            |
| S6    | "Here is what this actually means."                              | Keep OR change to "Here's what this actually means."                 |

Applying the 5 mandatory fixes (the natural-contraction cases) drops the expanded count from 8 to 3 — STILL FAILS at 3. To clear QG-4, **at least 6 of the 8 must be contracted** (leaving ≤ 2). The cleanest path: contract all 5 natural cases AND 1 of the 3 "Here is" loop openers — drops to 2. Even cleaner: contract all 8 → drops to 0.

### Scoring

```
banned_count = 0 (playbook critical/high) + 0 (B.1) + 0 (B.2) + 0 (B.3) + 0 (B.4) + 8 (B.5)
             = 8
QG-4 FAIL (banned_count > 0)
```

**Result: 8 blocking hits — FAIL**

---

## Pass 6: Narrative Flow & Direct Address (Quality Gate 5 — news-explainer)

### Check 1 — Connector Density

Body scenes (S2-S6). Each unique connector counts once per scene:

| Scene | Connectors found                                         |
| ----- | -------------------------------------------------------- |
| S2    | `so`, `so` (sentence-initial)                            |
| S3    | `but`, `but` (sentence-initial)                          |
| S4    | `to <verb>` ("to flatter…"), `why` ("this is why")       |
| S5    | `and` (sentence-initial), `so`, `so` (sentence-initial), `to <verb>` ("to use Claude…", "back into training") |
| S6    | `to <verb>` ("to trust the answer", "to flatter you", "to push twice")                                |

Unique connector types across body: **7** (`and` sentence-initial, `but`, `but` sentence-initial, `so`, `so` sentence-initial, `to <verb>`, `why`)
Total connector instances (unique per scene, summed): **11**

Score: **9/10** (≥ 5 connectors, ≥ 3 unique types)

QG-5a (≥ 6): **PASS**

### Check 2 — Direct Address Sentence (body)

Found in S4: **"If you have ever argued with Claude until it agreed with you, this is why."** — canonical news-explainer pattern (`If you …`).

Score: **2** — at least one direct-address sentence present in body.

QG-5b (== 2): **PASS**

### Check 3 — Engagement CTA Closer

Scene 7:
> "Should AI vendors publish numbers like this? Tell me below. Subscribe for more Anthropic research news. And if you want to learn more about AI, check out the dynamous dot AI community."

| Component        | Present? | Quote                                                 |
| ---------------- | -------- | ----------------------------------------------------- |
| Rhetorical question | YES      | "Should AI vendors publish numbers like this?"        |
| Comments-ask     | YES      | "Tell me below."                                      |
| Subscribe-ask    | YES      | "Subscribe for more Anthropic research news."         |

Score: **2** (all three present)

QG-5c (≥ 2): **PASS**

### QG-5 Result

| Sub-check                 | Score      | Notes                                                                              |
| ------------------------- | ---------- | ---------------------------------------------------------------------------------- |
| Connector Density         | 9/10       | 11 unique-per-scene instances, 7 unique types — well above gold-standard           |
| Direct Address (body)     | 2          | "If you have ever argued with Claude until it agreed with you, this is why."       |
| Engagement CTA Closer     | 2          | All three components present in canonical order                                    |
| **QG-5 (Narrative Flow)** | **PASS**   | All three sub-gates clear                                                          |

---

## Gate Summary

| Gate  | Check                              | Result      | Score/Status                                      |
| ----- | ---------------------------------- | ----------- | ------------------------------------------------- |
| QG-1  | Hook Strength                      | **PASS**    | 9.0/10 (threshold: 7.0)                           |
| QG-2a | Story Arc (Arc1+Arc2+Arc4 avg)     | **PASS**    | 8.8/10 (threshold: 7.0; +0.5 experience bonus)    |
| QG-2b | CTA Strength (Arc3 standalone)     | **PASS**    | 9.0/10 (threshold: 7.0, independent sub-gate)     |
| QG-3  | Loop Opener Frequency              | **PASS**    | 5 found, 2 required                               |
| QG-4  | AI-Phrasing Detection              | **FAIL**    | **8 banned phrases found (B.5 contractions)**     |
| QG-5  | Narrative Flow & Direct Address    | **PASS**    | Connectors 9/10, Direct Address 2, CTA 2          |

**Overall Verdict: FAIL** — QG-4 fails on §B.5 expanded-contractions count (8 ≥ 3-instance threshold).

---

## Resolution (2026-05-08)

All 8 expanded contractions were applied inline by the orchestrator (mechanical fixes, no rewrites): `were not`→`weren't`, `Here is the twist`→`Here's the twist`, `Here is the pattern`→`Here's the pattern`, `it is the scar`→`it's the scar`, `you are right`→`you're right`, `If you have ever`→`If you've ever`, `it is specific`→`it's specific`, `Here is what this actually means`→`Here's what this actually means`. Verified via grep — zero remaining `\b(it is|you are|Here is|were not|you have)\b` hits in the script. **Final QG-4 banned-count: 0 → PASS.** All other gates already PASS. **Final overall verdict: PASS.**

---

## Action Required (FAIL recovery)

**Single blocking issue: QG-4 §B.5 expanded contractions = 8 (threshold is < 3).**

Apply the 5 mandatory natural-contraction fixes listed in Pass 5 §B.5:

1. S2: `were not code` → `weren't code`
2. S4: `it is the scar` → `it's the scar`
3. S4: `agrees you are right` → `agrees you're right`
4. S4: `If you have ever argued` → `If you've ever argued`
5. S5: `it is specific` → `it's specific`

Then contract at least **one** of the three `Here is …` loop openers (writer's pick — recommend S6 "Here is what this actually means." → "Here's what this actually means." since it lands inside the takeaway scene where rhetorical formality matters less). That brings the count from 8 → 2, clearing the < 3 threshold.

Cleanest: contract all 8. The "Here is …" trio reads fine as "Here's the twist / Here's the pattern / Here's what this actually means" — the rhetorical weight is carried by the noun phrase that follows, not by the formal "is".

After revisions, re-run: `/diy-yt-creator:phase2-5-critique claude-personal-guidance`.

**STOP** — do NOT proceed to Phase 2a until QG-4 clears.

---

## Retention Checklist (Phase 2.5 — BLOCKING)

- [x] Every body scene (S2-S6) ends with an open loop or chapter hook (S2 "Here is the twist", S3 "Now watch the trigger", S4 "this is why", S5 "And the fix generalized to other domains.", S6 "Now you know when to trust the answer, and when to push twice on purpose.")
- [x] Scene names function as curiosity-direction labels (e.g., "The pushback flip", "How Anthropic closed the loop") — confirmed in headings
- [x] WPM in range — 369 words / 147.6s = 150 WPM (within 150-165 range)
- [ ] `[PAUSE]` markers before high-impact reveals — N/A pre-TTS-script (added in Phase 2a)
