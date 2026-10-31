#!/bin/bash
# Full build: locked shell + encrypted data -> android www -> /tmp/publish (what goes to GitHub Pages) ; also updates android-app/app/src/main/assets/www
# usage: ./publish_build.sh [base_url]     (PREV=<published dir> keeps unchanged categories byte-identical)
set -e
cd "$(dirname "$0")"
BASE=${1:-https://brucelee123king.github.io/asad-data/}
export DIST=/tmp/dist
rm -rf "$DIST"; ./build_site.sh "$BASE"
cp ../site/index.html ../android-app/source/index.html
(cd ../android-app && python3 tools/build_web.py /tmp/tw >/dev/null)
rm -rf /tmp/shellout; mkdir -p /tmp/shellout; python3 sign_shell.py ../android-app/app/src/main/assets/www/index.html /tmp/shellout "$BASE" "${PREV:-}"
rm -rf /tmp/publish; mkdir -p /tmp/publish
cp -r ../android-app/app/src/main/assets/www/. /tmp/publish/
cp -r "$DIST/data" /tmp/publish/data; cp "$DIST/lock.json" /tmp/publish/lock.json; cp "$DIST/admin.html" /tmp/publish/admin.html; cp /tmp/shellout/shell.html /tmp/shellout/shell.json /tmp/publish/; touch /tmp/publish/.nojekyll
echo "publish folder ready: /tmp/publish"; du -sh /tmp/publish
