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
C = {"r": "\033[0m", "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "b": "\033[1m",
     "dim": "\033[2m"}

# Vocabulario do campo opcional 'status' (auditoria Bloco V). Ausencia = 'ok'
# implicito (questao nao marcada). Presente, tem que ser um destes valores.
STATUS_VALIDOS = {"ok", "revisar", "ambigua", "distrator-fraco",
                  "explicacao-fraca", "estilo-divergente"}

# Vocabulario do campo opcional 'sub' (subtag). A 'tag' continua sendo o BLOCO
# (roteiro, progresso.csv, peso do simulado, erros/<tag>.md, --stats, historico);
# a 'sub' e so recorte de estudo para o filtro do quiz, e pode faltar.
SUB_VALIDAS = {"padroes-projeto", "uml", "java-moderno", "git-devops",
               "leitura-codigo"}


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
    # campo opcional 'sub' (subtag) — lista de strings do vocabulario fechado.
    # Nao substitui a 'tag': so acrescenta um recorte para o filtro do quiz.
    sub = q.get("sub")
    if sub is not None:
        if not isinstance(sub, list) or not all(isinstance(s, str) for s in sub):
            avisos.append(f"{rotulo}: campo 'sub' deve ser lista de strings (ex. ['uml'])")
        else:
            fora = sorted(set(sub) - SUB_VALIDAS)
            if fora:
                avisos.append(f"{rotulo}: subtag {fora} fora do vocabulario "
                              f"(esperado {sorted(SUB_VALIDAS)})")

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
# Piso para o ratio valer alguma coisa. Em questao cujas alternativas sao TERMOS
# secos ("dice", "slice", "drill-down", "pivot", "roll-up"), a razao estoura por
# causa do tamanho da palavra, nao de verbosidade da correta: 10 contra media 5,25
# da 1,9x com 5 caracteres de diferenca. Nao ha o que encurtar — o termo tem o
# nome que tem. So acusa quando as erradas ja sao frases (media >= MIN_MEDIA) E a
# correta tem folga real em caracteres (>= MIN_DELTA).
RATIO_MIN_MEDIA = 20
RATIO_MIN_DELTA = 12


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
        media_wl = sum(wl) / len(wl)
        if media_wl >= RATIO_MIN_MEDIA and cl - media_wl >= RATIO_MIN_DELTA:
            ratios.append((cl / media_wl, i))
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


# --- Detector de drift entre as camadas (apostila -> resumo -> dicas -> banco).
# A repeticao entre as camadas e INTENCIONAL (repeticao espacada: dica c resumo
# c apostila). O que nao pode e uma camada avancar e a outra ficar para tras.
# Duas checagens, as duas so avisam:
#   A) secao nova na apostila sem eco no resumo do bloco;
#   B) fato canonico (data, versao, numero de norma) que sumiu de uma camada.
#
# Linha de base de B: a camada esperada e onde o fato ESTAVA quando a checagem
# foi escrita, nao "tem que estar em todas". Presenca universal seria errada (o
# corte de 57,5 nao pertence as dicas; a data da prova nao pertence ao banco) e
# encheria a saida de ruido. Assim o aviso so acende quando o fato SOME.
CAMADAS = ("apostila", "resumo", "dicas", "banco")

FATOS_CANONICOS = [
    # (nome, regex ja normalizada/sem acento, camadas onde deve aparecer)
    ("STF art. 19 (26/06/2025)", r"26/06/2025|26 de junho de 2025", CAMADAS),
    ("OWASP Top 10 2021", r"owasp top 10\D{0,12}2021|top 10 de 2021", CAMADAS),
    # A 2025 e a edicao VIGENTE (final em jan/2026), mas o banco fica de fora de
    # proposito: as questoes de OWASP nomeiam a edicao de 2021 no enunciado, que
    # e a pratica certa (as duas numerações divergem em posicao e em nome).
    ("OWASP Top 10 2025", r"owasp top 10\D{0,12}2025|top 10 de 2025|top 10:?\s*2025",
     ("apostila", "resumo", "dicas")),
    ("ISO/IEC 27002:2022", r"27002:?\s*2022|27002 de 2022|revisao de 2022 da iso/iec 27002",
     ("apostila", "resumo", "banco")),
    ("COBIT 2019", r"cobit\s*2019", CAMADAS),
    ("ITIL 4", r"itil\s*v?4", CAMADAS),
    ("LGPD 13.709/2018", r"13\.?709", CAMADAS),
    # A ANPD virou Agencia (autarquia de natureza especial vinculada ao MJSP)
    # pela Lei 15.352/2026. Fica fora da camada "banco": a citacao vive no
    # banco-provas.json, e _texto_camadas() monta "banco" so com o banco.json.
    ("ANPD agencia (Lei 15.352/2026)", r"15\.?352", ("apostila", "resumo", "dicas")),
    ("Marco Civil 12.965/2014", r"12\.?965", CAMADAS),
    ("LAI 12.527/2011", r"12\.?527", CAMADAS),
    ("Lei 12.737/2012 (delitos informaticos)", r"12\.?737", CAMADAS),
    ("RFC 1918 (faixas privadas)", r"rfc\s*1918", ("apostila", "resumo", "banco")),
    ("23 padroes GoF", r"23 padr|vinte e tres padr", ("apostila", "resumo", "banco")),
    ("14 diagramas UML", r"14 diagramas|catorze diagramas", ("apostila", "resumo")),
    ("Scrum Guide", r"scrum guide", ("apostila", "resumo", "banco")),
    ("COBIT: 40 objetivos", r"40 objetivos", ("apostila", "resumo", "banco")),
    ("Java 17/21 LTS", r"java\s*(17|21)", CAMADAS),
    ("data da prova (11/10/2026)", r"11/10/2026", ("apostila", "resumo")),
    ("total de 115 pontos", r"\b115\b", ("apostila", "resumo", "dicas")),
    ("corte de eliminacao (57,5)", r"57,5", ("apostila", "resumo")),
]

# capitulo da apostila -> resumo(s) que deveriam ecoar suas secoes
CAP_RESUMO = {
    "02-eng-software": ["eng-software"],
    "03-padroes-uml": ["padroes-projeto", "uml"],
    "04-arquitetura": ["arquitetura"], "05-banco-dados": ["banco-dados"],
    "06-bi": ["bi"], "07-seguranca": ["seguranca"], "08-programacao": ["programacao"],
    "09-java": ["java"], "10-frontend": ["frontend"], "11-governanca": ["governanca"],
    "12-redes": ["redes"], "13-orfaos": ["orfaos"], "14-portugues": ["portugues"],
    "15-ingles": ["ingles"], "16-rlm": ["rlm"], "17-atualidades": ["atualidades"],
    "18-legislacao": ["legislacao"],
}


def _texto_camadas():
    """Concatena e normaliza o texto de cada camada. Camada ausente vira ''."""
    def ler(paths):
        out = []
        for p in paths:
            try:
                out.append(p.read_text(encoding="utf-8"))
            except OSError:
                pass
        return _norm(" ".join(out))
    banco = BASE / "banco.json"
    return {
        "apostila": ler(sorted((BASE / "apostila" / "capitulos").glob("*.tex"))),
        "resumo": ler(sorted((BASE / "resumo").glob("*.md"))),
        "dicas": ler(sorted((BASE / "dicas").glob("*.md"))),
        "banco": ler([banco]),
    }


# Piso das caixas de banca da apostila (veja o item D de avisos_drift).
# Totais medidos em 26/07/2026, no fim da fase 3 / lote 1 (programacao,
# padroes+UML e BI). As tres `pegadinha` a mais que o piso original (113) sao de
# conteudo NOVO — gestao de riscos e RUP (fase 2) e a secao de estruturas de
# dados do Cap. 9 (fase 3), que o livro nao tinha. Se voce ACRESCENTAR caixa
# legitimamente, suba o numero aqui junto.
PISO_CAIXAS = {"pegadinha": 116, "jacaiu": 20, "comosair": 24}


def avisos_drift():
    """Avisos (nao bloqueiam) de descompasso entre apostila, resumo, dicas e
    banco. Silencioso quando as camadas estao em dia."""
    linhas = []
    caps = BASE / "apostila" / "capitulos"
    if not caps.is_dir():
        return linhas
    texto = _texto_camadas()

    # A) secao da apostila sem eco no resumo do bloco
    for cap, blocos in sorted(CAP_RESUMO.items()):
        tex = caps / f"{cap}.tex"
        if not tex.exists():
            continue
        alvo = _norm(" ".join((BASE / "resumo" / f"{b}.md").read_text(encoding="utf-8")
                              for b in blocos
                              if (BASE / "resumo" / f"{b}.md").exists()))
        if not alvo:
            continue
        for m in re.finditer(r"\\section\{([^{}]*)\}", tex.read_text(encoding="utf-8")):
            titulo = re.sub(r"\\[a-zA-Z]+|[{}$]", " ", m.group(1))
            titulo = re.sub(r"\([^)]*\)", "", titulo).strip()
            palavras = [w for w in re.findall(r"[A-Za-zÀ-ÿ][\w\-]{4,}", titulo)]
            if palavras and not any(_norm(w) in alvo for w in palavras):
                linhas.append(f"[drift] apostila {cap}: secao '{titulo[:44]}' "
                              f"sem eco em resumo/{'|'.join(blocos)}.md")

    # B) fato canonico que sumiu de uma camada
    for nome, padrao, esperadas in FATOS_CANONICOS:
        sumiu = [c for c in esperadas if not re.search(padrao, texto.get(c, ""))]
        if sumiu:
            linhas.append(f"[drift] fato canonico '{nome}' sumiu de: {', '.join(sumiu)}")

    # C) contagem de questoes declarada no README x banco real
    try:
        n = len(json.loads((BASE / "banco.json").read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError):
        n = None
    if n:
        for doc in (BASE / "README.md", BASE / "resumo" / "README.md"):
            if not doc.exists():
                continue
            txt = doc.read_text(encoding="utf-8")
            m = re.search(r"(\d{3,4})\s+quest[oõ]es originais", txt)
            if m and int(m.group(1)) != n:
                linhas.append(f"[drift] {doc.name} diz '{m.group(1)} questoes "
                              f"originais', mas banco.json tem {n}")

    # D) caixa de banca que sumiu da apostila.
    # As caixas `pegadinha`, `jacaiu` e `comosair` sao o que a apostila tem de
    # melhor: custaram uma auditoria inteira contra as 432 questoes reais, e as
    # 35 `jacaiu` separam "prova real da FGV" (com sigla) do "nosso banco".
    # A frente de aprofundamento da apostila e ADITIVA — ela acrescenta
    # `conceito`, nunca dilui essas tres. Este contador e a trava: se um total
    # cair, alguma coisa foi reescrita por cima em vez de acrescentada.
    # `conceito` e `edital` ficam de fora de proposito: os dois devem crescer.
    for env, minimo in PISO_CAIXAS.items():
        achadas = sum(len(re.findall(rf"\\begin\{{{env}\}}",
                                     tex.read_text(encoding="utf-8")))
                      for tex in sorted(caps.glob("*.tex")))
        if achadas < minimo:
            linhas.append(f"[drift] apostila: {achadas} caixas '{env}', "
                          f"eram {minimo} — caixa de banca nao se apaga, "
                          f"so se acrescenta conceito ao redor")
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
    erros, avisos, avisos_f, avisos_d = [], [], [], []
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

    # drift entre apostila, resumo, dicas e banco (nao bloqueia)
    avisos_d = avisos_drift()

    # Separa o que e ACIONAVEL do que e permanente por natureza. Questao cujas
    # alternativas eram FIGURAS no caderno (BPMN, diagrama UML) sai da extracao
    # vazia e nunca vai ter texto — ela ja esta fora do sorteio e nao ha nada a
    # editar. Misturada aos avisos de verdade, ensina a ignorar a lista inteira.
    avisos_fs = [x for x in avisos if "[fora do sorteio]" in x]
    avisos = [x for x in avisos if "[fora do sorteio]" not in x]

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
    if avisos_fs:
        print(cor(f"  {len(avisos_fs)} questao(oes) fora do sorteio por dependerem de figura "
                  f"— esperado, nao ha o que editar:", "dim"))
        for x in avisos_fs[:5]:
            print(cor("    " + x, "dim"))
        if len(avisos_fs) > 5:
            print(cor(f"    ... e mais {len(avisos_fs) - 5}", "dim"))
    if avisos_f:
        print(cor(f"  {len(avisos_f)} aviso(s) de forma (banco.json) — nao bloqueiam, miram questoes novas:", "ama"))
        for x in avisos_f:
            print("   ", x)
    if avisos_d:
        print(cor(f"  {len(avisos_d)} aviso(s) de drift entre as camadas — nao bloqueiam:", "ama"))
        for x in avisos_d:
            print("   ", x)
    if not erros and not avisos and not avisos_f and not avisos_d:
        print(cor("  tudo integro.", "verde"))
    print()

    if erros or (strict and (avisos or avisos_f or avisos_d)):
        sys.exit(1)


if __name__ == "__main__":
    main()
