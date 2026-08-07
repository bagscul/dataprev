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
# sorteia.
#
# A regra ANTIGA era so a lista de termos, e trancava 51 questoes — das quais
# 45 nao dependiam de figura nenhuma. Ela casava "Código Florestal" (mpu Q20),
# "Código Penal" (tjrj Q70), "Código de Ética" (mpu Q32), "esquema de relação
# R(A,B,C)" escrito por extenso no proprio enunciado (cnsal-bd Q41/Q46),
# "esquema Estrela/Snowflake" como conceito (cnsal-bd Q51/Q63), "assinale o
# comando SQL que..." cuja resposta esta nas ALTERNATIVAS (cnsal-ads Q67), e
# ate questoes cujo codigo o pypdf extraiu direitinho e esta ali no enunciado
# (mpu Q51 numpy, Q59 CREATE ROLE, Q75 HTML/CSS, Q76 sealed, tjrj2 Q55 Spring).
#
# A regra NOVA exige tres coisas:
#   1. DEIXIS junto do termo — a palavra que aponta para FORA do texto
#      ("observe o diagrama abaixo"). Sem ela, "codigo"/"esquema"/"diagrama"
#      sao so vocabulario tecnico. "Figura 1" tambem conta, por si so.
#   2. AUSENCIA do artefato no proprio enunciado: se o pypdf trouxe o SELECT,
#      o <div> ou o @RestController, a questao se sustenta e vale o sorteio.
#   3. Alternativa vazia — sinal estrutural, nao de palavra: se a alternativa
#      e um simbolo que virou imagem (mpu Q41, os simbolos BPMN), nao ha o que
#      responder. Esta e a unica das tres que dispensa a lista de termos.
# Resultado: 6 questoes fora do sorteio (mpu 41/52/63/64/67 e dataprev2024 49,
# esta ultima com o codigo Java confirmadamente ausente da camada de texto).
_ARTEFATO = (r"figuras?|imagem|gr[áa]ficos?|diagramas?|ilustra[çc][ãa]o"
             r"|esquemas?|fluxogramas?|c[óo]digo|trecho de programa"
             r"|comando SQL|consulta SQL|modelo ER")

_DEIXIS = (r"a seguir|abaixo|acima|ao lado|adiante|seguintes?|apresentad\w+"
           r"|ilustrad\w+|mostrad\w+|exibid\w+|observe|analise")

# Suporte visual que E o proprio enunciado: charge, cartum, poster. Aqui o
# deitico esta no artigo/demonstrativo ("this poster", "a charge a seguir"), e
# nao numa palavra de apontamento — "The word 'because' in this poster
# introduces a(n)" nao casa nenhum dos dois lados da regra geral, mas sem a
# imagem a questao nao existe. Vale so quando a imagem E o texto da questao:
# "cartoon" citado dentro de uma alternativa nao tranca nada, porque a busca e
# feita apenas no enunciado.
_SUPORTE_VISUAL = re.compile(
    r"\b(?:this|the|that)\s+(?:poster|cartoon|comic strip|caricature)\b"
    r"|\b(?:a|na|da|desta?|nesta?)\s+(?:charge|tirinha|cartum)\b",
    re.IGNORECASE,
)

REFERE_IMAGEM = re.compile(
    rf"(?:{_DEIXIS})[^.;]{{0,60}}?(?:{_ARTEFATO})"
    rf"|(?:{_ARTEFATO})[^.;]{{0,60}}?(?:{_DEIXIS})"
    rf"|figuras?\s+\d"
    rf"|{_SUPORTE_VISUAL.pattern}",
    re.IGNORECASE,
)

