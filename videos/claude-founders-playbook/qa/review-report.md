# Video Review (Final, Extended) — claude-founders-playbook

**Verdict**: `FAIL_HIGH` · 0 BLOCKER · 4 HIGH · 4 MEDIUM · 2 LOW
**Mode**: pre-publish · **Auto-fix**: safe · **Visual**: off (static)
**Canvas**: 1080×1920 vertical Short · **Duration**: 143.22s (matches narration exactly)
**Pass**: final-extended-9-scene (re-review after Scene 5 insertion)

## Verdict summary

| Agent | Verdict | BLOCKER | HIGH | MEDIUM | LOW |
|---|---|---:|---:|---:|---:|
| video-timing-pacer | FAIL_HIGH | 0 | 1 | 3 | 0 |
| video-render-validator | WARN_MEDIUM | 0 | 0 | 1 | 2 |
| video-layout-typography | FAIL_HIGH | 0 | 3 | 0 | 0 |
| video-script-content | PASS | 0 | 0 | 0 | 0 |
| video-metadata-publish | PASS | 0 | 0 | 0 | 0 |

**Render-safe**: yes (font-var clear, composition 143.2s ≈ narration 143.22s, no missing media, no sub-comp mismatches, no oversized images, no overflow, all 8 SFX cues aligned to phase boundaries).
**Publish-ready**: no — same typography minimums violations as 8-scene + 1 new finding in Scene 5 + 4 visual-pacing-5s violations inside Scene 5 (paced to narration but exceed 5.0s threshold).

---

## Auto-fixes applied (0 this pass)

