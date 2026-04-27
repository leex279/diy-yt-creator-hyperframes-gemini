// shared/lib/effects/hero-slam-shake.js
//
// 4-tick inline shake that lands on the impact frame of a slam word.
// ±5px translate at 40ms intervals, then settles. Use sparingly — one
// shake per phase max, otherwise it cheapens the effect.
//
// SOURCE: templates/shorts/anthropic/index.html:514-517.
//
// USAGE:
//   // After narration transcript gives you the slam word's start time:
//   var slamT = transcript[heroWordIndex].start;  // seconds
//   heroSlamShake(tl, "#p1-hero", slamT);
//
// CONSTRAINTS:
//   - tl must be a paused gsap.timeline created synchronously
//   - sel must resolve to exactly one element
//   - The element should ALREADY be entered (visible at full scale).
//     Typical pattern: gsap.from() the element with back.out(1.7) at
//     scaleT, then heroSlamShake(tl, sel, scaleT + 0.15) so the shake
//     lands a few frames after the scale-in completes.
//   - overwrite: "auto" is set on every tick so this composes safely
//     with other x-tweens on the same element.

function heroSlamShake(tl, sel, slamT) {
  tl.to(sel, { x: 5,  duration: 0.04, ease: "none", overwrite: "auto" }, slamT);
  tl.to(sel, { x: -5, duration: 0.04, ease: "none", overwrite: "auto" }, slamT + 0.05);
  tl.to(sel, { x: 4,  duration: 0.04, ease: "none", overwrite: "auto" }, slamT + 0.10);
  tl.to(sel, { x: 0,  duration: 0.04, ease: "none", overwrite: "auto" }, slamT + 0.15);
}
