"""Build single-composition index.html from existing scene-*.html files.

Sub-composition injection has a bug we couldn't isolate (scenes 2,4,5,...
render empty under deterministic frame capture even though architecture
matches working videos). This collapses the 14 sub-compositions into one
root composition: each scene becomes an inline <div> with all animations
on the root timeline. No data-composition-src.
"""
import re
from pathlib import Path

PROJ = Path(__file__).parent
COMP = PROJ / "compositions"

# Scene order + word-anchored start times from transcript.json.
# Each anchor was the first word of the scene's narration paragraph,
# pulled with start - 0.3s lead so the visual hits slightly before the word.
SCENES = [
    # (name, file_basename, start_seconds)
    # Anchors are first-word transcript starts minus 0.3s lead (clamped >= 0).
    # Re-anchor after every script.txt change: re-run TTS, re-transcribe,
    # then update these values so the visual hits ~0.3s before each spoken line.
    # The dedicated install-node / install-ffmpeg scenes were dropped — the
    # download scenes already carry the install commands inline. The standalone
    # `preview` scene was replaced by the more-detailed agent flow:
    # open-agent → prompt-1 → studio-v1 → prompt-2 → studio-v2 → check.
    # Dynamous midroll inserted after init, before the agent flow begins.
    ("hook",             "scene-hook.html",              0.000),
    ("prereqs",          "scene-prereqs.html",          19.727),
    ("nodejs-download",  "scene-nodejs-download.html",  33.519),
    ("ffmpeg-download",  "scene-ffmpeg-download.html",  53.627),
    ("verify",           "scene-verify.html",           67.326),
    ("pick-agent",       "scene-pick-agent.html",       79.911),
    ("skill-install",    "scene-skill-install.html",    98.568),
    ("init",             "scene-init.html",            107.089),
    # Dynamous midroll — brand-locked block from shared/lib/blocks/dynamous-midroll/.
    # Brand audio (dynamous-midroll-v2.mp3, 31.007s) is spliced into narration.wav at
    # 122.700s (between init's "guide." TTS tail and open-agent's "Open" word).
    ("dynamous-midroll", "scene-dynamous-midroll.html",122.700),
    # Post-midroll TTS shifts by +31.007s from the TTS-only transcript anchors.
    ("open-agent",       "scene-open-agent.html",      153.897),
    ("prompt-1",         "scene-prompt-1.html",        164.694),
    ("studio-v1",        "scene-studio-v1.html",       176.350),
    ("prompt-2",         "scene-prompt-2.html",        189.259),
    ("studio-v2",        "scene-studio-v2.html",       201.159),
    ("check",            "scene-check.html",           209.182),
    ("render",           "scene-render.html",          226.782),
    ("cta",              "scene-cta.html",             242.339),
]
TOTAL = 264.5

def parse_scene(path: Path):
    """Return (style_text, body_html, anim_lines) from a scene file.

    body_html is the contents of the inner <div data-composition-id=...>
    minus the trailing <script>. anim_lines is the list of GSAP statements
    inside that script (between window.__timelines and the registration line).
    """
    text = path.read_text(encoding="utf-8")

    # Pull out the <style>...</style> block
    style_match = re.search(r"<style>(.*?)</style>", text, re.S)
    style = style_match.group(1).strip() if style_match else ""

    # Pull out body: everything inside <div data-composition-id=...> up to <script>
    body_match = re.search(
        r'<div data-composition-id="[^"]*"[^>]*>(.*?)<script\s+src=',
        text, re.S)
    if not body_match:
        raise RuntimeError(f"no body in {path}")
    body = body_match.group(1)
    # Strip the inner <style> block since we hoist styles to head
    body = re.sub(r"<style>.*?</style>", "", body, flags=re.S).strip()

    # Pull animation statements
    script_match = re.search(r"<script>\s*(.*?)\s*</script>\s*</div>\s*</template>", text, re.S)
    if not script_match:
        raise RuntimeError(f"no script in {path}")
    script = script_match.group(1)

    anim_lines = []
    for line in script.splitlines():
        s = line.strip()
        if not s: continue
        if s.startswith("//"): continue
        if "window.__timelines" in s and ("=" in s or "||" in s):
            # skip both `window.__timelines = window.__timelines || {}` and
            # `window.__timelines["scene-X"] = tl;`
            continue
        if s.startswith("const tl ="): continue
        if s.startswith("const transcript"): continue
        anim_lines.append(line.rstrip())

    return style, body, anim_lines