# O artefato veio junto na extracao: SQL, marcacao, codigo. Nao ha o que perder.
ARTEFATO_INLINE = re.compile(
    r"\bSELECT\b[^.]*\bFROM\b"
    r"|\bINSERT\s+INTO\b|\bCREATE\s+(?:TABLE|ROLE|VIEW|INDEX|FUNCTION)\b"
    r"|\bGRANT\b[^.]*\bTO\b|\bUPDATE\b[^.]*\bSET\b|\bDROP\s+TABLE\b"
    r"|\bALTER\s+TABLE\b"
    r"|</?\w+[\s/>]"
    r"|\bimport\s+\w+|\bfrom\s+\w+\s+import\b"
    r"|\b(?:public|private|protected)\s+\w+"
    r"|\bdef\s+\w+\s*\(|\bclass\s+\w+\b"
    r"|@\w+\s"
    r"|\w+\s*=\s*\w+\s*\("
    r"|\{[^{}]*\}",
)


# Excecao declarada, e nao regra: questao em que a figura E o dado, mas cuja
# redacao nao aciona a REFERE_IMAGEM. A cprm-ads Q17 diz "A Figura mostra como
# 17 caixas cubicas foram organizadas" — o artefato e SUJEITO do verbo, e a
# lista de deixis so tem o participio ("mostrada"), nao a forma do presente.
#
# Por que uma lista e nao mais uma regra: acrescentar os verbos no presente
# trancaria outras tres questoes que se sustentam sozinhas — a nav-med Q23 traz
# os pontos A(3,1) e B(6,3) no texto, a nav-med Q30 teve a tabela transcrita na
# extracao, e a nav-eng Q70 NARRA o diagrama BPMN por escrito, sem imprimi-lo.
# Da para calibrar um regex de tres condicoes que acerte so a Q17, mas seria
# uma regra ajustada a um unico exemplo. Enquanto o caso for um, a lista e mais
# honesta — e, por morar aqui e nao no JSON, sobrevive a reimportacao.
DEPENDE_DE_FIGURA_MANUAL = {
    ("cprm-ads", 17),  # 17 caixas empilhadas: a contagem so existe no desenho
}


def depende_de_figura(enunciado, alts, prova=None, num=None):
    """A questao e irrespondivel sem o que o PDF perdeu?"""
    if (prova, num) in DEPENDE_DE_FIGURA_MANUAL:
        return True
    if any(not a.strip() for a in alts):
        return True
    if ARTEFATO_INLINE.search(enunciado):
        return False
    return bool(REFERE_IMAGEM.search(enunciado))

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
    r"|informática"
    r"|conhecimentos específicos"
    r"|metodologia científica"
    r"|estatística"
    r"|módulo\s+[IVX]+"
    r"|legislação (?:específica|institucional)"
    r"|legislação e noções de ética"
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
# Tres formulas, porque a FGV nao padroniza o comando entre cadernos: a
# Dataprev 2024 escreve "Use the following TEXT to answer the next six
# questions"; a NAV Brasil 2026 (nivel medio) escreve "Read Text IV and answer
# the four questions that follow it"; e o portugues da NAV Brasil (nivel
# superior) escreve "Atencao! O texto a seguir refere-se as duas proximas
# questoes". Nos tres casos o que interessa e o numero por extenso, entao a
# quantidade fica num unico grupo de captura.
MARCA_TEXTO = re.compile(
    r"(?:use the following TEXT to answer the next"
    r"|read (?:the )?text\s+[IVX]+\s+and answer the)"
    r"\s+(\w+)\s+questions?"
    r"|os?\s+textos?\s+a seguir\s+refere[m]?-se\s+[àa]s\s+(\w+)\s+"
    r"pr[óo]ximas\s+quest[õo]es",
    re.IGNORECASE,
)
NUM_EXTENSO = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
               "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
               "duas": 2, "três": 3, "tres": 3, "quatro": 4, "cinco": 5,
               "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10}

