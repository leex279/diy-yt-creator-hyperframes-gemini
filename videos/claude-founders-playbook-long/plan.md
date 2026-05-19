# Composition Plan: claude-founders-playbook-long

**Generated**: 2026-05-17
**Template**: `templates/long-form/anthropic/` (1920×1080, 30fps)
**Topic type**: ARTICLE_RESPONSE
**Source authority**: `research/source-playbook.pdf` (Anthropic, "The Founder's Playbook: Building an AI-Native Startup", v3 May 6 2026, 35 pages)
**Brief**: `research/content-brief.md` (carried over from the 90s Short)
**Target duration**: 540s (~9 min), ~1350 narration words at ~150 WPM

This plan locks the 12-scene order, archetype mapping, image anchors (PDF chapter title pages), accent rotation, retention components, sponsor placement, and the hook/CTA wording for the long-form companion video. Phase 4 will replace placeholder `data_start` values with transcript-anchored word-boundary times once TTS lands.

The long-form expands the existing 143s Short (`videos/claude-founders-playbook/`) into a full chapter-by-chapter walkthrough of the playbook — same Anthropic dark-stage aesthetic, same thesis, but now each PDF chapter gets its own scene with the chapter's own title-page graphic as the visual anchor.

---

## Hook Locked — Long-form variant of the Short's Hook A

> **"Anthropic just published a thirty-five page playbook for AI-native founders. It rebuilds the startup lifecycle from scratch. Idea, M V P, Launch, Scale — same four stages, completely new rules. The cover says it. The first warning inside is that Claude Code will help you fail faster unless you run the discipline. Here is the playbook, chapter by chapter."**

~50 words ≈ 19s at 160 WPM. Pairs with the cover image (`assets/playbook-cover.png`) as the thumbnail-grade open. The cover is dominant from t=0 — YouTube's auto-thumbnail picks the playbook cover with the channel chrome on top.

**Source trace**:
- "35-page playbook" + "AI-native" + "Idea / MVP / Launch / Scale" — PDF table of contents (p.2)
- "Claude Code will help you fail faster" framing — PDF p.10 (42% no-market-need warning) + PDF p.16 (agentic technical debt)
- The cover image is the actual cover of the playbook PDF (page 1)

---

## CTA Locked — debate question, three-place agreement

**Spoken close (~6s narration at 150 WPM, ~15 words):**

> *"So here is the question. Are you running this playbook stage by stage, or still validating with vibes? Drop your stage in the comments."*

**On-screen `#cta-question` text (visible during the held final frame):**

> **"Running the playbook — or validating with vibes?"**

**YouTube description closer (Phase YT) repeats**: full spoken version verbatim.

