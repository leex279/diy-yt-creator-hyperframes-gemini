# The Faceless Tech Scriptwriting Playbook

> Engineering high-retention narrative for developer audiences with TTS narration and programmatic animation.

**Sources**: 77-video internal audit (964 scene files), NotebookLM creator transcript analysis, Kallaway retention formula, 6 Story Locks framework.

**How to use this document**: This is the generic scriptwriting voice reference. Phase 2 (`phase2-script.md`) references it during writing alongside `.claude/references/brand-voice.md` (the channel-specific narrator spec — overrides this where they differ). Phase 2.5 (`phase2-5-critique.md`) enforces both via QG-4.

**File path**: `.claude/references/faceless-tech-scriptwriting-playbook.md`

**Cross-reference fix-up**: Some sections below (§15 and the Appendix) point to file paths like `.claude/rules/scriptwriting.md` or `src/shared/components/retention/`. Those paths are placeholders — equivalent guidance in this repo lives in:
- `.claude/references/brand-voice.md` — channel-specific voice rules + 50-word banned list
- `.claude/references/retention-components-hyperframes.md` — HyperFrames retention vocabulary
- The individual phase command files under `.claude/commands/diy-yt-creator/` (e.g. Kallaway formula in `phase2-script.md`, quality gates in `phase2-5-critique.md`)

---

## 1. Retention Mechanics for Faceless Content

Without a face, there is no charisma shortcut. Every second of retention must be engineered through the script and visuals working together.

### The Personality Gap

In talking-head content, personality carries ~50% of retention (facial expression, vocal improvisation, body language). We have none of that. The script must compensate by being:
- **Denser** — every sentence must advance the narrative or create tension
- **More rhythmic** — sentence length variation replaces vocal variation
- **More visual** — the script must cue animation beats that replace facial reactions

### Visual-Audio Synchrony

The "Thumbnail-to-First-5-Seconds" rule: the opening visual must mirror the thumbnail to validate the click. This bypasses the viewer's "clickbait detector" before the first sentence finishes.

- **Shot frequency**: Change the visual every 1.7-2 seconds. In the first 30 seconds, aim for ~15-19 distinct visual states.
- **Stale visual cap**: No more than 20% of the first 30 seconds can be static or generic (plain background, unchanged diagram).
- **Every frame reinforces the topic** — no decorative filler shots.

### The Valley of Death (Minutes 3-6)

This is where initial curiosity dies. Two defenses:

1. **Sunk Cost Lever**: By minute 3, subtly reference the time invested. "We've covered the basics — now the part that actually matters." The viewer feels resistance to dropping off because they've already invested.
2. **Mid-Video Re-Hook**: At 55-65% of runtime, deploy a 3-5 sentence re-engagement passage that re-opens the primary curiosity gap. This is mandatory (see `.claude/rules/scriptwriting.md` §Mid-Video Re-Hook Rule).

### Attention Reset Cadence

