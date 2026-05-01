// video.config.js — per-video feature flags.
// Loaded as the first <script> in body, before any overlay HTML.
// All features default to false. Flip to true per video to enable.
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  // Three independent overlays — enable any combination.
  dynamous: {
    // Persistent bottom-left brand pill. Fades in at t=3s, stays full video.
    badge: false,

    // 3s slide-in module card at first scene transition (top-right corner).
    // Before enabling: set moduleId, moduleName, moduleAccentColor below to
    // match the curriculum module from dynamous-modules.json.
    moduleInterstitial: false,
    moduleId: 10,
    moduleName: 'MCP Servers + Skills',
    moduleAccentColor: '#ec4899',  // pink — module 10

    // Time-bounded 10% OFF pill. Auto-wired to the CTA scene start + duration.
    discountBubble: false,
    discountBubbleDuration: 12,    // seconds to show during the CTA scene
  },

  // ── Future overlays (not yet implemented) ─────────────────────────
  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
