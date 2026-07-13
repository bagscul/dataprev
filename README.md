# DATAPREV 2026 — Desenvolvimento de Software

Prova: **11/10/2026, 13h as 17h**. Portoes fecham 12h30.
Lotacao: Natal/RN. 20 vagas imediatas, 13 de ampla concorrencia.

## Rotina diaria

```bash
./status.py          # o que estudar hoje + como estou
./quiz.py --hoje     # questoes do bloco de hoje, direto no terminal
# ... plataforma de questoes FGV, anota erros em erros/*.md ...
./feito.sh 45 34     # questoes feitas FORA do quiz (plataforma, PDF)
./salvar.sh          # commit + push
```

## Quiz de terminal

```bash
./quiz.py                  # 10 aleatorias
./quiz.py java redes -n 15 # blocos especificos
./quiz.py --hoje           # bloco previsto no roteiro para hoje
./quiz.py --erradas        # refaz so o que voce errou (repeticao espacada)
./quiz.py --stats          # desempenho acumulado por bloco
```

70 questoes originais em estilo FGV, cobrindo os blocos na proporcao
da prova de 2024. O quiz oferece registrar o resultado no progresso.csv
sozinho, entao nao use ./feito.sh para as questoes do quiz.

IMPORTANTE: o quiz e complemento, nao substituto. Questoes REAIS da FGV
(Qconcursos, TEC, PDF oficial da prova Dataprev 2024) continuam sendo o
treino principal. Provas de banca sao protegidas por direito autoral,
por isso o banco local e original, inspirado no estilo.

## Como anotar um erro

Em `erros/<bloco>.md`, tres linhas. O "errei" e a parte que importa:

```markdown
## SOLID — principio da segregacao de interface
- **Errei:** confundi ISP com SRP
- **E:** ISP = interface pequena e especifica; SRP = classe com uma responsabilidade
- FGV 2024 Dataprev Q47 | 24/07
```

## Regras que o roteiro assume

- Questao **todo dia**, sem excecao. Resolver questao e o metodo, nao a revisao.
- Filtro de banca travado em **FGV**. Outra banca constroi reflexo errado.
- Nenhum topico mais de 2 dias seguidos; revisitar em ate 15 dias.
- Simulado **domingo, 13h**, cronometrado. Mesmo horario da prova.
- No simulado: **especificos primeiro** (valem 2,5x), gerais depois.

## Onde a prova se decide

| Bloco (Dataprev 2024) | Questoes | Pontos |
|---|---|---|
| Engenharia de Software | 10 | 25 |
| Programacao | 4 | 10 |
| Banco de Dados / BI | 4 | 10 |
| Seguranca | 3 | 7,5 |
| Redes (fora do edital!) | 3 | 7,5 |
| Arquitetura de Software | 2 | 5 |

Eng. de Software e Banco de Dados sao o eixo duplo da FGV em TI.
Redes caiu mesmo sem estar no conteudo do perfil 3.

## Pendencias

- [ ] Inscricao (ate 06/08, 16h)
- [ ] Boleto R$ 110,00 (ate 07/08)
- [ ] Confirmar com a FGV se Ciencia da Computacao vale como
      "graduacao em TI" sem pos de 360h — concursodataprev26@fgv.br
