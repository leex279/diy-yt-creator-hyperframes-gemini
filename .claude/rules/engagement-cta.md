# Engagement CTA — every video MUST end with a debate-sparking question

Every video shipped from this repo (Short OR long-form, every `voice_profile`, every template) MUST close on a **debate-sparking CTA**: a polarizing, easy-to-answer question that splits the audience and earns comments. The CTA appears in **three** places at once and they MUST agree:

1. **Spoken** — the final 3–5 seconds of narration in `videos/<slug>/script.txt` (Short) or the final scene of `videos/<slug>/scripts/full-script.md` (long-form).
2. **Visual** — a dedicated on-screen element in the final phase of `videos/<slug>/index.html` that displays the question while it is spoken and continues to hold during the loop/thumbnail freeze.
3. **YouTube description** — the same question is restated at the end of `videos/<slug>/youtube-description.md` (per [`youtube-metadata.md`](./youtube-metadata.md) — Engagement CTA section).

All three must reference the **same claim** from the video. This is a content rule, not a template flourish.

> **Why three places?** Spoken catches the listener who watched. Visual catches the looper who paused on the final frame (per [`shorts-thumbnail-frames.md`](./shorts-thumbnail-frames.md)). Description catches the reader and surfaces the question to YouTube's engagement signal. A CTA that exists in only one place leaks ~⅔ of its potential comments.

---

## What makes a CTA debate-sparking (HARD criteria)

A debate-sparking CTA satisfies **all four** of these properties. If any are missing, rewrite.

1. **Binary or short-list answer** — the viewer can answer in 1–5 words without thinking. `"Team A or team B?"` `"Which one are you switching to?"` `"Yes or no?"` `"Hype or hot air?"` Multi-sentence answers kill comment volume because typing on mobile is painful.
2. **Polarizing / contrarian stance baked in** — the question takes a side, dares the viewer to disagree, OR forces them to pick a side. Pure neutral questions (`"What do you think?"`) get pure neutral engagement. The question should make at least 30% of viewers want to push back.
3. **References a specific claim from the video** — the question must build on something concrete the viewer just watched (a stat, a product comparison, a hot take, a deprecation, a winner-takes-all framing). Generic questions disconnected from the content read as filler.
4. **Low cost to answer** — answering should NOT require domain expertise, doing homework, or remembering details. A senior dev and a first-week beginner should both be able to fire off an opinion in 5 seconds. "How would you architect this differently?" fails this test — most viewers won't.

---

## Question patterns that consistently earn comments

Use these as templates — fill in the topic-specific blanks, never copy verbatim.

| Pattern | Example | Why it works |
|---|---|---|
| **Tool-vs-tool** | `"Claude Code or Cursor — which one are you shipping with in 2026?"` | Forces team-picking. Tribal. Easy. |
| **Dead-or-alive** | `"Is the browser-tab era actually over, or is this just hype?"` | Splits skeptics vs. believers. Binary. |
| **Pick-the-winner** | `"Of the 15 new connectors — which one ships first to your daily workflow?"` | Specific to the video. Low-stakes opinion. |
| **Hot-take confirm** | `"Claude reading your emails inside the chat — useful or terrifying?"` | Forces emotional stance. Polarizing. |
| **Adoption deadline** | `"Three months from now, will you still be opening separate tabs for these tools?"` | Forces a prediction the viewer wants to defend. |
| **Stop-doing-X** | `"What's the first browser tab you'd close if Claude could do that job?"` | Constructive but specific. Easy to list one. |
| **Hill to die on** | `"Which Claude feature is the one you'd quit your job to keep?"` | Identity-tied. Strong-opinion bait. |

The strongest CTAs combine TWO patterns — e.g., `"Browser tabs are dying — or is this just another integration fad? Which side are you on?"` (Dead-or-alive + Pick-a-side).

---

## Anti-patterns (zero tolerance — rewrite if any appear)

These are BANNED as the closing line of any video script:

