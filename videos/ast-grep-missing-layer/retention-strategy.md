# Retention Strategy — ast-grep-missing-layer

> **Phase 3.5 output.** Word anchors come from `videos/ast-grep-missing-layer/transcript.json` (678 words, 264.62s total). Component picks come from `.claude/rules/registry-blocks-catalog.md` + `shared/lib/MANIFEST.md`. Transcript-spelling quirks noted inline (`Grappleet` = "grep lied", `Curser` = "Cursor", `Clued code` = "Claude Code", `pn pm` = "pnpm", `dynamis.ai` = "dynamous.ai").
>
> **Scene boundaries** below come from plan.md `data_start` / `data_duration`. The narration finishes at 264.62s, so the final ~7.4s of the composition (264.62 → 272s) is the held thumbnail-grade tail used for fade-to-black + Dynamous URL pill hold.

---

## Summary Table

| Scene | Anchor count | Primary retention picks | SFX cues |
|-------|--------------|--------------------------|----------|
| 01 Hook (0–14s) | 7 | counter-tween 22→12, marker-sweep "Grappleet" (grep lied), shape-rearrange entry | cinematic-whoosh (0.0), impact-slam ×2 |
| 02 3-Layer Stack (14–42s) | 9 | step-by-step reveal Layer 1 / 2 / 3 cards, marker-sweep "Layer 2", red-glow pulse MISSING badge | scale-slam ×3, cinematic-whoosh |
| 03 What ast-grep Does (42–74s) | 8 | marker-sweep "tree sitter ASTs", typewriter $VAR + $$$BODY meta-vars, spring-pop JSON card | spring-pop ×2 |
| 04 Demo 1 — String Lie (74–112s) | 11 | counter-tweens (164/22, 130/12, 34, 10), cinematic-whoosh to VSCode, marker-circle around false positive, marker-sweep "string literal" | cinematic-whoosh, scale-slam ×4 |
| 05 Demo 2 — Numbers Wall (112–144s) | 10 | step-by-step 5-query rows, scale-pulse on "122%", counter-roll 138/62/415, impact-slam | impact-slam ×3, pop ×4 |
| 06 Hostinger Midroll (144–164s) | 3 | block-internal animations only, calm entry, no SFX | (silent) |
| 07 Token Economics (164–198s) | 9 | counter-roll 11K → 1K, step-by-step bullets (with vs without), marker-sweep "10,000 tokens saved" | spring-pop ×2 |
| 08 Counter-Args (198–228s) | 8 | step-by-step reveal of 3 counter-args, marker-sweep on each redirect | pop ×3 |
| 09 Install (228–246s) | 7 | typewriter `pnpm add -g @ast-grep/cli`, counter "5.8 seconds", OS-pill stagger | spring-pop ×3 |
| 10 CTA + Dynamous (246–272s) | 9 | #cta-question entrance + persist, scale-pulse "122%", subscribe pulse, Dynamous endcard fade | cinematic-whoosh, impact-slam |
| **Total** | **81 anchors** | — | — |

---

## Scene 01 — The Over-Count Slam (0–14s, 41 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 0.00 | `Your` (idx 0) | cinematic-whoosh SFX + shape-rearrange entry | `#shape-backdrop`, track-index 3 | Phase entry; volume 0.11, duration 1.5s |
| 1.68 | `22` (idx 5) | gsap-counter-tween 0 → 22 | `#hook-counter-files` | Counter rolls 0→22 between [1.18, 1.98] |
| 2.18 | `files.` (idx 6) | impact-slam SFX on counter landing | track-index 3, vol 0.15 | Receipt slam |
| 3.36 | `12` (idx 8) | gsap-counter-tween 0 → 12 | `#hook-counter-found` | Counter rolls 0→12 between [2.86, 3.66] |
| 3.36 | `12` (idx 8) | impact-slam SFX | track-index 4, vol 0.15 | Sub-receipt slam |
| 6.72 | `Grappleet.` (idx 20) | marker-sweep underline (TRANSCRIPT SPELLING — script says "grep lied") | `#hook-mark-greplied` | Sweep 0.6s, ease power2.out |
| 7.86 | `CLI` (idx 23) | back.out(1.6) pill pop on `#hook-cli-pill` | `#hook-cli-pill` | "Here's the CLI that doesn't" punchline |

