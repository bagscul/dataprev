# Engenharia de Software — resumo (Perfil 3)

> **Edital (Perfil 3):** engenharia de requisitos (classificação, processo,
> técnicas de elicitação); testes (unitários, integração, ágeis, usabilidade,
> automatizados, TDD, ciclo de vida, RPA); metodologias ágeis (Scrum, Kanban,
> XP); padrões de desenvolvimento e reuso; codificação; Ponto de Função e
> Story Points; DevOps; design de software.
> **Peso esperado: MUITO ALTO.** Foi o maior bloco da Dataprev 2024 (~10 q).
> É metade do "eixo duplo" da FGV em TI (a outra é Banco de Dados).

## 1. Ciclo de vida e modelos de processo

- **Cascata (waterfall):** fases sequenciais estritas, sem sobreposição,
  requisitos congelados no início. Adequado quando os requisitos são
  **estáveis e bem compreendidos**. Rígido a mudanças.
- **Incremental:** entrega em incrementos que somam funcionalidade.
- **Iterativo:** refina o mesmo produto em ciclos.
- **Espiral (Boehm):** iterativo + **análise de risco** a cada volta.
- **Prototipação:** protótipo para validar requisitos (pode ser descartável).
- **Ágil:** iterativo-incremental com entregas curtas e adaptação a mudança.

Pegadinha clássica: o enunciado descreve "fases sequenciais, requisitos
congelados" → é **cascata**, não incremental nem ágil.

## 2. Engenharia de requisitos

**Classificação (o par que mais cai):**

| Tipo | O que descreve | Exemplo |
|---|---|---|
| **Funcional** | O QUE o sistema faz (uma função, um comportamento) | "emitir saldo da conta" |
| **Não funcional** | COMO/QUÃO BEM (qualidade, restrição) | "saldo em tempo real", desempenho, segurança, usabilidade |

Regra: "em tempo real", "seguro", "rápido", "disponível" → **não funcional**.

**Processo:** elicitação → análise → especificação → validação →
gerenciamento. **Elicitação** (levantamento) usa: entrevista, questionário,
**brainstorming**, workshop, observação, prototipação, análise de documentos.
A FGV afirma que "brainstorming é inadequado, use só entrevista formal" — é
**falso**; brainstorming é técnica legítima de elicitação.

## 3. Metodologias ágeis

- **Scrum** (framework, não metodologia): trabalho em **Sprints** de tamanho
  fixo (time-boxed). Papéis/responsabilidades: **Product Owner** (valor e
  Product Backlog), **Scrum Master** (remove impedimentos, serve ao time,
  não manda), **Developers**. Eventos: Sprint, Sprint Planning, Daily Scrum,
  Sprint Review, Sprint Retrospective. Artefatos: Product Backlog, Sprint
  Backlog, Increment.
  - **Review = produto** (inspeciona o incremento com stakeholders).
  - **Retrospective = processo** (o que melhorar no jeito de trabalhar).
  - No Daily, com risco à Sprint, o Scrum Master **facilita a solução do
    time**, não redistribui tarefas sozinho nem assume a tarefa.
- **Kanban:** **fluxo contínuo**, sem sprints fechadas; limita WIP (trabalho
  em progresso); entrega conforme conclui.
- **XP (Extreme Programming):** práticas de engenharia — programação em par,
  TDD, integração contínua, refatoração, cliente presente.
- **Lean:** eliminar desperdício, otimizar o fluxo de valor.
- **Ágil híbrido:** combina práticas ágeis com métodos tradicionais.

