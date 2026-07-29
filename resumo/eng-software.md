# Engenharia de Software — resumo (Perfil 3)

> **Edital (Perfil 3):** engenharia de requisitos (classificação, processo,
> técnicas de elicitação); testes (unitários, integração, ágeis, usabilidade,
> automatizados, TDD, ciclo de vida, RPA); metodologias ágeis (Scrum, Kanban,
> XP); padrões de desenvolvimento e reuso; codificação; Ponto de Função e
> Story Points; DevOps; design de software.
> **Peso esperado: MUITO ALTO.** Foi o maior bloco da Dataprev 2024 (9 q), à
> frente de Banco de Dados/BI e Programação (6 cada). É a maior fatia do
> "eixo duplo" da FGV em TI (a outra é Banco de Dados).

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

**Modelo V — cada fase tem o seu teste.** Variação do cascata que **espelha**
construção e verificação: o ramo descendente vai do requisito ao código, o
ascendente sobe testando, e cada nível confere o que foi decidido no nível
equivalente do outro lado.

| Fase (ramo descendente) | Nível de teste que a verifica |
|---|---|
| Requisitos do usuário | **Teste de aceitação** |
| Especificação do sistema | Teste de sistema |
| Projeto arquitetural (módulos e interfaces) | **Teste de integração** |
| Projeto detalhado (algoritmos) | Teste de unidade |
| Codificação | (vértice do V) |

A lógica é "quem definiu, confere": o que foi **acordado com o usuário** é
conferido na **aceitação**; o que foi decidido no **projeto arquitetural** — a
divisão em módulos e suas interfaces — é conferido na **integração**.
Pegadinha: requisito nunca casa com teste de unidade (unidade verifica o
**projeto detalhado**), nem codificação com aceitação. Na dúvida, use as
pontas: requisito ↔ aceitação em cima, código ↔ unidade embaixo.

**Verificação × validação** — par invertível, já caiu (ALERO 2026):

| | **Verificação** | **Validação** |
|---|---|---|
| A pergunta | "estamos construindo o produto **corretamente**?" | "estamos construindo o **produto certo**?" |
| Compara com | a **especificação** (documento da fase anterior) | a **necessidade real** do usuário |
| Quando | ao longo de todo o desenvolvimento | perto da entrega, com o usuário |
| Como | revisão, inspeção, *walkthrough*, análise estática, teste de unidade e de integração | teste de aceitação, alfa/beta, homologação, protótipo avaliado |
| Executa? | **não necessariamente** — revisar documento é verificar | na prática **sim** |

Âncora: verificação olha para o **papel** (a especificação); validação olha
para a **pessoa** (o usuário). Consequência que dá o gabarito: **um sistema
pode passar na verificação e falhar na validação** — implementa exatamente o
que foi especificado, só que foi especificada a coisa errada.

Pegadinha: definir **validação** como "conformidade com a especificação"
(é verificação) ou **verificação** como "atendimento às necessidades do
usuário" (é validação); dizer que verificação **exige execução** (não exige);
tratar as duas como sinônimas de "teste" (teste é técnica, usada pelas duas).

## 1.1 Maturidade de processo: CMMI e MPS.BR

Avaliam **quão maduro é o processo** da organização — não a qualidade de um
produto. **CMMI, representação por estágios** (a que a banca cobra):

| Nº | Nível | O que caracteriza |
|---|---|---|
| 1 | Inicial | imprevisível, reativo, dependente de heróis |
| 2 | Gerenciado | gerenciado **por projeto** (planejado, monitorado) |
| 3 | **Definido** | processo **padronizado na organização**, não projeto a projeto |
| 4 | Gerenciado Quantitativamente | processo **medido e controlado por estatística** |
| 5 | Em Otimização | melhoria contínua a partir da medição |

**As duas representações:** *por estágios* dá um número de **maturidade** à
organização inteira (a escala acima); *contínua* dá um nível de **capacidade**
a cada área de processo isolada, que podem evoluir em ritmos diferentes.

