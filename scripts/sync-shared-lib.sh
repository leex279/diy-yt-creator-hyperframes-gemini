#!/usr/bin/env bash
# sync-shared-lib.sh — Keep shared/lib/MANIFEST.md in sync with files on disk.
#
# Wired into the PostToolUse hook in .claude/settings.json so it runs after
# every Write / Edit / Bash. Cheap when there are no changes (early exits).
#
# Behavior:
#   - Walks shared/lib/ for entries by kind:
#       tokens/<name>.css                       → Tokens table
#       blocks/<name>/block.html                → Blocks table
#       components/<name>/component.html        → Components table
#       effects/<name>.js                       → Effects table
#       visual-styles/<name>.md                 → Visual Styles table
#   - For each kind, reads the existing table between sentinel comments
#   - Adds new entries with a "_TBD_ (added by sync — please fill)" hint
#   - Marks rows whose entry no longer exists with "[REMOVED]" prefix
#   - Preserves manual edits to existing rows
#   - Writes the file only if something changed

set -euo pipefail

# Locate repo root deterministically
if REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  :
else
  REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi

LIB_DIR="$REPO_ROOT/shared/lib"
MANIFEST_MD="$LIB_DIR/MANIFEST.md"

[ -d "$LIB_DIR" ] || exit 0
[ -f "$MANIFEST_MD" ] || exit 0

# Sentinels — split-quoted so the marker strings only appear ONCE in this script
TOKENS_BEGIN="<!""-- LIB:TOKENS:BEGIN ""-->"
TOKENS_END="<!""-- LIB:TOKENS:END ""-->"
BLOCKS_BEGIN="<!""-- LIB:BLOCKS:BEGIN ""-->"
BLOCKS_END="<!""-- LIB:BLOCKS:END ""-->"
COMPONENTS_BEGIN="<!""-- LIB:COMPONENTS:BEGIN ""-->"
COMPONENTS_END="<!""-- LIB:COMPONENTS:END ""-->"
EFFECTS_BEGIN="<!""-- LIB:EFFECTS:BEGIN ""-->"
EFFECTS_END="<!""-- LIB:EFFECTS:END ""-->"
STYLES_BEGIN="<!""-- LIB:VISUAL-STYLES:BEGIN ""-->"
STYLES_END="<!""-- LIB:VISUAL-STYLES:END ""-->"

for sentinel in "$TOKENS_BEGIN" "$TOKENS_END" "$BLOCKS_BEGIN" "$BLOCKS_END" \
                "$COMPONENTS_BEGIN" "$COMPONENTS_END" "$EFFECTS_BEGIN" "$EFFECTS_END" \
                "$STYLES_BEGIN" "$STYLES_END"; do
  if ! grep -qF "$sentinel" "$MANIFEST_MD"; then
    echo "[sync-shared-lib] ERROR: sentinel missing in $MANIFEST_MD: $sentinel" >&2
    exit 1
  fi
done

# Extract the lines currently between two sentinels (data rows only — header
# and separator rows are part of the rebuild target so we strip them too).
extract_block() {
  local begin="$1" end="$2"
  awk -v begin="$begin" -v end="$end" '
    $0 == begin { inblock = 1; next }
    $0 == end   { inblock = 0; next }
    inblock     { print }
  ' "$MANIFEST_MD"
}

# Parse a previously-extracted block into newline-separated KEY<TAB>REST
# (REST is everything after the first column, joined by |).
# Skips header / separator rows.
rows_to_kv() {
  local raw="$1"
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    case "$line" in
      "| File "*|"| Directory "*) continue ;;
      "|---"*) continue ;;
    esac
    local trimmed="${line#|}"
    trimmed="${trimmed%|}"
    local key="${trimmed%%|*}"
    local rest="${trimmed#*|}"
    key="$(echo "$key" | sed 's/^ *//;s/ *$//')"
    # Trim each remaining cell
    local out=""
    IFS='|' read -ra cells <<< "$rest"
    for c in "${cells[@]}"; do
      local t
      t="$(echo "$c" | sed 's/^ *//;s/ *$//')"
      if [ -z "$out" ]; then
        out="$t"
      else
        out="${out}|${t}"
      fi
    done
    printf '%s\t%s\n' "$key" "$out"
  done <<< "$raw"
}

# Look up a key in a KV blob; print "" if not found.
kv_get() {
  local kv="$1" needle="$2"
  awk -F '\t' -v k="$needle" '$1 == k { print $2; exit }' <<< "$kv"
}

# Build a new block. Args:
#   $1 header line
#   $2 separator line
#   $3 actual_list (newline-separated keys)
#   $4 existing_kv (output of rows_to_kv)
#   $5 number of metadata cells
build_block() {
  local header="$1" sep="$2" actual_list="$3" existing_kv="$4" cells="$5"
  echo "$header"
  echo "$sep"

  local placeholder="_TBD_ (added by sync — please fill)"
  local i extra=""
  for ((i=2; i<=cells; i++)); do
    extra="${extra} | "
  done

  declare -A actual_set=()

  # 1) Iterate actual files in sorted order
  while IFS= read -r k; do
    [ -z "$k" ] && continue
    actual_set["$k"]=1
    local existing
    existing="$(kv_get "$existing_kv" "$k")"
    if [ -n "$existing" ]; then
      echo "| $k | ${existing//|/ | } |"
    else
      echo "| $k | $placeholder${extra}|"
    fi
  done <<< "$actual_list"

  # 2) Append rows for entries removed from disk
  while IFS=$'\t' read -r k existing; do
    [ -z "$k" ] && continue
    if [ -z "${actual_set[$k]:-}" ]; then
      case "$existing" in
        *"[REMOVED]"*) ;;
        *) existing="[REMOVED] $existing" ;;
      esac
      echo "| $k | ${existing//|/ | } |"
    fi
  done <<< "$existing_kv"
}

