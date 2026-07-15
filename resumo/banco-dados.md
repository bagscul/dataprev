# Banco de Dados — resumo (Perfil 3)

> **Edital (Perfil 3):** modelagem (conceitual, lógica, física); abordagem
> relacional e multidimensional; normalização; integridade referencial;
> metadados; modelagem dimensional; SQL, DDL, DML; SGBD; propriedades de BD;
> NoSQL; banco em memória; data lakes/big data; dados estruturados e não
> estruturados; avaliação de modelos; ETL/ELT.
> **Peso esperado: ALTO.** Metade do "eixo duplo" com Eng. de Software; no
> MPU 2025 foi o bloco que mais caiu.

## 1. Modelagem em três níveis

| Nível | O que é | Artefato |
|---|---|---|
| **Conceitual** | visão de negócio, independe de SGBD | Modelo Entidade-Relacionamento (MER/DER) |
| **Lógico** | estrutura no modelo escolhido (relacional) | tabelas, chaves, tipos genéricos |
| **Físico** | implementação no SGBD específico | DDL, índices, particionamento |

Ordem: conceitual → lógico → físico. A FGV inverte a ordem ou troca o
artefato de cada nível.

## 2. Modelo relacional e integridade

- **Chave primária (PK):** identifica unicamente a tupla; não nula, única.
- **Chave estrangeira (FK):** referencia a PK de outra (ou da mesma) tabela.
- **Integridade referencial:** toda FK aponta para uma PK existente (ou é
  nula). Ações: CASCADE, SET NULL, RESTRICT/NO ACTION.
- **Integridade de entidade:** PK não pode ser nula.

## 3. Normalização (formas normais)

| FN | Elimina |
|---|---|
| **1FN** | atributos multivalorados / não atômicos (cada célula um valor) |
| **2FN** | dependência parcial da chave (só relevante com PK composta) |
| **3FN** | dependência transitiva (atributo que depende de outro não-chave) |
| **FNBC (BCNF)** | anomalia quando há mais de uma chave candidata sobreposta |

Ordem 1FN → 2FN → 3FN → BCNF. Normalizar reduz redundância; **desnormalizar
de propósito** (ex: Data Warehouse) é aceitável por desempenho de leitura.

## 4. SQL: DDL × DML × DCL × TCL

| Sublinguagem | Comandos | Observação |
|---|---|---|
| **DDL** (definição) | CREATE, ALTER, **DROP, TRUNCATE** | TRUNCATE é DDL (não DML), auto-commit |
| **DML** (manipulação) | SELECT, INSERT, UPDATE, DELETE | DELETE é DML e pode ter WHERE + rollback |
| **DCL** (controle) | GRANT, REVOKE | permissões |
| **TCL** (transação) | COMMIT, ROLLBACK, SAVEPOINT | |

Pegadinhas: **TRUNCATE (DDL) × DELETE (DML)**; `UNION` remove duplicatas /
`UNION ALL` mantém; `WHERE` filtra linhas / `HAVING` filtra grupos após
`GROUP BY`; `JOIN` sem `ON` vira produto cartesiano; ordem de execução
lógica: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

## 5. Propriedades ACID (transações)

- **A**tomicidade: tudo ou nada.
- **C**onsistência: leva o banco de um estado válido a outro.
- **I**solamento: transações concorrentes não interferem.
- **D**urabilidade: efeito confirmado persiste (mesmo após falha).

## 6. Relacional × Multidimensional (OLTP × OLAP)

| | OLTP (transacional) | OLAP (analítico) |
|---|---|---|
| Uso | operações do dia a dia | apoio à decisão / análise |
| Escrita/leitura | muitas escritas curtas | leitura pesada, agregação |
| Modelo | relacional normalizado | multidimensional (cubos) |
| Estrutura | tabelas | dimensões e métricas/fatos |

Pegadinha central: a FGV troca OLTP↔OLAP. "Cubos, dimensões, agregação,
análise" = OLAP; "transação, muitas gravações" = OLTP.

## 7. NoSQL e novos armazenamentos

- **NoSQL:** alta disponibilidade e **escalabilidade horizontal**; costuma
  relaxar ACID (modelo **BASE**: Basically Available, Soft state, Eventual
  consistency). Tipos: **chave-valor** (Redis), **documento** (MongoDB),
  **colunar** (Cassandra), **grafo** (Neo4j). Não é "sempre grafo" nem "segue
  ACID estritamente"; não substitui ERP/CRM transacional por padrão.
- **Teorema CAP:** em sistema distribuído, escolha 2 de 3 —
  **C**onsistency, **A**vailability, **P**artition tolerance. Com partição
  (P inevitável em rede), decide-se entre C e A.
- **Banco em memória** (in-memory, ex: Redis): baixa latência.
- **Data Lake × Data Warehouse × Lakehouse:** Lake guarda dado bruto
  (schema-on-read, estruturado e não estruturado); DW guarda dado tratado e
  modelado (schema-on-write); Lakehouse combina os dois.

## 8. ETL × ELT

| | ETL | ELT |
|---|---|---|
| Ordem | Extrai → **Transforma** → Carrega | Extrai → Carrega → **Transforma** |
| Transformação | antes de carregar (fora do destino) | depois, no próprio destino |
| Bom para | DW tradicional | destino com muito poder de processamento (nuvem, big data) |

Pegadinha: a **posição do T**. ELT aproveita o processamento do destino;
ETL é melhor quando a transformação ocorre antes/fora.

## O que já caiu (nossas questões)

Relacional × multidimensional (OLTP/OLAP); NoSQL (disponibilidade e escala
horizontal); ETL × ELT (a incorreta); ETL como ponte para o DW; normalização
1FN-3FN; integridade referencial; TRUNCATE/DELETE; teorema CAP; Star ×
Snowflake; desnormalização em DW; Data Warehouse × Data Lake × Lakehouse.
Rode `../quiz.py banco-dados` e `../quiz.py bi`.

## Pegadinhas da FGV (resumo)

- Inverter OLTP↔OLAP, ETL↔ELT, TRUNCATE↔DELETE, DW↔Data Lake.
- Absolutos sobre NoSQL ("sempre ACID", "sempre grafo", "sempre melhor").
- Trocar a ordem dos níveis de modelagem ou das formas normais.
- Ver `../dicas/banco-dados.md`.

## Alta probabilidade / pesquisa extra

- **SGBD do edital:** Oracle 19c, MySQL, PostgreSQL, MongoDB, MS-SQL Server
  2019 (aparecem no Perfil 2; conceitos podem vir no 3).
- **Modelagem dimensional (Kimball):** **Star Schema** (uma tabela fato +
  dimensões desnormalizadas, mais rápido) × **Snowflake** (dimensões
  normalizadas, menos redundância, mais joins).
- **Big Data — 5 V:** Volume, Velocidade, Variedade, Veracidade, Valor.
