# Fact-Check Report: openclaw-100-codex-fleet

Generated: 2026-05-16
Verification methods: WebFetch (URL liveness) + bidirectional cross-check vs. `research/content-brief.md` and source clipping `D:\Nextcloud\Obsidian\sync\smartcode\Clippings\Post by @steipete on X.md`
Scope: **ARTICLE_RESPONSE** — fact-check against the source post + brief only (no broad WebSearch, per `feedback_factcheck_article_response_scope`).

---

## Summary

| Metric                    | Count |
| ------------------------- | ----- |
| Total claims extracted    | 32    |
| Tier 1 (Critical)         | 12    |
| Tier 2 (Important)        | 14    |
| Tier 3 (Contextual)       | 6     |
| VERIFIED                  | 31    |
| CORRECTED                 | 0     |
| STALE                     | 0     |
| UNVERIFIED                | 1     |
| FAILED                    | 0     |
| Source URLs checked       | 6     |
| Broken sources            | 0     |

**Overall Verdict**: **PASS**

## Gate Result

- Tier 1 FAILED count: **0** (must be 0 to pass) ✅
- Tier 1 UNVERIFIED count: **0** (must be 0 to pass) ✅
- Broken critical sources: **0** ✅
- RECEIPT_AUDIT_FAIL count: **0** (must be 0 to pass) ✅

**Gate: PASS** — Zero Tier 1 FAILED, Zero Tier 1 UNVERIFIED, Zero broken Tier 1 sources, Zero RECEIPT_AUDIT_FAIL.

---

## Tier 1 Claims (Critical)

| #  | Scene | Claim | Verdict | Evidence | Notes |
|----|-------|-------|---------|----------|-------|
| 1  | s01   | "847,000 viewers this week" | VERIFIED | Brief line 6: "847.5K views"; spec note acknowledges 847K = within rounding | Spec-blessed tolerance |
| 2  | s01   | "~100 Codex agents in the cloud" | VERIFIED | Source clipping: "We constant run ~100 codex in the cloud, reviewing every PR, every issue." Brief §1, Big Claim #1. | Direct quote-able |
| 3  | s02   | Verbatim quote: "How would we build software in the future if tokens don't matter?" | VERIFIED | Source clipping line 14: identical wording. Brief §1 verbatim block. | Exact match, no punctuation drift |
| 4  | s03   | "roughly ten automations" (10 use cases) | VERIFIED | Brief §1 Breakdown table lists 11 automations (use cases 1–11). Script says "roughly ten" — acceptable rounding for spoken narration. | Numerically conservative |
| 5  | s05   | "clawsweeper open source, MIT licensed, lives under OpenClaw GitHub org" | VERIFIED | WebFetch github.com/openclaw/clawsweeper confirms MIT + openclaw org. Brief §3.1. | Source confirmed |
| 6  | s05   | "four lanes — Review, Apply, Repair, Commit Review" | VERIFIED | Brief §3.1 + WebFetch github confirms "four operational lanes: review lane, apply lane, repair lane, [and] commit review lane." | Exact match |
| 7  | s05   | "3,478 issues scanned, ~4 closed = 0.1% close rate" | VERIFIED | Brief §3.1: "in one reference week, scanned ~3,478 issues, closed roughly 4 — a 0.1% close rate." | Exact match |
| 8  | s06   | "brew install openclaw slash tap slash crab-box" | VERIFIED | WebFetch crabbox.sh confirms `brew install openclaw/tap/crabbox`. Spelling on tap/crabbox correct. | Exact match |
| 9  | s06   | "Cloudflare Worker brokers all secrets; CLI carries only bearer token" | VERIFIED | WebFetch crabbox.sh: "A Cloudflare Worker holds provider credentials and serializes lease state. Your CLI only carries a bearer token." | Exact match |
| 10 | s09   | "Vercel's deepsec, released two weeks before this post" | VERIFIED | WebFetch confirms release date May 4, 2026. Post date May 15, 2026 = 11 days. "About two weeks" is within rounding tolerance (spec explicitly accepts). | Within tolerance |
| 11 | s11   | Verbatim quote: "I could just disable fast mode and cut it down by 70%" | VERIFIED | Source clipping line 58: identical wording (script adds trailing period; words match exactly). | Exact match |
| 12 | s11   | "Fast mode is OpenAI Codex's 1.5x speed tier" | VERIFIED | WebFetch developers.openai.com/codex/speed: "Fast mode increases supported model speed by 1.5x and consumes credits at a higher rate than Standard mode." | Exact match |

