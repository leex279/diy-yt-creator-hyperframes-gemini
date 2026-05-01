// video.config.js — per-video feature flags.
// Loaded as the first <script> in body, before any overlay HTML.
// All features default to false. Flip to true per video to enable.
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  dynamous: {
    badge: true,

    moduleInterstitial: true,
    moduleId: 10,
    moduleName: 'MCP Servers + Skills',
    moduleAccentColor: '#ec4899',

    discountBubble: true,
    discountBubbleDuration: 12,
  },

  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
