#!/usr/bin/env python3
"""Valida a integridade dos bancos de questoes. Rode sempre que adicionar
questoes (geradas em banco.json, ou de prova via ./importar_provas.py) para
garantir que o quiz nao vai quebrar nem servir questao capenga.

Uso:
    ./valida.py             valida os dois bancos
    ./valida.py --strict    idem, mas sai com erro se houver QUALQUER aviso
                            (inclusive os de forma) — serve de portao pre-commit
    ./valida.py --novas 40  mede o vazamento de forma nas 40 ultimas questoes
                            (padrao: 30), para conferir um lote recem-adicionado

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


# Limiar por ESCOPO. O global e so rede de seguranca: numa banca de 5 alternativas
# sem nivelamento, a correta e a mais longa ~20% das vezes por acaso (alvo declarado
# no CONTRIBUINDO-QUESTOES.md), entao limiar global abaixo disso acenderia aviso em
# banco saudavel. Quem pega REGRESSAO e o escopo pequeno: um lote novo enviesado se
# dilui na media de centenas de questoes (60 questoes 100% enviesadas entrando num
# banco de 331 levam o global a so 18%), mas salta na janela recente e no bloco.
LIMIARES = {
    "global": {"longa": 0.25, "abs": 0.08, "gab": 0.30},
    "bloco":  {"longa": 0.35, "abs": 0.25, "gab": 0.45},
    "janela": {"longa": 0.30, "abs": 0.20, "gab": 0.45},
}
JANELA_PADRAO = 30   # questao nova e sempre anexada ao fim: as N ultimas = lote recente
BLOCO_MIN = 12       # bloco menor que isso nao e medido (flutuacao domina o sinal)
RATIO_LIM = 1.7      # correta / media das erradas, por questao
RATIO_MOSTRA = 5


def _metricas(itens):
    """itens = [(indice_no_banco, questao)]. Retorna None se nao houver questao
    mensuravel; senao (n, frac_mais_longa, frac_abs_so_distrator, (letra, n_letra),
    [indices mais longos], [indices com absoluto so no distrator], [(ratio, i)])."""
    n = 0
    mais_longa, abs_so, ratios = [], [], []
    dist = collections.Counter()
    for i, q in itens:
        alts, a = q.get("alts"), q.get("ans")
        if not (isinstance(alts, list) and len(alts) == 5 and isinstance(a, int)):
            continue
        n += 1
        dist[a] += 1
        cl = len(alts[a])
        wl = [len(x) for j, x in enumerate(alts) if j != a]
        if not wl:
            continue
        if cl > max(wl):
            mais_longa.append(i)
        ratios.append((cl / (sum(wl) / len(wl)), i))
        if not _tem_absoluto(alts[a]) and any(_tem_absoluto(x) for j, x in enumerate(alts) if j != a):
            abs_so.append(i)
    if not n:
        return None
    k = max(dist, key=dist.get)
    return n, len(mais_longa) / n, len(abs_so) / n, (k, dist[k]), mais_longa, abs_so, ratios


def _exemplos(indices, quantos=6):
    ex = ", ".join(f"#{i}" for i in indices[:quantos])
    return ex + (" ..." if len(indices) > quantos else "")


def _checa_escopo(itens, lim, rotulo):
    """Aplica os tres limiares de forma a um escopo (banco, bloco ou janela)."""
    m = _metricas(itens)
    if m is None:
        return []
    n, f_longa, f_abs, (k, n_k), i_longa, i_abs, _ = m
    linhas = []
    if n_k / n > lim["gab"]:
        linhas.append(f"[{rotulo}] gabarito concentrado em '{'ABCDE'[k]}': {n_k}/{n} "
                      f"({n_k/n*100:.0f}%) — embaralhe a posicao da correta")
    if f_longa > lim["longa"]:
        linhas.append(f"[{rotulo}] correta e a mais longa em {len(i_longa)}/{n} "
                      f"({f_longa*100:.0f}%) — alongue distratores ou encurte a correta "
                      f"(esperado ~20%): {_exemplos(i_longa)}")
    if f_abs > lim["abs"]:
        linhas.append(f"[{rotulo}] termo absoluto SO em distrator em {len(i_abs)}/{n} "
                      f"({f_abs*100:.0f}%): {_exemplos(i_abs)}")
    return linhas


def avisos_forma(banco, janela=JANELA_PADRAO):
    """Retorna avisos de forma (nao bloqueiam) sobre o banco original, em tres
    escopos: banco inteiro, cada bloco com n>=BLOCO_MIN e a janela das ultimas
    'janela' questoes (o lote recem-adicionado)."""
    # indice 1-based: e como as questoes sao referidas em todo o resto do repo
    # (#227-#236, #166-#185), e o aviso serve justamente para ir editar a questao
    itens = list(enumerate(banco, 1))
    if not itens:
        return []
    linhas = _checa_escopo(itens, LIMIARES["global"], "banco")

    por_tag = collections.defaultdict(list)
    for i, q in itens:
        por_tag[q.get("tag", "?")].append((i, q))
    for tag in sorted(por_tag):
        if len(por_tag[tag]) >= BLOCO_MIN:
            linhas += _checa_escopo(por_tag[tag], LIMIARES["bloco"], f"bloco {tag}")

    if janela and len(itens) > janela:
        linhas += _checa_escopo(itens[-janela:], LIMIARES["janela"],
                                f"ultimas {janela}")

    # ratio individual: sempre medido no banco inteiro, so as piores
    m = _metricas(itens)
    if m:
        altos = sorted((r for r in m[6] if r[0] >= RATIO_LIM), reverse=True)
        if altos:
            ex = ", ".join(f"#{i} ({r:.1f}x)" for r, i in altos[:RATIO_MOSTRA])
            resto = " ..." if len(altos) > RATIO_MOSTRA else ""
            linhas.append(f"correta >={RATIO_LIM}x a media das erradas em "
                          f"{len(altos)} questao(oes): {ex}{resto}")
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


def _arg_janela(argv):
    """Le '--novas N' (escopa a janela recente nas N ultimas questoes)."""
    if "--novas" in argv:
        i = argv.index("--novas")
        if i + 1 < len(argv) and argv[i + 1].isdigit():
            return int(argv[i + 1])
        print(cor("  --novas exige um numero (ex: --novas 40); usando o padrao", "ama"))
    return JANELA_PADRAO


def main():
    strict = "--strict" in sys.argv
    janela = _arg_janela(sys.argv)
    erros, avisos, avisos_f = [], [], []
    n_orig = n_prova = n_usaveis = 0

    # banco original
    bo = BASE / "banco.json"
    if bo.exists():
        banco = json.loads(bo.read_text(encoding="utf-8"))
        n_orig = len(banco)
        vistos = set()
        for i, q in enumerate(banco, 1):   # 1-based, igual aos avisos de forma
            e, a = checar_questao(q, f"banco.json #{i} [{q.get('tag','?')}]", usavel=True)
            erros += e
            avisos += a
            n_usaveis += 1
        avisos_f = avisos_forma(banco, janela=janela)
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

    if erros or (strict and (avisos or avisos_f)):
        sys.exit(1)


if __name__ == "__main__":
    main()
