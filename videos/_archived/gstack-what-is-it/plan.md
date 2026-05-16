# Plan — gstack: what is it? do you need it?

**Format:** YouTube Short, 1080x1920 vertical, 30fps, target ~180s (3 min YouTube Shorts max).
**Template:** `templates/shorts/standard/` (warm-paper, brand-neutral).
**Lean:** Pure community-question framing. Present, don't preach. No editorial verdict.
**Source of truth:** `tmp/source.md` (gstack README + Garry transcript + community-comments themes).

## Constraints

- No direct/attributed commenter quotes. Themes only — no @handles, no quote marks.
- No ad-hominem attacks on Garry.
- No "ADHD CEO / autistic CTO" line from Garry's video.
- 89.1k stars number = README at fetch time (real). "More stars than Ruby on Rails" = Garry's claim from 3 weeks earlier — frame as his claim, don't repeat as fact.
- Dynamous outro is **insider-framed** (we're on the team).
- Step-by-step reveal rule applies to every list scene — items appear one at a time on their own beat.
- Shorts typography minimums apply (list-item primary 48px+, descriptor 30px+, hero slam 140px+, CTA pill 44px+).

## Scene order (10 scenes, ~180s)

| # | Scene archetype | t (s) | Duration | Purpose | Source line |
|---|---|---|---|---|---|
| 1 | Title | 0–8 | 8s | Hook — open with the question itself. "gstack — what is it? do you need it?" | Topic title |
| 2 | Stat | 8–22 | 14s | The receipt. "89.1k★" with "Garry Tan's open-source Claude Code skill pack" caption. | source.md §1 (README) |
| 3 | Bullets | 22–42 | 20s | What it actually is. 3 cards: "Slash commands for Claude Code" / "Specialist roles like a team" / "MIT, free, all markdown". | source.md §1 README tagline + "23 specialists / 8 power tools / MIT" |
| 4 | Counter grid | 42–62 | 20s | Surface area. 3 metrics: 23 specialists / 8 power tools / 28 commands. (We use the 28 number Garry himself states at 16:09 in the transcript.) | source.md §2 [16:09] + §1 README |
| 5 | Marker | 62–78 | 16s | What it does in practice. Headline with `/office-hours` highlighted: "It runs office-hours, plans, reviews, ships." | source.md §1 skill list |
| 6 | Quote | 78–105 | 27s | Theme 1 — what supporters say. NO @handles, NO quote marks. "Founders say it gets them from idea to plan faster" + supporting line "Office hours forces 6 questions before code." | source.md §3 positive themes |
| 7 | Quote | 105–132 | 27s | Theme 2 — what skeptics ask. NO @handles. "Skeptics ask: is this just Claude Code's /plan + /review wrapped up?" + supporting line "How is it different from BMAD or Spec Kit?" | source.md §3 skeptic themes |
| 8 | Quote | 132–152 | 20s | Theme 3 — what critics push back on. NO @handles. "Critics say: at the end of the day, it's markdown files." + supporting line "Stars don't equal usefulness." | source.md §3 critical themes |
| 9 | Marker | 152–168 | 16s | The community question — engagement bait. "Have you tried it? What are YOU using to ship faster?" | original framing |
| 10 | CTA | 168–180 | 12s | Dynamous community CTA — insider-framed. Short URL pill + "discuss it inside Dynamous" tagline. | per memory feedback_dynamous_insider_outro.md |

**Total runtime: 180s** (right at the YouTube Shorts cap).

## Hook variants for scene 1 (pick one in script phase)

- A. "gstack hit 89,000 stars in three weeks. So — what is it? And do you need it?" (uses the receipt + the question)
- B. "Garry Tan dropped gstack. It's everywhere. Some love it. Some don't. So — what is it?" (sets the split immediately)
- C. "Is gstack a virtual engineering team — or just markdown files? Let's look." (opens with the polarizing critique itself)

Recommend **A** — receipt-first is the cleanest honest opener. The split is implied by the rest of the structure.

## Retention strategy (placeholder until transcript lands)

| Beat | What holds attention |
|---|---|
| 0–8 | Question in the title is the hook. |
| 8–22 | Big number (89.1k★) gives a concrete receipt. |
| 22–62 | Step-by-step reveal of skills/specialists/tools — eye keeps moving. |
| 62–78 | Marker sweep on the keyword `/office-hours` is a visual punctuation. |
| 78–152 | Three perspective scenes (praise / skeptic / critic) use *the same scene archetype* — viewer feels the symmetry which signals fairness. |
| 152–168 | Direct address ("YOU using to ship faster?") + open question is the engagement-bait beat. |
| 168–180 | Dynamous CTA closes — short, insider, no hard-sell. |

After TTS lands, retiming will pull each `data-start` to the word-boundary in `transcript.json` per `phase3-5-retention`.

## Risk register (things that could go wrong, surfaced now)

- **Risk: 89.1k stars stale.** README was fetched 2026-05-04. Re-verify before render — if it has changed materially, update the stat scene.
- **Risk: scene 5 marker may overflow at 16s.** If the headline copy runs long after script gets tightened, may need to drop to 14s or shorten.
- **Risk: 27s quote scenes may feel slow.** If retention drops, plan B is to compress to 18–20s each in a re-cut.
- **Risk: Dynamous CTA at 12s is tight.** If the URL pill + tagline feels rushed, push to 14s and trim scene 8 by 2s.
