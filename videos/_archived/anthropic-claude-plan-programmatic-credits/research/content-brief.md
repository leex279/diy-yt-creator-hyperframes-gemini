# Content Brief: Anthropic — Claude Plans Get Programmatic Credits + 50% Code Boost

## Video Metadata
- **Slug**: `anthropic-claude-plan-programmatic-credits`
- **Template**: shorts/anthropic
- **Duration**: 180s (long-Short, use full budget per source §5)
- **Tone**: News-explainer, fast-paced, punchy, slightly skeptical edge (per source §5)
- **Topic Type**: ARTICLE_RESPONSE — primary X-thread + secondary X-posts (ClaudeDevs)
- **Research Depth**: SOURCE-ONLY (no WebSearch / WebFetch — `tmp/source.md` is the entire truth)
- **WPM Target**: 160–170 → script budget ≈ 480–510 words (Phase 1 refines)

---

## 1. Topic & framing

Anthropic just announced two stacked changes to paid Claude plans, and the framing they DIDN'T put in the headline is the actual story. Starting **June 15**, every Pro / Max / Team / Enterprise plan gets a dedicated **monthly programmatic-usage credit** that covers the Agent SDK, `claude -p`, Claude Code GitHub Actions — and, the quietly-bigger beat, **third-party apps built on the Agent SDK like Conductor and OpenClaw**. On top of that, Claude Code weekly limits are **+50% through July 13**, already applied, no opt-in needed. This video is a fast news-explainer with a skeptical edge: who actually wins from this, and is "third-party tools draw from your plan" a quiet platform play or a backdoor price hike? (Source §1, §2, §6)

---

## 2. Headline news (T1 facts — verbatim-traceable)

- **New monthly programmatic credit** lands on paid Claude plans on **June 15**. (Source §1 Post 1)
- **Four covered surfaces** for the credit:
  - Claude **Agent SDK** (Source §1 Post 1)
  - `claude -p` (Source §1 Post 1)
  - **Claude Code GitHub Actions** (Source §1 Post 1)
  - **Third-party apps built on the Agent SDK** (Source §1 Post 1)
- **Third-party shift named explicitly**: tools like **Conductor** and **OpenClaw** now work with your Claude plan and **draw from your credit the same way your own scripts do**. (Source §1 Post 2)
- **Timeline announced**:
  - *Today / nothing to do today.* (Source §1 Post 3)
  - **June 8** — users get an email to claim their credits. (Source §1 Post 3)
  - **June 15** — the change goes into effect. (Source §1 Post 3)
- **Plans covered**: **Pro, Max, Team, and seat-based Enterprise** (intersect of both threads, §3).
- **Reference URL on screen**: `support.claude.com/en/articles/15036540` (Source §1, end of section).

---

## 3. Bonus stack (T2 facts)

- **Claude Code weekly limits are 50% higher through July 13** — announced alongside the credits beat. (Source §2 Post A + quote image)
- **All surfaces**: CLI, IDE extensions, desktop, and the web. (Source §2 Post B bullet 1)
- **Live now**; runs through **July 13 at 6PM PDT / 1AM GMT**. (Source §2 Post B bullet 2)
- **Nothing to opt into** — already applied. (Source §2 Post B bullet 3 + quote image)
- **Stacks with the 2× increase to 5-hour limits announced last week.** (Source §2 Post B bullet 4)
- **Plans covered**: Pro / Max / Team / Enterprise (seat-based). (Source §2 Post A)

---

## 4. Why this matters / the angle

The "+50% weekly limits" is the eye-catching number, but the third-party twist in Post 2 is the actually-new thing. Until now, building on Anthropic's Agent SDK from a paid Claude plan meant your *own* scripts only. The June 15 change makes external tools — **Conductor**, **OpenClaw**, anything built on the Agent SDK — first-class citizens that *pull from the same credit pool*. That's a platform move: it makes the paid Claude plan a substrate for a whole ecosystem of programmatic clients, not just a chat seat. The skeptical edge: is this a generous unlock, or a quiet way to migrate heavy programmatic users off raw API billing onto a more predictable seat-credit bucket? Both readings are defensible from the source — that tension is the hook. (Source §1 Post 1+2, §4 critical bucket)

---

## 5. Community sentiment landscape

Anonymized handles invented for Phase 2/4 consistency: **@devanon1, @builderx, @skeptic42, @cardholder, @oldschool, @buildermax, @cynicop**. Real handles in the source are not used. Per source §4, f-bombs paraphrased for TTS.