**MPS.BR** (modelo brasileiro, MR-MPS-SW): sete níveis identificados por
letras, **de G até A** — G (Parcialmente Gerenciado), F (Gerenciado), E
(Parcialmente Definido), D (Largamente Definido), C (Definido), B (Gerenciado
Quantitativamente), A (Em Otimização). Evolui-se **de G para A**: G é o ponto
de partida, A é o topo.

Pegadinhas: dizer que o **nível 3 é o Gerenciado** (é o **Definido**);
inverter o topo, pondo Gerenciado depois de Definido (acima do 3 vem
**Gerenciado Quantitativamente**); afirmar que o MPS.BR **começa no A** (é o
contrário). E a contagem: **cinco** níveis no CMMI, **sete** no MPS.BR.

## 2. Engenharia de requisitos

**Classificação (o par que mais cai):**

| Tipo | O que descreve | Exemplo |
|---|---|---|
| **Funcional** | O QUE o sistema faz (uma função, um comportamento) | "emitir saldo da conta" |
| **Não funcional** | COMO/QUÃO BEM (qualidade, restrição) | "saldo em tempo real", desempenho, segurança, usabilidade |

Regra: "em tempo real", "seguro", "rápido", "disponível" → **não funcional**.

**Os tipos de RNF** (a FGV pede o tipo, não só "é não funcional"):

| Tipo | Do que trata | Exemplo de enunciado |
|---|---|---|
| **De produto** | qualidade do software em si | desempenho, usabilidade, confiabilidade, portabilidade |
| **Organizacional** | política/processo da **casa** | "deve seguir o padrão de codificação do órgão", "entregar em Java" |
| **Externo** | o que vem de **fora** da organização | legislação (LGPD), interoperabilidade com outro órgão, norma do setor |

Usabilidade, desempenho e segurança são **de produto**; regra interna de
processo é **organizacional**; exigência legal é **externa**.

**Contar RF e RNF num enunciado longo** é item recorrente. Método: leia frase a
frase e marque **cada verbo de ação do sistema** ("emitir", "cadastrar",
"calcular", "permitir que o usuário…") como **RF**; marque cada "deve ser
rápido/seguro/disponível/exportável/compatível" como **RNF**. Uma frase pode
conter os dois. Cuidado com a frase que só descreve o contexto do negócio — ela
não é requisito nenhum e infla a contagem de quem lê no automático.

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
  - **Compromissos (Scrum Guide 2020):** cada artefato tem um **compromisso**
    associado, que lhe dá foco e permite medir progresso — três pares fixos:

    | Artefato | Compromisso | O que ele fixa |
    |---|---|---|
    | Product Backlog | **Meta do Produto** (Product Goal) | objetivo de longo prazo |
    | Sprint Backlog | **Meta da Sprint** (Sprint Goal) | objetivo único da Sprint |
    | Increment | **Definition of Done** | padrão de qualidade do "pronto" |

    A banca mantém os nomes certos e **embaralha as ligações**. Guie-se pelo
    horizonte: produto → Product Backlog; Sprint → Sprint Backlog; "pronto" →
    Incremento.
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
| **Fumaça (smoke)** | verificação rápida e superficial das funções principais |

**Testes de desempenho** — os três se confundem porque todos "sobrecarregam";
o que muda é **até onde** se vai:

- **Carga (load):** o volume de uso **esperado em produção**.
- **Estresse (stress):** vai **além** do previsto até achar o **ponto de
  ruptura** e ver como o sistema quebra (e se recupera).
- **Volume:** muita **massa de dados** armazenada, não muitos usuários.

Pegadinha: "ultrapassar o previsto até deixar de responder" = **estresse**; o
gatilho é a palavra *além/ultrapassa*. Carga é a quase-certa oferecida nesse
cenário.

**Cobertura de caixa-branca** — quanto do código os testes exercitam:

