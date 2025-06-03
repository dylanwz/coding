#!/bin/bash

# Usage: ./scripts/solve.sh <filename> <difficulty>
# Example: ./scripts/solve.sh problems/123_two_sum.py 4

set -e

FILENAME="$1"
DIFFICULTY="${2:-3}"

if [ -z "$FILENAME" ]; then
  echo "Please follow usage: $0 <problem_file> <difficulty (0-5)>"
  exit 1
fi

if ! [[ "$DIFFICULTY" =~ ^[0-5]$ ]]; then
  echo "❌ Difficulty must be an integer from 0 to 5"
  exit 1
fi

# Commit message: "add 123_two_sum.py [difficulty: 4]"
COMMIT_MSG="did $FILENAME [difficulty: $DIFFICULTY]"

# Git add, commit, push
git add .
git commit -m "$COMMIT_MSG"
git push

# Update revision schedule
revise add "$FILENAME" 2>/dev/null || echo "⚠️ Already tracked in revision."
revise update "$FILENAME" "$DIFFICULTY"

echo "✅ Done: committed and updated spaced repetition tracker"
