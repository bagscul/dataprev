# Órfãos — administração de BD + temas coringa (Perfil 3)

> Bloco "coringa" do quiz: o que não encaixa nos outros. Na prática, a maior
> parte das questões daqui é **administração de banco de dados (DBA)** e
> **administração de dados** — conteúdo do edital ("noções de administração de
> dados e de banco de dados; backup, restauração; otimização de performance")
> que o [banco-dados](banco-dados.md) (focado em modelagem/SQL) não detalha.
> O resto são temas avulsos (arquitetura de computadores, informática,
> sistemas de informação, blockchain).

## 1. Administração de Dados × Administração de Banco de Dados

| | Administração de **Dados** (AD) | Administração de **BD** (DBA) |
|---|---|---|
| Foco | **negócio/lógico**: o dado como recurso corporativo | **técnico/físico**: o SGBD funcionando |
| Faz | modelagem conceitual, políticas, governança, dicionário de dados | instalação, tuning, backup, segurança, disponibilidade |
| Papel | estratégico, independe de SGBD | operacional, ligado ao produto (Oracle, etc.) |

Pegadinha: AD é conceitual/negócio; DBA é físico/operacional. A FGV troca os dois.

## 2. Recuperação e transações (ARIES)

- **ARIES** (protocolo de recuperação da maioria dos SGBDs): usa **WAL**
  (Write-Ahead Logging — o log vai para disco **antes** do dado) e três fases
  na recuperação após falha, **nesta ordem**:
  1. **Analysis** (Análise): reconstrói o estado a partir do último checkpoint.
  2. **Redo** (Refazer): reaplica TODAS as operações registradas (até as de
     transações que não commitaram) — "repeating history".
  3. **Undo** (Desfazer): desfaz as transações que não commitaram.
- **WAL** garante a durabilidade (D do ACID) sem gravar o dado imediatamente.

Pegadinha: ordem Analysis → Redo → Undo (a FGV inverte Redo/Undo).

## 3. Armazenamento físico e desempenho

- **Tablespace** (Oracle) / filegroup: unidade lógica de armazenamento que
  agrupa objetos em arquivos físicos. Separa dados, índices, temporário.
- **Índices** (B+ Tree, bitmap, hash): aceleram busca ao custo de escrita.
  Bitmap é bom para **baixa cardinalidade** (poucos valores distintos);
  B+ Tree para alta cardinalidade e faixas.
- **Otimizador de consultas (query optimizer):** escolhe o **plano de
  execução** (ordem de joins, uso de índice). Planos ruins geralmente vêm de
  **estatísticas desatualizadas** — atualizar estatísticas costuma resolver.
- **Particionamento** (horizontal/sharding, vertical): divide tabela grande
  para escalar e melhorar desempenho.

## 4. Backup e recuperação

| Tipo | O que copia |
|---|---|
| **Completo (full)** | tudo |
| **Incremental** | só o que mudou **desde o último backup (de qualquer tipo)** |
| **Diferencial** | tudo que mudou **desde o último backup completo** |

- **RPO** (Recovery Point Objective): quanto de dado se aceita perder (janela)
  — é ele que determina a frequência do backup.
- **RTO** (Recovery Time Objective): em quanto tempo o serviço volta.
- O par completo, com MTBF/MTTR/SLA e a pegadinha da inversão, está em
  [seguranca](seguranca.md#61-continuidade-de-negócio-rto--rpo) — as questões
  de RTO/RPO estão etiquetadas como `seguranca`, não como `orfaos`.
- Backup **quente** (online, banco no ar) × **frio** (offline).

Pegadinha: incremental (desde o último **qualquer**) × diferencial (desde o
último **completo**) — a diferencial cresce até o próximo full.

## 5. Segurança e acesso no SGBD

- **GRANT/REVOKE** (DCL), **roles/papéis** (RBAC), **views** para restringir
  colunas, **row-level security**, auditoria.
- Princípio do **menor privilégio**: o gerente de RH acessa só o que precisa.

## 6. Temas coringa genuínos

- **Arquitetura de computadores:** CPU (Unidade de Controle × ULA), ciclo de
  instrução (busca-decodifica-executa), pipeline, memória (registrador →
  cache → RAM → disco, mais rápida e cara no topo), sistemas de numeração
  (binário, octal, hexadecimal — conversão dígito a dígito).
- **Noções de informática:** pacote office, sistemas de arquivos, atalhos.
- **Sistemas de informação:** SIG, SPT (transacional), SAD/SSD (decisão),
  ERP, CRM, SCM — o nível gerencial que cada um atende.

## 7. IA/ML (tema quente neste bloco)

Nas provas recentes a FGV vem carregando em IA/ML e cloud — trate como tema
quente. Os fundamentos de IA (hierarquia IA ⊃ ML ⊃ Deep Learning, tipos de
aprendizado, LLM/RAG/alucinação, ética e regulação) estão em
[atualidades](atualidades.md); aqui ficam os pares operacionais que caem
etiquetados como `orfaos`.

- **Supervisionado × não supervisionado × semissupervisionado.** Supervisionado
  usa dados **rotulados** (classificação, regressão); não supervisionado acha
  estrutura **sem rótulo** (clusterização, associação). A FGV inverte
  "rotulado" entre os dois.
- **Overfitting** (decora o treino, vai mal em dados novos) × **underfitting**
  (modelo simples demais). A **regularização combate o overfitting**.
- **Regularização: L1 (Lasso)** zera coeficientes e faz seleção de atributos;
  **L2 (Ridge)** encolhe sem zerar. A banca troca os dois. Caiu no TJ-RJ.
- **Concept drift** (muda a relação entrada→saída, o próprio conceito alvo) ×
  **data drift** (muda a distribuição da **entrada**). Fácil de trocar, e os
  dois caíram no TJ-RJ.
- **Métricas:** MAE = erro médio absoluto (regressão, caiu no TJ-RJ); F1 =
  média **harmônica** de precisão e recall; ROC/AUC = capacidade de separar
  classes variando o limiar. O detalhe de precisão × recall e da acurácia
  enganosa em base desbalanceada está em [atualidades](atualidades.md).
- **Redes neurais** (ativação sigmoide) e **CNN**; **LLM/IA generativa**: RAG,
  agentes, engenharia de prompt, ética e explicabilidade.
- **MLOps:** em cenário de IA em produção, "monitorar drift" e deploy
  blue-green/canário são as respostas típicas. Não confundir IA **generativa**
  (cria conteúdo) com **discriminativa** (classifica/prediz).

## 8. Onde cada tema coringa está detalhado

Este é o bloco mais transversal do material: como o quiz aponta o capítulo
pela **tag** da questão, tudo que é `orfaos` cai aqui — mesmo quando o
conteúdo mora, com razão, em outro lugar. Use este mapa.

| Tema | Onde está |
|---|---|
| Blockchain (hash do bloco anterior, raiz de Merkle, *nonce*, imutabilidade encadeada) | [programacao](programacao.md) |
| Servidor web × servidor de aplicação | [arquitetura](arquitetura.md) |
| 2PC (two-phase commit) e o contraste com Raft | [arquitetura](arquitetura.md) |
| Virtualização: hipervisor Tipo 1 × Tipo 2 × contêiner | [arquitetura](arquitetura.md) |
| SO: paginação/memória virtual, E/S bloqueante, troca de contexto | [arquitetura](arquitetura.md) |
| Low-code / no-code | [programacao](programacao.md) |
| RPA (Robotic Process Automation) | [eng-software](eng-software.md) e [programacao](programacao.md) |
| Os Vs do Big Data | [banco-dados](banco-dados.md) |
| Internet × intranet × extranet × portal | [redes](redes.md) |
| IA generativa, LLM, RAG, ética e regulação | [atualidades](atualidades.md) |

Três valem uma frase aqui, porque são o que a questão cobra e o candidato
resolve no reflexo errado:

- **2PC:** um **coordenador** pergunta a todos os participantes se podem
  confirmar (fase *prepare*) e só ordena o *commit* com **unanimidade** — um
  único "não" aborta tudo. Não é maioria simples (isso é consenso, tipo Raft)
  nem confirmação independente de cada nó.
- **RPA:** software que **imita o usuário** (clique, digitação, leitura de
  tela) em tarefas digitais repetitivas e **baseadas em regras**. Não é IA,
  não é robô físico, não substitui banco de dados.
- **Low-code:** desenvolvimento por **modelagem visual e configuração**, com o
  **mínimo** de código manual — *no-code* elimina o código de vez. Nenhum dos
  dois "dispensa desenvolvedor profissional": esse absoluto é o distrator.

## O que já caiu

**Em prova real da FGV: 21 questões, e nenhuma delas é conteúdo do Perfil 3.**
Depois que a classificação foi consertada, este bloco virou o que o nome sempre
prometeu — o que não tem casa — e se divide em duas famílias, as duas fora do
edital:

- **Arquitetura de computadores e sistema operacional (11).** Gargalo de **Von
  Neumann**, ULA e unidade de controle, *overflow* × *carry*, complemento de
  dois, conversão de base, ROM/firmware, periférico, ciclo
  busca-decodificação-execução, **MMU/TLB** e *thrashing*, tabela de páginas,
  **DMA** — **ALERO 2026** e **TJ-RJ**. O edital do Perfil 3 fala em
  arquitetura *de software* ([arquitetura](arquitetura.md)).
- **Administração e direito público (10).** Avaliação de desempenho de
  gestores, priorização de melhoria de processo, liderança de equipe,
  departamentalização, Resolução CNMP, redistribuição de cargo, compromisso da
  LINDB, critério de desempate em licitação, responsabilidade da concessionária
  e processo disciplinar — **MPU**, tudo do Módulo I daquele concurso.

**O que saiu daqui.** Até o fechamento do ITEM 7 este bloco declarava 68
questões e "maioria esmagadora DBA". Era sintoma de um defeito do importador: o
rótulo de sub-bloco dos mapas da ALERO usava o *slug* (`banco-dados`,
`eng-software`), que a tabela de tags não reconhecia, e 47 questões caíam aqui
por engano. Foram para onde sempre pertenceram — **34 para banco de dados**
([banco-dados](banco-dados.md)) e **13 para engenharia de software**
([eng-software](eng-software.md)). O *conteúdo* de administração física (ARIES,
B+ Tree, tablespaces, otimizador, backup) continua sendo ensinado aqui, e o
resumo de banco de dados remete para cá.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): blockchain pelo encadeamento de hash; RPA; low-code; os Vs do Big
Data; supervisionado × não supervisionado. Dois itens que já estiveram nesta
lista **caíram** de fato, só que sob outra tag na **Dataprev 2024**: **servidor
web × servidor de aplicação** ([arquitetura](arquitetura.md)) e
**internet/intranet/extranet/portal** (item de redes, [redes](redes.md)).

## Como se sair melhor

- O que este resumo **ensina** continua valendo muito: administração física de
  banco de dados é matéria de prova, e as questões dela agora estão sob
  `banco-dados`. O que ficou com a etiqueta de órfã é material de outro perfil —
  reconheça e siga em frente.
- Memorize os pares: AD × DBA, incremental × diferencial, RPO × RTO, ordem do
  ARIES, bitmap × B+ Tree, rotulado × não rotulado, data × concept drift,
  L1 × L2, Tipo 1 × Tipo 2, over × underfitting.

## Rode as questões

`../quiz.py orfaos` — mistura DBA, administração de dados, processos e temas
avulsos que caíram nas provas reais.
