#!/usr/bin/env python3
"""Quiz de terminal — banco de questoes estilo FGV para o Dataprev 2026.

Uso:
    ./quiz.py                    10 questoes aleatorias de todos os blocos
    ./quiz.py java               so do bloco java
    ./quiz.py java redes -n 15   15 questoes desses dois blocos
    ./quiz.py --hoje             questoes do bloco previsto no roteiro para hoje
    ./quiz.py --erradas          refaz apenas as que voce ja errou
    ./quiz.py --tags             lista os blocos disponiveis
    ./quiz.py --stats            desempenho acumulado por bloco

Ao final, oferece registrar o resultado no progresso.csv (soma ao dia de hoje)
e grava automaticamente as erradas em historico.json para o modo --erradas.
"""

import argparse
import csv
import json
import random
import sys
import textwrap
from datetime import date, datetime
from pathlib import Path

BASE = Path(__file__).parent
BANCO = BASE / "banco.json"
HIST = BASE / "historico.json"
CSV = BASE / "progresso.csv"

C = {"r": "\033[0m", "b": "\033[1m", "dim": "\033[2m",
     "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "ciano": "\033[36m"}


def cor(t, c):
    return f"{C[c]}{t}{C['r']}"


def wrap(t, indent="  "):
    return textwrap.fill(t, width=76, initial_indent=indent, subsequent_indent=indent)


def carregar_banco():
    with open(BANCO, encoding="utf-8") as f:
        banco = json.load(f)
    for i, q in enumerate(banco):
        q["id"] = i
    return banco


def carregar_hist():
    if HIST.exists():
        return json.loads(HIST.read_text(encoding="utf-8"))
    return {"respostas": []}


def salvar_hist(h):
    HIST.write_text(json.dumps(h, ensure_ascii=False, indent=1), encoding="utf-8")


def tag_de_hoje():
    """Le o progresso.csv e devolve a tag do dia atual, se houver."""
    if not CSV.exists():
        return None
    hoje = date.today().isoformat()
    with open(CSV, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            if l["data"] == hoje:
                t = l["tag"]
                return t if t not in {"revisao", "simulado", "descanso", "prova"} else None
    return None


def registrar_no_csv(qtd, acertos):
    """Soma o resultado da sessao ao dia de hoje no progresso.csv."""
    if not CSV.exists():
        print(cor("  progresso.csv nao encontrado; nada registrado.", "dim"))
        return
    hoje = date.today().isoformat()
    with open(CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        campos = rows and list(rows[0].keys())
    achou = False
    for r in rows:
        if r["data"] == hoje:
            r["questoes"] = str(int(r["questoes"]) + qtd)
            r["acertos"] = str(int(r["acertos"]) + acertos)
            r["feito"] = "1"
            achou = True
    if not achou:
        print(cor("  hoje nao esta no roteiro; nada registrado.", "dim"))
        return
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(rows)
    print(cor(f"  registrado: +{qtd} questoes, +{acertos} acertos no dia de hoje.", "verde"))


def rodar(questoes):
    total = len(questoes)
    acertos = 0
    erradas = []
    letras = "ABCDE"

    print()
    print(cor(f"  {total} questoes. Responda com a letra (A-E). 'q' abandona.", "dim"))
    print()

    for n, q in enumerate(questoes, 1):
        # embaralha alternativas preservando qual e a correta
        ordem = list(range(5))
        random.shuffle(ordem)
        correta_pos = ordem.index(q["ans"])

        print(cor(f"  Questao {n}/{total}", "b"), cor(f"[{q['tag']}]", "ciano"))
        print(wrap(q["q"]))
        print()
        for i, oi in enumerate(ordem):
            print(wrap(q["alts"][oi], indent=f"    {letras[i]}) "))
        print()

        while True:
            r = input("  > ").strip().upper()
            if r == "Q":
                print(cor("\n  sessao abandonada.\n", "dim"))
                return None
            if r in letras:
                break
            print(cor("  responda A, B, C, D, E ou q", "dim"))

        escolhida = letras.index(r)
        if escolhida == correta_pos:
            acertos += 1
            print(cor("  CERTO.", "verde"), end=" ")
        else:
            erradas.append(q)
            print(cor(f"  ERRADO. Correta: {letras[correta_pos]}", "verm"), end=" ")
        print(cor(q["why"], "dim"))
        print()

    return acertos, erradas


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("tags", nargs="*")
    p.add_argument("-n", type=int, default=10)
    p.add_argument("--hoje", action="store_true")
    p.add_argument("--erradas", action="store_true")
    p.add_argument("--tags", dest="listar", action="store_true")
    p.add_argument("--stats", action="store_true")
    p.add_argument("-h", "--help", action="store_true")
    a = p.parse_args()

    if a.help:
        print(__doc__)
        return

    banco = carregar_banco()
    hist = carregar_hist()

    if a.listar:
        from collections import Counter
        c = Counter(q["tag"] for q in banco)
        print()
        for t, n in sorted(c.items()):
            print(f"  {t:<16} {n} questoes")
        print(f"\n  total: {len(banco)}\n")
        return

    if a.stats:
        from collections import defaultdict
        d = defaultdict(lambda: [0, 0])
        for r in hist["respostas"]:
            d[r["tag"]][0] += 1
            d[r["tag"]][1] += r["ok"]
        print()
        if not d:
            print(cor("  nenhuma sessao registrada ainda.\n", "dim"))
            return
        print(cor("  Desempenho acumulado no quiz", "b"))
        for t, (tot, ok) in sorted(d.items(), key=lambda x: x[1][1] / x[1][0]):
            pct = ok / tot * 100
            c = "verde" if pct >= 75 else "ama" if pct >= 60 else "verm"
            print(f"    {t:<16} {cor(f'{pct:>3.0f}%', c)}  ({ok}/{tot})")
        print()
        return

    # selecao de questoes
    if a.erradas:
        ids_erradas = {r["id"] for r in hist["respostas"] if not r["ok"]}
        pool = [q for q in banco if q["id"] in ids_erradas]
        if not pool:
            print(cor("\n  nenhuma questao errada registrada. Otimo sinal.\n", "verde"))
            return
    elif a.hoje:
        t = tag_de_hoje()
        if t is None:
            print(cor("\n  hoje nao tem bloco de conteudo no roteiro (revisao/simulado?).", "dim"))
            print(cor("  rodando 10 aleatorias de tudo.\n", "dim"))
            pool = banco[:]
        else:
            pool = [q for q in banco if q["tag"] == t]
            print(cor(f"\n  bloco de hoje no roteiro: {t}", "ciano"))
    elif a.tags:
        pool = [q for q in banco if q["tag"] in a.tags]
        if not pool:
            print(cor(f"\n  nenhuma questao com tags {a.tags}. Use --tags para listar.\n", "verm"))
            return
    else:
        pool = banco[:]

    random.shuffle(pool)
    sel = pool[: a.n]

    res = rodar(sel)
    if res is None:
        return
    acertos, erradas = res
    total = len(sel)
    pct = acertos / total * 100

    c = "verde" if pct >= 75 else "ama" if pct >= 60 else "verm"
    print(cor("  " + "-" * 40, "dim"))
    print(f"  Resultado: {cor(f'{acertos}/{total} ({pct:.0f}%)', c)}")

    if erradas:
        print(f"\n  {cor('Anote no caderno de erros:', 'ama')}")
        for arq in sorted({f"erros/{q['tag']}.md" for q in erradas}):
            print(f"    {arq}")

    # persiste historico para --erradas e --stats
    agora = datetime.now().isoformat(timespec="seconds")
    ids_sel = {q["id"] for q in sel}
    ids_err = {q["id"] for q in erradas}
    for q in sel:
        hist["respostas"].append(
            {"id": q["id"], "tag": q["tag"], "ok": q["id"] not in ids_err, "quando": agora}
        )
    salvar_hist(hist)

    print()
    r = input("  registrar no progresso.csv? [S/n] ").strip().lower()
    if r in ("", "s", "sim"):
        registrar_no_csv(total, acertos)
    print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(cor("\n\n  interrompido.\n", "dim"))
        sys.exit(0)
