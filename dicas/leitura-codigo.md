# Leitura ativa de código — como a FGV cobra

Subtag transversal: as questões continuam nos blocos `java`, `programacao` e
`frontend`. Rode com `./quiz.py leitura-codigo`.

Item de leitura de código é o mais **objetivo** da prova: não há interpretação,
há execução. Se você simular o trecho linha a linha, acerta. O erro quase nunca
é de conhecimento — é de pressa.

## O método (use sempre, sem exceção)

1. **Não leia o código de cima a baixo procurando "o que ele faz".** Pergunte
   primeiro o que a questão quer: o valor impresso? a exceção lançada? a ordem
   de execução?
2. **Anote o estado ao lado.** Cada variável em uma coluna, um valor por linha
   executada. Rastrear de cabeça é onde a armadilha vence.
3. **Marque os pontos de saída.** `return` dentro de `try` com `finally`,
   `break`, curto-circuito de `&&`/`||`, `continue`.
4. **Confira o índice e o limite.** Fatiamento, laço `for`, tamanho de coleção:
   é onde mora o erro de um a mais/um a menos.

## Onde a FGV planta a armadilha

| Armadilha | Onde aparece |
|---|---|
| `finally` que sobrescreve o `return` do `try` | Java |
| escopo de variável (`var` em laço JS × `let`) | JavaScript |
| `==` × `equals()` em String; pool de literais | Java |
| ordem de iteração: `HashMap` × `LinkedHashMap` × `TreeMap` | Java |
| sobrecarga × sobrescrita (qual método é chamado) | Java |
| índice final **exclusivo** no fatiamento | Python |
| especificidade de seletor (id × classe × elemento) | CSS |
| estado assíncrono após `setState` | React |
| `NULL` em `NOT IN`, `WHERE` × `HAVING` | SQL |

## Como se sair melhor

Reserve os itens de código para o **fim** da prova se estiver apertado no
tempo — eles são demorados, mas têm a maior taxa de acerto por esforço quando
há tempo de simular. Nunca responda "de olho": duas linhas parecidas com uma
diferença de um caractere é exatamente o desenho do item.
