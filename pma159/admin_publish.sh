#!/bin/bash
# Publish the current data/app to GitHub Pages (repo asad-data cloned at /home/user/asad-data).
# Unchanged categories (same data + same password) stay byte-identical, so users only re-download what changed.
# usage: ./admin_publish.sh "commit message"
set -e
cd "$(dirname "$0")"
R=/home/user/asad-data
PREV=$R ./publish_build.sh
cd $R && find . -mindepth 1 -maxdepth 1 ! -name .git ! -name README.md -exec rm -rf {} +
cp -a /tmp/publish/. $R/ && git add -A
git diff --cached --quiet && { echo "nothing changed"; exit 0; }
git commit -q -m "${1:-Update app/data}"$'\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01DV24NYK3695QRHbm9zQ9dR'
git push -q origin HEAD:main && echo "pushed: users see the change at their next launch (GitHub Pages needs 1-5 minutes)"
