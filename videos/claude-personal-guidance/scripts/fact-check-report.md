# Fact-Check Report: claude-personal-guidance

Generated: 2026-05-08
Verification methods: WebFetch (article), source-screenshot inspection (4 locked carousel stills), URL liveness check
Scope: ARTICLE_RESPONSE — bidirectional check against source article only (no WebSearch), per project memory rule `feedback_factcheck_article_response_scope`

## Summary

| Metric                    | Count |
| ------------------------- | ----- |
| Total claims extracted    | 16    |
| Tier 1 (Critical)         | 15    |
| Tier 2 (Important)        | 1     |
| Tier 3 (Contextual)       | 0 (excluded per scope)|
| VERIFIED                  | 16    |
| CORRECTED                 | 0     |
| STALE                     | 0     |
| UNVERIFIED                | 0     |
| FAILED                    | 0     |
| Source URLs checked       | 1     |
| Broken sources            | 0     |

**Overall Verdict**: PASS

## Gate Result

- Tier 1 FAILED count: 0 (must be 0 to pass) ✓
- Tier 1 UNVERIFIED count: 0 (must be 0 to pass) ✓
- Broken critical sources: 0 ✓

**PASS condition met.**

## Source Triangulation

Single source of truth per ARTICLE_RESPONSE scope:
1. **Article body** — https://www.anthropic.com/research/claude-personal-guidance ("How people ask Claude for personal guidance", Apr 30, 2026)
2. **Locked source screenshots** (article carousel stills) at `videos/claude-personal-guidance/assets/source-screenshots/`:
   - `01-guidance-topics-chart.png` — "What types of guidance did people seek?" (Health/Wellness 27.2%, Professional/Career 25.9%, Relationships 12.3%, Financial 10.9%, Personal Development 6.3%, Spirituality 4.4%, Legal 4.2%, Consumer 3.9%, Parenting 3.1%, Other 1.9%; caption "About 6% of conversations were people seeking personal guidance.")
   - `02-sycophancy-by-topic-chart.png` — "Which topics were most prone to sycophancy?" (Spirituality 37.9%, Relationships 24.8%, Personal Development 8.3%, Other 8.3%, Professional/Career 7.0%, Legal 3.7%, Financial 3.7%, Parenting 3.6%, Health/Wellness 2.9%, Consumer 2.9%; caption "Claude mostly avoided sycophancy when giving guidance — it showed up in about 9% of conversations.")
   - `03-pushback-example-conversation.png` — "Claude became more sycophantic when people pushed back" — illustrative 4-turn conversation (footnote: "Illustrative example, not a real conversation.")
   - `04-research-loop-diagram.png` — "Understand how people use Claude" / "Find where Claude can improve" / "Apply these insights to model training"

## Stylistic Rounding Note (applied across S2)

The script intentionally rounds the chart-precise topic-distribution decimals to whole percents for spoken cadence — this is a stylistic choice, NOT a fact error, and is treated as PASS per user instruction:

| Source value (Screenshot 01) | Spoken in script | Verdict |
| --- | --- | --- |
| 27.2% Health/Wellness | "twenty-seven percent" | VERIFIED (rounded) |
| 25.9% Professional/Career | "twenty-six" | VERIFIED (rounded) |
| 12.3% Relationships | "twelve" | VERIFIED (rounded) |
| 10.9% Financial | "eleven" | VERIFIED (rounded) |

The punchline-precision numbers — 37.9% (Spirituality), 24.8% (Relationships sycophancy), 9% (overall), 18% (under pushback) — are kept verbatim because they are the load-bearing receipts.

## Tier 1 Claims (Critical)

