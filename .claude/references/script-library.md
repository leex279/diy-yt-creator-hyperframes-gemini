# Script Library — Annotated Gold Standards

**Status:** v1.0 — 2026-04-28
**Lives in:** `.claude/references/script-library.md`
**Read by:** `/diy-yt-creator:phase2-script` (BEFORE drafting), `/diy-yt-creator:phase2-5-critique` (calibration), `new-anthropic-short.md` (legacy/quick-path)

---

## Why This File Exists

Voice rules tell you what *bad* looks like. This file shows you what *good* looks like.

Every script that has cleared the human "I'd post this" bar lives here, quoted verbatim, with per-paragraph annotations calling out the moves that worked. **Phase 2 MUST read the matching profile section before drafting a new script.** Copy the rhythm, not the words. The library is the goal; voice rules are the fence.

When a new script ships and the user calls it good, add it here. When you find yourself drifting toward a stat-dump or a fragment-only opener, re-read the matching example.

---

## Profile: news-explainer

Gold-standard reference for shorts that report on third-party announcements (deals, releases, acquisitions, industry shifts) where the narrator is curating, not building.

### Source

Single-pass Gemini Pro draft on the Anthropic / AWS $100B compute deal. Lives at `videos/anthropic-100b-deal/script.txt`. Quoted here verbatim:

> Anthropic just made one of the biggest AI hardware deals in history. And the numbers are absolutely insane. To keep Claude at the top, Anthropic just committed over one hundred billion dollars to Amazon Web Services... over the next ten years. They are securing up to five gigawatts of compute, using Amazon's custom Trainium chips. But Amazon is paying up, too. Amazon is investing another five billion dollars directly into Anthropic right now... with the option to invest up to twenty billion more. This builds on the eight billion they already put in. Why are they pouring so much money into this? Because Claude's growth is exploding. Anthropic just casually dropped that their revenue run-rate has hit thirty billion dollars... up from just nine billion at the end of last year. If you've noticed Claude being slow or buggy during peak hours, this is why. The new deal brings massive new compute online by the end of this year, to fix those growing pains. Plus, the full Claude Platform is launching directly inside A W S. Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news.

### Per-paragraph annotations

| Lines (verbatim) | What it does | Why it works |
| --- | --- | --- |
| "Anthropic just made one of the biggest AI hardware deals in history. And the numbers are absolutely insane." | **Magnitude framing** (claim + emotional amplifier). NOT a triple-stat slam. | The first sentence makes ONE big claim and earns the click. The second sentence promises payoff without dumping numbers yet. Curiosity is high; specificity is medium-by-design. |
| "To keep Claude at the top, Anthropic just committed over one hundred billion dollars to Amazon Web Services... over the next ten years." | **Explanatory connector** ("To keep …, Anthropic just …") + the headline number. | The connector "to keep" gives the deal a *reason* before stating the size. Reason-first beats number-first for retention. |
| "They are securing up to five gigawatts of compute, using Amazon's custom Trainium chips. But Amazon is paying up, too." | **Stake** + **Scroll-stop pivot** ("But Amazon is paying up, too"). | Sets up bilateral stakes — it's not just Anthropic's deal, AWS has skin in too. The "But" is the stun gun. |
| "Amazon is investing another five billion dollars directly into Anthropic right now... with the option to invest up to twenty billion more. This builds on the eight billion they already put in." | **Stat-stacking, but with context.** Each number anchors back to "investing another / option / already put in". | Numbers are connective, not declarative. Each stat is bolted to a verb that explains its role in the deal. |
| "Why are they pouring so much money into this? Because Claude's growth is exploding." | **Rhetorical question + answer** (`Why? Because …`) — explanatory connector pair. | This is the canonical narrative-flow pattern. Question raises a loop; "Because" closes it inside the same beat. Direct, specific, no fluff. |
| "Anthropic just casually dropped that their revenue run-rate has hit thirty billion dollars... up from just nine billion at the end of last year." | **Proof point with comparison baseline.** | "Hit X up from Y" is the proper way to deploy a number — anchor it to a prior point. "Just casually dropped" is voice (slightly conspiratorial, peer-to-peer), not hype. |
| "If you've noticed Claude being slow or buggy during peak hours, this is why." | **Direct viewer address (in body, NOT in CTA).** Canonical pattern: `"If you've [verb]ed X, [implication]"`. | This is the line that turns a press-release summary into a YouTube short. It assumes the viewer has lived experience with the product and routes the news to that experience. ONE such line in the body is enough. |
| "The new deal brings massive new compute online by the end of this year, to fix those growing pains." | **"Growing pains" callback** to the previous sentence. Implication closes a loop. | "Growing pains" wasn't introduced; it's reframing "slow or buggy during peak hours" the viewer just heard. Mini-loop close inside two sentences. |
| "Plus, the full Claude Platform is launching directly inside A W S." | **Connector ("Plus") + bonus stake.** | "Plus" signals "one more thing" without an explicit transition. Spelled "A W S" for TTS. |
| "Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news." | **Engagement CTA — three patterns in three sentences.** Rhetorical question + comments-ask + subscribe-ask. | The CTA template. Question creates a debate prompt; "let me know in the comments" routes the debate; "subscribe for more X news" is generic but expected and works. NOT hype, just plumbing. |

