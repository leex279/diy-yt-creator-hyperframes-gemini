---
description: "Phase 2b — Fact-check all claims, stats, quotes, and sources before TTS generation"
argument-hint: <slug>
allowed-tools: Bash, Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

<objective>
Execute Phase 2b of the HyperFrames pipeline.

**Goal**: Verify every factual claim in the script before spending money on TTS audio generation. Zero tolerance for unverified statistics, misattributed quotes, or dead source links.

**Inputs**:
  - `videos/<slug>/scripts/full-script.md` (raw script with stats/claims)
  - `videos/<slug>/scripts/scene-NN-<name>.txt` (TTS-optimized scene files)
  - `videos/<slug>/script.txt` (flat narration — gets re-flattened if auto-correction applies)
  - `videos/<slug>/research/content-brief.md` (proof points table with source URLs)

**Output**: `videos/<slug>/scripts/fact-check-report.md`

**Gate condition**: All CRITICAL claims must be VERIFIED or CORRECTED. Zero FAILED verdicts in Tier 1. Zero broken Tier 1 source URLs.
</objective>

<autonomous-mode>
## When called from /diy-yt-creator:full-auto

Run all steps automatically. Use WebSearch for every claim. If `PERPLEXITY_API_KEY` is set in `.env` AND `scripts/perplexity-verify.py` exists, also run Perplexity deep-verify. (Neither is set up in this project today — Perplexity branch will silently skip.) If all Tier 1 claims pass, return control to the orchestrator. If any Tier 1 claim fails, STOP orchestration and report the specific failures with corrections.
</autonomous-mode>

<process>

### Phase Gate

Read `videos/<slug>/phase-status.md`.
- **Prerequisites**: Verify `2a - TTS Script` is `done`.
  - If not: STOP and report "Phase 2a (TTS Script) has not run. Run `/diy-yt-creator:phase2a-tts-script <slug>` first."
- **Re-run check**: If `2b - Fact Check` is already `done`, warn the user before overwriting. In autonomous mode, skip the warning and proceed.

---

## Step 1 — Extract All Factual Claims

Read these files:
1. `videos/<slug>/scripts/full-script.md` — the narrative script
2. `videos/<slug>/research/content-brief.md` — proof points table with sources
3. All `videos/<slug>/scripts/scene-NN-*.txt` files — final TTS scripts

### Claim Extraction Rules

Scan every sentence for factual claims. A "claim" is any statement that could be independently verified as true or false.

**Tier 1 — CRITICAL (must verify, blocks gate)**:
- Statistics with numbers ("24 million secrets", "40% higher", "$4.67M average cost")
- Direct quotes attributed to named people ("Jensen Huang said...", "Andrej Karpathy wrote...")
- Financial/legal data (costs, fines, breach amounts)
- Security/safety claims that could cause harm if wrong
- Year-specific data ("in 2024", "as of 2025")

**Tier 2 — IMPORTANT (must verify, advisory warning if unverified)**:
- Product feature claims ("supports X", "works with Y", "includes Z")
- Version numbers and release dates ("v2.3 released in March")
- Comparative claims ("faster than X", "more secure than Y")
- Market position claims ("most popular", "industry standard")
- GitHub stars, downloads, contributor counts (change rapidly)

**Tier 3 — CONTEXTUAL (best-effort verification, advisory only)**:
- General technical descriptions ("React uses a virtual DOM")
- Well-known historical facts ("Docker launched in 2013")
- Industry consensus ("microservices improve scalability")

### Output format for extraction

```
| # | Claim Text | Tier | Scene | Source URL (from brief) | Verification Method |
```

Report total: "Found X claims: Y Tier 1, Z Tier 2, W Tier 3"

---

## Step 2 — Verify Claims

### Method A: WebSearch (ALWAYS — for every Tier 1 and Tier 2 claim)

For each Tier 1 and Tier 2 claim:

1. **Search with year filter**: Always include the current year or the year claimed in the search query. Never trust training data alone for statistics.
   - Example: `"GitHub secret scanning 2024 statistics"`, `"IBM data breach cost 2025 report"`
2. **Cross-reference minimum 2 sources**: A single search result is not sufficient for Tier 1 claims. Find at least 2 independent sources that agree.
3. **Prefer primary sources**: Official reports, press releases, earnings transcripts, and documentation over blog posts or news articles.
4. **Check recency**: If the claim says "2024" but the best source is from 2023, flag as STALE.
5. **Verify exact numbers**: "nearly 24 million" vs "23.8 million" — the script can round, but the underlying number must be correct.

