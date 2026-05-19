# Shorts safe zone — content must stay out of the bottom 1/3 (mobile UI dead zone)

Vertical Shorts (1080×1920) render inside YouTube's mobile player, which **overlays a large UI panel on the bottom ~1/3 of the frame**: title, channel name, audio attribution, action stack (Like/Comment/Share/Remix), and sometimes ad cards. Any content placed in that region is obscured at playback time on phone — the most-watched device for Shorts.

The rule is simple and hard:

> **No information-bearing content may sit below y=1280 on the 1080×1920 canvas.** That includes text, primary visuals (cards, screenshots, diagrams), CTAs, debate questions, brand wordmarks shown as content, and any element the viewer is supposed to read or absorb.

Persistent decorative chrome (ambient gradients, shape backdrop, vignette, film-grain) and `index.html`-level branding strips (top-banner wordmark, progress bar) are exempt — they're either invisible at low opacity or part of the host frame, and YouTube's UI happens to land on top of them.

---

## The numbers

| Band | Canvas y-range | Height | Role |
|---|---|---|---|
| Top safe zone | 0 → 240 | 240px | Mobile status bar + creator/Shorts chrome overlay |
| **Active content zone** | **240 → 1280** | **1040px** | **The only region where text and primary visuals are guaranteed visible** |
| Bottom UI dead zone | 1280 → 1920 | 640px | Title, channel info, action stack, ad cards |

The 1280 cutoff comes from the observed footprint of YouTube's Shorts UI overlay on iPhone 13/14/15 + Pixel 7/8/9 — the most common viewing devices. Older phones cut even higher (up to y=1180 on smaller screens), so 1280 is the safe upper bound across the device fleet.

---

## How this interacts with `shorts-thumbnail-frames.md`

The thumbnail-grade first and final frames are screenshotted at frame zero (no UI overlay), so the 5 mandatory elements (topic / anchor / brand / outcome / CTA) can use the FULL 1920px canvas height. **But** if any of those elements lives below y=1280, it WILL be obscured during real-time playback — the thumbnail freeze-frame is a static-screenshot context, not a watched-on-phone context.

Practical implication: if the held final frame has a CTA pill or URL line below y=1280, it works as a screenshot tile but vanishes the moment the viewer un-pauses. Move informational elements above y=1280 even on the final hold — let only ambient/chrome live below.

## How this interacts with `shorts-typography.md`

Typography minimums (48px+ for list-item primary, 36px+ for descriptors, 140px+ for hero slam) are unchanged. This rule is about **placement**, not size. A perfectly-sized 56px CTA question at y=1450 still fails — not because it's too small, but because the viewer literally can't see it under the YouTube panel.

## How this interacts with `visual-pacing-5s.md`

Pacing beats inside the dead zone don't count — if a marker sweeps under text at y=1500, the viewer never sees the sweep, so it doesn't reset the static-frame clock. Every beat must land within the active content zone.

---

## Implementation guidance

### CSS pattern — flex `justify-content: center` on a tall column

Most scenes use `padding: var(--pad-top) var(--pad-x) var(--pad-bottom)` with `flex justify-content: center`. To respect the safe zone, set:

```css
:root {
  --pad-top: 240px;     /* top mobile UI overlay */
  --pad-x:   70px;
  --pad-bottom: 640px;  /* bottom UI dead zone */
}
```

With those values, content centers in y=240 → 1280 automatically. Operators who shrink one scene's vertical density (fewer rows, smaller hero) get the centering for free.

> **Note**: existing templates (incl. `templates/shorts/dynamous-slides/`) ship with `--pad-bottom: 200px` — too small. New templates MUST use `--pad-bottom: 640px` (or document the override). Existing templates need to be migrated as their next video lands.

### Bottom-anchored elements (cards, callouts, decorations)

If a scene uses `position: absolute; bottom: N px` for a card or callout, the card's BOTTOM EDGE must be at canvas y ≤ 1280:

- `bottom: N` from canvas bottom = canvas y of bottom edge = 1920 - N
- For bottom edge ≤ 1280: N ≥ 640

So anywhere you'd be tempted to write `bottom: 100px`, write `bottom: 640px` instead.

### Scenes that legitimately fill more vertical real estate

Some scene archetypes legitimately want the full canvas height (counter ramps, multi-row enumerations). For those: keep top stack anchored at y=240, end visual content by y=1280, and let any "tail" elements (marker sweeps, scale pulses on existing items) stay in the active zone.

If a 6-row list won't fit in 1040px at the required typography minimums:
- **First**: shorten copy (most overflows are wordy text, not sizing)
- **Then**: reduce gap between rows by 4-8px
- **Then**: trim to 5 rows (group items)
- **Never**: extend rows into the dead zone

### CTA scenes (thumbnail-grade final frame)

The CTA scene has special weight: it's both the last spoken moment AND the looped freeze-frame thumbnail. The 5 mandatory `shorts-thumbnail-frames` elements ALL belong above y=1280:

- Topic statement / debate question → upper-third (y=300-700)
- Visual anchor (flame/icon) → mid (y=500-900)
- Brand chrome → upper-third (y=300-450)
- Outcome receipt → mid (y=700-1100)
- CTA pill → mid-to-lower (y=900-1250)
- URL line → BOTTOM of active zone (y=1150-1250) — NOT in the dead zone

The Dynamous endcard pattern (4 community offerings + button + 10% OFF + URL) is dense. Either shrink offering type by ~10% to fit OR split across two stacked sub-cards both above y=1280.

---

## Self-check before declaring a Short done

Open the rendered MP4 in a player. Drag the playhead through every scene. At each frame:

1. Is any **information-bearing element** (text the viewer should read, a card/screenshot/diagram, a CTA, a URL) sitting below y=1280?
2. If yes — that element is invisible to the actual viewer on phone. Move it up.

The bottom 640px should contain ONLY persistent background chrome (ambient gradient, shape-backdrop drift, vignette edge, optional progress bar). Nothing the viewer needs to read.

A useful mental model: pretend YouTube has drawn a horizontal black bar from y=1280 to y=1920. Would the video still communicate? If not, content needs to move up.

---

## Why we didn't catch this sooner

The HyperFrames studio preview displays the full 1080×1920 canvas at desktop scale — every pixel is visible. The mobile UI overlay only appears when the rendered MP4 plays inside the actual YouTube Shorts player. Inspect + lint + validate all see the full canvas, so they pass on layouts that fail at playback time.

Until a lint rule lands that flags `position: absolute; bottom: N` with N < 640 OR information-bearing elements below y=1280, this is a human compensation. Audit by hand before declaring a Short done.

---

## Where this rule applies

- Every vertical Short (`templates/shorts/<style>/`, every `videos/<slug>/` with 1080×1920 canvas).
- Includes all aesthetic variants: anthropic, archon, dynamous-slides, claude-code-version, google, openai, standard, editorial, game-map.

## Where this rule does NOT apply

- Long-form (1920×1080) — landscape playback has no equivalent overlay panel.
- Square (1080×1080) for legacy formats — different UI footprint.
- A Short shipped explicitly as a desktop/web-only deliverable where mobile playback is not the primary target (rare; flag in the video's `notes.md`).

---

## When to update this rule

If YouTube changes its Shorts UI footprint (e.g., a new ad placement extends the dead zone further up), update the y=1280 cutoff and bump every template's `--pad-bottom` accordingly. Track the change date inline.

Last calibration: 2026-05-19 (iPhone 13/14/15 + Pixel 7/8/9 viewports, current YouTube Shorts player).