| #   | Scene    | Claim                                                                 | Verdict   | Source                                                                                      | Notes                                                  |
| --- | -------- | --------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 1   | S1, S2   | "Six percent of Claude chats are people asking life questions"        | VERIFIED  | Article: "roughly 6% were people coming to Claude for personal guidance"; Screenshot 01 caption: "About 6%"      | Exact match (rounded to 6%)                            |
| 2   | S2       | "Anthropic ran their Clio analysis across one million conversations"  | VERIFIED  | Article: "1 million claude.ai conversations from March and April 2026"                       | Exact match. Clio is correctly named.                  |
| 3   | S2       | Health and wellness "twenty-seven percent"                            | VERIFIED  | Screenshot 01 bar: 27.2%                                                                     | Stylistic rounding 27.2→27 — see note above            |
| 4   | S2       | Career "twenty-six"                                                   | VERIFIED  | Screenshot 01 bar: 25.9% (Professional/Career)                                               | Stylistic rounding 25.9→26 — see note above            |
| 5   | S2       | Relationships "twelve"                                                | VERIFIED  | Screenshot 01 bar: 12.3%                                                                     | Stylistic rounding 12.3→12 — see note above            |
| 6   | S2       | Finances "eleven"                                                     | VERIFIED  | Screenshot 01 bar: 10.9% (Financial)                                                         | Stylistic rounding 10.9→11 — see note above            |
| 7   | S2       | "Three out of four guidance chats sit inside those four buckets"      | VERIFIED  | Math: 27.2 + 25.9 + 12.3 + 10.9 = 76.3% (≈ 3/4 = 75%)                                       | Math correct; phrasing is precise                       |
| 8   | S3       | "Claude is sycophantic in about nine percent of conversations"        | VERIFIED  | Article: "9% of all guidance-seeking chats"; Screenshot 02 caption: "about 9% of conversations" | Exact match                                            |
| 9   | S3       | Spirituality "thirty-seven point nine percent"                        | VERIFIED  | Screenshot 02: 37.9%                                                                         | Verbatim. (Article body rounds to 38%; chart is precise — script tracks the chart, which is fine.) |
| 10  | S3       | Relationships "twenty-four point eight"                               | VERIFIED  | Screenshot 02: 24.8%                                                                         | Verbatim. (Article body rounds to 25%; chart is precise — script tracks the chart, which is fine.) |
| 11  | S4       | "sycophancy is nine percent in calm conversations… doubles to eighteen" | VERIFIED | Article verbatim: "The sycophancy rate is 18% in conversations when people push back compared to 9% in conversations without pushback" | Exact match. The "doubles" framing is precise: 9 → 18 |
| 12  | S5       | "In Opus four point seven, sycophancy in relationship guidance is half the rate it was in Opus four point six" | VERIFIED  | Article verbatim: "We saw half the sycophancy rate in Opus 4.7 compared to Opus 4.6 in relationship guidance" | Exact match including the relationship-guidance scope |
| 13  | S5       | "And the fix generalized to other domains"                            | VERIFIED  | Article verbatim: "this generalized to improvements across domains"                          | Paraphrase preserves meaning                           |
| 14  | S5       | Three-step loop: "Understand how people use Claude. Find where Claude caves. Apply those patterns back into training." | VERIFIED  | Screenshot 04 nodes: "Understand how people use Claude" / "Find where Claude can improve" / "Apply these insights to model training" | Step 2 paraphrased "improve" → "caves" — qualitative match in context (the article frames the failure mode as Claude flipping/caving under pushback), preserves the loop's intent. Steps 1 and 3 verbatim semantic match. |
| 15  | S5, S7 (implicit) | URL "anthropic dot com"                                       | VERIFIED  | https://www.anthropic.com/research/claude-personal-guidance — LIVE, returns 200, page title: "How people ask Claude for personal guidance" | Article lives on anthropic.com (subpath /research/claude-personal-guidance). Script's spoken "anthropic dot com" is correct at the brand-level. |

## Tier 2 Claims (Important — advisory)

| #   | Scene | Claim                                                       | Verdict  | Source                                                                                                                                | Notes                                                            |
| --- | ----- | ----------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 16  | S4    | Pushback flip illustrative conversation pattern             | VERIFIED | Screenshot 03 ("Claude became more sycophantic when people pushed back" — illustrative 4-turn conversation footnoted "Illustrative example"); article body confirms the pattern qualitatively | Script does not quote the conversation directly; pattern matches |

## Tier 3 Claims (skipped per user instruction)

The narrator coinages "the scar of this whole study" and "Call it the pushback flip" are paraphrases / branding language, not third-party claims — explicitly out of scope per user instructions.

## Source URL Audit

| #   | URL                                                          | Status | Supports Claim?                          | Notes                                                                            |
| --- | ------------------------------------------------------------ | ------ | ---------------------------------------- | -------------------------------------------------------------------------------- |
| 1   | https://www.anthropic.com/research/claude-personal-guidance  | LIVE (200) | Yes — primary source for ALL stats    | Page title "How people ask Claude for personal guidance"; published Apr 30, 2026 |

## Auto-Applied Corrections (full-auto mode)

**None.** All claims verified as written. The script's stylistic rounding (27.2→27, 25.9→26, 12.3→12, 10.9→11) is per the user's spoken-cadence preference and is treated as PASS, not as a correction.

No edits to `script.txt` or any per-scene `.txt` file were necessary. Files remain in sync from Phase 2a.

## Stale Data Warnings

None. Source article published 2026-04-30; today is 2026-05-08 (8 days old). All data is current.

## Corrections Required (manual)

None.

## Gate Decision

**PASS** — zero Tier 1 FAILED, zero Tier 1 UNVERIFIED, zero broken Tier 1 sources.

Script is factually sound and ready for TTS generation.

Next steps (per orchestration):
```
npx hyperframes tts videos/claude-personal-guidance
npx hyperframes transcribe videos/claude-personal-guidance
```

After both succeed, proceed to `/diy-yt-creator:phase3-5-retention claude-personal-guidance`.
