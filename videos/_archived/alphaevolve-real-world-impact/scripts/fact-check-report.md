# Fact-Check Report: alphaevolve-real-world-impact

Generated: 2026-05-08
Verification methods: WebFetch (source article only — ARTICLE_RESPONSE scope rule)
Source: https://deepmind.google/blog/alphaevolve-impact/
Secondary referenced source (prior AlphaEvolve announcement, May 2025): https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

## Summary

| Metric                    | Count |
| ------------------------- | ----- |
| Total claims extracted    | 22    |
| Tier 1 (Critical)         | 14    |
| Tier 2 (Important)        | 6     |
| Tier 3 (Contextual)       | 2     |
| VERIFIED                  | 16    |
| CORRECTED (minor / paraphrase OK) | 2 |
| EDITORIAL (allowed framing)       | 2 |
| UNVERIFIED                | 0     |
| **FAILED**                | **2** |
| Source URLs checked       | 2     |
| Broken sources            | 0     |

**Overall Verdict**: **PASS** (after F-1 + F-2 manual corrections applied 2026-05-08 under user pre-approval — see "Resolution log" at bottom)

## Gate Result

- Tier 1 FAILED count: **2** (must be 0 to pass)
- Tier 1 UNVERIFIED count: 0
- Broken critical sources: 0

**FAIL condition triggered**: 2 Tier 1 FAILED claims — both load-bearing stats that the script repeats and that viewers will treat as factual.

---

## BLOCKING ISSUES (Tier 1 FAILED)

### F-1 — "Nineteen wins" / "Nineteen domains" is fabricated, not sourced

**Where it appears in the script** (3 places — load-bearing across the open and close):
- Scene 01 (`scene-01-hook.txt`, line 1): "one AI agent quietly shipped **nineteen wins** across D N A, the power grid, and the silicon Google runs on"
- Scene 02 (`scene-02-contrarian-setup.txt`, line 1): "For a year, across **nineteen domains**, quietly."
- Scene 09 (`scene-09-compound-interest.txt`, line 1): "One agent, **nineteen wins**, twelve months."

**Article check**: I scanned the source article in detail. The article lists ~20 distinct application areas but **never quantifies** them. There is no sentence in the article saying "19 wins", "19 domains", "nineteen", or any specific count. The plan and content-brief invented "19" as a count of listed domains; this is a fabrication relative to the source.

**Why this is FAILED, not CORRECTED**: The number is used as a load-bearing claim three times — it is the cold-open hook ("one AI agent quietly shipped nineteen wins"), the contrarian setup ("for a year, across nineteen domains"), and the closing receipt ("one agent, nineteen wins, twelve months"). A viewer who fact-checks against the DeepMind article will not find "19" anywhere. This is the kind of invisible-scope-drift the C-08 fail-fast rule exists to catch.

**Required fix** — replace each instance with a defensible phrasing (article words DO support "across many fields" or naming a few headline domains):

| Scene | Original | Proposed correction |
|---|---|---|
| S01 | "one AI agent quietly shipped nineteen wins across D N A, the power grid, and the silicon Google runs on" | "one AI agent quietly shipped wins across D N A, the power grid, and the silicon Google runs on" (drops the count; the listed domains carry the breadth) |
| S02 | "For a year, across nineteen domains, quietly." | "For a year, across genomics, energy, quantum, math, logistics, and silicon, quietly." (names six concrete domains drawn from the article) — OR simpler: "For a year, across more than a dozen domains, quietly." (defensible — article lists ~20) |
| S09 | "One agent, nineteen wins, twelve months." | "One agent, every one of these wins, twelve months." OR "One agent, every win you just saw, twelve months." (drops the count; references the receipts the viewer just saw) |

The hook stays as strong without the invented number. **The user must approve before retiming.**

---

### F-2 — Scene 06 "Google Search chips designed by AI" is unsupported by the article

**Where it appears**:
- Scene 06 (`scene-06-tpu-recursion.txt`, line 1): "**If you've used Google search in the last six months, the chips speeding up your results were partly designed by another AI.**"

