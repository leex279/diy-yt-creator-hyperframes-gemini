# Claude Code v2.1.126 — marckrenn Highlights

**Release Date:** May 1

## Key Features

1. **Edit Tool Enhancement**: "Edit tool now performs exact string replacements in files, so edits only change exact matched text"

2. **Project Purge Command**: `claude project purge [path]` deletes Claude Code data including transcripts, tasks, files, history, and config, with `--dry-run/-i` option available

3. **Permission Bypass Flag**: `--dangerously-skip-permissions` disables prompts for `.claude/.git/.vscode` and shell RC files, enabling writes without confirmation

## Notable CLI Fixes

The release addressed 30+ issues, including:

- Image handling: Downscaling images larger than 2000px on paste; removing oversized images from history
- Authentication: Fixed OAuth failures on slow connections, IPv6-only environments, and localhost callback issues
- Session stability: Resolved "Stream idle timeout" errors during Mac sleep and long model thinking pauses
- Terminal rendering: Fixed trackpad scrolling speed in Cursor/VS Code 1.92–1.104 and garbled character display on Windows
- Input handling: Ctrl+L now redraws the screen rather than clearing prompt input

## Metadata

- Time since previous release: 15 hours 35 minutes
- Prompt tokens increased 6.0% (+5,142)
- Tools category in prompts expanded to 25.4% of token mix