## Tier 2 Claims (Important)

| #  | Scene | Claim | Verdict | Evidence | Notes |
|----|-------|-------|---------|----------|-------|
| 13 | s01   | "Peter Steinberger casually posted" (attribution) | VERIFIED | Source clipping `author: [[@steipete]]` and brief §4 Steinberger bio | Author correct |
| 14 | s03   | "claw-sweeper hunts down old issues quietly fixed on main" | VERIFIED | Source clipping: "@clawsweeper will eventually find that 6 month old issue and close it with an exact reference" | Faithful paraphrase |
| 15 | s03   | "Codex reviews every commit for security holes" | VERIFIED | Source clipping: "We run codex on every commit to review for security issues" | Exact paraphrase |
| 16 | s03   | "Codex polices spam comments" | VERIFIED | Source clipping: "codex running that scans comments for spam and blocks people" | Faithful paraphrase |
| 17 | s03   | "Codex tracks performance regressions into Discord" | VERIFIED | Source clipping: "codex instances running that verify performance benchmarks and report regressions into Discord" | Exact match |
| 18 | s03   | "Agents listen on team meetings and start work" | VERIFIED | Source clipping: "agents that listen on our meetings and proactively start work, e.g. create PRs when we discuss new features while we discuss them" | Faithful paraphrase |
| 19 | s06   | "shared agent workspace control plane" | VERIFIED | Brief §3.2 + WebFetch crabbox.sh confirms it's a "control plane for remote test environments" with the Lease → sync → run → release pattern | Match |
| 20 | s06   | "Backends: Hetzner, AWS, Azure (brokered); E2B, Daytona, Blacksmith, Semaphore (delegated)" | VERIFIED | WebFetch crabbox.sh lists Hetzner/AWS/Azure (brokered) + E2B/Daytona/Blacksmith/Semaphore (delegated). Note: docs also list Google Cloud + static SSH as additional options — script's enumeration is a subset, not a contradiction. | Subset match |
| 21 | s06   | "Linux, macOS on EC2 Mac, Windows on AWS/Azure — all stream over VNC" | VERIFIED | Brief §3.2 + WebFetch crabbox.sh: "Crabbox webvnc streams a Linux, macOS, or Windows desktop into the browser" + macOS via EC2 Mac, Windows via AWS/Azure | Exact match |
| 22 | s07   | "clawpatch.ai — open source MIT, made by OpenClaw team" | VERIFIED | WebFetch clawpatch.ai: "Made with care by the OpenClaw team. Released under MIT license." | Exact match |
| 23 | s07   | "semantic units: Routes (Next.js), Commands (npm/Go/Rust/Swift), Packages, CLI scripts, Tests" | VERIFIED | WebFetch clawpatch.ai + Brief §3.3 confirm exact unit list | Exact match |
| 24 | s07   | "Findings categorized: Bug, security, performance, docs gap, test gap, maintainability" | VERIFIED | WebFetch clawpatch.ai + Brief §3.3 confirm all six categories | Exact match |
| 25 | s07   | "Markdown + JSON reports" | VERIFIED | WebFetch clawpatch.ai: "Markdown reports and JSON state with severity levels, categories, and confidence scores." | Exact match |
| 26 | s09   | "Codex configured for security covers whatever deepsec doesn't" | UNVERIFIED | Brief §4 flags "Codex Security" as ambiguous shorthand by steipete — likely Codex configured for security review, not a discrete product. Script handles this correctly by NOT asserting it's a product. | Acknowledged ambiguity; script phrasing is safe |

## Tier 3 Claims (Contextual)

