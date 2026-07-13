#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
git add -A
git commit -m "estudo $(date +%d/%m)" || { echo "nada a commitar"; exit 0; }
git push 2>/dev/null || echo "(sem remote configurado ainda)"
