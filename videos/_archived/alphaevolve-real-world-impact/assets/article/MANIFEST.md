# Article Asset Manifest — AlphaEvolve impact (DeepMind)

Source: https://deepmind.google/blog/alphaevolve-impact/
Captured: 2026-05-07

All assets pulled from the live DeepMind article via agent-browser + curl with the `https://deepmind.google/` referer header. The four still images come straight from `lh3.googleusercontent.com` at 1440×810 source size; the two videos come from `storage.googleapis.com/gdm-deepmind-com-prod-public/`.

## Hero / cold-open candidates

- `hero-topo-motion.webm` (24 MB, animated, 3840×2160 source)
  Original URL: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/NNmL1hUvjZQiOHC-/alphaevolve-header-16x9-motion.webm
  Caption: article header / hero animation
  Shows: animated wireframe topographic terrain in Google's four-color palette — green, orange/yellow, magenta/red, purple/teal — overlaid on Python code text, with cyan probe markers rising from peaks. Visually evokes algorithmic optimization landscape ("hill-climbing" / search through a function). HERO candidate for Scene 01 cold-open. Animation is short loop — can be wired as a `<video>` element OR used as the still below.

- `hero-topo-still.png` (10 MB, 3840×2160 still extracted at t=1s)
  Static fallback / thumbnail candidate from the hero animation.

## AlphaEvolve UI demo

- `alphaevolve-demo.webm` (6 MB, animated)
  Original URL: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/NNmL1hUvjZQiOHC-/alphaevolve_demo_video.webm
  Caption: "Tammes Problem: Maximizing Spherical Point Separation" — interactive gallery walkthrough
  Shows: AlphaEvolve product UI — scoreboard graph of best programs over time, "Selected Program" panel with 3D scatter (sphere packing solution), code/notes panel. Strong "this is the actual product" beat. Use in Scene 06/07 to show the gallery exists at alphaevolve-examples.web.app.

- `alphaevolve-demo-still.png` (2 MB)
  Static still from the demo video at t=1s.

## Domain-section illustrations

- `dna-genomics.jpg` (118 KB, 1152×648, valid JPEG)
  Original URL: https://lh3.googleusercontent.com/AQO4-KC1y4l_eOV0jS66QbkoodWyfeeje-4HnoAnFFRgAuBz40WpwS2fbv6cPSnHrudBVPLHVboq4f6u_ZPejTGWJ_9vW1tmrpCSYHyjgLFiryaZtg=w1440-h810-n-nu
  Alt: "A 3D rendering of multiple DNA double helix structures made of small white and blue spheres, floating against a dark, textured background with a shallow depth of field."
  Section: Genomics / DeepConsensus
  Shows: stacked DNA helices, blue/white particle aesthetic. Pair with the "30% reduction in DNA sequencing variant detection errors" stat. Good for Scene 03 (biotech / health).

- `powerlines-grid.jpg` (200 KB, 1152×648, valid JPEG)
  Original URL: https://lh3.googleusercontent.com/xT26k7Gu_Lt0iDD2j_ZOQx2VmaZGH2U4j9vGCzo7cmla2UBefMcw-sQ6-12Dvb1SxDUG1Az4epE1bJg71z5KiYMxkMWdCL5eH9Rg6JiFIloZeWRBev8=w1440-h810-n-nu
  Alt: "A wide landscape shot of high-voltage power lines and transmission towers stretching across a lush green field under a clear blue sky."
  Section: Power Grid Optimization (AC Optimal Power Flow)
  Shows: high-voltage transmission infrastructure. Pair with the "14% → 88% feasible solutions" stat. Good for Scene 04 (logistics / infrastructure / energy).

- `microchip-quantum.jpg` (64 KB, 1152×648, valid JPEG)
  Original URL: https://lh3.googleusercontent.com/bhd0zRY8D-OCMR2gmX8bWQWa2auM6YuqTs1uj_UQKGFBwnqm8V6kkRj99dLZ8iVZjusyM8SS-FnlLRBP_W24nqvOM8aIeEabb6Y-St4I_DeQMtm9eQ=w1440-h810-n-nu
  Alt: "A gloved hand holding a square microchip processor with a reflective surface in a cleanroom setting."
  Section: Quantum Physics / hardware (also reusable for TPU silicon scene)
  Shows: cleanroom-gloved hand, square reflective microchip. Pair with the "10× lower error in quantum circuits" stat AND/OR the Jeff Dean TPU silicon quote. Hero candidate for Scene 05 (chip design / TPU recursion).

- `math-software-interface.jpg` (107 KB, 1152×648, valid JPEG)
  Original URL: https://lh3.googleusercontent.com/0PyMvA2pLEg69CeZUEWPy4U9D_VU9urOibCixZhsim2RoeC0cbmOMjEjCat0zRj0iN4eS0RSTWJRMjJi70qIxidYDeqjtiKpNWIW2ZWPke3Tr-5i1FM=w1440-h810-n-nu
  Alt: "A software interface showing a line graph of performance scores over time, overlaid with a 'Selected Program' window containing several bar charts and a snippet of Python code for an optimization experiment."
  Section: Mathematics
  Shows: AlphaEvolve gallery UI — performance score graph + bar charts + Python code overlay. Good for Scene 06 (math / Erdős / Tao quote) OR repurpose as supplementary product shot.

## Reference / debug

- `page-screenshot-top.png` (157 KB) — agent-browser screenshot of the live page top. Reference only; do NOT ship in the video.

## Ready-to-wire cheat sheet

If the composition uses html-in-canvas vfx-iphone-device for a "look at the actual product" moment, point it at `alphaevolve-demo-still.png` or sequence frames from `alphaevolve-demo.webm`.

If using a `<video>` element to play the hero loop, pass through `hero-topo-motion.webm` directly — it's already 4K H.264-equivalent webm and renders cleanly in HyperFrames Chromium.

For static screenshot cards (vfx-shatter / curtain-reveal / cinema-title-slam targets), use the four 1440×810 jpgs as-is — they crop well to 1080×1920 vertical.

## Blocked / not captured

- None. All five domain-section illustrations + both videos + the page chrome were captured successfully. No images returned `STATUS: blocked`.

## Notes

- The DeepMind article also references `alphaevolve-examples.web.app` (interactive gallery) — operator can capture additional UI screenshots there if a deeper "show the product" beat is wanted. Not required for Phase 0.
- Article authors retain copyright; usage is for editorial commentary on the published research and falls under fair use for an explainer video. Credit "Source: Google DeepMind, AlphaEvolve impact, May 7, 2026" in the description.