| #  | Scene | Claim | Verdict | Evidence | Notes |
|----|-------|-------|---------|----------|-------|
| 27 | s05   | "lives under OpenClaw GitHub org" | VERIFIED | WebFetch github.com/openclaw/clawsweeper resolves under openclaw org | Confirmed |
| 28 | s05   | "It never closes a maintainer's own issue, never touches protected labels" | VERIFIED | WebFetch confirms: "Maintainer-authored items are never auto-closed" + "Protected labels block close proposals" | Exact match |
| 29 | s05   | "re-fetches GitHub state right before any change" | VERIFIED | WebFetch: "Apply reads existing reports and mutates GitHub only when the stored review is still valid" | Confirmed |
| 30 | s06   | "No long-lived dev boxes" (TTL-bounded leases) | VERIFIED | Brief §3.2 + WebFetch confirms TTL-bounded leases + the Lease → sync → run → release pattern | Confirmed |
| 31 | s10   | "five reaction camps" (no commenter names, no @handles) | VERIFIED | Brief §2 enumerates 5 main buckets A-E (bucket F at 5% is folded into general framing). Script cleanly abstracts to 5. Zero commenter names, zero @handles, zero verbatim paraphrases. Per `feedback_no_fabrication_source_only` + brief §6 risk constraints. | Sentiment audit PASS |
| 32 | s10   | Each camp's stance (skeptic / forward-looking / cost-opt / admiring / confused) | VERIFIED | Maps 1:1 to brief §2 buckets A/B/C/D/E. "Steipete agreed publicly" (camp 2) traces to brief §2 bucket B ("replied with a single emphatic checkmark") + clipping comment thread (`💯`). | Exact mapping |

---

## Receipt Audit (Step 4b)

Receipts extracted from `scripts/full-script.md` and cross-checked against brief Section 4 + Source Map (Section 8 of brief).

| Scene | Receipt URL | In Brief? | Verdict |
|-------|-------------|-----------|---------|
| s01   | https://x.com/steipete/status/2055405041843052792 | YES (brief line 6) | MATCH |
| s02   | https://x.com/steipete/status/2055405041843052792 | YES | MATCH |
| s03   | https://x.com/steipete/status/2055405041843052792 | YES | MATCH |
| s05   | https://github.com/openclaw/clawsweeper | YES (brief §3.1 + Source Map) | MATCH |
| s06   | https://crabbox.sh/ | YES (brief §3.2 + Source Map) | MATCH |
| s07   | https://clawpatch.ai | YES (brief §3.3 + Source Map) | MATCH |
| s09   | https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base | YES (brief §4 + Source Map) | MATCH |
| s10   | https://x.com/steipete/status/2055405041843052792 | YES | MATCH |
| s11   | https://developers.openai.com/codex/speed | YES (brief §4 Source Map) | MATCH |
| s13   | https://crabbox.sh/ | YES | MATCH |

**Verdict**: **RECEIPT_AUDIT_PASS** — All 10 receipt URLs trace to the brief's verified Source Map.

---

## Source URL Audit (Step 4)

| #   | URL | Status | Supports Claim? | Notes |
|-----|-----|--------|-----------------|-------|
| 1   | https://crabbox.sh/ | LIVE (200) | YES | Primary source. Confirms install, OSes, backends, VNC, Cloudflare Worker broker. |
| 2   | https://clawpatch.ai | LIVE (200) | YES | Primary source. Confirms MIT, semantic units, finding categories, output formats. |
| 3   | https://github.com/openclaw/clawsweeper | LIVE (200) | YES | Primary source. Confirms MIT, four lanes, safety guardrails. 1.6k stars. |
| 4   | https://developers.openai.com/codex/speed | LIVE (200) | YES | Primary source. Confirms "1.5x speed" definition of fast mode + higher credit rate. |
| 5   | https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base | LIVE (200) | YES | Primary source. Confirms release date 2026-05-04 → 11 days before post = "about two weeks" ✓ |
| 6   | https://x.com/steipete/status/2055405041843052792 | LIVE (clipping verified 2026-05-16) | YES | Source of all post-quote claims. Bidirectional match with clipping file. |

**Broken sources: 0.**

---

## Forward-Direction Trace (script → brief)

