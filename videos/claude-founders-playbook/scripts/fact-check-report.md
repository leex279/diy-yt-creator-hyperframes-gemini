# Fact-Check Report: claude-founders-playbook
Generated: 2026-05-16 (re-run for 9-scene extension)
Verification methods: PDF primary-source grep (ARTICLE_RESPONSE scope) + page-marker audit
Scope rule: ARTICLE_RESPONSE — fact-check bidirectionally against `research/source-playbook.pdf` (+ `.txt`). WebSearch skipped per `feedback_factcheck_article_response_scope`.

## Re-run context

Original run (2026-05-16, 8-scene): 14/14 claims VERIFIED. PASS.
Extension run (2026-05-16, 9-scene): NEW Scene 5 "Four named killers" inserted between old S4 and old S5. Old scenes 5-8 re-numbered to 6-9. Wording of S1-S4 + S6-S9 narration unchanged — re-flatten of `script.txt` confirmed bit-identical narration for unchanged scenes. Only NEW Scene 5 needs verification.

## Summary (NEW claims only — Scene 5)

| Metric                    | Count |
| ------------------------- | ----- |
| New claims extracted      | 9     |
| Tier 1 (Critical)         | 4     |
| Tier 2 (Important)        | 4     |
| Tier 3 (Contextual)       | 1     |
| VERIFIED                  | 9     |
| CORRECTED                 | 0 (in narration) |
| STALE                     | 0     |
| UNVERIFIED                | 0     |
| FAILED                    | 0     |
| Source URLs checked       | 0 (no new URLs — Scene 5 receipt is local PDF only) |
| Broken sources            | 0     |

**Overall Verdict (extension)**: PASS
**Cumulative Verdict (14 prior + 9 new)**: PASS — 23/23 claims verified.

## Gate Result

- Tier 1 FAILED: 0
- Tier 1 UNVERIFIED: 0
- Broken critical sources: 0
- RECEIPT_AUDIT_FAIL: 0

**PASS** — all NEW Tier 1 claims verified verbatim against source PDF; auto-corrections applied to receipt provenance page numbers (no spoken-text impact).

## NEW Tier 1 Claims (Critical) — Scene 5

| # | Scene | Claim | Verdict | Source | Notes |
|---|-------|-------|---------|--------|-------|
| 15 | S5 | "Idea stage. Mistaking building for validating." | VERIFIED | source-playbook.txt line 175 — verbatim "Mistaking building for validating" as section heading under Idea-stage challenges | Exact verbatim match. Page-marker audit: line 175 sits AFTER p.9 marker (line 174) and BEFORE p.10 marker (line 214) → corresponds to **PDF p.10** (the user-provided p.9 in the receipt comment was off-by-one; auto-corrected). |
| 16 | S5 | "M V P stage. Agentic technical debt." | VERIFIED | source-playbook.txt line 392 — verbatim "Agentic technical debt" as section heading under MVP-stage challenges | Exact verbatim match. Page-marker audit: line 392 sits AFTER p.15 marker (line 375) and BEFORE p.16 marker (line 409) → corresponds to **PDF p.16** ✓ (user-provided receipt page correct). |
| 17 | S5 | "Launch stage. The founder becomes the bottleneck." | VERIFIED | source-playbook.txt line 588 — verbatim "The founder becomes the bottleneck" as section heading under Launch-stage challenges | Exact verbatim match. Page-marker audit: line 588 sits AFTER p.22 marker (line 587) and BEFORE p.23 marker (line 624) → corresponds to **PDF p.23** (user-provided p.22 was off-by-one; auto-corrected). |
| 18 | S5 | "Scale stage. Delegating the operational layer." | VERIFIED | source-playbook.txt line 697 — verbatim "Delegating the operational layer" as section heading under Scale-stage challenges | Exact verbatim match. Page-marker audit: line 697 sits AFTER p.25 marker (line 669) and BEFORE p.26 marker (line 704) → corresponds to **PDF p.26** ✓ (user-provided receipt page correct). |

