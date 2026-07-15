# Java — resumo (Perfil 3)

> **Edital (Perfil 3):** Java (versão 6+), JavaEE (6+), **JakartaEE**, **JPA**
> (2+), frameworks **JUnit, Hibernate, JSF, Primefaces, Spring/SpringCloud/
> SpringBoot**. É a linguagem-base do perfil.
> **Peso esperado: MÉDIO.** Na amostra de provas, Java concentrou-se no TJ-RJ
> (Analista de Sistemas); caiu pouco na Dataprev 2024. Mas está no edital —
> estude os pares que a FGV adora inverter.

## 1. Exceções: checked × unchecked

| | Checked (verificada) | Unchecked (não verificada) |
|---|---|---|
| Superclasse | `Exception` (não `RuntimeException`) | `RuntimeException` |
| Compilador | **exige** try-catch **ou** `throws` | não exige |
| Exemplos | `IOException`, `SQLException` | `NullPointerException`, `ArrayIndexOutOfBounds`, `IllegalArgument` |

Pegadinha nº 1 do bloco: trocar os exemplos. `NullPointerException` é
**unchecked** (estende RuntimeException); `IOException` é **checked**.

## 2. Polimorfismo: overload × override

| | Overload (sobrecarga) | Override (sobrescrita) |
|---|---|---|
| Onde | mesma classe | subclasse |
| Assinatura | **muda** (parâmetros diferentes) | **igual** à do pai |
| Resolução | compile-time (estática) | runtime (dinâmica) |
| Anotação | — | `@Override` |

Pegadinha: overload = mesmo nome, assinatura diferente; override = mesma
assinatura na subclasse. Sobrescrever **não** viola Liskov por si só.

## 3. OO e SOLID

- **Pilares:** abstração, encapsulamento, herança, polimorfismo.
- **SOLID:**
  - **S** – Single Responsibility (uma responsabilidade por classe).
  - **O** – Open/Closed (aberta a extensão, fechada a modificação).
  - **L** – **Liskov** (subtipo substitui o tipo base sem quebrar o programa).
  - **I** – Interface Segregation (interfaces pequenas e específicas).
  - **D** – Dependency Inversion (depender de abstração, não de implementação).

Pegadinha: confundir **ISP** (interface enxuta) com **SRP** (uma
responsabilidade). Liskov: a subclasse pode sobrescrever, desde que continue
substituível.

## 4. Coleções (Collections)

| Interface | Implementações | Característica |
|---|---|---|
| `List` | `ArrayList`, `LinkedList` | ordenada, permite duplicatas |
| `Set` | `HashSet`, `TreeSet`, `LinkedHashSet` | sem duplicatas |
| `Map` | `HashMap`, `TreeMap`, `LinkedHashMap` | chave-valor |

- **ArrayList** (array dinâmico, acesso O(1) por índice) × **LinkedList**
  (lista ligada, inserção/remoção O(1) no meio se já tem o nó).
- `HashMap` (sem ordem) × `LinkedHashMap` (ordem de inserção) × `TreeMap`
  (ordenado). `getOrDefault` retorna o default se a chave não existe.
- `==` compara **referência**; `.equals()` compara **conteúdo**.

## 5. JVM, JPA e JavaEE

- **JVM:** executa bytecode; **heap** (objetos), **garbage collection**
  (libera memória sem referência); ferramentas de monitoramento (jconsole,
  jps, jstack).
- **JPA** (especificação de persistência) × **Hibernate** (implementação
  ORM). `EAGER` × `LAZY` (carregamento antecipado × sob demanda). Problema
  **N+1** (uma consulta por relação): resolve com `LAZY` + `JOIN FETCH`.
- **JavaEE/JakartaEE:** EJB, JPA, JMS, JSF; **Jakarta** é a continuação do
  JavaEE sob a Eclipse Foundation (namespace `jakarta.*` em vez de `javax.*`).
- **JSF/Primefaces:** framework de UI server-side baseado em componentes.

## O que já caiu (nossas questões)

Checked × unchecked; overload × override; Liskov (SOLID); coleções
(ArrayList/LinkedList/HashMap); `==` × `equals`; sealed classes, virtual
threads, JPA N+1 (TJ-RJ). Rode `../quiz.py java`.

## Pegadinhas da FGV (resumo)

- Trocar exemplos de checked↔unchecked; overload↔override; ISP↔SRP.
- Absolutos ("sempre", "obrigatório throws para unchecked" — é o contrário).
- Ler código linha a linha e confiar na semântica da API.
- Ver `../dicas/java.md`.

## Alta probabilidade / pesquisa extra

- **Recursos modernos (Java 17/21 LTS):** `record`, `sealed`, `var`,
  switch expressions, pattern matching, **virtual threads** (Project Loom —
  leves, muitas por carrier thread; brilham em I/O-bound).
- **Streams e lambdas** (Java 8+): programação funcional em coleções.
- **Spring Boot + JPA** é a stack mais provável em cenário de código.