# Quarta forma, e a mais economica de todas: a Receita Federal 2023 e o
# Pesquisador do CPRM 2025 nao escrevem formula nenhuma — imprimem so "Text I"
# e emendam o texto. Sem a formula nao ha numero por extenso dizendo quantas
# questoes o texto cobre, entao o alcance vem da POSICAO: cada texto vale ate o
# proximo marcador, e o ultimo vale ate o cabecalho da secao seguinte.
# Duas marcas sem contagem, tratadas pela mesma regra de alcance por posicao:
# o "Text I" solto da Receita Federal 2023 e a abertura de secao do CPRM 2025
# ("As questoes da prova de Lingua Inglesa referem-se ao TEXTO a seguir:"),
# que vale para o bloco inteiro.
MARCA_TEXTO_NUA = re.compile(
    r"^TEXTO?\s+[IVX]+$"
    r"|^as quest[õo]es da prova de .{3,40}?\s+refere[m]?-se ao(?:\s+TEXTO a)?$",
    re.IGNORECASE,
)

# Onde a prova objetiva acaba: dali em diante nao ha questao numerada, e
# qualquer "TEXTO I" pertence a discursiva ou ao rascunho.
FIM_DA_OBJETIVA = re.compile(
    r"^(?:prova discursiva|reda[çc][ãa]o|rascunho|realização)$", re.IGNORECASE)


def quantas_questoes(m):
    """Numero de questoes que o texto-base cobre, venha de qual grupo vier."""
    achado = next((g for g in m.groups() if g), None)
    return NUM_EXTENSO.get(achado.lower()) if achado else None


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
    # A busca e por PALAVRA INTEIRA. Sem o \b, a chave de duas letras "bi"
    # casava DENTRO de outra palavra e levava dez questoes gerais do MPU para
    # Business Intelligence: "Nocoes de Sustentabilidade" (sustenta-BI-lidade,
    # Q16-20) e "Nocoes de Direitos Humanos ... e de Acessibilidade"
    # (acessi-BI-lidade, Q21-25). Alem de sujar `./quiz.py bi`, isso as fazia
    # valer 2,5x no --simulado, porque `bi` nao esta em GERAIS (quiz.py).
    achados = [(m.start(), -len(c), t)
               for c, t in TAGS.items()
               if (m := re.search(rf"\b{re.escape(c)}\b", s))]
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


# A FGV SUBLINHA o termo que a questao manda analisar ("assinale a opcao em que
# o termo sublinhado...", "o elemento destacado em..."). Nem o pypdf nem o
# pdftotext preservam sublinhado, entao esse termo chegava ao quiz indistinguivel
# do resto da frase — e a questao virava adivinhacao: das 44 questoes que citam a
# marcacao, a maioria e de portugues, o bloco mais pesado do Modulo I.
#
# No PDF o sublinhado nao e atributo de fonte: e um retangulo fino desenhado sob
# a palavra. O PyMuPDF le esses desenhos, e o texto recortado logo acima de cada
# reta e exatamente o trecho sublinhado. Conferido nas 15 provas: das 125 retas
# encontradas, as unicas que nao casam com nenhuma questao sao as da capa
# ("caderno de provas", "Boa prova!").
#
# Marcamos com «...» — o quiz mostra assim, e o candidato ve o que a banca
# grifou. Palavra de comando ja enfatizada pela banca (nao, incorreta, exceto)
# fica de fora: ela nao muda a resposta e so poluiria o enunciado.
MARCADOR = ("«", "»")

# So restauramos a marca na questao que PEDE a marca. A FGV sublinha por
# enfase em muito lugar, e marcar tudo cria ruido — pior, borda de tabela e
# reta de rodape entram como falso sublinhado (a cnsal-ads Q51 recebeu
# «Título_PL» e «150», que sao celulas de uma tabela). Quando o enunciado nao
# manda olhar a marca, a ausencia dela nao atrapalha ninguem.
CITA_MARCACAO = re.compile(
    r"sublinhad\w+|underlined|em negrito|em destaque|destacad\w+|grifad\w+",
    re.IGNORECASE,
)
COMANDO_ENFATIZADO = {
    "nao", "incorreta", "incorreto", "correta", "correto", "exceto",
    "apenas", "somente", "incorretamente", "corretamente",
}


