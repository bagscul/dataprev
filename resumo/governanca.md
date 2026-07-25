# Gestão e Governança de TI — resumo (Perfil 3)

> **Edital (Perfil 3):** gerenciamento de projetos (conceitos, áreas,
> projetos/programas/portfólio; abordagens tradicional, híbrida e ágil —
> Scrum, Lean, Kanban; Guia Scrum); processos e grupos de processos; gestão
> de riscos; **ITIL v4**; **COBIT 2019**; gestão e modelagem de processos com
> **BPMN**.
> **Peso esperado: MÉDIO.**

## 1. Gerenciamento de projetos (PMBOK)

- **Projeto × programa × portfólio:** projeto = esforço temporário com
  resultado único; **programa** = grupo de projetos relacionados;
  **portfólio** = conjunto de programas/projetos alinhados à estratégia.
- **PMBOK 6:** 5 **grupos de processos** (Iniciação, Planejamento, Execução,
  Monitoramento e Controle, Encerramento) × 10 **áreas de conhecimento**
  (integração, escopo, cronograma, custo, qualidade, recursos, comunicação,
  riscos, aquisições, partes interessadas).
- **PMBOK 7:** mudou para **princípios e domínios de desempenho** (foco em
  valor e resultados, menos prescritivo). Os **12 princípios**: ser um
  **administrador diligente/zeloso** (*steward*); criar um **ambiente
  colaborativo**; envolver-se com as **partes interessadas**; **focar no
  valor**; reconhecer e responder às interações do sistema (**pensamento
  sistêmico**); demonstrar **liderança**; **adaptar** (*tailoring*) ao
  contexto; incorporar a **qualidade**; navegar na **complexidade**; otimizar
  as respostas aos **riscos**; adotar **adaptabilidade e resiliência**;
  **permitir a mudança** para alcançar o estado futuro previsto.
- **Tripla restrição** ("triângulo de ferro"): **escopo, tempo e custo** — os
  três se condicionam, e mexer em um força ajuste nos outros; a **qualidade**
  é o que sofre o impacto direto.
- **Abordagens:** **tradicional/preditiva** (escopo fixo, cascata),
  **ágil/adaptativa**, e **híbrida** (combina as duas conforme a necessidade).

