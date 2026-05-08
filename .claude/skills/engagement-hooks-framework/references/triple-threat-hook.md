# Triple-Threat Hook — Visual + Text + Spoken alignment

The first 1.5 seconds decide whether the viewer stops scrolling. The first 4 seconds decide whether they stay. In a muted feed (~85% of plays), only **visual + text** are doing work. The spoken hook arrives third. If the three don't align, confusion breaks comprehension and the viewer bounces.

> "People hear a thing and they see a thing and it doesn't match in their brain. They get confused and then they churn. Confusion leads to churn." — Kallaway

## The three components

| Component | Role | Time-to-perceive | Failure mode |
|---|---|---|---|
| **Visual hook** | Stun gun. Different from what the feed has been showing. Movement, color, contrast, set. | <0.3s — pre-conscious | "Looks like every other video" → no scroll-stop |
| **Text hook** | Title text on screen (NOT captions). Confirms the visual claim in words. ~32-44px on 1080×1920 canvas, top third. | 0.5s — fast read | Tiny captions instead of title text → viewer can't read it before bouncing |
| **Spoken hook** | The narrator's first sentence. Active voice. Names the topic. Sets context. | 1-3s — sequential | Starts with "Hi guys" / "Today we're going to talk about" → wasted seconds |

## The alignment rule

The three must **agree**. Not echo word-for-word — but agree on the topic, the angle, and the promise. If you're saying "stop using YouTube tags", the text on screen says "STOP USING TAGS" or "TAGS ARE DEAD" or "TAGS DON'T WORK ANYMORE", and the visual shows a YouTube studio with tags being deleted or crossed out. All three point at one idea.

If they don't agree, the brain spends the first 2 seconds reconciling instead of leaning in.

## Failure modes (real cases from this repo's videos and the audited transcripts)

| Failure | What happened | Fix |
|---|---|---|
| Title text reads "Skills system" but visual is a generic gradient | Visual carries no information; the text is doing all the work alone | Visual must SHOW the skills system (a CLAUDE.md file? an icon set? a code snippet?). Even a stylized abstraction beats a gradient. |
| Spoken hook is "If you've ever struggled with..." but text on screen is a stat ("73%") | Mismatch — viewer reads the stat, hears a generic intro, bounces | Match: spoken says "Seventy-three percent of devs..." OR text says "If you've struggled" |
| Captions only, no title text | On muted feed the viewer reads tiny captions for 2s, not enough to anchor | Add title text in larger font (44px+) for the first 3s. Captions can stay small underneath. |
| Visual is the narrator (faceless channel exception): faceless videos showing only typography | No "different from feed" visual stun → doesn't stop scroll | Open with motion: a counter rolling, a card slamming in, a sweeping marker, a shape backdrop violently rearranging |

## The 5 alignment patterns

Pick the one that fits the topic. The pattern dictates how the three components carry the message.

### Pattern A — Anchor and Snap

- **Visual**: shows the common belief (tags being typed, a stat, a tool screenshot)
- **Text**: states the common belief directly (`STUFFING TAGS`, `73% OF DEVS DO THIS`)
- **Spoken**: reads the belief... then snaps with "But that's not how it works anymore."

Example (Transcript 1, TubeBuddy):
> "If you've been spending time stuffing tags into your YouTube videos, hoping it will push your videos to more people, I want to show you why that's not how it works anymore."

The visual shows the tags field being filled. The text confirms. The spoken sentence walks the viewer to +100 (validating their behavior) then drops them at -100 ("not how it works anymore"). Pattern A pairs naturally with **Violent Contrast** (see [`violent-contrast.md`](violent-contrast.md)).

### Pattern B — Direct Promise + Stakes

- **Visual**: shows the desired outcome (a graph going up, a viewer count climbing)
- **Text**: states the promise (`MORE VIEWS`, `2X RETENTION`)
- **Spoken**: opens with "If you want X, you have to Y."

Example (Transcript 2, TubeBuddy):
> "If you want more views on your YouTube videos, you have to start publishing at the right time."

This is the cleanest hook for utility content. No misdirection — just a direct conditional. Works because it's **second-person specific**. Does NOT use "Most creators don't..." (that's shame framing — banned in this repo's voice profile).

### Pattern C — Magnitude Frame + Insider Drop

