# Component: dynamous-badge

Persistent Dynamous brand mark for opted-in Shorts. Sits in the bottom-left YouTube Shorts safe zone, idle at opacity 0.55, fades in once at `t=3.0s` and stays static.

> **OPT-IN.** Do not add this component to a video unless the author opted in to the Dynamous promotion at spawn time. See `videos/_template-wiring-snippet.md` for the canonical opt-in flow.

## What it produces

```
   1080 × 1920 frame  (top of video)
   ┌────────────────────────────────────────┐
   │                                        │   ← top safe zone (380 px reserved
   │      [ video phase content ]           │     for YouTube title + channel)
   │                                        │
   │                                        │
   │                                        │
   │                                        │
   │   ┌────────────────────┐               │   ← badge: bottom-left,
   │   │ ◆  dynamous.ai     │               │     opacity 0.55, glass pill
   │   └────────────────────┘               │
   │                                        │   ← bottom safe zone (380 px,
   │   [ progress bar ]                     │     comments / likes / subscribe)
   └────────────────────────────────────────┘
```

Single 0.6s entrance at `t=3.0s` (`opacity: 0 → 1`, `x: -12 → 0`, ease `power2.out`). Then static for the rest of the composition.

## Required tokens

None. The component inlines its own colors (midroll v3 palette) and font (`Inter`). It does NOT depend on `--text-dim`, `--bg`, or other host-provided tokens — works on any dark canvas.

## Wire into a host composition

1. **Copy the logo asset** (HyperFrames bundler rejects parent-of-project paths):

   ```bash
   cp shared/logos/dynamous-logo.png videos/<slug>/assets/dynamous-logo.png
   # PowerShell: Copy-Item shared/logos/dynamous-logo.png videos/<slug>/assets/dynamous-logo.png
   ```

2. **Paste the three sections** from `component.html` into `videos/<slug>/index.html`:
   - The `<div id="dynamous-badge">…</div>` HTML at the top of your composition's root `<div>` (next to `#top-banner` and `#progress-track`).
   - The `<style>` block contents into your composition's existing `<style>`.
   - The `<script>` block contents into your composition's existing GSAP `<script>` (or as a separate `<script>` after GSAP loads).

3. **Call the entrance from your root timeline:**

   ```js
   addDynamousBadgeEntrance(tl);
   ```

## Position rationale (YouTube Shorts safe zone math)

YouTube Shorts reserves the top 380 px (title + channel name) and the bottom 380 px (action column + likes / comments / subscribe) of the 1920 px frame. The right ~120 px is also reserved for the action column.

Placing the badge at `bottom: 460px; left: 60px;` lands it:
- 80 px above the bottom-380 reserve — comfortably clear of the comments row.
- 60 px in from the left edge — clear of the left safe zone.
- Centered vertically in the lower third of the playable area, where viewers' eyes naturally drop after reading hook copy.

## Don'ts

- **Don't move into the right-edge action column.** The right ~120 px is reserved for YouTube's UI; a badge there will be partly hidden.
- **Don't raise opacity above 0.6.** The badge is meant to be quiet — louder than 0.6 starts competing with phase content.
- **Don't add `class="clip"`.** The badge is persistent — it must stay visible across phase boundaries. Adding `clip` would hide it during gaps in the timed-element list.
- **Don't lower `t=3.0s`.** The 3-second-hook rule is load-bearing: the badge must NOT appear during the opening hook. Strategy doc rule: "Never start the video with the brand name."
- **Don't pulse the badge.** The Remotion source had a `topicMatches` pulse — we intentionally dropped it. Use the module interstitial block instead for topic-matched moments.

## Lint expectation

```bash
npx hyperframes lint videos/<slug>
```

Expect 0 errors after wiring. Warnings are fine. The component does not introduce any timed (`data-start` / `data-duration` / `data-track-index`) elements.
