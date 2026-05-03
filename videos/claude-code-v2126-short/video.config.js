// video.config.js — per-video feature flags for claude-code-v2126-short.
// Loaded as the first <script> in body, before any overlay HTML.
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  dynamous: {
    // Persistent bottom-left brand pill. Fades in at t=3s, stays full video.
    badge: true,

    // 10% OFF discount bubble. Auto-wired to phase 4 start via discountBubblePhase4Start.
    discountBubble: true,
    discountBubbleDuration: 11,       // seconds (phase 4 runs ~12s before endcard)
    discountBubblePhase4Start: 87.70, // computed from transcript phase 4 boundary
  },

};
