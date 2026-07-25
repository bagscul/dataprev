# Java moderno (17/21 LTS) — resumo (Perfil 3)

> **Contexto:** o edital 2026 traz Java como linguagem-base. As versões LTS em
> uso são a **17** (set/2021) e a **21** (set/2023) — o que entrou nelas é
> material recente de banca. Este resumo é recorte do bloco `java`: veja
> `./quiz.py --resumo java` para o resto (coleções, exceções, JVM, Spring, JPA).
> **Prioridade média-alta** dentro do bloco.

## Inferência de tipo: `var`

```java
var lista = new ArrayList<String>();   // inferido como ArrayList<String>
var total = 0;                          // int
```

- Inferência em **tempo de compilação**: o tipo é deduzido do inicializador e
  **fica fixo**. Java continua estaticamente tipado.
- Vale só para **variável local** (e parâmetro de lambda). Em atributo de
  instância, parâmetro de método ou retorno: **não compila**.
- Exige inicializador: `var x;` não compila.

**Pegadinha:** "var torna a variável de tipo dinâmico". Não torna — depois de
inferido, atribuir valor incompatível é erro de compilação.

## `record` (Java 16)

```java
record Ponto(int x, int y) { }
```

O compilador gera, a partir dos componentes do cabeçalho:

| Gerado | Observação |
|---|---|
| construtor canônico | pode ser sobrescrito (compacto) para validar |
| métodos de acesso | `p.x()`, `p.y()` — sem `get` |
| `equals` / `hashCode` | comparam componente a componente |
| `toString` | formato `Ponto[x=1, y=2]` |

- Campos são **finais**: o objeto é imutável.
- O record é implicitamente **final** e já estende `java.lang.Record` — logo
  **não pode estender outra classe**. Pode **implementar interfaces**.
- Não pode declarar campos de instância adicionais (só estáticos).

## `sealed` / `permits` (Java 17)

```java
sealed interface Forma permits Circulo, Retangulo { }
final class Circulo implements Forma { }
non-sealed class Retangulo implements Forma { }
```

- Fecha a hierarquia: só os tipos listados podem herdar/implementar.
- Cada subtipo permitido deve ser **`final`**, **`sealed`** ou **`non-sealed`**
  (este último reabre a herança de propósito).
- `permits` pode ser **omitido** se os subtipos estiverem no **mesmo arquivo**.
- Serve à **exaustividade**: com a hierarquia fechada, o compilador reconhece um
  `switch` sobre tipos como completo, sem `default`.

**Pegadinha:** `sealed` **não** é sinônimo de `final`. O `final` proíbe herança;
o `sealed` permite herança, mas só pelos tipos autorizados.

## `switch` como expressão (Java 14)

```java
var dia = switch (n) {
    case 1, 7 -> "fim de semana";
    default   -> "útil";
};
```

- A forma com seta executa **só o ramo correspondente**: acabou o `break` e
  acabou o *fall-through*.
- Como **expressão**, devolve valor (use `yield` em bloco com chaves).

## Blocos de texto (Java 15)

Delimitados por `"""`, servem a conteúdo de **várias linhas** (JSON, SQL, HTML)
sem concatenação nem `\n` manual.

## Threads virtuais (Java 21)

Threads leves gerenciadas pela **JVM**, multiplexadas sobre um pequeno conjunto
de threads do sistema operacional (as *carrier threads*).

| | Thread de plataforma | Thread virtual |
|---|---|---|
| Corresponde a | uma thread do SO | nenhuma, enquanto bloqueada |
| Custo de criação | alto (pool se justifica) | baixo (uma por tarefa) |
| Quantidade viável | milhares | milhões |
| Ganha em | — | carga dominada por **espera** (E/S) |

Ao bloquear em E/S, a thread virtual é **desmontada** do carregador, que fica
livre para outra tarefa. É daí que vem a vazão.

```java
Thread.ofVirtual().start(() -> atende(req));
var exec = Executors.newVirtualThreadPerTaskExecutor();
```

### As duas armadilhas

1. **Pinning:** bloquear dentro de um bloco `synchronized` **prende** a thread
   virtual ao carregador, que deixa de ser liberado. Troque por
   `ReentrantLock` nas seções que bloqueiam.
2. **Pool:** o modelo pressupõe **uma thread virtual por tarefa**. Manter um
   pool fixo devolve o gargalo que a migração queria eliminar.

**Pegadinha:** confundir concorrência com paralelismo. Threads virtuais
aumentam **quantas tarefas ficam em andamento**; o paralelismo real continua
limitado pelo número de núcleos. Em tarefa limitada por CPU, não há ganho.
