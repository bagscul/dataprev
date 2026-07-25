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

## 3.1 Interface × classe abstrata

| | Classe abstrata | Interface |
|---|---|---|
| Construtor | **tem** | **não tem** |
| Atributo de instância | tem (com estado) | só `public static final` (constante) |
| Herança múltipla | **não** (estende uma só) | **sim** (implementa várias) |
| Método concreto | sim, desde sempre | sim, a partir do Java 8 (`default`/`static`) |
| Palavra-chave | `extends` | `implements` |

Regra de bolso: **estende uma** classe, **implementa várias** interfaces.
Classe abstrata quando há estado/comportamento comuns; interface quando o que
importa é o contrato.

Pegadinha: desde o Java 8 a interface tem método `default` **com corpo** —
"interface não pode ter implementação" virou falso, e a FGV usa essa
desatualização como distrator. O que a interface continua **não** tendo é
**construtor** e **atributo de instância**.

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

### String: imutabilidade

`String` é **imutável** — toda "alteração" (`+`, `concat`, `replace`,
`toUpperCase`) devolve **objeto novo**. Em concatenação intensiva use
**`StringBuilder`** (mutável, não sincronizado) ou `StringBuffer` (mutável e
sincronizado, mais lento). Literais iguais compartilham o *string pool*
(`"a" == "a"` → true), mas `new String("a") == "a"` → **false**; conteúdo é
sempre `.equals()`.

Pegadinha: "String é mutável porque posso reatribuir a variável" — o que muda
é a **referência**, não o objeto. E a FGV inverte `StringBuilder` (rápido, não
sincronizado) × `StringBuffer` (thread-safe, mais lento).

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

### Anotações que a FGV cobra pelo nome

- **Spring (estereótipos):** `@Component` (bean genérico), `@Service` (regra
  de negócio), **`@Repository`** (acesso a dados + **tradução automática de
  exceções** de persistência), `@Controller`/`@RestController` (camada web),
  `@Autowired` (injeta a dependência).
- **JPA:** **`@Entity` + `@Id`** é o par **mínimo** para uma entidade
  persistente (com `@GeneratedValue` para geração da chave); `@Table`/`@Column`
  renomeiam; **`@ManyToOne`** = muitos daqui para **um** de lá (lado dono, com
  a FK), `@OneToMany` é o inverso (com `mappedBy`), mais `@OneToOne` e
  `@ManyToMany`.

Pegadinha: trocar o estereótipo pela camada errada (`@Service` no DAO) e
inverter a cardinalidade do `@ManyToOne`; ou inventar anotação plausível
(`@Persistent`, `@PrimaryKey`). O papel de cada **framework** do ecossistema
Spring está em `programacao.md`.

## O que já caiu

**Em prova real da FGV:** classes `sealed` (o erro estava na subclasse
`sealed` *sem* `permits`) — **MPU**; threads virtuais sobre a *carrier*, JPA
N+1 (`FetchType.LAZY` + `JOIN FETCH`), leitura de REST controller
(`@RestController`, `@GetMapping`, `@PathVariable`) com `getOrDefault`, Spring
Cloud Eureka (`lease-expiration`) e Hibernate Envers (Revision Listener) —
**TJ-RJ**. Liskov caiu na Dataprev 2024 e no MPU, mas como item de
**Engenharia de Software**.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): checked × unchecked; overload × override; interface × classe
abstrata; coleções (ArrayList/LinkedList/TreeMap); `==` × `equals`; `String`
imutável e `StringBuilder`; anotações de Spring e JPA; `record` e `var`;
*pinning*; ordem de catch e exceção engolida por `finally`; escopo de variável
em bloco.

Rode `../quiz.py java` e `../quiz.py java-moderno`.

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
