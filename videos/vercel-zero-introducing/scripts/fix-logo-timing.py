"""Fix logo (filter + remove redundant text + 2x size), top-align phase content,
and retime ALL phase boundaries to actual narration word anchors from transcript.json."""
import re
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PATH = 'videos/vercel-zero-introducing/index.html'

with open(PATH, encoding='utf-8') as f:
    s = f.read()

# ─── 1) FIX LOGO: white pixels already, drop invert filter + remove duplicate text + 2x size ──
# Top banner: drop the <span class="wm-text">VERCEL</span>, double height 34→68
s = s.replace(
    '<div id="top-banner-wordmark"><img src="assets/vercel-logo.png" alt="Vercel" style="height:34px; vertical-align:middle; margin-right:14px; filter:invert(1) brightness(2);"><span class="wm-text" style="letter-spacing:4px;">VERCEL</span><span class="wm-sub">LABS</span></div>',
    '<div id="top-banner-wordmark"><img src="assets/vercel-logo.png" alt="Vercel" style="height:68px; vertical-align:middle; margin-right:18px;"><span class="wm-sub">LABS</span></div>'
)
print('  top-banner: logo 2x, text removed, filter removed')

# P1 brand-wordmark: 48px → 96px, drop filter
s = s.replace(
    '<div id="p1-brand-wordmark"><img src="assets/vercel-logo.png" alt="Vercel" style="height:48px; vertical-align:middle; filter:invert(1) brightness(2);"></div>',
    '<div id="p1-brand-wordmark"><img src="assets/vercel-logo.png" alt="Vercel" style="height:96px; vertical-align:middle;"></div>'
)
print('  p1-brand-wordmark: logo 2x, filter removed')

# P15 CTA footer: 28px → 56px, drop filter
s = s.replace(
    '<img src="assets/vercel-logo.png" alt="Vercel" style="height:28px; filter:invert(1) brightness(2);">',
    '<img src="assets/vercel-logo.png" alt="Vercel" style="height:56px;">'
)
print('  p15 CTA footer: logo 2x, filter removed')

# ─── 2) TOP-ALIGN PHASE CONTENT ──
# The simple_phase() output uses:
#   align-items:center; justify-content:center; gap:32px; padding-top:300px
# Change to flex-start vertical, reduce padding-top to 240px (just past the logo + LABS label)
s = re.sub(
    r'align-items:center; justify-content:center; gap:(\d+)px; padding-top:300px;',
    r'align-items:center; justify-content:flex-start; gap:\1px; padding-top:240px;',
    s
)
s = re.sub(
    r'align-items:center; justify-content:center; gap:(\d+)px; padding-top:280px;',
    r'align-items:center; justify-content:flex-start; gap:\1px; padding-top:240px;',
    s
)
print('  phase-content: top-aligned (justify-content:flex-start, padding-top:240px)')

# ─── 3) RETIME PHASE BOUNDARIES TO NARRATION WORD ANCHORS ──
# Old (1.49x scaling): T1=8.0, T2=15.5, ..., T14=110.5
# New (narration-aligned):
new_T = [7.3, 14.0, 25.5, 31.5, 40.0, 47.5, 54.5, 60.0, 71.0, 78.0, 87.5, 95.0, 104.5, 109.5]
# P-anchors = T + 0.5
new_P = [t + 0.5 for t in new_T]  # P2..P15

# Current values (from previous run): T1=8.0, T2=15.5, ..., T14=110.5
cur_T = [8.0, 15.5, 23.5, 31.5, 39.5, 47.5, 55.5, 63.5, 71.5, 79.5, 87.5, 95.5, 103.0, 110.5]
cur_P = [t + 0.5 for t in cur_T]  # current P-anchors

# Build all `const Tn = X;` replacements (both single-space and double-space forms)
n_repls = 0
for i, (cur, new) in enumerate(zip(cur_T, new_T), start=1):
    for sp in (' ', '  '):  # T1..T5 use single space; T6..T14 use double (per source)
        old_str = f'const T{i}{sp}= {cur};'
        new_str = f'const T{i}{sp}= {new};'
        cnt = s.count(old_str)
        if cnt:
            s = s.replace(old_str, new_str)
            n_repls += cnt

for i, (cur, new) in enumerate(zip(cur_P, new_P), start=2):
    old_str = f'const P{i} = {cur};'
    new_str = f'const P{i} = {new};'
    cnt = s.count(old_str)
    if cnt:
        s = s.replace(old_str, new_str)
        n_repls += cnt

# DUR + audio data-duration + TOTAL_DURATION extender + narration duration
# Current DUR=118, new DUR=116.5
s = s.replace('const DUR = 118;', 'const DUR = 116.5;')
# data-duration on root composition
s = re.sub(r'data-duration="118"', 'data-duration="116.5"', s)
# TOTAL_DURATION extender we injected
s = s.replace('tl.set({}, {}, 117.5);', 'tl.set({}, {}, 116);')
# Narration data-duration (currently 116)
s = re.sub(r'(audio id="narration"[^>]*data-duration=")\d+(")', r'\g<1>116\g<2>', s)

# Also retime SFX whoosh data-starts to match new T anchors
for i, new in enumerate(new_T, start=1):
    cur_audio = cur_T[i-1]
    s = re.sub(
        r'(id="sfx-whoosh-t' + str(i) + r'"[^>]*data-start=")' + re.escape(str(cur_audio)) + r'(")',
        rf'\g<1>{new}\g<2>',
        s
    )

print(f'  timeline retimed: {n_repls} anchor replacements + DUR/duration/SFX whooshes')

# ─── Write ──
with open(PATH, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print(f'file size: {len(s)} chars')
