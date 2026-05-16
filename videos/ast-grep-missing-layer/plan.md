# Composition Plan — ast-grep-missing-layer

> **Phase 1 output.** Built from `research/content-brief.md` (Phase 0). Consumed by Phase 2 (script), Phase 3.5 (retention), and Phase 4 (build).
>
> **Template:** `templates/long-form/standard/` (dark navy + 4-accent rotation, 1920×1080, 30fps)
> **Target duration:** 270s ±10% (4:30)
> **Voice:** edge-tts en-US-AndrewNeural @ +10% (draft) → 145 WPM ≈ 660 words narration budget
> **Audience:** developers using AI coding agents (Claude Code, Cursor, Copilot)
> **Tone:** tech-influencer-edgy, but every number traces to a verified receipt in the content brief

---

## 1. Scene Inventory

11 scenes. Sum of `data_duration` = **272s** (within +10% target).

| # | Scene archetype (template file) | `data_start` | `data_duration` | Topic-bar text | Key visual | Words | Retention components |
|---|---|---|---|---|---|---|---|
| 01 | `scene-hook.html` | 0 | 14 | THE OVER-COUNT SLAM | Animated counter slamming 164 → 130 hits, 22 → 12 files; orange/yellow accent | ~38 | impact-slam SFX on stat landing; back.out(1.6) pill pop; ambient breath; bg-music-hook fade-in |
| 02 | `scene-architecture-stack.html` | 14 | 28 | THE 3-LAYER SEARCH STACK | 3 horizontal accent-striped layers (blue=Layer 1 ripgrep/ugrep; cyan=Layer 2 ast-grep; purple=Layer 3 mgrep/vector) with a "MISSING" badge on Layer 2 | ~68 | Layer reveal stagger 150ms; "MISSING" badge red-glow pulse on Layer 2 (one finite yoyo); marker-sweep under "Layer 2" headline; bg-music-body crossfade |
| 03 | `scene-image-hero.html` | 42 | 32 | WHAT AST-GREP ACTUALLY DOES | Annotated diagram: text → AST → meta-var capture (`$VAR`, `$$$BODY`); JSON output overlay snippet | ~78 | Sub-line pattern reveal step-by-step (3 beats ~4s apart per `step-by-step-reveal.md`); typewriter on the `try { $$$BODY } catch ($ERR) { $$$CBODY }` pattern; spring-pop on JSON output card |
| 04 | `scene-video-embed.html` (re-purposed) | 74 | 38 | DEMO 1 — THE STRING-LITERAL LIE | Terminal capture: `grep` shows 164, then `ast-grep --lang ts` shows 130; cut to VSCode at `workflows/src/dag-executor.test.ts:2813` highlighting `'console.log("hi")'` as a string literal in red | ~88 | scale-slam SFX on each receipt landing (164, 130, 22, 12); cinematic-whoosh on cut to VSCode; marker-sweep under the highlighted string literal; arrow callout |
| 05 | `scene-stat-pill-row.html` | 112 | 32 | DEMO 2 — THE NUMBERS WALL | 2 huge color-rotated stat pills: `+122%` (orange) over-count on `useState`, `415` (yellow) `try…catch` blocks grep cannot find; full 5-query head-to-head table animated row-by-row below | ~78 | Step-by-step reveal of 5 rows in the table (~5s apart per `step-by-step-reveal.md`); impact-slam on `+122%`; impact-slam on `415`; back.out(1.6) on pills; bg-music-body continues |
| 06 | **HOSTINGER MIDROLL** — `shared/lib/blocks/hostinger-midroll/` (copy into `compositions/hostinger-midroll.html`) | 144 | 20 | (block-locked chrome) | Brand-locked 5-phase Hostinger panel: intro → Web Hosting → VPS → AI Website Builder → CTA → outro. Werbung badge top-left. URL: hostinger.com/DIYSMARTCODE | ~25 (spoken over) | Block-internal animations (purple gradient pills, glass cards, white flash transitions); bg-music ducks to `--cta` segment for energy bump; **no SFX inside block** (block ships silent for host-narrator handoff) |
| 07 | `scene-side-by-side.html` | 164 | 34 | TOKEN ECONOMICS — WHY YOUR AGENT BLEEDS | Left card (blue, "grep alone"): 22 Reads · ~11K tokens · 34 false positives. Right card (cyan, "with ast-grep"): 1 JSON pipe · 0 Reads · 130 real call sites. Arrow between cards labeled `~10K tokens saved / refactor` | ~80 | Side-by-side x-slide entrance from opposite sides; counter roll on token deltas; marker-sweep under "10K tokens"; spring-pop on the savings badge |
| 08 | `scene-source-cards.html` (re-purposed as steelman cards) | 198 | 30 | THE STEELMAN — "WAIT, BUT…" | 3 photo + overline + title cards: "MY IDE DOES THIS" / "MY CODEBASE IS SMALL" / "SEMGREP DOES MORE". Each card flips to a 1-line concession + 1-line redirect on second beat. | ~72 | 3-card entrance stagger 120ms; per-card flip-reveal on second narration beat (concede → redirect); marker-sweep under each redirect; pop SFX on each card landing |
| 09 | `scene-hook.html` (re-purposed as install receipt) | 228 | 18 | INSTALL IT NOW | Big mono code line: `pnpm add -g @ast-grep/cli` (Inter mono 84px). Sub-line: "5.8 seconds. Windows. macOS. Linux." Then a typewriter showing the first command: `ast-grep run -p 'console.log($$$A)' -l ts` | ~42 | Typewriter on command line; spring-pop on each OS-pill (Windows/macOS/Linux); marker-sweep under "5.8 seconds"; ambient stays calm before CTA build |
| 10 | `scene-cta.html` | 246 | 26 | THE DEBATE | `#cta-question` (44px): "grep over-counted by 122% on a real refactor. Are you giving ast-grep to your coding agent today — or still pretending Layer 1 is enough?" + comment pill + subscribe pulse + next-video card | ~64 | Subscribe pulse `repeat: 4` (finite); marker-sweep under "122%"; comment-pill spring-pop; bg-music-cta peaks; cinematic-whoosh on cta entrance |
| 11 | (Dynamous outro tail — embedded in `scene-cta.html`) | 272 (end-overlap on scene 10) | — | "dynamous.ai community" | Dynamous wordmark + URL pill fade-in over the last 4s of scene 10. Single locked spoken line. Endcard carries the rest visually. | ~14 | Wordmark fade-in 0.6s expo.out; URL pill back.out(1.4); fade-to-black at TOTAL_DURATION |