Pegadinha: híbrido = **combinar** ágil + tradicional (não "só ágil" nem "só
cascata"); não confundir grupo de processos (5, PMBOK 6) com área de
conhecimento (10) nem com princípio (12, PMBOK 7 — que **não** é baseado em
processos). A FGV oferece um princípio plausível, mas não o do cenário:
mudança de escopo por feedback = **foco em valor**; sistema que evolui e se
integra ao ambiente = **pensamento sistêmico**; cuidado ético com o produto =
**administrador zeloso**.

## 2. Scrum, Kanban, Lean (ágil)

- **Scrum:** framework com Sprints time-boxed; papéis, eventos, artefatos (ver
  `eng-software.md`). O Guia Scrum é citado no edital.
- **Time-boxes cobrados pelo número** (Sprint de um mês): **Daily Scrum = 15
  min**, conduzida pelos **Developers**, todo dia, para inspecionar o
  progresso rumo à **Meta da Sprint**; Sprint Planning 8 h; Review 4 h;
  Retrospective 3 h. Os 15 min da Daily são **fixos**; os demais encolhem em
  Sprints menores.
- **Kanban:** fluxo contínuo, limita WIP, sem sprints.
- **Lead time × cycle time:**

| Métrica | O que mede |
|---|---|
| **Lead time** | da **solicitação** (entrada no sistema, ótica do cliente) até a entrega — **inclui a fila** |
| **Cycle time** | do **início do trabalho** até a entrega — é um **trecho** do lead time |
| **Throughput** | **quantidade** entregue por período (não é tempo) |

  Sempre **lead time ≥ cycle time**; a diferença é o tempo esperando na fila.
  Reduzir o WIP encurta a fila e, com ela, o lead time (Lei de Little).

- **Lean:** eliminar desperdício, maximizar valor.

Pegadinha: dar ao **lead time** a definição do **cycle time**. A âncora é a
palavra **solicitação** — se conta a partir do pedido do cliente, é lead time.
E "itens entregues por semana" é **throughput**, não lead time.

## 3. ITIL 4 (gerenciamento de serviços)

Foco em **cocriação de valor** por meio de serviços.

- **Sistema de Valor de Serviço (SVS):** como os componentes trabalham juntos
  para gerar valor. Inclui: **princípios orientadores, governança, cadeia de
  valor de serviço, práticas e melhoria contínua.**
- **7 princípios orientadores:** focar no valor; começar de onde se está;
  progredir iterativamente com feedback; colaborar e promover visibilidade;
  pensar e trabalhar de forma holística; manter simples e prático; otimizar e
  automatizar.
- **4 dimensões:** (1) organizações e pessoas; (2) informação e tecnologia;
  (3) parceiros e fornecedores; (4) fluxos de valor e processos.
- **Cadeia de valor de serviço (6 atividades):** Planejar, Melhorar, Engajar,
  Desenhar e transicionar, Obter/construir, Entregar e suportar.
- **34 práticas** em 3 grupos: **gerais** (ex: gestão de risco, gestão de
  projeto), **de serviço** (ex: **gerenciamento de incidentes**, gestão de
  mudança/*change enablement*, gerenciamento de problemas, central de
  serviços), **técnicas** (ex: desenvolvimento de software, gestão de
  implantação).

Pegadinha: incidente (restaurar serviço) × problema (causa-raiz) ×
requisição de serviço; ITIL 4 fala em **práticas** (não "processos" como o
ITIL v3). A banca também troca o **propósito** de práticas parecidas —
memorize a frase de cada uma, que é o que ela cobra:

| Prática | Propósito (em uma frase) |
|---|---|
| Infraestrutura e plataforma | **monitorar/prover** as soluções tecnológicas da organização |
| Gerenciamento de liberação | tornar serviços e funcionalidades **disponíveis para uso** (mover para produção) |
| Central de serviços | ser o **ponto único de contato** entre provedor e usuários |
| Gerenciamento de incidentes | **restaurar** a operação normal o mais rápido possível |
| Gerenciamento de problemas | reduzir incidentes achando **causa raiz** e erros conhecidos |
| Gestão de mudança (*change enablement*) | maximizar mudanças bem-sucedidas avaliando **risco** e autorizando |

## 4. COBIT 2019 (governança de TI)

Distingue **governança** (avaliar, dirigir, monitorar — responsabilidade do
conselho) de **gestão** (planejar, construir, executar, monitorar).

- **40 objetivos de governança e gestão** em **5 domínios:**
  - **EDM** – Evaluate, Direct and Monitor (governança).
  - **APO** – Align, Plan and Organize.
  - **BAI** – Build, Acquire and Implement.
  - **DSS** – Deliver, Service and Support.
  - **MEA** – Monitor, Evaluate and Assess.
- **Fatores de desenho (design factors)** e **componentes do sistema de
  governança.** Princípios: sistema de governança feito sob medida; holístico;
  dinâmico; distingue governança de gestão; etc.

Pegadinha: EDM é **governança**; APO/BAI/DSS/MEA são **gestão**. A FGV troca
domínio ou atribui objetivo ao domínio errado — no MPU, "especificar e
priorizar requisitos com base na experiência do usuário" era **BAI**, não APO
nem DSS. Lembre também que o COBIT serve para **definir os componentes** que
constroem e sustentam um sistema de governança (foi o gabarito no TJ-RJ) — não
uma "estratégia de TI" nem um "inventário de ativos".

## 5. BPMN (modelagem de processos)

Notação para **processos de negócio**. Elementos-chave:

- **Eventos** (círculos): início (borda fina), intermediário (borda dupla),
  fim (borda grossa).
- **Atividades** (retângulos arredondados): tarefas e subprocessos.
- **Gateways** (losangos): decisões/desvios (exclusivo XOR, paralelo AND,
  inclusivo OR).
- **Raias (pools/lanes):** quem executa (papéis/organizações).
- **Fluxos:** de sequência (sólido) × de mensagem (tracejado).

Pegadinha: trocar o símbolo (evento início × fim pela espessura da borda;
gateway × atividade).

## O que já caiu

**Em prova real da FGV:** o domínio **BAI** do COBIT 2019 ("especificar e
priorizar requisitos com base na experiência do usuário") — **MPU**; a
aplicação do COBIT 2019 para **definir os componentes** de um sistema de
governança e o **propósito** da prática ITIL de infraestrutura e plataforma —
**TJ-RJ**; princípios do **PMBOK 7** aplicados a cenário (*adaptação e
resiliência*, *pensamento sistêmico*) — **TJ-RJ**.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): ágil híbrida (combinar); eventos do Scrum e o time-box de **15 min**
da Daily; Kanban (fluxo contínuo, limite de WIP); **lead time** × cycle time;
tripla restrição; ITIL 4 (4 dimensões, SVS, 6 atividades da cadeia de valor, 7
princípios, incidente × problema); os 5 domínios do COBIT; símbolos do BPMN;
os 5 grupos de processos do PMBOK 6; projeto × programa × portfólio.

Rode `../quiz.py governanca`.

## Pegadinhas da FGV (resumo)

- Inverter governança↔gestão (COBIT), incidente↔problema (ITIL), grupo de
  processos↔área de conhecimento (PMBOK).
- Dizer que híbrido é "só ágil".
- Trocar quantidades (5 domínios COBIT, 4 dimensões ITIL, 5 grupos PMBOK).
- Ver `../dicas/governanca.md`.

## Alta probabilidade / pesquisa extra

- **ITIL 4** ainda é o vigente; fique atento ao vocabulário novo (práticas,
  SVS, cocriação de valor).
- **COBIT 2019** usa "objetivos de governança e gestão" (não "processos" do
  COBIT 5).
- **Gestão de riscos (ISO 31000):** identificar, analisar, avaliar, tratar,
  monitorar.
