// video.config.js — per-video feature flags.
// Loaded as the first <script> in body, before any overlay HTML.
// Claude Code version videos ship with Dynamous promotion enabled by default.
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  // Three independent overlays — enable any combination.
  dynamous: {
    // Persistent bottom-left brand pill. Fades in at t=3s, stays full video.
    badge: true,

    // 3s slide-in module card at first scene transition (top-right corner).
    // Update moduleId, moduleName, moduleAccentColor per release if needed.
    moduleInterstitial: true,
    moduleId: 10,
    moduleName: 'MCP Servers + Skills',
    moduleAccentColor: '#ec4899',  // pink — module 10

    // Time-bounded 10% OFF pill. Auto-wired to the CTA scene start + duration.
    discountBubble: true,
    discountBubbleDuration: 12,    // seconds to show during the CTA scene
  },

  // ── Future overlays (not yet implemented) ─────────────────────────
  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
