#!/usr/bin/env python3
"""Importa as questoes das provas reais (provas/*.pdf) para banco-provas.json.

Uso:
    ./importar_provas.py              importa todas as provas de provas/
    ./importar_provas.py dataprev2024 importa so uma

As questoes entram com "ans": null, porque o caderno de questoes nao traz o
gabarito. Enquanto o gabarito nao for preenchido (veja ./gabarito.py), o quiz
ignora a questao. Isso e proposital: gabarito derivado por chute constroi
reflexo errado.

O bloco (tag) de cada questao vem da tabela do mapa correspondente em
notas/<prova>-mapa.md, que aponta o sub-bloco de cada numero.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).parent
PROVAS = BASE / "provas"
NOTAS = BASE / "notas"
SAIDA = BASE / "banco-provas.json"

# nomes de bloco usados nos mapas -> arquivo em erros/
TAGS = {
    # Os mapas usam ora o nome por extenso, ora o slug da tag. Os dois valem.
    "engenharia de software": "eng-software",
    "eng. de software": "eng-software",
    "eng software": "eng-software",
    "eng-software": "eng-software",
    "banco-dados": "banco-dados",
    "programacao": "programacao",
    "banco de dados": "banco-dados",
    "bi": "bi",
    "seguranca": "seguranca",
    "redes": "redes",
    # arquitetura de COMPUTADORES/SO nao e o bloco de arquitetura de SOFTWARE
    # do edital (Perfil 3): cai em prova de outro perfil e vai para orfaos.
    "arquitetura de computadores": "orfaos",
    "arquitetura de software": "arquitetura",
    "arquitetura": "arquitetura",
    "frontend": "frontend",
    "java": "java",
    "governanca": "governanca",
    "legislacao": "legislacao",
    "atualidades": "atualidades",
    "portugues": "portugues",
    "lingua portuguesa": "portugues",
    "ingles": "ingles",
    "lingua inglesa": "ingles",
    "rlm": "rlm",
    "raciocinio logico": "rlm",
    "raciocinio logico matematico": "rlm",
}

# Rodape de pagina. IGNORECASE nao e detalhe: sem ele, "FGV Conhecimento" (como
# sai do PDF) nao casava com "FGV CONHECIMENTO", e o rodape da pagina seguinte
# era emendado na ULTIMA alternativa da questao — em 52 das 432 questoes, junto
# com cabecalho de secao e ate o enunciado inteiro da prova discursiva.
LIXO = re.compile(
    r"pcimarkpci|pciconcursos\.com\.br|^\s*$"
    r"|FGV\s+CONHECIMENTO"
    r"|P[ÁA]GINA\s+\d+"
    r"|TIPO\s*\d*\s*[–\-]?\s*BRANCA",
    re.IGNORECASE,
)

# O texto do PDF perde figuras, codigo e tabelas (viram imagem). Questao que se
# apoia nisso fica impossivel de responder no terminal: marcamos e o quiz nao
# sorteia. Cuidado: "abaixo"/"a seguir" NAO entram aqui — em questao da FGV
# costumam apontar para afirmativas I/II/III que estao no proprio texto.
REFERE_IMAGEM = re.compile(
    r"\b(figura|imagem|gráfico|diagrama|ilustração|esquema|fluxograma"
    r"|código|trecho de programa|comando SQL|consulta SQL|modelo ER)\b",
    re.IGNORECASE,
)

# Titulo de secao do caderno, sozinho na linha. Irma do problema do rodape: o
# titulo nao e questao nem alternativa, entao o parser o emendava na ULTIMA
# alternativa da questao anterior ("...apontar a desigualdade social. Lingua
# Inglesa Use the following TEXT..."). Casa a LINHA INTEIRA de proposito —
# "Legislacao"/"Modulo"/"Realizacao" aparecem dentro de alternativas legitimas
# ("Bugs por Modulo.", "A realizacao de entrevistas...") e nao podem cortar.
CABECALHO_SECAO = re.compile(
    r"^(?:língua (?:portuguesa|inglesa)"
    r"|raciocínio lógico[ -]matemático"
    r"|atualidades"
    r"|conhecimentos específicos"
    r"|módulo\s+[IVX]+"
    r"|legislação (?:específica|institucional)"
    r"|noções de (?:sustentabilidade|administração pública|direito administrativo)"
    r"|história e geografia de rondônia"
    r"|realização"
    r"|rascunho"
    r"|prova discursiva"
    # Titulos que o PDF quebra em duas ou tres linhas: basta casar a PRIMEIRA,
    # porque a partir dai a alternativa ja esta encerrada e o resto e ignorado.
    r"|legislação acerca de segurança da"
    r"|noções de direitos humanos e"
    r"|legislação especial, noções dos direitos)$",
    re.IGNORECASE,
)

# A FGV imprime o texto de interpretacao UMA vez e o cobra em varias questoes
# seguidas. Como o parser so reconhece item numerado, esses textos se perdiam
# (e o comeco deles ainda por cima grudava na alternativa anterior): as 12
# questoes de Lingua Inglesa da Dataprev 2024 entravam citando um "TEXT" que
# nao estava em lugar nenhum — a Q14 ("What information is in TEXT?") e a Q21
# ficavam literalmente irrespondiveis. O texto capturado aqui e prefixado no
# enunciado de CADA questao do grupo, porque o quiz sorteia itens soltos e
# cada um precisa se sustentar sozinho.
MARCA_TEXTO = re.compile(
    r"use the following TEXT to answer the next (\w+) questions?", re.IGNORECASE
)
NUM_EXTENSO = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
               "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}


def sem_acento(t):
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c)).lower().strip()


def tag_de(texto):
    """Mapeia o nome de sub-bloco do mapa para o arquivo em erros/."""
    s = sem_acento(texto)
    # "Banco de Dados / BI" -> primeiro que casar
    for parte in re.split(r"[/,]", s):
        parte = parte.strip()
        if parte in TAGS:
            return TAGS[parte]
    # Busca por trecho: vale a chave que aparece MAIS CEDO no rotulo e, em
    # empate de posicao, a MAIS LONGA. Sem esses dois criterios a resolucao
    # dependia da ordem do dicionario, e errava duas vezes:
    #   "Legislacao (Seguranca da Informacao...)" caia em `seguranca`, porque
    #   "seguranca" vinha antes de "legislacao" no TAGS;
    #   "Arquitetura de computadores (SO)" caia em `arquitetura`, porque
    #   "arquitetura" e prefixo da chave mais especifica.
    achados = [(s.find(c), -len(c), t) for c, t in TAGS.items() if c in s]
    if achados:
        return min(achados)[2]
    return "orfaos"


def tags_do_mapa(prova):
    """Le notas/<prova>-mapa.md e devolve {numero_questao: tag}."""
    mapa = NOTAS / f"{prova}-mapa.md"
    if not mapa.exists():
        return {}
    tags = {}
    for linha in mapa.read_text(encoding="utf-8").splitlines():
        # linhas da tabela de especificos: | 41 | Tema | Sub-bloco |
        m = re.match(r"\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|", linha)
        if m:
            tags[int(m.group(1))] = tag_de(m.group(3))
            continue
        # tabela de blocos gerais: | Lingua Portuguesa | 1-12 |
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*[–\-]\s*(\d+)\s*\|", linha)
        if m:
            t = tag_de(m.group(1))
            for n in range(int(m.group(2)), int(m.group(3)) + 1):
                tags.setdefault(n, t)
    return tags


def texto_do_pdf(caminho):
    import pypdf

    r = pypdf.PdfReader(caminho)
    linhas = []
    for pag in r.pages:
        primeira_da_pagina = True
        for l in (pag.extract_text() or "").splitlines():
            if LIXO.search(l):
                continue
            linhas.append((l.rstrip(), primeira_da_pagina))
            primeira_da_pagina = False
    return linhas


def textos_base(linhas):
    """{numero_da_questao: texto} dos grupos que compartilham um texto-base.

    O marcador ("...answer the next six questions.") diz quantas questoes o
    texto cobre; o corpo vai dali ate a primeira linha que seja so um numero,
    que e justamente a primeira questao do grupo.
    """
    mapa = {}
    i = 0
    while i < len(linhas):
        m = MARCA_TEXTO.search(linhas[i][0])
        if not m:
            i += 1
            continue
        quantas = NUM_EXTENSO.get(m.group(1).lower())
        corpo, j, inicio = [], i + 1, None
        while j < len(linhas):
            n = re.match(r"^\s*(\d{1,2})\s*$", linhas[j][0].strip())
            if n:
                inicio = int(n.group(1))
                break
            corpo.append(linhas[j][0].strip())
            j += 1
        if quantas and corpo and inicio is not None:
            texto = re.sub(r"\s+", " ", " ".join(corpo)).strip()
            for k in range(inicio, inicio + quantas):
                mapa[k] = texto
        i = max(j, i + 1)
    return mapa


def parsear(linhas):
    """Quebra o texto corrido em questoes: numero, enunciado, 5 alternativas.

    `linhas` e uma lista de (texto, virou_pagina).

    Regra que importa: a alternativa NAO atravessa a virada de pagina. Depois
    do rodape vem cabecalho de secao ("MODULO II", "CONHECIMENTOS
    ESPECIFICOS"), o nome da organizadora ("Realizacao") ou ate o enunciado da
    prova discursiva -- e o parser antigo emendava tudo isso na ULTIMA
    alternativa. Se a alternativa de fato terminou antes da quebra (que e o
    caso em todas as 432 questoes ja importadas), cortar ali e correto.
    """
    questoes = []
    atual = None
    apos_quebra = False
    esperado = 1  # so aceita o PROXIMO numero da sequencia (veja abaixo)
    for l, virou_pagina in linhas:
        if virou_pagina:
            apos_quebra = True
        # Inicio de questao: linha com so o numero -- e que seja o proximo da
        # sequencia. Sem essa segunda condicao, um "2" solto dentro de uma
        # questao de RLM abria uma questao fantasma (era o caso da cnsal-ads
        # Q2, que entrava com as alternativas de outra questao).
        m = re.match(r"^\s*(\d{1,2})\s*$", l)
        if m and int(m.group(1)) == esperado:
            if atual:
                questoes.append(atual)
            atual = {"num": esperado, "enunciado": [], "alts": []}
            esperado += 1
            apos_quebra = False
            continue
        if atual is None:
            continue
        # alternativa: (A) texto
        m = re.match(r"^\s*\(([A-E])\)\s*(.*)$", l)
        if m:
            atual["alts"].append([m.group(2)])
            apos_quebra = False
            continue
        # Fim da secao (titulo sozinho na linha) ou inicio de um texto-base:
        # a alternativa corrente acabou, mesmo sem virada de pagina.
        if CABECALHO_SECAO.match(l.strip()) or MARCA_TEXTO.search(l):
            apos_quebra = True
            continue
        if atual["alts"]:
            if not apos_quebra:  # continuacao da ultima alternativa
                atual["alts"][-1].append(l.strip())
        else:
            atual["enunciado"].append(l.strip())
    if atual:
        questoes.append(atual)

    limpas = []
    for q in questoes:
        if len(q["alts"]) != 5:
            continue  # questao truncada/quebrada na extracao: descarta
        limpas.append(
            {
                "num": q["num"],
                "q": re.sub(r"\s+", " ", " ".join(q["enunciado"])).strip(),
                "alts": [re.sub(r"\s+", " ", " ".join(a)).strip() for a in q["alts"]],
            }
        )
    return limpas


def main():
    args = sys.argv[1:]
    tudo = "--tudo" in args
    alvos = [a for a in args if not a.startswith("-")] or [
        p.stem for p in sorted(PROVAS.glob("*.pdf"))
    ]

    antigo = {}
    if SAIDA.exists():
        for q in json.loads(SAIDA.read_text(encoding="utf-8")):
            antigo[(q["prova"], q["num"])] = q
    # Provas ja importadas guardam um RECORTE do caderno: das 80 questoes da
    # ALERO, por exemplo, ficaram so as de TI (as de Historia e Geografia de
    # Rondonia foram descartadas de proposito). Reimportar sem trava
    # ressuscitaria as descartadas. Por padrao mantemos o recorte; --tudo
    # traz o caderno inteiro.
    ja_tem = {p for p, _ in antigo}

    banco = []
    for prova in alvos:
        pdf = PROVAS / f"{prova}.pdf"
        if not pdf.exists():
            print(f"  {prova}: PDF nao encontrado, pulando.")
            continue
        tags = tags_do_mapa(prova)
        linhas = texto_do_pdf(pdf)
        qs = parsear(linhas)
        bases = textos_base(linhas)
        if prova in ja_tem and not tudo:
            fora = [q["num"] for q in qs if (prova, q["num"]) not in antigo]
            if fora:
                print(f"  {prova}: {len(fora)} questoes fora do recorte atual, mantidas de fora "
                      f"(use --tudo para trazer): {fora[0]}–{fora[-1]}")
            qs = [q for q in qs if (prova, q["num"]) in antigo]
        for q in qs:
            chave = (prova, q["num"])
            anterior = antigo.get(chave, {})
            base = bases.get(q["num"])
            banco.append(
                {
                    "prova": prova,
                    "num": q["num"],
                    "tag": tags.get(q["num"], "orfaos"),
                    "q": f"{base}\n\n{q['q']}" if base else q["q"],
                    "alts": q["alts"],
                    # gabarito: preenchido por ./gabarito.py, nunca por chute
                    "ans": anterior.get("ans"),
                    "why": anterior.get("why", ""),
                    "erradas": anterior.get("erradas", {}),
                    "fonte": f"FGV {prova} Q{q['num']}",
                    # o PDF perdeu a figura/codigo: nao da pra responder no terminal
                    "requer_imagem": bool(REFERE_IMAGEM.search(q["q"])),
                    # anulada e marcada a mao; preserva entre reimportacoes
                    "anulada": anterior.get("anulada", False),
                }
            )
        desta = [q for q in banco if q["prova"] == prova]
        com_gab = sum(1 for q in desta if q["ans"] is not None)
        com_img = sum(1 for q in desta if q["requer_imagem"])
        print(f"  {prova}: {len(qs)} questoes ({com_gab} com gabarito, {com_img} dependem de figura)")

    SAIDA.write_text(json.dumps(banco, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n  {len(banco)} questoes em {SAIDA.name}")
    sem_gab = sum(1 for q in banco if q["ans"] is None)
    if sem_gab:
        print(f"  {sem_gab} ainda sem gabarito — o quiz vai ignora-las.")
        print("  preencha com: ./gabarito.py <prova> \"1-C 2-A 3-E ...\"")


if __name__ == "__main__":
    main()
