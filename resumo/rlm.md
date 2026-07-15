# Raciocínio Lógico Matemático — resumo

> **Edital (Módulo I, 5 questões):** estruturas lógicas; lógica de argumentação
> (analogias, inferências, deduções, conclusões); lógica sentencial
> (proposições, tabelas-verdade, equivalências, diagramas); lógica de primeira
> ordem; **raciocínio lógico envolvendo problemas aritméticos, geométricos e
> matriciais.**

## ⚠️ Duas frentes: matemática E lógica formal

Cuidado com uma leitura só. A **Dataprev 2024** foi quase toda **conta** — por
isso a fama de "RLM da FGV é matemática". Mas o **edital 2026** lista a lógica
formal com peso próprio: estruturas lógicas, lógica de argumentação, lógica
sentencial e **lógica de primeira ordem** (itens 1–4), e só no item 5 os
"problemas aritméticos, geométricos e matriciais". São só **5 questões**, então
não dá para prever o mix — **não pule a lógica formal apostando no padrão de
2024.** Cubra as duas frentes.

| Assunto | Prioridade | O que revisar |
|---|---|---|
| **Porcentagem / aumentos sucessivos** | altíssima | fator multiplicativo (1,30 × 1,10), desconto, lucro |
| **Razão e proporção / regra de três** | alta | direta e inversa, divisão proporcional |
| **Análise combinatória** | alta | arranjo, combinação, permutação, princípio multiplicativo |
| **Médias e estatística** | alta | média simples, **ponderada**, mediana, moda |
| **Lógica: equivalências e argumentação** | **alta (edital 2026)** | condicional, contrapositiva, De Morgan, validade |
| **PA / PG** | média | termo geral, soma |
| **Geometria plana** | média | área, perímetro, Pitágoras |
| **Matrizes** | média | operações, determinante |
| **Diagramas lógicos / quantificadores** | média | todo/algum/nenhum, primeira ordem |

## Ferramentas mínimas

- **Aumentos sucessivos:** multiplique os fatores. +30% depois +10% →
  1,30 × 1,10 = 1,43 → aumento total **43%** (não 40%). Taxa média mensal:
  raiz, ≈ **19,6%** (entre 19% e 20%).
- **Divisão proporcional:** reparte na razão das partes (ex.: prejuízo
  proporcional ao capital investido).
- **Média ponderada:** Σ(nota × peso) / Σ(pesos). Colocar a menor nota no
  maior peso derruba a média — cuidado com "necessariamente".
- **Combinação** C(n,p) = n! / [p!(n−p)!] (ordem não importa) × **arranjo**
  A(n,p) (ordem importa). Grafo completo de n vértices tem C(n,2) arestas.

## Lógica formal (não subestime — o edital 2026 puxa)

**Conectivos e tabela-verdade:**

| Conectivo | Símbolo | Falso quando |
|---|---|---|
| Conjunção "e" | p ∧ q | ao menos um é falso |
| Disjunção "ou" | p ∨ q | ambos falsos |
| Condicional "se…então" | p → q | **V → F** (só nesse caso) |
| Bicondicional "se e somente se" | p ↔ q | valores diferentes |
| Disjunção exclusiva "ou…ou" | p ⊻ q | valores iguais |

**Equivalências que a FGV cobra:**
- **Contrapositiva:** p → q ≡ ¬q → ¬p. "Se é fã então assiste" ≡ "se **não**
  assiste então **não** é fã". (A recíproca q→p **não** é equivalente.)
- **Condicional como disjunção:** p → q ≡ ¬p ∨ q.
- **Negação da condicional:** ¬(p → q) ≡ p ∧ ¬q.
- **De Morgan:** ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q.

**Argumentação (validade):** um argumento é **válido** se, sempre que as
premissas forem verdadeiras, a conclusão também for.
- **Modus ponens:** p→q, p ⊢ q (válido).
- **Modus tollens:** p→q, ¬q ⊢ ¬p (válido).
- **Falácias:** afirmar o consequente (p→q, q ⊢ p) e negar o antecedente
  (p→q, ¬p ⊢ ¬q) são **inválidas** — a FGV usa como pegadinha.
- **Silogismo hipotético:** p→q, q→r ⊢ p→r.

**Quantificadores / primeira ordem e diagramas:**
- "Todo A é B", "Algum A é B", "Nenhum A é B".
- Negações: negar "todo A é B" → "**algum** A **não** é B"; negar "algum A é B"
  → "**nenhum** A é B". A FGV adora a negação errada do quantificador.
- **Diagramas lógicos** (círculos de Euler/Venn): resolvem "todo/algum/nenhum"
  desenhando os conjuntos e testando o que **necessariamente** decorre — não o
  que "pode ser".

Pegadinha recorrente: confundir **equivalência** com **implicação**, marcar a
**recíproca** como equivalente, ou negar quantificador trocando "todo" por
"nenhum" (o certo é "algum não").

## Como a FGV arma a pegadinha

- **Nas de matemática:** cada alternativa errada é o resultado de um **erro de
  conta específico** — esqueceu de somar o peso, inverteu numerador/denominador,
  contou o caso duplicado, somou as taxas em vez de multiplicar. Refaça com
  calma; o distrator "quase certo" vem de um passo omitido.
- **Nas de lógica:** troca **equivalência** por implicação, marca a
  **recíproca** como equivalente, nega o quantificador errado ("todo"→"nenhum"
  em vez de "algum não"), ou apresenta uma **falácia** (afirmar o consequente)
  como argumento válido.

## O que já caiu (nossas questões)

Divisão proporcional (prejuízo); média ponderada com pesos por bimestre;
sistema com soma e soma dos quadrados; equivalência da condicional
(contrapositiva); grafo/estradas (combinação); aumentos sucessivos e taxa
média. Rode `../quiz.py rlm`.

## Alta probabilidade / pesquisa extra

- **Probabilidade** básica (casos favoráveis / possíveis) pode aparecer.
- **Diagramas lógicos** (todo/algum/nenhum) para argumentação.
- Treine **velocidade**: são 5 questões valendo 1 ponto cada — não gaste
  tempo demais numa; os específicos valem 2,5×.
- Ver `../dicas/rlm.md`.
