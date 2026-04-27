# Recipe: timeline-cards

Three dated cards stacked vertically, each with an accent date chip on the left, sans title + mono subtitle in the middle, and an accent index badge on the right.

## What it produces

```
   SECTION LABEL
   ┌──────────────────────────────────────────┐
   │ JAN 1 │ First event title         │ 1 │  (orange)
   │       │ Subtitle line one         │   │
   ├──────────────────────────────────────────┤
   │ JAN 8 │ Second event title        │ 2 │  (purple)
   │       │ Subtitle line two         │   │
   ├──────────────────────────────────────────┤
   │ JAN 15│ Third event title         │ 3 │  (blue)
   │       │ Subtitle line three       │   │
   └──────────────────────────────────────────┘
```

Entrances stagger overline → card 1 → card 2 → card 3 (450ms apart, `back.out(1.5)`).

## Required tokens

```
--bg, --text, --orange, --purple, --blue, --green, --sans, --mono,
--pad-top, --pad-x, --pad-bottom
```

Hard fallbacks are baked in for each `var(...)`.

## Wire into a host composition

1. Copy `block.html` to `videos/<slug>/compositions/timeline-cards.html`.
2. In `videos/<slug>/index.html`, add:

```html
<div id="tlc"
     data-composition-id="timeline-cards"
     data-composition-src="compositions/timeline-cards.html"
     data-start="<start>"
     data-duration="<duration>"
     data-track-index="<track>"
     data-width="1080"
     data-height="1920"></div>
```

## Slots to edit

| Selector                       | Purpose                                  | Constraint                                    |
| ------------------------------ | ---------------------------------------- | --------------------------------------------- |
| `#tlc-overline`                | Mono section label, ALL CAPS            | 2-3 words                                     |
| `#tlc-card-1` (accent class)   | First card wrapper                       | use `.orange / .purple / .blue / .green`      |
| `#tlc-card-1 .tl-date`         | Solid accent date chip                   | mono, ALL CAPS, ≤ 7 chars (e.g. "JAN 15")    |
| `#tlc-card-1 .tl-title`        | Sans title                               | 3-5 words, single line at 40px                |
| `#tlc-card-1 .tl-sub`          | Mono subtitle                            | 3-6 words                                     |
| `#tlc-card-1 .tl-index`        | Index badge (defaults to "1")            | single digit recommended; 2 chars max          |
| `#tlc-card-2`, `#tlc-card-3`   | Same as card 1                           | rotate accents — see below                    |

## Accent rotation rule

Per `templates/shorts/anthropic/DESIGN.md`: **no two adjacent cards may share the same accent**. Default rotation: `orange → purple → blue`. Substitute `green` for any one of them if your content mood calls for "fixed / launched / positive". Avoid using two of any color in a row.

## Don'ts

- Don't widen `.timeline-list` past 940px — the cards lose their breathing margin against the 1080px canvas safe-zone.
- Don't drop the index badge — it doubles as a visual rhythm anchor and lets the cards survive even when titles vary in length.
- Don't change `.tl-date` `color: var(--bg)` — near-black on solid accent is the only combination that hits AAA contrast for date chip text.

## Lint expectations

`npx hyperframes lint videos/<slug>` — 0 errors expected.
