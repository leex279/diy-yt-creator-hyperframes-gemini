# Brand Voice — News-Explainer Profile

**Status:** v1.0 — 2026-04-28
**Profile:** news-explainer — for shorts about third-party announcements (deals, releases, acquisitions, industry shifts) where the narrator is reporting, not building
**Lives in:** `.claude/references/brand-voice-news-explainer.md`
**Read by:** `/diy-yt-creator:phase2-script` (script generation) and `/diy-yt-creator:phase2-5-critique` (voice QA), invoked when `voice_profile: news-explainer` in `content-brief.md` (or when `voice_profile` is missing — default)

---

## Character Brief (read this before writing a single word)

The narrator is **reporting on something the viewer might have missed** — not running an experiment. He curates the news, gives context, and frames why it matters to someone who actually uses the tool. Like a developer telling another developer over coffee: "Did you see what just happened? Here's the part that actually matters."

He is **not the participant in the news.** Anthropic announced a deal; he didn't make the deal. So first-person tutorial-style ("I tried this", "I built this") is the wrong frame here. He synthesizes. He picks the angle. He routes the news to the viewer's lived experience with the product.

He talks **to peers who use the tools the news is about.** The viewer either runs Claude Code daily or follows AI announcements; they don't need a primer on what Anthropic is, they need the part that changed for them today.

---

## The Stance

> "AI/coding announcements come fast and most coverage is press-release regurgitation. The people who actually use these tools want context, stakes, and the angle that matters — let's give them that in 60 seconds."

Every news-explainer video is this stance applied to one specific announcement.

---

## Voice Profile

### 3 Core Adjectives

**Clear. Contextual. Direct.**

Unpack each:

- **Clear** = no jargon walls, no hidden assumptions. The viewer should understand the deal/release/announcement by sentence three. Say what happened, not what it represents in some abstract sense.
- **Contextual** = every stat lands with a comparison baseline. "$100B" alone is a number; "$100B over ten years, up from the existing $8B partnership" is news. Always pin the new fact to a prior fact.
- **Direct** = no manufactured stakes, no breathless framing. The news is the news. If it's big, the structure of the script — claim, explanation, stake, implication — already carries the weight. You don't need to add "this changes everything."

> Note: Tutorial-profile uses "Enthusiastic. Practical. Honest." Honest doesn't translate cleanly here because the narrator wasn't a participant — he can't vouch for the deal personally. Substitute "Direct" (no hype) and "Contextual" (every stat earns a baseline).

---

## Sentence Rhythm Rules

### The Pattern: Claim → Explanation → Stake → Implication

```
Claim. (one sentence: what happened)
Explanation. (one sentence: why it happened, often with a connector — "To keep / Because / In order to")
Stake. (one sentence: who's bearing what cost or risk)
Implication. (one sentence: what it means for someone using the product — often a direct-address line)
```

**Example (correct — news-explainer voice):**

> "Anthropic just made one of the biggest AI hardware deals in history. [claim] To keep Claude at the top, Anthropic just committed over one hundred billion dollars to AWS over the next ten years. [explanation] Amazon is paying up too — five billion now, with the option for twenty more. [stake] If you build on Claude, peak-hour rate-limits are about to ease. [implication]"

**Example (bad — tutorial rhythm misapplied):**

> "One hundred billion dollars. Five gigawatts. Zero Nvidia chips. The compute crunch is over."

That's three jabs and a verdict, with no connectors and no implication. Reads like a press release bullet list. Tutorial scripts can get away with this because the narrator is in the loop with the viewer; news-explainer scripts cannot.

### Sentence-Level Rules