### Positive / pragmatic (Source §4 "Positive / pragmatic")
- **@cardholder** — "Makes the paid plan easier to justify to whoever approves the card."
- **@builderx** — "Anthropic quietly making it easier to go from idea to production."
- **@buildermax** — "Codex effect is real. Glad to see competition finally forcing some credits out of the vault."

### Confused / wanting clarity (Source §4 "Confused / wanting clarity")
- **@devanon1** — "Explain it like I'm normal."
- **@oldschool** — "So we're all being charged for hooks?"
- **@skeptic42** — "Does previous usage remain the same alongside monthly credits?"
- **@cynicop** — "The fuzzy bit: what counts as programmatic vs interactive when SDK and CLI mix?"

### Critical / angry (Source §4 "Critical / angry") — f-bomb line paraphrased per §4 note
- **@skeptic42** — "🫠"
- **@cynicop** — "This is how you know when a startup becomes enterprisey."
- **@oldschool** — "Your competitors will thank you. Genius way to reduce capacity constraints by relocating customers." *(paraphrased per source §4)*
- **@buildermax** — "Team standup: 'Everyone's upset about subscriptions. Quick — three ideas to make it worse!'" *(paraphrased per source §4, sarcastic)*

### Constructive (Source §4 "Constructive")
- **@devanon1** — "Build a proper ralph loop and Linear integration into Claude Code and we won't need external programmatic usage."

> **Handle assignment is a Phase-2/4 convention** — Phase 2 must use these exact placeholders so on-screen cards (Phase 4) match the spoken narration. Re-using the same handle across two quotes is intentional and reads natural for a montage.

---

## 6. Audience pain points & desires (grounded in §4 reactions)

### Pain points
1. **Confusion about programmatic vs. interactive** — the boundary is real and unaddressed by the post. (Source §4 — @cynicop "what counts as programmatic vs interactive when SDK and CLI mix")
2. **Hidden cost creep** — users worry credits replace, not add to, existing usage. (Source §4 — @skeptic42 "Does previous usage remain the same alongside monthly credits?")
3. **Fear of "enterprisey" pivot** — paid users on smaller plans wonder if this is a tier-up funnel. (Source §4 — @cynicop "startup becomes enterprisey", @oldschool relocating-customers paraphrase)

### Desires
1. **Easier card-approval story for paid plans** — a single seat plan that covers programmatic work simplifies expensing. (Source §4 — @cardholder "easier to justify to whoever approves the card")
2. **Production-ready path without API ops** — go from idea to shipped agent without leaving the seat plan. (Source §4 — @builderx "idea to production")
3. **Native integrations that reduce reliance on external tools** — a built-in loop+Linear story would shrink the third-party stack. (Source §4 constructive — @devanon1 ralph loop + Linear)

---

## 7. Hook angle candidates

Three patterns the script can pick from. None invents stats — every payload is source-traceable.

1. **Stat-led / scale punch** — *"+50% on Claude Code. Plus a new monthly credit. One catch."*
   - Payload: §2 (+50% / July 13) + §1 (monthly credit) + §1 Post 2 (third-party tools draw from YOUR credit).
   - Why it works: opens on the biggest number, immediately pivots to the "what's the catch" beat.

2. **Contrarian / "the headline is hiding something"** — *"Anthropic just changed who you're paying for."*
   - Payload: §1 Post 2 — Conductor and OpenClaw now draw from your Claude plan credit. The implication (without inventing): heavy third-party tool users are quietly being moved onto seat-plan economics.
   - Why it works: hooks on a provocation that holds up under the source's own framing.

3. **Mystery question / Q-pivot** — *"What do Conductor, OpenClaw, and your own Python script suddenly have in common?"*
   - Payload: §1 Post 1+2 — all four covered surfaces share a single credit on June 15.
   - Why it works: forces a 3-second curiosity hold; resolves with the four-surfaces reveal.

---

## 8. CTA candidates (debate-sparking)

Verbatim from source §7:

1. **"OpenClaw and Conductor on your plan — game changer or backdoor price hike?"**
2. **"Programmatic credits — overdue win, or first sign Anthropic is going enterprisey?"**
3. **"Credits good enough to switch off Codex — yes or no?"**

### Recommended pick (Phase 1 locks it)

**#1 — "OpenClaw and Conductor on your plan — game changer or backdoor price hike?"**

Why this wins the engagement-CTA rule's four criteria:

