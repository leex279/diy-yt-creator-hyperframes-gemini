// video.config.js — per-video feature flags for claude-code-v2128-133-short.
// Loaded as the first <script> in body, before any overlay HTML.
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  dynamous: {
    // Persistent bottom-left brand pill. Fades in at t=3s, stays full video.
    badge: true,

    // 10% OFF discount bubble. Auto-wired to phase 4 start via discountBubblePhase4Start.
    // Disabled — the new Dynamous endcard ships with its own 10% OFF badge,
    // so the floating bubble during phase 2 would be redundant.
    discountBubble: false,
  },

};