Every factual claim in the script traces to a brief section. No fabricated claims detected. No invented features. No dollar amounts asserted (per brief §6 constraint). Script correctly hedges "Codex Security" as Codex-configured-for-security rather than a product (Tier 2 #26).

## Reverse-Direction Trace (brief Big Claims → script)

Brief §5 lists 8 BIG CLAIMS. Coverage in script:

| # | Brief Big Claim | In script? |
|---|-----------------|------------|
| 1 | ~100 codex agents reviewing every PR + every issue | s01 ✓, s03 ✓ |
| 2 | clawsweeper closes fixed-on-main issues with reference; ~4 of 3,478 (0.1%) | s05 ✓ (full numerical detail) |
| 3 | crabbox.sh = ephemeral cloud VMs for real-world UI work (Telegram demo) | s06 ✓ (full demo flow) |
| 4 | clawpatch.ai = semantic functional unit review (Routes/Commands/Packages/CLI/Tests) | s07 ✓ (all 5 units enumerated) |
| 5 | Codex on every commit for security + Vercel deepsec + "Codex Security" | s03 ✓ + s09 ✓ |
| 6 | Agents listen on meetings, draft PRs in real time | s03 ✓ |
| 7 | "I could just disable fast mode and cut it down by 70%" — latency not cost | s11 ✓ (with full context) |
| 8 | Run "extremely lean" + community pushback | s10 ✓ (camp 1) |

**All 8 Big Claims present.** No unexpectedly absent claims.

---

## Heteronym / Pronunciation Audit (per `.claude/rules/tts-pronunciation.md`)

Spot-check of high-risk words in the flat `script.txt`:

- "live" — Not present in adjective sense. Phrase "real-time" (s11) used safely. ✓
- "lead" — Not present. ✓
- "read" — "reading" (s09 reading and writing) — present-participle, unambiguous. ✓
- "close" — "close rate" (s05), "closing the dead issues" (s09) — verb/noun. Context-clear. ✓
- "record" — "record" the screen (s06), "recording a video" (s13) — verb only, unambiguous. ✓

Tech-term spell-outs verified in scene .txt files:
- `crabbox` → `crab-box` ✓
- `clawsweeper` → `claw-sweeper` ✓
- `clawpatch.ai` → `claw-patch dot A I` ✓ (s07)
- `deepsec` → `deep-sec` ✓
- `Next.js` → `Next dot J S` ✓ (s07)
- `847,000` → `eight hundred forty-seven thousand` ✓ (s01)
- `3,478` → `three thousand four hundred seventy-eight` ✓ (s05)
- `0.1%` → `zero point one percent` ✓ (s05)
- `1.5x` → `one point five X` ✓ (s11)
- `70%` → `seventy percent` ✓ (s11)
- `18-36` → `eighteen to thirty-six` ✓ (s10)

**Pronunciation audit: PASS.** No heteronym risks; tech terms safely flattened.

---

## Auto-Applied Corrections (full-auto mode)

**None.** No corrections required. The script + flat `script.txt` + per-scene `.txt` files were already in sync and factually correct against the brief and source clipping.

## Stale Data Warnings

**None.** The source post is 1 day old (published 2026-05-15, fact-checked 2026-05-16). All tool versions/features verified against live primary sources within the same 24-hour window.

## Corrections Required (manual)

**None.**

---

## Notes on the single UNVERIFIED claim (#26)

The "Codex Security" reference in s09 is intentionally hedged. Brief §4 calls out: *"'Codex Security': not a separate product name surfaced in research — likely steipete's shorthand for Codex configured/prompted to do security review."* The script's phrasing — *"Codex configured for security covering whatever deep-sec doesn't"* — preserves the ambiguity correctly. This is NOT a blocker; it is the right authorial choice. Logged as UNVERIFIED only because the underlying product reference cannot be confirmed (because it likely isn't a product). No script change needed.

---

## Gate Decision

**PASS.** All Tier 1 claims verified. All source URLs live and supportive. Receipt audit clean. Pronunciation audit clean. The script is factually sound and ready for TTS.

**Next step**: run TTS + transcribe.
```bash
npx hyperframes tts videos/openclaw-100-codex-fleet
npx hyperframes transcribe videos/openclaw-100-codex-fleet
```

Then resume Phase 3.5 (retention).