def shift_anim_position(line: str, offset: float) -> str:
    """Add scene start offset to the position-arg of a GSAP tl.set/.to/.fromTo call.

    Exception — initial-state setters (tl.set(..., 0)) are NOT shifted. They establish
    hidden initial state and must fire at global t=0 so the elements are hidden BEFORE
    the scene's crossfade-in window. Otherwise elements show their CSS default (visible)
    during the 0.4s crossfade-in, then snap-hide at scene_start, then animate in —
    visible to the viewer as a "flash" of the next scene's content.
    """
    # The position arg is the LAST arg, a numeric literal followed by ');'
    m = re.search(r"^(.*),\s*([0-9]+\.?[0-9]*)\s*\);(.*)$", line)
    if m:
        prefix, pos, suffix = m.group(1), float(m.group(2)), m.group(3)
        # Keep initial-state tl.set(..., 0) at global t=0
        is_set = "tl.set(" in prefix
        if is_set and pos == 0:
            return f"{prefix}, 0.000);{suffix}"
        new_pos = pos + offset
        return f"{prefix}, {new_pos:.3f});{suffix}"
    # forEach lambdas with `}, t)` etc — try alternative
    m2 = re.search(r"^(.*\}),\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\);(.*)$", line)
    if m2:
        # variable-position form; not applicable in our scenes
        return line
    return line  # no position offset found; leave as-is


REPO_ROOT = PROJ.parent.parent  # videos/<slug> -> repo root

# When the banner enters in the host timeline (absolute global seconds).
# Support banner sits during pick-agent (well before the dynamous midroll at 123.5s).
# Subscribe banner enters early in the CTA scene; it exits ~7s later, just before
# the natural #cta-subscribe pulse at 264.9s.
SUPPORT_BANNER_AT = 84.0
SUBSCRIBE_BANNER_AT = 250.1


def parse_component(component_path: Path):
    """Return (html_markup, css_text, js_text) extracted from a paste-in component file.

    Components in shared/lib/components/ have three labelled sections:
      <!-- 1) HTML --> ... <!-- 2) CSS -->
      <style> ... </style>
      <script> ... </script>
    HTML markup = everything between section 1 and 2 markers (strips inline
    HTML comments). CSS and JS are taken verbatim from <style>/<script> blocks.
    """
    text = component_path.read_text(encoding="utf-8")
    # HTML markup section first (before stripping comments)
    html_match = re.search(r"<!--\s*1\)\s*HTML.*?-->\s*(.*?)\s*<!--\s*2\)\s*CSS",
                           text, re.S)
    # Strip ALL HTML comments before matching <style>/<script>. The component
    # file's section markers contain the literal text "<style>" and "<script>"
    # inside comments (e.g. "merge into your composition's <style> block").
    # Without stripping, the regex matches that text as a tag opener and
    # corrupts the captured CSS/JS.
    text_no_comments = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    css = re.search(r"<style>\s*(.*?)\s*</style>", text_no_comments, re.S)
    js = re.search(r"<script>\s*(.*?)\s*</script>", text_no_comments, re.S)
    if not (css and js and html_match):
        raise RuntimeError(f"could not parse component: {component_path}")
    html_markup = html_match.group(1)
    # Strip inline HTML comments from markup section
    html_markup = re.sub(r"<!--.*?-->", "", html_markup, flags=re.S).strip()
    return html_markup, css.group(1).strip(), js.group(1).strip()


