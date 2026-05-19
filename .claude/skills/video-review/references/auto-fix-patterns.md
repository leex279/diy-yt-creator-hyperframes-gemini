# Auto-fix patterns

Deterministic recipes the orchestrator applies when `--fix safe` (or `--fix aggressive`) is on.

Every recipe here is **safe**: the fix has exactly one correct answer derivable from the codebase, applying it never destroys user content, and re-running the relevant agent after the fix confirms the issue is resolved.

If a finding doesn't appear here, it requires user signoff. Even in `--fix aggressive` mode.

## Safe fixes (apply with `--fix safe`)

### `font-family-var-render-blocker`

Replace CSS-variable indirection with literal font names, derived from the video's tokens.

**Detection:** `grep -rE "font-family:\s*var\(--(sans|mono)" videos/<slug>/`

**Fix recipe:**
1. Read `videos/<slug>/tokens/*.css` to find what `--sans` and `--mono` map to. Typical defaults:
   - `--sans` → `'Inter', system-ui, sans-serif`
   - `--mono` → `'JetBrains Mono', ui-monospace, monospace`
2. Apply sed across `videos/<slug>/index.html` + every `videos/<slug>/compositions/*.html`:
   ```bash
   for f in videos/<slug>/index.html videos/<slug>/compositions/*.html; do
     sed -i \
       -e "s|font-family: *var(--sans)|font-family: 'Inter', system-ui, sans-serif|g" \
       -e "s|font-family: *var(--mono)|font-family: 'JetBrains Mono', ui-monospace, monospace|g" \
       "$f"
   done
   ```
3. Re-run `video-render-validator` to confirm grep returns no matches.

### `sub-comp-id-mismatch`

Parent mount's `data-composition-id` doesn't match the child file's published `data-composition-id`. Studio silently loads nothing.

**Fix recipe:**
1. Read the child file (`compositions/X.html`) and parse `<div id="root" data-composition-id="Y">`.
2. Open the parent's `index.html` line where the mount lives.
3. Replace the parent mount's `data-composition-id="WRONG"` with `data-composition-id="Y"` (child's value).
4. Re-run `video-render-validator` to confirm match.

### `render-filename-uses-short.mp4`

Doc/comment references use `-o videos/<slug>/out/short.mp4` instead of `<slug>.mp4`.

**Fix recipe:**
1. `grep -rn "out/short\.mp4" videos/<slug>/`
2. For each match: replace `out/short.mp4` with `out/<slug>.mp4` (substituting actual slug).
3. Re-grep to confirm zero matches.

### `youtube-description-missing`

`videos/<slug>/youtube-description.md` doesn't exist.

**Fix recipe:**
1. Read `meta.json.name` for the title.
2. Read research/vidiq-keywords.md if present for keyword shortlist.
3. Determine video kind (Short vs long-form) from canvas size.
4. Scaffold the description following the canonical structure from `.claude/rules/youtube-metadata.md`:
   - Short: SEO hook → Dynamous block → Resources → Hostinger block → engagement question → hashtags
   - Long-form: same + Chapters section (timestamps from `index.html` `data-start` values, adjusted for any speedup)
5. Fill the engagement question from the spoken closer in `script.txt`.
6. Re-run `video-metadata-publish` to confirm structure.

NOTE: The orchestrator will need user input for the hook paragraph topic-specific keywords. If the description is created with a placeholder hook, mark it `[REPLACE: hook paragraph]` and surface to user.

### `description-banned-phrase`

Description ends on a banned CTA phrase.

**Fix recipe:**
1. Read `videos/<slug>/script.txt` final paragraph — extract the spoken question.
2. Replace the description's final paragraph (last line before hashtags) with the spoken question verbatim.
3. Re-run `video-metadata-publish` to confirm.

### `description-forbidden-arrow`

`→` or `->` characters in description (YouTube may flag).

**Fix recipe:**
1. Read `videos/<slug>/youtube-description.md`.
2. Replace standalone `→` and `->` with `:` (when used as a separator) or empty (when decorative).
3. Re-run `video-metadata-publish`.

### `description-dynamous-block-missing`

The Dynamous CTA block is mandatory on every video and is missing from `youtube-description.md`.

**Detection:**
```bash
grep -c "dynamous\.ai/?code=646a60" videos/<slug>/youtube-description.md
# OR
grep -c "dynamous_ai_10_percent_discount" videos/<slug>/youtube-description.md
```
A `0` from either grep means the block is missing.

**Fix recipe:**
1. Read `videos/<slug>/youtube-description.md`.
2. Locate the position AFTER the SEO hook paragraph (first blank line after the first paragraph) and BEFORE the next section. For long-form, that's BEFORE the `Chapters` header. For Shorts, BEFORE `Resources:`.
3. Insert the exact block (do NOT generate, do NOT paraphrase — paste verbatim):
   ```
   ----
   🚀 Want to learn agentic coding with live daily events and workshops?
   Check out Dynamous AI: https://dynamous.ai/?code=646a60
   Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
   ----
   ```
4. Surround the block with one blank line above and below (in addition to the `----` separators).
5. Re-run `video-metadata-publish` to confirm grep returns ≥ 1 for both URL patterns.

Note: this fix is independent of the `dynamousPromotion` flag in `meta.json`. That flag gates ON-SCREEN Dynamous promotion (badge, midroll, interstitial) — the description block is unconditional per `.claude/rules/youtube-metadata.md`.

### `description-dynamous-block-malformed`

