# Banco de Dados — resumo (Perfil 3)

> **Atenção ao recorte:** o Perfil 3 **não tem "Banco de Dados" como
> disciplina**. O assunto entra por duas portas: **Inteligência de Negócios**
> ("arquitetura e aplicações de *data warehouse* com ETL e OLAP", "*data
> warehouse* e *data mining*", "visualização de dados: BD individuais e
> cubos") e o item 20 de Desenvolvimento de Sistemas ("Conceitos de
> Inteligência Artificial, **Análise de Dados** e Big Data").
>
> A lista fechada — modelagem e normalização, arquitetura, estrutura de dados,
> SQL (ANSI), administração de dados, backup/restauração, engenharia de
> dados/Big Data — e os **SGBD nomeados** (Oracle 19C, MySQL, PostgreSQL,
> MongoDB, MS-SQL Server 2019) estão no **Perfil 2**. Estudamos assim mesmo
> porque a **FGV cobrou banco de dados no Perfil 3 da Dataprev 2024** — do
> mesmo jeito que cobrou redes, que também não está no perfil.
>
> **Peso esperado: ALTO por evidência de prova**, não por peso de edital.
> Metade do "eixo duplo" com Eng. de Software; no MPU 2025 foi o bloco que
> mais caiu.

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
- **Álgebra relacional:** seleção (σ) = `WHERE` = filtra **linhas**; projeção
  (π) = filtra **colunas**.

### 2.1 Do MER para o relacional (como cada cardinalidade vira tabela)

| Cardinalidade | Implementação no modelo relacional |
|---|---|
| **1:1** | FK em uma das duas tabelas (de preferência no lado obrigatório), com restrição de unicidade |
| **1:N** | **FK no lado N** — a tabela "muitos" guarda a chave da tabela "um" |
| **N:M** | **tabela associativa** (intermediária), com as FKs das duas pontas formando a PK composta |

Pegadinha: N:M **nunca** se resolve com FK direta em uma das tabelas (isso só
atende 1:N) nem com coluna multivalorada — que viola a **1FN**. Trigger e
índice composto não implementam cardinalidade nenhuma.

**Entidade fraca × entidade associativa.** A **fraca** não se identifica
sozinha: sua chave é a chave da **entidade proprietária** somada a uma **chave
parcial** (discriminador) — DEPENDENTE só é identificado dentro do cadastro de
um SERVIDOR, pelo nome. O relacionamento com o proprietário é **identificador**
e a existência da fraca depende da forte. Já a **associativa** é o
relacionamento **N:M promovido a entidade**, quando ele precisa se relacionar
com uma terceira entidade ou ganhar atributos próprios.

Pegadinha: a quase-certa diz "entidade fraca, que **dispensa** a chave do
proprietário" — é o oposto. E ter atributos próprios **não** torna a entidade
forte: o que define a força é identificar-se sozinha.

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

### 4.1 Código no servidor: gatilho × procedimento armazenado

| | **Gatilho (trigger)** | **Procedimento armazenado** |
|---|---|---|
| Quem dispara | o **próprio SGBD**, em resposta a um **evento** de dados | a **aplicação**, por chamada explícita |
| Como se invoca | não se invoca — é automático | `CALL` / `EXECUTE` |
| Amarrado a | uma tabela + evento (INSERT, UPDATE, DELETE) | nada; é código nomeado e reutilizável |
| Parâmetros | não recebe | recebe (e pode retornar) |
| Bom para | auditoria, log, regra que **não pode depender** da aplicação lembrar | rotina de negócio chamada sob demanda |

Pegadinha: dizer que o **procedimento** é "acionado automaticamente pelo SGBD
a cada UPDATE" (isso é o gatilho) ou que o **gatilho** é "invocado com um
`CALL`" (isso é o procedimento). Gatilho também **não substitui** integridade
referencial declarada. Palavra-chave do enunciado: "**sem depender de a
aplicação lembrar**" → gatilho.

## 5. Propriedades ACID (transações)

- **A**tomicidade: tudo ou nada.
- **C**onsistência: leva o banco de um estado válido a outro.
- **I**solamento: transações concorrentes não interferem.
- **D**urabilidade: efeito confirmado persiste (mesmo após falha).

## 5.1 Concorrência: níveis de isolamento

O "I" do ACID não é tudo-ou-nada: o padrão SQL define **quatro níveis**, e
cada um *admite* certos fenômenos. Quanto maior o isolamento, **menor** a
concorrência — é trade-off, não ganho de graça.

**Os três fenômenos:**

- **Leitura suja** (*dirty read*): lê dado alterado por transação que **ainda
  não confirmou** (e pode desfazer).
- **Leitura não repetível**: relê a **mesma linha** e o valor mudou.
- **Leitura fantasma** (*phantom*): relê a **mesma faixa** e aparecem **linhas
  novas**, inseridas e confirmadas por outra transação.

| Nível | Leitura suja | Não repetível | Fantasma |
|---|---|---|---|
| READ UNCOMMITTED | admite | admite | admite |
| READ COMMITTED | **impede** | admite | admite |
| REPEATABLE READ | impede | **impede** | admite |
| SERIALIZABLE | impede | impede | **impede** |

Pegadinhas: dizer que **READ UNCOMMITTED é o mais restritivo** (é o mais
**permissivo**) e que **REPEATABLE READ elimina o fantasma** (elimina a não
repetível; fantasma só cai no SERIALIZABLE). E o absoluto invertido: "quanto
mais alto o isolamento, maior a concorrência". Marque pelo objeto: linha que
**muda de valor** = não repetível; linha **nova que aparece** = fantasma.

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

## 9. Índices e notações (apareceram nas provas)

- **Índices:** **B+ Tree** (padrão, bom para faixas e alta cardinalidade),
  **bitmap** (baixa cardinalidade, ex: sexo/status), **hash** (igualdade
  exata). **Hashing extensível:** hash dinâmico com um **diretório** de
  ponteiros e *global depth*; quando um bucket enche, ele faz **split** e
  dobra o diretório se preciso — cresce sem reorganizar tudo.
- **IDEF1X:** notação de modelagem de dados (comum em ferramentas como o
  erwin). Relacionamento **identificador** = linha **sólida**; entidade
  dependente = retângulo de **cantos arredondados**.
- Administração física (tablespaces, ARIES/recuperação, backup, otimizador)
  está em [orfaos](orfaos.md).

## O que já caiu (nossas questões)

Relacional × multidimensional (OLTP/OLAP); NoSQL (disponibilidade e escala
horizontal); ETL × ELT (a incorreta); ETL como ponte para o DW; normalização
1FN-3FN; integridade referencial; TRUNCATE/DELETE; teorema CAP; Star ×
Snowflake; desnormalização em DW; Data Warehouse × Data Lake × Lakehouse;
N:M resolvido por tabela associativa; entidade fraca; níveis de isolamento e
os fenômenos que cada um admite; gatilho × procedimento armazenado.
Rode `../quiz.py banco-dados` e `../quiz.py bi`.

## Pegadinhas da FGV (resumo)

- Inverter OLTP↔OLAP, ETL↔ELT, TRUNCATE↔DELETE, DW↔Data Lake.
- Absolutos sobre NoSQL ("sempre ACID", "sempre grafo", "sempre melhor").
- Trocar a ordem dos níveis de modelagem ou das formas normais.
- Ver `../dicas/banco-dados.md`.

## Alta probabilidade / pesquisa extra

- **SGBD nomeados no edital:** Oracle 19C, MySQL, PostgreSQL, MongoDB, MS-SQL
  Server 2019 — item **7.1 do Perfil 2**, não do 3. Nenhuma questão deve
  depender de sintaxe proprietária de um deles; o que pode vir para nós é o
  **conceito** (SQL ANSI, o par relacional × documento).
- **Modelagem dimensional (Kimball):** **Star Schema** (uma tabela fato +
  dimensões desnormalizadas, mais rápido) × **Snowflake** (dimensões
  normalizadas, menos redundância, mais joins).
- **Big Data — 5 V:** Volume, Velocidade, Variedade, Veracidade, Valor.
