// video.config.js — per-video feature flags.
// Loaded as the first <script> in body, before any overlay HTML.
// Google shorts ship with Dynamous promotion enabled by default
// (mirrors templates/long-form/claude-code-version + the parallel
// claude-code-version shorts template).
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  // Four independent overlays — enable any combination.
  dynamous: {
    // Persistent top-left brand pill. Fades in at t=3s, stays full video.
    // Top-left placement avoids the bottom progress rail on the vertical canvas.
    badge: true,

    // 3s slide-in module card at the first scene transition (~5.6s).
    // OFF by default — the popup competes with the hero→setup transition on
    // a 90-180s shorts canvas and most operators preferred it disabled.
    // Set to true per-video when the short is specifically promoting a
    // Dynamous module. Update moduleId, moduleName, moduleAccentColor to match.
    moduleInterstitial: false,
    moduleId: 10,
    moduleName: 'MCP Servers + Skills',
    moduleAccentColor: '#ec4899',  // pink — module 10

    // Time-bounded 10% OFF pill. Auto-wired to the Phase 4 (CTA) start by
    // the guard in index.html unless discountBubbleStart is overridden here.
    discountBubble: true,
    discountBubbleDuration: 6,    // seconds — Phase 4 is 6s long
    // discountBubbleStart: 18.4, // optional override; default = Phase 4 start

    // 5s contextual end-card — Mastery wordmark + 4 community offerings +
    // Link in Description ↓ + 10% OFF + dynamous.ai. Fires at totalDuration-5.
    // Per-video: set endcardStart explicitly, or leave undefined and the
    // guard auto-computes it from the root #root data-duration attribute.
    endcard: true,
    // endcardStart: 19.0,        // optional override; default = totalDuration - 5
  },

  // ── Future overlays (not yet implemented) ─────────────────────────
  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
