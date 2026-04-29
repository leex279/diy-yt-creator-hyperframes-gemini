# Recipe: dynamous-module-interstitial

Optional 3.0s mid-video card that names the matching Dynamous AI Mastery module. Slides in from the right at a natural narration pause, holds, slides out. **Opt-in per video** — only fires when the Short's topic directly maps to one of the 12 curriculum modules.

> **OPT-IN.** This block is opt-in even within an opted-in Short. If no module matches the topic cleanly, skip this block entirely.

## What it produces

```
   ┌──── 1080 × 1920 frame ──────────────────────┐
   │                                             │
   │   [ phase content above ]                   │
   │                                             │
   │   ┌─────────────────────────────────────┐  │   ← slides in from right
   │   │  ●  MODULE 10                       │  │     at t=0–0.6s
   │   │     MCP Servers + Skills            │  │
   │   │  Part of Dynamous AI Mastery        │  │
   │   └─────────────────────────────────────┘  │
   │                                             │
   │   [ phase content below ]                   │
   └─────────────────────────────────────────────┘
                       ↓
                slides out at t=2.4–3.0s
```

Animation:

- **Slide-in + fade-in** (0–0.6s) — `x: +540 → 0`, `opacity: 0 → 1`, `power3.out`.
- **Hold** (0.6–2.4s) — card sits centered horizontally.
- **Slide-out + fade-out** (2.4–3.0s) — `x: 0 → +540`, `opacity: 1 → 0`, `power3.in`.

## When to use

Use this block ONLY if **all** of these are true:

1. The Short's author has opted in to the Dynamous promotion at spawn time.
2. The Short's topic directly matches a curriculum module — verify with the helper:

   ```bash
   node scripts/find-dynamous-module.js "<tag-1>" "<tag-2>" "<tag-3>"
   ```

   If the helper prints `NO_MATCH`, skip this block.

3. The narration has a clean ≥1.0s breath where the card can land without overlapping a hero word. Consult `transcript.json` if you have one.

If any of those is false, do not wire this block. The endcard alone covers the brand recall — the interstitial is a *bonus* on topic-matched Shorts.

## Wire into a host composition

1. **Copy the block** into the video's `compositions/` folder:

   ```bash
   cp shared/lib/blocks/dynamous-module-interstitial/block.html \
      videos/<slug>/compositions/dynamous-module-interstitial.html
   ```

2. **No asset copy needed** — this block uses no logo SVG/PNG.

3. **Pick the start time** at a clean narration pause (the breath should be ≥ 1.0s — the card needs 0.6s to slide in before it's readable).

4. **Add the mount `<div>`** to `videos/<slug>/index.html`:

   ```html
   <div id="dynamous-mod-int-mount"
        data-composition-id="dynamous-module-interstitial"
        data-composition-src="compositions/dynamous-module-interstitial.html"
        data-start="<pause-start>"
        data-duration="3"
        data-track-index="3"
        data-width="1080"
        data-height="1920"></div>
   ```

5. **Edit the per-video copy** (`videos/<slug>/compositions/dynamous-module-interstitial.html`) to fill in the matching module:
   - `#dmi-module-num` — module ID (e.g. `5`).
   - `#dmi-module-title` — module title (e.g. `Systems for Planning`).
   - The accent dot color — set inline on `#dmi-dot`, e.g. `style="background: #ef4444"` (use the `color` field from `dynamous-modules.json` for that module).

6. **Lint**:

   ```bash
   npx hyperframes lint videos/<slug>
   ```

## Slots to edit

| Selector            | Purpose                                  | Constraint                                                       |
| ------------------- | ---------------------------------------- | ---------------------------------------------------------------- |
| `#dmi-module-num`   | Module ID (numeric)                      | 1–12 only — must match a real module from `dynamous-modules.json` |
| `#dmi-module-title` | Module title                             | Verbatim from `dynamous-modules.json`. ≤ 32 chars (1080px width). |
| `#dmi-dot`          | Accent dot color                         | Inline `style="background: <module.color>"`. Optional — falls back to `#ec4899` (pink). |

## Don'ts

- **Don't fire before `t=3.0s`.** Strategy doc rule — never compete with the opening hook.
- **Don't place over a hero word.** The card sits at `top: 420px` — that's the natural eye line for hero text in dark-stage Shorts. Find a phase gap or breath, not a hero moment.
- **Don't extend `data-duration` past 3.0s.** Longer holds steal attention from the narration.
- **Don't fabricate a module match.** If `find-dynamous-module.js` prints `NO_MATCH`, skip this block. A forced "Module 12 — Parallel Agentic Coding" on a news Short feels off-brand.
- **Don't add SFX.** Per `audio-design.md` — Shorts are silent on the SFX track.
- **Don't add a discount badge here.** The interstitial is informational ("you're learning a real curriculum module"), not transactional. The endcard carries the offer.

## Lint expectations

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors. Inspect should show the card at `top: 420px` with no overflow.
