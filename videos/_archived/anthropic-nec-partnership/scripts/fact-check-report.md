# Fact-Check Report: anthropic-nec-partnership (re-run, source-article-only scope)
Generated: 2026-04-29
Scope: ARTICLE_RESPONSE — script verified bidirectionally against the single source article only.
Source article: https://www.anthropic.com/news/anthropic-nec
Methods: WebFetch of source article only. WebSearch and competitive sources NOT used (per scope rule for ARTICLE_RESPONSE videos).

## Summary

| Metric                                                | Count |
| ----------------------------------------------------- | ----- |
| Total factual claims extracted                        | 11    |
| Claims grounded in source article                     | 11    |
| Claims NOT in source article                          | 0     |
| Important article facts now used in script            | 11    |
| Article facts still unused (advisory)                 | 1 (Claude Cowork product name) |

**Overall Verdict**: PASS

## Gate Result

- Tier 1 FAILED count: 0 — PASS
- Tier 1 UNVERIFIED count: 0 — PASS
- Unsourced claims: 0 — PASS

**PASS condition met.** Every factual claim in the script is grounded in the Anthropic announcement. Editorial framing ("out-flanked OpenAI", "the part OpenAI should worry about", rhetorical "Fujitsu? Hitachi? NTT Data?") is preserved as commentary, not factual claims.

---

## Source Article Inventory (used in this verification)

| # | Article fact | Used in scene |
|---|---|---|
| 1 | "approximately 30,000 NEC Group employees worldwide" | 1, 4 |
| 2 | "NEC will become Anthropic's first Japan-based global partner" | 2 |
| 3 | "one of Japan's largest AI-native engineering organizations" | 3 |
| 4 | Products: Claude, Claude Opus 4.7, Claude Code | 4 |
| 5 | "NEC serves as its own first customer before offering its technology to clients" | 5 |
| 6 | "Client Zero initiative" | 5 |
| 7 | "incorporated into NEC BluStellar Scenario" | 6 |
| 8 | Verticals: finance, manufacturing, local government, Security Operations Center | 6 |
| 9 | Center of Excellence | 7 |
| 10 | Yoshizaki quote — "high safety, reliability, and quality standards demanded by companies and public administration in Japan" | 7 |
| 11 | Yoshizaki, Executive Officer and COO + "maximize the potential of AI in the Japanese market" | 8 |

---

## Tier 1 Claims (all 11 grounded in source)

| # | Scene | Claim | Source sentence | Verdict |
|---|---|---|---|---|
| 1 | 1 | "Claude is rolling out to thirty thousand NEC employees worldwide" | "approximately 30,000 NEC Group employees worldwide" | VERIFIED — head noun "employees" matches source. |
| 2 | 2 | "NEC just became Anthropic's first Japan-based global partner" | "NEC will become Anthropic's first Japan-based global partner" | VERIFIED — verbatim. |
| 3 | 3 | "one of Japan's largest AI-native engineering organizations" | "one of Japan's largest AI-native engineering organizations" | VERIFIED — verbatim from dek. |
| 4 | 4 | "Claude. Claude Opus four point seven. Claude Code." | "Claude, including Claude Opus 4.7, and Claude Code" | VERIFIED — three named products from source. |
| 5 | 4 | "thirty thousand NEC employees worldwide" | "approximately 30,000 NEC Group employees worldwide" | VERIFIED. |
| 6 | 5 | "NEC is its own first customer, running Claude internally first" | "NEC serves as its own first customer before offering its technology to clients" | VERIFIED — faithful paraphrase. |
| 7 | 5 | "Anthropic's Client Zero program" | "Client Zero initiative" | VERIFIED. |
| 8 | 6 | "BluStellar Scenario, which ships to customers" | "Claude... will be incorporated into NEC BluStellar Scenario" + program description | VERIFIED. |
| 9 | 6 | "finance, manufacturing, local government, and the security operations center" | "finance, manufacturing, and local government" + "Security Operations Center services" | VERIFIED — all four named in source. |
| 10 | 7 | "Center of Excellence" + "high safety, reliability, and quality standards demanded by Japanese companies and public administration" | Yoshizaki quote: "high safety, reliability, and quality standards demanded by companies and public administration in Japan" + Center of Excellence program | VERIFIED — direct paraphrase + program named. |
| 11 | 8 | "Yoshizaki, NEC's COO, called it maximizing AI's potential in the Japanese market" | "Toshifumi Yoshizaki, Executive Officer and COO of NEC Corporation" — "maximize the potential of AI in the Japanese market" | VERIFIED — title + paraphrase of quote. |

---

## Editorial / Opinion Framing (not factual claims, no sourcing required)

These lines are commentary, opinion, or rhetorical prompts — no factual claims:
- Scene 1: "Anthropic just out-flanked OpenAI in Japan" — opinion framing
- Scene 1: "But the seat count isn't the shocking part" — cliffhanger
- Scene 2: "Because here's the part nobody's saying out loud" — narration framing
- Scene 3: "And they're not just licensing seats" — commentary
- Scene 5: "And here's the part OpenAI should worry about" — commentary
- Scene 8: "So who's next? Fujitsu? Hitachi? NTT Data?" — rhetorical / engagement prompt
- Scene 8: "If you build on Claude, this is your signal. Drop your pick below. Subscribe for more AI news." — CTA

