// shared/lib/effects/stat-pill-pop.js
//
// Single-element scale-pop entrance — back.out(1.6) from scale 0.85.
// Designed for stat pills, badges, and any "land with weight" element.
//
// SOURCE: templates/shorts/anthropic/index.html:535-536.
//
// USAGE:
//   statPillPop(tl, "#p2-pill-1", P2 + 0.9);
//   statPillPop(tl, "#p2-pill-2", P2 + 1.4);
//
// Stagger by 500ms when popping multiple pills in sequence (per the
// canonical pattern). Stagger lower (300ms) for tight beats; higher
// (700ms) for breathing room.
//
// CONSTRAINTS:
//   - Element should be CSS-positioned at its hero-frame target. The
//     tween animates FROM scale 0.85 + opacity 0 TO the CSS state.
//   - Don't pair with a competing scale-tween on the same element at
//     the same time — back.out's overshoot peak will be clipped.

function statPillPop(tl, sel, at) {
  tl.from(sel, { scale: 0.85, opacity: 0, duration: 0.6, ease: "back.out(1.6)" }, at);
}
