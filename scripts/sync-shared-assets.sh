#!/usr/bin/env bash
# sync-shared-assets.sh — Keep shared/ASSETS.md in sync with files on disk.
#
# Wired into the PostToolUse hook in .claude/settings.json so it runs after
# every Write / Edit / Bash. Cheap when there are no changes (early exits).
#
# Behavior:
#   - Walks shared/ for non-md, non-dotfile assets
#   - Reads the existing table between the marker comments in ASSETS.md
#   - Adds new files at the end with a "_TBD_ (added by sync — please fill)" hint
#   - Marks rows whose file no longer exists with "[REMOVED]" prefix
#   - Preserves any manual edits to existing rows (Category, Use for)
#   - Writes the file only if something changed (so the hook stays a no-op
#     for unrelated edits)

set -euo pipefail

# Locate repo root deterministically — git first, then walk up from the script
if REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  :
else
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi

SHARED_DIR="$REPO_ROOT/shared"
ASSETS_MD="$SHARED_DIR/ASSETS.md"

# Early exit if shared/ or ASSETS.md is missing — nothing to sync
[ -d "$SHARED_DIR" ] || exit 0
[ -f "$ASSETS_MD" ] || exit 0

# Sentinels are split-quoted so the marker strings only appear ONCE in this
# script (no risk of self-matching). The actual markers in ASSETS.md are
# the joined HTML comments below.
BEGIN="<!""-- ASSETS:BEGIN ""-->"
END="<!""-- ASSETS:END ""-->"

# List actual asset files relative to shared/, sorted, excluding *.md and dotfiles
actual_list=$(cd "$SHARED_DIR" && find . -type f ! -name '*.md' ! -path './.*' \
  | sed 's|^\./||' | LC_ALL=C sort)

# Extract the existing table block (only data rows — skip header + separator)
existing_rows=$(awk -v begin="$BEGIN" -v end="$END" '
  $0 == begin { inblock = 1; next }
  $0 == end   { inblock = 0; next }
  inblock && /^\| / { print }
' "$ASSETS_MD")

# Parse existing rows into an associative array: filename -> "category|description"
declare -A existing=()
while IFS= read -r line; do
  [ -z "$line" ] && continue
  case "$line" in
    "| File "*) continue ;;       # skip header
    "|---"*)    continue ;;       # skip separator
  esac
  # Strip the leading and trailing pipe + whitespace, split on | into 3 cells
  trimmed="${line#|}"
  trimmed="${trimmed%|}"
  IFS='|' read -ra cells <<< "$trimmed"
  if [ "${#cells[@]}" -ge 3 ]; then
    file=$(echo "${cells[0]}"  | sed 's/^ *//;s/ *$//')
    cat=$(echo  "${cells[1]}"  | sed 's/^ *//;s/ *$//')
    desc=$(echo "${cells[2]}"  | sed 's/^ *//;s/ *$//')
    existing["$file"]="${cat}|${desc}"
  fi
done <<< "$existing_rows"

# Build the new table content
header=$'| File | Category | Use for |\n|---|---|---|'
new_rows="$header"
changed=0
declare -A actual_set=()

# 1) Iterate actual files in sorted order — keep existing metadata, blank for new ones
while IFS= read -r f; do
  [ -z "$f" ] && continue
  actual_set["$f"]=1
  if [ -n "${existing[$f]:-}" ]; then
    cat="${existing[$f]%%|*}"
    desc="${existing[$f]#*|}"
  else
    cat=""
    desc="_TBD_ (added by sync — please fill)"
    changed=1
  fi
  new_rows+=$'\n'"| $f | $cat | $desc |"
done <<< "$actual_list"

# 2) Append rows for files that have been removed from disk
for f in "${!existing[@]}"; do
  if [ -z "${actual_set[$f]:-}" ]; then
    cat="${existing[$f]%%|*}"
    desc="${existing[$f]#*|}"
    case "$desc" in
      "[REMOVED]"*) ;;             # already marked
      *) desc="[REMOVED] $desc"; changed=1 ;;
    esac
    new_rows+=$'\n'"| $f | $cat | $desc |"
  fi
done

# Bail out if nothing actually changed — keeps the hook a no-op for unrelated edits
if [ "$changed" -eq 0 ]; then
  exit 0
fi

# Splice the new block back in, in place of the old one
tmp="${ASSETS_MD}.tmp.$$"
awk -v begin="$BEGIN" -v end="$END" -v block="$new_rows" '
  $0 == begin { print; print block; skipping = 1; next }
  $0 == end   { skipping = 0; print; next }
  !skipping   { print }
' "$ASSETS_MD" > "$tmp"
mv "$tmp" "$ASSETS_MD"

echo "[sync-shared-assets] Updated $ASSETS_MD"
