#!/bin/bash
# Update agent-browser skill from source repo
# Source: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser
#
# Usage: bash .claude/commands/agent-browser/update-from-source.sh

set -e

SKILL_DIR=".claude/commands/agent-browser"
REPO="vercel-labs/agent-browser"
SKILL_PATH="skills/agent-browser"

echo "Updating agent-browser skill from $REPO..."

# Create directories if they don't exist
mkdir -p "$SKILL_DIR/references" "$SKILL_DIR/templates"

# Download SKILL.md
echo "  - SKILL.md"
gh api "repos/$REPO/contents/$SKILL_PATH/SKILL.md" --jq '.content' | base64 -d > "$SKILL_DIR/SKILL.md"

# Download references
for file in authentication.md proxy-support.md session-management.md snapshot-refs.md video-recording.md; do
  echo "  - references/$file"
  gh api "repos/$REPO/contents/$SKILL_PATH/references/$file" --jq '.content' | base64 -d > "$SKILL_DIR/references/$file" 2>/dev/null || echo "    (not found, skipping)"
done

# Download templates
for file in authenticated-session.sh capture-workflow.sh form-automation.sh; do
  echo "  - templates/$file"
  gh api "repos/$REPO/contents/$SKILL_PATH/templates/$file" --jq '.content' | base64 -d > "$SKILL_DIR/templates/$file" 2>/dev/null || echo "    (not found, skipping)"
  chmod +x "$SKILL_DIR/templates/$file" 2>/dev/null || true
done

# Record update timestamp
echo "Last updated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" > "$SKILL_DIR/.source-info"
echo "Source: https://github.com/$REPO/tree/main/$SKILL_PATH" >> "$SKILL_DIR/.source-info"

echo "Done! Skill updated from source."
