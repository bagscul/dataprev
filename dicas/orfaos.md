# orfaos — como a FGV cobra

Bloco coringa: o que não entra em outro bloco cai aqui —
informática básica, arquitetura de computadores, sistemas
de informação, IA/ML e blockchain. Nas provas recentes a
FGV vem carregando em IA/ML e cloud; trate como tema quente.

## O que mais cai
- IA/ML: supervisionado x não supervisionado x
  semissupervisionado; over/underfitting e regularização
  L1/L2; concept drift x data drift; métricas (MAE, F1,
  ROC/AUC); redes neurais (ativação sigmoide) e CNN.
- LLM/IA generativa: RAG, agentes, engenharia de prompt,
  ética e explicabilidade.
- Arquitetura de computadores/SO: memória virtual e tabela
  de páginas, E/S bloqueante, troca de contexto,
  hipervisor Tipo 1 x Tipo 2 x contêiner.
- Sistemas de informação: internet x intranet x extranet x
  portal; SSD/BI; níveis de decisão.
- Blockchain: estrutura do bloco (hash do anterior,
  Merkle, nonce) e imutabilidade encadeada.

## Como a banca arma a pegadinha
- Troca os paradigmas de ML: supervisionado usa dados
  ROTULADOS (classificação/regressão); não supervisionado
  acha estrutura sem rótulo (clusterização/associação). A
  FGV inverte "rotulado" entre os dois.
- Confunde drift: DATA drift = muda a distribuição da
  ENTRADA; CONCEPT drift = muda a relação entrada→saída (o
  próprio conceito alvo). Fácil de trocar.
- Inverte hipervisor: Tipo 1 (bare-metal) roda direto no
  hardware; Tipo 2 roda sobre um SO hospedeiro; contêiner
  compartilha o kernel do host (não virtualiza hardware).
- Troca internet/intranet/extranet: intranet = interna;
  extranet = estende a intranet a parceiros externos.
- Regularização: L1 (Lasso) zera coeficientes e faz seleção
  de atributos; L2 (Ridge) encolhe sem zerar. A banca troca.
- Overfitting = decora o treino e vai mal em dados novos;
  underfitting = modelo simples demais. Distrator inverte
  qual deles a regularização combate (é o overfitting).

## Como se sair melhor
- Monte flashcards de PARES que a FGV inverte: rotulado x
  não rotulado, data x concept drift, L1 x L2, Tipo 1 x
  Tipo 2, over x underfitting, intranet x extranet.
- ML por métrica: MAE = erro médio absoluto (regressão);
  F1 = média harmônica de precisão e recall; ROC/AUC =
  capacidade de separar classes variando o limiar.
- Em cenário de IA em produção, "monitorar drift" e
  deploy blue-green/canário são as respostas de MLOps.
- Não confunda IA generativa (cria conteúdo) com IA
  discriminativa (classifica/prediz).
