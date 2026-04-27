# Recipe: url-cta

Closing CTA card: green-overline label + green-glow URL pill + rounded "Subscribe" pill with an orange arrow.

## What it produces

```
            READ THE FULL STORY
   ┌───────────────────────────────────┐
   │  example.com/path                 │   (green glow URL slam)
   └───────────────────────────────────┘
       ┌──────────────────┐
       │  Subscribe   →   │   (rounded pill, orange arrow)
       └──────────────────┘
```

Entrances: overline (0.0s) → URL slam at expo.out (0.5s, 0.7s long) → subscribe rises after (1.6s).

## Required tokens

```
--bg, --text, --orange, --green, --sans, --mono,
--pill-bg, --pill-border,
--pad-top, --pad-x, --pad-bottom
```

## Wire into a host composition

1. Copy `block.html` to `videos/<slug>/compositions/url-cta.html`.
2. In `videos/<slug>/index.html`:

```html
<div id="uc"
     data-composition-id="url-cta"
     data-composition-src="compositions/url-cta.html"
     data-start="<start>"
     data-duration="<duration>"
     data-track-index="<track>"
     data-width="1080"
     data-height="1920"></div>
```

## Slots to edit

| Selector         | Purpose                                             | Constraint                                    |
| ---------------- | --------------------------------------------------- | --------------------------------------------- |
| `#uc-overline`   | Mono section label                                  | 3-5 words                                     |
| `#uc-url`        | URL pill                                            | real URL only — never invent. ≤ 28 chars     |
| `#uc-subscribe`  | Subscribe pill (with `.arrow` span)                 | "Subscribe" recommended; or short variant     |

## Don'ts

- Don't fabricate URLs. Use a real, working URL or omit this block.
- Don't change the URL pill's accent — green is reserved for "go / read / launched", which is the correct semantic for a CTA.
- Don't widen `.url` past 920px — it overflows the safe zone otherwise.

## Lint expectations

`npx hyperframes lint videos/<slug>` — 0 errors expected.
