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
  valor e resultados, menos prescritivo).
- **Abordagens:** **tradicional/preditiva** (escopo fixo, cascata),
  **ágil/adaptativa**, e **híbrida** (combina as duas conforme a necessidade).

Pegadinha: híbrido = **combinar** ágil + tradicional (não "só ágil" nem "só
cascata"); não confundir grupo de processos (5) com área de conhecimento (10).

## 2. Scrum, Kanban, Lean (ágil)

- **Scrum:** framework com Sprints time-boxed; papéis, eventos, artefatos (ver
  `eng-software.md`). O Guia Scrum é citado no edital.
- **Kanban:** fluxo contínuo, limita WIP, sem sprints.
- **Lean:** eliminar desperdício, maximizar valor.

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
ITIL v3).

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
domínio ou atribui objetivo ao domínio errado.

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

## O que já caiu (nossas questões)

Ágil híbrida (combinar); Scrum Master e eventos; Kanban (fluxo contínuo);
ITIL 4 (dimensões, SVS); COBIT (domínios); BPMN (símbolos); lead time × cycle
time. Rode `../quiz.py governanca`.

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
