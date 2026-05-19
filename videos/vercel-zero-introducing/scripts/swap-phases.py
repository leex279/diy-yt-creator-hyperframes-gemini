"""Replace phases 3-15 of the vercel-zero-introducing index.html with
narration-aligned simple content. Run from repo root."""
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PATH = 'videos/vercel-zero-introducing/index.html'

with open(PATH, encoding='utf-8') as f:
    s = f.read()


def replace_phase_html(s, phase_num, new_inner_html):
    """Replace the inner HTML of <div id="phaseN" class="phase">...</div>"""
    pattern = re.compile(
        r'(<div id="phase' + str(phase_num) + r'" class="phase">)(.*?)(\n\s*</div>\s*\n\s*\n\s*<!--)',
        re.DOTALL
    )
    m = pattern.search(s)
    if not m:
        print(f'  P{phase_num}: MISS')
        return s
    new = m.group(1) + '\n' + new_inner_html + '\n  ' + m.group(3)
    s = s[:m.start()] + new + s[m.end():]
    print(f'  P{phase_num}: replaced')
    return s


# ── Reusable hello.0 code block ───────────────────────────────────────────────
CODE_BASE = '''<div id="{wid}" style="width:920px; background:#0E121A; border-radius:24px; border:1px solid rgba(245,241,235,0.10); box-shadow:0 24px 60px rgba(0,0,0,0.6); overflow:hidden;">
        <div style="display:flex; align-items:center; gap:14px; padding:18px 28px; background:#13171F; border-bottom:1px solid rgba(245,241,235,0.06);">
          <div style="width:14px; height:14px; border-radius:50%; background:#FF6058;"></div>
          <div style="width:14px; height:14px; border-radius:50%; background:#FFBD2F;"></div>
          <div style="width:14px; height:14px; border-radius:50%; background:#28C940;"></div>
          <div style="margin-left:14px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:24px; color:#9A958D;">hello.0</div>
        </div>
        <div style="padding:36px 36px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:38px; line-height:1.5; color:#F5F1EB;">
          <div><span style="color:#c084fc;">pub fun</span> <span style="color:#06b6d4;">main</span>(world: {WORLD}) -&gt; <span style="color:#fbbf24;">Void</span> {RAISES} {{</div>
          <div style="padding-left:48px;">{CHECK} world.out.write(<span style="color:#5eead4;">"hello from zero\\n"</span>)</div>
          <div>}}</div>
        </div>
      </div>'''


def code_block(wid, highlight_world=False, highlight_raises=False, highlight_check=False):
    world_html = '<span style="color:#fbbf24; background:rgba(251,191,36,0.22); padding:2px 10px; border-radius:6px;">World</span>' if highlight_world else '<span style="color:#fbbf24;">World</span>'
    raises_html = '<span style="color:#c084fc; background:rgba(192,132,252,0.22); padding:2px 10px; border-radius:6px;">raises</span>' if highlight_raises else '<span style="color:#c084fc;">raises</span>'
    check_html = '<span style="color:#c084fc; background:rgba(192,132,252,0.22); padding:2px 10px; border-radius:6px;">check</span>' if highlight_check else '<span style="color:#c084fc;">check</span>'
    return CODE_BASE.replace('{wid}', wid).replace('{WORLD}', world_html).replace('{RAISES}', raises_html).replace('{CHECK}', check_html)


def simple_phase(phase_num, overline, headline_html, sub_html='', extra_html=''):
    sub = ''
    if sub_html:
        sub = ('<div id="p{n}-sub" style="font-family: \'Inter\', system-ui, sans-serif; '
               'font-weight:500; font-size:36px; line-height:1.3; color:#9A958D; '
               'max-width:880px; margin-top:16px;">{txt}</div>').format(n=phase_num, txt=sub_html)
    return f'''    <div class="phase-content" style="align-items:center; justify-content:center; gap:32px; padding-top:300px; padding-left:60px; padding-right:60px; text-align:center;">
      <div class="overline" id="p{phase_num}-overline" style="color:#06b6d4;">{overline}</div>
      <div id="p{phase_num}-headline" style="font-family: 'Inter', system-ui, sans-serif; font-weight:900; font-size:96px; line-height:0.95; letter-spacing:-0.03em; color:#F5F1EB; max-width:960px;">{headline_html}</div>
      {sub}
      {extra_html}
    </div>'''


