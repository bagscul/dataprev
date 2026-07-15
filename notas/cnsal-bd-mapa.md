# Mapa de questões — ALE-RO 2026, Analista Legislativo TI / Banco de Dados (FGV)

Fonte: prova FGV para a Assembleia Legislativa de Rondônia (ALE-RO), Edital
01/2025, Analista Legislativo — Tecnologia da Informação, **Banco de Dados**,
tarde, tipo 1 (branca), 80 questões.

**Este arquivo cobre só os ESPECÍFICOS (Q41-80).** As questões 1-40 são o
**módulo comum** desta banca (Português, RLM, Legislação Específica, História e
Geografia de Rondônia) — idênticas às da prova de Análise/Desenvolvimento de
Sistemas e mapeadas em `notas/cnsal-ads-mapa.md`. Não repito aqui.

A coluna sub-bloco é classificação minha por conteúdo (nomes dos blocos de
`erros/`), não rótulo da FGV — guia de estudo, não gabarito de proporção.

## Módulo I (Conhecimentos Gerais) — comum, 1-40

Ver `notas/cnsal-ads-mapa.md`. Blocos: Língua Portuguesa (1-12), Raciocínio
Lógico-matemático (13-24), Legislação Específica (25-32), História e Geografia
de Rondônia (33-40).

## Módulo II — Conhecimentos Específicos (41-80)

| Q | Tema | Sub-bloco |
|---|---|---|
| 41 | Dependências funcionais, chave candidata e Forma Normal mais alta (BCNF) | banco-dados |
| 42 | SQL: CREATE TABLE com DEFAULT + INSERT sem o campo com padrão | banco-dados |
| 43 | SQL: departamentos com média salarial acima da média geral (GROUP BY / HAVING / subconsulta) | banco-dados |
| 44 | System Catalog — estatísticas para o otimizador de consultas | banco-dados |
| 45 | ARIES / WAL — fases de recuperação (Analysis, Redo, Undo) | banco-dados |
| 46 | Integridade referencial | banco-dados |
| 47 | Criptografia transparente de dados em repouso (TDE) | seguranca |
| 48 | Two-Phase Commit (2PC) — 1ª fase, vote-request/vote-commit | banco-dados |
| 49 | B+ Tree — folhas interligadas, eficiência em busca por intervalo | banco-dados |
| 50 | Data Warehouse x OLTP — desnormalização (estrela/floco) | bi |
| 51 | Snowflake x Star — mais JOINS, degradação de leitura | bi |
| 52 | ETL — operações da fase de Transformação | bi |
| 53 | Metadados e Dicionário de Dados / Catálogo do Sistema | banco-dados |
| 54 | Drivers JDBC/ODBC — tradução de chamadas de API ao SGBD | banco-dados |
| 55 | Hashing Extensível — global depth, bucket pointers, split | banco-dados |
| 56 | DBA proativo/preditivo — monitoramento e análise de tendências | banco-dados |
| 57 | Triggers para auditoria de alterações | banco-dados |
| 58 | Unidade de Controle (UC) — ciclo busca-decodificação-execução | arquitetura |
| 59 | Escopo de variáveis — estático/léxico x dinâmico | programacao |
| 60 | Compilador x interpretador | programacao |
| 61 | Índice de Bitmap — colunas de baixa cardinalidade em DW | bi |
| 62 | NoSQL chave-valor — latência mínima, escalabilidade horizontal | banco-dados |
| 63 | Tabela Fato (esquema estrela) — FKs + medidas numéricas | bi |
| 64 | Busca sequencial O(N) x binária O(log N) em arquivo desordenado | programacao |
| 65 | Data Mart — subconjunto do DW por departamento | bi |
| 66 | B+ Tree — alto fator de ramificação minimiza altura / acessos a disco | banco-dados |
| 67 | Índice Clustered — ordem física das tuplas | banco-dados |
| 68 | Backup Full + Differential — restauração, RPO/RTO | banco-dados |
| 69 | Tuning — criar índice para evitar Table Scan | banco-dados |
| 70 | Stored Procedure x Function/Trigger — controle transacional | banco-dados |
| 71 | Views para segurança no nível de coluna (omitir SALARIO) | banco-dados |
| 72 | XPath — consulta/extração de nó em documento XML | banco-dados |
| 73 | Função determinística — mesmo input, mesmo output, cacheável | banco-dados |
| 74 | Trigger AFTER INSERT — registro automático em outra tabela | banco-dados |
| 75 | Tablespaces — separação física de dados, backup parcial | banco-dados |
| 76 | XSD — validação da estrutura de documento XML | banco-dados |
| 77 | Atualização manual de estatísticas do otimizador | banco-dados |
| 78 | EXECUTE AS — SP executada com permissões de outro usuário | seguranca |
| 79 | Connection Pooling — reuso de conexões abertas | banco-dados |
| 80 | Especialização/generalização ER — restrições de totalidade e disjunção (Total, Sobreposta) | banco-dados |

## Como usar

Filtre por sub-bloco e abra as questões no PDF (mesma numeração). Cole aqui a
que você errou (número + gabarito, se tiver) que eu explico e já registro em
`erros/<bloco>.md`.