Dynamous block present but format drift (missing emoji, wording change, wrong URL, missing `----` separator).

**Fix recipe:**
1. Locate the Dynamous block in `youtube-description.md` (grep for `dynamous.ai` or `🚀`).
2. Replace the entire block (including the `----` separators) with the canonical block from `description-dynamous-block-missing` above.
3. Re-run `video-metadata-publish`.

### `description-hostinger-sponsored-wording`

Hostinger banner reads as "Sponsored by Hostinger" instead of "Try Hostinger" / "Self-host on Hostinger".

**Fix recipe:**
1. `grep -nE "Sponsored by Hostinger|Hostinger sponsored" videos/<slug>/youtube-description.md`
2. Replace with the canonical Hostinger block from `.claude/rules/youtube-metadata.md`:
   ```
   ----
   ⚡ Host your portfolio, side projects, n8n flows, or AI agents on Hostinger (10% OFF):
   Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE
   ----
   ```
3. Re-run.

### `description-banned-section`

Description contains a removed section (`Key Concepts`, `Key Stats`, `Key Changes in This Release`, etc.).

**Fix recipe:**
1. Identify the section header line + every following line until the next blank line or section break.
2. Delete the entire block.
3. Re-run `video-metadata-publish` to confirm structure remains valid.

### `chapter-timestamp-speedup-mismatch`

Long-form `Chapters` section has timestamps not adjusted for the rendered MP4's speedup factor.

**Fix recipe:**
1. Look in `videos/<slug>/out/` for `<slug>-<N>x.mp4`. If found: `speed_factor = N`. Otherwise: `speed_factor = 1.0`.
2. Read every scene's `data-start` from `videos/<slug>/index.html`.
3. For each chapter: recompute `chapter_seconds = data_start / speed_factor`, format as `M:SS` (rounded to nearest second).
4. Rewrite the Chapters section in `youtube-description.md` with the recomputed timestamps. Keep the chapter titles.
5. First chapter MUST be `0:00`. If two consecutive chapters land < 10s apart after recompute, merge them.
6. Re-run `video-metadata-publish`.

### `cta-question-element-missing`

The final phase of `index.html` doesn't have an `#cta-question` (or analogous) element. On-screen CTA is missing.

**Fix recipe:**
1. Read `script.txt` final paragraph — extract the spoken question.
2. Find the LAST phase in `index.html` (highest `data-start`).
3. Insert a new child element inside that phase:
   ```html
   <div id="cta-question" class="clip"
        data-start="1.5" data-duration="<phase_remaining>" data-track-index="2"
        style="position:absolute;bottom:300px;left:60px;right:60px;font-size:56px;font-weight:700;color:var(--accent);text-align:center;line-height:1.2;">
     <SPOKEN QUESTION VERBATIM>
   </div>
   ```
4. The `<phase_remaining>` value is the final phase's `data-duration - 1.5`.
5. Re-run `video-script-content` to confirm visual CTA exists.

## Aggressive fixes (apply only with `--fix aggressive`)

These touch narration content — they can change meaning, and the user has confirmed they accept the risk.

### `heteronym-risk-live-adjective`

"live today" / "live on the platform" reads as /lɪv/ (verb) in TTS.

**Fix recipe:**
1. `script.txt`: replace `live today` → `available today`, `live on` → `shipping on`.
2. Per-scene `scripts/scene-*.txt`: same.
3. If the script is already through TTS, the narration is divergent — recommend a re-TTS via `python scripts/elevenlabs-tts.py` and warn user.
4. NEVER auto-replace `live` in verb contexts ("they live in NYC"). Use grep `\blive\s+(today|on|tomorrow|now|here)\b` to scope.

### `heteronym-risk-lead-noun`

"lead agent" / "lead developer" reads as /lɛd/ (metal) in TTS.

**Fix recipe:**
1. Replace `lead agent` → `primary agent`.
2. Replace `lead developer` → `senior developer`.
3. NEVER auto-replace `lead` in verb contexts ("they lead the team"). Use grep `\blead\s+(agent|developer|architect|engineer)\b` to scope.

### `tech-term-pronunciation`

TTS script uses unspelled tech term (`npm`, `nginx`, etc.).

**Fix recipe:**
1. ONLY edit TTS scripts (`script.txt`, `scripts/scene-*.txt`) — NEVER the raw script (`scripts/full-script.md`).
2. Apply the spelling table from `.claude/rules/tts-pronunciation.md`.
3. If narration.wav already exists, recommend re-TTS.

## NEVER auto-fix (always require user signoff)

These either can't be safely automated or always need a human decision:

- Pacing edits to GSAP tweens (cascades into chapter timestamps, SFX alignment, transcript anchors)
- Script body rewrites (changes meaning; re-TTS required)
- Image resizing (touches assets; user picks output dir)
- Backdrop-filter rework (visual style choice)
- URL replacement after WebFetch 404 (user picks the correct URL)
- Hook score < 6 (the `engagement-hooks-framework` skill is the right tool, not a recipe)
- Bar-chart marker overlay fix (user picks marker-circle vs pill-row vs scale-pulse)

When the orchestrator encounters one of these in `--fix safe` or `--fix aggressive` mode, it surfaces the finding as `status: SUGGEST` with the recipe filled in — the user reads the report and applies the fix manually.

## Re-run discipline

After applying any auto-fix, the orchestrator MUST re-run the agent that originally reported the finding to confirm the fix landed. If re-run still reports the finding, leave it as `status: AUTO_FIX_FAILED` and surface to user — do NOT silently mark it resolved.