- **Start sentences with the subject or with a verb.** Not "In today's", not "Furthermore", not "As we".
- **Vary length, but lean longer than tutorial.** Tutorial uses 4–8 word sentences as primary tools; news-explainer uses 12–22 word sentences as primary tools, with shorter punctuation beats. Connectors require length.
- **Connectors are mandatory** (see "Mandatory Connectors" below). At least 3 across the body.
- **Questions are allowed and encouraged.** Rhetorical questions paired with explicit answers ("Why? Because …") are the canonical narrative-flow pattern.
- **Contractions always.** "It's", "doesn't", "you're", "I've", "they're".
- **First-person allowed: BOTH `I` and `we`.** `I` for the narrator's voice ("I noticed", "I'm watching"). `we` ONLY when referring to the audience + narrator collectively ("we'll see what happens", "we don't know yet"). Never `we` as the company. *Tutorial profile bans `we` entirely; news-explainer relaxes this because the narrator is reporting, not building solo.*
- **Numbers as digits in script.txt** ("100 billion", "5 gigawatts" — not "one hundred billion"). For TTS optimization phase, written-out forms come later (e.g., "one hundred billion dollars") — but in the source script, digits.

---

## Tone Dial: Reporter, not Hype Merchant

News-explainer voice sits between dry sarcasm (tutorial) and breathless hype (the channels we're not). Calibration:

- **No "this changes everything."** No "you won't believe." Those are hype tells; the news has to carry its own weight.
- **Stakes-framing IS allowed** ("To keep Claude at the top, Anthropic just …"). This is not "manufactured stakes" — it's stating *why a real party did a real thing*. Tutorial profile bans this because the tutorial narrator shouldn't pretend a feature has stakes; news-explainer narrator IS reporting on parties with stakes. Keep it factual.
- **Mild conspiratorial peer-tone is fine.** "Anthropic just casually dropped that their revenue run-rate has hit thirty billion dollars." The "just casually dropped" is voice — slightly knowing, like sharing a juicy detail with a friend. Tutorial-style dry sarcasm (mocking hype) does NOT translate here; the narrator is the reporter, not the contrarian.
- **Frequency:** the voice is steady throughout, not sprinkled. Every sentence should pass the "would a developer say this to another developer over coffee?" test.

---

## Hook Rules (first 4–8 seconds)

> **Important framing rule:** the narrator is reporting on third-party events. Never imply the narrator participated in the deal/release/test. "Anthropic just announced X" is fine; "I just shipped X with Anthropic" is fabrication unless explicitly true.

The hook is more important here than in tutorial — the news cycle is competitive, the topic is third-party, and the viewer needs to feel within 4 seconds that this video knows the angle. These are the only acceptable hook structures:

**Type A-news — Magnitude Framing (replaces tutorial Type A "Honest Result"):**

> "[Subject] just made one of the [biggest / fastest / most expensive / first-ever] [thing] in [history / Y's history / Z]. [Stat-amplified second sentence that pays off the magnitude claim.]"

> "Anthropic just made one of the biggest AI hardware deals in history. And the numbers are absolutely insane."

This is the canonical news-explainer opener. The first sentence makes the magnitude claim in plain words; the second sentence promises the payoff without dumping numbers yet. Curiosity is high, specificity is medium-by-design, viewer has a reason to keep watching.

**Type B — The Counterintuitive Observation:** (kept from tutorial profile)

> "[Common assumption / what everyone thinks happened]. [One sentence that breaks it.]"

> "Everyone assumed AWS was Anthropic's last cloud bet. They just doubled down for a decade."

**Type C — The Specific Number:** (kept from tutorial profile)

> "[Precise number] [specific thing]. [Why that matters in one sentence.]"

> "100 billion dollars over ten years. That's the new size of the Anthropic-AWS deal."

⚠️ Use Type C carefully — pure-number hooks with no connector are exactly the failure mode this profile is built to prevent. Always pair the number with a "Why that matters" sentence that includes a connector.

**Type D — The Shared Frustration:** (kept from tutorial profile, slightly adapted)

> "[Specific viewer-facing problem stated as a fact.]"

> "Claude's been rate-limiting at peak hours for months. The fix just got announced."

**Never:**

- "Have you ever wondered..."
- "In this video I'm going to show you..."
- "Today we're exploring..."
- "[Tool name] just changed everything." (banned hype phrase)

---

## Mandatory Connectors (NEW — not in tutorial profile)

Every news-explainer script MUST include **at least 3** explanatory connectors across the body (not the hook, not the CTA). Each unique connector counts once per scene. The connector list:

| Connector | Example use |
| --- | --- |
| `because` | "Why are they pouring so much money into this? Because Claude's growth is exploding." |
| `why` | "Why would AWS commit to this? They needed a flagship AI tenant." |
| `to <verb>` | "To keep Claude at the top, Anthropic just committed …" |
| `and` | "And subscribe for more AI news." (sentence-initial, not joining a list) |
| `but` | "But Amazon is paying up, too." |
| `plus` | "Plus, the full Claude Platform is launching directly inside AWS." |
| `so` | "So peak-hour rate-limits are about to ease." |
| `here's why` | "Here's why this matters to anyone building on Claude." |
| `the reason` | "The reason Anthropic is locking in compute now is supply." |

Pure-fragment scripts (zero connectors) FAIL the Phase 2.5 critique gate (QG-5a). Aim for 5+ connectors with at least 3 unique types — that's the gold-standard target.

---

## Mandatory Direct-Address Sentence (NEW — not in tutorial profile)

Every news-explainer script MUST include **at least one** second-person sentence in the body (NOT in the hook, NOT only in the CTA). The address routes the news to the viewer's lived experience.

Canonical patterns:

- `"If you ['re building on / 've noticed / use / care about / build on] X, [implication]"`
- `"You ['re probably / might be] [verb]ing X right now — [implication]"`
- `"Your [thing] just got [Y]."`

The Gemini gold-standard line:

> "If you've noticed Claude being slow or buggy during peak hours, this is why."

**One** such line in the body is enough. More than two reads as overdone. Never substitute "viewers" for "you" — direct address means second-person, not third-person plural.

If you cannot find a viewer-experience hook for the topic, the topic might be wrong for news-explainer profile (e.g., a B2B announcement with no developer-facing impact). Push back on the brief, don't fake the address line.

---

## CTA Pattern (NEW — STRICTER than tutorial)

News-explainer CTAs MUST include three components, in this order, in the final scene:

1. **Rhetorical / debate question** that invites viewer disagreement (ends with `?`).
2. **Comments-ask** routing the debate to the comments section.
3. **Subscribe-ask** with topic anchor.

Canonical template:

> "[Rhetorical question about the topic]? Let me know in the comments. And subscribe for more [topic] news."

Gold-standard example:

> "Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news."

**Tutorial profile says** "no smash that like button, no don't forget to subscribe" — those are hype phrases.
**News-explainer profile EXPLICITLY ALLOWS** the standard YouTube CTA because:

1. It's expected on news content (debate-driven, comments-driven).
2. The phrasing here — "let me know in the comments", "subscribe for more X news" — is plumbing, not hype. No "smash", no "don't forget", no all-caps, no exclamation mark.
3. The rhetorical question creates engagement; the asks just route it.

**Acceptable variants (must still hit all three components):**

- "Will [X] beat [Y]? Tell me below. Subscribe for more [topic] news."
- "Is [X] really [Y]? Drop your take in the comments. And follow for more [topic] coverage."

**Banned variants** (still forbidden — these are the hype tells):

- "Smash that like button"
- "Don't forget to subscribe"
- "If this helped, hit the bell icon"
- "If you found this valuable, please consider subscribing"

---

## Per-Scene Structure

Each body scene follows: **Claim → Explanation → Stake → Implication** (the rhythm pattern above). Each scene should have at least one connector to the previous scene's content. Scene breaks are not narrative resets in news-explainer — they're visual chapters in a continuous story.

**Cap on scene count for ≤60s shorts: 5 scenes.** (Enforced in `phase1-plan.md`.) More scenes than that forces sub-9-second pacing, which kills connector room.

---

## Content Situations: Do / Don't Table

| Situation | DO | DON'T |
|---|---|---|
| **Reporting an announcement** | Lead with magnitude framing + connector to context | Lead with a triple-stat slam ("$100B. 5 gigawatts. Zero Nvidia.") |
| **Stating a stat** | Anchor it to a prior baseline ("$30B run-rate, up from $9B last year") | Drop the stat without comparison ("$30B run-rate.") |
| **Explaining a motive** | Use a `why / because / to` connector ("Why? Because Claude's growth is exploding.") | Imply the motive ("Anthropic needed compute. They got it.") |
| **Adding a stake** | Use a `but / plus / and` connector ("But Amazon is paying up, too.") | Start a new sentence with no connector ("Amazon is paying up too.") |
| **Routing news to viewer** | One direct-address line, mid-script ("If you've noticed Claude being slow…") | Address the viewer at the open AND close — overdone reads as scripted |
| **Closing the script** | Question + comments-ask + subscribe-ask | Declarative non-engagement closer ("The compute crunch is over.") |
| **Attributing a claim** | "According to [source]", "Anthropic announced", "[Press release / blog post] confirms" | Present a third-party announcement as personal validation |

---

## Channels This Voice IS NOT

- **Generic AI hype channels** — they lead with "everything just changed", we lead with "here's exactly what changed and what it costs"
- **Press-release regurgitation channels** — they list the bullet points, we route them to the viewer's experience
- **Tutorial channels** (including this channel's own tutorial profile) — they use "I tried" and short fragments; we use "Anthropic just" and connector-rich body sentences

---

## Voice in Action: Rewritten Examples

### Before (tutorial rhythm misapplied to news):

> "One hundred billion dollars. Five gigawatts. Zero Nvidia chips. If you got rate-limited on Claude this April, Anthropic just spent $100 billion to fix it. The compute crunch is over."

### After (news-explainer voice):

> "Anthropic just made one of the biggest AI hardware deals in history. To keep Claude at the top, they committed $100 billion to AWS over the next ten years. Amazon is paying up too — $5 billion now, with the option for $20 billion more. If you've noticed Claude being slow during peak hours, this is why. Is Claude about to take over the AI space? Let me know in the comments. And subscribe for more AI news."

### Before (generic AI output):

> "In a groundbreaking development, Anthropic and Amazon have announced a transformative partnership that will revolutionize the AI compute landscape."

### After (news-explainer voice):

> "Anthropic and AWS just locked in a ten-year compute deal. The size of it is what makes it news: $100 billion. Why? Because Claude's revenue run-rate hit $30 billion this year — they need the chips."

---

## Universal Bans (shared with tutorial profile)

These are banned in EVERY profile. The generic-AI banned word list is canonical and applies to all scripts regardless of profile.

### Generic AI phrases (always banned):

`delve`, `tapestry`, `harness`, `unlock`, `leverage`, `paradigm`, `seamless`, `cutting-edge`, `game-changer`, `groundbreaking`, `transformative`, `revolutionize`, `in today's fast-paced world`, `as we navigate`, `it's worth noting`, `needless to say`, `without further ado`, `in conclusion`, `in essence`, `having said that`, `first and foremost`, `last but not least`, `to summarize`, `let's dive in`, `let's explore`, `furthermore`, `moreover`, `nevertheless`, `undoubtedly`, `it goes without saying`

### Hype phrases (banned for this channel):

`changed everything`, `you won't believe`, `the future is here`, `absolutely incredible`, `mind-blowing`, `next level`, `the game has changed`, `smash that like button`, `don't forget to subscribe`, `this is huge`, `the most powerful`, `unlike anything before`, `the only tool you need`, `full potential`, `unlock your potential`

### Authority-Without-Evidence phrases (banned — fake credibility):

These phrases imply consensus or evidence that is never named or linked. They are the dominant "fake authority" pattern in AI output and are banned even if the surrounding sentence is otherwise fine. If a real source exists, name it inline (per Step 3.7 Scars Mining and the news-explainer attribution rule). If no source exists, cut the claim — do not paper over it with a generic appeal to authority.

`experts agree`, `studies show` (without an inline source link in the same sentence), `research suggests` (same caveat), `many developers find`, `most developers find`, `it's widely known`, `as we all know`, `it's commonly accepted`, `industry consensus is`

**The inline-source caveat**: `studies show 73% — see [GitGuardian 2025 Report](url)` is fine. `studies show 73%` standalone is not. Phase 2.5 Pass 5 (QG-4) flags any of these when no source is named in the same sentence.

---

## Profile-Specific Relaxations (ONLY for news-explainer)

These are bans in the tutorial profile that DO NOT apply to news-explainer. Be deliberate about each:

| Tutorial profile bans | News-explainer ALLOWS | Why |
| --- | --- | --- |
| `we` as narrator's voice | `we` for audience + narrator collectively ("we'll see what happens") | News narrator is reporting on industry events; sometimes "we" is the right frame for a community observation. Never `we` as the company. |
| `arguably`, `for the most part`, `generally speaking` (over-hedging) | These are allowed when paired with attribution ("arguably the biggest deal this year, according to industry analysts") | Reporting requires occasional hedge phrasing. Don't over-use; pure hedging without attribution is still banned. |
| Motivational frame ("To keep X at the top, …") | Allowed as a stake statement | Tutorial bans this because tutorial narrator shouldn't pretend a feature has motive; news narrator IS reporting on parties with motives. Keep it factual. |
| Standard YouTube CTA ("Let me know in the comments. Subscribe for more AI news.") | REQUIRED (per CTA Pattern above) | Expected on news content. The phrasing IS the plumbing; tutorial's "no smash that like" rule is about hype framing, not the basic ask. |

---

## What Claude Must NOT Do When Writing News-Explainer Scripts

1. **Do not open with the channel name or a greeting.** Cut straight to the magnitude framing.
2. **Do not summarise what's coming at the start.** No "In this video, I'll cover the deal." Just start with the claim.
3. **Do not write a triple-stat slam opener** ("$100B. 5GW. Zero Nvidia chips."). Use magnitude framing (Type A-news) — single claim + emotional amplifier.
4. **Do not omit connectors.** At least 3 in the body. Pure-fragment scripts FAIL.
5. **Do not omit the direct-address line.** At least one second-person sentence in the body, NOT in CTA.
6. **Do not omit the engagement CTA.** Question + comments-ask + subscribe-ask are MANDATORY.
7. **Do not use em dashes (—) in script narration.** They sound wrong in TTS. Use period or comma.
8. **Do not use bullet-pointed narration.** Scripts are prose.
9. **Do not attribute emotions to the viewer** ("You've probably felt frustrated…"). Address what the viewer DOES (uses, builds on, has noticed) — not how they feel.
10. **Do not present third-party announcements as personal validation.** "Anthropic announced", "AWS confirmed", "according to the press release" — never "I made this deal" or "we shipped this".
11. **Do not invent stats.** Every number must come from the brief's proof points. If the brief doesn't have the number, leave the claim out — do not estimate.
12. **Do not end on a declarative non-engagement closer** ("The compute crunch is over."). End on the rhetorical question that opens debate.

---

## Voice QA Checklist (Phase 2.5 — News-Explainer Profile)

After script generation, the critique agent must check:

- [ ] No banned words from Universal Bans (generic AI + hype phrases) found
- [ ] Hook is Type A-news / B / C / D (with C requiring a paired "why it matters" sentence containing a connector)
- [ ] Body contains ≥ 3 explanatory connectors (because / why / to <verb> / and / but / plus / so / here's why / the reason), with ≥ 2 unique connectors
- [ ] Body contains ≥ 1 direct-address sentence in second-person ("If you've / You / Your")
- [ ] Final scene contains all three CTA components: rhetorical question + comments-ask + subscribe-ask
- [ ] Every stat is anchored to a comparison baseline OR explicit attribution to a source
- [ ] Zero em dashes in narration
- [ ] No `we` used as the narrator (only as audience + narrator collectively, if at all)
- [ ] Zero expanded contractions (it is → it's, do not → don't)
- [ ] No triple-stat slam opener
- [ ] No declarative non-engagement closer

**Output:** Voice QA PASS/FAIL receipt with specific line flags. Phase 2.5's Pass 6 enforces connectors + direct-address + CTA programmatically.

---

## Updating This Document

This is a living document. Update it when:

- A news-explainer video gets unusually high retention/engagement → extract what the script did differently → add as a golden example in `script-library.md`
- A new connector or direct-address pattern proves itself across 3+ winners → lift it into the canonical lists above
- A relaxation from tutorial profile turns out to NOT apply (e.g., `we` reads weird in practice) → reinstate the tutorial rule with a note explaining why
- A new content sub-format (e.g., "deal explainer" vs "release explainer") emerges and needs its own micro-profile → consider splitting