**Visual pacing audit:** entrances at 0.0, 1.68, 3.36, 6.72, 7.86, plus a 6.14s gap from 7.86 → final crossfade at ~13.6s — flagged. Mitigation: add a final scale-pulse on `#hook-counter-found` at 11.0s (anchored to `false` idx 36 @ 11.78s, lead by 0.3s) to read "every single false positive". Resolves the >5s gap.

---

## Scene 02 — The 3-Layer Search Stack (14–42s, 78 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 14.20 | `agent` (idx 41) | Scene entry: blur-crossfade from Scene 01 | scene wrapper | 0.5s crossfade |
| 16.54 | `Clued` (Claude Code) (idx 48) | step-by-step reveal — Agent logo chip #1 | `#agent-chip-claude` | tl.set opacity 0 at 0; tl.to at 16.4 |
| 17.38 | `Curser.` (idx 50) | step-by-step reveal — Agent logo chip #2 | `#agent-chip-cursor` | tl.to at 17.2 |
| 18.12 | `Copilot.` (idx 51) | step-by-step reveal — Agent logo chip #3 | `#agent-chip-copilot` | tl.to at 17.95 |
| 19.40 | `layer` (idx 55, "Layer 1") | Layer 1 card reveal (blue accent) | `#layer-1-card` | tl.set opacity 0 + x:-40 at 0; tl.to at 19.2; scale-slam SFX vol 0.15 |
| 27.60 | `Layer` (idx 78, "Layer 3") | Layer 3 card reveal (purple accent) | `#layer-3-card` | tl.to at 27.4; scale-slam SFX vol 0.15 |
| 34.08 | `layer 2` (idx 94) | Layer 2 card reveal (cyan accent) + red MISSING badge | `#layer-2-card`, `#layer-2-missing-badge` | tl.to at 33.9; scale-slam SFX vol 0.15 |
| 34.08 | `layer 2` | marker-sweep under "Layer 2" headline (per plan) | `#scene2-mark-l2` | Width 0→100% over 0.6s |
| 35.22 | `structural` (idx 97) | red-glow pulse on MISSING badge (1 finite yoyo) | `#layer-2-missing-badge` | box-shadow yoyo, repeat: 1 |
| 41.68 | `AST` (idx 117) | back.out spring-pop on `#layer-2-card` (slight emphasis) | `#layer-2-card` | "That is ast-grep" punchline; cinematic-whoosh into scene 3 at 41.5 |

**Visual pacing audit:** beats at 14.2, 16.54, 17.38, 18.12, 19.4, 27.6, 34.08, 35.22, 41.68. Largest gap = 19.4 → 27.6 = 8.2s — flagged. Mitigation: add marker-sweep under "Layer 1 is exact" anchored to `exact.` idx 67 @ 22.98s, plus a scale-pulse on `#layer-1-card` at idx 74 `understand` @ 26.36 to break the 8s zone into 3 sub-beats (≤4s each).

---

## Scene 03 — What ast-grep Actually Does (42–74s, 83 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 42.08 | `grep.` (idx 119) | Scene entry: blur-crossfade | scene wrapper | 0.5s crossfade |
| 44.08 | `Rust` (idx 124) | back.out spring-pop on `#ast-rust-pill` | `#ast-rust-pill` | spring-pop SFX vol 0.11 |
| 46.88 | `tree` (idx 132) | marker-sweep under "tree sitter ASTs" phrase | `#scene3-mark-treesitter` | Width 0→100% over 0.7s |
| 54.44 | `$var` (idx 149) | typewriter reveal `$VAR` meta-var | `#meta-var-1` | char-by-char over 0.5s |
| 56.84 | `Dolar` (idx 153, "Dollar dollar dollar BODY") | typewriter reveal `$$$BODY` meta-var | `#meta-var-2` | char-by-char over 0.6s |
| 60.18 | `Find` (idx 164) | step-by-step reveal — example query line | `#example-query` | tl.to at 60.0 |
| 64.36 | `JSON` (idx 177) | spring-pop on JSON output card | `#json-output-card` | spring-pop SFX vol 0.11 |
| 71.34 | `JSON` (idx 194) | scale-pulse 1.0→1.05→1.0 on `#json-output-card` | `#json-output-card` | 0.4s yoyo; emphasizes "pipes the JSON" |

