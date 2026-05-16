// shared/lib/effects/shake-reject.js
//
// Horizontal "no" shake on any element. 6 ticks: ±15px, ±10px, ±5px → 0
// over 0.5s total. Optional red tint filter (hue-rotate pulse) fires during
// the shake to reinforce the "rejected" / "wrong" read.
//
// SOURCE: original — no template source.
//
// USAGE:
//   shakeReject(tl, "#error-card", P2 + 3.0);
//   shakeReject(tl, "#error-card", P2 + 3.0, { duration: 0.6, intensity: 20 });
//   shakeReject(tl, "#error-card", P2 + 3.0, { tint: false }); // shake only
//
// CONSTRAINTS:
//   - Element must be visible before this fires (entrance completed).
//   - overwrite: "auto" on every x-tick so this composes with other x-tweens.
//   - intensity scales all displacement values proportionally.
//   - tint uses CSS filter: hue-rotate(-25deg) at peak → hue-rotate(0deg).
//     Works on any element; test on elements with complex gradients.
//
// SFX WIRING (host wires <audio> separately when calling this effect):
//
//   Cue 1: screen-shake   data-volume: 0.11   track-index: 3
//   Cue 2: glitch-zap     data-volume: 0.09   track-index: 4
//   Both fire LAYERED at: at + 0.0  (drift ≤ 0.05s)
//
//   Wire in your host index.html (replace <AT> with the `at` argument):
//
//   <audio id="sfx-shake-1"
//          class="clip"
//          src="assets/sfx/screen-shake.mp3"
//          data-start="<AT>"
//          data-duration="0.52"
//          data-track-index="3"
//          data-volume="0.11"></audio>
//   <audio id="sfx-zap-1"
//          class="clip"
//          src="assets/sfx/glitch-zap.mp3"
//          data-start="<AT>"
//          data-duration="0.52"
//          data-track-index="4"
//          data-volume="0.09"></audio>
//
//   Alignment check: both SFX fire at data-start == at (exact).
//   Drift ≤ 0.05s (percussive reject onset).
//   sfx-cues.txt must list: screen-shake, glitch-zap

function shakeReject(tl, sel, at, opts) {
  opts = opts || {};
  var duration  = opts.duration  !== undefined ? opts.duration  : 0.5;
  var intensity = opts.intensity !== undefined ? opts.intensity : 15;
  var tint      = opts.tint      !== undefined ? opts.tint      : true;

  // Scale tick distances by intensity (default 15 = max displacement 15px)
  var scale = intensity / 15;
  var d1 = 15 * scale;
  var d2 = 10 * scale;
  var d3 = 15 * scale;
  var d4 = 10 * scale;
  var d5 =  5 * scale;

  // Distribute 6 ticks evenly across duration
  var tick = duration / 6;

  tl.to(sel, { x:  d1, duration: tick, ease: 'none', overwrite: 'auto' }, at + tick * 0);
  tl.to(sel, { x: -d2, duration: tick, ease: 'none', overwrite: 'auto' }, at + tick * 1);
  tl.to(sel, { x:  d3, duration: tick, ease: 'none', overwrite: 'auto' }, at + tick * 2);
  tl.to(sel, { x: -d4, duration: tick, ease: 'none', overwrite: 'auto' }, at + tick * 3);
  tl.to(sel, { x:  d5, duration: tick, ease: 'none', overwrite: 'auto' }, at + tick * 4);
  tl.to(sel, { x:   0, duration: tick, ease: 'power2.out', overwrite: 'auto' }, at + tick * 5);

  // Optional red tint: hue-rotate peaks at the first big tick, fades out
  if (tint) {
    tl.to(sel, {
      filter: 'hue-rotate(-25deg) saturate(1.6)',
      duration: tick * 2,
      ease: 'power2.in'
    }, at);
    tl.to(sel, {
      filter: 'hue-rotate(0deg) saturate(1)',
      duration: tick * 3,
      ease: 'power2.out'
    }, at + tick * 2);
  }
}
