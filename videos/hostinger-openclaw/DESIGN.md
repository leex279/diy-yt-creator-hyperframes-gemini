# Design Reference — Hostinger × OpenClaw

## Identity direction

Practical, hands-on tutorial energy — built on a deep navy stage with Hostinger's signature purple. Tech-confident but beginner-friendly. No gradient overload, no AI-slop maximalism. Display weight does the heavy lifting; mono labels carry the structural rhythm.

## Color tokens

| Token            | Value                | Role                                          |
| ---------------- | -------------------- | --------------------------------------------- |
| `--bg`           | `#0E0F19`            | Page / scene background (deep navy)           |
| `--bg-2`         | `#15172A`            | Card / panel background                       |
| `--bg-3`         | `#1F2240`            | Elevated card surfaces, icon plates           |
| `--ink`          | `#FFFFFF`            | Primary text                                  |
| `--muted`        | `#A0A3BD`            | Secondary text                                |
| `--muted-2`      | `#6B6E8A`            | Tertiary / dim text                           |
| `--accent`       | `#673DE6`            | **Hostinger purple** — primary CTA + accents  |
| `--accent-2`     | `#8B5CF6`            | Lighter purple — kickers, highlights          |
| `--accent-dim`   | `#2D1B69`            | Deep purple — backgrounds, gradients          |
| `--success`      | `#00C896`            | Savings, applied coupons, "live" indicators   |
| `--line`         | `rgba(255,255,255,0.08)` | Subtle divider                            |
| `--line-2`       | `rgba(255,255,255,0.14)` | Stronger divider, pill borders            |

## Typography

| Family             | Weights         | Role                                                  |
| ------------------ | --------------- | ----------------------------------------------------- |
| **Manrope**        | 300 / 500 / 700 / 800 | Display headlines, body, UI labels             |
| **JetBrains Mono** | 400 / 500       | Kickers, data, prices, coupon codes, terminal feel    |

### Type scale (at 1920×1080)

| Use                        | Size       | Weight |
| -------------------------- | ---------- | ------ |
| Mega CTA headline (s14)    | 160px      | 800    |
| Hook headline (s1)         | 180px      | 800    |
| Big stat (s13)             | 480px      | 800    |
| Price hero (s7)            | 260px      | 800    |
| Section headline           | 84–96px    | 800    |
| Plan title                 | 56px       | 800    |
| Card title                 | 30–32px    | 700    |
| Body                       | 22–26px    | 300    |
| Kicker / mono label        | 22px       | 500    |
| Coupon code (mono)         | 80px       | 500    |

## Motion system

- **Entrance defaults**: `y: 30–60, autoAlpha: 0` → final position, `power3.out` or `expo.out`, 0.5–0.8s
- **Snappy bits** (badges, pills): `back.out(1.4–2)`, 0.4–0.5s
- **Counters**: 0.8–1.0s with `power2.out`, paired with `onUpdate` formatting
- **Breathing / mid-scene activity**: `sine.inOut`, `yoyo: true, repeat: 1`, 1.2–1.6s
- **Glow pulses**: opacity sine yoyo
- **Stagger**: 0.10–0.18s between siblings (cards, list items, pills)
- **Avoid**: same ease on every tween in a scene; use at least 3 different eases per scene

## Composition rhythm

- **Hard cuts** between most scenes — keeps the tutorial pacing snappy and feels professional
- **One shader transition** at the hero deal-reveal moment (s7 → s8, `cinematic-zoom` at 25.25s) — the moment the discount lands, vision shifts
- Scene durations: 2.5s (lockup) → 5s (plan comparison, setup grid). Heavier info = longer dwell.

## Signature visual elements

- **Mono kickers** at top-left of every section: `09 / Always on` — gives the video editorial structure
- **Accent line** under headlines on hero scenes — short purple bar, draws in
- **Subtle dotted grid** (80px) behind most scenes — masked to fade at edges, adds tech texture without competing
- **Purple glow blobs** on hero/CTA scenes — large, soft-blurred, low opacity, slow pulse
- **Grain layer** at 14% opacity, `mix-blend-mode: overlay` — gives video tooth
- **Vignette** on certain scenes — gentle edge darkening pulls focus to center
