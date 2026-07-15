#!/usr/bin/env python3
"""Preenche o gabarito oficial das questoes em banco-provas.json.

Uso:
    ./gabarito.py dataprev2024 "1-C 2-A 3-E 4-C ..."
    ./gabarito.py dataprev2024 --arquivo gabarito-dataprev2024.txt
    ./gabarito.py --falta                    mostra o que ainda esta sem gabarito

Aceita varios formatos, entao voce pode colar quase como vier do site da FGV:
    1-C 2-A 3-E        1 C 2 A 3 E        01-C, 02-A, 03-E        C A E (em ordem)

IMPORTANTE: use o gabarito OFICIAL da banca. Gabarito chutado treina o reflexo
errado, que e pior do que nao treinar.
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
BANCO = BASE / "banco-provas.json"
LETRAS = "ABCDE"


def carregar():
    if not BANCO.exists():
        sys.exit("  banco-provas.json nao existe. Rode ./importar_provas.py antes.")
    return json.loads(BANCO.read_text(encoding="utf-8"))


def parsear_gabarito(texto, nums_validos):
    """Devolve {numero: indice_da_letra}. Aceita '1-C', '1 C', ou so 'C A E'."""
    pares = re.findall(r"(\d{1,2})\s*[-.:)]?\s*([A-Ea-e])\b", texto)
    if pares:
        return {int(n): LETRAS.index(l.upper()) for n, l in pares}

    # sem numeros: assume sequencia na ordem das questoes da prova
    letras = re.findall(r"\b([A-Ea-e])\b", texto)
    if not letras:
        sys.exit("  nao consegui ler nenhuma resposta nesse texto.")
    ordenados = sorted(nums_validos)
    if len(letras) != len(ordenados):
        sys.exit(
            f"  {len(letras)} respostas para {len(ordenados)} questoes. "
            "Sem numeracao eu nao sei alinhar — use o formato '1-C 2-A ...'."
        )
    return {n: LETRAS.index(l.upper()) for n, l in zip(ordenados, letras)}


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return

    banco = carregar()

    if args[0] == "--falta":
        from collections import defaultdict

        d = defaultdict(list)
        for q in banco:
            if q["ans"] is None:
                d[q["prova"]].append(q["num"])
        print()
        if not d:
            print("  todas as questoes tem gabarito.\n")
            return
        for prova, nums in sorted(d.items()):
            print(f"  {prova}: {len(nums)} sem gabarito  (Q{min(nums)}–Q{max(nums)})")
        print()
        return

    prova = args[0]
    desta = [q for q in banco if q["prova"] == prova]
    if not desta:
        provas = sorted({q["prova"] for q in banco})
        sys.exit(f"  prova '{prova}' nao encontrada. Disponiveis: {', '.join(provas)}")

    if len(args) > 2 and args[1] == "--arquivo":
        texto = Path(args[2]).read_text(encoding="utf-8")
    elif len(args) > 1:
        texto = " ".join(args[1:])
    else:
        print(f"  cole o gabarito de {prova} e termine com Ctrl-D:")
        texto = sys.stdin.read()

    nums_validos = {q["num"] for q in desta}
    respostas = parsear_gabarito(texto, nums_validos)

    fora = set(respostas) - nums_validos
    if fora:
        print(f"  aviso: questoes {sorted(fora)} nao existem em {prova} (ignoradas)")

    n = 0
    for q in desta:
        if q["num"] in respostas:
            q["ans"] = respostas[q["num"]]
            n += 1

    BANCO.write_text(json.dumps(banco, ensure_ascii=False, indent=1), encoding="utf-8")

    falta = [q["num"] for q in desta if q["ans"] is None]
    print(f"\n  {prova}: {n} gabaritos preenchidos.")
    if falta:
        print(f"  ainda sem gabarito: {falta}")
    else:
        print("  prova completa — ja da pra rodar ./quiz.py --prova " + prova)
    print()


if __name__ == "__main__":
    main()
