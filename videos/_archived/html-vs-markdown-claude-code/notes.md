# Notes — html-vs-markdown-claude-code

## Final-frame thumbnail — 10-variant pick

- **Skill:** `shorts-final-frame-thumbnail` (Author mode default = 10 variants per request)
- **Target:** 1280×720 separately-uploaded YouTube thumbnail asset
- **Picked at:** 2026-05-09
- **Status:** AWAITING USER PICK — see `thumbnail/contact-sheet.png`

### Why 10 variants

Per the skill's hard rule and user feedback (`feedback_thumbnail_10_variants_default.md`), thumbnail authoring always produces 10 distinct headline-angle variants — never one. A single variant is a guess; ten variants makes the choice obvious. Compare them in `thumbnail/contact-sheet.png` and tell me which number to ship.

### The 10 variants

| # | Angle | Headline | Theme | File |
|---|---|---|---|---|
| 01 | Death-of-default | "Markdown is dying." | Cream / serif italic | `variant-01.png` |
| 02 | Versus declaration | "HTML beats markdown." | Cream / strikethrough | `variant-02.png` |
| 03 | Imperative · dark slam | "Stop writing markdown." | Dark / yellow Inter | `variant-03.png` |
| 04 | Insider receipt | "Claude Code's team stopped using markdown." | Cream / serif italic | `variant-04.png` |
| 05 | Strikethrough swap · white minimal | "~~MARKDOWN~~ → HTML" | White / Inter | `variant-05.png` |
| 06 | Cinematic dark slam | "Markdown's over." | Dark / yellow Inter | `variant-06.png` |
| 07 | Question hook | "Why is your AI still printing markdown?" | Cream / serif italic | `variant-07.png` |
| 08 | Big-number social proof | "751K agreed. Markdown lost." | Cream / mono number | `variant-08.png` |
| 09 | Replacement matter-of-fact | "Markdown got replaced." | Cream / serif italic | `variant-09.png` |
| 10 | Data-led | "2-4× the tokens. 10× the read-rate." | Cream / mono numbers | `variant-10.png` |

Theme split: **7 cream** (canonical editorial) + **2 dark** (cinematic slam) + **1 white** (neo-min wildcard) — per the 7/2/1 within-style variation rule in [`headline-angles.md`](../../../.claude/skills/shorts-final-frame-thumbnail/references/headline-angles.md).

### How the user picks

1. Open `videos/html-vs-markdown-claude-code/thumbnail/contact-sheet.png` — all 10 numbered side-by-side
2. Pick the number that lands hardest in your gut
3. The corresponding `variant-NN.png` is the upload asset for YouTube Studio
4. (Optional) record the pick + ship-date in this file's "Picked variant" section below

### Picked variant

_Pending user choice. Once picked, log here:_
- **Picked:** v??
- **Ship date:** YYYY-MM-DD
- **Why this one over the others:** 1-line gut reason

### Re-audit cadence

Re-run `audit-checklist.md` Layer 3 (shelf-life) on **2026-11-09** — 6 months. If the picked angle's framing has saturated the dev/AI feed by then, restyle the next long-form's thumbnail (different angle from the 10-pack).

### Files in this folder

```
thumbnail/
├── _base.css              ← shared layout primitives + theme tokens
├── variant-01.html..variant-10.html   ← 10 source compositions
├── variant-01.png..variant-10.png     ← captured PNGs (1280×720) for upload
├── contact-sheet.html     ← 2-column grid view of all 10
├── contact-sheet.png      ← captured contact sheet (THIS is what to look at)
└── thumbnail.html / .png  ← (deprecated) first-pass single variant; superseded by the 10-variant pack
```