- **Every 40 seconds**: Shift between "zoom in" (technical detail) and "zoom out" (big picture impact)
- **Every 60-90 seconds**: Deploy a Loop Opener (Story Lock #5) to reset the curiosity clock
- **At 55-65% runtime**: Deploy the Mid-Video Re-Hook

---

## 2. Script Structure Frameworks

### The "But/Therefore" Rule (Narrative Causality)

Every narrative beat must be a consequence of the previous one. "And then" sequences let viewers exit at any point. "But/Therefore" chains create logical necessity.

| Weak ("And Then") | Strong ("But/Therefore") |
|---|---|
| We deployed the cluster. And then we configured ingress. And then we checked logs. | We deployed the cluster. But the ingress controller failed DNS. Therefore we refactored the routing logic. But this exposed a security loophole. |

### Framework by Video Type

| Video Type | Best Structure | Why |
|---|---|---|
| Deep dive (single tool) | Why-What-How | Answer the "Assumptive Question" first, then teach |
| Changelog recap | Problem → Fix → Impact (per feature) | Each feature is a mini-story, not a bullet |
| Comparison/versus | Setup-Tension-Payoff per tool, then verdict | Honest tradeoffs build trust (see Honest Comparison rule) |
| 60-second Short | One claim → one proof → one CTA | No room for structure — density is the structure |
| Landscape/overview | Ranking with escalating stakes | "Good → better → the one nobody expected" |

### Mini-Story Architecture

Structure content as 5-10 "mini-stories," each with:
1. **Setup**: The situation or problem
2. **Tension**: The "bad behavior" or current failure (hold up a mirror to the viewer's approach)
3. **Payoff**: The solution or insight

This keeps the retention graph flat by providing constant micro-resolutions instead of one delayed payoff.

### The "Last Dab" Technique

Write the final line of the video FIRST. This ensures the narrative arc closes as a loop. The ending determines what the hook must set up.

---

## 3. Hook Architecture (First 30 Seconds)

The hook puts them in the seat. Everything else keeps them there.

### The 3-Step Kallaway Formula

(Full reference: `.claude/rules/scriptwriting.md` §Scriptwriting Framework)

1. **Context Lean-In** (first 4 seconds): Mind-blowing fact or shared pain point. Viewer self-selects.
2. **Scroll-Stop Interjection**: "But/However/Yet" stun gun mid-sentence.
3. **Contrarian Snapback**: The "Uno Reverse" — snap to an unexpected conclusion.

### The First-Liner Catalog

Ten proven opener types. Rotate — never default to the same type for consecutive videos.

| # | Type | Template | Example |
|---|---|---|---|
| 1 | The Question | "Have you ever wondered why [flaw] exists?" | "Have you ever wondered why CI takes 40 minutes?" |
| 2 | The Shocking Statement | "[Core assumption] is a lie." | "Your database is a lie." |
| 3 | The Input Bias Story | "I spent [time] doing [effort] so you don't have to." | "I spent 5 months analyzing 40 repos so you don't have to." |
| 4 | The Metaphor | "Your [system] is [vivid image]." | "Your deployment pipeline is a hamster on a wheel." |
| 5 | The Proof | "[Known person/brand] uses [this exact approach]." | "The team behind Cursor ships with this exact workflow." |
| 6 | The Contrast | "[Impressive thing], but get this..." | "86,000 GitHub stars. But it's not Anthropic's best repo." |
| 7 | The Expert Secret | "The top 1% of [role] never [common practice]." | "Senior engineers never review code line by line." |
| 8 | The Claim | "[Specific number] — [what it means]." | "Sixty-three releases in eight weeks. One team." |
| 9 | The Challenge | "I gave [subject] [constraint] for [time]." | "I gave 16 AI agents one codebase for 48 hours." |
| 10 | The Direct Signal | "If you want [outcome], you need [specific thing]." | "If you want sub-second deploys, you need this pipeline." |

### The Re-Hook (30-60 seconds)

The first hook survives the initial click. The re-hook at 30-60s survives the "should I keep watching?" decision. It must:
- Acknowledge the value already delivered ("We just covered X")
- Raise stakes for what's coming ("But the real surprise is...")
- Be a different TYPE than the opening hook (if the hook was a number, the re-hook should be a question)

### Hook Failures

- **Too vague**: "In this video, we'll explore..." — no curiosity gap
- **Too hyperbolic**: "This changes EVERYTHING" — triggers skepticism
- **Too slow**: More than 4 seconds before the first value signal — viewer has already swiped
- **Mismatch**: Hook promises X, video delivers Y — worst possible outcome for retention

---

## 4. Writing Voice for TTS

The "uncanny valley" of AI scripts read by AI voices is a failure of rhythm, not technology.

### The Gary Provost Method

Forbid uniform sentence lengths. Write sentences that "burn with energy":

> This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. It's like a stuck record. The ear demands some variety.
>
> Now listen. I vary my sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length. And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo.

**Rule**: No more than 3 consecutive sentences of similar length. After 2-3 short punches, flow into a longer sentence.

### The Jagged Edge Test

View the script with one sentence per line. If the right margin forms a straight vertical line, the rhythm is monotonous. It should look jagged — short lines mixed with long ones.

### The Golf Buddy Tone

Write as if explaining to a smart friend over coffee. Not a lecture, not a manual.

- **Use contractions**: "don't" not "do not," "it's" not "it is," "we'll" not "we will"
- **Use fragments**: "One command. Done." is valid. "It executes with a single command and completes immediately." is not how people talk.
- **Use rhetorical questions**: "Sound familiar?" "Know what happened next?"
- **Interrupt yourself**: "The deploy worked — actually, wait. It worked on staging."
- **Express genuine reactions**: "I was terrified this would crash the production build." Not: "This is a risky operation."

### TTS-Specific Voice Rules

- **Contractions sound more natural in TTS** than formal speech. "We're" flows better than "we are."
- **Em dashes create natural pauses** — use them for mid-sentence beats. TTS handles them well.
- **Ellipsis (...) creates longer pauses** — use for dramatic reveals.
- **Avoid stacked one-word sentences** ("Automatically. Everything. Done.") — TTS reads these as disconnected fragments. Vary with 2-3 word fragments instead.
- **Avoid adverbs ending in -ly** ("incredibly," "extremely," "fundamentally") — they add no specificity and trigger the fluff detector.

### The "AI Slop" Detector

Phrases that immediately signal AI-generated content to a developer audience:
- "In today's fast-paced world..."
- "It's worth noting that..."
- "At the end of the day..."
- "Let's unpack this..."
- "This is a game changer..."
- Any sentence starting with "Imagine" followed by a generic scenario

If it sounds like something ChatGPT would write in a LinkedIn post, cut it.

---

## 5. Transitions & Connective Tissue

Transitions are the glue between sections. Bad transitions feel like speed bumps. Good ones create forward momentum.

### By Function

**Topic shifts (moving to new section):**
- "That handles [X]. Now the question is [Y]."
- "So [X] is solved. The next problem is worse."
- "[X] gives us the foundation. [Y] is where it actually matters."
- "Forget [X] for a second. Look at [Y]."

**Building on a point:**
- "And it gets more specific than that."
- "Take that one step further."
- "The same logic applies to [Y] — except here, [twist]."
- "That's the theory. Here's what it looks like in practice."

**Introducing evidence:**
- "The numbers back this up."
- "Here's the proof: [specific metric]."
- "[Source] measured this. The result: [number]."
- "Don't take my word for it. [Person/org] ran the benchmark."

**Pivoting to a counterpoint:**
- "That sounds great until you try [specific scenario]."
- "One problem: [specific limitation]."
- "Except when [edge case] happens."
- "There's a catch — and it's not obvious."

**Moving to practical application:**
- "So how do you actually use this?"
- "In practice, this looks like [specific example]."
- "Three commands. That's it."
- "Here's what the config looks like."

### By Energy Level

**Calm explanation**: "The reason this works is...", "What's happening behind the scenes is...", "The tradeoff here is..."

**High energy**: "This is where it clicks.", "Now watch what happens.", "One line of code. That's all it took."

**Conversational**: "Sound familiar?", "Yeah, I thought the same thing.", "Okay, so why should you care?"

### Transitions to AVOID

- "Now, let's move on to..." (announces the transition instead of making it)
- "Speaking of which..." (too casual, too vague)
- "With that said..." (filler)
- "Moving along..." (draws attention to structure)
- "Let's dive into..." (our second most overused transition)

---

## 6. Contrast & Reframing Techniques

Contrast is essential to technical explanations. The goal: make the viewer FEEL the difference, not just hear you describe it.

### Techniques That Work

**The Mirror**: Show the viewer their current behavior before revealing the better way. "You open VS Code. You write a prompt. You wait. You read the output. You paste it in. You run it. It fails. You go back." — Then: "One command handles all of that."

**The Concrete Before/After**: Don't say "it's faster." Show the specific scenario. "That query used to take 4.2 seconds. After the index: 12 milliseconds."

**The Unexpected Comparison**: "This isn't a code editor. It's a deployment pipeline that happens to edit code."

**The Specificity Flip**: Replace vague contrast with precise numbers. Not "much faster" — "47x faster." Not "way more repos" — "40 repos, and the biggest one isn't the one you'd guess."

### Techniques to Retire

- "This isn't X — it's Y" (overused format, 10+ instances in our videos)
- "It's not just X — it's Y" (same structure, same fatigue)
- "The old way vs. the new way" (too clean, too binary — real tech has tradeoffs)
- Any contrast that doesn't include a specific detail or number

---

## 7. Information Hierarchy & Emphasis

### The "So What?" Filter

Every technical detail must answer a viewer pain point. If a feature doesn't solve a problem, it's noise. Before writing any feature description, ask: "What does the developer gain from knowing this?"

### The Zoom In / Zoom Out Pattern

Prevent lecture fatigue by alternating every ~40 seconds:
- **Zoom In**: Technical detail, code, specific implementation
- **Zoom Out**: Big picture impact, "what this means for your workflow"

Never stay zoomed in for more than 60 seconds without a zoom-out moment.

### Managing Lists and Feature Rundowns

Lists are the #1 cause of monotonous scripts (especially in changelog videos). Defenses:

1. **Never read more than 3 items in a row** without a re-hook or commentary
2. **Vary the framing**: Item 1 as a benefit, Item 2 as a problem it solves, Item 3 as a surprising detail
3. **Group items into categories** with mini-hooks between groups: "Those were the stability fixes. Now the features."
4. **Assign unequal weight**: Not every feature deserves 30 seconds. The most impactful gets 60s, the rest get 10-15s each.

### Breathe Moments

Script deliberate 3-5 second pauses where the visuals carry the moment:
- After a complex code reveal — let the animation land
- After a surprising number — let it sink in
- Before a major reveal — build anticipation with silence

Mark these in the script with `[PAUSE]` (see `.claude/rules/scriptwriting.md` §Silence Cue Convention).

---

## 8. Emotional Architecture

Technical content needs emotional beats. Not hype — genuine intellectual emotion.

### Building Anticipation

The "Setup-Tension-Payoff" mini-story (§2) is the primary tool. The Tension phase is NOT a delay — it's the "hold up a mirror" moment where you show the viewer their current suboptimal approach before revealing the fix.

### Making the Viewer Feel Smart

The worst thing a technical video can do is make the viewer feel stupid. Techniques:
- **Explain context before jargon**: "The system runs a loop — in formal terms, an event-driven architecture"
- **Use the Distillation Technique**: Expert line, then a 5-year-old metaphor. "It uses vector similarity search — basically, it finds the closest match in a giant bucket of examples."
- **Acknowledge complexity**: "This part is genuinely tricky. Here's how it breaks down." — validates the viewer's potential confusion.

### Creating Stakes

Every video needs a "why should I care?" answer within 30 seconds. Stakes are not hype — they're specific consequences:
- **Bad**: "This will revolutionize your workflow."
- **Good**: "If you pick the wrong tool, you'll rebuild your workflow in 6 months. I've done it twice."

### Genuine Excitement vs. Hype

- **Hype**: "This is INSANE. This changes EVERYTHING."
- **Genuine**: "I ran this three times because I didn't believe the benchmark. Same result."

Developers trust restrained surprise. "Honestly, I didn't expect this to work" is more credible than "This is incredible."

### Input Bias (Effort as Trust Signal)

Developers don't trust self-proclaimed expertise. They trust visible effort. Mention the work:
- "I spent three weeks testing every configuration."
- "I analyzed all 40 repos — here's what I found."
- "I ran the benchmark on five different machines to make sure."

This creates an immediate "value trade" — the viewer feels they're getting compressed effort for free.

---

## 9. CTA & Closing Strategies

The traditional "like and subscribe" is a strategic failure — it signals the end of value.

### The "Next Problem" Strategy (Spiderweb Effect)

Identify the roadblock the viewer will face AFTER applying the current lesson. Point to the next video as the solution.

Framework: **Hook → Curiosity → Action**
1. "There's something I didn't mention about [current solution]."
2. "Now your [system] is fast — but it's wide open for [new problem]."
3. "I broke down how to fix that in [this video / next week's video]."

### CTA Categories

| Type | Template | Best For |
|---|---|---|
| **Curiosity** | "Next week: [specific related topic]. That's the piece that makes this actually work." | Series content, deep dives |
| **Challenge** | "Try [specific thing] yourself. Drop your results in the comments." | Tutorials, tools |
| **Debate** | "[Specific polarizing claim]? Tell me below." | Comparisons, opinion pieces |
| **Community** | "Join the [community name] — 2,000 developers already testing this." | Brand building |
| **Story continuation** | "I'm running this same setup for 30 days. I'll report back." | Experiments |

### The Debate CTA (MANDATORY)

The last spoken line must be a debate-sparking question (see `.claude/rules/scriptwriting.md` §Debate CTA). This is non-negotiable — it's our highest-engagement CTA pattern.

### CTAs to AVOID

- "If this helped, hit subscribe" (19x in our videos — generic, interchangeable)
- "Subscribe for more deep dives" (content-free)
- "Thanks for watching" (signals end of value)
- "Let me know what you think" (too vague to provoke actual comments)

---

## 10. Short-Form Adaptations (60-Second Shorts)

### Hook Timing

The viewer decides to stay or swipe within **1.5 seconds**. The first frame must contain text-on-screen with the value proposition. Audio hook must be a complete thought within 3 seconds.

### Structure Template

| Phase | Time | Content |
|---|---|---|
| Hook | 0-3s | One shocking claim or number + text on screen |
| Proof | 3-15s | One concrete example or demonstration |
| Explanation | 15-40s | The "how" — keep it to ONE mechanism |
| CTA | 40-60s | One specific action + debate question |

### Density Rules

- **One concept per Short** — don't try to cover three features
- **No preamble** — first word must be the hook
- **No "in this video"** — every second counts
- **Loop openers every 20-30 seconds** — attention span is shorter in vertical format
- **End with a loop** — Shorts that loop back to the opening get re-watched

### What Works in Shorts That Doesn't Work in Long-Form

- Pure shock value hooks (too thin for 10 minutes, perfect for 60 seconds)
- Single-stat reveals
- Direct challenge CTAs ("Try this right now")

---

## 11. Banned Patterns & Alternatives

These phrases are retired from all future scripts. For each, the audit count is listed alongside replacements.

### Critical (KILL — never use again)

| Banned Phrase | Count | Alternatives |
|---|---|---|
| "But here's the thing" | 61 | State the fact directly. / "One detail changes this." / "Look at what happens when..." / "[Specific thing] flips this." |
| "Most developers don't know / missed / are sleeping on" | 45 | State the surprising fact and let the viewer react. / "Anthropic has 40 repos. The biggest one isn't claude-code." / "[Stat] — and nobody's using it." / "The recruitment team won't tell you this, but..." |
| "No more [X]" | 36 | Describe the new behavior concretely. / "Alt-tabbing to Chrome? That's over." / "[X] now happens automatically." / "One command replaces that entire workflow." |
| "[X] changes everything" | 20 | "[X] refactors how we think about [Y]." / Drop the phrase entirely — the specific claim IS the impact. / "After [X], the old approach stops making sense." |
| "If this [helped/changed], subscribe" | 19 | Use a video-specific CTA (see §9). / "Next week: [specific topic]." / "[Debate question]? Tell me below." |
| "Nobody is talking about / the part nobody talks about / no one is talking about" | NEW | State the thing directly. If it's interesting, it doesn't need a wrapper. / "But the real story is..." / Just say the fact. |
| "Experts agree / studies show / research suggests" (without inline source) | NEW | Name the source in the same sentence: "GitGuardian's 2025 report shows 73%..." / Cut the claim if no source exists. / See `brand-voice-news-explainer.md` "Authority-Without-Evidence" section — single source of truth. |
| "Many / most developers find" / "It's widely known" / "As we all know" | NEW | If you can name "many developers", name them. If you can't, cut the appeal to consensus and state the fact directly. |

### High (Phase out — max 1 per 5 videos)

| Banned Phrase | Count | Alternatives |
|---|---|---|
| "Let me show you / walk you through" | 16 | Jump straight into the demonstration. / "Watch what happens." / "Three steps. First: [action]." |
| "Here's the thing" (standalone) | 16 | Drop it. State the thing. |
| "The future of [X]" | 14 | "Where [X] is heading in 2026." / "The next version of [X] looks nothing like this." / Be specific about WHAT is changing. |
| "Under the hood" | 12 | Name the actual mechanism. / "Here's the six-step loop." / "The pipeline runs three stages." / "Internally, it works like [specific thing]." |
| "Game changer / game-changing" | 11 | Use a specific metric. / "[X] cut build time by 73%." / "This is the feature that made me switch." |
| "Imagine [generic scenario]" | 11 | Use one vivid analogy per video max. / Open with concrete reality, not imagination. / "You've seen this: [specific relatable moment]." |

### Medium (Limit to 1 per video)

| Banned Phrase | Count | Alternatives |
|---|---|---|
| "It's not just X — it's Y" | 10 | "It does [X]. It also does [Y]. And [Y] is the one that matters." |
| "Nobody talks about" | 9 | "[Specific thing] gets zero attention." / "This repo has 2 stars. It should have 2,000." |
| "Where it gets interesting" | 9 | Jump to the interesting part. / "Now watch this." / "This next part surprised me." |
| "Think about it / that" | 6 | Let the fact speak. If it's genuinely surprising, the viewer will think about it without being told. |
| "Paradigm shift" | 5 | Describe the specific change. / "After this, the old workflow doesn't make sense." |

### Structural Anti-Patterns (Banned)

| Pattern | Why It Feels AI | Fix |
|---|---|---|
| Preview scene formula: `[Stat]. [Superlative]. [Three things]. This changes everything.` | Every video uses the same algorithm | Vary preview structure — try a question, a cold open, or a single bold claim |
| Staccato one-word drama: "Automatically. Everything. Done." | TTS reads these as disconnected fragments | Use 2-3 word fragments with variety: "One command. Full deploy. No rollbacks." |
| Every point gets equal time | Real expertise means knowing what matters most | Give the most important point 3x the time of lesser points |
| Setup-payoff that's too clean | Real engineering has messy tradeoffs | Include at least one honest limitation or "it depends" moment |
| Lack of tangents or asides | Human speakers digress; scripts that don't feel robotic | Add 1-2 brief personality moments: reactions, opinions, brief stories |

---

## 12. Developer Audience Psychology

### How Developers Detect Fluff

- **Vague claims** ("incredibly powerful," "revolutionary") — no specificity = no trust
- **Uniform enthusiasm** — everything being "amazing" means nothing is
- **No tradeoffs mentioned** — real engineers know everything has downsides
- **Marketing syntax** — "unlock," "leverage," "empower," "supercharge"
- **Round numbers** — "10x faster" is suspicious; "8.3x faster" is credible

### Trust Signals That Work

- **Specific numbers** with sources: "According to the 2025 Stack Overflow survey, 73% of..."
- **Input Bias** (visible effort): "I tested all 40 repos" > "I looked at some repos"
- **Honest limitations**: "This breaks on monorepos larger than 500 packages"
- **Peer-level syntax**: "You've probably hit this" > "Many developers experience this"
- **Behind-the-curtain reveals**: "What the changelog doesn't mention is..."

### What Makes Developers Share a Video

1. **It taught them something specific** they can use immediately
2. **It validated a belief** they couldn't articulate ("YES, I've been saying this!")
3. **It contained a specific, falsifiable claim** worth debating
4. **It was shorter than expected** for the value delivered

---

## 13. Visual-Script Integration Notes

### Writing for Animation

Since visuals are built AFTER the script, the script must create clear animation opportunities:

- **Narrate actions, not abstractions**: "The request hits the API gateway, bounces to the auth service, then fans out to three microservices" — this naturally maps to an animated flow diagram.
- **Use concrete numbers**: "Three stages. Five services. One bottleneck." — each number is a visual beat.
- **Signal reveals**: "Watch what happens when we add the cache layer" — cues a visual transformation.

### Breathe Moments for Visuals

When a complex diagram, code block, or metaphor animation is planned, the script should:
1. Set up the visual: "Here's what the architecture looks like."
2. Go silent for 3-5 seconds (mark with `[PAUSE]`)
3. Resume with commentary on what the viewer just saw

Never talk OVER a complex visual reveal — let the animation land first.

### Show Don't Tell

- **Bad**: "The system is very fast."
- **Good**: "4.2 seconds. That's how long the old query took." `[PAUSE]` "12 milliseconds. Same query, with the index." — This scripts two visual beats (before/after numbers) with a pause between them.

---

## 14. Quality Enforcement (QG-5)

Phase 2.5 enforces this playbook via Quality Gate 5:

### QG-5: AI-Phrasing Detection

Scan `full-script.md` for phrases from the §11 Banned Patterns list.

**Scoring:**
- `banned_count` = count of Critical or High banned phrases found
- **QG-5 PASS**: `banned_count == 0`
- **QG-5 FAIL**: `banned_count > 0`

**If FAIL:**
- List each banned phrase found with the scene it appears in
- Suggest 2-3 alternatives from §11 for each
- Re-run QG-5 after fixes

**Note**: Medium-severity phrases are flagged as advisories, not blockers. Limit to 1 per video.

---

## 15. Actionable Rules (Ordered by Impact)

### Tier 1: Non-Negotiable (violating these causes measurable retention loss)

1. **[HOOK] Validate the click within 3 seconds.** Visual text on screen must mirror the thumbnail's promise before the first sentence ends. *Instead of a generic intro, open directly on the subject the viewer clicked for.*

2. **[RETENTION] Change the visual state every 2 seconds in the first 30 seconds.** Static visuals cause faceless content to lose viewers 3x faster than talking-head. *Instead of one background for 10 seconds, plan 15+ distinct visual beats.*

3. **[VOICE] Vary sentence length — never 3+ consecutive sentences of similar length.** Uniform rhythm is the #1 signal of AI-generated text to a developer ear. *Instead of five 6-word sentences, try: short. Short. Then a longer sentence that builds momentum and earns the next pause.*

4. **[STRUCTURE] Connect every beat with "But" or "Therefore," never "And then."** Causal chains create logical necessity; sequential lists create exit points. *Instead of "And then we configured X," try "But the config broke Y. Therefore we had to Z."*

5. **[VOICE] Write in Golf Buddy tone — contractions, fragments, rhetorical questions.** TTS narration without conversational markers sounds like a manual being read aloud. *Instead of "We do not recommend this approach," try "Don't do this. Seriously."*

6. **[EMPHASIS] Use specific numbers, never vague claims.** "Fast" means nothing. "12 milliseconds" means everything to a developer. *Instead of "significantly faster," try "8.3x faster — from 4.2 seconds to 510 milliseconds."*

7. **[RETENTION] Deploy a Loop Opener every 60-90 seconds.** Curiosity naturally decays; loop openers reset the attention clock. *Instead of letting a section end cleanly, try: "That's not even the most surprising part."*

### Tier 2: High Impact (significant quality improvement)

8. **[HOOK] Apply the Context-Stop-Snapback formula for every hook.** The 3-step Kallaway formula ensures curiosity, disruption, and promise in the first 10 seconds. *Instead of "In this video, we'll cover X," try a mind-blowing fact, then "But," then the unexpected conclusion.*

9. **[STRUCTURE] Use Why-What-How hierarchy for all technical points.** Viewers won't invest in "how" until "why should I care?" is answered. *Instead of starting with code, start with the pain point the code solves.*

10. **[EMOTION] Show the "bad behavior" before the solution.** Tension is holding up a mirror to the viewer's current suboptimal approach. The payoff feels earned only if the problem felt real. *Instead of "Use this tool," try "If you keep doing X, your latency will spike."*

11. **[RETENTION] Alternate zoom-in (technical detail) and zoom-out (big picture) every 40 seconds.** Constant technical density causes lecture fatigue; constant big picture feels shallow. *Instead of 3 minutes of code, try: 40s code → 20s impact → 40s code → 20s "what this means for you."*

12. **[VOICE] Eliminate -ly adverbs and AI slop phrases.** "Incredibly," "fundamentally," "revolutionary," "In today's fast-paced world" — all trigger the developer BS filter. *Instead of "extremely powerful," try "robust" or give a specific metric.*

13. **[EMPHASIS] Lead with Input Bias in the first 60 seconds.** Developers trust effort over expertise. *Instead of "Here's a guide to X," try "I spent three weeks testing every option — here's what survived."*

14. **[CTA] Frame the outro as the "Next Problem" solution.** The Spiderweb Effect keeps viewers in your ecosystem. *Instead of "Subscribe for more," try "Now your API is fast — but it's wide open. I cover the fix next week."*

15. **[STRUCTURE] Build every segment as a mini-story (setup → tension → payoff).** Mini-stories keep the retention graph flat with constant micro-resolutions. *Instead of listing features, try: "The problem was X. They tried Y. But Z happened. The fix: W."*

### Tier 3: Quality Polish (separates good from great)

16. **[HOOK] Rotate opener types — never use the same hook type for consecutive videos.** If the last video opened with a number, this one opens with a question or story. *Check the First-Liner Catalog (§3) for 10 types.*

17. **[VOICE] Use the Jagged Edge Test on every script.** One sentence per line — if the right margin is straight, the rhythm is monotonous. *Visually scan the script before submitting for critique.*

18. **[RETENTION] Script explicit "Breathe Moments" for complex visuals.** Mark `[PAUSE]` for 3-5 seconds of silence when a diagram or code reveal needs to land. *Instead of talking over the animation, let it breathe.*

19. **[EMPHASIS] Give the most important point 3x the time of lesser points.** Equal time for all points signals that none of them matter. *In a 5-feature changelog, give the killer feature 60 seconds and the rest 15 seconds each.*

20. **[STRUCTURE] Write the final line first, then write the hook that sets it up.** The "Last Dab" technique ensures a closed narrative arc. *Instead of writing linearly, start with the payoff and reverse-engineer the setup.*

21. **[VOICE] Add 1-2 personality moments per video — brief reactions, opinions, or stories.** Pure information delivery without personality feels robotic. *Try: "I ran this three times because I didn't believe it." Or: "Okay, this next part is genuinely clever."*

22. **[EMOTION] Express genuine, restrained surprise instead of hype.** "I didn't expect this to work" is more credible than "This is INSANE." *Instead of superlatives, describe your honest reaction.*

23. **[RETENTION] Leverage the Sunk Cost Fallacy at minute 3.** Reference the viewer's time investment to prevent drop-off in the Valley of Death. *Try: "We've covered the basics. Now the part that actually matters."*

24. **[SHORTS] Hook within 1.5 seconds — first frame must have text on screen.** Vertical swipe-away culture is faster than long-form click-away. *Instead of any preamble, open with the claim as large animated text.*

25. **[CTA] End every video with a debate-sparking question under 15 words.** Polarizing claims drive comments from both sides. *Instead of "Thanks for watching," try "Claude or Cursor — what are you shipping with?"*

26. **[STRUCTURE] Never read more than 3 list items in a row without commentary.** Lists are the #1 cause of monotonous changelog scripts. *After 3 items, insert a re-hook or change framing.*

27. **[VOICE] Check for banned phrases before Phase 2.5 submission.** QG-5 will block scripts with Critical/High banned phrases. Catch them during writing, not during critique. *Scan §11 before submitting.*

28. **[EMPHASIS] Use "Behind-the-Curtain" framing for insider insights.** Developers value unspoken truths over public-facing PR. *Instead of "The company says X," try "What the engineers actually said was Y."*

29. **[RETENTION] Use pattern interrupts (music key change, visual shift) at natural section breaks.** Sensory monotony causes passive viewing; breaks force re-engagement. *Plan these in the script as visual cues for Phase 4.*

30. **[STRUCTURE] For videos >10 minutes, introduce a subplot or secondary thread.** A single storyline can't sustain 10+ minutes of focus. *Try a side-challenge, a running comparison, or a "let's find out" experiment.*

---

## Appendix: Cross-References

| Topic | Primary Source | This Playbook Section |
|---|---|---|
| Kallaway Formula | `.claude/rules/scriptwriting.md` §Scriptwriting Framework | §3 |
| 6 Story Locks | `.claude/references/story-locks.md` | §1 (Loop Openers), §5 (Contrast Words) |
| Hook Variants | `.claude/rules/scriptwriting.md` §Three Hook Variants | §3 |
| Quality Gates 1-4 | `.claude/rules/scriptwriting.md` §Quality Gates | §14 |
| WPM Calibration | `.claude/rules/scriptwriting.md` §WPM Calibration | Not duplicated — use rules file |
| Honest Comparisons | `.claude/rules/scriptwriting.md` §Honest Comparisons | §8 (stakes), §12 (trust) |
| Debate CTA | `.claude/rules/scriptwriting.md` §Debate CTA | §9 |
| TTS Conventions | `.claude/rules/scriptwriting.md` §TTS Script Conventions | §4 (voice layer only) |
| Retention Components | `src/shared/components/retention/` | Not duplicated — visual layer |
| Banned Phrase Audit | `.claude/research/scriptwriting-audit.md` | §11 (condensed + alternatives) |
