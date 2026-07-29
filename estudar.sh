#!/usr/bin/env bash
# Abre o(s) capitulo(s) da apostila em janela(s) do zathura (via apostila.py,
# WSLg) e roda o quiz no terminal atual.
#
#   ./estudar.sh                 --hoje no quiz, capitulos do dia na apostila
#   ./estudar.sh java            ./quiz.py java  +  apostila.py java
#   ./estudar.sh java redes -n 15   blocos passam pros dois; -n so pro quiz
#   ./estudar.sh --simulado      sem bloco -> apostila cai no plano de hoje
#   ./estudar.sh --dia ontem     recupera outro dia nos dois (--quem idem)
set -euo pipefail
cd "$(dirname "$0")"

QUIZ_ARGS=("$@")
BLOCOS=()
APOSTILA_FLAGS=()
esperando=""
for a in "$@"; do
    if [ -n "$esperando" ]; then
        [ "$esperando" = apostila ] && APOSTILA_FLAGS+=("$a")
        esperando=""
        continue
    fi
    case "$a" in
        --dia|--quem)
            APOSTILA_FLAGS+=("$a")
            esperando=apostila
            ;;
        -n|--prova)
            esperando=quiz
            ;;
        --*) ;;
        *) BLOCOS+=("$a") ;;
    esac
done
[ ${#BLOCOS[@]} -eq 0 ] && BLOCOS=(hoje)

./apostila.py "${APOSTILA_FLAGS[@]}" "${BLOCOS[@]}"

if [ ${#QUIZ_ARGS[@]} -eq 0 ]; then
    exec ./quiz.py --hoje
else
    exec ./quiz.py "${QUIZ_ARGS[@]}"
fi