**Total `data_duration` sum:** 14 + 28 + 32 + 38 + 32 + 20 + 34 + 30 + 18 + 26 = **272s** ✅ (within 270 ±10%)

**Words budget:** 38 + 68 + 78 + 88 + 78 + 25 + 80 + 72 + 42 + 64 + 14 ≈ **647 words** ≈ 268s @ 145 WPM ✅

> **Scene 11 note:** The Dynamous outro is not a separate scene — it is the final 4 seconds of `scene-cta.html` content (per the rule: Dynamous artifacts are Shorts-shaped; long-form uses scene-cta. We inline the wordmark + url pill + locked spoken line at the tail of scene 10). It is listed separately above for clarity but does NOT add to `data_duration`.

---

## 2. Hook — Scene 01 first two sentences (LOCKED, copy verbatim into Phase 2)

> **"Your AI agent just searched 22 files. Only 12 of them had what it was looking for. The other 10? grep lied. Here's the CLI that doesn't."**

Source: content-brief.md §7 H1 (RECOMMENDED). Anchored to Archon Query 1 (`console.log` in `.ts`: grep 164/22 vs ast-grep 130/12) per `examples/archon-head-to-head.md` Query 1.

Phase 2 may light-edit for TTS flow (sentence breaks, breath beats) but MUST NOT change the numbers (22, 12, 10) or the rhetorical structure.

---

## 3. Hostinger Midroll — Spec & Decision

**Approach: USE THE EXISTING BLOCK.** `shared/lib/blocks/hostinger-midroll/` is a 20s long-form (1920×1080) block, brand-locked, silent (host narrator covers), already ships with Werbung badge for DE law. It is purpose-built for exactly this slot and is already in production use across the channel's long-form videos.

**Placement:** `data_start=144s` (53% of 272s — between the killer Demo 2 receipts and the Token Economics scene, which is the natural breath-beat in the narrative arc per content-brief.md §11).

**Wiring:**
1. Copy block into the video: `cp shared/lib/blocks/hostinger-midroll/block.html videos/ast-grep-missing-layer/compositions/hostinger-midroll.html`
2. Add a wrapper in `index.html` between the stat-pill-row and side-by-side wrappers:
   ```html
   <div id="scene-hostinger-wrap" class="scene-wrapper"
        data-composition-id="hostinger-midroll"
        data-composition-src="compositions/hostinger-midroll.html"
        data-start="144"
        data-track-index="1"></div>
   ```
