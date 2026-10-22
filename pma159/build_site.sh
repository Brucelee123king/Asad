#!/bin/bash
# Builds the locked online system into DIST (default /tmp/dist): index.html (shell without MCQs), data/<cat>.json (encrypted), lock.json
# usage: ./build_site.sh [base_url]   (default base = the GitHub Pages address)
# passwords: /home/user/keystore/section_passwords.json (NOT in git; keep it safe)
set -e
cd "$(dirname "$0")"
BASE=${1:-https://brucelee123king.github.io/asad-data/}
DIST=${DIST:-/tmp/dist}
PW=${SEC_PW:-/home/user/keystore/section_passwords.json}
python3 merge_into_site.py base_original_site.html /tmp/plain_index.html
NODE_PATH=$(npm root -g) node dump_all.js /tmp/plain_index.html /tmp/all_dump.json
mkdir -p "$DIST"
python3 lock_sections.py /tmp/plain_index.html /tmp/all_dump.json "$PW" "$DIST" "$BASE" ${PREV:+"$PREV"}
cp "$DIST/index.html" ../site/index.html
