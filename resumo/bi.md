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

Pegadinha: trocar drill-down↔roll-up; star↔snowflake; OLAP↔OLTP.

## 5. Sistemas de Suporte à Decisão (SSD/DSS)

Apoiam gestores em problemas **estruturados, semiestruturados e não
estruturados** — oferecem flexibilidade para vários contextos. Não são "só
para problemas estruturados" nem "só não estruturados".

## 6. Mapeamento de fontes de dados (boas práticas)

- **Fazer:** entrevistar stakeholders, analisar sistemas existentes, avaliar
  **qualidade** e adequação do dado, documentar fontes (governança).
- **NÃO fazer:** coletar **tudo sem discriminação**, incluindo dados
  inconsistentes/irrelevantes "para maximizar quantidade" — isso é a prática
  **não recomendada** (a FGV pede a errada).

## 7. Data Mining e visualização

- **Data Mining:** descobrir padrões em grandes volumes (classificação,
  agrupamento/clustering, associação, regressão).
- **Dashboards e relatórios interativos:** camada de visualização (Power BI,
  Qlik, etc.).

## O que já caiu (nossas questões)

ETL como ponte/objetivo (extrair-transformar-carregar); SSD para os três tipos
de problema; prática não recomendada no mapeamento de fontes (coletar tudo
sem discriminar); relacional × multidimensional; ETL × ELT. Rode `../quiz.py bi`.

## Pegadinhas da FGV (resumo)

- Trocar o objetivo do ETL (dizer que é dashboard ou ML).
- Restringir SSD a um só tipo de problema.
- Marcar como "boa prática" o "coletar tudo sem filtrar qualidade".
- Inverter operações OLAP e esquemas dimensionais.
- Ver `../dicas/bi.md`.

## Alta probabilidade / pesquisa extra

- **Kimball (bottom-up, data marts) × Inmon (top-down, DW corporativo).**
- **Lakehouse:** une governança do DW com flexibilidade do Lake.
- **Self-service BI** e **storytelling com dados** (aparece no Perfil 1).
- **KPI × métrica:** KPI é indicador-chave atrelado a objetivo.
