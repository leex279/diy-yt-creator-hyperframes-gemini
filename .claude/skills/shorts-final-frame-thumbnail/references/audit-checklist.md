# Audit checklist — final-frame quality gate

Two layers of audit run together: the **baseline rule** (`.claude/rules/shorts-thumbnail-frames.md` — what MUST be present) and the **style-specific** audit (does the picked style's design contract hold?). A final frame ships only when both layers pass.

## Layer 1 — Baseline rule (mandatory)

Run the 4 self-check tests from `.claude/rules/shorts-thumbnail-frames.md` §"Self-check before declaring a Short done":

### Test A — Topic test
Could a stranger paused on the final frame, with no audio and no prior frames, name the video's topic in one sentence?
- **PASS:** Topic statement is dominant (≥120px), clear, and not phrased as a question.
- **FAIL examples:** Topic is missing, is a question, or is overshadowed by a CTA pill.

### Test B — Tap test
Shown as a tile in a YouTube Shorts feed surrounded by other thumbs, would this frame make a thumb-stopping viewer tap?
- **PASS:** The frame uses one of the 11 styles AND the style is pattern-interrupt-y in the channel's adjacent feed (per `style-picker.md` Step 3).
- **FAIL:** The frame is generic (text overlay on a dark background with no style identity).

### Test C — Loop test
When the Short loops and this frame becomes the opening frame, does it set up the topic — or confuse?
- **PASS:** The end frame and the intro frame are different, and the end frame's topic statement IS the video's promise.
- **FAIL:** Same frame as the intro, OR the frame teases something the video already delivered.

### Test D — Screenshot test
If a viewer screenshots and shares this frame, does the share carry the channel + topic — or is it a generic CTA?
- **PASS:** Brand chrome (logo / wordmark / @handle) is present and legible at tile size; topic is in the share.
- **FAIL:** No brand chrome, OR the share is dominated by "Subscribe →".

### Test E — Hold-window static test
Pause the rendered MP4 at `data-start + 0.4s`, `+0.7s`, `+1.0s`, `+1.5s`. Are all four frames identical?
- **PASS:** Yes — the hold is genuinely static after the entrance window ends.
- **FAIL:** A counter is still rolling, a marker is still sweeping, or the shape backdrop is drifting visibly.

### Test F — 5-element completeness
Open the closing-phase HTML. Confirm 4 of these 5 elements are present (#5 is optional):
1. Topic statement (≥120px, dominant)
2. Visual anchor (logo / version / icon / screenshot anchor)
3. Brand chrome (channel logo at corner, ≥40px height)
4. Outcome receipt (one short line, ≥36px)
5. CTA pill (optional, NEVER dominant)

If element 1-4 missing → FAIL. If element 5 is dominant → FAIL (CTA is subordinate).

## Layer 2 — Style-specific audit

Once you've identified which of the 11 styles the frame attempts (from `notes.md` documentation, OR by visual inspection if `notes.md` is absent), run the matching style's audit below. If the style is "no style — generic", that's automatically a FAIL — restyle.

### #1 Neo-minimalism audit
- [ ] ≥50% of canvas is empty (negative space)
- [ ] ≤2 colors total (background + 1 accent)
- [ ] Single subject, no second focal point
- [ ] Topic statement is small-to-medium, NOT slammed jumbo (the empty space carries weight, not the type)
- [ ] No drop shadows, glows, or gradients on the subject
- [ ] No CTA pill on this frame (CTA breaks the calm)

### #2 Surround audit
- [ ] Central anchor (face / object / logo) is dead center
- [ ] 4–8 supporting items in an organized circle / hex / radial pattern
- [ ] Every supporting item identifiable at ~240×135 tile size
- [ ] Center element is LARGER than supporting items (hierarchy is clear)
- [ ] Topic statement is on a top or bottom strip, not at the center

### #3 Tier-rank rainbow audit
- [ ] 3, 5, or 7 ranked items (odd count)
- [ ] Color gradient follows red → blue intuitively (or another committed-to scheme)
- [ ] Number badges visible and ≥48px
- [ ] Base imagery is consistent across rows (same crop, same icon style)
- [ ] Topic statement names the ranking criterion explicitly

### #4 Whiteboard audit
- [ ] Real-feeling whiteboard texture (not flat white)
- [ ] Diagram has hand-drawn feel (not sharp vector lines)
- [ ] Diagram raises curiosity but doesn't fully self-explain
- [ ] If host's hand is in frame: it's authentic, not faked

### #5 Familiar interface audit
- [ ] Source UI matched within ±5% on spacing, fonts, colors, corner radius
- [ ] Platform-specific cues present (verification check, upvote, star rating, etc.)
- [ ] Text inside the interface is curiosity-driven or controversial
- [ ] Topic statement IS the interface content (no separate overlay)
- [ ] Brand chrome is below or beside the fake card, not on top
- [ ] No real-person verified handle used without permission

### #6 Cinematic text audit
- [ ] 3-4 words maximum
- [ ] Text is INSIDE the scene (respects perspective, lighting, depth)
- [ ] Not stuck to corners / edges
- [ ] High-contrast color (yellow + dark scene is canonical)
- [ ] Heavy clean type weight (Inter Black, GT Walsheim Bold, or equivalent)
- [ ] Composition was scene-first, then text placed naturally

### #7 Warped faces audit
- [ ] Distortion looks intentional (clean blend, deliberate offset)
- [ ] Pattern is recognizable (triple-expose / mirror-split / glitch / double-expose)
- [ ] Face is still recognizable (not over-distorted)
- [ ] Palette is desaturated / duotone
- [ ] Background plain or heavily blurred
- [ ] Topic statement is minimal or absent
- [ ] Topic vibe genuinely matches "psychological / heavy / identity"

### #8 Maximalist audit
- [ ] 12-30 items in the collection
- [ ] Items are perfectly arranged (grid / herringbone / isometric / radial)
- [ ] Person, if present, is small and corner-placed (NOT center)
- [ ] Lighting is even across all items
- [ ] Topic statement runs along an edge, not over the collection

### #9 Encyclopedia grid audit
- [ ] 6-12 items in a clean grid (2×3, 3×3, 3×4)
- [ ] Each icon is flat illustration, no shadows / gradients / depth
- [ ] Icon style is CONSISTENT across all items
- [ ] 1-2 word labels per item, same font and size everywhere
- [ ] Background is neutral (white / black / single muted brand color)
- [ ] Topic statement on top: "Every X explained" or equivalent

### #10 Candid fake audit
- [ ] Photo could plausibly have been captured (geometry consistent)
- [ ] No obvious AI artifacts (extra fingers, melted faces, impossible reflections)
- [ ] No text, no arrows, no red circles
- [ ] Decoration is graphic not annotative (floating UI, glowing aura, particles)
- [ ] Brand chrome is small / corner watermark
- [ ] Story is honest (not presenting impossible events as documentary)

### #11 Anti-thumbnail (quiet) audit
- [ ] Background is dark (charcoal / deep navy / muted black, NOT pure black)
- [ ] Subject is host's face with direct camera contact
- [ ] Lighting is dramatic (single key, side or below, NOT flat front)
- [ ] One time-constraint text item, off-round number ("47 seconds", "53 seconds")
- [ ] Type is large, clean sans-serif, high-contrast
- [ ] No CTA, no decoration, no extra text — quiet wins

## Layer 3 — Shelf-life audit (every 6 months)

Run this when reviewing a recurring style or before reusing a style on a new Short:

1. **Saturation re-check.** Open YouTube Shorts feed for the channel's niche. Count thumbs in the picked style across 40 recent uploads (channel + 3 nearest competitors).
   - 0–2 thumbs (≤5%): style still fresh, keep using
   - 3–10 thumbs (8–25%): borderline, differentiate within the style
   - 11+ thumbs (≥28%): saturated, restyle the next Short
2. **Performance correlation.** Pull CTR and replay-rate for the 3 most recent Shorts using this style on the channel.
   - If CTR is rising: keep the style.
   - If CTR is flat: the style still works but isn't winning anymore — explore variants.
   - If CTR is declining: the style has expired for this channel; restyle.
3. **Update notes.** In `videos/<slug>/notes.md` for the most recent Short using this style, log the audit date and outcome.

## Audit output format

When running this checklist, output a structured report:

```markdown
## Final-frame audit — videos/<slug>

**Picked style:** [#N name] (per notes.md)
**Audit date:** YYYY-MM-DD

### Layer 1 — Baseline
- Test A (Topic): PASS / FAIL — <1-line reason>
- Test B (Tap): PASS / FAIL — <1-line reason>
- Test C (Loop): PASS / FAIL — <1-line reason>
- Test D (Screenshot): PASS / FAIL — <1-line reason>
- Test E (Hold-window static): PASS / FAIL — <1-line reason>
- Test F (5-element completeness): PASS / FAIL — <missing element if any>

### Layer 2 — Style-specific (#N)
- [bullet list of style-checks with PASS/FAIL]

### Verdict
- SHIP / RESTYLE / FIX
- If FIX: <ordered list of concrete edits>
- If RESTYLE: <recommended alternate style from the picker>
```

The audit is advisory — the user decides whether to ship, fix, or restyle. The skill's audit mode does NOT edit files unless the user asks.
