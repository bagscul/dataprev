#!/usr/bin/env python3
"""Leitura compartilhada do roteiro (progresso.csv) — usada pelo quiz.py e
pelo status.py para saberem, de forma consistente, o que estudar HOJE.

Cada dia do roteiro tem dois assuntos: o especifico (coluna 'tag') e o geral
(coluna 'secundario', em texto prefixado: "Portugues: ...", "Ingles: ...").
Este modulo resolve isso num plano com a LISTA de blocos do dia.
"""

import csv
import unicodedata
from datetime import date, timedelta
from pathlib import Path

# tags que nao sao bloco de conteudo, e sim tipo de dia
DIAS_ESPECIAIS = {"revisao", "simulado", "descanso", "prova"}

# prefixo do 'secundario' -> bloco (tag). Escala: adicione linhas aqui.
_SECUNDARIO = {
    "portugues": "portugues",
    "ingles": "ingles",
    "rlm": "rlm",
    "raciocinio": "rlm",
    "legislacao": "legislacao",
    "atualidades": "atualidades",
}


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower().strip()


def resolver_data(ref, hoje=None):
    """Converte uma referencia de dia em date. Aceita: 'hoje', 'ontem',
    'anteontem', um deslocamento como '-1'/'-2', ou 'AAAA-MM-DD'.
    Devolve None se nao entender."""
    hoje = hoje or date.today()
    if ref is None:
        return hoje
    r = _norm(ref)
    fixos = {"hoje": 0, "ontem": -1, "anteontem": -2, "amanha": 1}
    if r in fixos:
        return hoje + timedelta(days=fixos[r])
    try:  # deslocamento numerico: -1, -2, +1...
        return hoje + timedelta(days=int(r))
    except ValueError:
        pass
    try:  # data absoluta
        return date.fromisoformat(r)
    except ValueError:
        return None


def bloco_do_secundario(sec):
    """Mapeia o texto de 'secundario' para um bloco, ou None se nao for um
    bloco estudavel (ex: 'Questoes mistas', 'Correcao comentada')."""
    chave = _norm(sec).split(":")[0].strip()
    for prefixo, tag in _SECUNDARIO.items():
        if chave.startswith(prefixo):
            return tag
    return None


def linha_de_hoje(csv_path, hoje=None):
    """Devolve a linha do roteiro para hoje (dict), ou None."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        return None
    alvo = (hoje or date.today()).isoformat()
    with open(csv_path, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            if l["data"] == alvo:
                return l
    return None


def plano_de_hoje(csv_path, hoje=None):
    """Resolve o plano do dia. Devolve dict:
        tipo    -> 'conteudo' | 'revisao' | 'simulado' | 'descanso' | 'prova' | None
        blocos  -> lista de tags a estudar hoje (especifico + geral)
        foco, secundario, linha -> contexto para exibir
    None em 'tipo' significa que hoje nao esta no roteiro."""
    l = linha_de_hoje(csv_path, hoje)
    if l is None:
        return {"tipo": None, "blocos": [], "foco": "", "secundario": "", "linha": None}

    tag = l["tag"]
    if tag in DIAS_ESPECIAIS:
        return {"tipo": tag, "blocos": [], "foco": l["foco"],
                "secundario": l["secundario"], "linha": l}

    blocos = [tag]
    sec = bloco_do_secundario(l["secundario"])
    if sec and sec not in blocos:
        blocos.append(sec)
    return {"tipo": "conteudo", "blocos": blocos, "foco": l["foco"],
            "secundario": l["secundario"], "linha": l}


def pendentes(csv_path, hoje=None):
    """Dias de conteudo ja passados e ainda nao marcados como feitos.
    Devolve lista de dicts {data, dia, foco} do mais antigo ao mais novo."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        return []
    hoje = hoje or date.today()
    atrasados = []
    with open(csv_path, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            d = date.fromisoformat(l["data"])
            if d < hoje and l["feito"] != "1" and l["tag"] not in {"descanso", "prova"}:
                atrasados.append({"data": l["data"], "dia": l["dia"], "foco": l["foco"]})
    return atrasados