### What to learn (rhythm targets, not phrase copies)

1. **Magnitude-first opener, then numbers.** Frame the size of the thing in plain words before any stat lands.
2. **Every body sentence has a connector to the prior one.** "To keep …", "But …", "Because …", "Plus …", "If you've …", "And subscribe …". Count them — at least 5 in this script.
3. **One direct-address sentence in the body.** Not at the open, not at the close. Mid-script, applied to a specific viewer experience.
4. **Three-part CTA.** Question → comments-ask → subscribe-ask. Three sentences total, no outro padding.
5. **Numbers are bolted to verbs.** "Just committed", "are securing", "is investing", "is launching". Never a bare stat dropped on its own line.

### What NOT to copy (texture, not transcription)

- Don't reuse the phrase "And the numbers are absolutely insane." Once shipped, it's burned. Find your own emotional amplifier ("And the math is wild." / "The scale of this is hard to picture.")
- Don't reuse "Is X about to take over Y?" verbatim. Tailor the debate question to your topic.
- Don't reuse "growing pains". Pick a callback word that names *your* topic's friction.

The shape is the asset. The words are disposable.

---

## Profile: tutorial

*Placeholder.* Add a winning tutorial script here once one ships and the user calls it good.

The tutorial profile target rhythm is in `brand-voice-tutorial.md` (Short → Longer → Short → Opinion). Tutorials are *allowed* to be terse and fragment-heavy because the narrator is the practitioner — they don't need to explain why something matters across scenes; they're showing it. Different gates apply (Pass 6 of phase2-5-critique skips for tutorial profile).

When the first tutorial winner ships:

1. Quote the script verbatim here.
2. Annotate the moves that earned the click — per-scene observations, the scar moment, the term-branding example, the embedded truths.
3. List "what to learn" and "what NOT to copy" as above.

---

## How to Use

1. **Phase 2 (script writing) — MANDATORY READ.** Before applying any voice rules, read the section matching the brief's `voice_profile` field.
2. **Copy the rhythm, not the words.** Each annotated example is a rhythm template. Find your topic's equivalent of each annotated move.
3. **Phase 2.5 (critique) — calibration anchor.** When scoring a new script, the gates' threshold is "would this script's annotations look like the gold standard's?" If your script has fewer connectors than the example, that's a gap.
4. **Add to it.** When a script ships and the user calls it good, copy it in here under the matching profile, annotate per the existing pattern, and update the profile's "what to learn" list if a new pattern emerged.

---

## Updating This Document

This is a living document. Update it when:

- A shipped script earns the user's "I'd post this to YouTube" gut check → add as a new annotated entry under the matching profile.
- A pattern recurs across 3+ winners → lift it into the profile's `brand-voice-<profile>.md` rules.
- A new voice profile gets added (e.g., `comparison`) → add a new top-level Profile section here for it.
- An entry stops representing the current channel voice → strike through the entry with a note explaining what changed (don't delete — context matters for future writers).
