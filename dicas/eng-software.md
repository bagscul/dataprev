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
  contínua e reduzem retrabalho de regressão.
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
- Gatilhos de distrator: "sempre", "apenas", "exclusivamente",
  "nunca precisa alterar", "após a implementação".
