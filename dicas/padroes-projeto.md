# padroes-projeto — como a FGV cobra

## O que mais cai
- Identificar o padrão a partir de um CENÁRIO ("precisa de uma única
  instância...", "criar objeto sem acoplar à classe concreta...").
- Os campeões: Singleton, Factory Method/Abstract Factory, Strategy, Observer,
  Adapter, Facade, Decorator, Proxy, MVC.
- Distinguir padrão × anti-padrão e ligar padrões a princípios SOLID/GRASP.

## Como a banca arma a pegadinha
- Troca padrões da MESMA família com intenção parecida: Factory Method ×
  Abstract Factory, Strategy × State, Adapter × Facade × Proxy, Observer ×
  Mediator.
- Descreve a ESTRUTURA de um padrão mas pede a INTENÇÃO de outro.
- Usa absolutos ("Singleton sempre é a melhor solução", "Decorator só funciona
  com herança").

## Como se sair melhor
- Decore a INTENÇÃO (o "para quê"), não o diagrama: Singleton=uma instância;
  Factory=criar sem acoplar ao concreto; Strategy=trocar algoritmo em runtime;
  Observer=notificar dependentes; Adapter=compatibilizar interfaces;
  Facade=simplificar subsistema; Proxy=controlar acesso; Decorator=agregar
  comportamento dinâmico.
- Memorize os pares confundíveis lado a lado (veja `../resumo/padroes-projeto.md`).
- Grupo do padrão ajuda a eliminar: criacional (criar), estrutural (compor),
  comportamental (interagir).