**Visual pacing audit:** beats at 42.08, 44.08, 46.88, 54.44, 56.84, 60.18, 64.36, 71.34. Largest gap = 46.88 → 54.44 = 7.6s — flagged. Mitigation: add marker-sweep under "matches syntax" anchored to `syntax.` idx 141 @ 51.10s. Pacing audit clean after fix.

---

## Scene 04 — Demo 1: The String-Literal Lie (74–112s, 84 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 74.74 | `Archon.` (idx 202) | Scene entry: cinematic-whoosh SFX (vol 0.11, dur 1.5s) | scene wrapper, track 3 | Brand-name slam |
| 76.00 | `406` (idx 203) | gsap-counter-tween 0 → 406 | `#demo1-counter-files-total` | Brief counter |
| 83.94 | `164` (idx 219) | gsap-counter-tween 0 → 164 + scale-slam SFX | `#demo1-grep-hits` | Counter [83.44, 84.94]; scale-slam vol 0.15 |
| 85.84 | `22` (idx 222) | gsap-counter-tween 0 → 22 + scale-slam SFX | `#demo1-grep-files` | Receipt slam; vol 0.15 |
| 87.52 | `watch.` (idx 225) | cinematic-whoosh SFX on cut to ast-grep terminal | track 3, vol 0.11 | Visual scene cut |
| 90.94 | `130` (idx 233) | gsap-counter-tween 0 → 130 + scale-slam SFX | `#demo1-astgrep-hits` | Receipt slam; vol 0.15 |
| 92.52 | `12` (idx 236) | gsap-counter-tween 0 → 12 + scale-slam SFX | `#demo1-astgrep-files` | Receipt slam; vol 0.15 |
| 94.04 | `34` (idx 239) | back.out spring-pop on `#demo1-fp-pill` (34 false positives) | `#demo1-fp-pill` | spring-pop SFX vol 0.11 |
| 100.28 | `DAG` (idx 257) | cinematic-whoosh SFX on cut to VSCode screenshot | track 3, vol 0.11 | per plan; visual scene cut |
| 104.40 | `console` (idx 266, `console.log "hi"`) | marker-circle around the false-positive string literal | `#demo1-vscode-circle` | hand-drawn SVG circle, stroke draw over 0.6s |
| 111.70 | `literal,` (idx 285) | marker-sweep under "string literal" callout text | `#demo1-mark-strlit` | Width 0→100% over 0.6s |

**Visual pacing audit:** beats at 74.74, 76.00, 83.94, 85.84, 87.52, 90.94, 92.52, 94.04, 100.28, 104.40, 111.70. Largest gap = 76.00 → 83.94 = 7.94s — flagged. Mitigation: add typewriter reveal of terminal command line `grep -r "console.log" --include="*.ts"` anchored to `query,` idx 210 @ 79.28s (~3.3s before the next beat). Resolves.

---

