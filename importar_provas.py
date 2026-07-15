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
    "engenharia de software": "eng-software",
    "eng. de software": "eng-software",
    "eng software": "eng-software",
    "programacao": "programacao",
    "banco de dados": "banco-dados",
    "bi": "bi",
    "seguranca": "seguranca",
    "redes": "redes",
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

LIXO = re.compile(r"pcimarkpci|pciconcursos\.com\.br|^\s*$|PÁGINA \d+|TIPO BRANCA|FGV CONHECIMENTO")

# O texto do PDF perde figuras, codigo e tabelas (viram imagem). Questao que se
# apoia nisso fica impossivel de responder no terminal: marcamos e o quiz nao
# sorteia. Cuidado: "abaixo"/"a seguir" NAO entram aqui — em questao da FGV
# costumam apontar para afirmativas I/II/III que estao no proprio texto.
REFERE_IMAGEM = re.compile(
    r"\b(figura|imagem|gráfico|diagrama|ilustração|esquema|fluxograma"
    r"|código|trecho de programa|comando SQL|consulta SQL|modelo ER)\b",
    re.IGNORECASE,
)


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
    for chave, tag in TAGS.items():
        if chave in s:
            return tag
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
        for l in (pag.extract_text() or "").splitlines():
            if not LIXO.search(l):
                linhas.append(l.rstrip())
    return linhas


def parsear(linhas):
    """Quebra o texto corrido em questoes: numero, enunciado, 5 alternativas."""
    questoes = []
    atual = None
    for l in linhas:
        # inicio de questao: linha com so o numero
        m = re.match(r"^\s*(\d{1,2})\s*$", l)
        if m and 1 <= int(m.group(1)) <= 90:
            if atual:
                questoes.append(atual)
            atual = {"num": int(m.group(1)), "enunciado": [], "alts": []}
            continue
        if atual is None:
            continue
        # alternativa: (A) texto
        m = re.match(r"^\s*\(([A-E])\)\s*(.*)$", l)
        if m:
            atual["alts"].append([m.group(2)])
            continue
        if atual["alts"]:
            atual["alts"][-1].append(l.strip())  # continuacao da ultima alternativa
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
    alvos = sys.argv[1:] or [p.stem for p in sorted(PROVAS.glob("*.pdf"))]

    antigo = {}
    if SAIDA.exists():
        for q in json.loads(SAIDA.read_text(encoding="utf-8")):
            antigo[(q["prova"], q["num"])] = q

    banco = []
    for prova in alvos:
        pdf = PROVAS / f"{prova}.pdf"
        if not pdf.exists():
            print(f"  {prova}: PDF nao encontrado, pulando.")
            continue
        tags = tags_do_mapa(prova)
        qs = parsear(texto_do_pdf(pdf))
        for q in qs:
            chave = (prova, q["num"])
            anterior = antigo.get(chave, {})
            banco.append(
                {
                    "prova": prova,
                    "num": q["num"],
                    "tag": tags.get(q["num"], "orfaos"),
                    "q": q["q"],
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
