#!/usr/bin/env python3
"""Painel de acompanhamento — Concurso Dataprev 2026.

Uso:
    python3 status.py              painel completo (lucas)
    python3 status.py hoje         so o conteudo de hoje
    python3 status.py --quem geys          painel completo dela
    python3 status.py --quem geys hoje     conteudo de hoje, dela
    python3 status.py --vs geys            compara lucas x geys lado a lado
"""

import csv
import sys
from datetime import date, datetime
from pathlib import Path

import roteiro  # leitura compartilhada do plano do dia

BASE = Path(__file__).parent
PROVA = date(2026, 10, 11)
CSV = BASE / "progresso.csv"


def csv_de(quem):
    """Caminho do progresso.csv de uma pessoa. 'lucas' usa o arquivo
    original; qualquer outro nome usa progresso-<quem>.csv, criado pelo
    ./quiz.py --quem <nome> na primeira vez que ela roda o quiz."""
    quem = (quem or "lucas").strip().lower()
    return CSV if quem == "lucas" else BASE / f"progresso-{quem}.csv"

# tags que nao contam como "bloco de conteudo" para fins de revisitacao
NAO_CONTEUDO = {"revisao", "simulado", "descanso", "prova"}

C = {
    "reset": "\033[0m", "bold": "\033[1m", "dim": "\033[2m",
    "verde": "\033[32m", "amarelo": "\033[33m", "vermelho": "\033[31m",
    "azul": "\033[34m", "ciano": "\033[36m",
}


def cor(txt, c):
    return f"{C[c]}{txt}{C['reset']}"


def barra(pct, largura=20):
    cheio = int(pct / 100 * largura)
    return "#" * cheio + "." * (largura - cheio)


def carregar(csv_path=CSV):
    with open(csv_path) as f:
        linhas = list(csv.DictReader(f))
    for l in linhas:
        l["data"] = datetime.strptime(l["data"], "%Y-%m-%d").date()
        l["questoes"] = int(l["questoes"])
        l["acertos"] = int(l["acertos"])
        l["feito"] = l["feito"] == "1"
    return linhas


def fraqueza_do_dia(minimo_erros=2):
    """O primeiro microtopico do ranking do ./fraquezas.py, se ja tiver
    'minimo_erros' erros no caderno. Devolve (subtag, erros, banco) ou None —
    com um erro so nao ha padrao ainda, e o painel nao inventa lembrete. Falha
    em silencio se o caderno/banco nao der para ler: e um extra do painel, nao
    pode derrubar o resto."""
    try:
        import fraquezas
        from quiz import carregar_originais, carregar_provas
        questoes = carregar_originais() + carregar_provas()
        dados = fraquezas.agregar(fraquezas.ler_caderno(),
                                  fraquezas.ler_historico("lucas"), questoes)
        for s, d in fraquezas.ordenar(dados):
            if len(d["erros"]) >= minimo_erros:
                return s, len(d["erros"]), d["banco"]
    except Exception:
        return None
    return None


def mostrar_hoje(linhas, csv_path=CSV, quem="lucas"):
    hoje = date.today()
    l = next((x for x in linhas if x["data"] == hoje), None)
    if l is None:
        print(cor("\n  Hoje nao esta no roteiro.\n", "dim"))
        return

    print()
    print(cor(f"  {l['data'].strftime('%d/%m')} ({l['dia']}) — semana {l['semana']}", "bold"))
    print(f"  {cor('Foco:', 'ciano')} {l['foco']}")
    print(f"  {cor('Tambem:', 'ciano')} {l['secundario']}")

    plano = roteiro.plano_de_hoje(csv_path)
    tipo = plano["tipo"]
    print()
    if tipo == "descanso":
        print(cor("  Hoje e descanso. Recarregue as energias.", "ciano"))
    elif tipo == "prova":
        print(cor("  Hoje e a PROVA. Boa sorte!", "ciano"))
    elif tipo == "revisao":
        print(cor("  Dia de revisao:", "bold"))
        print("    ./estudar.sh            apostila do dia + quiz --hoje")
        print("    ./estudar.sh --teoria   idem, mas abre teoria/main.pdf (livro-texto)")
        print("    ./quiz.py --hoje        so o quiz, refaz erradas (originais + provas)")
    elif tipo == "simulado":
        print(cor("  Dia de simulado:", "bold"))
        print("    ./estudar.sh --simulado apostila do dia + simulado cronometrado")
        print("    ./quiz.py --hoje        so o quiz, questoes reais de prova")
    else:  # conteudo
        print(cor("  Estudar hoje:", "bold"))
        print("    ./estudar.sh            apostila do dia + quiz --hoje")
        print("    ./estudar.sh --teoria   idem, mas abre teoria/main.pdf (livro-texto)")
        print("    ./quiz.py --hoje        so o quiz, questoes dos blocos do dia")
        for b in plano["blocos"]:
            atalhos = []
            if (BASE / "resumo" / f"{b}.md").exists():
                atalhos.append(f"--resumo {b}")
            if (BASE / "dicas" / f"{b}.md").exists():
                atalhos.append(f"--dica {b}")
            extra = cor("   ./quiz.py " + " / ".join(atalhos), "dim") if atalhos else ""
            print(f"    • {b}{extra}")

    # ponta solta do dia: o microtopico no topo do ranking, se ja errado 2+ vezes.
    # So aparece quando existe — lembrete que aparece sempre vira ruido. Fica
    # de fora de --quem: o caderno de erros (erros/*.md) e o do Lucas.
    quente = fraqueza_do_dia() if quem == "lucas" else None
    if quente:
        s, n, banco = quente
        print(cor(f"\n  Ponto fraco: {s} — {n} erros no caderno, "
                  f"{banco} questoes no banco", "bold"))
        # ljust + 2 espacos: subtag longa nao pode colar no texto da direita
        print(cor(f"    {f'./quiz.py {s}'.ljust(22)}  treina so esse microtopico", "dim"))
        print(cor(f"    {'./fraquezas.py'.ljust(22)}  ranking completo", "dim"))
    print()