## NEW Tier 2 Claims (Important) — Scene 5 per-mode consequences

| # | Scene | Claim | Verdict | Source | Notes |
|---|-------|-------|---------|--------|-------|
| 19 | S5 | Idea-stage consequence: "You ship a prototype in four hours and call it proof." | VERIFIED (faithful paraphrase) | PDF p.10 (txt lines 177-184) — "When technical blockers are lifted, an impassioned founder risks skipping the most important work in the startup journey: validating that their idea is genuinely a solution that people need and will use… the rapidity and ease of spinning up a prototype that looks something like a product also, counterintuitively, presents a genuinely dangerous existential risk" | "Four hours" is the script's rhetorical compression of the playbook's "rapidity and ease of spinning up a prototype" — concrete time figure not in source, but represents the speed-collapse the source explicitly invokes. Faithful framing; no fabricated stat (no specific time claim in source to contradict). |
| 20 | S5 | MVP-stage consequence: "Skip the specs and every Claude session drifts the codebase further from your plan." | VERIFIED | PDF p.16 (txt lines 402-405) — verbatim "Founders who skip specs, architectural decisions, and context files (like CLAUDE.md) hit a predictable wall where every new session requires re-explaining the codebase and AI-generated changes drift from the original vision" | Script's "drifts the codebase further from your plan" is a near-verbatim compression of "AI-generated changes drift from the original vision" + "each session re-derives foundational decisions from scratch, and those decisions drift" (line 404). Head noun and verb both match. |
| 21 | S5 | Launch-stage consequence: "Decisions that should take an hour now take a week." | VERIFIED | PDF p.23 (txt lines 597-600) — verbatim "Telltale signs that this is happening include decisions that should take an hour now take a week for you to get around to them" | Verbatim direct quote (clause-level — "decisions that should take an hour now take a week"). |
| 22 | S5 | Scale-stage consequence: "You built the systems, and now you have to actually trust them." | VERIFIED | PDF p.27 (txt lines 705-707) — verbatim "Your Launch stage work was creating the systems; in the Scale phase, it becomes (1) maturing these systems until they are fully trustworthy and (2) then actually trusting them" | Verbatim "actually trusting them" clause + "creating the systems" → script's "built the systems" head-noun match. |

## NEW Tier 3 Claims (Contextual) — Scene 5

| # | Scene | Claim | Verdict | Source | Notes |
|---|-------|-------|---------|--------|-------|
| 23 | S5 | "Each stage has a named killer." + "Four stages. Four named ways to die." | VERIFIED | PDF chapters 3-6 each have a `<stage> stage challenges` section, with the first sub-heading per chapter being the named primary failure mode (Idea = Mistaking building for validating, MVP = Agentic technical debt, Launch = The founder becomes the bottleneck, Scale = Delegating the operational layer) | Structural claim. Source organizes each stage's failure modes into a named-challenges section; the four named modes are precisely the four sub-headings the script enumerates. "Killer" / "ways to die" are the script's rhetorical compression of the source's "challenges" framing. Defensible. |

## Source URL Audit (extension)

No new URLs introduced by Scene 5. Receipt comment references local PDF only (`research/source-playbook.pdf`). The original 4 source URLs (validated in prior run — see preserved audit below) are unchanged.

### Preserved from prior run

| # | URL | Status | Supports Claim? | Notes |
|---|-----|--------|-----------------|-------|
| 1 | https://claude.com/blog/the-founders-playbook | LIVE (200) | Yes | Primary blog source |
| 2 | https://www.cbinsights.com/research/report/startup-failure-reasons-top/ | LIVE (200) | Partial | Per PDF primary source |
| 3 | https://www.buildmvpfast.com/blog/one-person-unicorn-ai-agents-solo-founder-billion-dollar-2026 | HTTP 403 (bot-block) | N/A | Anti-bot; ordinary browsers reach it; non-blocking |
| 4 | https://claude.com/blog/building-companies-with-claude-code | LIVE (200) | Yes — verbatim | Vulcan stats |

