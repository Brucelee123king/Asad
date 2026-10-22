#!/bin/bash
# Builds the locked site: merge (plain, not saved in the repo) -> dump -> encrypt every category with its password -> ../site/index.html
# passwords: /home/user/keystore/section_passwords.json  (keep it safe; ask the user if it is lost)
set -e
cd "$(dirname "$0")"
PW=${SEC_PW:-/home/user/keystore/section_passwords.json}
python3 merge_into_site.py base_original_site.html /tmp/plain_index.html
NODE_PATH=$(npm root -g) node dump_all.js /tmp/plain_index.html /tmp/all_dump.json
python3 lock_sections.py /tmp/plain_index.html /tmp/all_dump.json "$PW" ../site/index.html