### Method B: Perplexity API (OPTIONAL — skipped in this project)

This project does NOT currently have:
- `PERPLEXITY_API_KEY` configured in `.env`
- `scripts/perplexity-verify.py` (only `scripts/sync-shared-assets.sh` and `scripts/measure-logo.cjs` exist)

Probe both. If either is missing, **silently skip** Method B. Do NOT fail the phase. Log: "Perplexity API not configured — using WebSearch only."

If both ever exist later (someone adds the key + script), invoke as `python scripts/perplexity-verify.py <slug>` and merge results into the report. Do not implement the script as part of Phase 2b.

### Method C: URL Liveness Check (for all source URLs in content-brief)

For every URL listed in the content-brief's Proof Points table:
1. Use `WebFetch` to check if the URL returns a 200 response
2. Verify the page content actually supports the claimed statistic
3. Flag dead links (404, 403, timeout) as BROKEN_SOURCE

### Method D: Technical Accuracy Spot-Check

For claims about specific tools, libraries, or APIs:
1. Check official documentation via WebSearch
2. Verify feature claims match current version (not deprecated/removed)
3. Check that any code/CLI examples in the script are syntactically valid

---

## Step 3 — Render Verdicts

For each claim, assign one verdict:

| Verdict           | Meaning                                          | Action Required                                       |
| ----------------- | ------------------------------------------------ | ----------------------------------------------------- |
| **VERIFIED**      | Claim confirmed by 2+ sources                    | None                                                  |
| **CORRECTED**     | Claim was slightly wrong, fix applied            | Script update needed                                  |
| **STALE**         | Claim uses outdated data, newer data available   | Script update needed                                  |
| **UNVERIFIED**    | Could not confirm or deny                        | Tier 1: BLOCKS gate / Tier 2: Warning                 |
| **FAILED**        | Claim is demonstrably false                      | Script update REQUIRED                                |
| **BROKEN_SOURCE** | Source URL is dead or doesn't support claim      | Replace URL needed                                    |

### Correction Protocol

When a claim is CORRECTED or STALE:
1. Record the original claim text
2. Record the corrected value with source
3. Provide the exact replacement text for the script
4. Note which scene file(s) need updating

---

## Step 4 — URL & Resource Audit

Read `videos/<slug>/research/content-brief.md` and extract all URLs from:
- Proof Points source URLs
- Any "Resources" or "Links" sections
- Referenced documentation, blog posts, reports

For each URL:
1. **Liveness**: Does it resolve? (`WebFetch`)
2. **Relevance**: Does the page content match what it's cited for?
3. **Recency**: Is there a newer version of this resource?
4. **Primary vs Secondary**: Is this the original source or a secondary blog post? Flag secondary sources and suggest the primary.

---

## Step 5 — Auto-correction (full-auto mode only)

When running under `/diy-yt-creator:full-auto` AND corrections are minor (rounding, date updates, URL swaps):

1. Apply corrections directly to the per-scene `.txt` files affected
2. **CRITICAL**: After editing any per-scene `.txt`, re-flatten the narration into `videos/<slug>/script.txt`. Concatenate all per-scene narration text (strip break tags and `[PAUSE]` markers, preserve paragraph breaks) and overwrite `script.txt`. This keeps the existing `npx hyperframes tts` pipeline in sync. Without this step, the flat `script.txt` and per-scene `.txt` files diverge — TTS generates audio for the OLD content while the captions/transcript downstream use the NEW content.
3. Log every change in the report under "Auto-Applied Corrections"
4. Do NOT re-run Phase 2a TTS optimization for minor edits — pronunciation is unaffected
5. Return control to the orchestrator

When corrections are major (wrong statistic, misattributed quote, false claim):
1. STOP orchestration
2. Report the failure with exact issues
3. User must review and approve before continuing

In **interactive mode** (not full-auto), do NOT auto-edit. Present corrections to the user; they apply them manually.

---

## Step 6 — Generate Fact-Check Report

</process>

<output>

### Report Structure

Save to: `videos/<slug>/scripts/fact-check-report.md`

