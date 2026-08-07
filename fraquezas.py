#!/usr/bin/env python3
"""fraquezas.py — ranqueia os MICROTOPICOS onde voce mais erra, para mirar a
geracao de questao nova (e o estudo) no que realmente esta doendo.

O bloco (a 'tag') e grosso demais para isso: 'portugues' sao 90 questoes e sete
erros seus em sete assuntos diferentes. Quem tem a granularidade certa e a
SUBTAG (subtags.py) — o mesmo vocabulario do campo 'sub' das questoes e da
linha '- **sub:**' do caderno de erros.

Fontes (leitura pura, nao altera nada):
  erros/*.md        o caderno — cada '## entrada' com '- **sub:**' vira um erro
                    contado no microtopico
  historico*.json   as respostas do quiz, de onde sai a CAUSA do erro
                    (conceitual x armadilha) e a taxa de acerto
  banco.json +      quantas questoes JA existem sobre o microtopico — e o que
  banco-provas.json diz se vale gerar mais ou se o buraco e de estudo, nao de banco

Uso:
    ./fraquezas.py              ranking completo
    ./fraquezas.py --top 5      so os 5 piores
    ./fraquezas.py --sem-sub    entradas do caderno ainda sem etiqueta (com sugestao)
    ./fraquezas.py --prompt     briefing pronto para gerar questao dos piores
    ./fraquezas.py --quem geys  usa o historico de outra pessoa
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import subtags
from quiz import APOSTILA, carregar_originais, carregar_provas, hist_de

BASE = Path(__file__).parent
C = {"r": "\033[0m", "b": "\033[1m", "dim": "\033[2m",
     "verde": "\033[32m", "verm": "\033[31m", "ama": "\033[33m", "ciano": "\033[36m"}


def cor(t, c):
    return f"{C[c]}{t}{C['r']}"


# --- caderno de erros -------------------------------------------------------
# '## titulo <!-- auto <id> -->' — o marcador e opcional (entrada escrita a mao
# nao tem), e e ele que liga a entrada a resposta gravada no historico.
RX_ENTRADA = re.compile(r"^##\s+(.*?)\s*(?:<!--\s*auto\s+(\S+)\s*-->)?\s*$", re.M)
RX_SUB = re.compile(r"^-\s*\*\*sub:\*\*\s*(.+?)\s*$", re.M)
RX_E = re.compile(r"^-\s*\*\*E:\*\*\s*(.+?)\s*$", re.M)
RX_DATA = re.compile(r"\|\s*(\d{2}/\d{2})\s*$", re.M)


def ler_caderno():
    """Uma lista de entradas do caderno: dict(bloco, titulo, id, subs, correcao,
    data, texto)."""
    entradas = []
    dir_erros = BASE / "erros"
    if not dir_erros.is_dir():
        return entradas
    for md in sorted(dir_erros.glob("*.md")):
        txt = md.read_text(encoding="utf-8")
        marcas = list(RX_ENTRADA.finditer(txt))
        for i, m in enumerate(marcas):
            fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(txt)
            corpo = txt[m.end():fim]
            m_sub = RX_SUB.search(corpo)
            subs = []
            if m_sub:
                subs = [s.strip() for s in m_sub.group(1).split(",") if s.strip()]
            m_e = RX_E.search(corpo)
            datas = RX_DATA.findall(corpo)
            entradas.append({
                "bloco": md.stem,
                "titulo": m.group(1).strip(),
                "id": m.group(2),
                "subs": subs,
                "correcao": m_e.group(1).strip() if m_e else "",
                "data": datas[-1] if datas else "",
                "texto": m.group(1) + " " + corpo,
            })
    return entradas


# --- historico do quiz ------------------------------------------------------
def ler_historico(quem):
    h = hist_de(quem)
    if not h.exists():
        return []
    return json.loads(h.read_text(encoding="utf-8")).get("respostas", [])


def agregar(entradas, respostas, questoes):
    """Junta caderno + historico + banco por microtopico.

    O erro e contado a partir do CADERNO (e la que ele esta etiquetado); o
    historico entra para dizer a causa e a taxa de acerto. A entrada auto-anotada
    carrega o id da questao, que e a chave da juncao entre os dois."""
    por_id = {q["id"]: q for q in questoes}
    causa_de = {r["id"]: r.get("causa") for r in respostas
                if not r["ok"] and r.get("causa")}

    dados = defaultdict(lambda: {"erros": [], "causas": Counter(),
                                 "tentativas": 0, "acertos": 0, "banco": 0})
    for e in entradas:
        for s in e["subs"]:
            if s not in subtags.VOCAB:
                continue      # o ./valida.py ja avisa; aqui so nao conta
            d = dados[s]
            d["erros"].append(e)
            causa = causa_de.get(e["id"])
            if causa:
                d["causas"][causa] += 1

    # taxa de acerto: so vale para questao com 'sub' EXPLICITO (etiqueta a mao),
    # nunca por palavra-chave — chute de keyword aqui viraria estatistica falsa
    for r in respostas:
        q = por_id.get(r["id"])
        if not q:
            continue          # questao saiu do banco depois de respondida
        for s in q.get("sub") or []:
            if s in subtags.VOCAB:
                dados[s]["tentativas"] += 1
                dados[s]["acertos"] += bool(r["ok"])

    for s in dados:
        dados[s]["banco"] = sum(1 for q in questoes if subtags.cobre(s, q))
    return dados


def ordenar(dados):
    """Mais erros primeiro; empate desempata pelo banco mais magro (buraco de
    conteudo antes de assunto ja bem coberto)."""
    return sorted(dados.items(), key=lambda kv: (-len(kv[1]["erros"]), kv[1]["banco"]))


ORIENTACAO = {
    # A mesma trava anti-vicio do ./quiz.py --stats: o que gerar depende da CAUSA.
    "conceitual": ("faltou conteudo", "conceitual/direta — definicao ou comparacao "
                                      "de par, comando terminando em ':'"),
    "armadilha": ("sabia e caiu na leitura", "aplicacao com a quase-certa reforcada, "
                                             "repetindo o padrao de distrator que pegou"),
}
PADRAO = ("causa nao marcada", "metade direta (definicao), metade aplicada")


def orientacao(causas):
    if not causas:
        return PADRAO
    conc, arm = causas.get("conceitual", 0), causas.get("armadilha", 0)
    return ORIENTACAO["conceitual" if conc >= arm else "armadilha"]


def relatorio(dados, top, quem):
    ordem = ordenar(dados)
    if top:
        ordem = ordem[:top]
    print()
    if not ordem:
        print(cor("  nenhum erro etiquetado ainda.", "ama"))
        print(cor("  etiquete as entradas do caderno com '- **sub:** <microtopico>'", "dim"))
        print(cor("  (veja o que falta: ./fraquezas.py --sem-sub)\n", "dim"))
        return
    print(cor(f"  Microtopicos por dificuldade{'' if quem == 'lucas' else f' — {quem}'}", "b"))
    print(cor(f"  {'microtopico':<22}{'erros':>6}{'banco':>7}  {'acerto':>7}  ultimo   causa", "dim"))
    for s, d in ordem:
        n = len(d["erros"])
        c = "verm" if n >= 3 else "ama" if n == 2 else "dim"
        tx = f"{d['acertos']}/{d['tentativas']}" if d["tentativas"] else "—"
        ult = max((e["data"] for e in d["erros"] if e["data"]), default="—")
        causa = "·".join(f"{k[:4]} {v}" for k, v in d["causas"].most_common()) or "—"
        alerta = cor(" ←", "verm") if n >= 2 and d["banco"] <= 5 else ""
        print(f"  {cor(f'{s:<22}', c)}{n:>6}{d['banco']:>7}  {tx:>7}  {ult:<7}  "
              f"{cor(causa, 'dim')}{alerta}")
    print(cor("\n  erros = entradas do caderno etiquetadas com essa subtag", "dim"))
    print(cor("  banco = questoes que ja cobrem o assunto (etiqueta 'sub' ou palavra-chave)", "dim"))
    print(cor("  ← = errou 2+ vezes e o banco tem 5 questoes ou menos: gere ai primeiro", "dim"))
    print(cor("\n  treine um: ./quiz.py <microtopico>   |   gere questao: ./fraquezas.py --prompt\n", "dim"))


def sem_sub(entradas):
    """Entradas do caderno ainda sem '- **sub:**' — elas ficam FORA do ranking.
    Sugere etiqueta por palavra-chave, mas quem decide e voce (a sugestao le o
    texto da entrada, nao o assunto real da questao)."""
    orfas = [e for e in entradas if not e["subs"]]
    print()
    if not orfas:
        print(cor("  todas as entradas do caderno estao etiquetadas.\n", "verde"))
        return
    print(cor(f"  {len(orfas)} entrada(s) do caderno sem subtag — fora do ranking:", "ama"))
    for e in orfas:
        sug = [s for s in subtags.sugerir(e["texto"])
               if not subtags.VOCAB[s]["blocos"] or e["bloco"] in subtags.VOCAB[s]["blocos"]]
        cauda = cor("  sugestao: " + ", ".join(sug), "ciano") if sug else cor("  (sem sugestao)", "dim")
        print(f"    [{e['bloco']}] {e['titulo'][:52]:<52}{cauda}")
    print(cor("\n  etiquete acrescentando '- **sub:** <microtopico>' logo abaixo do titulo.", "dim"))
    print(cor("  microtopico novo? crie no subtags.py antes (o ./valida.py cobra).\n", "dim"))


def _curto(txt, limite):
    """Corta no espaco anterior ao limite, para nao partir palavra no briefing."""
    if len(txt) <= limite:
        return txt
    return txt[:limite].rsplit(" ", 1)[0] + "…"


def briefing(dados, top, questoes):
    """Briefing pronto para colar num pedido de geracao de questoes."""
    ordem = ordenar(dados)[:top]
    if not ordem:
        print("\n  nada etiquetado ainda — rode ./fraquezas.py --sem-sub primeiro.\n")
        return
    por_sub = defaultdict(list)
    for q in questoes:
        for s in q.get("sub") or []:
            por_sub[s].append(q)

    print("\nGere questoes novas para banco.json mirando o que eu mais erro.")
    print("Siga CONTRIBUINDO-QUESTOES.md (ancoragem em fonte primaria, distrator")
    print("ancorado em erro real, sem vazamento de forma) e o estilo do CLAUDE.md.\n")
    for i, (s, d) in enumerate(ordem, 1):
        v = subtags.VOCAB[s]
        cap = APOSTILA.get(v["apostila"] or "", (None, None, ""))
        motivo, formato = orientacao(d["causas"])
        quantas = 4 if len(d["erros"]) >= 2 else 3
        # o bloco da questao nova e o bloco onde o erro aconteceu (a 'tag' e o
        # que manda no roteiro/simulado; a subtag so acompanha)
        bloco = Counter(e["bloco"] for e in d["erros"]).most_common(1)[0][0]
        print(f"{i}. {s} — {v['desc']}")
        print(f"   {len(d['erros'])} erro(s) no caderno; {d['banco']} questao(oes) ja cobrem o assunto"
              + (f"; {len(por_sub[s])} com a etiqueta 'sub'" if por_sub[s] else ""))
        if cap[0]:
            print(f"   leitura de referencia: Apostila Cap. {cap[0]} — {cap[2]}")
        print(f"   causa dominante: {motivo} -> {formato}")
        for e in d["erros"][:3]:
            print(f"   errei ({e['data'] or 's/data'}): {_curto(e['correcao'], 220)}")
        print(f"   gerar {quantas}, cada uma com \"tag\": \"{bloco}\" e \"sub\": [\"{s}\"]\n")
    print("Nao repita enunciado ja existente no banco. Ao terminar, rode ./valida.py.\n")


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("--top", type=int, default=None)
    p.add_argument("--sem-sub", dest="sem_sub", action="store_true")
    p.add_argument("--prompt", action="store_true")
    p.add_argument("--quem", default="lucas")
    p.add_argument("-h", "--help", action="store_true")
    a = p.parse_args()
    if a.help:
        print(__doc__)
        return

    quem = a.quem.strip().lower()
    entradas = ler_caderno()

    if a.sem_sub:
        sem_sub(entradas)
        return

    questoes = carregar_originais() + carregar_provas()
    dados = agregar(entradas, ler_historico(quem), questoes)

    if a.prompt:
        briefing(dados, a.top or 3, questoes)
        return

    relatorio(dados, a.top, quem)
    orfas = [e for e in entradas if not e["subs"]]
    if orfas:
        print(cor(f"  ({len(orfas)} entrada(s) do caderno ainda sem subtag e fora do ranking "
                  f"— veja ./fraquezas.py --sem-sub)\n", "ama"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
