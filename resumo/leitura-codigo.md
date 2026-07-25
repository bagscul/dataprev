# Leitura ativa de código — resumo (Perfil 3)

> **Contexto:** recorte transversal dos blocos `java`, `programacao` e
> `frontend`. Não é um conteúdo novo: é a **técnica** de resolver o item que
> mostra um trecho e pergunta a saída. **Prioridade alta** — é o tipo de questão
> com maior taxa de acerto por esforço, desde que você não responda de olho.

## O método

1. **Leia a pergunta antes do código.** O que se pede: o valor impresso? a
   exceção? a ordem de execução? o número de iterações? Isso decide o que
   rastrear.
2. **Simule com uma tabela de estado ao lado.** Uma coluna por variável, uma
   linha por passo. Rastrear de cabeça é onde a armadilha vence.
3. **Marque os pontos de saída e de desvio:** `return` dentro de `try` com
   `finally`, `break`, `continue`, curto-circuito de `&&` / `||`.
4. **Confira índices e limites** — laço `for`, fatiamento, tamanho de coleção.
5. **Só então olhe as alternativas.** Elas costumam ser variações de um
   caractere: ler primeiro contamina a simulação.

## Catálogo de armadilhas por linguagem

### Java

| Armadilha | O que acontece |
|---|---|
| `finally` com `return` | o `return` do `finally` **sobrescreve** o do `try` |
| `==` × `equals()` em String | `==` compara referência; literais iguais compartilham o *pool*, mas `new String(...)` não |
| sobrecarga × sobrescrita | sobrecarga resolve em **compilação** (tipo declarado); sobrescrita, em **execução** (tipo real) |
| `HashMap` × `LinkedHashMap` × `TreeMap` | sem ordem / ordem de inserção / ordem natural das chaves |
| checked × unchecked | o que estende `RuntimeException` não exige `throws` nem `catch` |
| escopo de variável | variável declarada dentro do bloco não existe fora dele |

### JavaScript

- `var` tem escopo de **função** e é içada (*hoisting*): num laço, todas as
  closures enxergam o **mesmo** valor final. Com `let` (escopo de bloco), cada
  iteração tem sua própria variável — é o item clássico.
- `==` faz coerção de tipo; `===` não.

### Python

- Fatiamento `lista[a:b]` inclui `a` e **exclui** `b`.
- Índice negativo conta do fim; `-1` é o último.
- `max(dic)` compara **chaves**; `max(dic, key=dic.get)` compara valores.

### CSS

- **Especificidade:** `id` (100) > `classe`/atributo/pseudoclasse (10) >
  elemento (1). A ordem de declaração só desempata **especificidades iguais**.
- Box model: `padding` é o espaço **interno**; `margin`, o externo.

### SQL

- `WHERE` filtra **linhas** (antes do agrupamento); `HAVING` filtra **grupos**
  (depois).
- `NOT IN` com um `NULL` na subconsulta devolve conjunto **vazio**;
  `NOT EXISTS`, não.
- `LEFT JOIN` preserva as linhas da tabela da esquerda sem correspondência.

## Gestão de tempo na prova

O item de código é demorado, mas **determinístico**: quem simula, acerta. Se o
tempo apertar, deixe-o para o fim — e nunca o responda por reconhecimento
visual, porque duas alternativas separadas por um caractere é exatamente o
desenho do item.
