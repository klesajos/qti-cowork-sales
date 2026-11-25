#!/usr/bin/env bash
# Zips plugins/quanti-sales into dist/quanti-sales.zip for upload in Claude
# (Customize > Plugins > Upload, or Organization settings > Plugins & skills > Add > Upload a plugin).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/quanti-sales.zip
(cd plugins && zip -qr -X ../dist/quanti-sales.zip quanti-sales -x '*.DS_Store')
unzip -l dist/quanti-sales.zip | grep -c 'SKILL.md' | xargs -I{} echo "dist/quanti-sales.zip: {} skills"