- **Visual**: shows the subject of the magnitude claim (a logo slam, a $-amount roll)
- **Text**: states the magnitude (`$100B DEAL`, `BIGGEST IN HISTORY`)
- **Spoken**: "[Subject] just made one of the biggest [thing] in history. And the numbers are insane."

Example (existing repo brand-voice spec, news-explainer):
> "Anthropic just made one of the biggest AI hardware deals in history. And the numbers are absolutely insane."

The first sentence is medium-specificity by design — promise the payoff without dumping numbers yet. The text on screen carries the headline number; the spoken hook earns the lean-in. Pair with `Type A-news` from `brand-voice-news-explainer.md`.

### Pattern D — Authority + Stakes-Reveal

- **Visual**: shows the narrator's credentials manifesting (subscriber count, view count, a clip wall)
- **Text**: states a counterintuitive frame (`THE GAME RESET`, `UNCHARTED TERRITORY`)
- **Spoken**: opens with the frame, then drops a credibility line.

Example (Transcript 3, Kallaway):
> "We are officially entering uncharted territory for social media. And the pace of change is only getting faster... I have a million followers. I've done billions of views."

Use sparingly. Authority hooks read as flex unless the credibility is genuinely earned and the topic genuinely benefits from the speaker's experience. Faceless brand channels (this repo's default) usually skip Pattern D in favor of B or C.

### Pattern E — Personal Confession + System Reveal

- **Visual**: shows the narrator in vulnerable framing (looking tired, behind-the-scenes shot, raw screen recording)
- **Text**: contradicts expectation (`I HATE THIS`, `I ALMOST QUIT`)
- **Spoken**: opens warm, then pivots to the system that fixed it.

Example (Transcript 4, Kallaway):
> "Today we're talking about content systems... I'll be honest, the truth is, as weird as it sounds, I've never really liked making content."

Confession hooks work because they break the expected confidence. They MUST resolve to a system / framework / payoff within 15s — otherwise it reads as therapy, not content. Faceless channels can adapt this by confessing on behalf of the audience: "Most devs don't admit this, but..." (caveat: this repo's voice profile bans the "most devs" frame — adapt to "If you've ever felt..." instead).

## How to design the three together

Don't write the spoken hook first and retrofit visuals. Design all three at once:

1. **Pick the pattern (A-E)** based on topic + audience.
2. **Sketch the visual beat** — what motion / element / contrast lands at 0.5s? Note as `[VISUAL: ...]`.
3. **Write the text hook** — 3-7 words, 44px+ on shorts, top-third placement. Note as `[TEXT: ...]`.
4. **Write the spoken hook** so the first 8-12 words match the text + visual claim. Add the second sentence (the snap / promise / payoff lean-in) within the 4-second budget.
5. **Test at 0.5s, 1.5s, 4s** — at each cut-off, what does the viewer know? The first cut-off (0.5s) tells you if visual+text alone carry the topic.

## Annotation format inside the hook block

When authoring a hook in `videos/<slug>/scripts/full-script.md`, structure Scene 01 like this:

```markdown
## Scene 1: Hook

[VISUAL: counter rolling 0 → 64, gold accent, full-screen]
[TEXT: $64 BILLION (top third, 84px, mono)]

Last year, sixty-four billion dollars flowed through TikTok Shop. Two-year-old platform. And Instagram just launched their version.
```

Phase 2a strips the bracket annotations during TTS optimization — they're for the composition author and the engagement audit, not for the narrator. The composition build step (`new-anthropic-short.md` etc.) translates them to actual HTML markup.

## Self-check before declaring the hook done

- [ ] Visual stuns within 0.5s (different from generic feed pattern)
- [ ] Text on screen is readable in 0.8s on a phone (≥44px on shorts canvas)
- [ ] Visual + text + spoken all point at the same topic by sentence 1
- [ ] On a muted playthrough of the first 4s, the topic is clear from text+visual alone
- [ ] Spoken hook completes a full sentence inside 3.5s (no orphan opening clause that finishes at 5s)
- [ ] No greeting, no "in this video", no "let me show you" — straight into the topic
- [ ] Pattern selection (A-E) is documented in the Phase 1 plan's `hook_variants`

If any check fails, redesign. The hook is the fulcrum — every other improvement to the script gets capped by hook strength.