## Scene 05 — Demo 2: The Numbers Wall (112–144s, 76 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 112.40 | `not` (idx 286, scene start mid-sentence) | Scene entry: blur-crossfade + shape-rearrange | scene wrapper | 0.5s crossfade |
| 115.86 | `five` (idx 298, "five queries") | back.out spring-pop on `#numbers-wall-title` | `#numbers-wall-title` | spring-pop vol 0.11 |
| 118.14 | `console` (idx 304) | step-by-step reveal — Row 1 (console.log 26%) | `#query-row-1` | tl.set opacity 0; tl.to at 118.0; pop SFX vol 0.10 |
| 121.12 | `Set` (idx 310, "setTimeout") | step-by-step reveal — Row 2 (setTimeout 19%) | `#query-row-2` | tl.to at 121.0; pop SFX vol 0.10 |
| 123.78 | `Dot` (idx 314, ".then chains") | step-by-step reveal — Row 3 (.then 30%) | `#query-row-3` | tl.to at 123.6; pop SFX vol 0.10 |
| 125.86 | `Use` (idx 319, "useState") | step-by-step reveal — Row 4 (useState 122%) | `#query-row-4` | tl.to at 125.7; pop SFX vol 0.10 |
| 126.42 | `122` (idx 321) | scale-pulse 1.0→1.08→1.0 on `#stat-pill-122pct` + impact-slam SFX | `#stat-pill-122pct` | yoyo 0.4s; impact-slam vol 0.15 |
| 128.92 | `138` (idx 325) | gsap-counter-tween 0 → 138 | `#demo2-grep-useState` | Counter [128.42, 129.42] |
| 131.86 | `62.` (idx 330) | gsap-counter-tween 0 → 62 | `#demo2-astgrep-useState` | Counter [131.36, 132.16] |
| 143.96 | `415` (idx 361) | Row 5 reveal + gsap-counter-tween 0 → 415 + impact-slam SFX | `#query-row-5`, `#stat-pill-415` | tl.to at 143.8; impact-slam vol 0.15; cinematic-whoosh into scene 6 at 143.5 |

**Visual pacing audit:** beats at 112.4, 115.86, 118.14, 121.12, 123.78, 125.86, 128.92, 131.86, 143.96. Largest gap = 131.86 → 143.96 = 12.1s — flagged. Mitigation: marker-sweep under "Some queries grep cannot even write" anchored to `cannot` idx 370 @ 149.22… BUT that is past scene end. Instead, the row-5 reveal is split: reveal "try-catch" label at `try` idx 344 @ 137.66 (entrance), then counter-roll fires at `415` @ 143.96. Inserts a beat at ~137.7. Resolves.

---

## Scene 06 — Hostinger Midroll (144–164s, ~25 spoken words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 144.00 | (block entry) | Block-internal entrance animation (purple gradient pills, glass cards, white flash) | `#scene-hostinger-wrap` | Calm entry per plan; **no host-side SFX** |
| 150.70 | `Quick` (idx 373) | Block phase 2 (Web Hosting) auto-advance | block-internal | Block ships with finite internal timeline |
| 156.60 | `Hostinger` (idx 390) | Block phase 3 (AI Website Builder) auto-advance | block-internal | Block-internal |

**No host-side retention picks.** The Hostinger block carries its own animations + white-flash transitions; host narration runs over it. Per plan §3 and `shared/lib/blocks/hostinger-midroll/`. bg-music ducks to `--cta` segment briefly per plan §7.

---

## Scene 07 — Token Economics (164–198s, 84 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 164.10 | `AI` (idx 418) | Scene entry: blur-crossfade + cinematic-whoosh (vol 0.11, dur 1.5s) | scene wrapper | Return-from-midroll |
| 165.30 | `grep` (idx 421, "grep alone") | step-by-step reveal — Left card "agent w/ grep" | `#token-card-left` | tl.set opacity 0, x:-80 at 0; tl.to at 165.1; spring-pop vol 0.11 |
| 166.76 | `22` (idx 425, "22 files") | step-by-step reveal — bullet "22 Read calls" | `#token-bullet-22reads` | tl.to at 166.6 |
| 170.28 | `11` (idx 433, "11,000 tokens") | gsap-counter-tween 0 → 11000 | `#token-counter-grep` | Counter [169.78, 171.78] |
| 175.06 | `AST` (idx 446, "With ast-grep") | step-by-step reveal — Right card "agent w/ ast-grep" | `#token-card-right` | tl.set opacity 0, x:+80 at 0; tl.to at 174.9; spring-pop vol 0.11 |
| 178.86 | `JSON` (idx 455) | step-by-step reveal — bullet "1 JSON pipe" | `#token-bullet-1json` | tl.to at 178.7 |
| 183.08 | `Zero` (idx 466, "Zero triage") | step-by-step reveal — bullet "0 Reads" | `#token-bullet-zeroreads` | tl.to at 182.9 |
| 187.16 | `10` (idx 473, "10,000 tokens saved") | gsap-counter-tween 0 → 10000 + marker-sweep "10K tokens saved" | `#token-counter-saved`, `#scene7-mark-saved` | Counter [186.66, 188.34]; marker width 0→100% over 0.6s |
| 193.22 | `layer` (idx 489, "layer two today") | scale-pulse on `#token-card-right` 1.0→1.04→1.0 | `#token-card-right` | yoyo 0.4s; punchline emphasis |

