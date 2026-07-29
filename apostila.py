#!/usr/bin/env python3
"""Abre o(s) capitulo(s) da apostila (apostila/main.pdf) que correspondem a um
bloco, no PDF de verdade (zathura), ja na pagina inicial do capitulo —
pensado pra rodar ao lado do quiz (veja estudar.sh).

Uso:
    ./apostila.py java           abre o PDF (zathura) no Cap. 10 (Java)
    ./apostila.py java redes     abre uma janela por capitulo, nessa ordem
    ./apostila.py hoje           capitulos dos blocos do plano de hoje
    ./apostila.py --quem geys hoje

Descobre a pagina inicial de cada capitulo lendo o cabecalho de pagina do PDF
("Capitulo N ... Dataprev 2026 — Perfil 3") via pdftotext, entao nao depende
de numero de pagina fixo — sobrevive a recompilacao do latex. A exibicao em
si e o zathura renderizando o PDF (--fork: cada janela e independente do
processo deste script), sem extracao de texto — sem quebra de coluna/negrito.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
PDF = BASE / "apostila" / "main.pdf"

sys.path.insert(0, str(BASE))
from quiz import APOSTILA, _alvos  # noqa: E402


def mapa_paginas():
    """cap (int) -> (pagina_inicial, pagina_final), 1-indexado, fisico no PDF."""
    texto = subprocess.run(
        ["pdftotext", "-layout", str(PDF), "-"],
        capture_output=True, text=True, check=True,
    ).stdout
    paginas = texto.split("\x0c")
    inicio = {}
    for i, pag in enumerate(paginas, start=1):
        m = re.search(r"Cap[ií]tulo\s+(\d+)", pag)
        if m:
            cap = int(m.group(1))
            inicio.setdefault(cap, i)
    total = len(paginas)
    caps = sorted(inicio)
    faixas = {}
    for idx, cap in enumerate(caps):
        fim = (inicio[caps[idx + 1]] - 1) if idx + 1 < len(caps) else total
        faixas[cap] = (inicio[cap], fim)
    return faixas


def resolve_blocos(args, quem):
    blocos = []
    for a in args:
        if a == "hoje":
            blocos.extend(_alvos("hoje", quem))
        else:
            blocos.append(a)
    return blocos


def main():
    p = argparse.ArgumentParser()
    p.add_argument("blocos", nargs="*", default=["hoje"])
    p.add_argument("--quem", default="lucas")
    a = p.parse_args()

    if not PDF.exists():
        sys.exit(f"nao achei {PDF} — compile a apostila primeiro (cd apostila && latexmk -pdf main.tex)")

    blocos = resolve_blocos(a.blocos, a.quem.strip().lower())
    if not blocos:
        sys.exit("nenhum bloco pra mostrar (plano de hoje vazio?)")

    faixas = mapa_paginas()

    titulos = {}
    for b in blocos:
        info = APOSTILA.get(b)
        if not info:
            print(f"  aviso: sem capitulo mapeado pra '{b}', pulando.", file=sys.stderr)
            continue
        cap, _arq, titulo = info
        titulos.setdefault(cap, titulo)

    if not titulos:
        sys.exit("nenhum dos blocos pedidos tem capitulo mapeado na apostila.")

    for cap, titulo in titulos.items():
        if cap not in faixas:
            print(f"  aviso: nao achei o Cap. {cap} no PDF, pulando.", file=sys.stderr)
            continue
        ini, _fim = faixas[cap]
        print(f"abrindo Cap. {cap} — {titulo}  (pagina {ini} do PDF) no zathura")
        subprocess.Popen(
            ["zathura", "--fork", "-P", str(ini), str(PDF)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )


if __name__ == "__main__":
    main()
