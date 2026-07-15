#!/usr/bin/env python3
"""Quiz de terminal — banco de questoes estilo FGV para o Dataprev 2026.

Uso:
    ./quiz.py                    10 questoes aleatorias do banco original
    ./quiz.py java               so do bloco java
    ./quiz.py java redes -n 15   15 questoes desses dois blocos
    ./quiz.py --hoje             questoes do bloco previsto no roteiro para hoje
    ./quiz.py --erradas          refaz o que voce errou (originais + provas juntos)
    ./quiz.py --prova dataprev2024   questoes REAIS daquela prova (precisa gabarito)
    ./quiz.py --prova todas      questoes reais de todas as provas importadas
    ./quiz.py --dica java        dica de banca (FGV) do bloco; sem bloco, lista
    ./quiz.py --tags             inventario de blocos (os dois bancos juntos)
    ./quiz.py --stats            desempenho acumulado por bloco
    ./quiz.py --quem geys        roda como outra pessoa (progresso separado)
    ./quiz.py --sem-anotar       nao grava as erradas no caderno de erros

Duas fontes de questao (ambas escalaveis — o quiz le quantas houver):
  banco.json         questoes ORIGINAIS, estilo FGV (o padrao)
  banco-provas.json  questoes REAIS das provas em provas/, via ./importar_provas.py
                     (so entram no sorteio depois do gabarito oficial; veja ./gabarito.py)

Ao errar, o quiz explica por que cada alternativa errada esta errada e grava
AUTOMATICAMENTE a entrada em erros/<bloco>.md (deduplicando por questao).
"""

import argparse
import csv
import json
import random
import sys
import textwrap
from datetime import date, datetime
from pathlib import Path

BASE = Path(__file__).parent
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