# ── P3 ── Tagline pull-quote
P3_EXTRA = '''<div id="p3-pillars" style="display:flex; flex-wrap:wrap; gap:18px; justify-content:center; max-width:980px; margin-top:24px;">
        <div class="p3-pill" id="p3-pill-1" style="padding:18px 32px; border-radius:9999px; background:rgba(6,182,212,0.14); border:1px solid rgba(6,182,212,0.35); font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight:700; font-size:32px; color:#06b6d4;">explicit effects</div>
        <div class="p3-pill" id="p3-pill-2" style="padding:18px 32px; border-radius:9999px; background:rgba(192,132,252,0.14); border:1px solid rgba(192,132,252,0.35); font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight:700; font-size:32px; color:#c084fc;">predictable memory</div>
        <div class="p3-pill" id="p3-pill-3" style="padding:18px 32px; border-radius:9999px; background:rgba(96,165,250,0.14); border:1px solid rgba(96,165,250,0.35); font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight:700; font-size:32px; color:#60a5fa;">structured output</div>
        <div class="p3-pill" id="p3-pill-4" style="padding:18px 32px; border-radius:9999px; background:rgba(251,191,36,0.14); border:1px solid rgba(251,191,36,0.35); font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight:700; font-size:32px; color:#fbbf24;">small native tools</div>
      </div>'''
s = replace_phase_html(s, 3, simple_phase(
    3, 'The tagline',
    'The programming language<br><span style="color:#06b6d4;">for agents.</span>',
    '', P3_EXTRA
))

# ── P4 ── hello.0 code
s = replace_phase_html(s, 4, simple_phase(
    4, 'Hello world · examples/hello.0',
    'Files end in <span style="color:#06b6d4; font-family:\'JetBrains Mono\', monospace;">.0</span>',
    'Numeric zero. Not the letter O.',
    code_block('p4-code-wrap')
))

# ── P5 ── World capability
s = replace_phase_html(s, 5, simple_phase(
    5, 'Capability',
    '<span style="color:#fbbf24;">World</span> is handed in.',
    'No global stdout. If you want to write, you accept a World — and the compiler checks you did.',
    code_block('p5-code-wrap', highlight_world=True)
))

# ── P6 ── raises + check
s = replace_phase_html(s, 6, simple_phase(
    6, 'Errors + side effects',
    '<span style="color:#c084fc;">raises</span> &middot; <span style="color:#c084fc;">check</span>',
    'Functions declare they can fail. Every side effect is prefixed with check — the compiler sees where you touched the outside.',
    code_block('p6-code-wrap', highlight_raises=True, highlight_check=True)
))

# ── P7 ── Build line callout
P7_EXTRA = '''<div id="p7-build-out" style="width:880px; padding:36px 40px; background:#0E121A; border-radius:20px; border:1px solid rgba(245,241,235,0.10); font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:38px; color:#F5F1EB; text-align:left;">
        <span style="color:#5eead4;">✓</span> .zero/out/hello (<span style="color:#06b6d4; font-weight:800;">16.2 KiB</span>, <span style="color:#fbbf24; font-weight:800;">1 ms</span>)
      </div>
      <!-- Hidden counter targets so GSAP countUp() does not crash -->
      <span id="p7-metric" style="display:none;">0</span>
      <span id="p7-delta" style="display:none;">0</span>'''
s = replace_phase_html(s, 7, simple_phase(
    7, 'From the announcement',
    '<span style="font-family:\'JetBrains Mono\', monospace; font-size:72px;">$ zero build hello.0</span>',
    '', P7_EXTRA
))

# ── P8 ── Big metrics  (also dead targets for p3-val-1..4 + p6-stat-l/r so countUps don't crash)
P8_EXTRA = '''<!-- Hidden counter targets for legacy GSAP countUp() calls in P3/P6 -->
      <span id="p3-val-1" style="display:none;">0</span>
      <span id="p3-val-2" style="display:none;">0</span>
      <span id="p3-val-3" style="display:none;">0</span>
      <span id="p3-val-4" style="display:none;">0</span>
      <span id="p6-stat-l" style="display:none;">0</span>
      <span id="p6-stat-r" style="display:none;">0</span>'''