No new auto-fixes applied in this re-review. The 5 word-anchor drift fixes from the 8-scene review (T-002 #p6-pill-1, T-003 #p6-pill-2, T-004 #p6-pill-3, T-005 #p5-col-cowork, T-006 #p5-col-code) are already baked into the extended composition (now at phase 6/7 selectors).

The 4 new HIGH findings in this pass (typography sizes + Scene 5 pacing) all require user signoff per video-review skill recipe — pacing edits and visual design changes are not in the safe auto-fix table.

---

## Net change vs 8-scene review

| Metric | 8-scene | 9-scene | Δ |
|---|---:|---:|---|
| Composition duration | 105.04s | 143.22s | +38.18s |
| Scenes | 8 | 9 | +1 (Scene 5) |
| HIGH findings (total) | 18 | 4 | **−14** |
| MEDIUM findings (total) | 14 | 4 | **−10** |
| Typography violations | 17 | 18 | +1 (Scene 5 #p5-headline 50px<56px) |
| Timing gaps over 5s | 1 | 4 | +3 (all inside Scene 5 between killer-row entrances) |
| Terminal hold (last frame thumbnail) | 1.18s (FAIL) | 1.72s (PASS) | **+0.54s** |
| SFX whoosh alignment | PASS | PASS | unchanged |
| First-frame thumbnail-grade | PASS | PASS | unchanged |
| Description char count | 1294 | 1437 | +143 |
| Hashtags | 20 | 22 | +2 (+AgenticTechDebt, +StartupFailureModes) |
| CTA 3-place alignment | PASS | PASS | unchanged |
| WCAG contrast warnings (decorative) | 24 | 31 | +7 (Scene 5 badges/skulls) |

Net: HIGH and MEDIUM counts both DROPPED significantly. The big 8-scene blocker (last-frame thumbnail terminal hold <1.5s) is now CLEARED. The new HIGH findings are concentrated in Scene 5 pacing — a natural consequence of pacing 4 stage-killers to ~7s narration beats.

---

## HIGH — needs user signoff before publish (4)

### Timing — Scene 5 visual-pacing-5s violations (1 issue, 4 gaps)

**T-001 — Phase 5 (Four named killers) 4 consecutive gaps > 5s**

The 4-stage-killer cadence is paced to narration word anchors (each stage gets ~7s of narration). But the rule's threshold is 5.0s between meaningful entrances. Four gaps inside Phase 5 exceed it:

| Gap | From | To | Duration |
|---|---|---|---:|
| 1 | 59.02 (#p5-conseq-1) | 64.54 (#p5-row-2) | **5.52s** |
| 2 | 66.45 (#p5-conseq-2) | 72.96 (#p5-row-3) | **6.51s** |
| 3 | 74.16 (#p5-conseq-3) | 80.20 (#p5-row-4) | **6.04s** |
| 4 | 81.20 (#p5-conseq-4) | 88.11 (#p5-wrap-line) | **6.91s** |

**Recommended fix** (NOT auto-applied — pacing edits require user signoff):
Add a marker-sweep beat (sweeping color underline on the killer-name) at the midpoint of each gap. Suggested anchors: 61.7, 69.7, 77.0, 84.5. Each marker is decorative on existing geometry (no chart screenshots involved, so the screenshot-anchor-markers rule does NOT apply). This brings each gap inside Scene 5 down to ≤3.5s.

### Layout/Typography (3 HIGH)

**L-template — 17 pre-existing typography violations** (carried over from 8-scene)
- `.cp-title` 36px → needs 48px (list-item primary)
- `.cp-sub` 24px → needs 30px (descriptor)
- `.surface-name` 34px → needs 48px (list-item primary)
- `.surface-job` 22px → needs 30px (descriptor, renders ~8px on iPhone 13)
- (+ 13 more sub-element selectors in Phases 4 / 6 / 7 / 8)

**Recommended fix**: V3 template-wide issue inherited from `templates/shorts/anthropic/`. Either bump in the video only OR fix at the template root so future videos don't repeat the violation.

**L-005 — NEW Scene 5 phase headline 6px below min**
- `#p5-headline` 50px < 56px phase-headline minimum
- Killer-row body sizes are FINE (50px primary, 30px descriptor — both at-or-above min)

**Recommended fix**: Bump `#p5-headline` from 50px to 56px (line 373 in index.html). Confirm overflow stays clean. The body of Scene 5 is well-sized; only the headline needs the bump.

**L-006 — Last-frame outcome line below min**
- `#p9-outcome` "4 STAGES · 3 SURFACES · 1 FOUNDER" is 32px, outcome-receipt minimum is 36px
- Otherwise the last frame is thumbnail-grade: topic slam 160px PASS, marker-circle on URL PASS, brand chrome PASS, CTA-question PASS, terminal hold 1.72s ≥1.5s PASS.

**Recommended fix**: Bump `#p9-outcome` from 32px to 40px so the last frame fully satisfies the thumbnail-frame outcome-line requirement.

---

## MEDIUM — quality improvements (4)

- **T-002**: Phase 3 quote-card 6.08s real-content gap (20.50 → 26.58 with only a decorative scale-pulse between). Insert marker-sweep under quote-text at ~23.0s on "Instagram".
- **T-003**: Phase 6 5.58s gap (94.32 #p6-pagepill → 99.90 #p6-col-chat). Same pattern as 8-scene review T-001, widened slightly by phase boundary shift. Skeleton-reveal the 3 empty column containers at t=96.5 to fix.
- **T-004**: Phase 4 51.80 scale-pulse decoration doesn't satisfy 5s rule per spec (decorative pulses don't count as beats). Replace with a marker-underline beat.
- **R-001**: 31 decorative WCAG contrast warnings (up from 24 in 8-scene by +7 from Scene 5 badges/skulls). All decorative — token-stream filler, badges, skulls, surface icons, code-num ordinals. No body text fails.

## LOW — informational (2)

- **R-002**: Lint `overlapping_gsap_tweens` false-positive on `#phase-label` (chrome ticker re-applies; `overwrite: 'auto'` already on the initial fromTo).
- **R-003**: Lint `duplicate_media_discovery_risk` on `anthropic-logo-light.svg` — known dual-use (top banner + Phase 1 brand lockup).

---

## Phase YT — YouTube description update (Part A)

- **File**: `videos/claude-founders-playbook/youtube-description.md`
- **Char count**: 1437 (target 1300-1500 Shorts) — PASS
- **Delta vs prior**: +143 chars (1294 → 1437)
- **First 200 chars keywords**: "Claude Code, Anthropic's Founder's Playbook, ... four named killers ... Idea (mistaking building for validating), MVP (agentic technical debt), Launch (founder bottleneck)" — primary keywords front-loaded PASS
- **Hashtags**: 22 (target 15-25) PASS · added: #AgenticTechDebt, #StartupFailureModes · removed: none
- **Hostinger affiliate block**: byte-match PASS, in `----` separators per rule, affiliate wording (no "Sponsored by")
- **Dynamous block**: correctly absent (`meta.json` `dynamousPromotion: false`)
- **Chapters**: correctly absent (Shorts rule)
- **Resources**: 3 URLs unchanged from pre-extension Phase YT run today (all validated live earlier today; not re-fetched per task note)
- **Engagement CTA**: same line in all 3 places (spoken `script.txt`, on-screen `#cta-question` in `index.html`, description closer) — anchor words "playbook" + "vibes" — cross-reference aligned

---

## What ran

- ✅ `video-timing-pacer` · 78 entrances audited across 9 phases · 4 gaps > 5s (all inside Scene 5) · 0 SFX drift over 0.05s · whoosh duration + alignment 100% correct on all 8 cues · first frame thumbnail PASS · last frame thumbnail PASS (terminal hold 1.72s ≥ 1.5s, IMPROVED from 1.18s)
- ✅ `video-render-validator` · lint 0/3 (unchanged warnings) · validate 0/31 (all decorative, +7 from Scene 5 badges/skulls) · inspect 0/0 · font-var blocker CLEAR · composition duration 143.2s matches narration 143.22s
- ✅ `video-layout-typography` · 18 typography violations (+1 from Scene 5 #p5-headline 50<56) · first frame PASS 5/5 · last frame PASS_WITH_MINOR (outcome 32<36) · screenshot-marker check PASS · shape-backdrop rearrange PASS (8/8 phase transitions)
- ✅ `video-script-content` · 0 heteronyms · 23/23 cumulative claims sourced (4 new Scene 5 claims all verified verbatim from PDF p.10/16/23/26) · CTA in all 3 places aligned (anchors: playbook, vibes) · hook score 9.2/10 (+0.2 for mid-video re-hook) · WPM 151 (healthy band)
- ✅ `video-metadata-publish` · description 1437 chars · structure order correct · Hostinger byte-match · 22 hashtags (+2 net) · 4/4 URLs (3 validated today + 1 canonical Hostinger) · CTA cross-reference matches across all 3 places · no banned sections

---

## Next steps for the user

1. **Decide on Scene 5 pacing**: option (a) accept and ship — gaps are paced to actual narration beats and the eye is anchored by the consequence sub-line that drops 1-2s after each row entrance; option (b) insert 4 marker-sweep beats at 61.7 / 69.7 / 77.0 / 84.5 to bring all gaps under 5s.
2. **Decide on Scene 5 headline bump**: `#p5-headline` 50→56 is a 1-line CSS edit; safe.
3. **Decide on last-frame `#p9-outcome` bump**: 32→40px is a 1-line edit; brings last frame fully into thumbnail-grade.
4. **Pre-existing typography (L-template)**: same decision matrix as 8-scene review — fix video-only or push to `templates/shorts/anthropic/` root.

After fixes, re-render and ship.

Report JSON files: `qa/timing-pacer.json`, `qa/render-validator.json`, `qa/layout-typography.json`, `qa/script-content.json`, `qa/metadata-publish.json` (all overwritten this pass).