def _compacto(texto):
    """Devolve (texto sem espacos e sem acento, mapa de indices para o original)."""
    saida, mapa = [], []
    for i, c in enumerate(texto):
        if c.isspace():
            continue
        base = unicodedata.normalize("NFKD", c)
        base = "".join(ch for ch in base if not unicodedata.combining(ch)).lower()
        base = {"“": '"', "”": '"', "’": "'", "‘": "'", "–": "-"}.get(base, base)
        if base:
            saida.append(base[0])
            mapa.append(i)
    return "".join(saida), mapa


def marcacoes_do_pdf(caminho):
    """Trechos sublinhados no PDF, do mais longo para o mais curto."""
    try:
        import fitz
    except ImportError:  # sem PyMuPDF o importador segue funcionando, sem marca
        return []
    doc = fitz.open(caminho)
    achados = set()
    for pagina in doc:
        for desenho in pagina.get_drawings():
            r = desenho["rect"]
            # reta fina e do tamanho de uma palavra ou trecho: e sublinhado.
            # Larguras maiores sao regua de cabecalho e borda de tabela.
            if r.height >= 2.0 or not (8 < r.width < 260):
                continue
            faixa = fitz.Rect(r.x0 - 1, r.y0 - 9.5, r.x1 + 1, r.y0 - 0.5)
            trecho = " ".join(pagina.get_text("text", clip=faixa).split())
            if not trecho or len(trecho) > 120:
                continue
            nucleo = re.sub(r"^\W+|\W+$", "", trecho).lower()
            if len(nucleo) < 3 or sem_acento(nucleo) in COMANDO_ENFATIZADO:
                continue
            achados.add(trecho)
    return sorted(achados, key=len, reverse=True)


def marcas_uteis(marcas, campos):
    """Filtra as marcas que identificam um trecho SO.

    O sublinhado vive numa alternativa especifica, mas a lista vem da prova
    inteira — e sem esta trava um trecho curto grifado na Q9 ("de um",
    "alguns") era marcado tambem na Q40, em toda parte onde a sequencia de
    letras aparecesse. Foram 351 questoes alteradas na primeira tentativa,
    para 42 que precisavam. Vale a marca que casa em UM unico campo do
    caderno: e o proprio sinal de que ela identifica aquele trecho.
    """
    compactos = [_compacto(c)[0] for c in campos]
    uteis = []
    for m in marcas:
        agulha, _ = _compacto(m)
        if agulha and sum(1 for c in compactos if agulha in c) == 1:
            uteis.append(m)
    return uteis


def marcar(texto, marcas):
    """Envolve em «...» os trechos que a banca sublinhou."""
    if not texto or not marcas:
        return texto
    alvo, mapa = _compacto(texto)
    intervalos = []
    for m in marcas:
        agulha, _ = _compacto(m)
        if not agulha:
            continue
        pos = alvo.find(agulha)
        if pos < 0:
            continue
        ini, fim = mapa[pos], mapa[pos + len(agulha) - 1] + 1
        # o recorte do PDF as vezes corta palavra no meio ("Após d", "aprese"):
        # se o trecho nao comeca e termina em fronteira de palavra, e lixo.
        antes = texto[ini - 1] if ini > 0 else " "
        depois = texto[fim] if fim < len(texto) else " "
        if antes.isalnum() or depois.isalnum():
            continue
        # nao marca dentro de trecho ja marcado (o mais longo entrou primeiro)
        if any(a <= ini < b or a < fim <= b for a, b in intervalos):
            continue
        intervalos.append((ini, fim))
    saida = texto
    for ini, fim in sorted(intervalos, reverse=True):
        saida = saida[:ini] + MARCADOR[0] + saida[ini:fim] + MARCADOR[1] + saida[fim:]
    return saida