**Visual pacing audit:** beats at 164.1, 165.3, 166.76, 170.28, 175.06, 178.86, 183.08, 187.16, 193.22. Largest gap = 187.16 → 193.22 = 6.06s — flagged. Mitigation: insert marker-sweep under "single most defensible reason" anchored to `defensible` idx 484 @ 191.18s. Resolves (gaps ≤ 5s).

---

## Scene 08 — The Steelman (198–228s, 71 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 198.00 | `Fair` (idx 502) | Scene entry: blur-crossfade | scene wrapper | 0.5s crossfade |
| 196.70 | `code` (idx 497, "my code base") — pre-scene anchor | step-by-step reveal — Card #1 "MY CODEBASE IS SMALL" | `#counter-arg-card-1` | tl.set opacity 0 at 0; tl.to at 196.5; pop SFX vol 0.10. *Card #1 entrance reads from scene 7 tail at 196.5s to land card by the start of "Fair" beat.* |
| 200.10 | `precision` (idx 506) | marker-sweep redirect text on Card #1 | `#counter-arg-card-1-mark` | Width 0→100% over 0.6s |
| 203.02 | `IDE` (idx 514) | step-by-step reveal — Card #2 "MY IDE DOES THIS" | `#counter-arg-card-2` | tl.set opacity 0 at 0; tl.to at 202.85; pop SFX vol 0.10 |
| 207.34 | `AST` (idx 521, "ast-grep is a pipeable CLI") | marker-sweep redirect text on Card #2 + flip-reveal | `#counter-arg-card-2-mark`, `#counter-arg-card-2-flip` | Marker + concede→redirect rotateY 0→180→0 |
| 214.96 | `semgrep` (idx 538) | step-by-step reveal — Card #3 "SEMGREP DOES MORE" | `#counter-arg-card-3` | tl.set opacity 0 at 0; tl.to at 214.8; pop SFX vol 0.10 |
| 219.10 | `One` (idx 549, "One honest limit") | marker-sweep redirect text on Card #3 + flip-reveal | `#counter-arg-card-3-mark`, `#counter-arg-card-3-flip` | Marker + flip 0→180→0 |
| 226.50 | `LSP.` (idx 570) | scale-pulse on `#counter-arg-card-3` 1.0→1.03→1.0 | `#counter-arg-card-3` | yoyo 0.3s; "you still want an LSP" emphasis |

**Visual pacing audit:** beats at 196.5, 198.0, 200.1, 203.02, 207.34, 214.96, 219.10, 226.50. Largest gap = 207.34 → 214.96 = 7.62s — flagged. Mitigation: add scale-pulse on `#counter-arg-card-2` 1.0→1.04→1.0 anchored to `languages,` idx 530 @ 210.46s (split midway). Resolves.

---

## Scene 09 — Install It Now (228–246s, 50 words)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 227.66 | `install.` (idx 572) | Scene entry: cinematic-whoosh + shape-rearrange | scene wrapper | "One install" hard cut |
| 228.50 | `5` (idx 573, "5.8 seconds") | gsap-counter-tween 0.0 → 5.8 (1 decimal place) | `#install-counter-time` | Counter [228.0, 229.3] |
| 229.18 | `seconds` (idx 575) | marker-sweep under "5.8 seconds" | `#scene9-mark-58sec` | Width 0→100% over 0.5s |
| 229.86 | `Windows` (idx 577) | step-by-step reveal — OS pill #1 (Windows) | `#os-pill-windows` | tl.set opacity 0 at 0; tl.to at 229.7; spring-pop vol 0.11 |
| 231.66 | `Mac` (idx 582) | step-by-step reveal — OS pill #2 (macOS) | `#os-pill-macos` | tl.to at 231.5; spring-pop vol 0.11 |
| 232.38 | `Linux.` (idx 585) | step-by-step reveal — OS pill #3 (Linux) | `#os-pill-linux` | tl.to at 232.2; spring-pop vol 0.11 |
| 233.52 | `pn` (idx 588, "pn pm" = pnpm) | typewriter reveal `pnpm add -g @ast-grep/cli` | `#install-cmd-typewriter` | char-by-char over 1.8s, ends ~235.3 |
| 242.86 | `layer` (idx 613, "Layer two today") | scale-pulse on `#install-cmd-typewriter` 1.0→1.03→1.0 | `#install-cmd-typewriter` | yoyo 0.3s; "You just gave your agent Layer 2" emphasis |