s = replace_phase_html(s, 8, simple_phase(
    8, 'Static binary',
    '<span style="color:#06b6d4;">16 KB.</span><br><span style="color:#fbbf24;">1 ms.</span>',
    'No runtime. No glibc. One file.',
    P8_EXTRA
))

# ── P9 ── JSON CLI list
P9_EXTRA = '''<div id="p9-cli-list" style="display:flex; flex-direction:column; gap:14px; width:880px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:32px; color:#F5F1EB; text-align:left;">
        <div class="p9-cmd" id="p9-cmd-1" style="padding:14px 28px; background:rgba(14,18,26,0.7); border-radius:14px; border-left:3px solid #06b6d4;"><span style="color:#9A958D;">$</span> zero check <span style="color:#06b6d4;">--json</span> hello.0</div>
        <div class="p9-cmd" id="p9-cmd-2" style="padding:14px 28px; background:rgba(14,18,26,0.7); border-radius:14px; border-left:3px solid #c084fc;"><span style="color:#9A958D;">$</span> zero run <span style="color:#c084fc;">--json</span> add.0</div>
        <div class="p9-cmd" id="p9-cmd-3" style="padding:14px 28px; background:rgba(14,18,26,0.7); border-radius:14px; border-left:3px solid #60a5fa;"><span style="color:#9A958D;">$</span> zero graph <span style="color:#60a5fa;">--json</span> systems-package</div>
        <div class="p9-cmd" id="p9-cmd-4" style="padding:14px 28px; background:rgba(14,18,26,0.7); border-radius:14px; border-left:3px solid #fbbf24;"><span style="color:#9A958D;">$</span> zero size <span style="color:#fbbf24;">--json</span> point.0</div>
        <div class="p9-cmd" id="p9-cmd-5" style="padding:14px 28px; background:rgba(14,18,26,0.7); border-radius:14px; border-left:3px solid #06b6d4;"><span style="color:#9A958D;">$</span> zero doctor <span style="color:#06b6d4;">--json</span></div>
      </div>'''
s = replace_phase_html(s, 9, simple_phase(
    9, 'Every command speaks JSON',
    'Built for <span style="color:#06b6d4;">agents,</span><br>not humans.',
    '', P9_EXTRA
))

# ── P10 ── Audience is an agent
s = replace_phase_html(s, 10, simple_phase(
    10, 'The audience',
    'A <span style="color:#06b6d4;">human</span> reads a terminal.<br>An <span style="color:#fbbf24;">agent</span> reads a pipe.',
    'Structured output is the whole pitch.',
))

# ── P11 ── EXPERIMENTAL
s = replace_phase_html(s, 11, simple_phase(
    11, 'Now the honest part',
    '<span style="color:#D14343;">EXPERIMENTAL.</span>',
    'The README says it directly: "the language is not stable yet."',
))

# ── P12 ── Honest gaps list
P12_EXTRA = '''<div id="p12-gaps" style="display:flex; flex-direction:column; gap:18px; width:920px; text-align:left;">
        <div class="p12-gap" id="p12-gap-1" style="padding:22px 32px; background:rgba(209,67,67,0.10); border-left:4px solid #D14343; border-radius:12px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:32px; color:#F5F1EB;"><span style="color:#D14343; font-weight:800;">×</span> No public module system documented</div>
        <div class="p12-gap" id="p12-gap-2" style="padding:22px 32px; background:rgba(209,67,67,0.10); border-left:4px solid #D14343; border-radius:12px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:32px; color:#F5F1EB;"><span style="color:#D14343; font-weight:800;">×</span> No published benchmarks</div>
        <div class="p12-gap" id="p12-gap-3" style="padding:22px 32px; background:rgba(209,67,67,0.10); border-left:4px solid #D14343; border-radius:12px; font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:32px; color:#F5F1EB;"><span style="color:#D14343; font-weight:800;">×</span> Examples all under 50 lines</div>
      </div>'''