## Receipt Audit (Step 4b)

All `<!-- Receipt: <url> -->` comments in `scripts/full-script.md` trace to entries in the brief's `## Receipts` section OR to `research/source-playbook.pdf` (local primary source). NEW Scene 5 receipt references local PDF only (p.10 + p.16 + p.23 + p.26) — page numbers auto-corrected per page-marker audit (see auto-correction below).

**Verdict**: RECEIPT_AUDIT_PASS

## Auto-Applied Corrections

### Correction 1 (extension): Scene 5 receipt page-number provenance
- **Original**: `<!-- Receipt: research/source-playbook.pdf p.9 (Mistaking building for validating) + p.16 (Agentic technical debt) + p.22 (The founder becomes the bottleneck) + p.26 (Delegating the operational layer) -->`
- **Corrected**: `<!-- Receipt: research/source-playbook.pdf p.10 (Mistaking building for validating) + p.16 (Agentic technical debt) + p.23 (The founder becomes the bottleneck) + p.26 (Delegating the operational layer) -->`
- **Source**: page-marker audit on source-playbook.txt — "Mistaking building for validating" (line 175) sits between p.9 marker (line 174) and p.10 marker (line 214), so it's on PDF page 10 (not 9). "The founder becomes the bottleneck" (line 588) sits between p.22 marker (line 587) and p.23 marker (line 624), so it's on PDF page 23 (not 22). Other two pages (16 and 26) already correct.
- **Files updated**: `videos/claude-founders-playbook/scripts/full-script.md` ONLY
- **Impact**: Provenance comment only — NOT viewer-facing, NOT in any per-scene `.txt`, NOT in flat `script.txt`. No TTS / no on-screen text affected.
- **Re-flatten**: NOT required for this correction (no spoken-text edit). Re-flatten of `script.txt` was ALREADY done independently by Phase 2a as part of the 9-scene extension.

### Preserved from prior run

Correction 1 (prior): Scene 7 receipt provenance page number (p.16 → p.16-17) — applied 2026-05-16. No change in this re-run.

## Stale Data Warnings

None new in Scene 5. (Prior CB Insights advisory preserved — see notes from prior run.)

## Corrections Required (manual)

None.

## Notes (extension)

- ARTICLE_RESPONSE scope honored: no WebSearch performed; all NEW claim verification against source-playbook.pdf primary source via `grep` on source-playbook.txt.
- All 4 NEW Tier 1 phrases ("Mistaking building for validating", "Agentic technical debt", "The founder becomes the bottleneck", "Delegating the operational layer") are VERBATIM section headings in the PDF, used as named failure modes exactly as the script presents them.
- All 4 NEW Tier 2 per-mode consequences are either verbatim quotes (Launch — "decisions that should take an hour now take a week") or faithful paraphrases of source sentences (MVP — "AI-generated changes drift from the original vision" → "drifts the codebase further from your plan"; Scale — "actually trusting them" → "have to actually trust them"; Idea — "rapidity and ease of spinning up a prototype" → "ship a prototype in four hours and call it proof"). The Idea consequence's "four hours" is rhetorical compression — no specific time figure in source to contradict it.
- Re-flatten of `script.txt` was completed by Phase 2a: 9 narration paragraphs (1632 chars previously → 2178 chars after extension; +546 chars from new Scene 5).
- Per-scene file count: 9 narration files + 0 preview file = 9 total in `scripts/`.

## Cumulative claim totals (prior 14 + new 9)

| Tier | Count | Verdict breakdown |
|------|-------|-------------------|
| Tier 1 | 13 | 13 VERIFIED |
| Tier 2 | 8 | 8 VERIFIED |
| Tier 3 | 2 | 2 VERIFIED |
| **Total** | **23** | **23 VERIFIED** |

Gate: PASS.