def resumo(linhas, hoje=None):
    """Calcula as metricas do painel para uma pessoa: aderencia, sequencia,
    taxa de acerto geral e desempenho por bloco. Usado pelo painel individual
    e pela comparacao (--vs)."""
    hoje = hoje or date.today()

    passados = [l for l in linhas if l["data"] < hoje and l["tag"] not in {"descanso", "prova"}]
    feitos = [l for l in passados if l["feito"]]
    com_q = [l for l in linhas if l["questoes"] > 0]

    total_q = sum(l["questoes"] for l in com_q)
    total_a = sum(l["acertos"] for l in com_q)
    taxa = total_a / total_q * 100 if total_q else 0
    aderencia = len(feitos) / len(passados) * 100 if passados else 100

    seq = 0
    for l in reversed([l for l in linhas if l["data"] < hoje]):
        if l["feito"]:
            seq += 1
        else:
            break

    blocos = {}
    for l in com_q:
        t = l["tag"]
        if t in NAO_CONTEUDO:
            continue
        blocos.setdefault(t, [0, 0])
        blocos[t][0] += l["questoes"]
        blocos[t][1] += l["acertos"]

    return {
        "total_q": total_q, "taxa": taxa, "aderencia": aderencia,
        "feitos": len(feitos), "passados": len(passados),
        "seq": seq, "blocos": blocos,
    }


def painel(linhas, quem="lucas"):
    hoje = date.today()
    faltam = (PROVA - hoje).days
    r = resumo(linhas, hoje)

    print()
    print(cor("=" * 52, "azul"))
    print(cor("  DATAPREV 2026 — Desenvolvimento de Software", "bold"))
    if quem != "lucas":
        print(cor(f"  sessao de: {quem}", "ciano"))
    print(cor("=" * 52, "azul"))
    print()

    c = "verde" if faltam > 30 else "amarelo" if faltam > 7 else "vermelho"
    print(f"  Faltam {cor(str(faltam), c)} dias para a prova (11/10)")
    print()

    # aderencia
    aderencia = r["aderencia"]
    c = "verde" if aderencia >= 85 else "amarelo" if aderencia >= 65 else "vermelho"
    pct_aderencia = cor(f"{aderencia:.0f}%", c)
    print(f"  Aderencia ao roteiro  {barra(aderencia)} {pct_aderencia}"
          f"  ({r['feitos']}/{r['passados']} dias)")

    # sequencia
    print(f"  Sequencia atual       {cor(str(r['seq']), 'bold')} dias seguidos")
    print()

    # questoes
    print(f"  Questoes resolvidas   {cor(str(r['total_q']), 'bold')}")
    if r["total_q"]:
        taxa = r["taxa"]
        c = "verde" if taxa >= 75 else "amarelo" if taxa >= 60 else "vermelho"
        pct_taxa = cor(f"{taxa:.0f}%", c)
        print(f"  Taxa de acerto geral  {barra(taxa)} {pct_taxa}")
    print()

    # desempenho por bloco
    if r["blocos"]:
        print(cor("  Desempenho por bloco", "bold"))
        ordenado = sorted(r["blocos"].items(), key=lambda x: x[1][1] / x[1][0])
        for tag, (q, a) in ordenado:
            p = a / q * 100
            c = "verde" if p >= 75 else "amarelo" if p >= 60 else "vermelho"
            alerta = cor("  <-- atencao", "vermelho") if p < 60 else ""
            pct = cor(f"{p:>3.0f}%", c)
            print(f"    {tag:<16} {barra(p, 12)} {pct}  ({a}/{q}){alerta}")
        print()

    # revisitacao — a regra dos 15 dias
    ultimo = {}
    for l in linhas:
        if l["data"] < hoje and l["feito"] and l["tag"] not in NAO_CONTEUDO:
            ultimo[l["tag"]] = l["data"]

    frios = [(t, (hoje - d).days) for t, d in ultimo.items() if (hoje - d).days > 15]
    if frios:
        print(cor("  Esfriando (regra dos 15 dias)", "amarelo"))
        for t, dias in sorted(frios, key=lambda x: -x[1]):
            print(f"    {t:<16} sem revisar ha {cor(str(dias), 'vermelho')} dias")
        print()

    # proximo simulado
    prox = next((l for l in linhas if l["data"] >= hoje and l["tag"] == "simulado"), None)
    if prox:
        d = (prox["data"] - hoje).days
        quando = "HOJE" if d == 0 else "amanha" if d == 1 else f"em {d} dias"
        print(f"  Proximo simulado: {cor(prox['foco'], 'ciano')} ({quando})")
        print()

    print(cor("-" * 52, "dim"))
    mostrar_hoje(linhas, csv_de(quem), quem)


