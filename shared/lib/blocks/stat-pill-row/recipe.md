# Recipe: stat-pill-row

Two-pill stat row in color-rotated accent pills. Default canvas: 1080×1920 (Shorts). For long-form, override `data-width="1920" data-height="1080"` on the wiring `<div>` and adjust `.stat-num` font-size in the host's overrides.

## What it produces

```
   SECTION LABEL
   Headline goes here
   ┌──────┐  ┌──────┐
   │  3   │  │  6   │
   │ FIRST│  │SECOND│
   └──────┘  └──────┘
```

Entrances stagger overline → headline → pill 1 → pill 2 (back.out(1.6) on the pills). 2.0s total animation length.

## Required tokens

The block reads the following CSS vars; either link `shared/lib/tokens/anthropic-dark.css` (or your own equivalent) before the block, or override them per-host:

```
--bg, --text, --orange, --purple, --blue, --green, --sans, --mono,
--pad-top, --pad-x, --pad-bottom
```

Hard fallbacks are baked in for each `var(...)` so the block won't render plain black if a token is missing — but contrast may degrade.

## Wire into a host composition

1. Copy `block.html` to `videos/<slug>/compositions/stat-pill-row.html`.
2. In `videos/<slug>/index.html`, add (replace `<start>`, `<duration>`, `<track>`):

```html
<div id="spr"
     data-composition-id="stat-pill-row"
     data-composition-src="compositions/stat-pill-row.html"
     data-start="<start>"
     data-duration="<duration>"
     data-track-index="<track>"
     data-width="1080"
     data-height="1920"></div>
```

3. The framework auto-nests the block's timeline under the host root timeline. No manual integration needed in the host's `<script>`.

## Slots to edit

In the copied `compositions/stat-pill-row.html`:

| Selector          | Purpose                          | Constraint                        |
| ----------------- | -------------------------------- | --------------------------------- |
| `#spr-overline`   | Mono section label, ALL CAPS    | 2-3 words, ~16 chars max          |
| `#spr-headline`   | Sans headline                    | 5-9 words, wraps at 940px         |
| `#spr-pill-1`     | First pill wrapper (accent class) | swap `.orange` → `.purple/.blue/.green` |
| `#spr-pill-1` `.stat-num` | First number              | digits only, ≤ 4 chars             |
| `#spr-pill-1` `.stat-label` | First label             | mono, UPPERCASE recommended, ≤ 18 chars |
| `#spr-pill-2`     | Second pill — same as pill 1     | accent should differ from pill 1  |

## Customizing accents

Built-in accent classes: `.orange`, `.purple`, `.blue`, `.green`. For another color, add a new rule set following the existing pattern (5 declarations: `background` linear-gradient, `border`, `box-shadow`, `.stat-num color`, `.stat-num text-shadow`).

## Don'ts

- Don't widen `.stat-pill` past 480px without re-checking the gap — at 1080px canvas with 60px padding and 18px gap, two 460px pills fit exactly (460×2 + 18 = 938 < 960 available).
- Don't drop `font-variant-numeric: tabular-nums` from `.stat-num` — without it, digits jitter horizontally during scale-pop.
- Don't add `overflow: hidden` to `.stat-pill` — would clip the `text-shadow` glow.

## Lint expectations

`npx hyperframes lint videos/<slug>` should report 0 errors. Common warnings to ignore: nothing specific to this block. Common errors if wired wrong:

- `missing_track_index` — add `data-track-index` to the wiring `<div>`.
- `composition_id_mismatch` — `data-composition-id` on the wiring `<div>` MUST be `stat-pill-row` (matches the block file's internal ID).