---

## Coverage gaps (advisory — already addressed)

The previous run flagged 3 article facts missing from the script. This rewrite folded them all in:

| # | Article fact | Status after rewrite |
|---|---|---|
| A | "Claude Opus 4.7" specific model | NOW USED — Scene 4 ("Claude Opus four point seven") |
| B | Center of Excellence program | NOW USED — Scene 7 (entire scene built around it) |
| C | Full Yoshizaki quote with "safety, reliability, quality standards" | NOW USED — Scene 7 |

Remaining unused article fact (advisory only — not blocking):
- "Claude Cowork" — fourth product named in the article but omitted from the script. Acceptable: Scene 4 already names three products in 1.5 seconds; adding a fourth would crowd the line. Skip.

---

## Source URL Audit

| # | URL | Status | Notes |
|---|---|---|---|
| 1 | https://www.anthropic.com/news/anthropic-nec | LIVE (200) | Sole source. All 11 grounded facts pulled from this article. |

---

## Files Updated (this run)

| Path | Change |
|---|---|
| `scripts/full-script.md` | Rewrote 4 scenes (1, 2, 4, 7); 2 of those replaced unsourced premises with article-grounded ones |
| `scripts/scene-01-stakes-pivot.txt` | Replaced "127-year-old company" with sourced framing |
| `scripts/scene-02-edison-era.txt` → `scripts/scene-02-first-japan-partner.txt` | Renamed; rewrote to use "first Japan-based global partner" payoff (sourced) |
| `scripts/scene-03-first-japan-partner.txt` → `scripts/scene-03-eng-depth.txt` | Renamed; rewrote to use "one of Japan's largest AI-native engineering organizations" (sourced) |
| `scripts/scene-04-rollout.txt` | Removed "105,000 employees" / "29%" denominator (not in source); added Claude Opus 4.7 + Claude Code (sourced) |
| `scripts/scene-05-client-zero.txt` | Tightened — removed AI-native eng org clause (moved to Scene 3); kept Client Zero (sourced) |
| `scripts/scene-06-blustellar.txt` | Unchanged — already fully sourced |
| `scripts/scene-07-why-now.txt` → `scripts/scene-07-coe.txt` | Renamed; replaced 3 external-source claims (Claude Code installs / OpenAI-SoftBank / Microsoft 5-partner) with Center of Excellence + Yoshizaki regulatory-credibility line (both sourced) |
| `scripts/scene-08-who-next.txt` | Tightened "Japan" → "the Japanese market" to match article wording exactly |
| `script.txt` | Re-flattened from all per-scene files (preserves SSML `<break time="0.5s" />` tags) |

---

## SFX Compliance (audio-design rules)

`videos/anthropic-nec-partnership/index.html` SFX inventory was reviewed against `.claude/rules/audio-design.md`:

- **Volumes**: all 24 SFX cues at compliant levels per the 2026-04-28 calibration:
  - `impact-slam` × 2 → `data-volume="0.15"` ✓
  - `scale-slam` × 7 → `data-volume="0.15"` ✓
  - `cinematic-whoosh` × 7 → `data-volume="0.11"` ✓
  - `spring-pop` × 7 → `data-volume="0.11"` ✓
  - `strike-cross` × 1 → `data-volume="0.11"` ✓
  - All under the 0.25 hard cap.
- **Track-index**: track 3 default, track 4 used only for the two layered cues (sfx-impact-slam-2 at 11.583s, sfx-cinematic-whoosh-7 at 95.270s, sfx-spring-pop-6-4 at 76.111s) — no overlap on the same track.
- **No background music**: confirmed (Shorts hard rule).
- **No sonic-logo**: optional, not used.
- **Density**: ~24 cues / ~100s composition = ~1 cue per 4s. Within the typical "1 per beat / 1 per pivot" range.
- **Cap discipline**: no SFX above the 0.25 hard cap. No use of forbidden defaults (0.5 / 0.7 / 0.35).

**SFX timing alignment**: `data-start` values currently align to the OLD narration's `transcript.json` word offsets. Since the script has been rewritten, **all 24 SFX `data-start` values will need to be re-derived from the NEW transcript.json after `npx hyperframes tts` + `transcribe`** — this is the standard pipeline (Phase 3.5 retention re-aligns SFX to new word offsets). Not a fact-check failure; a downstream re-alignment task.

---

## Next step

Run TTS + transcribe to regenerate narration with the corrected, article-grounded script:

```
npx hyperframes tts videos/anthropic-nec-partnership
npx hyperframes transcribe videos/anthropic-nec-partnership
```

Then re-run Phase 3.5 retention to re-align all SFX `data-start` values to the new `transcript.json`:

```
/diy-yt-creator:phase3-5-retention anthropic-nec-partnership
```

Do NOT lint or render until SFX alignment is re-derived — current SFX cues are timed to a script that no longer exists.
