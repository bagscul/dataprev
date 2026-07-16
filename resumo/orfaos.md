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

- **RPO** (Recovery Point Objective): quanto de dado se aceita perder (janela).
- **RTO** (Recovery Time Objective): em quanto tempo o serviço volta.
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
- **Blockchain:** ver [programacao](programacao.md).

## Como se sair melhor

- Muita questão "órfã" é DBA disfarçado — se o cenário fala em backup,
  tablespace, plano de execução, log/recuperação, é administração de BD.
- Memorize os pares: AD × DBA, incremental × diferencial, RPO × RTO, ordem do
  ARIES, bitmap × B+ Tree.

## Rode as questões

`../quiz.py orfaos` — mistura DBA, administração de dados, processos e temas
avulsos que caíram nas provas reais.
