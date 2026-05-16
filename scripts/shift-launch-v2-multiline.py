"""Follow-up pass: shift multi-line tween end-lines that the line-based
shift script missed. Pattern: ENDING with `}, N.NN);` on its own line."""

import re
from pathlib import Path

PATH = Path("videos/hyperframes-launch-v2/index.html")
SHIFT = -3.0

text = PATH.read_text(encoding="utf-8")
orig = text

# Match lines that LOOK like the closing of a multi-line tween:
#   `<indent>{ ... }, NUMBER);`
# We only want to shift the trailing time after `},`.
pat = re.compile(
    r"(^[ \t]+\{[^{}\n]*\}),\s*(\d+\.?\d*)\)\s*;\s*$",
    re.MULTILINE,
)


def repl(m):
    obj, t_str = m.group(1), m.group(2)
    t = float(t_str)
    new = max(0.0, round(t + SHIFT, 3))
    return f"{obj}, {new});"


text, n = pat.subn(repl, text)

if text == orig:
    print("NO CHANGES.")
else:
    PATH.write_text(text, encoding="utf-8")
    print(f"Shifted {n} multi-line tween timestamps by {SHIFT}s.")