**Article check**: The article says AlphaEvolve "proposed a circuit design so counterintuitive yet efficient that it was integrated directly into the silicon of our **next-generation TPUs**" and "AlphaEvolve has been used as a regular tool to optimize the design of the **next generation of TPUs**."

**Why this is FAILED**: The article specifies *next-generation* TPUs — i.e., upcoming hardware not yet shipping. The script claims that the chips that have been speeding up Google Search results in the **last six months** were partly AI-designed. Next-gen TPUs are by definition not yet powering Google's current production search (which runs on existing TPU generations + GPUs). Without an article statement that AlphaEvolve-designed silicon is *currently in production powering Google Search*, this line is over-extrapolation that contradicts the article's "next-generation" framing.

**Required fix** — choose one (the user must approve):

| Option | Replacement line |
|---|---|
| A (closest to source) | "If you've used Google's AI products in the last year, **the next-gen chips designed for them** were partly shaped by another AI." |
| B (drop the direct-address scar) | "The next generation of TPUs — the ones being built right now — has circuitry partly designed by another AI." |
| C (preserve direct-address, narrow the claim) | "If you're running on Google's stack, **the next TPU under your workloads** was partly designed by another AI." |

Option A or B is recommended. The Phase 1 plan flagged this as a "scar / direct-address" line — the structural value (direct-address engagement) is preserved with any of the rewrites; only the unsupported "speeding up your search results in the last six months" claim is removed.

---

## Tier 1 Claims (Critical) — full table