def marcar_alternativas(alts, marcas):
    """Marca as alternativas — ou todas, ou nenhuma.

    Marcacao PARCIAL e pior do que nenhuma: quando a banca sublinha um termo em
    cada alternativa e o recorte so recupera parte deles, a formatacao vira
    pista. Na cnsal-ads Q7 a unica alternativa que ficaria sem marca era
    exatamente o gabarito — o candidato acertaria pelo artefato, nao pelo
    portugues. Sao 18 questoes nessa situacao; nelas o texto fica como veio, e
    a explicacao (que cobre as cinco alternativas) sustenta o item.
    """
    marcadas = [marcar(a, marcas) for a in alts]
    if any(MARCADOR[0] in a for a in marcadas) and not all(
            MARCADOR[0] in a for a in marcadas):
        return alts
    return marcadas


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


def prosa(corpo):
    """O corpo capturado e texto de leitura, ou so o rotulo e a fonte?

    Quando o "texto" e uma IMAGEM (o poster e o cartum da NAV Brasil 2026), a
    camada de texto do PDF so devolve "TEXT III" e a linha de credito. Prefixar
    isso no enunciado suja questoes que se sustentam sozinhas (a analogia
    "Height is to high as" nao precisa do desenho) sem devolver nada em troca.
    """
    util = [l for l in corpo
            if not re.match(r"^TEXT\s+[IVX]+$", l, re.IGNORECASE)
            and not re.match(r"^(?:adapted\s+)?from:", l, re.IGNORECASE)]
    return len(" ".join(util).split()) >= 10


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
        quantas = quantas_questoes(m)
        corpo, j, inicio = [], i + 1, None
        while j < len(linhas):
            n = re.match(r"^\s*(\d{1,2})\s*$", linhas[j][0].strip())
            if n:
                inicio = int(n.group(1))
                break
            # Outro marcador antes da primeira questao: os textos sao vizinhos
            # de coluna na mesma pagina (NAV Brasil, TEXT II ao lado do TEXT
            # III). Sem este corte, o comando e a fonte do texto seguinte
            # entrariam no corpo do anterior.
            if MARCA_TEXTO.search(linhas[j][0]):
                break
            corpo.append(linhas[j][0].strip())
            j += 1
        if quantas and corpo and inicio is not None and prosa(corpo):
            texto = re.sub(r"\s+", " ", " ".join(corpo)).strip()
            for k in range(inicio, inicio + quantas):
                mapa[k] = texto
        i = max(j, i + 1)
    for k, texto in textos_base_nus(linhas).items():
        mapa.setdefault(k, texto)  # a formula explicita, quando existe, manda
    return mapa


