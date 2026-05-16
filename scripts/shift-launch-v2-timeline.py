"""One-shot: shift every tween/audio timestamp in hyperframes-launch-v2 by -2.8s
so narration starts at t=0.2 instead of t=3.0 (kills the silent intro).

Whitelist approach: only shifts timestamps that match clear tl.X(...) tween
patterns or audio data-start attributes. Conservative — better to miss one
and edit by hand than corrupt unrelated numerics."""

import re
import sys
from pathlib import Path

PATH = Path("videos/hyperframes-launch-v2/index.html")
SHIFT = -3.0

text = PATH.read_text(encoding="utf-8")
orig = text


def shift(t: float) -> float:
    new = t + SHIFT
    return max(0.0, round(new, 3))


# 1. Audio data-start values inside <audio ...> elements.
#    Match `<audio ... data-start="N.NN" ...>` (single-line audio tags).
def repl_audio(m):
    indent, prefix, t_str, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
    t = float(t_str)
    new = shift(t)
    return f"{indent}{prefix}data-start=\"{new}\"{suffix}"


audio_re = re.compile(
    r"(\n[ \t]*)(<audio\b[^>]*?\s)data-start=\"([\d.]+)\"([^>]*?>)",
    re.DOTALL,
)
text, audio_n = audio_re.subn(repl_audio, text)

# 2. Tween timestamps — last numeric argument of tl.to / tl.from / tl.set / tl.fromTo
#    The pattern is: `, NUMBER);` or `, NUMBER)\n` on the same line as a tl.X(
#    Match by scanning tween calls and grabbing the trailing position.
tween_n = 0


def shift_tween_line(line: str) -> str:
    global tween_n
    # Only operate on lines that invoke tl.<method>(
    if not re.search(r"\btl\.(to|from|set|fromTo|call)\(", line):
        return line
    # Find ending `, NUMBER);` or `, NUMBER)` (possibly with trailing whitespace/comments)
    m = re.search(r",\s*(\d+\.?\d*)\s*\)(\s*;?\s*(?://.*)?)$", line)
    if not m:
        return line
    t = float(m.group(1))
    new = shift(t)
    tween_n += 1
    return line[: m.start()] + f", {new})" + m.group(2)


text = "\n".join(shift_tween_line(l) for l in text.split("\n"))

# 3. Root composition data-duration (was 159.5, shorten by SHIFT)
def repl_root_duration(m):
    t = float(m.group(1))
    new = round(t + SHIFT, 3)
    return f"data-duration=\"{new}\""


# Only the root composition's data-duration is on the same line as id="root"
# We don't want to touch audio data-duration (those are clip lengths, not timeline positions).
root_re = re.compile(r"data-duration=\"(\d+\.?\d*)\"(?=[\s\n][^<]*<!--\s*reduced)?")
# Actually safer — explicit replacement of the root composition data-duration.
text = re.sub(
    r"(<div\s+id=\"root\"[^>]*?\bdata-duration=\")(\d+\.?\d*)(\"[^>]*?>)",
    lambda m: m.group(1) + str(round(float(m.group(2)) + SHIFT, 3)) + m.group(3),
    text,
    flags=re.DOTALL,
)

# 4. Progress-fill width tween references 159.5 explicitly — shift that constant too.
text = text.replace(
    "{ width: 1080, duration: 159.5, ease: 'none' },",
    "{ width: 1080, duration: 156.5, ease: 'none' },",
)
text = text.replace(
    "Math.floor(159.5 / 2.4)",
    "Math.floor(156.5 / 2.4)",
)

# 5. Confetti and any "static_duration" / fixed constants in JS — leave for manual review.

if text == orig:
    print("NO CHANGES.")
    sys.exit(1)

PATH.write_text(text, encoding="utf-8")
print(f"Shifted {audio_n} audio cues and {tween_n} tween timestamps by {SHIFT}s.")