- `"What do you think?"` — neutral, lazy, gets neutral engagement
- `"Let me know in the comments!"` (without a question) — no anchor for the comment
- `"Like and subscribe if you enjoyed this"` — generic plug, not a CTA
- `"Drop your thoughts below"` — same neutrality problem
- `"How would you build this differently?"` / `"How would you architect this?"` — too high-effort to answer, kills volume
- `"Did this help you?"` — yes/no with no debate value
- `"Anything I missed?"` — invites pedantry but no real engagement
- `"Link below"` (as the standalone closer) — directive, not a question
- Any CTA that requires watching the video twice to answer

If the current script's closer matches any of these patterns, it FAILS Phase 2.5 QG-2b regardless of the rest of the score.

---

## The spoken-line constraint (Shorts)

Shorts have ~30–60s total. The CTA narration MUST fit in **3–5 seconds of speech** at the script's WPM (typically 150–165 WPM = 8–14 words). Don't write a 25-word CTA — there's no room.

Template (Shorts):
- 1 sentence stating the implication the video built (~1.5s)
- 1 short question with the four debate-sparking properties (~2s)
- Optional: 1 comments-ask half-line (~1s) — `"Drop your pick below."`

Example, ~4s @ 160 WPM:
> `"The browser-tab era is ending. Or is this just another integration fad? Drop your pick below."`

That's 16 words, ~6 seconds at 160 WPM — slightly over the budget but acceptable for a Short whose body ends a few seconds early. Trim to 12–14 words for tighter Shorts.

---

## The visual element (every template)

The final phase of every template's `index.html` MUST contain a dedicated element (`id="cta-question"` or analogous) that holds the on-screen text of the CTA question. Requirements:

- **Typography** — meets [`shorts-typography.md`](./shorts-typography.md) minimums: Short = 48px+, long-form = 36px+.
- **Distinct from the URL/subscribe/brand chrome** — the question must NOT compete with the directive elements. Give it its own row and color emphasis.
- **Enters AFTER the URL/brand chrome have settled** — typically 1.5s into the CTA phase.
- **Persists through the thumbnail-grade final frame** — per [`shorts-thumbnail-frames.md`](./shorts-thumbnail-frames.md), the question should be visible at composition end.
- **Placeholder when template is bare** — `id="cta-question"` ships with text like `"<REPLACE: debate-sparking question>"` so the slot is impossible to miss when spawning a new video. Operators replace it per video.

---

## Where this rule applies

- Every Short (`templates/shorts/<style>/`, every `videos/<slug>/` with a vertical canvas).
- Every long-form (`templates/long-form/<style>/`, every `videos/<slug>/` with a horizontal canvas).
- Every `voice_profile` (`tutorial`, `news-explainer`, `comparison`). The existing Phase 2.5 Pass 6 skip-for-tutorial does NOT apply to this rule — even tutorials must end on a debate question. Tutorials are allowed terse phrasing but cannot skip the CTA itself.

## Where this rule does NOT apply

- Test renders / smoke renders (`--quality draft` while iterating). The bare template still ships with the CTA slot, but operators may render without a real question while in mid-build.
- Pure technical demos where the closer is genuinely a hard CTA (`"Try it: $ claude update"`) — but in those cases the YouTube description STILL must close on a debate question per `youtube-metadata.md`. Only the spoken/visual constraint is relaxed, and only when the operator explicitly justifies it in the video's `notes.md`.

---

## Self-check before declaring a video done

For every video:

1. **Spoken**: read the final sentence of `script.txt` / `full-script.md` aloud. Does it ask a question? Does it match all four HARD criteria above?
2. **Visual**: pause the rendered MP4 at the final frame. Is the question visible on screen? Is it the same wording as the spoken line?
3. **Description**: open `youtube-description.md`. Does the final paragraph contain the same question? Does it match what is spoken and shown?

If any of the three is missing or weak, rewrite before declaring done. Phase 2.5 QG-2b and QG-5c both backstop this gate — but the cheapest place to fix a weak CTA is BEFORE TTS, not after.

---

## When to update this rule

When a CTA pattern produces a measurable comment-count outlier (3× the video's baseline), add the pattern to the table above. When a pattern consistently underperforms, move it to anti-patterns. This list grows with shipped data.
