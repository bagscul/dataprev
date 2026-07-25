# Business Intelligence (BI) — resumo (Perfil 3)

> **Edital (Perfil 3):** conceitos, fundamentos, técnicas e métodos de BI;
> sistemas de suporte à decisão (SSD) e gestão de conteúdo; arquitetura e
> aplicações de **data warehouse com ETL e OLAP**; data warehouse e data
> mining; visualização (BD individuais e cubos); mapeamento das fontes de
> dados; arquitetura de BI.
> **Peso esperado: MÉDIO.** Costuma cair junto com Banco de Dados.

## 1. O que é BI

Conjunto de conceitos e ferramentas para transformar **dado** em
**informação** e apoiar a **tomada de decisão**. Pirâmide clássica:
**dado → informação → conhecimento → inteligência/sabedoria**.

## 2. Data Warehouse (DW)

Repositório central de dados **integrados, históricos e orientados a assunto**,
para análise (não para transação). Características (Inmon): **orientado a
assunto, integrado, não volátil, variante no tempo**.

- **Data Mart:** recorte departamental do DW.
- **DW × Data Lake:** DW guarda dado **tratado e modelado** (schema-on-write);
  Lake guarda dado **bruto** estruturado e não estruturado (schema-on-read).
- **Staging area:** área intermediária onde o ETL trata os dados.
- **Lakehouse:** une a governança do DW com a flexibilidade do Lake. Camadas
  típicas: **Bronze** (bruto) → **Silver** (limpo) → **Gold** (dimensional,
  pronto para BI). ML consome o bruto; BI consome o Gold.

Pegadinha: o Data Lake **não** "substitui" o DW e **não** guarda só dado
estruturado. Lakehouse é o que combina os dois — não é sinônimo de nenhum
deles isoladamente.

## 3. ETL — a ponte para o DW

**Extract → Transform → Load.** Principal objetivo: **extrair de várias
fontes, transformar em formato padronizado e consistente, e carregar no DW.**
Não é "criar dashboards" nem "treinar modelo de ML" — isso vem depois.

- **ETL × ELT:** ver `banco-dados.md` (a posição do T).

## 4. OLAP e modelagem dimensional

- **OLAP** (analítico) × **OLTP** (transacional): ver `banco-dados.md`.
- **Cubo:** dados organizados em **dimensões** (tempo, produto, local) e
  **métricas/fatos** (vendas, quantidade).
- **Operações OLAP:**
  - **Drill-down:** desce ao detalhe (ano → mês → dia).
  - **Roll-up (drill-up):** sobe à agregação.
  - **Slice:** fatia uma dimensão (fixa um valor).
  - **Dice:** subcubo (vários valores de várias dimensões).
  - **Pivot (rotate):** gira a visão.
- **Modelagem dimensional:** **Star Schema** (fato + dimensões
  desnormalizadas, mais rápido) × **Snowflake** (dimensões normalizadas).

**Relacional × multidimensional** — duas formas de organizar o mesmo dado:

| | Relacional (OLTP) | Multidimensional (OLAP) |
|---|---|---|
| Organiza em | tabelas normalizadas (até 3FN) | fatos × dimensões (cubo) |
| Otimizado para | **escrita** curta e concorrente | **leitura** analítica, agregação |
| Redundância | evitada | **aceita de propósito** |

Armazenamento do cubo: **ROLAP** (fica no relacional, cubo montado por
consulta), **MOLAP** (cubo pré-calculado, consulta mais rápida), **HOLAP**
(híbrido).

Pegadinha: trocar drill-down↔roll-up; star↔snowflake; OLAP↔OLTP; ROLAP↔MOLAP
(o **M** é de multidimensional, o cubo pré-calculado).

### 4.1 Granularidade (o grão da fato)

**Grão = o que uma linha da tabela fato representa.** É a primeira decisão do
projeto dimensional e, na prática, irreversível.

- Grão **fino** ("uma linha por atendimento"): **amplia** as análises
  possíveis — dá para agregar depois em qualquer nível.
- Grão **grosso** ("uma linha por unidade por dia"): tabela menor, mas o
  detalhe está **perdido para sempre**.

Regra de Kimball: declare o grão no nível **mais atômico** que a fonte
permitir; agregados vêm **a partir** do detalhe, nunca no lugar dele.

Pegadinha: a FGV inverte a consequência (diz que o grão detalhado *restringe*
as análises) ou define granularidade pela quantidade de dimensões — é pelo
que **uma linha da fato representa**.

### 4.2 Tipos de fato e dimensão

- **Fato aditivo:** soma em **todas** as dimensões (ex.: vendas).
- **Fato semiaditivo:** **não** soma em todas — tipicamente não no tempo
  (saldo, estoque).
- **Fato não aditivo:** razão/percentual, nunca soma.
- **Dimensão degenerada:** atributo de identificação (nº do pedido) que fica
  na tabela fato, sem dimensão própria.

Pegadinha: trocar semiaditivo por aditivo — o saldo de hoje não é a soma dos
saldos anteriores.