def comparar(nome_a, linhas_a, nome_b, linhas_b):
    """Painel lado a lado de duas pessoas: quem esta na frente em cada bloco
    e onde os dois estao fracos ao mesmo tempo (prioridade pra estudar juntos)."""
    hoje = date.today()
    faltam = (PROVA - hoje).days
    ra, rb = resumo(linhas_a, hoje), resumo(linhas_b, hoje)

    print()
    print(cor("=" * 52, "azul"))
    print(cor(f"  DATAPREV 2026 — {nome_a.capitalize()} vs {nome_b.capitalize()}", "bold"))
    print(cor("=" * 52, "azul"))
    print()
    c = "verde" if faltam > 30 else "amarelo" if faltam > 7 else "vermelho"
    print(f"  Faltam {cor(str(faltam), c)} dias para a prova (11/10)")
    print()

    def linha(rotulo, va, vb, fmt="{}"):
        print(f"  {rotulo:<22} {nome_a:<8} {fmt.format(va):<8} {nome_b:<8} {fmt.format(vb)}")

    linha("Questoes resolvidas", ra["total_q"], rb["total_q"])
    linha("Taxa de acerto geral", ra["taxa"], rb["taxa"], "{:.0f}%")
    linha("Aderencia ao roteiro", ra["aderencia"], rb["aderencia"], "{:.0f}%")
    linha("Sequencia atual", ra["seq"], rb["seq"], "{} dias")
    print()

    tags = sorted(set(ra["blocos"]) | set(rb["blocos"]))
    if tags:
        print(cor(f"  Desempenho por bloco ({nome_a} | {nome_b})", "bold"))
        fracos_comuns = []
        for tag in tags:
            qa, aa = ra["blocos"].get(tag, (0, 0))
            qb, ab = rb["blocos"].get(tag, (0, 0))
            pa = aa / qa * 100 if qa else None
            pb = ab / qb * 100 if qb else None
            txt_a = f"{pa:>3.0f}%" if pa is not None else "  - "
            txt_b = f"{pb:>3.0f}%" if pb is not None else "  - "
            marca = ""
            if pa is not None and pb is not None:
                if pa - pb >= 10:
                    marca = cor(f"  <-- {nome_a} na frente", "verde")
                elif pb - pa >= 10:
                    marca = cor(f"  <-- {nome_b} na frente", "verde")
                if pa < 60 and pb < 60:
                    fracos_comuns.append(tag)
            print(f"    {tag:<16} {txt_a}  |  {txt_b}{marca}")
        if fracos_comuns:
            print()
            print(cor("  Fracos nos dois — bom pra estudar junto:", "amarelo"))
            for t in fracos_comuns:
                print(f"    {t}")
        print()


def _resolver_args(args):
    """Le --quem <nome>, --vs <nome> e 'hoje' de sys.argv[1:]. Devolve
    (modo, quem, outro, ver_hoje) onde modo e 'painel' ou 'vs'."""
    args = list(args)
    outro = None
    pediu_vs = "--vs" in args
    if pediu_vs:
        i = args.index("--vs")
        outro = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    quem = "lucas"
    if "--quem" in args:
        i = args.index("--quem")
        quem = args[i + 1] if i + 1 < len(args) else "lucas"
        del args[i:i + 2]
    ver_hoje = "hoje" in args
    modo = "vs" if pediu_vs else "painel"
    return modo, quem, outro, ver_hoje


if __name__ == "__main__":
    modo, quem, outro, ver_hoje = _resolver_args(sys.argv[1:])

    if modo == "vs":
        if not outro:
            print(cor("\n  uso: ./status.py --vs <nome>\n", "vermelho"))
            sys.exit(1)
        arq_outro = csv_de(outro)
        if not arq_outro.exists():
            print(cor(f"\n  {arq_outro.name} nao existe ainda — peca pra {outro} rodar "
                       f"./quiz.py --quem {outro} --hoje pelo menos uma vez.\n", "amarelo"))
            sys.exit(1)
        comparar("lucas", carregar(CSV), outro, carregar(arq_outro))
    else:
        arq = csv_de(quem)
        if quem != "lucas" and not arq.exists():
            print(cor(f"\n  {arq.name} nao existe ainda — rode ./quiz.py --quem {quem} --hoje "
                       "pelo menos uma vez.\n", "amarelo"))
            sys.exit(1)
        dados = carregar(arq)
        if ver_hoje:
            mostrar_hoje(dados, arq, quem)
        else:
            painel(dados, quem)
