# Padrões de Projeto (Design Patterns) — resumo (Perfil 3)

> **Edital (Perfil 3):** "padrões de projeto", "design de software", "padrões
> de desenvolvimento e reuso", "análise e projeto orientados a objetos".
> **Alta probabilidade.** A FGV dá um CENÁRIO ("preciso garantir uma única
> instância...", "preciso criar objetos sem acoplar à classe concreta...") e
> pergunta QUAL padrão. Decore o gatilho de cada um, não só o nome.

## Como a FGV cobra

O enunciado descreve um **problema de design** e você identifica o padrão que
o resolve. A chave é reconhecer a **intenção** (o "para quê") de cada padrão.
O catálogo GoF (Gang of Four) reúne **23 padrões**, divididos em 3 grupos:
**criacionais** (5), **estruturais** (7) e **comportamentais** (11) — o número
e a classificação em três grupos são cobrados diretamente.

## 1. Criacionais (como criar objetos)

| Padrão | Intenção (gatilho no enunciado) |
|---|---|
| **Singleton** | garantir **uma única instância** e ponto global de acesso ("apenas uma conexão/configuração no sistema todo") |
| **Factory Method** | delegar a criação a subclasses; criar objeto **sem acoplar à classe concreta** ("decidir em runtime qual objeto criar") |
| **Abstract Factory** | criar **famílias** de objetos relacionados sem especificar classes concretas ("kit de UI para Windows e Mac") |
| **Builder** | construir objeto complexo **passo a passo**, separando construção da representação ("montar um objeto com muitos parâmetros opcionais") |
| **Prototype** | criar novos objetos **clonando** um protótipo ("copiar um objeto existente em vez de criar do zero") |

Pegadinhas: **Factory Method** (uma criação, via herança) × **Abstract
Factory** (famílias de produtos, via composição). Singleton = **uma** instância.

## 2. Estruturais (como compor objetos/classes)

| Padrão | Intenção (gatilho) |
|---|---|
| **Adapter** | fazer interfaces **incompatíveis** trabalharem juntas ("adaptar uma API legada à nova") |
| **Facade** | interface **simplificada** para um subsistema complexo ("uma fachada única para vários serviços") |
| **Proxy** | um **substituto** que controla acesso ao objeto real (lazy load, cache, segurança) |
| **Decorator** | adicionar responsabilidades a um objeto **dinamicamente**, sem herança ("empilhar comportamentos em runtime") |
| **Composite** | tratar objetos individuais e composições **de forma uniforme** (árvore parte-todo) |
| **Bridge** | separar **abstração** da **implementação** para variarem independentes |
| **Flyweight** | compartilhar objetos para economizar memória (muitos objetos semelhantes) |

Pegadinhas: **Adapter** (compatibiliza o que já existe) × **Facade**
(simplifica um subsistema) × **Decorator** (adiciona comportamento). **Proxy**
× **Decorator**: proxy **controla acesso**; decorator **acrescenta função**.

## 3. Comportamentais (como objetos interagem)

| Padrão | Intenção (gatilho) |
|---|---|
| **Strategy** | família de algoritmos **intercambiáveis**, escolhidos em runtime ("trocar a regra de cálculo sem if gigante") |
| **Observer** | notificar automaticamente **dependentes** quando o estado muda ("publish-subscribe", eventos) |
| **Command** | encapsular uma **requisição como objeto** (undo/redo, fila de operações) |
| **State** | mudar o comportamento conforme o **estado interno** ("o objeto age diferente conforme sua situação") |
| **Template Method** | definir o **esqueleto** de um algoritmo, deixando passos para subclasses |
| **Iterator** | percorrer uma coleção **sem expor sua estrutura** |
| **Chain of Responsibility** | passar a requisição por uma **cadeia** de handlers até alguém tratar |
| **Mediator** | centralizar a comunicação entre objetos (reduz acoplamento N-para-N) |
| **Memento** | capturar/restaurar o estado de um objeto (snapshot) |
| **Visitor** | adicionar operações a uma estrutura sem alterar as classes |
| **Interpreter** | definir uma **gramática** para uma linguagem e um interpretador que avalia suas sentenças ("interpretar expressões/regras escritas numa mini-linguagem") |

Pegadinhas: **Strategy** (troca o algoritmo) × **State** (troca conforme o
estado) — parecidos na estrutura, diferentes na intenção. **Observer** = o
padrão de eventos/notificação. **Interpreter** é o 11º comportamental e o mais
esquecido — some da lista de quem conta de cabeça, e é justamente aí que a FGV
pergunta o número.

## GRASP (princípios de atribuição de responsabilidade)

O edital cita GRASP no Perfil 2, mas o conceito permeia. São princípios (não
"caixas de código") para decidir **qual classe recebe qual responsabilidade**:
Information Expert, Creator, Controller, Low Coupling, High Cohesion,
Polymorphism, Pure Fabrication, Indirection, Protected Variations.

## Padrões arquiteturais (não são GoF, mas caem)

- **MVC** (Model-View-Controller): separa dados, apresentação e controle.
- **MVVM / MVP**: variações com binding/presenter.
- **DAO / Repository**: isola o acesso a dados.
- **DTO**: objeto para transportar dados entre camadas.
- **Front Controller, Singleton de configuração** aparecem em Java EE.
- Ver também `arquitetura.md` (hexagonal, microsserviços, API gateway, SOA).

## Reuso e anti-padrões

- **Reuso:** herança (é-um) × **composição** (tem-um) — prefira composição
  ("favor composition over inheritance"). Bibliotecas, frameworks, componentes.
- **Anti-padrões:** God Object (classe que faz tudo), Spaghetti Code, Golden
  Hammer (usar sempre a mesma solução), Copy-Paste. A FGV usa "qual é o
  anti-padrão" ou "qual prática viola SOLID".

### SOLID — os cinco, para consultar aqui

Aparecem **com todas as letras no edital do Perfil 2** (item 16) e são a
linguagem em que a banca cobra "qual prática viola" e "que princípio o padrão X
concretiza". O tratamento completo, com as armadilhas de Java, está em
[java](java.md#3-oo-e-solid); aqui fica o essencial para ligar padrão a
princípio sem sair do assunto:

- **S** – *Single Responsibility*: uma responsabilidade (um motivo para mudar)
  por classe.
- **O** – *Open/Closed*: aberta à **extensão**, fechada à **modificação**.
- **L** – *Liskov*: o subtipo substitui o tipo base sem quebrar o programa.
- **I** – *Interface Segregation*: interfaces pequenas e específicas, em vez
  de uma interface gorda.
- **D** – *Dependency Inversion*: depender de **abstração**, não de
  implementação concreta.

O par que a FGV inverte é **ISP** (interface enxuta) × **SRP** (uma
responsabilidade): os dois falam em "pequeno e específico", mas um trata de
*interface* e o outro de *classe*.

## Como se sair melhor

1. **Leia a intenção, não a implementação.** O enunciado descreve o problema;
   case com o "para quê" da tabela.
2. **Memorize os pares confundíveis:** Factory Method × Abstract Factory;
   Adapter × Facade × Decorator; Strategy × State; Proxy × Decorator.
3. **Ligue ao SOLID:** Strategy e Template Method concretizam o Open/Closed;
   Dependency Inversion aparece em Factory/Abstract Factory.

## Alta probabilidade / pesquisa extra

- Os mais cobrados pela FGV: **Singleton, Factory Method/Abstract Factory,
  Strategy, Observer, Adapter, Facade, Decorator, MVC.**
- Relação com frameworks: Spring usa Singleton (beans), Factory, Proxy (AOP),
  Template Method (JdbcTemplate), Observer (eventos).
