# 5 Claude Skills Eating GitHub — overnight build notes

**Topic picked**: 2026-05-10 via vidIQ MCP. The "claude code skills" keyword has
484k monthly searches at competition 39.4 / overall 75.16 — strongest keyword in
the niche right now. Listicle shorts on this topic are breaking out (Sean No Code
"Claude skills are a super power" at 18.99 breakout, multiple others).

**Title**: "These 5 Claude Skills Are Eating GitHub" — vidIQ title score 89.

**Render**: `out/5-claude-skills-viral-short.mp4` · 1080×1920 · 30fps ·
**2:14 duration** · 26.2 MB · 4020 frames. Verified with ffprobe; the studio's
"1m 34.0s" display is a string-format quirk — the actual MP4 is 134.021s.

## Pipeline deviations from the standard flow

- **ElevenLabs quota exhausted (24 credits, needed 65+).** Could not generate
  ElevenLabs narration. Fell back to **edge-tts** (free Microsoft cloud TTS) via
  the new `scripts/edge-tts-fallback.py`. Voice = `en-US-AndrewNeural` (warm,
  confident, tech-narration grade). Rate = `+10%` to mimic the channel's usual
  `ELEVENLABS_SPEED_SHORTS=1.13` cadence. Audio quality is broadcast-grade but
  not the channel's usual ElevenLabs voice — if you want to re-cut with the
  proper voice after topping up the ElevenLabs balance, just re-run
  `python scripts/elevenlabs-tts.py videos/5-claude-skills-viral-short --shorts --force`
  and re-transcribe to refresh `transcript.json`.
- **Whisper transcription used directly** (not the bundled whisper.cpp). The
  hyperframes `transcribe` command expects whisper.cpp's CLI shape; we used
  OpenAI Whisper Python (`small.en`, word_timestamps=True) and converted to the
  hyperframes transcript.json format. Same word-level granularity, identical
  format.

## Phase timing (anchored to whisper word boundaries)

| Phase | Start | End | Content |
|---|---|---|---|
| P1 hook | 0.0s | 6.5s | "EATING GITHUB" hero slam |
| P2 receipts | 6.5s | 26.5s | 360K / 132K / 15.5K stat pills |
| P3 Frontend Design | 26.5s | 47.5s | 110K weekly installs |
| P4 Superpowers | 47.5s | 65.2s | 40K stars / 3.1K forks |
| P5 Remotion | 65.2s | 82.5s | 117K weekly installs |
| P6 Vercel WDG | 82.5s | 100.2s | 133K weekly installs |
| P7 Skill Creator | 100.2s | 116.3s | META — Anthropic ships free |
| P8 outro + thumb | 116.3s | 134s | Stripe + Wiz receipts, "SKILLS EAT SDKs" |

## Validation receipts

- `npx hyperframes lint` → 0 errors · 1 warning (composition_file_too_large, cosmetic)
- `npx hyperframes inspect` → 0 layout issues across 9 samples
- `npx hyperframes validate` → 0 errors · 3 contrast warnings (all on faded-out
  phase 8 receipt lines at t=40s/67s/93.8s — false positives during opacity=0
  windows)
- 8 phase screenshots in `qa-screenshots/` — every phase visually verified
- Rendered final frame at t=132.5s saved to `qa-screenshots/rendered-final-frame.png`
  — passes all 5 shorts-thumbnail-frames.md requirements

## Things you might want to retouch in the morning

1. **The "ANTHROPIC" top banner**. The video uses the existing Anthropic
   wordmark from the template. Skill ecosystem video → makes sense; if you'd
   rather brand this with your own channel mark, swap
   `assets/anthropic-logo-light.svg`.
2. **Re-render with the real ElevenLabs voice** once the quota is topped up
   (see deviation #1 above). The visual composition does not need to change —
   only the audio + transcript.json + GSAP scene anchor timestamps would
   re-derive.
3. **YouTube description** — drafted in `youtube-description.md`. Worth a
   45-second skim before upload to make sure the chapter math still lines up
   (it's pre-speedup at 1.0×, so if you ffmpeg-speed it before upload, divide
   chapter timestamps).