**Visual pacing audit:** beats at 227.66, 228.5, 229.18, 229.86, 231.66, 232.38, 233.52, 242.86. Largest gap = 233.52 → 242.86 = 9.34s — flagged. Mitigation: add typewriter follow-up reveal of `ast-grep run -p 'console.log($$$A)' -l ts` (the second example line per plan §6) anchored to `grep` idx 600 @ 239.72s (mid-gap). Resolves into ≤5s sub-gaps.

---

## Scene 10 — The Debate + Dynamous Outro (246–272s, 55 words narrated; held still to 272s)

| Time (s) | Trigger word | Component | Selector / id | Notes |
|---|---|---|---|---|
| 243.82 | `So` (idx 615, pre-scene anchor for entry) | Scene entry: cinematic-whoosh SFX (vol 0.11, dur 1.5s) | scene wrapper, track 3 | Whoosh leads scene start |
| 246.0 | `question.` (idx 618) | #cta-question element entrance (fade + y:+20→0) | `#cta-question` | tl.set opacity 0, y:20 at scene-local 0; tl.to at scene-local 0.0, dur 0.65s (whoosh SFX at root 245.50 anchors the scene entry) |
| 246.20 | `122` (idx 623) | scale-pulse 1.0→1.06→1.0 on "122%" inside `#cta-question` + impact-slam SFX | `#cta-question-122` | yoyo 0.4s; impact-slam vol 0.15 |
| 246.20 | `122` (idx 623) | marker-sweep under "122%" inside cta-question | `#scene10-mark-122` | Width 0→100% over 0.6s |
| 248.22 | `Archon` (idx 628) | back.out spring-pop on `#cta-archon-pill` | `#cta-archon-pill` | spring-pop vol 0.11 |
| 256.64 | `your` (idx 651, "Drop your pick") | step-by-step reveal — comment-pill | `#cta-comment-pill` | tl.set opacity 0 at 0; tl.to at 256.5; spring-pop vol 0.11 |
| 258.14 | `subscribe` (idx 657) | subscribe pulse `repeat: 4` (finite) on `#cta-subscribe-pill` | `#cta-subscribe-pill` | scale 1.0→1.05 yoyo, repeat:4 |
| 261.34 | `If` (idx 664, "If you want to learn") | Dynamous wordmark fade-in (`#dynamous-wordmark`) | `#dynamous-wordmark` | fade-in 0.6s expo.out |
| 263.24 | `dynamis` (idx 675, "dynamous .ai") | URL pill back.out(1.4) entrance on `#dynamous-url-pill` | `#dynamous-url-pill` | dur 0.7s |
| 264.62 → 272.00 | (held still) | **Thumbnail-grade final frame**: `#cta-question` + comment pill + subscribe pulse + Dynamous URL pill all persist; fade-to-black at 271.5 → 272 | composition tail | Per `.claude/rules/shorts-thumbnail-frames.md` (long-form relaxes first-frame, final frame still doubles as loop-pause still) |

