// video.config.js — per-video feature flags.
// Loaded as the first <script> in body, before any overlay HTML.
// Google shorts ship with Dynamous promotion enabled by default
// (mirrors templates/long-form/claude-code-version + the parallel
// claude-code-version shorts template).
window.VIDEO_CONFIG = {

  // ── Dynamous AI promotion ──────────────────────────────────────────
  // Three independent overlays — enable any combination.
  dynamous: {
    // Persistent top-left brand pill. Fades in at t=3s, stays full video.
    // Top-left placement avoids the bottom progress rail on the vertical canvas.
    badge: true,

    // 3s slide-in module card at the first scene transition (~5.6s).
    // Update moduleId, moduleName, moduleAccentColor per release if needed.
    moduleInterstitial: true,
    moduleId: 10,
    moduleName: 'MCP Servers + Skills',
    moduleAccentColor: '#ec4899',  // pink — module 10

    // Time-bounded 10% OFF pill. Auto-wired to the Phase 4 (CTA) start by
    // the guard in index.html unless discountBubbleStart is overridden here.
    discountBubble: true,
    discountBubbleDuration: 39,   // seconds — bubble runs 132.96 → 171.96, just before endcard
    discountBubbleStart: 132.96,  // override — matches recomputed P4 anchor

    // 5s end-card with 4 community offerings, fires at TOTAL_DURATION - 5.
    endcard: true,
    endcardStart: 172,            // override — total 177s, endcard owns last 5s
  },

  // ── Future overlays (not yet implemented) ─────────────────────────
  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