Why it satisfies `engagement-cta.md` HARD criteria:
1. Binary or short-list answer — "running it" vs "validating with vibes" (or pick the stage you're stuck in) ✓
2. Polarizing stance — directly accuses the audience of skipping validation ✓
3. References specific claim from the video — the playbook's own warning that 42% fail because they shipped without validating ✓
4. Low cost to answer — 1-word stage pick OR a yes/no, senior + beginner can both answer in 5 seconds ✓

---

## Composition Layout (12 scenes)

Scenes map 1:1 to PDF chapters where possible. Chapters 3–6 (the four stages) are the spine. Chapters 1+2 fold into the hook + a setup scene about how the founder role is changing. Chapter 7 ("Same job, new rules") becomes the recap before the CTA. Chapter 8 (Resources) folds into the CTA + YouTube description.

### Accent rotation rule

Anthropic dark-stage long-form: orange leads hook + CTA. Purple / blue / green rotate through the middle. The four stage scenes share a deliberate stage-energy progression (Idea=orange, MVP=purple, Launch=blue, Scale=green) — none of them sit adjacent to a scene of the same accent.

| #  | scene_id                   | archetype                       | data_start | data_dur | accent | figure (PDF anchor)                | purpose |
| -- | -------------------------- | ------------------------------- | ---------- | -------- | ------ | ---------------------------------- | ------- |
| 1  | scene-hook                 | scene-hook.html                 | 0          | 35       | orange | `playbook-cover.png` (PDF p.1)     | Thumbnail-grade open. Cover image dominant + thesis + "chapter by chapter" promise. |
| 2  | scene-source-cards         | scene-source-cards.html         | 35         | 25       | purple | `chapter-1-lifecycle.png` (PDF p.3) + meta cards | Source authority. 3 cards: (a) Anthropic Applied AI byline / publisher, (b) "v3 — May 6 2026 / 35 pages / 7 chapters", (c) Chapter 1 title graphic as proof. |
| 3  | scene-founder-changing     | scene-side-by-side.html         | 60         | 45       | blue   | `chapter-2-founder.png` (PDF p.5)  | Chapter 2 — "What it means to be a founder is changing." Left: old playbook (validate → raise → hire → build → raise → hire more). Right: new playbook (founder + Claude → ship → talk to users → ship). |
| 4  | scene-subscribe-banner-1   | scene-subscribe-banner.html     | 105        | 12       | green  | (no figure; CTA chrome)            | Support banner #1 — ~22% mark. "Subscribe + hit the bell for the rest of the playbook." |
| 5  | scene-idea-stage           | scene-image-3d-reveal.html      | 117        | 80       | orange | `chapter-3-idea.png` (PDF p.8)     | Chapter 3 — Idea Stage. 3D-reveal the chapter title page, then 4 callout pills: goals / exit criteria / failure mode (mistaking building for validating) / Claude surface (Chat for research, Claude as devil's advocate). |
| 6  | scene-mvp-stage            | scene-image-3d-reveal.html      | 197        | 80       | purple | `chapter-4-mvp.png` (PDF p.15)     | Chapter 4 — MVP Stage. 3D-reveal + 4 callouts: goals (real users, real data) / exit criteria (Sean Ellis 40%) / failure mode (false PMF + agentic technical debt) / Claude surface (Claude Code + CLAUDE.md). |
| 7  | hostinger-midroll          | hostinger-midroll.html (block)  | 277        | 20       | (locked) | (brand-locked)                   | Hostinger affiliate midroll, ~51% mark. 20s LOCKED — silent block; narrator does sponsor read over it. |
| 8  | scene-launch-stage         | scene-image-3d-reveal.html      | 297        | 80       | blue   | `chapter-5-launch.png` (PDF p.21)  | Chapter 5 — Launch Stage. 3D-reveal + 4 callouts: goals (first paying customers + small team) / exit criteria (~10 customers, repeatable acquisition) / failure mode (founder bottleneck) / Claude surface (Claude Cowork for ops, Claude Code for shipping). |
| 9  | scene-scale-stage          | scene-image-3d-reveal.html      | 377        | 80       | green  | `chapter-6-scale.png` (PDF p.25)   | Chapter 6 — Scale Stage. 3D-reveal + 4 callouts: goals (durable enterprise revenue + sustainable company) / exit criteria (founder no longer in every loop) / failure mode (delegating before the systems exist) / Claude surface (Claude across the whole company — workflow lock-in). |
| 10 | scene-subscribe-banner-2   | scene-subscribe-banner.html     | 457        | 12       | orange | (no figure; CTA chrome)            | Support banner #2 — ~85% mark. "Hit subscribe + drop your stage in the comments." Sets up the CTA. |
| 11 | scene-same-job             | scene-quote-card.html           | 469        | 45       | purple | `chapter-7-same-job.png` (PDF p.31)| Chapter 7 — "Same job, new rules." The job hasn't changed: find a real problem people will pay to solve. What changed is the tool stack. Pull-quote on the discipline + Resources footnote (4 deeper reads). |
| 12 | scene-cta                  | scene-cta.html                  | 514        | 26       | orange | (chrome only; cover image returns small as receipt) | CTA — debate question on screen + spoken close + brand chrome. Held still ≥1.5s on final frame per `shorts-thumbnail-frames.md` long-form analog. |
| —  | tail                       | (timeline extender)             | 540        | —        | —      | —                                  | `tl.set({}, {}, 540)` to extend the root timeline to the full narration length. |

**Total runtime**: 540.0s (9 min 0 s) ✓

**Sum-check**: 35 + 25 + 45 + 12 + 80 + 80 + 20 + 80 + 80 + 12 + 45 + 26 = 540 ✓

---

## Sponsor placement strategy (locked per user direction 2026-05-17)

User explicitly requested: **Hostinger midroll + 2 channel support banners**. NO Dynamous on-screen midroll (Dynamous still ships in the YouTube description per `youtube-metadata.md` canonical structure rule).

| Placement | Type | Scene | Time (% of runtime) | Job |
|---|---|---|---|---|
| First support | Subscribe banner #1 | Scene 4 | 105s (~19%) | Set the subscribe ask early — before sponsor — so it doesn't read as "sub for more sponsors". |
| Midroll | Hostinger (locked 20s) | Scene 7 | 277s (~51%) | Hostinger affiliate read at the natural mid-point — between MVP and Launch stages. |
| Second support | Subscribe banner #2 | Scene 10 | 457s (~85%) | Final support ask BEFORE the CTA — bridges the recap to the engagement question. |

The two support banners use the same `scene-subscribe-banner.html` archetype with slightly different copy on each (banner #1 = "subscribe for the rest of the playbook"; banner #2 = "if this helped, hit subscribe and drop your stage below").

---

## Retention Component Picks

| # | scene_id                   | Retention components (visual + audio) |
| - | -------------------------- | --------------------------------------- |
| 1 | scene-hook                 | (a) Cover image visible from t=0 (no fade — thumbnail-grade). (b) `effects/hero-slam-shake.js` on the "35 PAGES · 4 STAGES" stat-slam at +6s. (c) `components/highlight-marker-sweep/` on "fail faster" key phrase. (d) `cinematic-whoosh` SFX at boundary (data-start=35, data-volume=0.11) + one `impact-slam` at stat-slam (volume 0.15). |
| 2 | scene-source-cards         | (a) 3-card 5s stagger from archetype. (b) `effects/stat-pill-pop.js` on the "v3 · May 6 2026" date pill. (c) Marker sweep under "Anthropic Applied AI team". (d) Whoosh at boundary. |
| 3 | scene-founder-changing     | (a) Left-right side-by-side entry from opposite directions (~0.8s apart). (b) Strikethrough on the old-playbook chain ("hire → raise → hire more"). (c) Sub-line counter "10-person unicorn" tick from 0→10. (d) Marker sweep under "deliberate plan of action". (e) Whoosh at boundary. |
| 4 | scene-subscribe-banner-1   | (a) Built-in pop-in from archetype. (b) Subscribe-pill finite pulse (3 pulses then settle). (c) Whoosh at boundary. |
| 5 | scene-idea-stage           | (a) 3D rotateY entrance on the chapter graphic (rotateY -25°→0°, back.out(1.4)). (b) 4 callout pills (goals / exit / failure / Claude surface) entering ~15s apart per `step-by-step-reveal.md`. (c) Marker sweep under "mistaking building for validating". (d) `effects/hero-slam-shake.js` on the "IDEA" overline. (e) Whoosh + `scale-slam` (0.15) when the figure locks. |
| 6 | scene-mvp-stage            | (a) 3D rotateY entrance on chapter graphic. (b) 4 callout pills ~15s apart. (c) Marker sweep under "agentic technical debt". (d) Sub-stat counter for "Sean Ellis 40%" tick. (e) Whoosh + `scale-slam` at lock. |
| 7 | hostinger-midroll          | (Brand-locked block — its own internal timeline owns every motion.) Only addition: `cinematic-whoosh` at IN boundary (data-start=277) AND OUT boundary (data-start=297), both volume 0.11. NO additional retention components inside this scene. |
| 8 | scene-launch-stage         | (a) 3D rotateY entrance on chapter graphic. (b) 4 callout pills ~15s apart. (c) Marker sweep under "founder becomes the bottleneck". (d) Counter pill "1 hour → 1 week" decision-delay roll. (e) Whoosh + `scale-slam` at lock. |
| 9 | scene-scale-stage          | (a) 3D rotateY entrance on chapter graphic. (b) 4 callout pills ~15s apart. (c) Marker sweep under "workflow lock-in". (d) Concentric-ring expansion micro-graphic for the Scale-stage moat metaphor. (e) Whoosh + `scale-slam` at lock. |
| 10| scene-subscribe-banner-2   | (a) Built-in pop-in. (b) Subscribe-pill finite pulse + "drop your stage" comment-pill scale pulse. (c) Whoosh at boundary. |
| 11| scene-same-job             | (a) 180px orange quote-mark spring entrance. (b) Marker sweep under "same job". (c) Marker sweep under "new rules". (d) Mono author attribution pill scale pulse. (e) Whoosh at boundary. |
| 12| scene-cta                  | (a) Built-in CTA archetype finite-pulse on `#cta-question` pill. (b) `effects/stat-pill-pop.js` on the comment-pill icon. (c) Subscribe pulse (3 finite pulses). (d) Marker sweep under "validating with vibes" in the spoken hook. (e) `effects/hero-slam-shake.js` on the topic slam at scene start. (f) Held final frame ≥ 1.5s. NO whoosh after scene 12. |

**Pick count summary**: 12 scenes × ~3 components each = ~35 retention picks total. Zero scenes with no picks. Hostinger midroll deliberately has only boundary whooshes (its internal block owns the rest).

---

## Visual Design Language

```yaml
design_tokens:
  template_design_md: "templates/long-form/anthropic/DESIGN.md"
  overrides: []
  accent_rotation:
    - scene_1_hook:                "orange"
    - scene_2_source_cards:        "purple"
    - scene_3_founder_changing:    "blue"
    - scene_4_subscribe_banner_1:  "green"
    - scene_5_idea:                "orange"
    - scene_6_mvp:                 "purple"
    - scene_7_hostinger:           "(locked)"   # brand-locked Hostinger purple
    - scene_8_launch:              "blue"
    - scene_9_scale:               "green"
    - scene_10_subscribe_banner_2: "orange"
    - scene_11_same_job:           "purple"
    - scene_12_cta:                "orange"
  no_adjacent_same_accent: true   # verified by inspection of the table above
  fonts:
    sans: "Inter"
    mono: "JetBrains Mono"
```

---

## Screenshot / Figure Inventory

```yaml
figures:
  - name: "playbook-cover.png"
    source: "User screenshot — PDF p.1 cover (orange)"
    scene: "scene-hook + scene-cta (small return)"
    usage: "Thumbnail-grade first frame anchor. Small cover-chip in CTA scene as the receipt."
  - name: "chapter-1-lifecycle.png"
    source: "PDF p.3 (Chapter 1 title page) — rendered via PyMuPDF"
    scene: "scene-source-cards (one of the 3 cards)"
    usage: "Chapter graphic as visual proof we're reading the actual book."
  - name: "chapter-2-founder.png"
    source: "PDF p.5"
    scene: "scene-founder-changing"
    usage: "Backdrop / small inline chip for the founder-role-change side-by-side."
  - name: "chapter-3-idea.png"
    source: "PDF p.8"
    scene: "scene-idea-stage"
    usage: "Hero anchor for 3D-reveal entrance."
  - name: "chapter-4-mvp.png"
    source: "PDF p.15"
    scene: "scene-mvp-stage"
    usage: "Hero anchor for 3D-reveal entrance."
  - name: "chapter-5-launch.png"
    source: "PDF p.21"
    scene: "scene-launch-stage"
    usage: "Hero anchor for 3D-reveal entrance."
  - name: "chapter-6-scale.png"
    source: "PDF p.25"
    scene: "scene-scale-stage"
    usage: "Hero anchor for 3D-reveal entrance."
  - name: "chapter-7-same-job.png"
    source: "PDF p.31"
    scene: "scene-same-job"
    usage: "Recap scene backdrop."
  - name: "page-11-decision-table.png"
    source: "PDF p.11 — Chat / Cowork / Code decision table"
    scene: "scene-founder-changing (optional secondary anchor)"
    usage: "OPTIONAL — only if the side-by-side scene needs a third proof beat."
```

All figures rendered at 2× scale (DPI ~144 from the PDF), file size well under the `2× canvas dimensions` budget per `.claude/rules/hyperframes-pitfalls.md` §2.

---

## Fact-Check Audit (Phase 1 pass; full audit at Phase 2b)

Every numeric claim, named person, and named company in the script anchors has been verified against `research/source-playbook.pdf` / `research/source-playbook.txt`.

| # | Claim | Scene | Source location | Status |
|---|-------|-------|----------------|--------|
| 1 | Anthropic published a 35-page Founder's Playbook | 1, 2 | PDF cover + page count (36 pages incl. cover) | SOURCED |
| 2 | 4 stages: Idea / MVP / Launch / Scale | 1, 5–9 | PDF table of contents p.2 + chapter titles | SOURCED |
| 3 | "Founders who've never written a line of code are shipping production applications" | 3 | PDF p.4 (Chapter 1 body) | SOURCED |
| 4 | "10-person unicorn has gone from underdog story to deliberate plan of action" | 3 | PDF p.4 | SOURCED |
| 5 | Idea-stage failure mode: "Mistaking building for validating" | 5 | PDF p.10 (Chapter 3 challenges header) | SOURCED |
| 6 | 42% fail because they built something nobody wanted (CB Insights) | 5 (sub) | PDF p.10 + `https://www.cbinsights.com/research/report/startup-failure-reasons-top/` | SOURCED |
| 7 | MVP failure mode: "Falling for false product-market fit" | 6 | PDF p.17 (Chapter 4 challenges header) | SOURCED |
| 8 | Sean Ellis 40% PMF gate | 6 | PDF p.19 ("Build your measurement framework before launch") + Sean Ellis primary source | SOURCED |
| 9 | "Agentic technical debt" framing | 6 | PDF p.16+18 | SOURCED |
| 10 | Launch failure mode: "The founder becomes the bottleneck" | 8 | PDF p.23 (Chapter 5 challenges header) | SOURCED |
| 11 | Launch-stage exit: ~10 paying customers + repeatable acquisition | 8 | PDF p.22 (Launch stage exit criteria) | SOURCED |
| 12 | Scale-stage: founder's role recenters from builder to publisher | 9 | PDF p.26 (Chapter 6 body) | SOURCED |
| 13 | Scale-stage moat: workflow lock-in / compounding data network effects | 9 | PDF p.30 ("Create workflow lock-in") | SOURCED |
| 14 | "Same job, new rules" — find a real problem people will pay to solve | 11 | PDF p.31–32 (Chapter 7) | SOURCED |
| 15 | Resources chapter has 4+ deeper reads | 11 (mention) | PDF p.33–35 | SOURCED |

**Audit conclusion**: CLEAN — every script anchor traces to a specific PDF page. Phase 2b will re-verify and add any new claims the Phase 2 script introduces.

**Banned-claim self-check**: no inventions of percentages not in the source; no fabricated case-study stats; no claims about which Claude surface is "best" beyond what the playbook itself says. Vulcan / Carta Healthcare / Ambral / HumanLayer / Anything case studies are **NOT** in scope for the long-form (they live in `claude.com/blog/building-companies-with-claude-code`, not in the Founder's Playbook PDF). The long-form sticks to the PDF.

**Pronunciation notes pre-flagged for Phase 2a TTS audit** (per `.claude/rules/tts-pronunciation.md`):

- `MVP` → "M V P"
- `CLAUDE.md` → "claude dot M D" (only mentioned once, in scene 6)
- `PMF` → "P M F" (Sean Ellis context)
- Heteronyms: no "live" (adjective sense) appears; no "lead" (noun sense) appears. Both safe.

---

## Composition wiring notes (for Phase 4)

These are the wiring contracts the composition build phase MUST honor:

1. **Scene wrapper `data-composition-id` must match each child file's internal `data-composition-id`.** Per `.claude/rules/sub-composition-wiring.md`. Failure here causes the studio to silently load nothing.
2. **The 4 stage-scenes share the `scene-image-3d-reveal.html` archetype but need 4 separate wrapper IDs** (`scene-idea-wrap`, `scene-mvp-wrap`, `scene-launch-wrap`, `scene-scale-wrap`) and 4 separate `data-composition-id`s. Fork the archetype into 4 distinct scene files under `compositions/` — the figure_src and overline/caption/callouts differ per stage.
3. **The 2 subscribe-banner scenes likewise need separate IDs** (`scene-subscribe-banner-1`, `scene-subscribe-banner-2`) and slightly different copy.
4. **Hook scene must render its topic content visible from t=0** (no fade-in opacity 0). The cover image and "FOUNDER'S PLAYBOOK" overline must be at full opacity at the first rendered frame — that frame is YouTube's auto-thumbnail.
5. **CTA scene must hold final frame ≥ 1.5s after last entrance settles** per `.claude/rules/engagement-cta.md` + the long-form analog of `shorts-thumbnail-frames.md`.
6. **TOTAL_DURATION = 540.0** in the root composition's `tl.set({}, {}, TOTAL_DURATION)` extender.
7. **Whoosh wiring**: 11 inter-scene whooshes at boundaries (data-start = 35, 60, 105, 117, 197, 277, 297, 377, 457, 469, 514), data-duration = 1.5, data-track-index = 3, data-volume = 0.11. NO whoosh after scene 12 (final-frame hold has no boundary).
8. **Hostinger midroll** uses `data-track-index="20"` (block recipe's recommendation), with the host-level CSS `#hostinger-midroll-mount { position: absolute; inset: 0; width: 1920px; height: 1080px; z-index: 50; pointer-events: none; }`.
9. **Accent overrides per scene**: each scene's `--scene-accent` CSS var should be set in the scene wrapper's inline style or in the per-scene HTML. The accent column above is canonical.
10. **`font-family: var(--sans|--mono)` is a render blocker** per `.claude/rules/hyperframes-pitfalls.md` §8. After Phase 4 build, run the sed-fix to replace var() references with literal `'Inter'` / `'JetBrains Mono'` font names in every scene HTML. Grep for matches before render — must be empty.

---

## Open items / Phase 4 retime hooks

- **Replace placeholder `data_start` values** with transcript-anchored word-boundary times after TTS lands and `npx hyperframes transcribe videos/claude-founders-playbook-long` runs.
- **The retimed `data_start` values may shift each scene's end by ±2s** vs the 540.0s budget here. If retimed total drifts beyond ±10s, scenes 5–9 (the four 80s stage scenes) are the safest to trim — their callout-pill pacing has ~15s gaps that can compress to ~12s without violating `step-by-step-reveal.md`.
- The hook (#1), hostinger-midroll (#7 — locked 20s), and CTA (#12) are LOCKED for duration — don't trim those.
- **Hostinger sponsor narration line** must be ~18–19s long to cover the 20s silent block. The script's "Quick break — Hostinger has been running my own VPS for a while now…" beat sits at narration timestamp 277–296s.
