#!/usr/bin/env bash
# Marca o dia de hoje como feito, SOMANDO ao que ja estava registrado.
#   ./feito.sh 45 34         -> +45 questoes, +34 acertos
#   ./feito.sh               -> so marca presenca
#   ./feito.sh --set 45 34   -> substitui (corrige um registro errado)
#
# Somar e o padrao porque estudar em duas sessoes no mesmo dia e o caso comum:
# a versao antiga sobrescrevia, entao rodar de manha e de novo a noite jogava
# fora a sessao da manha sem avisar.
set -euo pipefail
cd "$(dirname "$0")"

MODO=somar
if [ "${1:-}" = "--set" ]; then MODO=set; shift; fi
Q="${1:-0}"; A="${2:-0}"; HOJE=$(date +%F)

python3 - "$HOJE" "$Q" "$A" "$MODO" <<'PY'
import csv, sys
hoje, q, a, modo = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rows = list(csv.DictReader(open("progresso.csv")))
ok = False
for r in rows:
    if r["data"] == hoje:
        antes_q, antes_a = int(r["questoes"] or 0), int(r["acertos"] or 0)
        if modo == "somar":
            novo_q, novo_a = antes_q + q, antes_a + a
        else:
            novo_q, novo_a = q, a
        r["questoes"], r["acertos"], r["feito"] = str(novo_q), str(novo_a), "1"
        ok = True
        if modo == "somar" and antes_q:
            print(f"  {hoje}: +{q}q / +{a} acertos  (total do dia: {novo_q}q / {novo_a})")
        else:
            print(f"  {hoje} marcado: {novo_q}q / {novo_a} acertos")
        print(f"  foco: {r['foco']}")
if not ok:
    print(f"  {hoje} nao esta no roteiro (fim de semana extra? prova ja passou?)")
    sys.exit(0)
# lineterminator="\n": o csv escreve CRLF por padrao, e o progresso.csv e LF.
# Sem isso, marcar UM dia reescrevia as 92 linhas do arquivo e o diff do commit
# virava o arquivo inteiro.
with open("progresso.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys(), lineterminator="\n")
    w.writeheader(); w.writerows(rows)
PY
