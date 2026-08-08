#!/usr/bin/env python3
"""Quiz de terminal — banco de questoes estilo FGV para o Dataprev 2026.

Uso:
    ./quiz.py                    10 questoes aleatorias do banco original
    ./quiz.py java               so do bloco java
    ./quiz.py java redes -n 15   15 questoes desses dois blocos
    ./quiz.py regencia           microtopico (subtag de subtags.py): atravessa
                                 os blocos; ./fraquezas.py diz quais valem hoje
    ./quiz.py --hoje             segue o plano do roteiro para hoje (todos os
                                 blocos do dia; revisao/simulado tratados)
    ./quiz.py --dia ontem        faz o plano de outro dia (ontem, anteontem,
                                 -3, ou AAAA-MM-DD); credita naquele dia
    ./quiz.py --pendentes        lista os dias de roteiro em aberto (atrasados)
    ./quiz.py --simulado         simulado cronometrado no formato da prova (70q,
                                 especificos 2,5x, sem feedback ate o fim); prioriza
                                 questao nunca vista e avisa bloco com pool curto
    ./quiz.py --erradas          repeticao espacada: so o que voce ainda nao fixou
    ./quiz.py --prova dataprev2024   questoes REAIS daquela prova (precisa gabarito)
    ./quiz.py --prova todas      questoes reais de todas as provas importadas
    ./quiz.py --dica java        dica de banca (FGV) do bloco; --dica hoje = do dia
    ./quiz.py --resumo java      resumo de conteudo; --resumo hoje = do dia
    ./quiz.py --apostila java    aponta o capitulo da apostila; --apostila hoje = do dia
    ./quiz.py --tags             inventario de blocos (os dois bancos juntos)
    ./quiz.py --stats            desempenho acumulado por bloco
    ./quiz.py --quem geys        roda como outra pessoa (progresso separado)
    ./quiz.py --sem-anotar       nao grava as erradas no caderno de erros

Duas fontes de questao (ambas escalaveis — o quiz le quantas houver):
  banco.json         questoes ORIGINAIS, estilo FGV (o padrao)
  banco-provas.json  questoes REAIS das provas em provas/, via ./importar_provas.py
                     (so entram no sorteio depois do gabarito oficial; veja ./gabarito.py)

Ao errar, o quiz explica por que cada alternativa errada esta errada e grava
AUTOMATICAMENTE a entrada em erros/<bloco>.md (deduplicando por questao) — com
a linha '- **sub:**' quando a questao tem microtopico, que e o que alimenta o
ranking do ./fraquezas.py.
"""

import argparse
import csv
import json
import random
import sys
import textwrap
import time
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

import roteiro  # leitura compartilhada do plano do dia
import subtags  # vocabulario fechado das subtags (fonte unica)

BASE = Path(__file__).parent

# blocos gerais (peso 1 na prova); os demais sao especificos (peso 2,5)
GERAIS = {"portugues", "ingles", "rlm", "atualidades", "legislacao"}
# proporcao do edital 2026 (Modulo I = 40 questoes)
ALVO_GERAIS = {"portugues": 12, "ingles": 12, "rlm": 5, "atualidades": 6, "legislacao": 5}
# subtags: recorte transversal do campo opcional 'sub'. NAO sao blocos — nao
# entram no roteiro, no progresso.csv nem no peso do simulado; servem so para
# filtrar questoes ('./quiz.py uml') e para --dica/--resumo/--apostila.
# Vocabulario em subtags.py (fonte unica, compartilhada com valida.py/fraquezas.py).
SUBTAGS = subtags.SUB_VALIDAS
# Dias ate uma questao ja fixada (2 acertos seguidos) voltar ao pool do --erradas.
# 21 dias cabe ~3 revisitas no que sobra ate 11/10 sem afogar o pool do dia; a
# curva do esquecimento derruba retencao bem antes de 30 dias, e abaixo de ~14 a
# repeticao vira desperdicio de sessao em questao que voce acabou de acertar.
INTERVALO_REVISAO = 21


def peso_de(tag):
    return 1.0 if tag in GERAIS else 2.5


# Mapa bloco -> capitulo da apostila (apostila/main.pdf). O numero IMPRESSO do
# capitulo = numero do arquivo + 1 (00-como-usar e o Cap. 1). As SUBTAGS
# (padroes-projeto, uml, java-moderno, git-devops, leitura-codigo) entram aqui
# tambem: nao sao blocos do roteiro, mas o --apostila e o --dica respondem por
# elas. padroes-projeto e uml caem no Cap. 4, separado de arquitetura (Cap. 5).
APOSTILA = {
    "tecnica-fgv": (2, "01-tecnica-fgv.tex", "Técnica de prova FGV"),
    "eng-software": (3, "02-eng-software.tex", "Engenharia de Software"),
    "padroes-projeto": (4, "03-padroes-uml.tex", "Padrões de Projeto e UML"),
    "uml": (4, "03-padroes-uml.tex", "Padrões de Projeto e UML"),
    "java-moderno": (10, "09-java.tex", "Java — recursos modernos (17/21 LTS)"),
    "git-devops": (9, "08-programacao.tex", "Versionamento com Git e DevOps"),
    "leitura-codigo": (9, "08-programacao.tex", "Leitura ativa de código"),
    "arquitetura": (5, "04-arquitetura.tex", "Arquitetura de Software"),
    "banco-dados": (6, "05-banco-dados.tex", "Banco de Dados"),
    "bi": (7, "06-bi.tex", "Business Intelligence (BI)"),
    "seguranca": (8, "07-seguranca.tex", "Segurança da Informação"),
    "programacao": (9, "08-programacao.tex", "Programação"),
    "java": (10, "09-java.tex", "Java"),
    "frontend": (11, "10-frontend.tex", "Frontend"),
    "governanca": (12, "11-governanca.tex", "Gestão e Governança de TI"),
    "redes": (13, "12-redes.tex", "Redes de Computadores"),
    "orfaos": (14, "13-orfaos.tex", "Órfãos — Administração de BD e Temas Coringa"),
    "portugues": (15, "14-portugues.tex", "Língua Portuguesa"),
    "ingles": (16, "15-ingles.tex", "Língua Inglesa"),
    "rlm": (17, "16-rlm.tex", "Raciocínio Lógico Matemático"),
    "atualidades": (18, "17-atualidades.tex", "Atualidades e Inteligência Artificial"),
    "legislacao": (19, "18-legislacao.tex", "Legislação — Segurança da Informação e Proteção de Dados"),
}


