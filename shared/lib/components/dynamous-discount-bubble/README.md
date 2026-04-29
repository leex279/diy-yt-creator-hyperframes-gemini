# Component: dynamous-discount-bubble

Opt-in 3–4s pill that pops up while the screen recording shows the Dynamous platform. Logo + `Dynamous.ai` + red `10% OFF` badge + `in the link ↓` pointer. **No coupon code field** — the discount applies automatically via the description link.

> **OPT-IN PER VIDEO AND PER SCENE.** This component is opt-in even within an opted-in Short. If the platform isn't visibly on screen, skip this artifact.

## What it produces

```
   ┌─[ time-bounded — 3.0–4.0s scene ]───────────────────────────┐
   │   ┌────────────────────────────────────────────────────┐   │
   │   │ ◆  Dynamous.ai   [10% OFF]   in the link ↓        │   │
   │   └────────────────────────────────────────────────────┘   │
   └─────────────────────────────────────────────────────────────┘
```

Animation:

- **Slide-up + fade-in** (`sceneStart`–`sceneStart + 0.5s`) — `y: +16 → 0`, `opacity: 0 → 1`, `power2.out`.
- **Hold** for the bulk of the scene.
- **Fade-out** in the final 0.4s — `opacity: 1 → 0`, `power2.in`.

Unlike the persistent badge, this component IS time-bounded — it carries `class="clip"` and `data-start` / `data-duration` attributes.

## When to use

Wire this component ONLY if **all** of these are true:

1. The Short's author has opted in to the Dynamous promotion at spawn time.
2. **The Dynamous platform is visibly on screen during the chosen scene** — typically a screen recording of `dynamous.ai` or the Circle community feed. If the platform isn't shown, skip this artifact.
3. The chosen `data-start` is `≥ 3.0s` — never fire during the opening hook.
4. The chosen scene has no hero word in the lower-third — the bubble lands at `top: 1180px` by default.

If any of those is false, do not use this component.

## What it does NOT carry

**No coupon code field.** The discount applies automatically when viewers click through the description link (user-confirmed 2026-04-28). The bubble exists to give sound-off viewers a visible reminder that the offer is real and waiting in the description.

If you find yourself wanting to add a code field, stop and re-read the wiring snippet's pinned-comment template — the link does the work. A code on screen creates friction that doesn't exist in the actual purchase flow.

## Required tokens

None. Inlines its own colors and font.

## Wire into a host composition

1. **Copy the logo asset:**

   ```bash
   cp shared/logos/dynamous-logo.png videos/<slug>/assets/dynamous-logo.png
   ```

2. **Pick a `data-start` and `data-duration`** from your scene timing. Typical values: `data-start="6.0" data-duration="3.5"`. Constraints: `data-start ≥ 3.0`, `data-duration ≤ 4.0`.

3. **Paste the three sections** from `component.html` into `videos/<slug>/index.html`:
   - The HTML — replace `__SCENE_START__` and `__DURATION__` with your values.
   - The `<style>` block contents into your `<style>`.
   - The `<script>` block contents into your existing GSAP `<script>` (or as a separate `<script>` after GSAP loads).

4. **Call the entrance from your root timeline:**

   ```js
   addDynamousDiscountBubbleEntrance(tl, 6.0, 3.5);  // sceneStart, duration
   ```

5. **Lint:**

   ```bash
   npx hyperframes lint videos/<slug>
   ```

## Slots to edit

| Element                | Purpose                       | Constraint                                                |
| ---------------------- | ----------------------------- | --------------------------------------------------------- |
| `data-start`           | Scene start time (seconds)    | ≥ 3.0 — never during the hook                             |
| `data-duration`        | Scene length (seconds)        | 3.0–4.0; 3.5 is the recommended default                   |
| `data-track-index`     | Track ordering                | Default `9` — clear of SFX (3–5) and captions (6)         |
| `top` (in `<style>`)   | Vertical position (px)        | Default `1180` (just below platform recording). Adjust per scene if the recording covers a different region. |
| `left` (in `<style>`)  | Horizontal position (px)      | Default `60`. Don't move into the right-edge action column. |

## Don'ts

- **Don't add a coupon code field.** The discount is automatic via the link. A code on screen creates friction. (User-confirmed 2026-04-28.)
- **Don't fire before `t=3.0s`.** Strategy doc rule.
- **Don't fire during a hero word.** The bubble is a soft reminder, not a slam — pick a calm moment in the platform recording.
- **Don't extend `data-duration` past 4.0s.** Longer holds break the rhythm of the surrounding narration.
- **Don't add SFX.** Per `audio-design.md`.
- **Don't omit `class="clip"`.** Without it, the bubble would persist after the scene ends and clash with the badge / endcard.