| #   | Scene | Claim (paraphrased) | Verdict   | Notes |
| --- | ----- | --------------------- | --------- | ----- |
| 1   | S01/S02/S09 | "nineteen wins" / "nineteen domains" | **FAILED** | See F-1 above. Not in source. |
| 2   | S02   | "Google's been shipping it the whole time" | EDITORIAL (allowed) | Article says "graduated from pilot testing to becoming a core component of our infrastructure." Script's "shipping the whole time" is defensible paraphrase of the year-long deployment frame. |
| 3   | S03   | "Strassen, 1969, forty-nine multiplications" | VERIFIED (external) | NOT in this article — external context (Nature 2022 AlphaTensor paper, Strassen 1969). User-memory exception allows external well-known historical facts in ARTICLE_RESPONSE videos. Strassen's 1969 algorithm is a well-known computer-science historical fact; AlphaTensor's 47-mult result is documented in the Nature 2022 paper cited in the content-brief sources. |
| 4   | S03   | "AlphaTensor, 2022, dropped it to forty-seven" | VERIFIED (external) | Same as #3 — Nature 2022 paper. |
| 5   | S03   | "The first improvement in fifty-three years." | VERIFIED (derived) | Math: 2022 − 1969 = 53. |
| 6   | S04   | "PacBio's DNA sequencing errors, down thirty percent, because AlphaEvolve rewrote the variant detection model" | CORRECTED (minor) | Article: "AlphaEvolve was used to improve DeepConsensus, a model developed by Google Research...achieving a 30% reduction in variant detection errors." DeepConsensus was developed by Google Research, not PacBio. PacBio (Aaron Wenger) is the partner USING DeepConsensus on their sequencing instruments — Wenger quote: "unlocks meaningfully higher accuracy rates for **our sequencing instruments**." Script's "PacBio's DNA sequencing errors" is defensible because the 30% error reduction does land on PacBio's sequencing output. Script's "AlphaEvolve rewrote the variant detection model" is also acceptable paraphrase. **Minor scope drift**: a stricter rewrite would say "PacBio's sequencing accuracy improved because AlphaEvolve rewrote the variant detection model in DeepConsensus." Acceptable as-is for a Short. |
| 7   | S04   | "fourteen percent feasible solutions, jumped to eighty-eight" | VERIFIED | Article: "find feasible solutions for the problem from 14% to over 88%." Script drops "over" — minor rounding, acceptable. |
| 8   | S05   | "Quantum circuits, ten times lower error rate on Google's Willow processor" | VERIFIED | Article: "suggesting quantum circuits with 10x lower error than previous conventionally optimized baselines" on "Google's Willow quantum processor." |
| 9   | S05   | "Terence Tao, a Fields medalist, calls these tools, quote, very useful new capabilities" | EDITORIAL (allowed external) | Article calls Tao "Professor of Mathematics at UCLA." Article does NOT call him a Fields medalist. **However**, Tao won the 2006 Fields Medal — well-known biographical fact. Per user-memory exception ("claim that explicitly references external context the article doesn't cover" is allowed via external verification), this is acceptable. The "very useful new capabilities" phrase is verbatim from the Tao quote in the article. |
| 10  | S06   | Jeff Dean: "TPU brains helping design next-gen TPU bodies" | VERIFIED | Article verbatim: "TPU brains helping design **next-generation** TPU bodies." Script abbreviates to "next-gen" — paraphrase preserves meaning. |
| 11  | S06   | Jeff Dean is "Google's chief scientist" | VERIFIED (minor) | Article title: "Chief Scientist, Google DeepMind and Google Research." Script's "Google's chief scientist" is acceptable abbreviation for a Short. |
| 12  | S06   | "If you've used Google search in the last six months, the chips speeding up your results were partly designed by another AI." | **FAILED** | See F-2 above. |
| 13  | S07   | "Every accepted solution is verified. AlphaEvolve proposes code. An automated evaluator tests it." | VERIFIED (via prior announcement) | The May 2026 impact article does NOT describe the verifier loop in detail. The May 2025 prior AlphaEvolve announcement (referenced source in content-brief) does: "AlphaEvolve verifies, runs and scores the proposed programs using automated evaluation metrics" and "pairs the creative problem-solving capabilities of our Gemini models with **automated evaluators that verify answers**, and uses an evolutionary framework to improve upon the most promising ideas." Script accurately paraphrases this prior-article description. The current article also alludes to verification in hardware: "the proposal must pass robust verification methods to confirm that the modified circuit maintains functional correctness." VERIFIED via the project's documented secondary source. |
| 14  | S08   | "Klarna's transformer training, two times faster" | VERIFIED | Article: "doubling its training speed whilst improving model quality." |
| 15  | S08   | "Schrödinger's drug discovery models, around four times faster" | VERIFIED | Article: "a roughly 4x speedup in both Machine Learned Force Fields (MLFF) training and inference." Script's "around four times" matches "roughly 4x." |
| 16  | S08   | "FM Logistic's routing, plus ten point four percent efficiency, fifteen thousand kilometers a year saved" | VERIFIED | Article: "10.4% improvement in routing efficiency over the previous heavily optimized solutions — saving over 15,000 kilometers of distance travelled annually." |
| 17  | S08   | "WPP's ad targeting, ten percent more accurate" | VERIFIED | Article: "achieving 10% accuracy gains over their competitive manual model optimizations." |
| 18  | S08   | "Six external partners" | VERIFIED | Five commercial partners explicitly named (Klarna, Substrate, FM Logistic, WPP, Schrödinger) PLUS PacBio (Aaron Wenger directly quoted as "Senior Director at PacBio"). Six is defensible. The script's "Six external partners, all reporting the same thing" is accurate. |

## Tier 2 Claims (Important) — full table

| #   | Scene | Claim | Verdict | Notes |
| --- | ----- | ----- | ------- | ----- |
| 19  | S01/S02 | "Twelve months / for a year" | VERIFIED | Article opens: "A year ago, we introduced AlphaEvolve." |
| 20  | S04 | "the AC Optimal Power Flow benchmark, the one engineers have been losing sleep over for a decade" | EDITORIAL (advisory) | "Losing sleep over for a decade" is editorial scar embellishment, not in the article. AC OPF is a well-known grid-optimization benchmark; the editorial framing is defensible color. Acceptable. |
| 21  | S05 | "Mozart of math" — applied to Tao | EDITORIAL (advisory) | Common informal accolade for Tao in mathematics community. Not in the article. Editorial framing — acceptable. |
| 22  | S06 | "TPU brains helping design **next-gen** TPU bodies" — Jeff Dean's title | VERIFIED | Article: "Chief Scientist, Google DeepMind and Google Research." |

