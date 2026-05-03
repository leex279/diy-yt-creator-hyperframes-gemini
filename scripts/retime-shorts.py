#!/usr/bin/env python3
"""Retime short compositions to transcript word-anchors.

For each of the 6 customization-feature shorts:
  1. Reads videos/<slug>/transcript.json (word-level timings from elevenlabs-tts).
  2. Locates the anchor word for each animated element (overlines, headline, 5
     cards, 5 matrix rows, hero slam, CTA, phase transitions).
  3. Computes new entrance times = anchor_word.start - lead_in (default 0.20s).
  4. Recomputes total duration, phase boundaries, endcard mount.
  5. Patches videos/<slug>/index.html in-place:
     - data-duration on #root
     - Adds <audio id="narration"> if missing
     - Updates SFX <audio> data-start values
     - Updates endcard mount data-start
     - Updates JS constants (TOTAL, T1, T2, T3, P2, P3, P4)
     - Updates per-tween entrance times in the GSAP block

Usage:
  python scripts/retime-shorts.py             # retime all 6
  python scripts/retime-shorts.py <slug>      # retime one
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEAD_IN = 0.20  # seconds before the anchor word that the entrance starts
PHASE_TRANSITION_GAP = 0.30  # gap between narration end and phase fade
TRANSITION_DURATION = 0.6  # phase transition full length (blur + crossfade)
ENDCARD_DURATION = 5.0
TAIL_BUFFER = 0.5

# --- Per-video anchor configs ---
# Each entry maps an element id to a list of words to search for in the transcript.
# The script picks the FIRST occurrence after `after` (in seconds), or the absolute
# first occurrence if `after` is omitted. The anchor's `start` time becomes the basis
# for the entrance time (which is anchor.start - LEAD_IN, with a floor of 0.0).
#
# Key patterns:
#   - overline / headline / pre / caption: text setup; anchor on a phase-defining word
#   - card_N / row_N: anchor on the word in narration that NAMES the card/row content
#   - hero: the punchline word that the hero slam should land on (peak of back-ease)
#   - p4_pill: anchor on the "subscribe"/CTA word

VIDEO_CONFIGS = {
    "claude-customization-5-features-short": {
        # Phase 1 - hook "MOST DEVS USE 1." with hero slam on "one"
        "p1_overline": {"words": ["Most"]},                       # appears with first word
        "p1_pre":      {"words": ["developers"]},
        "p1_hero":     {"words": ["one."], "lead": 0.55},         # slam peak hits ~0.6s after entrance start
        "p1_caption":  {"words": ["five"]},                       # shows when "five" is spoken
        # Phase 2 - 5 features named in order
        "p2_overline": {"words": ["Each"], "lead": 0.30},
        "p2_headline": {"words": ["Each"]},
        "p2_card_1":   {"words": ["First,"], "lead": 0.10},       # CLAUDE.md
        "p2_card_2":   {"words": ["Second,"], "lead": 0.10},      # Skills
        "p2_card_3":   {"words": ["Third,"], "lead": 0.10},       # Sub-agents
        "p2_card_4":   {"words": ["Fourth,"], "lead": 0.10},      # Hooks
        "p2_card_5":   {"words": ["fifth,"], "lead": 0.10},       # MCP Servers
        # Phase 3 - 5 questions / answers (P3 starts after "protocol." at 33.34)
        "p3_overline": {"words": ["Five"], "lead": 0.30, "after": 33},
        "p3_headline": {"words": ["Five"], "after": 33},
        "p3_row_1":    {"words": ["always"], "lead": 0.35},       # CLAUDE.md
        "p3_row_2":    {"words": ["sometimes?"], "lead": 0.55},
        "p3_row_3":    {"words": ["isolation?"], "lead": 0.65},
        "p3_row_4":    {"words": ["automatically"], "lead": 0.55},
        "p3_row_5":    {"words": ["external"], "lead": 0.50, "after": 50},  # skip P2 "External tool integrations"
        # Phase 4 - CTA
        "p4_overline": {"words": ["Watch"], "lead": 0.40},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10},
        "p4_pill":     {"words": ["breakdown"], "lead": 0.10},
    },
    "claudemd-vs-skills-short": {
        # P1: "Most developers put everything into CLAUDE dot M D. That's the wrong place."
        "p1_overline": {"words": ["Most"]},
        "p1_pre":      {"words": ["developers"]},
        "p1_hero":     {"words": ["wrong"], "lead": 0.55},        # slam on "wrong"
        "p1_caption":  {"words": ["everything"], "lead": 0.20},
        # P2: 5 differentiating facts
        "p2_overline": {"words": ["Here's"], "lead": 0.30},
        "p2_headline": {"words": ["Here's"]},
        "p2_card_1":   {"words": ["loads"], "lead": 0.30},        # CLAUDE.md "loads into every conversation"
        "p2_card_2":   {"words": ["demand."], "lead": 0.30},      # Skills "load on demand."
        "p2_card_3":   {"words": ["cost"], "lead": 0.30},         # "Context cost is high…" (single "cost" occurrence)
        "p2_card_4":   {"words": ["Trigger"], "lead": 0.30},
        "p2_card_5":   {"words": ["Best"], "lead": 0.30},
        # P3: 5 examples
        "p3_overline": {"words": ["Five"], "lead": 0.30},
        "p3_headline": {"words": ["Five"]},
        "p3_row_1":    {"words": ["TypeScript"], "lead": 0.30},
        "p3_row_2":    {"words": ["PR"], "lead": 0.30},
        "p3_row_3":    {"words": ["pnpm"], "lead": 0.30},
        "p3_row_4":    {"words": ["Deployment"], "lead": 0.30},
        "p3_row_5":    {"words": ["Never"], "lead": 0.30},
        # P4: CTA
        "p4_overline": {"words": ["Watch"], "lead": 0.40},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10},
        "p4_pill":     {"words": ["dive"], "lead": 0.10},
    },
    "claude-skills-autotrigger-short": {
        # P1: "You don't need a slash command. Claude Code Skills auto-trigger from your request."
        "p1_overline": {"words": ["You"]},
        "p1_pre":      {"words": ["don't"]},
        "p1_hero":     {"words": ["auto-trigger"], "lead": 0.55},
        "p1_caption":  {"words": ["request."], "lead": 0.20},
        # P2: 5 facts about Skills (P2 starts at "Here's how" ~5s)
        "p2_overline": {"words": ["A"], "lead": 0.30, "after": 5},
        "p2_headline": {"words": ["A"], "after": 5},
        "p2_card_1":   {"words": ["SKILL"], "lead": 0.30, "after": 6},          # SKILL.md mention
        "p2_card_2":   {"words": ["Auto-matching"], "lead": 0.30},
        "p2_card_3":   {"words": ["Slash"], "lead": 0.30, "after": 18},         # skip P1 "slash command"
        "p2_card_4":   {"words": ["Supporting"], "lead": 0.30},
        "p2_card_5":   {"words": ["Sharing"], "lead": 0.30},
        # P3: 5 trigger examples (starts at "Five real triggers" ~43s)
        "p3_overline": {"words": ["Five"], "lead": 0.30, "after": 42},
        "p3_headline": {"words": ["Five"], "after": 42},
        "p3_row_1":    {"words": ["review"], "lead": 0.30, "after": 42},
        "p3_row_2":    {"words": ["deploy"], "lead": 0.30, "after": 45},
        "p3_row_3":    {"words": ["commit"], "lead": 0.30, "after": 48},
        "p3_row_4":    {"words": ["add"], "lead": 0.30, "after": 51},
        "p3_row_5":    {"words": ["run"], "lead": 0.30, "after": 53},
        # P4
        "p4_overline": {"words": ["Watch"], "lead": 0.40, "after": 56},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10, "after": 56},
        "p4_pill":     {"words": ["breakdown"], "lead": 0.10, "after": 56},
    },
    "claude-subagents-explained-short": {
        # P1: "Claude just read fifty files for one question. Why is your context window dead?"
        "p1_overline": {"words": ["Claude"]},
        "p1_pre":      {"words": ["just"]},
        "p1_hero":     {"words": ["dead?"], "lead": 0.55},
        "p1_caption":  {"words": ["Sub-agents"], "lead": 0.20},
        # P2: 5 facts (built-in trio + custom + memory)
        "p2_overline": {"words": ["A"], "lead": 0.30, "after": 5},
        "p2_headline": {"words": ["A"], "after": 5},
        "p2_card_1":   {"words": ["Explore"], "lead": 0.30},
        "p2_card_2":   {"words": ["Plan"], "lead": 0.30},
        "p2_card_3":   {"words": ["General-purpose"], "lead": 0.30},
        "p2_card_4":   {"words": ["Custom"], "lead": 0.30},
        "p2_card_5":   {"words": ["Persistent"], "lead": 0.30},
        # P3: 5 routing decisions
        "p3_overline": {"words": ["Five"], "lead": 0.30},
        "p3_headline": {"words": ["Five"]},
        "p3_row_1":    {"words": ["Explore"], "lead": 0.30, "after": 40},
        "p3_row_2":    {"words": ["Read-only"], "lead": 0.30, "after": 40},
        "p3_row_3":    {"words": ["Long"], "lead": 0.30},
        "p3_row_4":    {"words": ["Cost-sensitive"], "lead": 0.30},
        "p3_row_5":    {"words": ["Validate"], "lead": 0.30},
        "p4_overline": {"words": ["Watch"], "lead": 0.40},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10},
        "p4_pill":     {"words": ["breakdown"], "lead": 0.10},
    },
    "claude-hooks-explained-short": {
        # P1: "Skills are request-driven. Hooks are event-driven. The difference is everything."
        "p1_overline": {"words": ["Skills"]},
        "p1_pre":      {"words": ["are"]},
        "p1_hero":     {"words": ["event-driven."], "lead": 0.55},
        "p1_caption":  {"words": ["everything."], "lead": 0.20},
        # P2: 5 facts about hooks (P2 starts at "A hook fires" ~5s)
        "p2_overline": {"words": ["A"], "lead": 0.30, "after": 4},
        "p2_headline": {"words": ["A"], "after": 4},
        "p2_card_1":   {"words": ["thirty"], "lead": 0.30},                  # 30+ event types
        "p2_card_2":   {"words": ["PreToolUse"], "lead": 0.30, "after": 11}, # first PreToolUse in P2
        "p2_card_3":   {"words": ["PostToolUse"], "lead": 0.30, "after": 16},
        "p2_card_4":   {"words": ["SessionStart"], "lead": 0.30, "after": 23},
        "p2_card_5":   {"words": ["Prompt"], "lead": 0.30, "after": 32},
        # P3: 5 hook recipes (P3 starts at "Five hook recipes" ~40s)
        "p3_overline": {"words": ["Five"], "lead": 0.30, "after": 40},
        "p3_headline": {"words": ["Five"], "after": 40},
        "p3_row_1":    {"words": ["Block"], "lead": 0.30, "after": 40},      # skip P2 "Block destructive commands"
        "p3_row_2":    {"words": ["Auto-format"], "lead": 0.30, "after": 44},
        "p3_row_3":    {"words": ["Inject"], "lead": 0.30, "after": 48},     # skip P2 "Inject environment state"
        "p3_row_4":    {"words": ["Validate"], "lead": 0.30, "after": 52},
        "p3_row_5":    {"words": ["Refuse"], "lead": 0.30, "after": 56},
        "p4_overline": {"words": ["Watch"], "lead": 0.40, "after": 59},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10, "after": 59},
        "p4_pill":     {"words": ["dive"], "lead": 0.10, "after": 59},
    },
    "claude-mcp-vs-skills-short": {
        # P1: "Half the community swapped MCP for Skills. Here's when to pick each."
        "p1_overline": {"words": ["Half"]},
        "p1_pre":      {"words": ["the"]},
        "p1_hero":     {"words": ["pick"], "lead": 0.55},                    # slam on "pick" at 3.90
        "p1_caption":  {"words": ["each."], "lead": 0.20},
        # P2: 5 facts about MCP (P2 starts at "MCP is the Model Context Protocol" ~4.66)
        "p2_overline": {"words": ["MCP"], "lead": 0.30, "after": 4},         # second MCP mention (4.66)
        "p2_headline": {"words": ["MCP"], "after": 4},
        "p2_card_1":   {"words": ["Model"], "lead": 0.30, "after": 4},       # "Model Context Protocol" → MCP fact
        "p2_card_2":   {"words": ["Hundreds"], "lead": 0.30},                # "Hundreds of servers"
        "p2_card_3":   {"words": ["Installation"], "lead": 0.30},
        "p2_card_4":   {"words": ["transports"], "lead": 0.30},
        "p2_card_5":   {"words": ["Context"], "lead": 0.30, "after": 30},    # skip P2 "Model Context Protocol"
        # P3: 5 decision examples (starts at "Five decision examples" ~39.7s)
        "p3_overline": {"words": ["Five"], "lead": 0.30, "after": 39},
        "p3_headline": {"words": ["Five"], "after": 39},
        "p3_row_1":    {"words": ["External"], "lead": 0.30, "after": 39},
        "p3_row_2":    {"words": ["Custom"], "lead": 0.30, "after": 43},
        "p3_row_3":    {"words": ["Database"], "lead": 0.30},
        "p3_row_4":    {"words": ["Coding"], "lead": 0.30},
        "p3_row_5":    {"words": ["Third-party"], "lead": 0.30},
        # P4 — narration ends at "system." 63.82, so Watch is ~60s
        "p4_overline": {"words": ["Watch"], "lead": 0.40, "after": 59},
        "p4_pre":      {"words": ["Watch"], "lead": 0.10, "after": 59},
        "p4_pill":     {"words": ["dive"], "lead": 0.10, "after": 59},
    },
}


def find_word(transcript: list[dict], words: list[str], after: float = 0.0) -> dict | None:
    """Find the first transcript entry whose word matches any of `words` (case-insensitive,
    trailing punctuation tolerant) and whose `start` >= after."""
    targets = [w.lower().rstrip('.,?!:;"\'') for w in words]
    for entry in transcript:
        if entry["start"] < after:
            continue
        clean = entry["word"].lower().rstrip('.,?!:;"\'')
        if clean in targets or entry["word"].lower() in [w.lower() for w in words]:
            return entry
    return None


def compute_timings(slug: str, transcript: list[dict]) -> dict:
    """Compute all timing values for a single short."""
    config = VIDEO_CONFIGS[slug]
    narration_end = max(e["end"] for e in transcript)
    timings: dict = {}

    for elem_id, spec in config.items():
        anchor = find_word(transcript, spec["words"], spec.get("after", 0.0))
        if anchor is None:
            print(f"  WARN: {slug}: no anchor found for {elem_id} (words={spec['words']})", file=sys.stderr)
            timings[elem_id] = None
            continue
        lead = spec.get("lead", LEAD_IN)
        entrance = max(0.0, anchor["start"] - lead)
        timings[elem_id] = round(entrance, 2)

    # Phase boundaries derived from timings
    # T1 = phase 1 → 2 transition start (= just before p2_overline reveal)
    # We start the transition early so it completes by the time the overline shows.
    # P2 = T1 + transition (overline anchor moment)
    p2_anchor = timings["p2_overline"]
    timings["T1"] = round(max(0.0, p2_anchor - TRANSITION_DURATION), 2)
    timings["P2"] = round(p2_anchor, 2)

    p3_anchor = timings["p3_overline"]
    timings["T2"] = round(max(timings["P2"], p3_anchor - TRANSITION_DURATION), 2)
    timings["P3"] = round(p3_anchor, 2)

    p4_anchor = timings["p4_overline"]
    timings["T3"] = round(max(timings["P3"], p4_anchor - TRANSITION_DURATION), 2)
    timings["P4"] = round(p4_anchor, 2)

    # Total duration = narration end + tail buffer + endcard
    total = narration_end + TAIL_BUFFER + ENDCARD_DURATION
    timings["TOTAL"] = round(total, 2)
    timings["ENDCARD_START"] = round(total - ENDCARD_DURATION, 2)
    timings["FADE_OUT"] = round(total - ENDCARD_DURATION - 0.5, 2)
    timings["NARRATION_END"] = round(narration_end, 2)

    # --- Ordering sanity checks ---
    ordered_cards = [
        ("p2_card_1", "p2_card_2", "p2_card_3", "p2_card_4", "p2_card_5"),
        ("p3_row_1", "p3_row_2", "p3_row_3", "p3_row_4", "p3_row_5"),
    ]
    for group in ordered_cards:
        prev_t = -1.0
        for key in group:
            t = timings.get(key)
            if t is None:
                continue
            if t < prev_t:
                print(
                    f"  WARN: {slug}: {key}={t} is BEFORE previous group element ({prev_t}) — "
                    f"anchor probably matched in the wrong phase",
                    file=sys.stderr,
                )
            prev_t = t

    # Phase ordering: p1_hero < P2 < P3 < P4 < TOTAL
    phase_order = [
        ("p1_hero", timings.get("p1_hero")),
        ("P2", timings["P2"]),
        ("P3", timings["P3"]),
        ("P4", timings["P4"]),
        ("ENDCARD_START", timings["ENDCARD_START"]),
        ("TOTAL", timings["TOTAL"]),
    ]
    prev_t = -1.0
    for name, t in phase_order:
        if t is None:
            continue
        if t < prev_t:
            print(
                f"  WARN: {slug}: phase boundary {name}={t} is BEFORE previous ({prev_t}) — "
                f"check anchor configs",
                file=sys.stderr,
            )
        prev_t = t

    return timings


def render_index_html(slug: str, timings: dict, base_html: str) -> str:
    """Apply timing replacements to the existing index.html content."""
    html = base_html

    # 1. data-duration on #root
    html = re.sub(
        r'(<div id="root"[^>]*data-duration=")[\d.]+(")',
        rf'\g<1>{timings["TOTAL"]}\g<2>',
        html,
    )

    # 2. Insert <audio id="narration"> right before the SFX block (before "Phase 1 hero slam")
    if 'id="narration"' not in html:
        narration_block = f"""
  <!-- Narration — single ElevenLabs track on track 2 -->
  <audio id="narration" class="clip" src="audio/narration.wav"
         data-start="0" data-duration="{timings['NARRATION_END']}" data-track-index="2" data-volume="1"></audio>
