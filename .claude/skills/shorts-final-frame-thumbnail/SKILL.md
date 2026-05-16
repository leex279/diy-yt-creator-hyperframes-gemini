---
name: shorts-final-frame-thumbnail
description: Design the held-still final frame of a Short so it doubles as a thumbnail-grade tile that stops the scroll, survives the loop, and earns the tap. Layers an 11-style design vocabulary (neo-minimalism, surround, tier-rank, whiteboard, familiar-interface, cinematic-text, warped-faces, maximalist, encyclopedia-grid, candid-fake, anti-thumbnail) on top of the mandatory 5-element rule from `.claude/rules/shorts-thumbnail-frames.md`. Use when the user asks to "design the final frame", "make the last frame thumbnail-worthy", "pick a thumbnail style", "improve the thumbnail", "the closing frame is weak", "what should the end frame be", "build a 2026 thumbnail", or when reviewing a Short whose final phase fails the topic / tap / loop / screenshot tests. Complements (does NOT replace) the rule.
---

# Shorts Final-Frame Thumbnail

Engineer the last frame of every vertical Short so it functions as a stand-alone thumbnail — the tile YouTube auto-picks, the still a paused viewer sees, the screenshot that gets shared, the loop-pause moment. Distilled from `.claude/rules/shorts-thumbnail-frames.md` (mandatory baseline) plus vidIQ's 2026 thumbnail research (https://www.youtube.com/watch?v=Yv6RLQv889M).

## Position in the pipeline

Two layers, two roles:

| Layer | Source | Role |
|---|---|---|
| **Baseline** | [`.claude/rules/shorts-thumbnail-frames.md`](../../rules/shorts-thumbnail-frames.md) | What MUST be present — topic statement, visual anchor, brand chrome, outcome line, (optional) CTA. Hold ≥1.5s, entrance ≤0.5s. The blocking gate. |
| **Design menu** | This skill | HOW to compose those 4-5 elements so the frame feels new and disruptive in the 2026 feed instead of generic. The style vocabulary. |

The baseline rule alone produces a *valid* final frame. This skill is what makes it a *winning* final frame.

## When to invoke

- Inside `/diy-yt-creator:phase1-plan` when picking the closing visual treatment (style-pick mode)
- Inside `/diy-yt-creator:phase3-5-retention` or `/diy-yt-creator:phase2-script` when the closing scene is being authored
- Whenever a user says: *"design the final frame", "make the last frame thumbnail-worthy", "pick a thumbnail style", "improve the thumbnail", "the closing frame is weak", "what should the end frame be"*
- Whenever a Short review surfaces a final frame that fails any of the 4 self-check tests in the baseline rule (topic / tap / loop / screenshot)
- Whenever the user wants to A/B variant final frames — pick 2 styles from this skill's catalog and author both

## The four modes

| Mode | When | Output |
|---|---|---|
| **Pick** | Before authoring — Phase 1 plan or pre-Phase-2 closing-frame design | A chosen style + 1-2 backup styles, with rationale |
| **Author** | While building the closing phase HTML | **10 variants** — each one a working `#phase-thumb` block (or 1280×720 thumbnail HTML for long-form) that satisfies the baseline rule, with different headline angles and minor style variation. Plus a contact-sheet PNG showing all 10 numbered. The user picks one to ship. |
| **Audit** | After preview / before render | Pass/fail report against the rule's 4 tests AND the picked style's design rules; rewrite suggestions for any failure |
| **Restyle** | When the audit fails OR the user wants more variants | Generate another batch of 10 variants (different angles than the first batch) |

## Workflow

### Mode 1 — Pick (style selection)

1. **Read the brief** — what is the video's topic, niche, tone, and outcome receipt?
2. **Read the existing closing phase** if one exists (`videos/<slug>/index.html`, search for `phase-thumb`, `phase-end`, or the last `data-start` div).
3. **Read** [`references/style-catalog.md`](references/style-catalog.md) — the 11 styles with their psychology, fit, and anti-patterns.
4. **Read** [`references/style-picker.md`](references/style-picker.md) — the decision tree mapping topic → recommended styles. Cross-reference niche-bending opportunities (a tutorial Short can borrow encyclopedia-grid from explainer videos; a dev tool announce can borrow candid-fake from challenge content).
5. **Pick one primary + one backup**. Document the choice in the video's `notes.md` (or in a comment at the top of the closing-phase HTML block) so the audit and any future restyle has the rationale.

### Mode 2 — Author (build 10 variants, user picks)

**HARD RULE: Author mode produces 10 variants, never 1.** The user picks a thumbnail by visual gut decision; ten variants makes the choice obvious, one variant is a guess.

