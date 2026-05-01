# Screenshots

Operators drop release-specific screenshots here per video. The template
ships without any screenshot placeholders — the variant's scenes
(`scene-stats-opener`, `scene-feature-cards`, `scene-terminal`) are
typography-driven and do not require backing images.

If a release benefits from a screencap demo, the optional
`compositions/scene-video-embed.html` is wired commented-out by default in
`index.html`. To use it: drop a clip at `assets/clips/demo.mp4` and
uncomment the wrapper.

## Asset guidelines

- Keep source dimensions ≤ 3840x2160 (HyperFrames performance budget — see
  `hyperframes-cli` skill `docs performance`).
- Prefer PNG for screenshots with sharp text, JPG for photos.