def ref_apostila(q):
    """Referencia curta da apostila para uma questao, no formato do caderno de
    erros: 'Apostila Cap. N §X' quando a questao traz o campo opcional
    'apostila' (ex. '§3.4'), senao 'Apostila Cap. N — Titulo'. Devolve '' se o
    bloco nao estiver mapeado."""
    info = APOSTILA.get(q.get("tag"))
    if not info:
        return ""
    cap, _arq, titulo = info
    sec = str(q.get("apostila", "")).strip()
    if sec:
        sec = sec if sec.startswith("§") else f"§{sec}"
        return f"Apostila Cap. {cap} {sec}"
    return f"Apostila Cap. {cap} — {titulo}"


BANCO = BASE / "banco.json"
BANCO_PROVAS = BASE / "banco-provas.json"
CSV = BASE / "progresso.csv"


def hist_de(quem):
    """Cada pessoa tem seu proprio historico; 'lucas' mantem o arquivo original."""
    return BASE / ("historico.json" if quem == "lucas" else f"historico-{quem}.json")


def csv_de(quem):
    """O roteiro (datas/foco) e compartilhado; os contadores sao de cada um."""
    return CSV if quem == "lucas" else BASE / f"progresso-{quem}.csv"

C = {"r": "\033[0m", "b": "\033[1m", "dim": "\033[2m",
     "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "ciano": "\033[36m"}


def cor(t, c):
    return f"{C[c]}{t}{C['r']}"


def wrap(t, indent="  "):
    # linhas de continuacao alinham com o texto, sem repetir o prefixo ("C) ")
    return textwrap.fill(t, width=76, initial_indent=indent, subsequent_indent=" " * len(indent))


def carregar_originais():
    """Todas as questoes de banco.json, com id 'o0', 'o1', ... (escalavel:
    le quantas houver, sem numero fixo)."""
    banco = json.loads(BANCO.read_text(encoding="utf-8"))
    for i, q in enumerate(banco):
        q["id"] = f"o{i}"  # 'o' de original
    return banco


def provas_disponiveis():
    """Nomes das provas em banco-provas.json (vazio se o arquivo nao existe)."""
    if not BANCO_PROVAS.exists():
        return []
    return sorted({q["prova"] for q in json.loads(BANCO_PROVAS.read_text(encoding="utf-8"))})


def carregar_provas(prova=None):
    """Questoes USAVEIS das provas (com gabarito oficial, sem figura perdida e
    nao anuladas). prova=None traz todas as provas juntas; escala sozinho
    conforme voce roda ./importar_provas.py em novos PDFs."""
    if not BANCO_PROVAS.exists():
        return []
    todas = json.loads(BANCO_PROVAS.read_text(encoding="utf-8"))
    if prova is not None:
        todas = [q for q in todas if q["prova"] == prova]
    for q in todas:
        q["id"] = f"{q['prova']}:{q['num']}"
    return [
        q for q in todas
        if q["ans"] is not None and not q.get("requer_imagem") and not q.get("anulada")
    ]


def carregar_hist(quem):
    h = hist_de(quem)
    if h.exists():
        return json.loads(h.read_text(encoding="utf-8"))
    return {"respostas": []}


def salvar_hist(h, quem):
    hist_de(quem).write_text(json.dumps(h, ensure_ascii=False, indent=1), encoding="utf-8")


def _pendentes_por_motivo(hist, hoje=None):
    """Repeticao espacada (estilo Leitner): uma questao 'deve' revisao se voce
    ja a errou ao menos uma vez E ainda nao emendou 2 acertos seguidos desde o
    ultimo erro. Assim que voce acerta 2x seguidas, ela se aposenta.

    A aposentadoria e TEMPORARIA: passados INTERVALO_REVISAO dias desde a ultima
    vez que a questao apareceu, ela volta ao pool. Sem isso o Leitner fica pela
    metade — o que foi fixado em agosto nunca mais seria revisto em outubro, e a
    prova e em 11/10. Acertar de novo reempurra o prazo por mais um intervalo;
    errar zera o streak e ela volta ao regime normal.

    Devolve (nao_fixadas, vencidas): a primeira e quem ainda nao emendou os dois
    acertos, a segunda e quem ja tinha fixado e venceu o intervalo."""
    hoje = hoje or date.today()
    seq = defaultdict(list)
    visto = {}
    for r in hist["respostas"]:
        seq[r["id"]].append(bool(r["ok"]))
        quando = r.get("quando")
        if quando:
            try:
                d = datetime.fromisoformat(quando).date()
            except ValueError:
                continue
            visto[r["id"]] = max(visto.get(r["id"], d), d)
    nao_fixadas, vencidas = set(), set()
    for id_, outs in seq.items():
        if all(outs):
            continue  # nunca errou
        streak = 0
        for o in reversed(outs):
            if o:
                streak += 1
            else:
                break
        if streak < 2:
            nao_fixadas.add(id_)
            continue
        # aposentada: so volta quando o intervalo vence. Registro sem data (ou
        # com data ilegivel) conta como antigo — melhor rever a mais que a menos.
        ultima = visto.get(id_)
        if ultima is None or (hoje - ultima).days >= INTERVALO_REVISAO:
            vencidas.add(id_)
    return nao_fixadas, vencidas


def erradas_pendentes(hist, hoje=None):
    """Uniao dos dois motivos de revisao (ver _pendentes_por_motivo)."""
    nao_fixadas, vencidas = _pendentes_por_motivo(hist, hoje)
    return nao_fixadas | vencidas


def garantir_csv(quem):
    """Para quem nao e o lucas, cria o progresso a partir do roteiro, zerado."""
    destino = csv_de(quem)
    if destino.exists() or not CSV.exists():
        return destino
    with open(CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        campos = list(rows[0].keys())
    for r in rows:
        r["questoes"], r["acertos"], r["feito"] = "0", "0", "0"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(rows)
    print(cor(f"  criei {destino.name} a partir do roteiro (contadores zerados).", "ciano"))
    return destino


def _alvos(valor, quem):
    """Resolve o argumento de --dica/--resumo. 'hoje' vira os blocos do plano
    do dia; '__listar__' (sem argumento) lista; senao, o proprio bloco."""
    if valor == "hoje":
        plano = roteiro.plano_de_hoje(csv_de(quem))
        if plano["blocos"]:
            return plano["blocos"]
        print(cor("\n  hoje nao tem bloco de conteudo no roteiro.\n", "dim"))
        return []
    return [valor]


def cabecalho_plano(plano):
    """Imprime o plano do dia e os atalhos (dica/resumo) de cada bloco."""
    l = plano["linha"]
    if l:
        print(cor(f"\n  Plano do dia — {l['data']} ({l['dia']}), semana {l['semana']}", "b"))
        print(cor(f"    Foco:   {plano['foco']}", "dim"))
        print(cor(f"    Também: {plano['secundario']}", "dim"))
    for b in plano["blocos"]:
        extras = []
        if (BASE / "resumo" / f"{b}.md").exists():
            extras.append(f"resumo: ./quiz.py --resumo {b}")
        if (BASE / "dicas" / f"{b}.md").exists():
            extras.append(f"dica: ./quiz.py --dica {b}")
        linha = f"    • {b}"
        if extras:
            linha += cor("   (" + "  |  ".join(extras) + ")", "dim")
        print(linha)


def registrar_no_csv(qtd, acertos, quem, dia=None):
    """Soma o resultado ao dia informado (default hoje) no progresso da pessoa.
    Recuperar um dia atrasado (--dia) credita naquele dia e o marca como feito."""
    arq = csv_de(quem)
    if not arq.exists():
        print(cor(f"  {arq.name} nao encontrado; nada registrado.", "dim"))
        return
    alvo = (dia or date.today()).isoformat()
    with open(arq, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        campos = rows and list(rows[0].keys())
    achou = False
    for r in rows:
        if r["data"] == alvo:
            r["questoes"] = str(int(r["questoes"]) + qtd)
            r["acertos"] = str(int(r["acertos"]) + acertos)
            r["feito"] = "1"
            achou = True
    if not achou:
        print(cor(f"  {alvo} nao esta no roteiro; nada registrado.", "dim"))
        return
    with open(arq, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(rows)
    print(cor(f"  registrado em {arq.name}: +{qtd} questoes, +{acertos} acertos.", "verde"))


def _titulo_erro(q):
    """Titulo curto e reconhecivel: primeira oracao do enunciado, ate ~70 chars."""
    t = " ".join(q["q"].split())
    corte = t.split(":")[0].split(".")[0]  # primeira clausula
    if len(corte) > 70:
        corte = corte[:70].rsplit(" ", 1)[0] + "…"
    return corte or f"questao {q['id']}"


def anotar_erro(q, marcou, correta):
    """Grava AUTOMATICAMENTE a entrada no caderno erros/<bloco>.md, no formato
    do repositorio. Deduplica por questao (marcador HTML oculto): a mesma
    questao errada duas vezes nao vira duas anotacoes. Para desligar, use
    --sem-anotar."""
    arq = BASE / "erros" / f"{q['tag']}.md"
    if not arq.exists():
        arq.write_text(f"# {q['tag']}\n", encoding="utf-8")

    marcador = f"<!-- auto {q['id']} -->"
    if marcador in arq.read_text(encoding="utf-8"):
        return  # ja anotada antes

    letras = "ABCDE"
    correcao = q.get("why", "").strip() or f"a correta era {letras[correta]}: {q['alts'][correta]}"
    fonte = q.get("fonte") or "quiz local"
    ref = ref_apostila(q)
    linha_ref = f"- {ref}\n" if ref else ""

    # microtopico do erro: so quando a questao ja vem etiquetada. Questao de
    # prova real nao tem 'sub' — a etiqueta entra a mao na hora de estudar o
    # erro, e o ./fraquezas.py --sem-sub lista o que ficou sem.
    subs = [s for s in (q.get("sub") or []) if s in SUBTAGS]
    linha_sub = f"- **sub:** {', '.join(subs)}\n" if subs else ""

    entrada = (
        f"\n## {_titulo_erro(q)} {marcador}\n"
        f"{linha_sub}"
        f"- **Errei:** marquei {letras[marcou]}, a correta era {letras[correta]}\n"
        f"- **E:** {correcao}\n"
        f"{linha_ref}"
        f"- {fonte} | {date.today():%d/%m}\n"
    )
    with open(arq, "a", encoding="utf-8") as f:
        f.write(entrada)
    print(cor(f"  anotado em erros/{q['tag']}.md", "dim"))


def mostrar_apostila(bloco):
    """Aponta o capitulo/secao da apostila (apostila/main.pdf) do bloco. Sem
    argumento, lista os blocos mapeados. A apostila e PDF: o comando indica
    onde ler, nao imprime o conteudo (diferente de --dica/--resumo)."""
    if bloco == "__listar__" or not bloco:
        print(cor("\n  Apostila — capitulos por bloco (apostila/main.pdf):", "b"))
        for b, (cap, _arq, titulo) in sorted(APOSTILA.items(), key=lambda x: x[1][0]):
            marca = cor(" (subtag)", "dim") if b in SUBTAGS else ""
            print(f"    Cap. {cap:>2}  {b:<16} {cor(titulo, 'dim')}{marca}")
        print(cor("\n  uso: ./quiz.py --apostila <bloco>   (--apostila hoje = do dia)\n", "dim"))
        return
    info = APOSTILA.get(bloco)
    if not info and bloco in SUBTAGS:
        # subtag de microtopico (nascida do caderno de erros) nao tem capitulo
        # proprio: cai no capitulo do bloco que cobre o assunto.
        info = APOSTILA.get(subtags.VOCAB[bloco]["apostila"])
    if not info:
        print(cor(f"\n  sem capitulo mapeado para '{bloco}'. Use ./quiz.py --apostila para listar.\n", "verm"))
        return
    cap, arq, titulo = info
    print(cor(f"\n  {bloco} → Apostila Cap. {cap} — {titulo}", "b"))
    print(cor(f"    fonte: apostila/capitulos/{arq}", "dim"))
    print(cor(f"    abra:  apostila/main.pdf  (Cap. {cap})\n", "dim"))


def _resolve_arquivo(pasta, alvo):
    """Acha o .md de dica/resumo do alvo. As cinco subtags antigas tem arquivo
    proprio; as de microtopico (nascidas do caderno de erros) nao — essas caem
    no arquivo do bloco que cobre o assunto, dizendo de onde veio.
    Retorna (arquivo | None, nota | None)."""
    arq = pasta / f"{alvo}.md"
    if arq.exists():
        return arq, None
    if alvo in SUBTAGS:
        pai = subtags.VOCAB[alvo]["apostila"]
        alt = pasta / f"{pai}.md" if pai else None
        if alt is not None and alt.exists():
            return alt, f"  (nao ha {pasta.name}/{alvo}.md — mostrando o do bloco '{pai}')"
    return None, None


def mostrar_dica(bloco):
    """Imprime a dica de banca (dicas/<bloco>.md). Sem argumento, lista os blocos."""
    dicas = BASE / "dicas"
    if bloco == "__listar__" or not bloco:
        disp = sorted(p.stem for p in dicas.glob("*.md")) if dicas.exists() else []
        print(cor("\n  Dicas de banca (FGV) disponiveis:", "b"))
        for d in disp:
            print(f"    {d}")
        print(cor("\n  uso: ./quiz.py --dica <bloco>\n", "dim"))
        return
    arq, nota = _resolve_arquivo(dicas, bloco)
    if arq is None:
        print(cor(f"\n  sem dica para '{bloco}'. Use ./quiz.py --dica para listar.\n", "verm"))
        return
    print()
    if nota:
        print(cor(nota, "dim"))
    for linha in arq.read_text(encoding="utf-8").splitlines():
        if linha.startswith("# "):
            print(cor("  " + linha[2:], "b"))
        elif linha.startswith("## "):
            print(cor("  " + linha[3:], "ciano"))
        else:
            print(wrap(linha) if linha.strip() else "")
    print()


def mostrar_resumo(bloco):
    """Imprime o resumo de conteudo (resumo/<bloco>.md) cru — sem quebra de
    linha, para as tabelas nao desalinharem. Sem argumento, lista os blocos."""
    resumo = BASE / "resumo"
    if bloco == "__listar__" or not bloco:
        disp = sorted(p.stem for p in resumo.glob("*.md")) if resumo.exists() else []
        print(cor("\n  Resumos de conteudo disponiveis:", "b"))
        for d in disp:
            if d != "README":
                print(f"    {d}")
        print(cor("\n  uso: ./quiz.py --resumo <bloco>", "dim"))
        print(cor("  (a visao geral esta em resumo/README.md)\n", "dim"))
        return
    arq, nota = _resolve_arquivo(resumo, bloco)
    if arq is None:
        print(cor(f"\n  sem resumo para '{bloco}'. Use ./quiz.py --resumo para listar.\n", "verm"))
        return
    print()
    if nota:
        print(cor(nota, "dim"))
    for linha in arq.read_text(encoding="utf-8").splitlines():
        if linha.startswith("# "):
            print(cor("  " + linha[2:], "b"))
        elif linha.startswith("## "):
            print(cor("  " + linha[3:], "ciano"))
        else:
            print("  " + linha)
    print()


def perguntar_causa():
    """Ao errar, captura a CAUSA do erro numa tecla (opcional): conceitual (nao
    sabia o conteudo) vs. armadilha (sabia e caiu na construcao). Enter pula.
    Devolve 'conceitual', 'armadilha' ou None. A causa e da TENTATIVA, nao da
    questao — vai como campo opcional no historico."""
    prompt = cor("  causa do erro? [c]onceitual (nao sabia) / [l]eitura (sabia, caí) / Enter pula: ", "dim")
    while True:
        try:
            r = input(prompt).strip().lower()
        except EOFError:
            return None
        if r == "":
            return None
        if r in ("c", "conceitual"):
            return "conceitual"
        if r in ("l", "leitura", "armadilha", "a"):
            return "armadilha"
        print(cor("  responda c, l ou Enter", "dim"))


def rodar(questoes, anotar=True):
    total = len(questoes)
    acertos = 0
    erradas = []
    causas = {}   # id_da_questao -> 'conceitual' | 'armadilha' (so as erradas com resposta)
    letras = "ABCDE"

    print()
    print(cor(f"  {total} questoes. Responda com a letra (A-E). 'q' abandona.", "dim"))
    print()

    for n, q in enumerate(questoes, 1):
        # embaralha alternativas preservando qual e a correta.
        # 'ordem[i]' = indice original da alternativa mostrada na posicao i.
        ordem = list(range(5))
        random.shuffle(ordem)
        correta_pos = ordem.index(q["ans"])

        cab = cor(f"  Questao {n}/{total}", "b") + " " + cor(f"[{q['tag']}]", "ciano")
        if q.get("fonte"):
            cab += " " + cor(q["fonte"], "dim")
        print(cab)
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
        certo = escolhida == correta_pos
        print()
        if certo:
            acertos += 1
            print(cor(f"  CERTO — {letras[correta_pos]}.", "verde"))
        else:
            erradas.append(q)
            print(cor(f"  ERRADO. Voce marcou {r}; a correta e {letras[correta_pos]}.", "verm"))

        # por que a correta esta certa
        if q.get("why"):
            print()
            print(wrap(q["why"], indent="    "))

        # por que cada uma das outras esta errada (fixacao)
        # 'erradas' e indexado pelo indice ORIGINAL da alternativa, como string
        expl = q.get("erradas") or {}
        if expl:
            print()
            print(cor("    Por que as outras estao erradas:", "dim"))
            for i, oi in enumerate(ordem):
                if i == correta_pos:
                    continue
                texto = expl.get(str(oi))
                if texto:
                    marca = cor(" <- sua", "verm") if i == escolhida else ""
                    print(wrap(texto, indent=f"      {letras[i]}) ") + marca)

        if not certo:
            causa = perguntar_causa()
            if causa:
                causas[q["id"]] = causa
            if anotar:
                anotar_erro(q, escolhida, correta_pos)
        print()

    return acertos, erradas, causas


def montar_simulado(banco, n, hist=None):
    """Monta um simulado no formato da prova: gerais (peso 1) na proporcao do
    edital + especificos (peso 2,5) completando, escalado para n questoes.
    Ordena os especificos primeiro (valem 2,5x — a estrategia do roteiro).

    Prioriza frescor: dentro de cada tag, quem nunca apareceu (em qualquer
    modo do quiz — diario, revisao ou simulado, e' o mesmo historico.json)
    ou apareceu ha mais tempo vem primeiro. So repete uma questao vista
    recentemente quando o resto do pool da tag ja se esgotou. Sem hist,
    cai no sorteio puro (comportamento antigo).

    Devolve (sel, avisos): avisos sinaliza blocos com pool curto demais pra
    manter a proporcao do edital, ou que so entraram repetindo questao ja
    vista por falta de fresco — os dois sintomas de que vale gerar questoes
    novas pra aquele bloco antes do proximo simulado."""
    ultima_vez = defaultdict(str)  # "" (nunca vista) ordena antes de qualquer ISO
    if hist:
        for r in hist["respostas"]:
            ultima_vez[r["id"]] = max(ultima_vez[r["id"]], r["quando"])

    def mais_fresca_primeiro(pool):
        pool = pool[:]
        random.shuffle(pool)  # desempate aleatorio dentro da mesma faixa de frescor
        pool.sort(key=lambda q: ultima_vez[q["id"]])
        return pool

    por_tag = defaultdict(list)
    for q in banco:
        por_tag[q["tag"]].append(q)
    n_ger = round(n * 40 / 70)  # 40 de 70 sao gerais na prova
    sel, usados = [], set()
    avisos = []
    for tag, alvo in ALVO_GERAIS.items():
        k = round(n_ger * alvo / 40)  # distribui os gerais pela proporcao do edital
        total_tag = len(por_tag.get(tag, []))
        if total_tag < k:
            avisos.append(
                f"{tag}: banco tem so {total_tag} questao(oes), precisava de {k} "
                f"pra manter a proporcao do edital num simulado de {n}."
            )
        pool = mais_fresca_primeiro(por_tag.get(tag, []))
        for q in pool[:k]:
            sel.append(q)
            usados.add(id(q))
    espec = mais_fresca_primeiro([q for q in banco if q["tag"] not in GERAIS and id(q) not in usados])
    sel += espec[: max(0, n - len(sel))]
    sel.sort(key=lambda q: 0 if q["tag"] not in GERAIS else 1)  # especificos 1o

    # repeticao forcada: entrou porque o pool fresco da tag ja tinha acabado
    repetidas = defaultdict(int)
    for q in sel:
        if ultima_vez[q["id"]]:
            repetidas[q["tag"]] += 1
    for tag, n_rep in sorted(repetidas.items()):
        avisos.append(
            f"{tag}: {n_rep} questao(oes) repetida(s) neste simulado "
            f"(pool tem so {len(por_tag.get(tag, []))} no total)."
        )
    return sel, avisos


def rodar_simulado(questoes, minutos=240):
    """Roda em condicoes de prova: SEM feedback por questao, cronometrado.
    Devolve (respondidas, tempo_seg). Cada respondida: (q, ok)."""
    letras = "ABCDE"
    n = len(questoes)
    print(cor(f"\n  SIMULADO — {n} questoes | tempo sugerido {minutos} min", "b"))
    print(cor("  Sem correcao ate o fim. 'q' encerra e corrige o que voce fez.", "dim"))
    print(cor("  Especificos primeiro; eles valem 2,5x.", "dim"))
    inicio = time.monotonic()
    respondidas = []
    for i, q in enumerate(questoes, 1):
        ordem = list(range(5))
        random.shuffle(ordem)
        correta_pos = ordem.index(q["ans"])
        peso = peso_de(q["tag"])
        etq = cor("[2,5x]", "ama") if peso == 2.5 else cor("[1,0x]", "dim")
        restante = minutos - (time.monotonic() - inicio) / 60
        print(f"\n  {cor(f'Q{i}/{n}', 'b')} {etq}  {cor(f'~{restante:.0f} min rest.', 'dim')}")
        print(wrap(q["q"]))
        print()
        for j, oi in enumerate(ordem):
            print(wrap(q["alts"][oi], indent=f"    {letras[j]}) "))
        while True:
            r = input("  > ").strip().upper()
            if r == "Q":
                print(cor("\n  encerrando simulado...", "dim"))
                return respondidas, time.monotonic() - inicio
            if r in letras:
                break
            print(cor("  responda A-E (ou q para encerrar)", "dim"))
        respondidas.append((q, letras.index(r) == correta_pos))
    return respondidas, time.monotonic() - inicio


def corrigir_simulado(respondidas, tempo_seg, total):
    """Mostra a nota ponderada, o tempo e o desempenho por bloco."""
    letras = "ABCDE"
    pontos = sum(peso_de(q["tag"]) for q, ok in respondidas if ok)
    poss_resp = sum(peso_de(q["tag"]) for q, _ in respondidas)
    max_total = 115.0  # a prova inteira vale 115
    acertos = sum(1 for _, ok in respondidas if ok)
    mm = int(tempo_seg // 60)

    print(cor("\n  " + "=" * 44, "dim"))
    print(cor(f"  RESULTADO DO SIMULADO", "b"))
    print(f"  Respondidas: {len(respondidas)}/{total}   Tempo: {mm} min")
    c = "verde" if acertos / max(1, len(respondidas)) >= 0.7 else "ama" if acertos / max(1, len(respondidas)) >= 0.5 else "verm"
    print(f"  Acertos: {cor(f'{acertos}/{len(respondidas)}', c)}")
    print(f"  Pontos (peso): {cor(f'{pontos:.1f}', c)} de {poss_resp:.1f} feitos"
          + cor(f"  (prova inteira vale {max_total:.0f})", "dim"))
    corte = 57.5
    proj = pontos / poss_resp * max_total if poss_resp else 0
    cc = "verde" if proj >= corte else "verm"
    print(f"  Projecao p/ 115: {cor(f'{proj:.0f}', cc)}  (corte de eliminacao: {corte:.0f})")

    por_tag = defaultdict(lambda: [0, 0])
    for q, ok in respondidas:
        por_tag[q["tag"]][0] += 1
        por_tag[q["tag"]][1] += ok
    print(cor("\n  Por bloco:", "b"))
    for t, (tot, ok) in sorted(por_tag.items(), key=lambda x: x[1][1] / x[1][0]):
        p = ok / tot * 100
        c = "verde" if p >= 75 else "ama" if p >= 60 else "verm"
        print(f"    {t:<16} {cor(f'{ok}/{tot}', c)}")
    print(cor("\n  As erradas viram material de revisao (./quiz.py --erradas).", "dim"))
    print()


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("tags", nargs="*")
    p.add_argument("-n", type=int, default=None)
    p.add_argument("--hoje", action="store_true")
    p.add_argument("--dia", default=None)   # ontem, anteontem, -2, AAAA-MM-DD
    p.add_argument("--pendentes", action="store_true")
    p.add_argument("--simulado", action="store_true")
    p.add_argument("--erradas", action="store_true")
    p.add_argument("--prova", default=None)
    p.add_argument("--quem", default="lucas")
    p.add_argument("--sem-anotar", dest="anotar", action="store_false")
    p.add_argument("--tags", dest="listar", action="store_true")
    p.add_argument("--stats", action="store_true")
    p.add_argument("--dica", nargs="?", const="__listar__", default=None)
    p.add_argument("--resumo", nargs="?", const="__listar__", default=None)
    p.add_argument("--apostila", nargs="?", const="__listar__", default=None)
    p.add_argument("-h", "--help", action="store_true")
    a = p.parse_args()

    if a.help:
        print(__doc__)
        return

    quem = a.quem.strip().lower()

    if a.dica is not None:
        for b in _alvos(a.dica, quem):
            mostrar_dica(b)
        return

    if a.resumo is not None:
        for b in _alvos(a.resumo, quem):
            mostrar_resumo(b)
        return

    if a.apostila is not None:
        for b in _alvos(a.apostila, quem):
            mostrar_apostila(b)
        return

    if quem != "lucas":
        print(cor(f"\n  sessao de: {quem}", "ciano"))
        garantir_csv(quem)

    if a.pendentes:
        atr = roteiro.pendentes(csv_de(quem))
        print()
        if not atr:
            print(cor("  Nenhum dia atrasado. Em dia com o roteiro!\n", "verde"))
            return
        print(cor(f"  {len(atr)} dia(s) de roteiro em aberto:", "ama"))
        for d in atr:
            print(f"    {d['data']} ({d['dia']})  {d['foco']}")
        print(cor("\n  recupere um dia com: ./quiz.py --dia AAAA-MM-DD  (ou --dia ontem)\n", "dim"))
        return

    # dia-alvo do roteiro: --dia tem prioridade; senao --hoje = hoje
    data_roteiro = None
    if a.dia is not None:
        data_roteiro = roteiro.resolver_data(a.dia)
        if data_roteiro is None:
            sys.exit(cor(f"\n  nao entendi --dia '{a.dia}'. Use: ontem, anteontem, -2, ou AAAA-MM-DD\n", "verm"))
    elif a.hoje:
        data_roteiro = date.today()

    # --- carga dos bancos (escalavel: le o que houver, sem numero fixo) ---
    if a.prova is not None:
        if a.prova != "todas" and a.prova not in provas_disponiveis():
            disp = ", ".join(provas_disponiveis()) or "(nenhuma importada)"
            sys.exit(cor(f"\n  prova '{a.prova}' nao existe. Disponiveis: {disp}\n", "verm"))
        banco = carregar_provas(None if a.prova == "todas" else a.prova)
        if not banco:
            print(cor(f"\n  nenhuma questao utilizavel em '{a.prova}'.", "verm"))
            print(cor(f"  falta gabarito? preencha com: ./gabarito.py {a.prova} \"1-C 2-A ...\"\n", "dim"))
            return
    elif a.erradas or data_roteiro is not None:
        # erradas e o plano do dia buscam nos DOIS bancos (originais + provas),
        # para o pool de cada bloco (inclusive portugues/ingles/etc) ser o maior
        banco = carregar_originais() + carregar_provas()
    else:
        banco = carregar_originais()

    hist = carregar_hist(quem)

    if a.listar:
        # inventario combinado dos dois bancos, para ver tudo que da pra estudar
        # defaultdict junto: os re-imports locais mais abaixo em main() tornam o
        # nome local a funcao inteira, e o do modulo (linha 47) deixa de valer aqui
        from collections import Counter, defaultdict
        tudo = carregar_originais() + carregar_provas()
        c = Counter(q["tag"] for q in tudo)
        print()
        for t, n in sorted(c.items()):
            tem_dica = "" if (BASE / "dicas" / f"{t}.md").exists() else cor("  (sem dica)", "dim")
            print(f"  {t:<16} {n} questoes{tem_dica}")
        # subtags: o vocabulario INTEIRO (subtags.py), agrupado pelo bloco que
        # cobre o assunto. Mostra todas, inclusive as que ainda nao tem questao
        # etiquetada — e esta lista que responde "que valor posso usar no 'sub'?".
        sub = Counter(s for q in tudo for s in q.get("sub", []))
        por_bloco = defaultdict(list)
        for nome, v in subtags.VOCAB.items():
            por_bloco[v["apostila"] or "(transversal)"].append(nome)
        print(cor("\n  subtags — microtopicos (a questao continua no bloco dela);"
                  " (n) = questoes etiquetadas:", "dim"))
        for bloco in sorted(por_bloco):
            # texto PURO no wrap: textwrap conta o escape de cor como largura
            # visivel e quebraria os nomes no meio ("gof-\ncriacionais")
            itens = " ".join(f"{n}({sub[n]})" if sub[n] else n
                             for n in sorted(por_bloco[bloco]))
            print(f"  {cor(bloco, 'ciano')}")
            print(textwrap.fill(itens, width=74, initial_indent="    ",
                                subsequent_indent="    ", break_on_hyphens=False))
        print(f"\n  total: {len(tudo)} questoes | {len(subtags.VOCAB)} microtopicos "
              f"| dica de banca: ./quiz.py --dica <bloco>\n")
        return

    if a.stats:
        from collections import defaultdict
        # por bloco: [total, acertos, erros conceituais, erros de leitura]
        d = defaultdict(lambda: [0, 0, 0, 0])
        for r in hist["respostas"]:
            d[r["tag"]][0] += 1
            d[r["tag"]][1] += r["ok"]
            if not r["ok"]:
                causa = r.get("causa")  # opcional: dados antigos nao tem
                if causa == "conceitual":
                    d[r["tag"]][2] += 1
                elif causa == "armadilha":
                    d[r["tag"]][3] += 1
        print()
        if not d:
            print(cor("  nenhuma sessao registrada ainda.\n", "dim"))
            return
        print(cor("  Desempenho acumulado no quiz", "b"))
        for t, (tot, ok, conc, arm) in sorted(d.items(), key=lambda x: x[1][1] / x[1][0]):
            pct = ok / tot * 100
            c = "verde" if pct >= 75 else "ama" if pct >= 60 else "verm"
            errs = tot - ok
            sem = errs - conc - arm  # erros sem causa marcada (pulou / dado antigo)
            partes = []
            if conc:
                partes.append(cor(f"{conc} conceitual", "verm"))
            if arm:
                partes.append(cor(f"{arm} leitura", "ama"))
            if sem:
                partes.append(cor(f"{sem} ?", "dim"))
            cauda = ("   erros: " + " · ".join(partes)) if partes else ""
            print(f"    {t:<16} {cor(f'{pct:>3.0f}%', c)}  ({ok}/{tot}){cauda}")

        # Trava anti-vicio: a recomendacao depende da CAUSA. Erro majoritariamente
        # conceitual = falta conteudo -> mandar reler a apostila e fazer mais
        # questoes, SEM falar de tecnica de eliminacao (senao vira muleta pra nao
        # estudar). So quando o erro e de leitura/armadilha os sete padroes de
        # distrator entram em cena. Empate pende pro lado conteudo (mais seguro).
        recs = []
        for t, (tot, ok, conc, arm) in d.items():
            if conc == 0 and arm == 0:
                continue  # sem causa marcada: nada a recomendar
            if conc >= arm:
                cap = APOSTILA.get(t, (None,))[0]
                onde = f"Apostila Cap. {cap}" if cap else "o resumo do bloco"
                recs.append((conc + arm, "verm", t,
                             f"erros mais CONCEITUAIS → releia {onde} + mais questões de {t}"))
            else:
                recs.append((conc + arm, "ama", t,
                             "erros mais de LEITURA → treine os 7 padrões de distrator: "
                             "./quiz.py --dica tecnica-fgv (Cap. 2)"))
        if recs:
            print(cor("\n  Onde focar (pela causa do erro):", "b"))
            for _peso, c, t, msg in sorted(recs, key=lambda x: -x[0]):
                print(f"    {cor(t, c)}: {msg}")
        print()
        return

    # numero de questoes: 70 no simulado, 10 no resto (a menos que -n)
    n = a.n if a.n is not None else (70 if a.simulado else 10)

    # dia de simulado no roteiro tambem dispara o modo cronometrado
    dia_sim = None
    if data_roteiro is not None:
        pl = roteiro.plano_de_hoje(csv_de(quem), data_roteiro)
        if pl["tipo"] == "simulado":
            a.simulado = True
            dia_sim = data_roteiro

    if a.simulado:
        base = carregar_originais() + carregar_provas()
        sel, avisos = montar_simulado(base, n, hist)
        if avisos:
            print(cor("\n  Cobertura curta neste simulado (gere questoes novas):", "ama"))
            for av in avisos:
                print(cor(f"    - {av}", "dim"))
        respondidas, tempo = rodar_simulado(sel)
        if not respondidas:
            return
        corrigir_simulado(respondidas, tempo, len(sel))
        agora = datetime.now().isoformat(timespec="seconds")
        for q, ok in respondidas:
            hist["respostas"].append({"id": q["id"], "tag": q["tag"], "ok": ok, "quando": agora})
        salvar_hist(hist, quem)
        acertos = sum(1 for _, ok in respondidas if ok)
        destino = f" ({dia_sim})" if dia_sim else ""
        r = input(f"  registrar em {csv_de(quem).name}{destino}? [S/n] ").strip().lower()
        if r in ("", "s", "sim"):
            registrar_no_csv(len(respondidas), acertos, quem, dia=dia_sim)
        print()
        return

    # selecao de questoes
    if a.erradas:
        nao_fixadas, vencidas = _pendentes_por_motivo(hist)
        pool = [q for q in banco if q["id"] in (nao_fixadas | vencidas)]
        if not pool:
            print(cor("\n  nada pendente de revisao — voce fixou o que tinha errado.\n", "verde"))
            return
        if vencidas:
            print(cor(f"\n  {len(nao_fixadas)} ainda nao fixada(s) + {len(vencidas)} de volta "
                      f"por intervalo ({INTERVALO_REVISAO} dias sem ver).", "ciano"))
    elif data_roteiro is not None:
        plano = roteiro.plano_de_hoje(csv_de(quem), data_roteiro)
        cabecalho_plano(plano)
        tipo = plano["tipo"]
        if tipo is None:
            print(cor(f"\n  {data_roteiro} nao esta no roteiro; rodando 10 aleatorias.\n", "dim"))
            pool = banco[:]
        elif tipo == "descanso":
            print(cor("\n  Hoje e descanso no roteiro. Bom descanso!\n", "ciano"))
            return
        elif tipo == "prova":
            print(cor("\n  Hoje e a PROVA. Boa sorte, voce se preparou pra isso.\n", "ciano"))
            return
        elif tipo == "revisao":
            print(cor("\n  Dia de revisao: refazendo o que ainda nao fixou (repeticao espacada).\n", "ciano"))
            pool = [q for q in banco if q["id"] in erradas_pendentes(hist)]
            if not pool:
                print(cor("  nada pendente de revisao — voce fixou o que tinha errado.\n", "verde"))
                return
        # tipo == "simulado" ja foi tratado antes (modo cronometrado)
        else:  # conteudo — os blocos do dia (especifico + geral)
            pool = [q for q in banco if q["tag"] in plano["blocos"]]
            if not pool:
                print(cor("\n  sem questoes para os blocos de hoje; rodando aleatorias.\n", "dim"))
                pool = banco[:]
    elif a.tags:
        # aceita bloco (tag) e subtag (campo opcional 'sub'): './quiz.py uml'
        alvo = set(a.tags)
        pool = [q for q in banco if q["tag"] in alvo or alvo & set(q.get("sub", []))]
        if not pool:
            # subtag de microtopico recem-criada ainda nao tem questao etiquetada:
            # cai na busca por palavra-chave (subtags.py) para haver o que treinar
            # hoje. So entra quando o filtro exato deu zero — sessao de subtag
            # antiga (uml, padroes-projeto) continua exatamente como era.
            alvo_sub = [t for t in a.tags if t in SUBTAGS]
            pool = [q for q in banco if any(subtags.cobre(s, q) for s in alvo_sub)]
            if pool:
                print(cor(f"\n  nenhuma questao etiquetada com {', '.join(alvo_sub)} — "
                          f"peguei {len(pool)} por palavra-chave.", "dim"))
        if not pool:
            print(cor(f"\n  nenhuma questao com tags {a.tags}. Use --tags para listar.\n", "verm"))
            return
        # lembrete de banca: mostra a dica do bloco quando ha exatamente um
        if len(a.tags) == 1 and (BASE / "dicas" / f"{a.tags[0]}.md").exists():
            print(cor(f"\n  dica de banca deste bloco: ./quiz.py --dica {a.tags[0]}", "dim"))
    else:
        pool = banco[:]

    random.shuffle(pool)
    sel = pool[:n]

    res = rodar(sel, anotar=a.anotar)
    if res is None:
        return
    acertos, erradas, causas = res
    total = len(sel)
    pct = acertos / total * 100

    c = "verde" if pct >= 75 else "ama" if pct >= 60 else "verm"
    print(cor("  " + "-" * 40, "dim"))
    print(f"  Resultado: {cor(f'{acertos}/{total} ({pct:.0f}%)', c)}")

    # conteudos que caíram nesta sessao, e como voce foi em cada um
    from collections import defaultdict

    por_tag = defaultdict(lambda: [0, 0])
    ids_err = {q["id"] for q in erradas}
    for q in sel:
        por_tag[q["tag"]][0] += 1
        por_tag[q["tag"]][1] += q["id"] not in ids_err
    print(cor("\n  Conteudos desta sessao:", "b"))
    for t, (tot, ok) in sorted(por_tag.items(), key=lambda x: x[1][1] / x[1][0]):
        p_ = ok / tot * 100
        c_ = "verde" if p_ >= 75 else "ama" if p_ >= 60 else "verm"
        print(f"    {t:<16} {cor(f'{ok}/{tot}', c_)}")

    # persiste historico para --erradas e --stats
    agora = datetime.now().isoformat(timespec="seconds")
    for q in sel:
        rec = {"id": q["id"], "tag": q["tag"], "ok": q["id"] not in ids_err, "quando": agora}
        if q["id"] in causas:  # causa e opcional: so as erradas em que voce respondeu
            rec["causa"] = causas[q["id"]]
        hist["respostas"].append(rec)
    salvar_hist(hist, quem)

    print()
    # recuperando um dia atrasado (--dia)? credita naquele dia; senao, hoje.
    dia_reg = data_roteiro if a.dia is not None else None
    destino = f" ({dia_reg})" if dia_reg else ""
    r = input(f"  registrar em {csv_de(quem).name}{destino}? [S/n] ").strip().lower()
    if r in ("", "s", "sim"):
        registrar_no_csv(total, acertos, quem, dia=dia_reg)
    print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(cor("\n\n  interrompido.\n", "dim"))
        sys.exit(0)
