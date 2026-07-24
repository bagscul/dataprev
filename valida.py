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

import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).parent
C = {"r": "\033[0m", "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "b": "\033[1m"}

# Vocabulario do campo opcional 'status' (auditoria Bloco V). Ausencia = 'ok'
# implicito (questao nao marcada). Presente, tem que ser um destes valores.
STATUS_VALIDOS = {"ok", "revisar", "ambigua", "distrator-fraco",
                  "explicacao-fraca", "estilo-divergente"}


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

    # campo opcional 'apostila' (secao do capitulo, ex. '§3.4') — se presente,
    # tem que ser texto nao-vazio; ausencia e ok (degrada pra Cap. N no quiz).
    ap = q.get("apostila")
    if ap is not None and (not isinstance(ap, str) or not ap.strip()):
        avisos.append(f"{rotulo}: campo 'apostila' presente mas vazio/invalido (esperado ex. '§3.4')")

    # campo opcional 'status' (marcacao da auditoria, Bloco V) — se presente,
    # tem que ser um dos valores permitidos; ausencia e ok (equivale a 'ok', sem
    # marcacao). Nao bloqueia o quiz; so sinaliza valor fora do vocabulario.
    st = q.get("status")
    if st is not None and st not in STATUS_VALIDOS:
        avisos.append(f"{rotulo}: campo 'status' = {st!r} invalido "
                      f"(esperado {sorted(STATUS_VALIDOS)} ou ausente)")

    # questao que nao entra no sorteio nao pode machucar o aluno: problema
    # estrutural nela (ex: figura perdida na extracao) vira aviso, nao erro.
    if not usavel:
        return [], avisos + [e.replace(": ", ": [fora do sorteio] ", 1) for e in erros]
    return erros, avisos


# --- Checagens 8.1 (vazamento de forma) — avisos automaticos, nao bloqueiam.
# Miram questoes novas geradas por IA: um gerador que "vaza a forma" faz a
# correta ser sempre a mais longa, poe absoluto so no distrator, ou concentra
# o gabarito numa posicao. Rodam so no banco.json (o banco-provas e real). ---
ABS_TERMOS = ["sempre", "nunca", "exclusivamente", "apenas", "somente", "todo",
              "toda", "todos", "todas", "invariavelmente", "garante", "garantem",
              "impossivel", "estritamente", "jamais", "qualquer"]


def _norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _tem_absoluto(s):
    t = _norm(s)
    return any(re.search(r"\b" + re.escape(a) + r"\b", t) for a in ABS_TERMOS)


def avisos_forma(banco):
    """Retorna avisos de forma (nao bloqueiam) sobre o banco original."""
    n = len(banco)
    if not n:
        return []
    linhas = []
    dist = collections.Counter(q.get("ans") for q in banco if isinstance(q.get("ans"), int))
    if dist:
        k = max(dist, key=dist.get)
        if dist[k] / n > 0.35:
            linhas.append(f"gabarito concentrado em '{'ABCDE'[k]}': {dist[k]}/{n} "
                          f"({dist[k]/n*100:.0f}%) — embaralhe a posicao da correta")
    mais_longa = 0
    ratio_alta, abs_so_distr = [], []
    for i, q in enumerate(banco):
        alts, a = q.get("alts"), q.get("ans")
        if not (isinstance(alts, list) and len(alts) == 5 and isinstance(a, int)):
            continue
        cl = len(alts[a])
        wl = [len(x) for j, x in enumerate(alts) if j != a]
        if wl and cl > max(wl):
            mais_longa += 1
        if wl and cl / (sum(wl) / len(wl)) >= 1.8:
            ratio_alta.append(i)
        if not _tem_absoluto(alts[a]) and any(_tem_absoluto(x) for j, x in enumerate(alts) if j != a):
            abs_so_distr.append(i)
    if mais_longa / n > 0.30:
        linhas.append(f"correta e a mais longa em {mais_longa}/{n} ({mais_longa/n*100:.0f}%) "
                      f"— alongue distratores ou encurte a correta (esperado ~20%)")
    if ratio_alta:
        ex = ", ".join(f"#{i}" for i in ratio_alta[:8]) + (" ..." if len(ratio_alta) > 8 else "")
        linhas.append(f"correta >=1.8x a media das erradas em {len(ratio_alta)} questao(oes): {ex}")
    if len(abs_so_distr) / n > 0.15:
        ex = ", ".join(f"#{i}" for i in abs_so_distr[:8]) + (" ..." if len(abs_so_distr) > 8 else "")
        linhas.append(f"termo absoluto SO em distrator em {len(abs_so_distr)}/{n} "
                      f"({len(abs_so_distr)/n*100:.0f}%): {ex}")
    return linhas


CAUSAS_VALIDAS = {"conceitual", "armadilha"}


def checar_historico():
    """Checagem leve dos historico*.json (progresso do quiz por pessoa). O campo
    'causa' e OPCIONAL (so nas erradas em que a pessoa respondeu); dados antigos
    nao tem e isso e normal. So avisa (nao bloqueia) se uma 'causa' gravada tiver
    valor fora de {conceitual, armadilha}."""
    avisos = []
    for h in sorted(BASE.glob("historico*.json")):
        try:
            dados = json.loads(h.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            avisos.append(f"{h.name}: nao consegui ler ({e})")
            continue
        for i, r in enumerate(dados.get("respostas", [])):
            causa = r.get("causa")
            if causa is not None and causa not in CAUSAS_VALIDAS:
                avisos.append(f"{h.name} resposta #{i}: causa={causa!r} invalida "
                              f"(esperado {sorted(CAUSAS_VALIDAS)} ou ausente)")
    return avisos


def main():
    strict = "--strict" in sys.argv
    erros, avisos, avisos_f = [], [], []
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
        avisos_f = avisos_forma(banco)
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

    # progresso do quiz (opcional): so avisa se 'causa' vier com valor invalido
    avisos += checar_historico()

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
    if avisos_f:
        print(cor(f"  {len(avisos_f)} aviso(s) de forma (banco.json) — nao bloqueiam, miram questoes novas:", "ama"))
        for x in avisos_f:
            print("   ", x)
    if not erros and not avisos and not avisos_f:
        print(cor("  tudo integro.", "verde"))
    print()

    if erros or (strict and avisos):
        sys.exit(1)


if __name__ == "__main__":
    main()
