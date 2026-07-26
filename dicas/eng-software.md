# eng-software — como a FGV cobra

## O que mais cai
- Engenharia de requisitos: funcional x não funcional. É o
  tema mais recorrente do bloco (caiu em Dataprev, MPU e
  TJ-RJ). Cobra CONTAR quantos RF e quantos RNF há num
  enunciado longo, e classificar o tipo de RNF (usabilidade,
  desempenho, produto, organizacional, externo).
- Métricas de tamanho: Análise de Pontos de Função (APF) e
  Story Points. Também recorrente. Pede classificar função a
  partir de telas: Entrada Externa (EE), Saída Externa (SE),
  Consulta Externa (CE), Arquivo Lógico Interno (ALI),
  Arquivo de Interface Externa (AIE). E PF x Story Points.
- Ágil/Scrum: papel do Scrum Master (remove impedimento, NÃO
  assume tarefa), Sprint Planning (priorizar pela capacidade
  da equipe), mudança tardia de escopo (avaliar com o PO e
  adaptar o backlog), ágil híbrida, Kanban x Scrum x XP x
  Lean x Cascata.
- Testes: unitário x integração x TDD (teste antes) x
  usabilidade; testes automatizados servem à integração
  contínua e reduzem retrabalho de regressão. Também:
  cobertura de comandos x decisões (caixa-branca) e os
  testes de desempenho — carga x estresse x volume.
- Maturidade de processo: CMMI por estágios (cinco níveis,
  o 3 é o Definido) e MPS.BR (sete letras, de G até A).
- Modelo V: parear fase de desenvolvimento com nível de
  teste. Tipos de manutenção: corretiva, adaptativa,
  perfectiva, preventiva.
- Scrum Guide 2020: os três COMPROMISSOS pareados com os
  três artefatos (Product Backlog/Meta do Produto, Sprint
  Backlog/Meta da Sprint, Incremento/Definition of Done).
- BPMN/CBOK: swim lanes/handoffs, gateways exclusivo x
  paralelo. UML: agregação composta. SNAP (medição não
  funcional). SVN x Git (binários). GitLab CI (variáveis,
  pipelines). No edital, mas raro na amostra.

## Como a banca arma a pegadinha
- Requisito "em tempo real"/desempenho é NÃO funcional; a FGV
  oferece a alternativa que o chama de funcional. RNF fala de
  COMO (qualidade, restrição); RF fala de O QUE o sistema faz.
- Inverte PF x Story Points: diz que Story Point é objetivo/
  padronizável entre times ou serve a contrato de escopo
  fechado — é o contrário (PF = objetivo e independente do
  time; Story Point = relativo, subjetivo, intra-time).
- Scrum Master: distrator faz ele "assumir a tarefa",
  "redistribuir sozinho" ou "encerrar o Sprint". O certo é
  facilitar a solução colaborativa e remover obstáculos.
- Troca CI (integra e testa a cada commit) por CD (entrega/
  implanta em produção). Absolutos: teste automatizado "nunca
  precisa ser alterado".
- Elicitação: chama brainstorming de "técnica inadequada" ou
  diz que requisito vem DEPOIS da implementação.
- CMMI: diz que o nível 3 é o "Gerenciado" (é o Definido),
  inverte o topo (acima do 3 vem Gerenciado QUANTITATIVAMENTE,
  depois Em Otimização) ou afirma que o MPS.BR começa no A —
  começa no G. Cuidado com "a escala tem quatro níveis".
- Modelo V: embaralha os pares — casa requisito com teste de
  UNIDADE (unidade verifica o projeto detalhado) ou
  codificação com aceitação.
- Manutenção: chama de corretiva a troca de versão do SGBD
  (não há defeito: é ADAPTATIVA, a causa é o ambiente), ou
  oferece "evolutiva", que está fora da classificação.
- Cobertura: diz que comandos e decisões são equivalentes, ou
  que num if sem else um caso verdadeiro já fecha os dois.
- Estresse x carga: oferece "carga" no cenário que fala em
  ULTRAPASSAR o previsto — carga fica DENTRO do esperado.
- Compromissos do Scrum: mantém os nomes certos e troca as
  ligações (Definition of Done colada ao Product Backlog).

## Como se sair melhor
- Decore o par: RF = função/comportamento; RNF = qualidade
  (desempenho, usabilidade, segurança, manutenibilidade) ou
  restrição. Ao contar, marque cada verbo de ação (RF) e cada
  "deve ser rápido/seguro/exportável" (RNF).
- APF: cada tela que ENTRA e grava dado = EE; que SÓ mostra
  dado processado/calculado = SE; que só consulta e exibe sem
  cálculo = CE; grupo lógico mantido dentro = ALI; referência
  externa só lida = AIE.
- Scrum: SM remove impedimento e facilita, não decide nem
  executa; PO prioriza; time estima e se compromete pela
  capacidade. Mudança de escopo → backlog + PO, nunca "recusar
  por comprometer o plano".
- Modelo V, na dúvida use as pontas: em cima requisito ↔
  aceitação; embaixo código ↔ unidade. O meio se resolve por
  eliminação (arquitetural ↔ integração).
- Manutenção: pergunte QUAL A CAUSA. Defeito = corretiva;
  ambiente mudou = adaptativa; melhoria = perfectiva; falha
  que ainda não aconteceu = preventiva.
- Cobertura: 100% de decisões IMPLICA 100% de comandos, nunca
  o contrário. Comandos < decisões < caminhos.
- Compromissos do Scrum, pelo horizonte: produto (longo prazo)
  → Product Backlog; a Sprint → Sprint Backlog; o "pronto" →
  Incremento.
- Gatilhos de distrator: "sempre", "apenas", "exclusivamente",
  "nunca precisa alterar", "após a implementação".
- Verificação × validação: verificação = "construímos
  CORRETAMENTE?" (contra a especificação, aceita revisão de
  documento, sem executar); validação = "construímos o
  produto CERTO?" (contra a necessidade do usuário,
  aceitação/homologação). Passar na verificação e falhar na
  validação é o cenário: implementou o que foi especificado,
  mas foi especificada a coisa errada.