### 4.3 Dimensões lentamente mutantes (SCD)

Quando um atributo de dimensão muda (o cliente troca de cidade):

| Tipo | O que faz | Histórico |
|---|---|---|
| **1** | **sobrescreve** o valor antigo | **perdido** |
| **2** | **insere novo registro** versionado (nova chave *surrogate*, com data início/fim) | **preservado por completo** |
| **3** | guarda o **valor anterior em outra coluna** | só **uma** mudança |

O **tipo 2** é o do cenário clássico ("as vendas antigas continuam associadas
à cidade da época") — e é ele que justifica a **chave *surrogate*** da
dimensão, que identifica a **versão**, não a entidade.

Pegadinha: oferecer o tipo 1 para cenário que pede histórico (ou o tipo 2 para
correção de erro de digitação, onde o certo *é* sobrescrever). O tipo 3 é o
distrator "quase certo": preserva só o valor imediatamente anterior.

## 5. Sistemas de Suporte à Decisão (SSD/DSS)

Apoiam gestores em problemas **estruturados, semiestruturados e não
estruturados** — oferecem flexibilidade para vários contextos. Não são "só
para problemas estruturados" nem "só não estruturados".

## 6. Mapeamento de fontes de dados (boas práticas)

- **Fazer:** entrevistar stakeholders, analisar sistemas existentes, avaliar
  **qualidade** e adequação do dado, documentar fontes (governança).
  Referência: **DAMA-DMBOK**, dados **mestres** e de **referência**.
- **NÃO fazer:** coletar **tudo sem discriminação**, incluindo dados
  inconsistentes/irrelevantes "para maximizar quantidade" — isso é a prática
  **não recomendada** (a FGV pede a errada).

## 7. Data Mining e visualização

- **Data Mining:** descobrir padrões, correlações e conhecimento não trivial
  em grandes volumes.

| Tarefa | Tem rótulo? | Cenário típico |
|---|---|---|
| Classificação | **sim** (supervisionada) | prever se o cliente vai inadimplir |
| Regressão | **sim** (supervisionada) | prever um **valor numérico** |
| Clusterização | **não** (não supervisionada) | **descobrir grupos** parecidos, sem rótulo prévio |
| Regras de associação | não | **o que é comprado junto** (cesta de compras) |

- **Regras de associação:** **suporte** = frequência do conjunto no total de
  transações; **confiança** = força da implicação A→B. A FGV confunde os dois.
- **Dashboards e relatórios interativos:** camada de visualização (Power BI —
  com **drillthrough** entre páginas —, Qlik, etc.).

Pegadinha: **classificação × clusterização** — "sem rótulos prévios" ou
"descobrir grupos" é clusterização; "produtos comprados juntos" é regra de
associação, nunca clusterização.

### 7.1 CRISP-DM — o ciclo de um projeto de mineração

1. Entendimento do **negócio** (é por aqui que começa, não pelos dados)
2. Entendimento dos **dados**
3. **Preparação** dos dados
4. **Modelagem**
5. **Avaliação** (os resultados atendem aos objetivos de **negócio**?)
6. **Implantação**

Ciclo **iterativo**, não cascata. Pegadinha: confundir a avaliação (fase 5,
contra o negócio) com a validação técnica do modelo (parte da modelagem); ou
começar o ciclo pelo entendimento **dos dados**. Depois da avaliação vem a
**implantação**.

## O que já caiu

**Em prova real da FGV:** SSD para os três tipos de problema e a prática *não*
recomendada no mapeamento de fontes (coletar tudo sem discriminar) —
**Dataprev 2024**; Star × Snowflake em varejo/DW (contagem de *joins*), o que
a tabela fato contém (FKs + medidas numéricas), Data Mart como recorte
departamental e o que pertence à fase de **Transformação** do ETL — **ALERO
2026**; arquitetura **Lakehouse** e **dice** — **TJ-RJ**; **suporte** ×
**confiança**, relacional × multidimensional e *drillthrough* no Power BI —
**MPU**. O par ETL × ELT caiu na **Dataprev 2024**, como item de Banco de
Dados (`banco-dados.md`).

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): granularidade (o grão da fato); **SCD tipo 2**; as fases do
**CRISP-DM**; fato semiaditivo; as quatro características de Inmon;
clusterização × regras de associação; DW × Data Lake; drill-down × roll-up.

Rode `../quiz.py bi`.

## Pegadinhas da FGV (resumo)

- Trocar o objetivo do ETL (dizer que é dashboard ou ML).
- Restringir SSD a um só tipo de problema.
- Marcar como "boa prática" o "coletar tudo sem filtrar qualidade".
- Inverter operações OLAP e esquemas dimensionais.
- Ver `../dicas/bi.md`.

## Alta probabilidade / pesquisa extra

- **Kimball (bottom-up, data marts) × Inmon (top-down, DW corporativo).**
- **Self-service BI** e **storytelling com dados** (aparece no Perfil 1).
- **KPI × métrica:** KPI é indicador-chave atrelado a objetivo.