def main():
    print("=== Building single-composition index.html ===\n")

    all_styles = []
    all_bodies = []
    all_anims = []

    for name, fname, start in SCENES:
        path = COMP / fname
        style, body, anim_lines = parse_scene(path)

        # Strip clip + data-* from background <img> tags — wrapper opacity
        # controls visibility now, so they don't need timeline registration.
        body = re.sub(
            r'<img\s+class="clip"\s+([^>]*?)\s*data-start="[0-9.]+"\s+data-duration="[0-9.]+"\s+data-track-index="[0-9]+"',
            r'<img \1',
            body, flags=re.S)

        # Shift <video class="clip"> data-start by scene start; extend
        # data-duration so the video plays for the full scene window
        # (loops via the loop attribute already on the element).
        # Find next-scene start to compute duration.
        idx = [i for i, s in enumerate(SCENES) if s[0] == name][0]
        next_start = SCENES[idx+1][2] if idx+1 < len(SCENES) else TOTAL
        scene_duration = next_start - start
        def shift_video(m, _start=start, _dur=scene_duration):
            attrs = m.group(0)
            attrs = re.sub(r'data-start="0"', f'data-start="{_start:.3f}"', attrs)
            attrs = re.sub(r'data-duration="[0-9.]+"', f'data-duration="{_dur:.3f}"', attrs)
            return attrs
        body = re.sub(
            r'<video[^>]*class="clip"[^>]*?>',
            shift_video,
            body, flags=re.S)

        # Sub-compositions live at compositions/scene-*.html and use ../assets/...
        # to reach project assets. After flattening into root index.html, the
        # ../ would escape the project directory and 404 in the studio. Rewrite.
        body = body.replace('"../assets/', '"assets/').replace("'../assets/", "'assets/")

        # Wrap body in a scene-mount div. Dynamous midroll's inner content uses
        # absolute-positioned phases that overlap, but the inspector measures
        # natural-flow text bounds — so flag the wrapper as overflow-allowed.
        wrapper_id = f"scene-mount-{name}"
        extra_attrs = ' data-layout-allow-overflow="true"' if name == "dynamous-midroll" else ''
        all_bodies.append(f'  <!-- scene: {name} (data-start={start}s) -->')
        all_bodies.append(f'  <div class="scene-mount" id="{wrapper_id}"{extra_attrs}>')
        all_bodies.append(body)
        all_bodies.append(f'  </div>')
        all_bodies.append('')

        all_styles.append(f'/* === scene: {name} === */')
        all_styles.append(style)
        all_styles.append('')

        # Shift every animation by `start`
        all_anims.append(f'  // === scene: {name} (start={start}s) ===')
        for line in anim_lines:
            shifted = shift_anim_position(line, start)
            all_anims.append(shifted)
        all_anims.append('')

    # Build final HTML
    styles_text = "\n".join(all_styles)
    bodies_text = "\n".join(all_bodies)
    anims_text = "\n".join(all_anims)

    # Scene mount visibility: at start-0.4, set visible and fade-in;
    # at next_start-0.7 (0.3 after fadeIn began), set hidden.
    # First scene starts visible.
    mount_init = []
    crossfade = []
    for i, (name, _, start) in enumerate(SCENES):
        sel = f"#scene-mount-{name}"
        if i == 0:
            mount_init.append(f'  // scene-mount-{name}: starts visible')
        else:
            mount_init.append(f'  gsap.set("{sel}", {{ opacity: 0, visibility: "hidden" }});')

    for i, (name, _, start) in enumerate(SCENES):
        sel = f"#scene-mount-{name}"
        if i > 0:
            cf_at = max(0, start - 0.4)
            crossfade.append(f'  tl.set("{sel}", {{ visibility: "visible" }}, {cf_at:.3f});')
            crossfade.append(f'  tl.to("{sel}", {{ opacity: 1, duration: 0.4, ease: "power1.inOut" }}, {cf_at:.3f});')
        if i < len(SCENES) - 1:
            next_start = SCENES[i+1][2]
            out_at = max(0, next_start - 0.4)
            crossfade.append(f'  tl.to("{sel}", {{ opacity: 0, duration: 0.4, ease: "power1.inOut" }}, {out_at:.3f});')
            crossfade.append(f'  tl.set("{sel}", {{ visibility: "hidden" }}, {out_at + 0.4:.3f});')

    mount_init_text = "\n".join(mount_init)
    crossfade_text = "\n".join(crossfade)

    # Whoosh SFX — one per scene transition (skip dynamous-midroll, which
    # uses dedicated midroll-transition-in/out SFX wired below). The same
    # set of scene-start times drives shape-backdrop re-randomisation.
    whoosh = []
    whoosh_scene_starts = []  # absolute scene-start seconds for each whoosh
    for i, (name, _, start) in enumerate(SCENES):
        if i == 0: continue
        if name == "dynamous-midroll": continue
        # Skip whoosh on the scene immediately AFTER dynamous-midroll too
        # (transition-out SFX handles that boundary).
        prev_name = SCENES[i-1][0]
        if prev_name == "dynamous-midroll": continue
        cf_at = max(0, start - 0.5)
        whoosh.append(
            f'  <audio id="sfx-whoosh-{i:02d}" class="clip" '
            f'src="assets/sfx/cinematic-whoosh.mp3" '
            f'data-start="{cf_at:.3f}" data-duration="1.5" '
            f'data-track-index="3" data-volume="0.11"></audio>'
        )
        whoosh_scene_starts.append(start)
    whoosh_text = "\n".join(whoosh)
    whoosh_times_js = "[" + ", ".join(f"{t:.3f}" for t in whoosh_scene_starts) + "]"

    # Dynamous midroll: brand-locked transition-in/out SFX (host-level, see
    # shared/lib/blocks/dynamous-midroll/recipe.md step 7). Volumes at 0.20/0.15
    # per .claude/rules/audio-design.md cap of 0.25.
    midroll_sfx = ""
    for name, _, start in SCENES:
        if name == "dynamous-midroll":
            midroll_sfx = (
                f'\n  <audio id="midroll-sfx-in" class="clip" '
                f'src="audio/midroll-transition-in.mp3" '
                f'data-start="{start:.3f}" data-duration="1.5" '
                f'data-track-index="4" data-volume="0.20"></audio>'
                f'\n  <audio id="midroll-sfx-out" class="clip" '
                f'src="audio/midroll-transition-out.mp3" '
                f'data-start="{start + 30.5:.3f}" data-duration="1.5" '
                f'data-track-index="4" data-volume="0.15"></audio>'
            )
            break
    whoosh_text = whoosh_text + midroll_sfx

    # Banners: shared paste-in components from shared/lib/components/.
    # We extract the HTML/CSS/JS once and inline them in the final template,
    # then call addSupportBanner / addSubscribeBanner with absolute timestamps.
    sup_html, sup_css, sup_js = parse_component(
        REPO_ROOT / "shared" / "lib" / "components" / "support-banner" / "component.html")
    sb_html, sb_css, sb_js = parse_component(
        REPO_ROOT / "shared" / "lib" / "components" / "subscribe-banner" / "component.html")

    # Final HTML
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>How to Install and Use HyperFrames — Beginner Setup Tutorial</title>
<link rel="stylesheet" href="tokens/long-form.css">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{
    width: 1920px; height: 1080px;
    overflow: hidden;
    background: var(--bg);
    font-family: var(--sans);
    color: var(--text);
    -webkit-font-smoothing: antialiased;
  }}

  #ambient {{
    position: absolute; inset: -200px;
    background:
      radial-gradient(circle at 25% 20%, rgba(59,130,246,.08), transparent 55%),
      radial-gradient(circle at 78% 78%, rgba(139,92,246,.06), transparent 60%),
      radial-gradient(circle at 50% 100%, rgba(6,182,212,.05), transparent 50%);
    pointer-events: none; z-index: 0;
  }}
  #shape-backdrop {{
    position: absolute; inset: 0;
    pointer-events: none; overflow: hidden; z-index: 0;
  }}
  #shape-backdrop img {{
    position: absolute; opacity: .045;
    object-fit: contain; pointer-events: none;
  }}
  #noise-overlay {{
    position: absolute; inset: 0;
    width: 1920px; height: 1080px;
    pointer-events: none; z-index: 8;
    opacity: .035; mix-blend-mode: overlay;
  }}

  #top-banner {{
    position: absolute; top: 26px; left: 0;
    width: 1920px; z-index: 10;
    pointer-events: none; text-align: center;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,.5));
  }}
  #top-banner .wordmark {{
    display: inline-flex; align-items: center; gap: 14px;
    font-family: var(--sans); font-weight: 800;
    font-size: 28px; letter-spacing: 4px;
    color: var(--text); text-transform: uppercase;
  }}
  #top-banner .wordmark .dot {{
    width: 12px; height: 12px; border-radius: 50%;
    background: var(--accent-warn);
    box-shadow: 0 0 14px rgba(249,115,22,.7);
  }}
  #top-banner .wordmark .light {{
    color: var(--text-secondary);
    font-weight: 500; letter-spacing: 3px;
    font-size: 22px;
  }}

  #progress-track {{
    position: absolute; bottom: 0; left: 0;
    width: 1920px; height: 6px;
    background: rgba(255,255,255,.06);
    z-index: 10;
  }}
  #progress-fill {{
    width: 0; height: 100%;
    background: var(--accent-warn);
    box-shadow: 0 0 12px rgba(249,115,22,.55);
  }}

  /* Scene mounts — each a 1920×1080 layer; root timeline drives visibility */
  .scene-mount {{
    position: absolute; top: 0; left: 0;
    width: 1920px; height: 1080px;
    z-index: 1;
  }}