- **Binary-or-short-list**: two-option pick (game changer / backdoor) — answerable in 3 words.
- **Polarizing stance baked in**: "backdoor price hike" forces a defend-or-attack reflex; pure neutrals will get pushed off the fence.
- **References a specific claim from the video**: directly cites the third-party shift (Source §1 Post 2 — Conductor + OpenClaw named) which the video makes its lead beat.
- **Low cost to answer**: senior dev and first-week builder can both fire off an opinion in 5 seconds.

#2 is also strong (and a fair backup if Phase 1 decides "enterprisey" is the better framing) — but #1 anchors to a CONCRETE artifact (two named tools) which makes the comment thread richer. #3 fails the "low cost" test slightly — assumes the viewer knows Codex enough to compare.

---

## 9. Must-mention checklist (Phase 2 enforcement)

Verbatim items from the source that the script MUST include:

- [ ] **Four covered surfaces** named — Claude Agent SDK, `claude -p`, Claude Code GitHub Actions, third-party apps built on the Agent SDK (Source §1 Post 1).
- [ ] **Conductor** and **OpenClaw** named explicitly as examples (Source §1 Post 2).
- [ ] **June 8** date for the claim email (Source §1 Post 3).
- [ ] **June 15** date for the change going live (Source §1 Post 3).
- [ ] **Plans covered**: Pro, Max, Team, Enterprise (seat-based) (Source §3).
- [ ] **Support URL on screen**: `support.claude.com/en/articles/15036540` (Source §1 end).
- [ ] **Claude Code weekly limits +50% through July 13** (Source §2 Post A + quote image).
- [ ] **Already applied / nothing to opt into** for the +50% (Source §2 Post A image + Post B bullet 3).
- [ ] **All surfaces (CLI, IDE extensions, desktop, web)** for the +50% (Source §2 Post B bullet 1).
- [ ] **Stacks with last week's 2× 5-hour limit increase** (Source §2 Post B bullet 4).
- [ ] **CTA question** appears in spoken closer + on-screen `#cta-question` + YouTube description final paragraph (Source §7 + repo rule `engagement-cta.md`).

---

## 10. Visual / registry suggestions

Reference: `.claude/rules/registry-blocks-catalog.md` (project-local catalog of installable blocks).

- **`x-post` block** (Social media overlays family) — perfect for the **community-reactions montage** phase (P7 in the suggested 9-phase arc). 5–6 anonymized reaction cards cycling through, mixing positive/critical/confused buckets. (Source §6 phase 7, §8.)
- **`macOS-notification` block** (Animation & effects family) — lands the **"email on June 8"** beat as a desktop-style notification banner sliding in. Single beat, dismisses, transition to June-15 reveal. (Source §6 phase 5, §8.)
- **Shader transitions** between phases — `flash-through-white`, `whip-pan`, `light-leak` for the fast news-explainer cadence. Use sparingly — one or two distinct transition types max so the cuts feel intentional. (Source §8.)
- **Shape-backdrop reposition on every phase transition** — repo-default behavior per memory rule, paired with cinematic-whoosh SFX. (Source §5 hard constraints.)

Do NOT invent block names — every block listed above traces to the registry catalog file.

---

## 11. Open questions / gaps (Phase 2 must NOT fabricate around these)

The source does NOT answer these. Phase 2 either omits them or names them as open questions on-screen ("Anthropic didn't say"):

- **Exact credit dollar amount or token volume per tier** — not stated. Source only says "a dedicated monthly credit for programmatic usage" (§1 Post 1).
- **Whether the credit replaces or stacks with existing usage allowance** — explicitly raised by @skeptic42 in §4, unanswered by source.
- **Whether the 2× 5-hour limit increase also gets +50%** — Source §2 Post B bullet 4 says "stacks with" but doesn't specify the per-window math.
- **Conductor / OpenClaw pricing details, their own subscription tiers, or how their billing changes** — entirely outside scope.
- **Whether non-paid (free) Claude users get any version of this** — not addressed; "paid Claude plans" is the only scope language used.
- **Roadmap beyond June 15** — no future commitments mentioned in the source.
- **Definition of "programmatic vs. interactive"** — explicitly flagged by @cynicop in §4 community quotes, NOT defined in posts.

These are **block-the-script-from-fabricating** gaps, not workflow blockers. Phase 2 should script around them.

---

## 12. Anti-fabrication ledger (the script MUST NOT claim)

Per memory rule `feedback_no_fabrication_source_only`, the script MUST NOT claim:

- Any specific dollar amount, token amount, or message-count for the new credit.
- Any specific rate-limit numbers (e.g., "from X requests/week to Y") for the +50% beat.
- Any pricing, feature, or comparison detail about **Conductor** or **OpenClaw** beyond "they're third-party tools built on the Agent SDK" (Source §1 Post 2).
- Any pricing, feature, or comparison detail about **Codex** beyond what's in source §4 (a single user reference to "the Codex effect" — that's the entire mention).
- Any specific timeline beyond June 8 / June 15 / July 13 / "today" / "last week".
- That this announcement is a response to specific competitor moves (the user reaction names "Codex" but that's commentary, not an Anthropic claim).
- That the +50% is permanent or will renew (source says "through July 13" — a defined window).
- Any claim about other plans (e.g., free, Education) or about which Enterprise sub-tiers qualify (source says "seat-based Enterprise" only).
- Any speculation about *why* Anthropic shipped this (no "to compete with X" framing).
- Any real X handles, follower counts, or quote attribution — anonymized handles in §5 are the only source.

---

## Reference: 9-phase arc & hard constraints

Already specified by source §5 + §6 — Phase 1 will refine, but the bones are:

| #  | Phase                          | Window      | Visual anchor                                  |
|----|--------------------------------|-------------|------------------------------------------------|
| 1  | Thumbnail-grade open           | 0–2.5s      | Topic + date + brand (Anthropic + Claude)      |
| 2  | Hook pivot                     | 2.5–12s     | Four covered surfaces, fast-cut reveal         |
| 3  | The shift explained            | 12–40s      | Conductor + OpenClaw — third-party twist       |
| 4  | Who gets it                    | 40–60s      | Pro / Max / Team / Enterprise pill row         |
| 5  | Timeline                       | 60–80s      | Today → June 8 (email) → June 15 (live)        |
| 6  | Bonus stack                    | 80–110s     | +50% Claude Code weekly limits through July 13 |
| 7  | Community reactions montage    | 110–150s    | 5–6 anonymized x-post cards cycling            |
| 8  | The big question               | 150–170s    | Debate framing — enterprisey vs. win-for-builders |
| 9  | Thumbnail-grade close          | 170–180s    | Recap + brand + CTA question on screen         |

Hard constraints (verbatim from source §5):

- Thumbnail-grade FIRST frame at t=0 (no fade-in, dominant topic visible).
- Thumbnail-grade FINAL frame held ≥1.5s before composition ends.
- Engagement CTA in 3 places (spoken + on-screen + description), binary-or-short-list answerable.
- Anonymize all community handles; paraphrase f-bombs.
- Phase-mutex Anthropic shorts pattern (no sub-comps unless needed).
- Shape-backdrop reposition on every phase transition.
- Visual-pacing-5s rule (every phase has a beat at least every 5s).
- Step-by-step-reveal for list rows (Pro/Max/Team/Enterprise, reactions).
- Heteronym audit before TTS (`live → available`, `lead → primary`, etc.).
- Shorts typography minimums: ≥48px list items, ≥36px descriptors, ≥140px hero slam.

---

## Sources

| Source | Where | Used For |
|--------|-------|----------|
| ClaudeDevs primary thread (Posts 1–4) | `tmp/source.md` §1 | T1 facts: credit launch, four surfaces, third-party tools, timeline |
| ClaudeDevs secondary posts (A + B) | `tmp/source.md` §2 | T2 facts: +50% weekly limits, surfaces, dates, stacking |
| Plans covered (intersect) | `tmp/source.md` §3 | Pro/Max/Team/Enterprise reach |
| Community reactions | `tmp/source.md` §4 | Four-bucket sentiment quotes (positive / confused / critical / constructive) |
| Hard constraints | `tmp/source.md` §5 | Tone, duration, voice profile, anonymization, repo-rule overlay |
| 9-phase arc suggestion | `tmp/source.md` §6 | Phase mapping |
| CTA candidates | `tmp/source.md` §7 | Three debate-sparking questions |
| Registry picks | `tmp/source.md` §8 | x-post, macOS-notification, shader transitions |
| Brand palette pointer | `tmp/source.md` §9 | tokens already in templates/shorts/anthropic |
| Support URL | `tmp/source.md` §1 end | On-screen reference URL |

**No external sources used.** Per the ARTICLE_RESPONSE memory rule, every fact, stat, quote, URL, and bullet in this brief traces back to `tmp/source.md`.
