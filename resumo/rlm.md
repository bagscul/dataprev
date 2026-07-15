# Raciocínio Lógico Matemático — resumo

> **Edital (Módulo I, 5 questões):** estruturas lógicas; lógica de argumentação
> (analogias, inferências, deduções, conclusões); lógica sentencial
> (proposições, tabelas-verdade, equivalências, diagramas); lógica de primeira
> ordem; **raciocínio lógico envolvendo problemas aritméticos, geométricos e
> matriciais.**

## ⚠️ A regra de ouro: RLM da FGV é MATEMÁTICA

O edital diz explicitamente "problemas aritméticos, geométricos e matriciais".
Na Dataprev 2024, quase tudo foi **conta**, não lógica formal. Estudar só
tabela-verdade e parar por aí é o erro clássico. Priorize:

| Assunto | Peso prático | O que revisar |
|---|---|---|
| **Porcentagem / aumentos sucessivos** | altíssimo | fator multiplicativo (1,30 × 1,10), desconto, lucro |
| **Razão e proporção / regra de três** | alto | direta e inversa, divisão proporcional |
| **Análise combinatória** | alto | arranjo, combinação, permutação, princípio multiplicativo |
| **Médias e estatística** | alto | média simples, **ponderada**, mediana, moda |
| **PA / PG** | médio | termo geral, soma |
| **Geometria plana** | médio | área, perímetro, Pitágoras |
| **Matrizes** | médio | operações, determinante |
| **Lógica proposicional** | baixo (1 questão) | equivalências, tabela-verdade |

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

## Lógica proposicional (a fatia pequena)

- **Condicional** p→q. **Equivalente:** contrapositiva ¬q→¬p. "Se é fã então
  assiste" ≡ "se **não** assiste então **não** é fã".
- **Negação da condicional:** ¬(p→q) ≡ p ∧ ¬q.
- **De Morgan:** ¬(p∧q) ≡ ¬p∨¬q; ¬(p∨q) ≡ ¬p∧¬q.
- **Modus ponens** (p→q, p ⊢ q) e **modus tollens** (p→q, ¬q ⊢ ¬p).

## Como a FGV arma a pegadinha

Em RLM matemático, **cada alternativa errada é o resultado de um erro de conta
específico**: esqueceu de somar o peso, inverteu numerador/denominador, contou
o caso duplicado, somou as taxas em vez de multiplicar. Refaça a conta com
calma; o distrator "quase certo" costuma vir de um passo omitido.

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