s = replace_phase_html(s, 12, simple_phase(
    12, 'What it does NOT have yet',
    'Things the README<br>does <span style="color:#D14343;">not</span> answer.',
    '', P12_EXTRA
))

# ── P13 ── Self-host fact
s = replace_phase_html(s, 13, simple_phase(
    13, 'But also',
    'Self-host already<br><span style="color:#5eead4;">in progress.</span>',
    'A brand new C compiler — being rewritten in Zero itself. Repo path: compiler-zero/',
))

# ── P14 ── Transition to question
P14_EXTRA = '''<!-- Hidden counter targets for legacy GSAP countUp() calls in P14 -->
      <span id="p14-k1" style="display:none;">0</span>
      <span id="p14-k1d" style="display:none;">0</span>
      <span id="p14-k2" style="display:none;">0</span>
      <span id="p14-k2d" style="display:none;">0</span>
      <span id="p14-k3" style="display:none;">0</span>
      <span id="p14-k3d" style="display:none;">0</span>
      <span id="p14-k4" style="display:none;">0</span>'''
s = replace_phase_html(s, 14, simple_phase(
    14, 'So here is the real question',
    'Real new <span style="color:#06b6d4;">category</span>?<br>Or <span style="color:#fbbf24;">Go</span> with better JSON?',
    'Vercel Labs is betting agents need their own systems language.',
    P14_EXTRA
))

# ── P15 ── CTA
P15_NEW = '''    <div id="p15-flash"></div>
    <div class="phase-content" style="align-items:center; justify-content:center; gap:28px; padding-top:280px; padding-left:60px; padding-right:60px;">
      <div class="overline" id="p15-overline" style="color:#06b6d4;">Drop your verdict</div>
      <div id="p15-cta-headline" style="font-family: 'Inter', system-ui, sans-serif; font-weight:900; font-size:132px; line-height:0.95; letter-spacing:-0.03em; color:#F5F1EB; text-align:center;">REAL LANG.<br><span style="color:#9A958D;">OR HYPE?</span></div>
      <div id="p15-url-wrap" style="display:flex; align-items:center; gap:16px; padding:24px 36px; background:#0E121A; border-radius:18px; border:1px solid rgba(245,241,235,0.18); margin-top:20px;">
        <span style="font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:32px; color:#9A958D;">→</span>
        <span id="p15-url" style="font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight:700; font-size:42px; color:#F5F1EB;"><span id="p15-url-text"></span><span id="p15-caret" style="display:inline-block; width:3px; height:42px; background:#06b6d4; vertical-align:middle; margin-left:4px;"></span></span>
        <div id="p15-url-pulse"></div>
      </div>
      <div id="p15-cta-question" style="font-family: 'Inter', system-ui, sans-serif; font-weight:600; font-size:42px; color:#06b6d4; text-align:center; margin-top:14px; max-width:920px; line-height:1.25;">Real language, or hype with a dot-zero extension?</div>
      <div id="p15-cta-vercel" style="display:flex; align-items:center; gap:14px; margin-top:14px; opacity:0.75;">
        <img src="assets/vercel-logo.png" alt="Vercel" style="height:28px; filter:invert(1) brightness(2);">
        <span style="font-family: 'JetBrains Mono', ui-monospace, monospace; font-size:24px; letter-spacing:3px; color:#9A958D;">VERCEL LABS · ZERO · v0.1.1</span>
      </div>
      <!-- Hidden counter targets for legacy GSAP countUp() calls in P15 -->
      <span id="p15-stat-likes" style="display:none;">0</span>
      <span id="p15-stat-reposts" style="display:none;">0</span>
      <span id="p15-stat-views" style="display:none;">0K</span>
    </div>'''

m15 = re.search(r'(<div id="phase15" class="phase">)(.*?)(\n\s*</div>\s*\n\s*<!--\s*[─ ]*\s*Overlays)', s, re.DOTALL)
if m15:
    s = s[:m15.start()] + m15.group(1) + '\n' + P15_NEW + '\n  ' + m15.group(3) + s[m15.end():]
    print('  P15: replaced')
else:
    print('  P15: MISS')

with open(PATH, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print(f'file size: {len(s)} chars')