{styles_text}

  /* === support-banner component === */
  {sup_css}

  /* === subscribe-banner component === */
  {sb_css}
</style>
</head>
<body>
<div id="root"
     data-composition-id="main"
     data-start="0"
     data-duration="{TOTAL}"
     data-width="1920"
     data-height="1080">

  <div id="ambient"></div>
  <div id="shape-backdrop"></div>

  <div id="top-banner">
    <div class="wordmark">
      <span class="dot"></span>
      <span>HyperFrames</span>
      <span class="light">&middot; setup tutorial</span>
    </div>
  </div>

  <div id="progress-track"><div id="progress-fill"></div></div>

{bodies_text}

  <audio id="narration"
         class="clip"
         src="audio/narration.wav"
         data-start="0"
         data-duration="{TOTAL}"
         data-track-index="2"
         data-volume="1"></audio>

{whoosh_text}

  <svg id="noise-overlay" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="noise-filter" x="0%" y="0%" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="4" seed="42" stitchTiles="stitch" result="noise" />
        <feColorMatrix type="saturate" values="0" in="noise" result="monoNoise" />
      </filter>
    </defs>
    <rect width="100%" height="100%" filter="url(#noise-filter)" fill="white" />
  </svg>

  <!-- === support-banner component (paste-in HTML, anim driven by host JS) === -->
  {sup_html}

  <!-- === subscribe-banner component (paste-in HTML, anim driven by host JS) === -->
  {sb_html}
