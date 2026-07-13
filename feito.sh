#!/usr/bin/env bash
# Marca o dia de hoje como feito.
#   ./feito.sh 45 34     -> 45 questoes, 34 acertos
#   ./feito.sh           -> so marca presenca
set -euo pipefail
cd "$(dirname "$0")"
Q="${1:-0}"; A="${2:-0}"; HOJE=$(date +%F)

python3 - "$HOJE" "$Q" "$A" <<'PY'
import csv, sys
hoje, q, a = sys.argv[1], sys.argv[2], sys.argv[3]
rows = list(csv.DictReader(open("progresso.csv")))
ok = False
for r in rows:
    if r["data"] == hoje:
        r["questoes"], r["acertos"], r["feito"] = q, a, "1"
        ok = True
        print(f"  {hoje} marcado: {q}q / {a} acertos")
        print(f"  foco: {r['foco']}")
if not ok:
    print(f"  {hoje} nao esta no roteiro (fim de semana extra? prova ja passou?)")
    sys.exit(0)
with open("progresso.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)
PY