- **Comandos** (*statement*): cada linha executada ao menos uma vez.
- **Decisões** (ramos/*branch*): cada decisão avaliada **como verdadeira e
  como falsa**.
- **Caminhos:** cada combinação de caminhos — o mais forte, em geral inviável.

Força crescente: comandos < decisões < caminhos. **100% de decisões implica
100% de comandos; a recíproca é falsa.** O caso-teste da banca é o `if` **sem
else**: com `if (a > 10) { x = 1; }` e um único caso `a = 20`, comandos ficam
em **100%** e decisões em **50%**, porque a condição nunca foi avaliada como
falsa — ainda que não exista `else` escrito.

- **TDD (Test-Driven Development):** escreve o **teste antes** do código
  (red → green → refactor). Foco em design e cobertura.
- **BDD (Behavior-Driven Development):** evolução do TDD, especifica
  comportamento em linguagem acessível ao negócio (Gherkin: Dado-Quando-Então).
- **Caixa-preta** (sem ver o código, só entrada/saída) × **caixa-branca**
  (baseado na estrutura interna/código).
- **RPA (Robotic Process Automation):** automatiza tarefas repetitivas de
  interface (robôs de software), não é teste.

## 4.1 Manutenção de software

Classificação clássica (ISO/IEC 14764) do que se faz **depois de entregue**. O
critério é a **causa** da alteração, não o momento nem o tamanho:

| Tipo | Causa da alteração |
|---|---|
| **Corretiva** | **corrigir defeito** já detectado (erro relatado, falha em produção) |
| **Adaptativa** | acompanhar **mudança do ambiente**: SO, SGBD, plataforma, hardware, legislação |
| **Perfectiva** | **melhorar** o que já funciona: desempenho, manutenibilidade, requisito novo |
| **Preventiva** | corrigir **falha latente** antes que ela se manifeste |

Pegadinha: atualização obrigatória do SGBD, sem defeito relatado e sem
funcionalidade nova, é **adaptativa** — a causa é o **ambiente**. Não é
corretiva (não há defeito), nem perfectiva (não melhora nada), nem preventiva
(não antecipa falha latente). "Evolutiva" é rótulo de fora dessa classificação
que a banca oferece como se fosse um dos quatro tipos.

## 5. Mensuração: Ponto de Função × Story Points

| | Ponto de Função (APF) | Story Points |
|---|---|---|
| Natureza | **objetiva**, padronizada (IFPUG) | **relativa/subjetiva**, do time |
| Independe do time? | **sim** | não (calibrado por time) |
| Bom para | contrato de escopo fechado, comparação entre projetos | estimativa ágil interna |
| Baseado em | funções do sistema (EE, SE, CE, ALI, AIE) | esforço/complexidade percebidos |

Pegadinha: Ponto de Função é o **objetivo e comparável**; Story Points é o
**relativo do time**. A FGV troca os dois.

**Decodificando EE / SE / CE / ALI / AIE** — a banca dá telas e pede a
classificação. Os cinco tipos de função se dividem em dois grupos:

| Sigla | Nome | Como reconhecer na tela |
|---|---|---|
| **EE** | Entrada Externa | a tela **recebe dado e grava** (inclui, altera, exclui) |
| **SE** | Saída Externa | a tela **mostra dado processado/calculado** (relatório com totalização, gráfico) |
| **CE** | Consulta Externa | a tela **só consulta e exibe**, sem cálculo nem dado derivado |
| **ALI** | Arquivo Lógico Interno | grupo lógico de dados **mantido dentro** do sistema |
| **AIE** | Arquivo de Interface Externa | grupo lógico **só lido**, mantido por **outro** sistema |

As três primeiras são **funções de transação**; as duas últimas, **funções de
dados**. O corte que decide a questão: **SE × CE** — se há **cálculo, soma ou
dado derivado**, é **SE**; se é leitura pura, é **CE**. E **ALI × AIE**: quem
**mantém** o dado? Se é o próprio sistema, ALI; se é outro, AIE.

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

## 8. Vizinhos do bloco (aparecem no edital, raros na amostra)

- **BPMN** (Business Process Model and Notation): notação de **processo de
  negócio**, não de software. **Raias/*swim lanes*** dividem quem faz o quê, e
  a passagem de uma raia para outra é um ***handoff***. O losango é
  ***gateway***: **exclusivo** (XOR — segue **um** caminho) × **paralelo**
  (AND — segue **todos**) × inclusivo (OR — um ou mais). Não confundir com o
  losango da UML, que é **nó de decisão** ([uml](uml.md)).
- **CBOK** (*Common Body of Knowledge*, da ABPMP): o corpo de conhecimento de
  **BPM** — gerenciamento de processos como disciplina (modelagem, análise,
  desenho, medição, transformação, governança).
- **SNAP** (*Software Non-functional Assessment Process*): mede o tamanho do
  que a **APF não conta** — o **não funcional**. É **complementar** ao Ponto de
  Função, não substituto: PF mede a funcionalidade, SNAP mede o restante.
- **GitLab CI:** o pipeline é declarado no arquivo **`.gitlab-ci.yml`**, na
  raiz do repositório. Ele define ***stages*** (etapas em ordem) e ***jobs***
  (o que roda em cada etapa); jobs do mesmo *stage* rodam em **paralelo**, e um
  *stage* só começa quando o anterior termina. Variáveis podem vir do arquivo
  ou da configuração do projeto — as **protegidas/mascaradas** servem a
  segredo, e é aí que a banca cutuca.

## O que já caiu

**Em prova real da FGV: 39 questões — e é o bloco específico mais bem
distribuído do corpus**, o único que aparece forte em *todas* as provas (13 na
ALERO, 9 na Dataprev, 10 no MPU, 7 no TJ-RJ). Outros blocos têm total maior por
causa de uma prova de perfil diferente; este não depende de nenhuma. É o bloco
mais confiável para investir tempo. Requisito funcional × não
funcional no cenário do saldo em tempo real, com **brainstorming** como
elicitação válida; **Scrum Master no Daily**; **Sprint Planning** pela
capacidade do time; metodologia ágil para mudança frequente (Scrum, com
Kanban/XP/Lean/Cascata como distratores); **CD** no DevOps; **Ponto de Função ×
Story Points**; **design alto × baixo nível** (a banca inverte os dois em
alternativas consecutivas); testes I/II/III/IV + **TDD**; **ágil híbrido**;
**Liskov** em leitura de código — **Dataprev 2024**. Contagem de RF/RNF,
**BPMN** (Data Object × Data Association e leitura de diagrama), **CBOK 4.0**
(*handoffs*), **APF** sobre telas, **SNAP** (medição não funcional), testes
automatizados, Liskov pela definição formal e **UML 2.5.1** — **MPU**. Mudança
tardia de escopo, **DDD** com especialistas de domínio, APF, contagem de RF/RNF
e o **MoReq-Jus** (Resolução CNJ nº 522/2023) — **TJ-RJ**. **CMMI e MPS.BR** no
mesmo enunciado, **Ponto de Função** como métrica independente de linguagem,
**modelo cascata** (validação só na fase final), **RUP** (quatro fases, risco
na Elaboração), **prototipação** para requisito volátil, **verificação ×
validação** e negociação de requisitos conflitantes — **ALERO 2026**.
Versionamento (SVN × Git, GitLab CI) vem tagueado aqui, mas o conteúdo está em
[programacao](programacao.md).

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): Sprint Review × Retrospective; os três compromissos do Scrum (Meta do
Produto, Meta da Sprint, Definition of Done); modelo V (requisitos ↔ aceitação,
arquitetural ↔ integração); tipos de manutenção (adaptativa na troca de SGBD);
cobertura de comandos × decisões; teste de estresse × carga; cascata ×
incremental como par explícito.

Rode `../quiz.py eng-software`.

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