```markdown
# Fact-Check Report: <slug>
Generated: [DATE]
Verification methods: WebSearch [+ Perplexity API if available]

## Summary

| Metric                    | Count |
| ------------------------- | ----- |
| Total claims extracted    | N     |
| Tier 1 (Critical)         | N     |
| Tier 2 (Important)        | N     |
| Tier 3 (Contextual)       | N     |
| VERIFIED                  | N     |
| CORRECTED                 | N     |
| STALE                     | N     |
| UNVERIFIED                | N     |
| FAILED                    | N     |
| Source URLs checked       | N     |
| Broken sources            | N     |

**Overall Verdict**: PASS / FAIL

## Gate Result

- Tier 1 FAILED count: N (must be 0 to pass)
- Tier 1 UNVERIFIED count: N (must be 0 to pass)
- Broken critical sources: N

**PASS condition**: Zero Tier 1 FAILED + Zero Tier 1 UNVERIFIED + Zero broken Tier 1 sources

## Tier 1 Claims (Critical)

| #   | Scene    | Claim                                       | Verdict   | Sources                                | Notes                |
| --- | -------- | ------------------------------------------- | --------- | -------------------------------------- | -------------------- |
| 1   | Scene 02 | "23.8M secrets leaked on GitHub in 2024"    | VERIFIED  | [GitGuardian 2025 Report](url)         | Exact match          |
| 2   | Scene 03 | "70% of leaked secrets still valid"         | CORRECTED | [GitGuardian](url)                     | Was "70%", actual is "69%" — rounded OK |

## Tier 2 Claims (Important)

| #   | Scene | Claim | Verdict | Sources | Notes |
| --- | ----- | ----- | ------- | ------- | ----- |

## Tier 3 Claims (Contextual)

| #   | Scene | Claim | Verdict | Sources | Notes |
| --- | ----- | ----- | ------- | ------- | ----- |

## Source URL Audit

| #   | URL          | Status        | Supports Claim? | Notes              |
| --- | ------------ | ------------- | --------------- | ------------------ |
| 1   | https://...  | LIVE          | Yes             | Primary source     |
| 2   | https://...  | BROKEN (404)  | N/A             | Need replacement   |

## Auto-Applied Corrections (full-auto mode)

If any minor corrections were applied, list each:

### Correction 1: [Scene NN]
- **Original**: "24 million secrets were leaked in 2024"
- **Corrected**: "23.8 million secrets were leaked in 2024"
- **Source**: [GitGuardian State of Secrets Sprawl 2025](url)
- **Files updated**: `videos/<slug>/scripts/scene-02-problem.txt` AND `videos/<slug>/script.txt` (re-flattened)
- **Impact**: Minor rounding — acceptable as "nearly 24 million" in spoken script

## Stale Data Warnings

List any claims using data older than 12 months where newer data exists.

## Corrections Required (manual)

For interactive mode, list every correction the user needs to apply manually.
```

### Gate Decision

**On PASS** (zero Tier 1 FAILED, zero Tier 1 UNVERIFIED):

All critical claims verified. Script is factually sound.

If corrections were applied: list the specific changes made AND confirm `script.txt` was re-flattened.
If Tier 2 warnings exist: list as advisories but do not block.

Next step (in autonomous orchestration): the orchestrator pauses here and prompts the user to run:
```
npx hyperframes tts videos/<slug>
npx hyperframes transcribe videos/<slug>
```
After both succeed (producing `audio/narration.wav` and `transcript.json`), the orchestrator resumes with Phase 3.5.

In standalone mode: tell the user the same — run TTS + transcribe, then `/diy-yt-creator:phase3-5-retention <slug>`.

**On FAIL** (any Tier 1 FAILED or UNVERIFIED):

STOP. Do NOT proceed.

Numbered list of blocking issues:
1. Which claim failed, in which scene
2. What the correct information is (with source)
3. Exact replacement text for the script

After corrections, re-run: `/diy-yt-creator:phase2b-factcheck <slug>`

### Update Phase Status

Update `videos/<slug>/phase-status.md`:
- If all gates **PASS**: set the `2b - Fact Check` row to `done (N/N claims verified) <YYYY-MM-DD>`.
- If any gate **FAILS**: set the `2b - Fact Check` row to `blocked (N failed claims) <YYYY-MM-DD>`.

## C-08 Hard Rule: Fail-Fast on Unsourced Claims

If this Phase 2b fact-check finds ANY unsourced direct quote or unverified statistic, STOP the workflow and report the issues to the user. DO NOT proceed to TTS audio generation. Audio generation is the point of no return — once narration is rendered, every fact-check failure becomes a content-integrity bug that requires a full re-run.

Output format on failure:
- List each unverified claim with the exact line in the script
- Suggest: "Remove" / "Rephrase as paraphrase with attribution" / "Find source URL"
- Halt with exit-style message: `FACT-CHECK FAILED: N unverified claims. TTS generation BLOCKED.`
</output>
