# DESIGN — Long-Form Screencap-Dubbed (Recording + AI-Voice Dub)

Visual system for **horizontal long-form videos** (1920x1080, 30fps, typically 1-15 minutes) where the bulk of the screen is a **real screen recording** dubbed with an **AI voice** generated from the user's own transcribed narration. Forked from [`templates/long-form/standard`](../standard/) — reuses its palette, type, and motion. Only diffs are documented here.

## What's different from `standard`

| Dimension | `standard` | `screencap-dubbed` |
|---|---|---|
| Scene count | 8 archetypes + captions | **3 scenes**: `title`, `screencap` (full-bleed video), `cta` |
| Persistent chrome | Centered top-banner + bottom progress | **Corner watermark** (top-right, 44px) + bottom progress |
| Captions | Recommended (`captions.html` wired by default) | **None** — tutorial pacing reads fine without burned-in captions |
| Bulk content | Custom GSAP scenes | **Full-bleed `<video>` clip** (muted) on a dedicated z-index 2 wrapper |
| Audio bed | Narration + 3-segment bg-music | **Narration only** — UI clicks in the recording would muddy bg-music |
| Voice | Stock TTS from a freshly-written script | **TTS dub of the user's own spoken transcript** — preserves natural pacing |

## Style Prompt

A dark navy bookend around a real screen recording. The opener (title, ~4-5s) and closer (CTA, ~10s) carry the brand chrome and the debate question. The middle is the operator's actual screen capture, full-bleed, with the original voice replaced by a polished AI dub. A 44px corner watermark stays visible across all three scenes so screenshots and pause-frames trace back to the channel. Motion: identical to `standard` (back.out on chrome, expo.out on hero text, sine.inOut on ambient). The recording itself carries no synthetic motion — what the operator did on screen IS the motion.

## Canvas

- Resolution: **1920 x 1080**
- Frame rate: **30fps** (the screen recording itself can be 30 or 60fps — the renderer normalizes)
- Duration target: **1-15 minutes** depending on the recording length
- Background: same `#0B0F1A` near-black navy as `standard`. Behind the screencap it's invisible; during title + CTA it provides the dark stage.

## Colors

Same palette as `standard` — see [`../standard/DESIGN.md`](../standard/DESIGN.md). Per-video, swap accents per the standard playbook.

## Typography

Same type scale as `standard`. The screencap scene has no body text by default (the recording IS the content); optional **step-callout pills** use mono 28px / weight 700 to match the rest of the system.

## Layout

Three scenes, fixed slots:

```
0       4.5s                                            105s     115s
+-------+------------------------------------------------+--------+
  title              screencap (full-bleed video)             cta
  (track 1)          (track 2 — paints over chrome)        (track 1)
```

The screencap scene is the only one on track 2 — it covers ambient + shape backdrop. Title and CTA stay on track 1 so the chrome shows through.

**Safe zones for screencap content:** the corner watermark (top-right, 44px tall, 36px from top + 48px from right) and the 6px progress bar will sit over the recording. App UI that lives in the top-right corner of the recording (e.g. account avatar, notification bell) will collide with the watermark. If the recording's top-right matters, either crop the recording or move the watermark to top-left (then the app's left-side menu is at risk instead). Always preview before render.

**Step-callout pills** (optional) are anchored bottom-left, max 720px wide. Use them sparingly — every callout fights for attention against the real screen recording. Default to <= 1 callout per ~15s of screencap.

## Motion Language

Same easings and durations as `standard`. The screencap scene itself has no entrance animations on the `<video>` element — the recording starts playing the moment the scene fades in (handled by the root crossfade). Per-video, operator MAY add `tl.from()` reveals on step-callout pills anchored to TTS word timestamps from `transcript.json` — same pattern as Shorts narration sync.

## Surface Detail

- **Corner watermark:** 44px logo height, 0.88 opacity, `drop-shadow(0 4px 12px rgba(0,0,0,0.55))`. Top-right because app UI usually lives top-left.
- **Step-callout pill:** 14px radius, `rgba(15,23,42,0.78)` fill + `backdrop-filter: blur(8px)`, accent number chip on the left at 6px radius. Single blur layer (well within the <=2-3 backdrop-filter cap from [`hyperframes-pitfalls.md`](../../../.claude/rules/hyperframes-pitfalls.md)).
- **Full-bleed video frame:** no chrome around the recording. `object-fit: contain` so aspect-mismatched recordings letterbox into pure black rather than crop. If your recording is 1920x1080 native, you'll never see the letterbox.

## Audio Bed (Screencap-Specific)

| Track | Role | data-volume |
|---|---|---|
| `2` | **Narration** — the AI-voice dub of the user's transcribed words | `1.0` |
| `3` | Optional cinematic-whoosh on title->screencap and screencap->cta transitions | `0.11` |

**No bg-music by default.** Screen recordings often include ambient UI sounds (clicks, page transitions, system notifications captured by the screen recorder). A music bed under those reads as cluttered. If a specific video genuinely needs music, mirror the standard template's 3-segment block — but verify the recording is truly silent (or mute-extract its audio first) before adding it.

**The recording's original audio MUST be muted** — the `<video>` element gets `muted` and the AI-voice plays separately on track 2. Without `muted`: (a) browsers block autoplay, (b) the two audio tracks overlap.

## What NOT to Do

Same don'ts as `standard` (no light canvas, no `repeat: -1`, no `tl.from()` at position > 5 without `immediateRender: false`, no `class="clip"` on `<audio>` / `<video>`, etc.). Screencap-dubbed-specific additions:

1. **Never restructure the script after transcription.** The whole sync premise rests on the AI voice having ~the same pacing as the original recording. Strip filler words, fix flubs, apply heteronym audit per [`.claude/rules/tts-pronunciation.md`](../../../.claude/rules/tts-pronunciation.md) — but never add new sentences, reorder paragraphs, or rewrite for "flow." If the script needs significant edits, re-record instead.
2. **Never leave the `<video>` element un-`muted`.** Both audio tracks will play and the dub becomes useless.
3. **Never set `class="clip"` on the `<video>` element.** The scene wrapper in `index.html` owns timing; the video element is a plain media tag.
4. **Never put a live media tag inside an HTML comment.** The linter parses comments for media references and reports `duplicate_media_discovery_risk`. Use prose ("operator wires the video element") instead.
5. **Never auto-trim or auto-stretch the recording to match the dub.** If the dub is significantly shorter or longer than the recording, fix the script first (most common cause: too much filler stripped, or new content added). If sync still drifts after a clean dub, use the segment-warp escape hatch documented in the playbook — not blanket `setpts`.
6. **Never render with placeholder media.** The bare template's `<div id="screencap-placeholder">` is for spawn-time-only — the operator MUST replace it with the real video element snippet before render.