1. Start from the canonical 5-element scaffold in [`.claude/rules/shorts-thumbnail-frames.md`](../../rules/shorts-thumbnail-frames.md) §"How to author it".
2. Open [`references/code-templates.md`](references/code-templates.md) and review the per-style scaffold for the picked style.
3. Open [`references/headline-angles.md`](references/headline-angles.md) — pick **10 different headline angles** that all carry the same topic, varying by psychological frame (death-of-default, versus, imperative, insider receipt, strikethrough, cinematic dark, question hook, big-number social proof, replacement, data-led). Headline copy MUST be 2-4 words contrarian punch — never the source article's verbatim title.
4. Vary the **theme** across the 10 (most in the picked style, 2-3 in adjacent styles for diversity — e.g., 7 cream/cinematic-text, 2 dark/cinematic-text, 1 white/neo-min strikethrough — so the user sees real choice, not 10 reskinned twins).
5. **Output structure**:
   - `videos/<slug>/thumbnail/_base.css` — shared layout primitives (chrome, brand mark, cover-anchor zone)
   - `videos/<slug>/thumbnail/variant-01.html` ... `variant-10.html` — one per angle, each at the spec'd canvas (1280×720 long-form, 1080×1920 shorts)
   - `videos/<slug>/thumbnail/variant-01.png` ... `variant-10.png` — captured via agent-browser
   - `videos/<slug>/thumbnail/contact-sheet.html` — grid view of all 10 numbered + angle labels for comparison
   - `videos/<slug>/thumbnail/contact-sheet.png` — captured contact sheet (this is what you SHOW the user)
6. For shorts (1080×1920) the variants are `#phase-thumb` blocks that can be swapped into `videos/<slug>/index.html`. For long-form (1280×720) the variants are standalone HTML files captured to PNG for separate YouTube Studio upload.
7. Confirm each variant: every entrance animation finishes by `data-start + 0.5s`. Static hold ≥1.5s. No yoyo, glow-pulse, drift, or counter-roll. (Shorts only — long-form thumbnails are static.)
8. Run `npx hyperframes lint videos/<slug>` and `npx hyperframes inspect videos/<slug>` if any variant is wired into the actual MP4 composition.
9. Show the user the contact sheet and ask which variant to ship. Do NOT pick on their behalf.

### Mode 3 — Audit (review existing final frame)

1. **Run the rule's 4 self-check tests** from `.claude/rules/shorts-thumbnail-frames.md` §"Self-check before declaring a Short done":
   - Topic test, Tap test, Loop test, Screenshot test
2. **Run the style-specific checks** from [`references/audit-checklist.md`](references/audit-checklist.md) — once you've identified which of the 11 styles the frame is attempting (or "no style — generic"), audit against that style's design rules.
3. Output a per-test PASS/FAIL with line citations to the closing-phase HTML.
4. For every FAIL, propose a concrete rewrite that keeps the same style but fixes the failure.
5. Audit-mode does NOT modify the file unless the user asks.

### Mode 4 — Restyle (replace with a different style)

1. Run Mode 1 with the constraint: "exclude the previously-attempted style from candidates".
2. Run Mode 2 with the new style.
3. Run Mode 3 to verify.
4. If the user wants A/B variants, author BOTH closing phases as separate `#phase-thumb-a` / `#phase-thumb-b` and toggle which is active via comment-out — render once for each, compare.

## The 11 styles at a glance

Full design rules in [`references/style-catalog.md`](references/style-catalog.md). One-liners:

1. **Neo-minimalism** — one subject, ≥50% negative space, max 2 colors. Visual rest stop in a chaotic feed.
2. **Surround** — central face/object, organized circle/grid of supporting items around it. Scope flex.
3. **Tier-rank rainbow** — 3/5/7 items color-coded red→blue, numbered hierarchy. Engagement bait via opinion.
4. **Whiteboard** — hand-drawn frameworks. Signals "real value, no fluff" against AI-generated saturation.
5. **Familiar interface** — fake tweet / Reddit / Yelp / Amazon listing. Borrows the platform's credibility.
6. **Cinematic text** — 3-4 words embedded INSIDE the scene's lighting, not stuck to edges. Netflix-still feel.
7. **Warped faces** — pattern-interrupt distortion (double exposure, glitch, triple-expose). For psych / commentary topics.
8. **Maximalist (I own everything)** — collection IS the star, person is secondary. For collector / hobbyist content.
9. **Encyclopedia grid** — flat-icon grid with 1-2 word labels. Wikipedia-page-as-thumbnail. For "every X explained".
10. **Candid fake** — engineered photo that *could* have happened. No text/arrows/circles. For travel / challenge / lifestyle.
11. **Anti-thumbnail (quiet)** — dark, serious face, "59 seconds" / off-round time stamp. Removes commitment risk.