# ──────────────────────────────────────────────────────────────────────
# Discover entries on disk for each kind
# ──────────────────────────────────────────────────────────────────────

actual_tokens=""
[ -d "$LIB_DIR/tokens" ] && actual_tokens=$(cd "$LIB_DIR/tokens" \
  && find . -maxdepth 1 -type f -name '*.css' | sed 's|^\./||' | LC_ALL=C sort)

actual_blocks=""
[ -d "$LIB_DIR/blocks" ] && actual_blocks=$(cd "$LIB_DIR/blocks" \
  && find . -maxdepth 2 -type f -name 'block.html' \
  | sed 's|^\./||;s|/block\.html$|/|' | LC_ALL=C sort)

actual_components=""
[ -d "$LIB_DIR/components" ] && actual_components=$(cd "$LIB_DIR/components" \
  && find . -maxdepth 2 -type f -name 'component.html' \
  | sed 's|^\./||;s|/component\.html$|/|' | LC_ALL=C sort)

actual_effects=""
[ -d "$LIB_DIR/effects" ] && actual_effects=$(cd "$LIB_DIR/effects" \
  && find . -maxdepth 1 -type f -name '*.js' | sed 's|^\./||' | LC_ALL=C sort)

actual_styles=""
[ -d "$LIB_DIR/visual-styles" ] && actual_styles=$(cd "$LIB_DIR/visual-styles" \
  && find . -maxdepth 1 -type f -name '*.md' | sed 's|^\./||' | LC_ALL=C sort)

# ──────────────────────────────────────────────────────────────────────
# Parse existing tables → KV blobs
# ──────────────────────────────────────────────────────────────────────

KV_TOKENS=$(rows_to_kv "$(extract_block "$TOKENS_BEGIN" "$TOKENS_END")")
KV_BLOCKS=$(rows_to_kv "$(extract_block "$BLOCKS_BEGIN" "$BLOCKS_END")")
KV_COMPONENTS=$(rows_to_kv "$(extract_block "$COMPONENTS_BEGIN" "$COMPONENTS_END")")
KV_EFFECTS=$(rows_to_kv "$(extract_block "$EFFECTS_BEGIN" "$EFFECTS_END")")
KV_STYLES=$(rows_to_kv "$(extract_block "$STYLES_BEGIN" "$STYLES_END")")

# ──────────────────────────────────────────────────────────────────────
# Build new tables
# ──────────────────────────────────────────────────────────────────────

NEW_TOKENS=$(build_block \
  "| File | Description | Tags |" \
  "|---|---|---|" \
  "$actual_tokens" \
  "$KV_TOKENS" \
  2)

NEW_BLOCKS=$(build_block \
  "| Directory | Description | Dimensions | Tags |" \
  "|---|---|---|---|" \
  "$actual_blocks" \
  "$KV_BLOCKS" \
  3)

NEW_COMPONENTS=$(build_block \
  "| Directory | Description | Tags |" \
  "|---|---|---|" \
  "$actual_components" \
  "$KV_COMPONENTS" \
  2)

NEW_EFFECTS=$(build_block \
  "| File | Description | Tags |" \
  "|---|---|---|" \
  "$actual_effects" \
  "$KV_EFFECTS" \
  2)

NEW_STYLES=$(build_block \
  "| File | Description | Tags |" \
  "|---|---|---|" \
  "$actual_styles" \
  "$KV_STYLES" \
  2)

# ──────────────────────────────────────────────────────────────────────
# Splice and detect change
# ──────────────────────────────────────────────────────────────────────

tmp="${MANIFEST_MD}.tmp.$$"
awk -v t_begin="$TOKENS_BEGIN" -v t_end="$TOKENS_END" -v t_block="$NEW_TOKENS" \
    -v b_begin="$BLOCKS_BEGIN" -v b_end="$BLOCKS_END" -v b_block="$NEW_BLOCKS" \
    -v c_begin="$COMPONENTS_BEGIN" -v c_end="$COMPONENTS_END" -v c_block="$NEW_COMPONENTS" \
    -v e_begin="$EFFECTS_BEGIN" -v e_end="$EFFECTS_END" -v e_block="$NEW_EFFECTS" \
    -v s_begin="$STYLES_BEGIN" -v s_end="$STYLES_END" -v s_block="$NEW_STYLES" '
{
  if      ($0 == t_begin) { print; print t_block; skipping = 1; next }
  else if ($0 == t_end)   { skipping = 0; print; next }
  else if ($0 == b_begin) { print; print b_block; skipping = 1; next }
  else if ($0 == b_end)   { skipping = 0; print; next }
  else if ($0 == c_begin) { print; print c_block; skipping = 1; next }
  else if ($0 == c_end)   { skipping = 0; print; next }
  else if ($0 == e_begin) { print; print e_block; skipping = 1; next }
  else if ($0 == e_end)   { skipping = 0; print; next }
  else if ($0 == s_begin) { print; print s_block; skipping = 1; next }
  else if ($0 == s_end)   { skipping = 0; print; next }
  else if (!skipping)     { print }
}
' "$MANIFEST_MD" > "$tmp"

if cmp -s "$tmp" "$MANIFEST_MD"; then
  rm -f "$tmp"
  exit 0
fi

mv "$tmp" "$MANIFEST_MD"
echo "[sync-shared-lib] Updated $MANIFEST_MD"