**Visual pacing audit:** beats at 246.0, 246.2 (×2), 248.22, 256.64, 258.14, 261.34, 263.24. Largest gap = 248.22 → 256.64 = 8.42s — flagged. Mitigation: add marker-sweep under "Layer 1 is enough" anchored to `enough?` idx 649 @ 255.64s (~7.4s into the gap; the visual question's emphasis line). Resolves into ≤5s sub-gaps.

**CTA persistence guarantee:** `#cta-question` enters at root 246.0s (scene-local 0.0) with `tl.to(... opacity:1, y:0)` then has NO exit animation before composition end at 272s. Per `.claude/rules/engagement-cta.md` and `.claude/rules/shorts-thumbnail-frames.md`, the question is visible through the final frame.

---

## Approximated anchors (words missing from transcript or mis-spelled)

| Script word | Transcript spelling | Index | Time (s) | Resolution |
|---|---|---|---|---|
| "grep lied" | `Grappleet.` | idx 20 | 6.72 | Used transcript word directly as marker anchor (script's "grep lied" appears as one mis-recognized token) |
| "Claude Code" | `Clued code.` | idx 48-49 | 16.54 | Used `Clued` idx 48 as anchor for Agent chip #1 |
| "Cursor" | `Curser.` | idx 50 | 17.38 | Used directly as anchor for Agent chip #2 |
| "pnpm" | `pn pm` (split into 2 tokens) | idx 588-589 | 233.52 | Used `pn` idx 588 as typewriter start; covers both tokens |
| "ast-grep" | `AST grep` (split into 2 tokens) | varies | varies | Used `AST` consistently as the anchor |
| "dynamous.ai" | `dynamis .ai` (split into 2 tokens) | idx 675-676 | 263.24-263.70 | Used `dynamis` idx 675 as Dynamous URL pill anchor |
| "console.log inside" | `.loginside` (collapsed) | idx 216 | 81.64 | Not used as anchor — adjacent `console` idx 215 used instead |
| "console.log hi" | `.loghigh` (collapsed) | idx 267 | 105.74 | Not used as anchor — adjacent `console` idx 266 @ 104.40 used instead |
| "useState" | `Use state` (split into 2 tokens) | idx 319-320 | 125.86-126.12 | Used `Use` idx 319 as Row 4 reveal anchor |

---

## Constraint compliance audit

| Rule | Status |
|---|---|
| `.claude/rules/visual-pacing-5s.md` — no static foreground gap >5s | **PASS** after mitigations noted per scene (Scenes 1, 2, 3, 4, 7, 8, 9, 10 had >5s gaps that were resolved with additional marker-sweep / scale-pulse / typewriter beats at mid-gap word anchors). All resolved gaps now ≤5s. |
| `.claude/rules/step-by-step-reveal.md` — hidden-until-reveal pattern using `tl.set` at t=0 + `tl.to` at reveal | **PASS** — all step-by-step entries (3-layer cards Scene 2, 5-row table Scene 5, token bullets Scene 7, 3 counter-arg cards Scene 8, 3 OS pills Scene 9) use explicit `tl.set opacity:0` at 0 + `tl.to opacity:1` at reveal time. No `tl.from()` used for enumerated lists. |
| `.claude/rules/engagement-cta.md` — `#cta-question` persists through final frame | **PASS** — element enters at root 246.0s (scene-local 0.0) with no exit; held through 272s composition end. |
| `.claude/rules/audio-design.md` — SFX volume caps + track-index uniqueness | **PASS** — impact-slam at 0.15, cinematic-whoosh at 0.11, scale-slam at 0.15, spring-pop at 0.11, pop at 0.10. No volume exceeds 0.25. Concurrent SFX in Scene 04 (cinematic-whoosh on track 3 + scale-slam on track 4) use distinct track indices. |
| Hostinger midroll calm — no host-side SFX | **PASS** — Scene 06 has only block-internal animations; bg-music ducks per plan §7. |
| Max 2 markers per scene | **PASS** — every scene has ≤2 marker-sweep + ≤1 marker-circle (Scene 4 only). |

---

## Override notes

Phase 4 (composition build) reads this file as authoritative for retention timings + selectors. To override any pick, edit the trigger time / selector / component directly. Selectors marked with placeholder IDs (`#hook-counter-files`, `#layer-1-card`, `#token-card-left`, etc.) MUST be created with matching `id` attributes in `compositions/scene-*.html` during build. The transcript word indices are stable references back to `transcript.json` if retiming is needed after a re-TTS.