## Hard rules across all modes

1. **Baseline rule is non-negotiable.** Topic + visual anchor + brand chrome + outcome receipt are still required, regardless of style. Never strip them to satisfy a style's "minimalism." If a style genuinely conflicts with the rule, document the deviation in `notes.md` and flag it to the user — don't silently break the rule.
0. **Author mode = 10 variants, never 1.** A single thumbnail is a guess; 10 is a choice. Generate 10 distinct headline angles per [`references/headline-angles.md`](references/headline-angles.md), capture all to PNG, build a contact sheet, let the user pick. Never deliver one and ask "is this good?"
0a. **Headlines are 2-4 word contrarian punches.** Never reuse the source article's verbatim title. Editorial titles read as quoted reverence; thumbnails need takes. "X is dying.", "Y beats X.", "Stop using X." — that energy. The video script can quote the source; the thumbnail must take a side.
2. **Hold ≥1.5s static, entrance ≤0.5s.** This is the loop-pause window. Every style obeys this — even maximalist (the 12 surrounding items enter together within 0.5s, then freeze).
3. **Style match must fit the topic.** Warped-faces on a productivity-hack Short reads off-brand. Candid-fake on a serious AI ethics short reads dishonest. The style-picker's "when NOT to use" column is a hard constraint, not a soft suggestion.
4. **Never reuse the intro hero-slam frame as the final frame.** End is the receipt; intro is the question. Same frame = no payoff.
5. **No trailing animation in the hold window.** Counter still rolling, marker still sweeping, shape still drifting — all violate the still-frame contract. Every motion finishes ≥0.3s before the hold begins.
6. **Test the screenshot, not the video.** Pause the rendered MP4 on the very last frame and ask whether THIS PNG, with no audio and no prior frames, communicates the topic in <1 second. If it doesn't, restyle.
7. **Trends have shelf life.** Note in `notes.md` which style was picked + when. After 6 months, re-audit — a style that was disruptive becomes generic when 90% of the feed copies it. The catalog is the menu, not the prescription.
8. **Cite your source for fabricated photo content.** If you use the candid-fake style, the still must be either (a) an actual frame from earlier in the Short, or (b) flagged as composed/AI-assisted in the video description. Never present a synthetic still as documentary footage.

## What this skill is NOT

- A renderer / image generator — the skill produces HyperFrames composition HTML, not finished JPGs.
- A replacement for `.claude/rules/shorts-thumbnail-frames.md` — the rule is the blocking gate; this skill is the design layer on top.
- A long-form thumbnail tool — long-form videos use a separately-uploaded thumbnail asset, not the rendered final frame. This skill is Shorts-only (1080×1920).
- A general thumbnail-design service — it's tuned to the diy-yt-creator pipeline's closing-phase pattern, not arbitrary thumbnail jobs.
- A clickbait engine — the styles MUST land on the actual topic, not bait something the video doesn't deliver. The candid-fake style especially requires restraint per its own design rules.

## When invoked from `/diy-yt-creator` commands

- `phase1-plan` — call in **Pick mode** when drafting the closing phase. Output the chosen style + rationale into the plan markdown.
- `phase2-script` — the Step where the closing CTA narration is written should reference the picked style so the spoken outro matches what's on screen.
- `phase3-5-retention` — call in **Audit mode** after the per-scene retention strategy is drafted, to verify the closing frame still passes the 4 tests with whatever retention adjustments were made.
- A direct user request ("design the final frame for `<slug>`") — run all four modes in order: Pick → Author → Audit, with Restyle as needed.

## Self-improvement

When a Short ships and the final frame's performance is observable (CTR, replay-rate, screenshot-shares):

1. Note which style was picked in the video's `notes.md`.
2. After 14 days, note the actual CTR vs. the channel's running average for the same niche.
3. If a "PASS" frame underperformed, the audit is missing a check — propose the new check and add it to [`references/audit-checklist.md`](references/audit-checklist.md) with the failure-mode example.
4. If a deviating frame overperformed, the rule for that style might be too strict — relax it with the reasoning logged.
5. When a NEW style appears in the wider creator ecosystem (something not in this catalog), add it as style #12+ to [`references/style-catalog.md`](references/style-catalog.md) with the same structure and a citation to where it was first observed.

This catalog grows from real ship-data and ecosystem observation, not theory.
