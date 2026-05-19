# Script Quote Attribution — Never Narrate "quote"

When a narration script attributes a verbatim quote from a source (article, X post, YouTube comment, blog), NEVER use the literal word **quote** (or *unquote*, *quoting*, *and I quote*) in the spoken text.

## Hard rule

> The narration script MUST NOT contain the spoken word `"quote"` (case-insensitive) as a quotation marker. The visual already presents the source's words as a quoted card with distinct typography, attribution chip, and like-count. Saying `"quote"` audibly is redundant, breaks the cinematic register, and reads as a research-paper voice-over.

A 30-second grep on `script.txt` before TTS saves a 3-5 minute re-TTS cycle.

## Bad — never write these into a TTS script

- *"Thariq said — quote — H T M L continues to be undefeated."*
- *"Quote — simplicity is the feature, not a bug."*
- *"He wrote, quote: markdown is the wrong format."*
- *"And I quote — wherever a human looks, H T M L."*

## Good — use natural attribution + a beat / colon-style pause

- *"Thariq said it again. H T M L continues to be undefeated."*
- *"The top reply — simplicity is the feature, not a bug."*
- *"He wrote it like this. Markdown is the wrong format."*
- *"The thesis that holds across both camps — wherever a human looks, H T M L."*

## Pattern

Use a natural attribution + an em-dash or sentence break before the quoted content. The micro-pause in narration is enough to signal "the next sentence is somebody else's words." The visual reinforces it.

Two reliable templates:

1. **Attribution + em-dash + verbatim words.** Example:
   *"One reply, three hundred and sixty-nine likes — simplicity is the feature, not a bug."*

2. **Attribution sentence + new sentence carrying the quote.** Example:
   *"Another engineer doubled down. H T M L continues to be undefeated."*

## Where this applies

- **Every video** in this repo — Shorts and long-form.
- **Every `voice_profile`** — `tutorial`, `news-explainer`, `comparison`, `article-response`.
- **Phase 2** (raw script) and **Phase 2a** (TTS-script). The Phase 2.5 critique loop MUST treat any spoken `"quote"` token as a publish-blocking defect.

## Why

1. **Cinematic register.** Narrating "quote" sounds like a court-reporter reading a transcript. Our videos are explainers, not transcripts.
2. **Redundant with visuals.** The quote already gets a visually distinct treatment on screen (italic serif, quotation chip, like-count badge, attribution avatar). Doubling that signal in audio is filler.
3. **Tighter pacing.** Each `quote` token costs ~0.4-0.6s of audio that delivers zero information beyond a quote-mark.
4. **TTS read** — `eleven_multilingual_v2` pronounces the word /kwoʊt/ literally, even when context implies a meta-marker. There's no way to "tell" the engine it's a structural element vs. spoken content.

## Self-check (mandatory before running `npx hyperframes tts` or `python scripts/elevenlabs-tts.py`)

```bash
grep -nEi '\bquot(e|ed|ing|ation)\b|\bunquote\b' videos/<slug>/script.txt videos/<slug>/scripts/*.txt
```

If ANY match returns, rewrite the line to use natural attribution instead. Re-run the grep; only run TTS once the grep returns zero results.

## Adding exceptions

There are NO exceptions. If a future case feels like it needs the literal `"quote"` token, restructure the sentence. This rule grows zero exceptions over time.

## Where the SOURCE of a quote does appear

This rule covers the spoken word `"quote"` only. The narration MAY still:
- Name the speaker (a famous engineer, e.g. *"Thariq, from the Claude Code team"*) — see also `feedback_no_username_unless_famous` style guidance.
- Anonymously attribute (e.g. *"One comment, three hundred and sixty-nine likes…"*).
- Reference the venue (*"on X"* / *"on YouTube"*).

Just never say *"quote"* as the marker.