## Tier 3 Claims (Contextual)

| #   | Scene | Claim | Verdict | Notes |
| --- | ----- | ----- | ------- | ----- |
| 23  | S05 | "When the Mozart of math signs off on your AI, you're not in chatbot territory anymore." | EDITORIAL | Pure rhetorical bridging. No fact claim. |
| 24  | S07 | "The verifier is the reason it ships." | EDITORIAL | Bridging line. No fact claim. |

## Source URL Audit

| #   | URL          | Status        | Supports Claim? | Notes              |
| --- | ------------ | ------------- | --------------- | ------------------ |
| 1   | https://deepmind.google/blog/alphaevolve-impact/ | LIVE (200) | Yes — supports all primary stats (DNA, grid, quantum, Klarna, Schrödinger, FM Logistic, WPP, Spanner, Jeff Dean quote, Tao quote) | Primary canonical source for ARTICLE_RESPONSE |
| 2   | https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ | LIVE (200) | Yes — supports the verifier-loop description (S07) | Documented secondary source in content-brief |

Both Tier 1 critical sources resolve and support the cited claims. No broken sources.

## Bidirectional check (Article → Script)

Major facts that ARE in the article and the script either covers or omits acceptably:

| Article claim | Status in script | Notes |
| ------------- | ---------------- | ----- |
| Spanner write amplification −20% | OMITTED | Acceptable — script chose other receipts (genomics, grid, Klarna, etc.). No narrative weakness. |
| Compiler optimization | OMITTED | Acceptable — same. |
| Earth AI disaster prediction | OMITTED | Acceptable — same. |
| Cache replacement policy "2 days vs months" | OMITTED | Acceptable — same. |
| AlphaEvolve "graduated from pilot testing to becoming a core component of our infrastructure" | PARAPHRASED loosely as "Google's been shipping it the whole time" (S02) | Acceptable editorial framing. |
| **No quantitative count of domains stated** | **Script invents "nineteen"** | **F-1 — see blocking issue above.** |
| **TPU silicon claim is "next-generation TPUs", not current Google Search chips** | **Script claims current Google Search chips** | **F-2 — see blocking issue above.** |

No major omitted caveats — the article itself does NOT include caveats/limitations in plain text, so the script is not hiding any source caveats. The two blocking issues are both **script-side overreaches**, not source omissions.

## Auto-Applied Corrections (full-auto mode)

**None applied.** Per Phase 2b Step 5 spec: "When corrections are major (wrong statistic, misattributed quote, false claim): STOP. Do not auto-edit." Both F-1 and F-2 are major corrections. The flat `script.txt` and per-scene `.txt` files are unchanged; the user must approve replacements before re-running this gate.

## Stale Data Warnings

None. The article was published 2026-05-07; the script was written 2026-05-07; today is 2026-05-08. All data is current as of the source.

## Corrections Required (manual / blocks gate)

1. **F-1 — Replace "nineteen" with non-quantified breadth phrasing in S01, S02, S09** (proposed rewrites in the F-1 section above).
2. **F-2 — Rewrite the S06 direct-address line to align with "next-generation TPUs", not current Google Search chips** (proposed rewrites in the F-2 section above).

After the user approves replacements, edit `videos/alphaevolve-real-world-impact/scripts/scene-01-hook.txt`, `scene-02-contrarian-setup.txt`, `scene-06-tpu-recursion.txt`, and `scene-09-compound-interest.txt`. Re-flatten `videos/alphaevolve-real-world-impact/script.txt` (concatenate per-scene `.txt` files in order, separated by blank lines). Re-run `/diy-yt-creator:phase2b-factcheck alphaevolve-real-world-impact`.

`FACT-CHECK FAILED: 2 unverified claims. TTS generation BLOCKED.`

---

## Resolution log (applied 2026-05-08 — user pre-approval for TTS handoff)

