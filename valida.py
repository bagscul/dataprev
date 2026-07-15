#!/usr/bin/env python3
"""Valida a integridade dos bancos de questoes. Rode sempre que adicionar
questoes (geradas em banco.json, ou de prova via ./importar_provas.py) para
garantir que o quiz nao vai quebrar nem servir questao capenga.

Uso:
    ./valida.py            valida os dois bancos
    ./valida.py --strict   idem, mas sai com erro se houver QUALQUER aviso

Erros (bloqueiam): estrutura quebrada — sem enunciado, sem 5 alternativas,
ans fora de 0-4, chaves de 'erradas' que nao batem com o gabarito.
Avisos (nao bloqueiam): questao usavel sem explicacao ('why'/'erradas'); o
quiz ainda roda, so nao mostra o comentario.
"""

import json
import sys
from pathlib import Path

BASE = Path(__file__).parent
C = {"r": "\033[0m", "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "b": "\033[1m"}


def cor(t, c):
    return f"{C[c]}{t}{C['r']}"


def checar_questao(q, rotulo, usavel):
    """Retorna (erros, avisos) para uma questao. 'usavel' = deveria estar
    pronta pro quiz (com gabarito, nao anulada, sem figura perdida)."""
    erros, avisos = [], []
    if not q.get("q", "").strip():
        erros.append(f"{rotulo}: enunciado vazio")
    alts = q.get("alts")
    if not isinstance(alts, list) or len(alts) != 5:
        erros.append(f"{rotulo}: precisa de exatamente 5 alternativas (tem {len(alts) if isinstance(alts, list) else '?'})")
        return erros, avisos  # sem 5 alts nao da pra checar o resto
    if any(not str(a).strip() for a in alts):
        erros.append(f"{rotulo}: alternativa vazia")
    if not q.get("tag"):
        erros.append(f"{rotulo}: sem 'tag' (bloco)")
    ans = q.get("ans")
    if ans is not None and (not isinstance(ans, int) or not 0 <= ans <= 4):
        erros.append(f"{rotulo}: ans={ans!r} fora de 0-4")

    if usavel and isinstance(ans, int):
        esperado = {str(j) for j in range(5) if j != ans}
        er = q.get("erradas") or {}
        if er:  # se tem explicacao das erradas, tem que bater com o gabarito
            if set(er) != esperado:
                erros.append(f"{rotulo}: chaves de 'erradas' {sorted(er)} != esperado {sorted(esperado)}")
            for k, v in er.items():
                if not str(v).strip():
                    erros.append(f"{rotulo}: explicacao da alt {k} vazia")
        if not q.get("why", "").strip():
            avisos.append(f"{rotulo}: usavel mas sem 'why' (o quiz roda, so nao explica)")
        if not er:
            avisos.append(f"{rotulo}: usavel mas sem 'erradas' (idem)")

    # questao que nao entra no sorteio nao pode machucar o aluno: problema
    # estrutural nela (ex: figura perdida na extracao) vira aviso, nao erro.
    if not usavel:
        return [], avisos + [e.replace(": ", ": [fora do sorteio] ", 1) for e in erros]
    return erros, avisos


def main():
    strict = "--strict" in sys.argv
    erros, avisos = [], []
    n_orig = n_prova = n_usaveis = 0

    # banco original
    bo = BASE / "banco.json"
    if bo.exists():
        banco = json.loads(bo.read_text(encoding="utf-8"))
        n_orig = len(banco)
        vistos = set()
        for i, q in enumerate(banco):
            e, a = checar_questao(q, f"banco.json #{i} [{q.get('tag','?')}]", usavel=True)
            erros += e
            avisos += a
            n_usaveis += 1
    else:
        avisos.append("banco.json nao existe")

    # banco de provas
    bp = BASE / "banco-provas.json"
    if bp.exists():
        provas = json.loads(bp.read_text(encoding="utf-8"))
        n_prova = len(provas)
        chaves = set()
        for q in provas:
            ch = (q.get("prova"), q.get("num"))
            if ch in chaves:
                erros.append(f"banco-provas.json: ({ch[0]} Q{ch[1]}) duplicada")
            chaves.add(ch)
            usavel = (q.get("ans") is not None and not q.get("requer_imagem")
                      and not q.get("anulada"))
            rot = f"banco-provas.json {q.get('prova')} Q{q.get('num')} [{q.get('tag','?')}]"
            e, a = checar_questao(q, rot, usavel=usavel)
            erros += e
            avisos += a
            if usavel:
                n_usaveis += 1

    print()
    print(cor(f"  banco.json: {n_orig} questoes | banco-provas.json: {n_prova} questoes", "b"))
    print(f"  utilizaveis no quiz: {n_usaveis}")
    print()
    if erros:
        print(cor(f"  {len(erros)} ERRO(S) — bloqueiam o quiz:", "verm"))
        for x in erros[:40]:
            print("   ", x)
        if len(erros) > 40:
            print(f"    ... e mais {len(erros) - 40}")
    if avisos:
        print(cor(f"  {len(avisos)} aviso(s) — quiz roda, sem explicacao:", "ama"))
        for x in avisos[:15]:
            print("   ", x)
        if len(avisos) > 15:
            print(f"    ... e mais {len(avisos) - 15}")
    if not erros and not avisos:
        print(cor("  tudo integro.", "verde"))
    print()

    if erros or (strict and avisos):
        sys.exit(1)


if __name__ == "__main__":
    main()