3. Add `addLabel("hostinger", 144)` to the root timeline and bracket it with two `crossfadeScenes()` calls (from `#scene-stat-pill-row-wrap` → `#scene-hostinger-wrap` at `hostinger-=0.4`, then `#scene-hostinger-wrap` → `#scene-side-by-side-wrap` at `side-by-side-=0.4`).
4. Recipe will instruct on any asset copy (product screenshots already ship with the block).

**Spoken voiceover during the 20s** (host narrator delivers over the silent block; written into `script.txt` as scene 06):
> *"Quick word from our affiliate — Hostinger. If you're spinning up your own AI agents or coding sandboxes, Hostinger gives you 10% off with the code DIYSMARTCODE in the description. Now — back to ast-grep."*

(~28 words @ 145 WPM ≈ 11.5s, fits comfortably inside 20s window with room for breath and the block's "Back to the video." outro at 18.5–20s.)

---

## 4. Retention Strategy — Pre-Allocation

Per-scene retention components reserved. Phase 3.5 will fine-tune timings to word-anchors after `transcript.json` exists. Count: **38 pre-allocated retention components** across 10 active scenes.

| Scene | Components |
|---|---|
| 01 Hook | impact-slam SFX, counter-roll (164→130, 22→12), back.out(1.6) pill pop, marker-sweep underline on "grep lied", ambient breath |
| 02 Layer model | layer reveal stagger (150ms), marker-sweep under "Layer 2", red-glow pulse on MISSING badge (1 finite yoyo), bg-music-body crossfade |
| 03 Concept | typewriter on `try { $$$BODY } catch ($ERR) { $$$CBODY }`, step-by-step reveal (3 beats), spring-pop on JSON card |
| 04 Demo 1 | scale-slam SFX on receipts (×4), cinematic-whoosh on VSCode cut, marker-sweep under the highlighted string literal, red arrow callout overlay |
| 05 Demo 2 | impact-slam on +122% & 415, back.out(1.6) pill pop, step-by-step row reveal of the 5-query table |
| 06 Hostinger | (block-internal animations only — no host-side retention beats; bg-music ducks to cta-energy briefly) |
| 07 Token economics | side-by-side x-slide (±80), counter-roll on token deltas, marker-sweep under "10K tokens", spring-pop on savings badge |
| 08 Steelman | 3-card stagger (120ms), per-card concede→redirect flip, marker-sweep on each redirect, pop SFX ×3 |
| 09 Install | typewriter on install command, spring-pop on OS pills (×3), marker-sweep under "5.8 seconds" |
| 10 CTA | subscribe-pulse `repeat: 4`, marker-sweep under "122%" inside the cta-question, comment-pill spring-pop, bg-music-cta peak, cinematic-whoosh on entrance |

**Visual-pacing audit (per `.claude/rules/visual-pacing-5s.md`):** every scene has at least one beat per 4–5 seconds. The longest scene is `04 Demo 1` (38s) which has 4 receipt-landings + VSCode cut + marker-sweep + arrow callout (7 beats / 38s = avg 5.4s gap — flagged for Phase 3.5 to tighten with one extra beat, likely a row-by-row reveal of the file paths).

---

## 5. Engagement CTA — Locked wording

Per `.claude/rules/engagement-cta.md`: binary/short-list answerable, polarizing, references a specific claim from the video, low-cost to answer.

**Spoken (scene 10 final 4s of narration, before the Dynamous outro):**
> *"grep over-counted by 122% on a real refactor. Are you giving ast-grep to your coding agent today — or still pretending Layer 1 is enough? Drop your pick in the comments."*

**On-screen (`#cta-question` element in `scene-cta.html`, 44px, persists through final frame):**
> *"grep over-counted by 122%. Giving ast-grep to your agent today — or still pretending Layer 1 is enough?"*

**YouTube description (Phase YT — final paragraph of `youtube-description.md`):**
> *"grep over-counted by 122% on a real Archon refactor — 138 hits vs ast-grep's 62, across 30 files vs 26. So: are you giving ast-grep to your coding agent today, or still pretending Layer 1 is enough? Drop your pick below."*

All three reference the same claim (`+122%` on `useState` — Archon Query 2 per `examples/archon-head-to-head.md`). Binary (today / still-pretending), polarizing (calls out the skeptic tribe), low-cost to answer (5-second opinion).

---

## 6. Visual Proof Shots — per-scene placeholder spec

These are the screen-shareable hero visuals Phase 4 will scaffold. Real screenshots get dropped into `videos/ast-grep-missing-layer/assets/screenshots/` during build.

| Scene | Visual asset | Source receipt |
|---|---|---|
| 01 Hook | Animated counter slamming `164 → 130` (`.ts` `console.log` hits) with file count `22 → 12` below | Archon Query 1 |
| 02 Layer model | 3-tier diagram (Exact / Structural / Semantic) with ripgrep, ast-grep, mgrep logos and one example query per tier | ceaksan.com framing |
| 03 Concept | Inline animated diagram: source code box → AST tree-icon → meta-var capture overlay; JSON output snippet card with `byteOffset`, `metaVariables.A` fields | GitHub README + setup-and-live-test §4 |
| 04 Demo 1 | VSCode screenshot at `workflows/src/dag-executor.test.ts:2813` with `'console.log("hi")'` highlighted in red strike; PowerShell terminal showing `grep \| measure` → 164 then `ast-grep run -p ... -l ts` → 130 | archon-head-to-head Query 1 receipts |
| 05 Demo 2 | Full 5-query head-to-head table animated row-by-row; two huge stat pills (`+122%` orange, `415` yellow) leading | archon-head-to-head full table |
| 06 Hostinger | (block-locked — Hostinger wordmark, 3 product screenshots ship with the block) | shared/lib/blocks/hostinger-midroll/ |
| 07 Token economics | Left card: "agent w/ grep — 22 Reads ≈ 11K tokens". Right card: "agent w/ ast-grep — 1 JSON pipe, 0 Reads". Arrow with `~10K tokens saved / refactor` callout | archon-head-to-head §agent-coding angle |
| 08 Steelman | 3 cards with skeptic icons: laptop+IDE / tiny-codebase / semgrep-logo. Each flips to concede→redirect text on beat 2 | research/00-summary.md §7 |
| 09 Install | Big mono `pnpm add -g @ast-grep/cli` command; sub-line "5.8s on Windows 11"; 3 OS pills (Windows / macOS / Linux); typewriter follow-up showing `ast-grep run -p 'console.log($$$A)' -l ts` | setup-and-live-test §1 |
| 10 CTA | `#cta-question` element + comment pill + subscribe pulse + next-video card (placeholder `next-video-thumbnail.png`). Dynamous wordmark + URL pill fade in for the last 4s. | engagement-cta + dynamous outro rule |

**Final-frame slam:** end of scene 10 holds on the `#cta-question` text + subscribe pulse + Dynamous URL for ~1.5s before fade-to-black. Per `.claude/rules/shorts-thumbnail-frames.md`, long-form's first-frame rule is more relaxed (manual thumbnail), but the final frame still doubles as the loop-pause still — keep the question persistent.

---

## 7. SFX Cue Mapping (`videos/ast-grep-missing-layer/sfx-cues.txt`)

Currently shipped: `impact-slam, scale-slam, cinematic-whoosh, spring-pop, pop`. **No changes needed** — these cover every cue this plan reserves. Volumes per `.claude/rules/audio-design.md`:

| Cue | Usage in this video | data-volume |
|---|---|---|
| `impact-slam` | Hero receipts (`+122%` and `415` in scene 5; `10K tokens` in scene 7) | 0.15 |
| `scale-slam` | Demo 1 receipt landings (164, 130, 22, 12) | 0.15 |
| `cinematic-whoosh` | Scene 4 cut to VSCode; scene 10 CTA entrance; possibly scene 06 entry/exit | 0.11, **1.5s duration** per audio-design.md whoosh placement rule |
| `spring-pop` | Card / pill entrances (savings badge, JSON card, OS pills, comment pill) | 0.11 |
| `pop` | Small chip / list item (steelman card landings, table rows) | 0.10 |

**Ambient bg-music bed (3-segment, per long-form template):**
- `bg-music-hook` — 0–14s (data-volume 0.12)
- `bg-music-body` — 14–246s (data-volume 0.07; ducked even further at 144–164s while Hostinger CTA energy peaks — operator note for build)
- `bg-music-cta` — 246–272s (data-volume 0.12)

No per-scene SFX during the Hostinger midroll (06) — the block ships with its own crossfades and the host narrator covers.

---

## 8. Total Duration Sanity Check ✅

Sum of `data_duration`:
```
14 (01) + 28 (02) + 32 (03) + 38 (04) + 32 (05) + 20 (06) + 34 (07) + 30 (08) + 18 (09) + 26 (10) = 272s
```
Target: 270s ±10% (243–297s). **272s lands within target.** ✅

`TOTAL_DURATION = 272` (set in `index.html` per template instructions).
`tl.set({}, {}, TOTAL_DURATION)` pad enforced at root timeline tail per `.claude/rules/hyperframes-pitfalls.md` §1.

Words budget: ~647 words ÷ 145 WPM × 60 ≈ 268s narration. Leaves ~4s for breath beats / Hostinger handoff silence. ✅

---

## 9. Index.html Wiring Map (for Phase 4 build)

Sub-composition wrapper count: **11** (10 scenes + 1 Hostinger midroll + captions wrapper).

```
scene-hook              data-start=0
scene-architecture-stack data-start=14
scene-image-hero         data-start=42      (re-purposed for concept diagram)
scene-video-embed        data-start=74      (re-purposed for terminal+VSCode demo)
scene-stat-pill-row      data-start=112
hostinger-midroll        data-start=144     (NEW wrapper — block from shared/lib)
scene-side-by-side       data-start=164
scene-source-cards       data-start=198     (re-purposed for steelman cards)
scene-hook (clone #2)    data-start=228     (re-purposed for install receipt)
scene-cta                data-start=246
captions                 data-start=0  (captions sub-comp, track-index 9)
```

**Two scene-hook instances:** scene 9 (install) re-uses `scene-hook.html` as a clone. Standard pattern per template README "Adding more scenes" — duplicate to `compositions/scene-install.html`, change `data-composition-id` to `scene-install`, update `window.__timelines["scene-install"]` registration. Phase 4 documents the duplication step.

**Crossfade chain** (per `crossfadeScenes()` template helper, fires at `<next-label>-=0.4`):
hook → arch-stack → image-hero → video-embed → stat-pill-row → **hostinger** → side-by-side → source-cards → install → cta. 10 crossfades total. Add `addLabel("hostinger", 144)` + `addLabel("install", 228)` to the label chain.

---

## 10. Open Items for Phase 2 (script) to settle

1. **Hostinger spoken script wording** — locked above in §3 but Phase 2 may tighten for breath/cadence (don't change the URL or the code `DIYSMARTCODE`).
2. **Layer 3 (mgrep) attribution** — per content-brief.md §4 care note, "mgrep ~2× fewer tokens" is single-anecdotal. Phase 2 narration in scene 02 should attribute as *"some authors report"* OR drop the claim entirely. Recommend: drop the token figure; keep the 3-tier model.
3. **Claude Code switched to ugrep+bfs** — per content-brief.md §13, this claim is plausible-but-unconfirmed. Phase 2 should attribute as *"per one independent author"* OR drop. Recommend: attribute in scene 02 as background, don't lead with it.
4. **Steelman card ordering** — content-brief.md §6 has 3 (IDE / codebase-small / semgrep) plus a 4th lighter one ("just a refactor tool"). Plan reserves 3 cards in scene 08. Phase 2 picks the 3 strongest — recommend the original 3, drop the 4th.
5. **Scene 03 concept depth** — 78 words in 32s is comfortable but Phase 2 should decide whether to spend the full beat on meta-vars (`$VAR`, `$$$BODY`) or split between meta-vars + tree-sitter parsers. Recommend: lead with meta-vars (more visual), mention tree-sitter once.

---

## Acceptance — Phase 1 complete

- [x] Scene table with 11 rows, all `data_start` + `data_duration` set, sum = 272s ✅
- [x] Hook locked: scene 01 first 2 sentences verbatim
- [x] Hostinger midroll spec: existing block at `shared/lib/blocks/hostinger-midroll/`, placed at 144s
- [x] Retention components pre-allocated: 38 across 10 active scenes
- [x] Engagement CTA: spoken + on-screen + YouTube wording locked
- [x] Visual proof shots listed per scene (10 entries + Hostinger block reference)
- [x] SFX cue mapping verified against shipped `sfx-cues.txt`
- [x] Total duration math checked
- [x] Wiring map for Phase 4 build provided
- [x] Open items for Phase 2 enumerated