def textos_base_nus(linhas):
    """{numero_da_questao: texto} dos textos marcados so por "Text I".

    Sem a formula que diz quantas questoes o texto cobre, o alcance sai da
    posicao: um texto vale ate a questao anterior ao proximo marcador, e o
    ultimo vale ate a ultima questao antes do cabecalho da secao seguinte.
    """
    marcas = []
    ultima_vista = 0
    for i, (linha, _) in enumerate(linhas):
        s0 = linha.strip()
        # A discursiva do CPRM tambem abre com "TEXTO I", so que ali nao ha
        # questao numerada: sem este corte, o texto da redacao era prefixado
        # nas 30 questoes objetivas do inicio do caderno.
        if FIM_DA_OBJETIVA.match(s0):
            break
        n = re.match(r"^\s*(\d{1,2})\s*$", s0)
        if n:
            ultima_vista = max(ultima_vista, int(n.group(1)))
        if not MARCA_TEXTO_NUA.match(s0):
            continue
        corpo, j, inicio = [], i + 1, None
        while j < len(linhas):
            s = linhas[j][0].strip()
            n = re.match(r"^\s*(\d{1,2})\s*$", s)
            if n:
                inicio = int(n.group(1))
                break
            if MARCA_TEXTO_NUA.match(s) or CABECALHO_SECAO.match(s):
                break
            # O PDF quebra "...refere-se ao TEXTO a / seguir:" em duas linhas;
            # a segunda e rabo do marcador, nao inicio do texto.
            if not corpo and re.match(r"^(?:TEXTO\s+a\s+)?seguir:?$", s,
                                      re.IGNORECASE):
                j += 1
                continue
            corpo.append(s)
            j += 1
        # A questao que abre o grupo tem de vir DEPOIS das ja vistas. Se o
        # numero encontrado retrocede, o "texto" nao pertence a prova objetiva
        # (e o caso da redacao, cujo comando cita "20 (vinte) linhas").
        if inicio is None or inicio <= ultima_vista:
            continue
        # prosa() barra o poster e o cartum, em que o "texto" e uma imagem e a
        # camada de texto do PDF devolve so o rotulo e a linha de credito.
        # Mesmo sem corpo aproveitavel a marca entra na lista, porque ela
        # delimita o alcance do texto ANTERIOR — foi o que faltou na primeira
        # versao desta funcao, que estendia o Text I da NAV Brasil por cima das
        # questoes do poster (Q51–Q56).
        texto = re.sub(r"\s+", " ", " ".join(corpo)).strip() if prosa(corpo) else None
        marcas.append((i, inicio, texto))

    mapa = {}
    for k, (linha_marca, inicio, texto) in enumerate(marcas):
        if not texto:
            continue
        if k + 1 < len(marcas):
            fim = marcas[k + 1][1] - 1
        else:
            fim = ultima_questao_da_secao(linhas, linha_marca)
        for n in range(inicio, (fim or inicio) + 1):
            mapa[n] = texto
    return mapa


def ultima_questao_da_secao(linhas, desde):
    """Numero da ultima questao antes do proximo cabecalho de secao."""
    ultima = None
    for linha, _ in linhas[desde:]:
        s = linha.strip()
        if CABECALHO_SECAO.match(s):
            break
        n = re.match(r"^\s*(\d{1,2})\s*$", s)
        if n:
            ultima = int(n.group(1))
    return ultima


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
        marcas = marcacoes_do_pdf(pdf)
        linhas = texto_do_pdf(pdf)
        qs = parsear(linhas)
        bases = textos_base(linhas)
        marcas = marcas_uteis(marcas, [c for q in qs for c in [q["q"], *q["alts"]]])
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
            texto_q = f"{base}\n\n{q['q']}" if base else q["q"]
            pede = bool(CITA_MARCACAO.search(q["q"]))
            banco.append(
                {
                    "prova": prova,
                    "num": q["num"],
                    "tag": tags.get(q["num"], "orfaos"),
                    "q": texto_q if not pede else marcar(texto_q, marcas),
                    "alts": marcar_alternativas(q["alts"], marcas) if pede
                            else q["alts"],
                    # gabarito: preenchido por ./gabarito.py, nunca por chute
                    "ans": anterior.get("ans"),
                    "why": anterior.get("why", ""),
                    "erradas": anterior.get("erradas", {}),
                    "fonte": f"FGV {prova} Q{q['num']}",
                    # o PDF perdeu a figura/codigo: nao da pra responder no terminal
                    "requer_imagem": depende_de_figura(q["q"], q["alts"], prova, q["num"]),
                    # anulada e marcada a mao; preserva entre reimportacoes
                    "anulada": anterior.get("anulada", False),
                }
            )
            # A subtag tambem e etiquetada a mao (questao de prova nao nasce com
            # ela) e tambem tem de sobreviver a reimportacao — senao o ranking do
            # ./fraquezas.py perde a granularidade sem ninguem perceber. Fica
            # ausente quando nao ha etiqueta, porque o campo e opcional: o
            # ./valida.py so cobra 'sub' no banco.json.
            if anterior.get("sub"):
                banco[-1]["sub"] = anterior["sub"]
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
