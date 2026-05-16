# Style picker — decision tree

Pick the right thumbnail style for the Short's topic in <60 seconds. Use this AFTER reading [`style-catalog.md`](style-catalog.md) for the full design rules — this file is just the routing logic.

## Step 1 — Topic-shape question

Answer ONE question to narrow the field from 11 to 2-3 candidates:

**Q: What's the dominant shape of the video's payload?**

| If the payload is... | Primary candidates | Rationale |
|---|---|---|
| One feature, one product, one announcement | Neo-minimalism (#1), Cinematic text (#6) | Single-idea topics need single-focus frames |
| Multiple features around one hero (creator, product, framework) | Surround (#2) | Center holds the brand; orbit shows scope |
| A ranked list with explicit hierarchy | Tier-rank rainbow (#3) | The ranking IS the engagement |
| A teaching framework, system, or step-by-step | Whiteboard (#4), Encyclopedia grid (#9) | Educational signal |
| A reaction to / commentary on someone else's content | Familiar interface (#5) | Borrows the source platform's credibility |
| A psychological / identity / heavy theme | Warped faces (#7) | Pattern-interrupt matches the gravity |
| A collection / hobbyist / "I have all of X" flex | Maximalist (#8) | Collection IS the star |
| "Every X explained" style explainer | Encyclopedia grid (#9) | Wikipedia-as-thumbnail |
| Travel / lifestyle / challenge / aspirational moment | Candid fake (#10) | Engineered-yet-believable photo |
| Authority / expert / quick-take direct-to-camera | Anti-thumbnail (#11) | Quiet wins amid the chaos |

If the topic fits multiple rows, run Step 2 to narrow further.

## Step 2 — Channel-fit filter

Eliminate candidates that don't match the channel's voice / brand:

| Style | Eliminate if channel is... |
|---|---|
| Tier-rank rainbow (#3) | Conflict-averse, neutral-tone, educational-without-opinion |
| Whiteboard (#4) | Cinematic / aesthetic / minimalist brand identity |
| Familiar interface (#5) | Original-content-first; relies on host authority not external posts |
| Cinematic text (#6) | Information-density-first; doesn't have access to cinematic photography |
| Warped faces (#7) | Upbeat / feel-good / professional-corporate |
| Maximalist (#8) | Doesn't actually have a collection (don't fake authority) |
| Encyclopedia grid (#9) | Personal / opinion / story-driven |
| Candid fake (#10) | Editorially-credible (news, science, ethics) |
| Anti-thumbnail (#11) | Energetic / playful / entertainment-first |

After Step 2, you should have 1-2 candidates. If 0 — go back to Step 1, the topic-shape was misread. If 3+ — go to Step 3.

## Step 3 — Pattern-interrupt audit

For each remaining candidate, ask: **"How saturated is this style in the channel's adjacent feed RIGHT NOW?"**

Look at the channel's 10 most recent uploads + the 10 most recent uploads on 3 nearest-competitor channels. Count how many of those 40 thumbnails use the candidate style.

| Saturation in adjacent feed | Recommendation |
|---|---|
| 0–2 thumbs (≤5%) | Strong pick. The style is disruptive in this niche right now. |
| 3–10 thumbs (8–25%) | Workable. Still pattern-interrupt-y but watch your differentiation within the style. |
| 11–20 thumbs (28–50%) | Marginal. You're following, not leading. Pick a different style if available. |
| 20+ thumbs (>50%) | Skip. Style has saturated; pick a different one. |

If two candidates tie on saturation, prefer the one that better fits Step 1's topic-shape (the topic match is more important than the saturation tiebreaker).

## Step 4 — Niche bending check

Before finalizing, ask: **"Is there a style from a DIFFERENT niche that would land harder here than the niche-conventional pick?"**

Common cross-niche borrows:

- Tutorial → cinematic-text (steal from lifestyle: cinematic teaching is rare and feels premium)
- Tier rank → encyclopedia grid (steal from explainers: more visual hierarchy than rainbow alone)
- Tech announce → candid-fake (steal from travel: aspirational moment for a tool)
- Commentary → familiar-interface (steal from review channels: borrowed credibility)
- Personal story → cinematic-text (steal from short-film: feels like a Netflix tile)
- Roundup → maximalist (steal from collector channels: visible "I have everything" authority)
- Quote / philosophy → anti-thumbnail (steal from authority channels: gravity matches gravity)
- Code / dev → whiteboard (steal from teacher channels: signals depth in a vibe-coded feed)

If a cross-niche borrow scores higher on Step 3 (lower saturation) AND still passes Step 2 (channel fit), it's the better pick.

## Step 5 — Document the choice

In `videos/<slug>/notes.md` (create if missing), append:

```markdown
## Final-frame thumbnail style

- **Primary style:** [#N name]
- **Backup style:** [#N name] — if A/B testing or restyling
- **Picked at:** [YYYY-MM-DD]
- **Rationale (1-2 sentences):** Topic shape is X, channel fit eliminated Y, saturation in adjacent feed is N/40.
- **Niche-bend?** [no | yes — borrowed from <niche> because <reason>]
```

This rationale becomes the audit trail when future shorts re-pick a style. After 6 months, run [`audit-checklist.md`](audit-checklist.md) §"Shelf-life audit" to see whether the chosen style still feels fresh.

## Worked examples

### Example 1 — "Claude Code 2.0 ships with new MCP defaults"

- **Step 1.** Single announcement → neo-minimalism (#1) or cinematic text (#6).
- **Step 2.** Channel is a dev-tool review channel; both pass.
- **Step 3.** Adjacent feed: 8/40 use neo-minimalism, 1/40 use cinematic text. → cinematic text scores stronger.
- **Step 4.** Niche-bend? Cinematic text IS a niche-bend from lifestyle into dev-tool. Pick stays.
- **Pick: Cinematic text (#6).** Backup: Neo-minimalism (#1).

### Example 2 — "Every coding agent ranked, October 2026"

- **Step 1.** Ranked list → Tier-rank rainbow (#3).
- **Step 2.** Channel is opinionated (Step 2 OK).
- **Step 3.** Adjacent feed: 14/40 use tier-rank → marginal. Check encyclopedia grid (#9) as alternate from "every X explained": 3/40 → strong.
- **Step 4.** Encyclopedia grid is the cross-niche borrow (explainer → ranking content). Combines hierarchy with visual classification.
- **Pick: Encyclopedia grid (#9) with hierarchical labels.** Backup: Tier-rank rainbow (#3).

### Example 3 — "I built an agent that replaced my IDE"

- **Step 1.** Personal-build aspirational story → Cinematic text (#6) OR Candid fake (#10).
- **Step 2.** Channel is dev-focused, host appears on camera; both pass.
- **Step 3.** Adjacent feed: 2/40 use cinematic text, 0/40 use candid fake → both strong, candid fake stronger.
- **Step 4.** Candid fake = niche bend from travel into dev. Engineered photo of host with a glowing IDE-as-orb floating in their workspace.
- **Pick: Candid fake (#10).** Backup: Cinematic text (#6).

### Example 4 — "Why I burned out at 23 — what every founder hides"

- **Step 1.** Heavy / identity / psychological → Warped faces (#7) OR Anti-thumbnail (#11).
- **Step 2.** Channel is mentor / direct-to-camera; both fit.
- **Step 3.** Adjacent feed: 5/40 warped faces, 4/40 anti-thumbnail → both workable.
- **Step 4.** Anti-thumbnail with "53 seconds. The truth about burnout." pairs the time-constraint hook with the heaviness. Warped faces would also work, slightly higher friction for the mentor-tone channel.
- **Pick: Anti-thumbnail (#11).** Backup: Warped faces (#7).

## When to skip the picker

If the user explicitly names a style in the request ("design a neo-minimalist final frame for this short"), skip Steps 1-4 and go straight to Author mode. Document the choice in `notes.md` with `## Picked at [date], style chosen by user (no picker run)`.

If the channel has a signature style across all its Shorts (e.g., Dan Martell's anti-thumbnail consistency), respect the brand consistency over picker-output novelty. The picker is for new variants, not for forcing change on a working signature.