"""
        # Insert just before the "Phase 1 hero slam" comment
        html = html.replace(
            "  <!-- Phase 1 hero slam — layered impact + screen-shake at t≈1.7s -->",
            narration_block + "  <!-- Phase 1 hero slam — layered impact + screen-shake at t≈1.7s -->",
        )
    else:
        # Update narration data-duration if already present
        html = re.sub(
            r'(<audio id="narration"[^>]*data-duration=")[\d.]+(")',
            rf'\g<1>{timings["NARRATION_END"]}\g<2>',
            html,
        )

    # 3. Endcard mount data-start
    html = re.sub(
        r'(<div id="dynamous-endcard-mount"[\s\S]*?data-start=")[\d.]+(")',
        rf'\g<1>{timings["ENDCARD_START"]}\g<2>',
        html,
    )

    # 4. SFX data-start values
    sfx_map = {
        "sfx-impact":   timings["p1_hero"],
        "sfx-shake":    timings["p1_hero"],
        "sfx-whoosh-1": timings["T1"],
        "sfx-whoosh-2": timings["T2"],
        "sfx-whoosh-3": timings["T3"],
        "sfx-card-1":   timings["p2_card_1"],
        "sfx-card-2":   timings["p2_card_2"],
        "sfx-card-3":   timings["p2_card_3"],
        "sfx-card-4":   timings["p2_card_4"],
        "sfx-card-5":   timings["p2_card_5"],
        "sfx-row-1":    timings["p3_row_1"],
        "sfx-row-2":    timings["p3_row_2"],
        "sfx-row-3":    timings["p3_row_3"],
        "sfx-row-4":    timings["p3_row_4"],
        "sfx-row-5":    timings["p3_row_5"],
        "sfx-cta-pill": timings["p4_pill"],
    }
    for sfx_id, t in sfx_map.items():
        if t is None:
            continue
        html = re.sub(
            rf'(<audio id="{sfx_id}"[^>]*data-start=")[\d.]+(")',
            rf'\g<1>{t}\g<2>',
            html,
        )

    # 4b. Move sfx-impact to track 5 (out of track 3) to avoid overlap with whoosh-1
    # when phase 1 → 2 transition fires close to the hero slam (tight narration pacing).
    # Audio-design rules: layered cues at the same moment need separate tracks.
    html = re.sub(
        r'(<audio id="sfx-impact"[^>]*data-track-index=")[\d]+(")',
        r'\g<1>5\g<2>',
        html,
    )

    # 4c. Shorten cinematic-whoosh data-duration from 0.8s → 0.6s to avoid overlap
    # with the next sequential SFX (card-1 / cta-pill) when narration pacing is tight.
    # 0.6s still reads as a clear cinematic transition swoosh.
    html = re.sub(
        r'(src="assets/sfx/cinematic-whoosh\.mp3"\s*data-start="[\d.]+" data-duration=")[\d.]+(")',
        r'\g<1>0.6\g<2>',
        html,
    )

    # 5. JS constants
    js_replacements = [
        (r'const TOTAL = [\d.]+;', f'const TOTAL = {timings["TOTAL"]};'),
        (r'const T1 = [\d.]+;',    f'const T1 = {timings["T1"]};'),
        (r'const T2 = [\d.]+;',    f'const T2 = {timings["T2"]};'),
        (r'const T3 = [\d.]+;',    f'const T3 = {timings["T3"]};'),
        (r'const P2 = [\d.]+;',    f'const P2 = {timings["P2"]};'),
        (r'const P3 = [\d.]+;',    f'const P3 = {timings["P3"]};'),
        (r'const P4 = [\d.]+;',    f'const P4 = {timings["P4"]};'),
    ]
    for pattern, replacement in js_replacements:
        html = re.sub(pattern, replacement, html)

    # 6. Phase 1 entrance times (absolute, not P-relative)
    # The current pattern: tl.from("#p1-overline", { ... }, 0.4);
    # Replace the trailing time argument for each p1 element.
    p1_map = {
        "#p1-overline": timings["p1_overline"],
        "#p1-pre":      timings["p1_pre"],
        "#p1-hero":     timings["p1_hero"],
        "#p1-caption":  timings["p1_caption"],
    }
    for sel, t in p1_map.items():
        if t is None:
            continue
        # Match `tl.from("#p1-X", { ... }, NNN);` — N may be float
        pattern = rf'(tl\.from\("{re.escape(sel)}",\s*\{{[^}}]+\}},\s*)[\d.]+(\s*\);)'
        html = re.sub(pattern, rf'\g<1>{t}\g<2>', html)

    # Hero shake offsets — 4 mini-tweens at hero+0.25, +0.30, +0.35, +0.40
    # Pattern: tl.to("#p1-hero", { x: 5,  duration: ..., ... }, 1.95);
    # Replace each absolute time. Recompute relative to new hero entrance.
    hero_t = timings["p1_hero"]
    if hero_t is not None:
        shake_offsets = [(5, 0.25), (-5, 0.30), (4, 0.35), (0, 0.40)]
        for x_val, off in shake_offsets:
            pattern = rf'(tl\.to\("#p1-hero",\s*\{{\s*x:\s*{x_val},\s*[^}}]+\}},\s*)[\d.]+(\s*\);)'
            html = re.sub(pattern, rf'\g<1>{round(hero_t + off, 2)}\g<2>', html)

    # 7. Phase 2 / 3 / 4 entrance offsets (relative to P2 / P3 / P4 base)
    # Convert absolute timings to offsets relative to phase base.
    def offset(elem_t: float | None, phase_base: float) -> str:
        if elem_t is None:
            return "0.0"
        return str(round(elem_t - phase_base, 2))

    p2_base = timings["P2"]
    p3_base = timings["P3"]
    p4_base = timings["P4"]

    phase_map = [
        # (selector, absolute time, phase const name, phase base value)
        ("#p2-overline", timings.get("p2_overline"), "P2", p2_base),
        ("#p2-headline", timings.get("p2_headline"), "P2", p2_base),
        ("#p2-card-1",   timings.get("p2_card_1"),   "P2", p2_base),
        ("#p2-card-2",   timings.get("p2_card_2"),   "P2", p2_base),
        ("#p2-card-3",   timings.get("p2_card_3"),   "P2", p2_base),
        ("#p2-card-4",   timings.get("p2_card_4"),   "P2", p2_base),
        ("#p2-card-5",   timings.get("p2_card_5"),   "P2", p2_base),
        ("#p3-overline", timings.get("p3_overline"), "P3", p3_base),
        ("#p3-headline", timings.get("p3_headline"), "P3", p3_base),
        ("#p3-row-1",    timings.get("p3_row_1"),    "P3", p3_base),
        ("#p3-row-2",    timings.get("p3_row_2"),    "P3", p3_base),
        ("#p3-row-3",    timings.get("p3_row_3"),    "P3", p3_base),
        ("#p3-row-4",    timings.get("p3_row_4"),    "P3", p3_base),
        ("#p3-row-5",    timings.get("p3_row_5"),    "P3", p3_base),
        ("#p4-overline", timings.get("p4_overline"), "P4", p4_base),
        ("#p4-pre",      timings.get("p4_pre"),      "P4", p4_base),
        ("#p4-pill",     timings.get("p4_pill"),     "P4", p4_base),
    ]
    for sel, abs_t, phase_const, phase_base in phase_map:
        if abs_t is None:
            continue
        off = offset(abs_t, phase_base)
        # Match `tl.to("#sel", { ... }, P2 + X.X);` — replace the offset
        pattern = rf'(tl\.to\("{re.escape(sel)}",\s*\{{[^}}]+\}},\s*{phase_const}\s*\+\s*)[\d.]+(\s*\);)'
        html = re.sub(pattern, rf'\g<1>{off}\g<2>', html)

    return html


def main() -> int:
    target_slugs = sys.argv[1:] if len(sys.argv) > 1 else list(VIDEO_CONFIGS.keys())
    failed = []

    for slug in target_slugs:
        if slug not in VIDEO_CONFIGS:
            print(f"unknown slug: {slug}", file=sys.stderr)
            failed.append(slug)
            continue
        video_dir = REPO_ROOT / "videos" / slug
        transcript_path = video_dir / "transcript.json"
        index_path = video_dir / "index.html"

        if not transcript_path.exists():
            print(f"  ERROR: {slug}: missing transcript.json", file=sys.stderr)
            failed.append(slug)
            continue
        if not index_path.exists():
            print(f"  ERROR: {slug}: missing index.html", file=sys.stderr)
            failed.append(slug)
            continue

        transcript = json.loads(transcript_path.read_text(encoding="utf-8"))
        timings = compute_timings(slug, transcript)
        base_html = index_path.read_text(encoding="utf-8")
        new_html = render_index_html(slug, timings, base_html)
        index_path.write_text(new_html, encoding="utf-8")

        print(f"=== {slug} ===")
        print(f"  narration: {timings['NARRATION_END']}s, TOTAL: {timings['TOTAL']}s")
        print(f"  T1={timings['T1']} T2={timings['T2']} T3={timings['T3']}")
        print(f"  P2={timings['P2']} P3={timings['P3']} P4={timings['P4']}")
        print(f"  hero slam at {timings['p1_hero']}, endcard at {timings['ENDCARD_START']}")
        print(f"  cards: {timings['p2_card_1']}, {timings['p2_card_2']}, {timings['p2_card_3']}, {timings['p2_card_4']}, {timings['p2_card_5']}")
        print(f"  rows:  {timings['p3_row_1']}, {timings['p3_row_2']}, {timings['p3_row_3']}, {timings['p3_row_4']}, {timings['p3_row_5']}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