def tag_de_hoje(quem):
    """Le o progresso e devolve a tag do dia atual, se houver."""
    arq = csv_de(quem)
    if not arq.exists():
        return None
    hoje = date.today().isoformat()
    with open(arq, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            if l["data"] == hoje:
                t = l["tag"]
                return t if t not in {"revisao", "simulado", "descanso", "prova"} else None
    return None


def registrar_no_csv(qtd, acertos, quem):
    """Soma o resultado da sessao ao dia de hoje no progresso da pessoa."""
    arq = csv_de(quem)
    if not arq.exists():
        print(cor(f"  {arq.name} nao encontrado; nada registrado.", "dim"))
        return
    hoje = date.today().isoformat()
    with open(arq, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        campos = rows and list(rows[0].keys())
    achou = False
    for r in rows:
        if r["data"] == hoje:
            r["questoes"] = str(int(r["questoes"]) + qtd)
            r["acertos"] = str(int(r["acertos"]) + acertos)
            r["feito"] = "1"
            achou = True
    if not achou:
        print(cor("  hoje nao esta no roteiro; nada registrado.", "dim"))
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

    entrada = (
        f"\n## {_titulo_erro(q)} {marcador}\n"
        f"- **Errei:** marquei {letras[marcou]}, a correta era {letras[correta]}\n"
        f"- **E:** {correcao}\n"
        f"- {fonte} | {date.today():%d/%m}\n"
    )
    with open(arq, "a", encoding="utf-8") as f:
        f.write(entrada)
    print(cor(f"  anotado em erros/{q['tag']}.md", "dim"))


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
    arq = dicas / f"{bloco}.md"
    if not arq.exists():
        print(cor(f"\n  sem dica para '{bloco}'. Use ./quiz.py --dica para listar.\n", "verm"))
        return
    print()
    for linha in arq.read_text(encoding="utf-8").splitlines():
        if linha.startswith("# "):
            print(cor("  " + linha[2:], "b"))
        elif linha.startswith("## "):
            print(cor("  " + linha[3:], "ciano"))
        else:
            print(wrap(linha) if linha.strip() else "")
    print()


def rodar(questoes, anotar=True):
    total = len(questoes)
    acertos = 0
    erradas = []
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

        if not certo and anotar:
            anotar_erro(q, escolhida, correta_pos)
        print()

    return acertos, erradas


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("tags", nargs="*")
    p.add_argument("-n", type=int, default=10)
    p.add_argument("--hoje", action="store_true")
    p.add_argument("--erradas", action="store_true")
    p.add_argument("--prova", default=None)
    p.add_argument("--quem", default="lucas")
    p.add_argument("--sem-anotar", dest="anotar", action="store_false")
    p.add_argument("--tags", dest="listar", action="store_true")
    p.add_argument("--stats", action="store_true")
    p.add_argument("--dica", nargs="?", const="__listar__", default=None)
    p.add_argument("-h", "--help", action="store_true")
    a = p.parse_args()

    if a.help:
        print(__doc__)
        return

    if a.dica is not None:
        mostrar_dica(a.dica)
        return

    quem = a.quem.strip().lower()
    if quem != "lucas":
        print(cor(f"\n  sessao de: {quem}", "ciano"))
        garantir_csv(quem)

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
    elif a.erradas:
        # refazer erradas busca nos DOIS bancos (originais + todas as provas)
        banco = carregar_originais() + carregar_provas()
    else:
        banco = carregar_originais()

    hist = carregar_hist(quem)

    if a.listar:
        # inventario combinado dos dois bancos, para ver tudo que da pra estudar
        from collections import Counter
        tudo = carregar_originais() + carregar_provas()
        c = Counter(q["tag"] for q in tudo)
        print()
        for t, n in sorted(c.items()):
            tem_dica = "" if (BASE / "dicas" / f"{t}.md").exists() else cor("  (sem dica)", "dim")
            print(f"  {t:<16} {n} questoes{tem_dica}")
        print(f"\n  total: {len(tudo)}  |  dica de banca: ./quiz.py --dica <bloco>\n")
        return

    if a.stats:
        from collections import defaultdict
        d = defaultdict(lambda: [0, 0])
        for r in hist["respostas"]:
            d[r["tag"]][0] += 1
            d[r["tag"]][1] += r["ok"]
        print()
        if not d:
            print(cor("  nenhuma sessao registrada ainda.\n", "dim"))
            return
        print(cor("  Desempenho acumulado no quiz", "b"))
        for t, (tot, ok) in sorted(d.items(), key=lambda x: x[1][1] / x[1][0]):
            pct = ok / tot * 100
            c = "verde" if pct >= 75 else "ama" if pct >= 60 else "verm"
            print(f"    {t:<16} {cor(f'{pct:>3.0f}%', c)}  ({ok}/{tot})")
        print()
        return

    # selecao de questoes
    if a.erradas:
        ids_erradas = {r["id"] for r in hist["respostas"] if not r["ok"]}
        pool = [q for q in banco if q["id"] in ids_erradas]
        if not pool:
            print(cor("\n  nenhuma questao errada registrada. Otimo sinal.\n", "verde"))
            return
    elif a.hoje:
        t = tag_de_hoje(quem)
        if t is None:
            print(cor("\n  hoje nao tem bloco de conteudo no roteiro (revisao/simulado?).", "dim"))
            print(cor("  rodando 10 aleatorias de tudo.\n", "dim"))
            pool = banco[:]
        else:
            pool = [q for q in banco if q["tag"] == t]
            print(cor(f"\n  bloco de hoje no roteiro: {t}", "ciano"))
    elif a.tags:
        pool = [q for q in banco if q["tag"] in a.tags]
        if not pool:
            print(cor(f"\n  nenhuma questao com tags {a.tags}. Use --tags para listar.\n", "verm"))
            return
        # lembrete de banca: mostra a dica do bloco quando ha exatamente um
        if len(a.tags) == 1 and (BASE / "dicas" / f"{a.tags[0]}.md").exists():
            print(cor(f"\n  dica de banca deste bloco: ./quiz.py --dica {a.tags[0]}", "dim"))
    else:
        pool = banco[:]

    random.shuffle(pool)
    sel = pool[: a.n]

    res = rodar(sel, anotar=a.anotar)
    if res is None:
        return
    acertos, erradas = res
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
        hist["respostas"].append(
            {"id": q["id"], "tag": q["tag"], "ok": q["id"] not in ids_err, "quando": agora}
        )
    salvar_hist(hist, quem)

    print()
    r = input(f"  registrar em {csv_de(quem).name}? [S/n] ").strip().lower()
    if r in ("", "s", "sim"):
        registrar_no_csv(total, acertos, quem)
    print()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(cor("\n\n  interrompido.\n", "dim"))
        sys.exit(0)
