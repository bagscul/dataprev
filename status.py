#!/usr/bin/env python3
"""Painel de acompanhamento — Concurso Dataprev 2026.

Uso:
    python3 status.py              painel completo
    python3 status.py hoje         so o conteudo de hoje
"""

import csv
import sys
from datetime import date, datetime
from pathlib import Path

import roteiro  # leitura compartilhada do plano do dia

BASE = Path(__file__).parent
PROVA = date(2026, 10, 11)
CSV = BASE / "progresso.csv"

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


def carregar():
    with open(CSV) as f:
        linhas = list(csv.DictReader(f))
    for l in linhas:
        l["data"] = datetime.strptime(l["data"], "%Y-%m-%d").date()
        l["questoes"] = int(l["questoes"])
        l["acertos"] = int(l["acertos"])
        l["feito"] = l["feito"] == "1"
    return linhas


def mostrar_hoje(linhas):
    hoje = date.today()
    l = next((x for x in linhas if x["data"] == hoje), None)
    if l is None:
        print(cor("\n  Hoje nao esta no roteiro.\n", "dim"))
        return

    print()
    print(cor(f"  {l['data'].strftime('%d/%m')} ({l['dia']}) — semana {l['semana']}", "bold"))
    print(f"  {cor('Foco:', 'ciano')} {l['foco']}")
    print(f"  {cor('Tambem:', 'ciano')} {l['secundario']}")

    plano = roteiro.plano_de_hoje(CSV)
    tipo = plano["tipo"]
    print()
    if tipo == "descanso":
        print(cor("  Hoje e descanso. Recarregue as energias.", "ciano"))
    elif tipo == "prova":
        print(cor("  Hoje e a PROVA. Boa sorte!", "ciano"))
    elif tipo == "revisao":
        print(cor("  Dia de revisao:", "bold"))
        print("    ./quiz.py --hoje        refaz suas erradas (originais + provas)")
    elif tipo == "simulado":
        print(cor("  Dia de simulado:", "bold"))
        print("    ./quiz.py --hoje        questoes reais de prova, cronometre")
    else:  # conteudo
        print(cor("  Estudar hoje:", "bold"))
        print("    ./quiz.py --hoje        questoes dos blocos do dia")
        for b in plano["blocos"]:
            atalhos = []
            if (BASE / "resumo" / f"{b}.md").exists():
                atalhos.append(f"--resumo {b}")
            if (BASE / "dicas" / f"{b}.md").exists():
                atalhos.append(f"--dica {b}")
            extra = cor("   ./quiz.py " + " / ".join(atalhos), "dim") if atalhos else ""
            print(f"    • {b}{extra}")
    print()


def painel(linhas):
    hoje = date.today()
    faltam = (PROVA - hoje).days

    passados = [l for l in linhas if l["data"] < hoje and l["tag"] not in {"descanso", "prova"}]
    feitos = [l for l in passados if l["feito"]]
    com_q = [l for l in linhas if l["questoes"] > 0]

    total_q = sum(l["questoes"] for l in com_q)
    total_a = sum(l["acertos"] for l in com_q)
    taxa = total_a / total_q * 100 if total_q else 0

    aderencia = len(feitos) / len(passados) * 100 if passados else 100

    print()
    print(cor("=" * 52, "azul"))
    print(cor("  DATAPREV 2026 — Desenvolvimento de Software", "bold"))
    print(cor("=" * 52, "azul"))
    print()

    c = "verde" if faltam > 30 else "amarelo" if faltam > 7 else "vermelho"
    print(f"  Faltam {cor(str(faltam), c)} dias para a prova (11/10)")
    print()

    # aderencia
    c = "verde" if aderencia >= 85 else "amarelo" if aderencia >= 65 else "vermelho"
    print(f"  Aderencia ao roteiro  {barra(aderencia)} {cor(f'{aderencia:.0f}%', c)}"
          f"  ({len(feitos)}/{len(passados)} dias)")

    # sequencia
    seq = 0
    for l in reversed([l for l in linhas if l["data"] < hoje]):
        if l["feito"]:
            seq += 1
        else:
            break
    print(f"  Sequencia atual       {cor(str(seq), 'bold')} dias seguidos")
    print()

    # questoes
    print(f"  Questoes resolvidas   {cor(str(total_q), 'bold')}")
    if total_q:
        c = "verde" if taxa >= 75 else "amarelo" if taxa >= 60 else "vermelho"
        print(f"  Taxa de acerto geral  {barra(taxa)} {cor(f'{taxa:.0f}%', c)}")
    print()

    # desempenho por bloco
    blocos = {}
    for l in com_q:
        t = l["tag"]
        if t in NAO_CONTEUDO:
            continue
        blocos.setdefault(t, [0, 0])
        blocos[t][0] += l["questoes"]
        blocos[t][1] += l["acertos"]

    if blocos:
        print(cor("  Desempenho por bloco", "bold"))
        ordenado = sorted(blocos.items(), key=lambda x: x[1][1] / x[1][0])
        for tag, (q, a) in ordenado:
            p = a / q * 100
            c = "verde" if p >= 75 else "amarelo" if p >= 60 else "vermelho"
            alerta = cor("  <-- atencao", "vermelho") if p < 60 else ""
            print(f"    {tag:<16} {barra(p, 12)} {cor(f'{p:>3.0f}%', c)}  ({a}/{q}){alerta}")
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
    mostrar_hoje(linhas)


if __name__ == "__main__":
    dados = carregar()
    if len(sys.argv) > 1 and sys.argv[1] == "hoje":
        mostrar_hoje(dados)
    else:
        painel(dados)
