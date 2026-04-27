// shared/lib/effects/phase-crossfade.js
//
// Blur + opacity crossfade between two scene containers. Total span
// 1.1s (0.5s outgoing blur, 0.4s outgoing fade, 0.5s incoming bloom).
// Outgoing scene gets visibility:hidden after the swap so it stops
// painting. Incoming scene must start at opacity:0 in CSS or the
// initial tl.set will surface a 1-frame flash.
//
// SOURCE: templates/shorts/anthropic/index.html:520-527 (T1 transition;
//         pattern repeats unchanged at T2 and T3).
//
// USAGE:
//   phaseCrossfade(tl, "#phase1", "#phase2", { at: 5.6 });
//   phaseCrossfade(tl, "#phase2", "#phase3", { at: 11.6, blur: 20 });
//
// Drop this function into your host composition's <script> (above the
// timeline construction) and call it once per scene boundary.
//
// CONSTRAINTS:
//   - tl must be a paused gsap.timeline created synchronously
//   - fromSel and toSel must each resolve to exactly one element
//   - The two scenes should be siblings under the composition root
//   - Both scenes need explicit z-index so the incoming paints over
//     the outgoing during the overlap window
//   - Do NOT also tween fromSel's opacity to 0 elsewhere — this owns
//     the exit. Per the hyperframes skill: scenes have entrances only;
//     the transition handles the exit.

function phaseCrossfade(tl, fromSel, toSel, opts) {
  var at = (opts && opts.at) || 0;
  var blur = (opts && opts.blur) || 20;
  var outgoingOpacityDuration = (opts && opts.outgoingOpacityDuration) || 0.4;

  // Outgoing: blur + small zoom-in (0.5s), then fade (0.4s, starting +0.3s)
  tl.to(fromSel, { filter: "blur(" + blur + "px)", scale: 1.04, duration: 0.5, ease: "power1.in" }, at);
  tl.to(fromSel, { opacity: 0, duration: outgoingOpacityDuration, ease: "power1.in" }, at + 0.3);
  tl.set(fromSel, { visibility: "hidden" }, at + 0.7);

  // Incoming: prepare (blurred + slightly small + invisible) at +0.4
  tl.set(toSel, { filter: "blur(" + blur + "px)", scale: 0.97, opacity: 0, visibility: "visible" }, at + 0.4);
  // Fade in (0.3s) starting +0.4
  tl.to(toSel, { opacity: 1, duration: 0.3, ease: "power1.inOut", overwrite: "auto" }, at + 0.4);
  // Settle: blur clears + scale corrects (0.5s) starting +0.6
  tl.to(toSel, { filter: "blur(0px)", scale: 1, duration: 0.5, ease: "power1.out", overwrite: "auto" }, at + 0.6);
}
