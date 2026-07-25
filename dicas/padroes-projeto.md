# padroes-projeto — como a FGV cobra

## O que mais cai
- Identificar o padrão a partir de um CENÁRIO ("precisa de uma única
  instância...", "criar objeto sem acoplar à classe concreta...").
- Os campeões: Singleton, Factory Method/Abstract Factory, Strategy, Observer,
  Adapter, Facade, Decorator, Proxy, MVC.
- Distinguir padrão × anti-padrão e ligar padrões a princípios SOLID/GRASP.
- A CONTAGEM direta: 23 padrões GoF em três famílias — criacionais (5),
  estruturais (7), comportamentais (11). A banca pergunta o número e a
  família de um padrão específico.
- Anti-padrões nomeados: God Object, Spaghetti Code, Golden Hammer,
  Copy-Paste. E "qual prática viola SOLID".
- Padrões arquiteturais fora do GoF, mas que caem no mesmo item: MVC,
  MVVM/MVP, e o par ESB (SOA) × microsserviços.

## O gatilho de cada padrão (o que faz a questão)

O enunciado descreve o PROBLEMA; você casa com a intenção. Criacionais:

- "apenas uma instância no sistema todo" → Singleton
- "decidir em runtime qual objeto criar, sem acoplar ao concreto" →
  Factory Method
- "família de objetos relacionados / kit para Windows e Mac" →
  Abstract Factory
- "montar objeto complexo passo a passo, muitos parâmetros opcionais" →
  Builder
- "copiar um objeto existente em vez de criar do zero" → Prototype

Estruturais:

- "fazer duas interfaces incompatíveis conversarem / adaptar API legada" →
  Adapter
- "uma fachada única e simples para um subsistema complexo" → Facade
- "substituto que controla o acesso (lazy load, cache, segurança)" → Proxy
- "empilhar comportamentos em runtime, sem herança" → Decorator
- "tratar item e conjunto de forma uniforme / árvore parte-todo" → Composite
- "separar abstração da implementação para variarem independentes" → Bridge
- "muitos objetos semelhantes, economizar memória" → Flyweight

Comportamentais:

- "trocar a regra de cálculo sem if gigante" → Strategy
- "notificar dependentes quando o estado muda / eventos" → Observer
- "requisição como objeto, undo/redo, fila de operações" → Command
- "o objeto age diferente conforme sua situação interna" → State
- "esqueleto do algoritmo com passos deixados para subclasses" →
  Template Method
- "percorrer a coleção sem expor a estrutura" → Iterator
- "passar por uma cadeia de handlers até alguém tratar" →
  Chain of Responsibility
- "centralizar a comunicação N-para-N" → Mediator
- "salvar e restaurar o estado (snapshot)" → Memento
- "adicionar operações sem alterar as classes da estrutura" → Visitor
- "avaliar expressões/regras de uma mini-linguagem (gramática)" →
  Interpreter

## Como a banca arma a pegadinha
- Troca padrões da MESMA família com intenção parecida: Factory Method ×
  Abstract Factory, Strategy × State, Adapter × Facade × Proxy, Observer ×
  Mediator.
- Descreve a ESTRUTURA de um padrão mas pede a INTENÇÃO de outro.
- Usa absolutos ("Singleton sempre é a melhor solução", "Decorator só funciona
  com herança").
- Erra a CONTAGEM: diz que são 20 ou 25 padrões, ou põe um comportamental na
  família estrutural. Interpreter é o mais esquecido dos 11 — some da lista
  de quem conta de cabeça, e é aí que ela pergunta o número.
- Inverte o par reuso: diz para preferir HERANÇA à composição (é o
  contrário — "favor composition over inheritance").

## Como se sair melhor
- Decore a INTENÇÃO (o "para quê"), não o diagrama: Singleton=uma instância;
  Factory=criar sem acoplar ao concreto; Strategy=trocar algoritmo em runtime;
  Observer=notificar dependentes; Adapter=compatibilizar interfaces;
  Facade=simplificar subsistema; Proxy=controlar acesso; Decorator=agregar
  comportamento dinâmico.
- Memorize os pares confundíveis lado a lado (veja `../resumo/padroes-projeto.md`).
- Grupo do padrão ajuda a eliminar: criacional (criar), estrutural (compor),
  comportamental (interagir). Se o cenário fala em CRIAR objeto, os sete
  estruturais já saem.
- Os quatro pares que decidem a questão:
  - Factory Method (uma criação, por herança) × Abstract Factory (famílias,
    por composição);
  - Strategy (troca o ALGORITMO) × State (muda conforme o ESTADO interno);
  - Proxy (controla ACESSO) × Decorator (ACRESCENTA função);
  - Adapter (compatibiliza o que já existe) × Facade (simplifica o
    subsistema).
- Ligue ao SOLID: Strategy e Template Method concretizam o Open/Closed;
  Dependency Inversion aparece em Factory/Abstract Factory; Singleton é o
  que mais tensiona o Single Responsibility.
- Ancore no framework que você já usa: o Spring aplica Singleton (beans),
  Factory, Proxy (AOP), Template Method (JdbcTemplate) e Observer (eventos).
