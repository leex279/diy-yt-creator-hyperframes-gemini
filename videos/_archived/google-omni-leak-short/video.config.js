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

    // 3s slide-in module card — disabled per-video (template default OFF).
    moduleInterstitial: false,

    // Time-bounded 10% OFF pill. Wired to the recomputed Phase 4 start (60.94).
    discountBubble: true,
    discountBubbleStart: 60.94,
    discountBubbleDuration: 22,    // Phase 4 spans 60.94 → 85.68 (~25s, bubble visible most of it)

    // 5s contextual end-card — Mastery wordmark + 4 community offerings +
    // Link in Description ↓ + 10% OFF + dynamous.ai. Default = totalDuration-5.
    endcard: true,
  },

  // ── Future overlays (not yet implemented) ─────────────────────────
  // subscriptionBanner: { enabled: false },
  // supportBanner:      { enabled: false },
};