</div>

<script>
  // Deterministic seeded shape backdrop (xmur3-style)
  function seedHash(seed) {{
    let h = 1779033703 ^ seed.length;
    for (let i = 0; i < seed.length; i++) {{
      h = Math.imul(h ^ seed.charCodeAt(i), 3432918353);
      h = (h << 13) | (h >>> 19);
    }}
    h = Math.imul(h ^ (h >>> 16), 2246822507);
    h = Math.imul(h ^ (h >>> 13), 3266489909);
    h ^= h >>> 16;
    return (h >>> 0) / 4294967296;
  }}

  function spawnShapes(seedPrefix, container) {{
    const shapes = ['assets/shapes/shape1.svg','assets/shapes/shape2.svg','assets/shapes/shape3.svg'];
    const count = 14, w = 1920, h = 1080, minSize = 200, sizeRange = 220;
    const minDist = 360, MAX_TRIES = 80;
    const placed = [];
    let attempt = 0;
    for (let i = 0; i < count; i++) {{
      let best = null, bestScore = -1;
      for (let t = 0; t < MAX_TRIES; t++) {{
        const seed = seedPrefix + '-' + i + '-' + attempt++;
        const size = minSize + seedHash(seed + '-size') * sizeRange;
        const cx = seedHash(seed + '-x') * (w - size * 0.4) + size * 0.2;
        const cy = seedHash(seed + '-y') * (h - size * 0.4) + size * 0.2;
        const rot = (seedHash(seed + '-rot') - 0.5) * 90;
        let nearest = Infinity;
        for (const p of placed) {{
          const dx = cx - p.cx, dy = cy - p.cy;
          const d2 = dx*dx + dy*dy;
          if (d2 < nearest) nearest = d2;
        }}
        if (nearest >= minDist*minDist) {{ best = {{cx,cy,size,rot}}; break; }}
        if (nearest > bestScore) {{ bestScore = nearest; best = {{cx,cy,size,rot}}; }}
      }}
      placed.push(best);
      const img = document.createElement('img');
      img.src = shapes[i % shapes.length];
      img.style.cssText =
        'left:'+(best.cx-best.size/2)+'px;'+
        'top:'+(best.cy-best.size/2)+'px;'+
        'width:'+best.size+'px;'+
        'height:'+best.size+'px;';
      container.appendChild(img);
      gsap.set(img, {{ rotation: best.rot }});
    }}
  }}

  // Re-randomise shape positions at every scene transition (paired with the
  // cinematic-whoosh SFX so the field re-scatter reads as part of the whoosh).
  // Mirrors templates/long-form/claude-code-version/index.html.
  function repositionShapesPerScene(tl, container, seedPrefix, sceneStartTimes) {{
    const imgs = Array.from(container.querySelectorAll('img'));
    if (!imgs.length || !sceneStartTimes.length) return;
    const w = 1920, h = 1080, minDist = 360, MAX_TRIES = 80;
    const anchors = imgs.map(img => ({{
      left: parseFloat(img.style.left),
      top:  parseFloat(img.style.top),
      size: parseFloat(img.style.width),
    }}));
    sceneStartTimes.forEach((sceneT, sceneIdx) => {{
      const placed = [];
      let attempt = 0;
      const positions = imgs.map((img, i) => {{
        const size = anchors[i].size;
        let best = null, bestScore = -1;
        for (let t = 0; t < MAX_TRIES; t++) {{
          const seed = seedPrefix + '-scene' + sceneIdx + '-' + i + '-' + (attempt++);
          const cx = seedHash(seed + '-x') * (w - size * 0.4) + size * 0.2;
          const cy = seedHash(seed + '-y') * (h - size * 0.4) + size * 0.2;
          const rot = (seedHash(seed + '-rot') - 0.5) * 90;
          let nearest = Infinity;
          for (const p of placed) {{
            const dx = cx - p.cx, dy = cy - p.cy;
            const d2 = dx * dx + dy * dy;
            if (d2 < nearest) nearest = d2;
          }}
          if (nearest >= minDist * minDist) {{ best = {{ cx, cy, rot }}; break; }}
          if (nearest > bestScore) {{ bestScore = nearest; best = {{ cx, cy, rot }}; }}
        }}
        placed.push({{ cx: best.cx, cy: best.cy }});
        return {{
          x: (best.cx - size / 2) - anchors[i].left,
          y: (best.cy - size / 2) - anchors[i].top,
          rot: best.rot,
        }};
      }});
      tl.to(imgs, {{
        x: (i) => positions[i].x,
        y: (i) => positions[i].y,
        rotation: (i) => positions[i].rot,
        duration: 1.4,
        ease: 'power2.inOut',
      }}, sceneT - 0.4);
    }});
  }}

  spawnShapes('hyperframes-setup-tutorial', document.getElementById('shape-backdrop'));

  window.__timelines = window.__timelines || {{}};
  const TOTAL_DURATION = {TOTAL};
  const tl = gsap.timeline({{ paused: true, defaults: {{ ease: "power3.out" }} }});

  // Ambient breath
  tl.fromTo("#ambient",
    {{ opacity: 0.85, scale: 1.0 }},
    {{ opacity: 1.0, scale: 1.04, duration: 35, ease: "sine.inOut", yoyo: true, repeat: 9 }},
    0);

  // Re-randomise shape backdrop at every whoosh-tagged scene transition.
  // Times come from build-single-comp.py (one per non-midroll scene boundary).
  repositionShapesPerScene(
    tl,
    document.getElementById('shape-backdrop'),
    'hyperframes-setup-tutorial',
    {whoosh_times_js}
  );

  // Linear progress fill
  tl.fromTo("#progress-fill", {{ width: 0 }}, {{ width: 1920, duration: TOTAL_DURATION, ease: "none" }}, 0);

  // Top wordmark fade-in
  tl.from("#top-banner", {{ y: -16, opacity: 0, duration: 0.6, ease: "power2.out" }}, 0.2);

  // Initial mount visibility — first scene visible, rest hidden
{mount_init_text}

  // Scene crossfades — fade IN at start-0.4, fade OUT at next_start-0.4
{crossfade_text}

  // Scene-internal animations, position-shifted by each scene's start time
{anims_text}

  // === Banner components (paste-in JS) ===
  {sup_js}

  {sb_js}

  // Fire each banner once at its chosen anchor time.
  addSupportBanner(tl, {SUPPORT_BANNER_AT});
  addSubscribeBanner(tl, {SUBSCRIBE_BANNER_AT});

  // Pad to full duration
  tl.set({{}}, {{}}, TOTAL_DURATION);

  window.__timelines["main"] = tl;
</script>
</body>
</html>
"""

    out = PROJ / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out}")
    print(f"  total lines: {len(html.splitlines())}")
    print(f"  total duration: {TOTAL}s")
    print(f"  scenes: {len(SCENES)}")
    print(f"  whoosh SFX: {len(SCENES)-1}")


if __name__ == "__main__":
    main()