Cuidado FGV: Kanban **não** tem sprint (é o distrator "Kanban organiza em
sprints"); Scrum **tem** time-box.

## 4. Testes

| Nível/Tipo | O que verifica |
|---|---|
| **Unitário** | menor unidade isolada (função/método) |
| **Integração** | interação entre módulos/componentes |
| **Sistema** | o sistema completo |
| **Aceitação** | atende ao cliente/requisito |
| **Usabilidade** | experiência/interface intuitiva |
| **Regressão** | mudança não quebrou o que já funcionava |

- **TDD (Test-Driven Development):** escreve o **teste antes** do código
  (red → green → refactor). Foco em design e cobertura.
- **BDD (Behavior-Driven Development):** evolução do TDD, especifica
  comportamento em linguagem acessível ao negócio (Gherkin: Dado-Quando-Então).
- **Caixa-preta** (sem ver o código, só entrada/saída) × **caixa-branca**
  (baseado na estrutura interna/código).
- **RPA (Robotic Process Automation):** automatiza tarefas repetitivas de
  interface (robôs de software), não é teste.

## 5. Mensuração: Ponto de Função × Story Points

| | Ponto de Função (APF) | Story Points |
|---|---|---|
| Natureza | **objetiva**, padronizada (IFPUG) | **relativa/subjetiva**, do time |
| Independe do time? | **sim** | não (calibrado por time) |
| Bom para | contrato de escopo fechado, comparação entre projetos | estimativa ágil interna |
| Baseado em | funções do sistema (EE, SE, CE, ALI, AIE) | esforço/complexidade percebidos |

Pegadinha: Ponto de Função é o **objetivo e comparável**; Story Points é o
**relativo do time**. A FGV troca os dois.

## 6. DevOps e entrega

- **CI (Integração Contínua):** integra e testa o código com frequência.
- **CD (Entrega/Implantação Contínua):** leva a nova versão à produção
  rapidamente, com mínima interrupção. "Fornecer rapidamente nova versão em
  produção" = **CD**.
- **DevOps** une desenvolvimento e operações; **DevSecOps** injeta segurança
  no pipeline.

## 7. Design de software

- **Design de alto nível** = estrutura geral, módulos e sua interação
  (próximo da arquitetura). **Design de baixo nível** = detalhe de funções,
  métodos, algoritmos.
- **Arquitetura** = decisões amplas e estruturais; **design** = decisões
  detalhadas. Não é "arquitetura só serve para projeto grande".
- **Padrões de projeto** (Singleton, Factory, Strategy, Observer…) e **UML**
  têm resumo próprio: [padroes-projeto](padroes-projeto.md) e [uml](uml.md).

## O que já caiu (nossas questões)

Cascata × incremental; Sprint Review × Retrospective; requisito funcional ×
não funcional (cenário do saldo em tempo real); brainstorming como elicitação
válida; Scrum Master no Daily e no Sprint Planning (capacidade do time);
metodologia ágil para mudança frequente (XP/Scrum/Kanban); CD no DevOps;
Ponto de Função × Story Points; design alto × baixo nível; testes I/II/III/IV
+ TDD; ágil híbrido. Rode `../quiz.py eng-software`.

## Pegadinhas da FGV (resumo)

- Inverter pares: Review↔Retro, funcional↔não funcional, PF↔Story Points,
  cascata↔incremental, TDD↔BDD, alto↔baixo nível.
- Absolutos: "sempre", "exclusivamente", "apenas", "impossível" — quase
  sempre marcam o distrator.
- Distorcer papel do Scrum Master (ele **facilita/serve**, não comanda nem
  executa a tarefa do dev).
- Ver `../dicas/eng-software.md` para o detalhe.

## Alta probabilidade / pesquisa extra

- **Scrum Guide 2020**: usa "accountabilities" (não "papéis"); removeu a
  figura do "time de desenvolvimento" como subgrupo — hoje é um **Scrum Team**
  único com Developers. Sprint Goal, Product Goal, Definition of Done.
- **Clean Code / SonarQube** (no edital): análise **estática** de código
  (sem executar) para dívida técnica, code smells, cobertura.
- **MVP, design thinking, UX** aparecem no edital do Perfil 1 mas permeiam;
  MVP = menor versão que entrega valor e valida hipótese.