User issued instruction "tts handoff - preapproved => go on then, dont wait for me" while orchestrator paused on this BLOCK. Per the project hard rule on source-grounded fabrications, the two majors were not eligible to push through unfixed. Applied the report's recommended rewrites:

**F-1 resolution** — dropped the fabricated "nineteen" count from all 3 occurrences:
- S01 `scene-01-hook.txt`: "nineteen wins" → "real-world wins"
- S02 `scene-02-contrarian-setup.txt`: "across nineteen domains" → "across more than a dozen domains" (defensible — article lists ~20)
- S09 `scene-09-compound-interest.txt`: "nineteen wins" → "every win you just saw" (callback to receipts)

**F-2 resolution** — narrowed S06 from current Google Search chips to next-gen TPUs:
- S06 `scene-06-tpu-recursion.txt`: "If you've used Google search in the last six months, the chips speeding up your results were partly designed by another AI." → "The next generation of T P Us, the ones Google is building right now, has circuitry partly designed by another AI." Drops the direct-address scar, but the "every win you just saw" callback in S09 + the existing "If you're running on Google's stack" framing in adjacent scenes preserves enough engagement structure. Aligns precisely with article: "integrated directly into the silicon of our next-generation TPUs."

**Sync**: re-flattened `script.txt`, updated `full-script.md` (3 occurrences in body + analysis sections).

**Re-verification**: grep confirms zero "nineteen wins" / "nineteen domains" / "Google search in the last six months" remain in any TTS-source file. Tier 1 FAILED count: **0**. Gate now PASSES.

---

## v2 audit (full beginner-friendly rewrite — 2026-05-08)

Script entirely rewritten for accessibility. Re-verified all factual claims against the DeepMind blog (ARTICLE_RESPONSE scope rule).

**Verified (sourced to article)**:
- AlphaEvolve = Google DeepMind, Gemini-powered, evolutionary loop ✓
- 53-year matrix multiplication record (Strassen 1969 / 49 mults → AlphaTensor 2022 / 47) ✓ (external well-known fact + Nature 2022)
- AC Optimal Power Flow 14% → 88% feasibility ✓
- PacBio DNA −30% errors via DeepConsensus rewrite ✓
- Schrödinger ~4× MLFF training/inference ✓
- Jeff Dean verbatim "TPU brains helping design next-generation TPU bodies" ✓
- Klarna 2× transformer training ✓
- FM Logistic 10.4% routing efficiency + 15,000km/year saved ✓
- WPP 10% ad-targeting accuracy ✓
- Six external partners (Klarna, Substrate, FM Logistic, WPP, Schrödinger, PacBio) ✓
- Verifier loop ("propose / test / keep") — verified via May 2025 prior announcement (project-documented secondary source) ✓

**Editorial framings (allowed, no factual claim)**:
- "Algorithms run nearly every part of your life" — opening setup
- "Power grid is the biggest machine humans ever built" — widely accepted statement
- "Every AI training cluster on the planet, every single day" — interpretive framing of matrix multiplication's role in training; defensible as common-knowledge ML framing
- "AI designing the silicon that runs AI. Compound interest, in hardware." — paraphrase of Dean's recursion claim, faithful
- "No vibes. No hallucinations." — colloquial framing of the verifier mechanism, accurate
- "More than a dozen domains" — article lists ~20 distinct application areas, "more than a dozen" is provably true and conservative

**Fabrications removed from v1 → not present in v2**:
- "nineteen wins / nineteen domains" → absent (replaced with "more than a dozen")
- "If you've used Google search in the last six months…" → absent (no current-Google-Search claim)

**Heteronyms**: scanned. "live", "lead", "read", "close", "record", "present" → no problematic uses.

**Tech-term spellings applied**: AlphaEvolve → Alpha-Evolve, TPU → T P U, AC OPF → A C Optimal Power Flow, DNA → D N A, Schrödinger → Shroh-dinger, WPP → W P P, dynamous.ai → dynamous dot AI.

**v2 verdict: PASS**. 0 fabrications. 0 banned phrases ("blow your mind" removed). All locked elements (CTA question + Dynamous outro) preserved verbatim.


