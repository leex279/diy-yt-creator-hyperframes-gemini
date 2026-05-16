# Headline angle rotation — 10 angles for variant generation

Author mode produces 10 thumbnail variants per request. The 10 differ primarily by **headline angle** — the psychological frame the topic is delivered through. Same topic, ten different ways of weaponizing it for the scroll-stop.

## Hard rules for thumbnail headlines

1. **2–4 words for the dominant slam.** Never the source article's verbatim title. Editorial titles ("The unreasonable effectiveness of HTML") read as quoted reverence; thumbnails need *takes*.
2. **Take a side.** A thumbnail that hedges loses the click. "X is dying" beats "X has problems." "Y beats X" beats "Y has advantages over X."
3. **Concrete > abstract.** "Markdown" beats "default formats." "751K agreed" beats "many people agreed." Specifics earn the click; abstractions don't.
4. **Source attribution is optional and SUBORDINATE.** If you cite the source ("[Trusted team] stopped using X"), it goes on a smaller line below the punch — never IS the punch.
5. **Never quote the source verbatim as the dominant text.** That's editorial restraint, which is the opposite of thumbnail energy.

## The 10 angles

For any topic where the video argues "X is being replaced by Y" or "the conventional wisdom is wrong," generate one variant for each of these 10 angles:

| # | Angle | Pattern | Example (X = markdown, Y = HTML) |
|---|---|---|---|
| 01 | **Death-of-default** | "X is dying." | "Markdown is dying." |
| 02 | **Versus declaration** | "Y beats X." | "HTML beats markdown." |
| 03 | **Imperative command** | "Stop [doing X]." | "Stop writing markdown." |
| 04 | **Insider receipt** | "[Trusted team] stopped using X." | "Claude Code's team stopped using markdown." |
| 05 | **Strikethrough swap** | "~~X~~ → Y" (visual punch) | Big struck-through "MARKDOWN" with arrow to "HTML" |
| 06 | **Cinematic dark slam** | "X's over." (yellow on charcoal) | "Markdown's over." |
| 07 | **Question hook** | "Why is your [thing] still using X?" | "Why is your AI still writing markdown?" |
| 08 | **Big-number social proof** | "[N] agreed. X lost." | "751K agreed. Markdown lost." |
| 09 | **Replacement matter-of-fact** | "X got replaced." | "Markdown got replaced." |
| 10 | **Data-led** | "[stat-1]. [stat-2]." | "2-4× the tokens. 10× the read-rate." |

## When the topic isn't "replacement"

For topics that aren't about something replacing something else — e.g., a tool announcement, a tutorial, a personal story — adapt the angle table:

| Topic shape | 10-angle adaptation |
|---|---|
| **Tool announce** ("X 2.0 ships") | death (the old way is over) / versus (Y beats X) / imperative (stop doing the old) / insider (the team uses it) / numbered (5 features) / dark (cinematic version slam) / question (what's new?) / big-stat (2M downloads in 3 days) / receipt (here's what changed) / data (specs vs. last gen) |
| **Tutorial** ("How I built X") | imperative (stop building like this) / receipt (X in 47 lines) / time (built in 24 hours) / contrarian (the wrong way) / insider (top engineers do this) / strikethrough (~~old way~~ → new way) / question (why is this so hard?) / big-stat (3,200 stars in week 1) / data (10× faster) / cinematic dark (the secret) |
| **Personal story** ("I burned out") | confession (I broke) / contrarian (the lie) / time (5 years wasted) / question (why don't we talk about X?) / receipt (the proof) / cinematic dark (the truth) / imperative (stop pretending) / insider (every founder I know) / data (47% never recover) / replacement (what works instead) |

The 10-angle structure stays — only the specific framings rotate based on what the topic is.

## Within-style variation across 10 variants

The 10 variants share the picked style (e.g., #6 cinematic text) but vary minor accents to give the user real choice:

- **7 variants in the picked style's canonical theme** (e.g., cream + serif italic terracotta for cinematic-text editorial)
- **2 variants in the style's adjacent theme** (e.g., dark + yellow Inter for cinematic-text streaming)
- **1 variant in a sibling style** (e.g., neo-minimalism strikethrough on white) — gives the user a "wildcard" to compare against

This 7/2/1 split keeps the pack feeling coherent (90% in the picked style) while giving enough diversity that the user can see the angle and the style separately.

## Output format

Each variant is a self-contained HTML file at the spec'd canvas size (1280×720 long-form thumbnails, 1080×1920 shorts final-frames). All 10 variants link to a shared `_base.css` with the layout primitives (chrome, brand mark, cover-anchor zone), and each variant inlines its own headline + theme overrides.

The contact sheet (`contact-sheet.html` → `contact-sheet.png`) shows all 10 in a numbered grid with their angle labels — that's what you show the user to pick from.

## Self-check before generating variants

Before writing the 10 HTML files:

1. Have you written down all 10 distinct headlines (not 10 reskins of the same headline)?
2. Are all 10 headlines 2-4 words on their dominant line?
3. Does any headline match the source article's verbatim title? If yes, replace it.
4. Are 7 in the canonical theme, 2 in adjacent, 1 wildcard?
5. Does each variant satisfy the 5-element rule (topic / anchor / brand / outcome)?

If any answer is "no", refine before authoring.
