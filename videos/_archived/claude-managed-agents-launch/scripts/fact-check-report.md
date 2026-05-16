# Fact-Check Report: claude-managed-agents-launch
Generated: 2026-05-07
Verification methods: ARTICLE_RESPONSE-mode bidirectional check against source.md + WebFetch (claude.com blog, claude.com form, platform.claude.com docs, claude.com pricing). Perplexity API not configured — skipped per process.

## Summary

| Metric                    | Count |
| ------------------------- | ----- |
| Total claims extracted    | 16    |
| Tier 1 (Critical)         | 14    |
| Tier 2 (Important)        | 2     |
| Tier 3 (Contextual)       | 0     |
| VERIFIED                  | 15    |
| CORRECTED                 | 1     |
| STALE                     | 0     |
| UNVERIFIED                | 0     |
| FAILED                    | 0     |
| Source URLs checked       | 5     |
| Broken sources            | 0     |

**Overall Verdict**: PASS

## Gate Result

- Tier 1 FAILED count: 0 (must be 0 to pass) ✓
- Tier 1 UNVERIFIED count: 0 (must be 0 to pass) ✓
- Broken critical sources: 0 ✓

**PASS** — all Tier 1 claims verified after one auto-correction.

## Tier 1 Claims (Critical)

| #   | Scene    | Claim                                       | Verdict   | Sources                                | Notes                |
| --- | -------- | ------------------------------------------- | --------- | -------------------------------------- | -------------------- |
| 1   | Scene 01 | "Anthropic just made Claude agents DREAM. Live from Code with Claude." | VERIFIED | source.md §2 lead post: "Live from Code with Claude: we're launching dreaming…" | Exact context match |
| 2   | Scene 02 | "Three of these shipped today. One is gated behind a form." | VERIFIED | source.md §2 thread reply 4 + thread reply 1 | RP/public-beta split confirmed |
| 3   | Scene 03 | "Dreaming. Outcomes. Multiagent orchestration. Webhooks. Three are public beta… One, the named flagship, is research preview only." | VERIFIED | source.md §2 lead post (X-post is the announcement-day source of truth — note that platform docs page now lists outcomes/multiagent under research preview as well, but the launch-day public-beta framing matches the source the script was written against) | Locked-source compliant |
| 4   | Scene 04 | Dreaming function: "reviews its past sessions, extracts patterns, and curates memories" | VERIFIED | source.md §2 thread reply 1 (verbatim phrasing from the announcement) + blog post | Near-verbatim quote |
| 5   | Scene 04 | "Request access at the form" → claude.com/form/claude-managed-agents | VERIFIED | source.md §2 thread reply 1; URL liveness check below | URL live as of 2026-05-07 |
| 6   | Scene 05 | Outcomes function: "rubric. A separate grader checks the output in its own context window. The agent iterates until it clears the bar." | VERIFIED | source.md §2 thread reply 2 + blog post | Faithful paraphrase |
| 7   | Scene 05 | "Plus ten points on task success versus standard prompting." | VERIFIED | https://claude.com/blog/new-in-claude-managed-agents — "outcomes improved task success by up to 10 points" | Exact stat match. Head-noun gate: "task success" ↔ "task success" ✓ |
| 8   | Scene 06 | Multiagent function: "lead agent farm work to specialists running in parallel, on a shared filesystem, with their own tools" | VERIFIED | source.md §2 thread reply 3 + blog post (shared-FS detail in blog) | Faithful paraphrase |
| 9   | Scene 06 | "Harvey hit roughly six times completion rate" | VERIFIED | https://claude.com/blog/new-in-claude-managed-agents — "Completion rates went up ~6x in their tests" | Exact stat. Head-noun gate: "completion rate" ↔ "completion rates" ✓ |
| 10  | Scene 06 | "That's a legal-AI production deployment" | VERIFIED | Harvey is a legal-AI company; blog directly attributes the 6× stat to Harvey | Attribution legitimate |
| 11  | Scene 07 | "webhooks are what finally close the loop for real production workflows" (community paraphrase) | VERIFIED | source.md §3 Reaction C — paraphrased without attribution per source.md hard rule | Compliant with anonymization rule |
| 12  | Scene 08 | ~~"Pricing is public"~~ → REMOVED | CORRECTED | No pricing page exists at platform.claude.com/docs/en/managed-agents/* nor at claude.com/pricing for session-hour rates. Brief flagged this for primary-source verification — verification failed. | See Auto-Applied Corrections below |
| 13  | Scene 08 | "the beta header ships in the SDK" | VERIFIED | https://platform.claude.com/docs/en/managed-agents/overview — "All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically." | Exact match |
| 14  | Scene 09 | "available today on the Claude Platform" | VERIFIED | source.md §2 thread reply 4 — "Available today on the Claude Platform" | Verbatim |

## Tier 2 Claims (Important)

| #   | Scene | Claim | Verdict | Sources | Notes |
| --- | ----- | ----- | ------- | ------- | ----- |
| 15  | Scene 04 | "Sleep-time learning, basically." | VERIFIED | Anthropic's own framing of Dreaming as session-review-and-memory-curation maps cleanly to "sleep-time learning" — the brief's `Visual Metaphor Inventory` calls this Anthropic's anthropomorphic framing | Editorial paraphrase, not a stat |
| 16  | Scene 09 | "If you want to learn more about AI, check out the dynamous dot AI community." | VERIFIED | Locked-memory rule `feedback_dynamous_short_outro` — verbatim required line | Compliant |

## Tier 3 Claims (Contextual)

None — every script claim was Tier 1 or Tier 2.

## Source URL Audit

| #   | URL          | Status        | Supports Claim? | Notes              |
| --- | ------------ | ------------- | --------------- | ------------------ |
| 1   | https://claude.com/blog/new-in-claude-managed-agents | LIVE (200) | Yes — primary source for features, customer stats, +10pt lift, Harvey 6× | Primary blog source |
| 2   | https://claude.com/form/claude-managed-agents | LIVE (200) | Yes — Dreaming research-preview waitlist form for Claude Managed Agents | Title: "Claude Managed Agents \| Claude by Anthropic" |
| 3   | https://platform.claude.com/docs/en/managed-agents/overview | LIVE (200) | Yes — confirms beta header `managed-agents-2026-04-01` and SDK auto-set behavior | Used to verify claim #13 |
| 4   | https://platform.claude.com/docs/en/managed-agents/pricing | 404 (does not exist) | N/A | Confirms no public pricing page for Managed Agents at this URL |
| 5   | https://claude.com/pricing | LIVE (200) | No — pricing page covers Free/Pro/Max/Team/Enterprise plans only; no session-hour rate listed | Reinforces removal of "Pricing is public" claim |

## Auto-Applied Corrections (full-auto mode)

### Correction 1: Scene 08 — Trust Strip

- **Original**: "Here's why this lands. Pricing is public, the beta header ships in the SDK, and the verification question, which agent earned the result, is finally on the table."
- **Corrected**: "Here's why this lands. The beta header ships in the SDK, and the verification question, which agent earned the result, is finally on the table."
- **Reason**: Brief's content-brief.md `Gaps` section flagged "$0.08/session-hour" as third-party-summary-sourced and required Phase 2b primary-source re-verify. Verification at https://platform.claude.com/docs/en/managed-agents/* (overview lists no pricing; /pricing returns 404) and https://claude.com/pricing (no session-hour rate) failed. Per the brief gate ("If the script mentions pricing at all… If unconfirmed, REMOVE from script — don't risk fabrication"), the "Pricing is public" assertion was removed. The script never quotes the specific dollar amount, so removal is a deletion of one clause; the remaining sentence still flows and keeps the verified beta-header beat plus the verification-question pivot.
- **Source for non-existence**: 404 at https://platform.claude.com/docs/en/managed-agents/pricing; absence at https://platform.claude.com/docs/en/managed-agents/overview; absence at https://claude.com/pricing
- **Files updated**:
  - `videos/claude-managed-agents-launch/scripts/scene-08-trust-strip.txt`
  - `videos/claude-managed-agents-launch/scripts/full-script.md`
  - `videos/claude-managed-agents-launch/script.txt` (re-flattened — narration is in sync with per-scene files)
- **Impact**: Removes ~1 word of narration time (~0.5s). No retiming needed at Phase 3.5; transcript word-anchors will land slightly earlier in S08 but the scene's 15s budget absorbs it.

### YouTube description correction (paired with above)

- **File**: `videos/claude-managed-agents-launch/youtube-description.md`
- **Original chapter line**: `1:39 The Trust Strip: Pricing, Beta Header, and the Verification Question`
- **Corrected**: `1:39 The Trust Strip: Beta Header and the Verification Question for Claude Agents`
- **Reason**: Same — "Pricing" referenced an unverified primary-source claim. Replacement keeps the chapter SEO-strong (adds "Claude Agents" keyword for searchability per youtube-metadata.md's chapter SEO rule) while removing the unsourced claim.
- **Body text audit**: scanned youtube-description.md for `pricing`, `$0.08`, `session-hour` — no other matches. Body description never quotes the dollar amount; chapter title was the only carrier.

## Stale Data Warnings

None. Everything is dated 2026-05-06 (announcement) and verifications run 2026-05-07 — all sources are within hours of fresh.

## Notable cross-source tension (advisory, NOT blocking)

The platform docs page at https://platform.claude.com/docs/en/managed-agents/overview lists Outcomes and Multiagent under "research preview" status:

> "Certain features (outcomes and multiagent) are in research preview. Request access to try them."

The X-post (source.md §2 lead post) and the announcement blog post both frame Outcomes / Multiagent / Webhooks as "public beta" on launch day. This is an apparent contradiction — but the X-post is the locked source and is the announcement-day truth the script was written against. The docs page may have shifted feature gates post-launch, or the docs page text predates the launch and is being updated. Either way: the script's "public beta" framing matches the locked source.md and is correct as-of-announcement. Advisory only — no script change.

## Corrections Required (manual)

None. All Phase 2b corrections applied automatically per autonomous-mode rules.

## Gate Decision

**PASS** — 16/16 claims verified (15 verified + 1 corrected via deletion). Zero Tier 1 UNVERIFIED. Zero broken Tier 1 sources. YouTube description carries one paired correction (chapter title). Script is factually sound and source-grounded.

Next step: run `npx hyperframes tts videos/claude-managed-agents-launch` and `npx hyperframes transcribe videos/claude-managed-agents-launch`, then `/diy-yt-creator:phase3-5-retention claude-managed-agents-launch`.
