# bi — como a FGV cobra

## O que mais cai
- Modelagem dimensional (Kimball): Star Schema x Snowflake
  Schema — cenário longo de varejo/DW, hierarquia de
  produtos. Aparece nas duas provas de TI.
- OLAP: conceito de banco analítico e operações — dice
  (filtro múltiplo), slice, drill-down/up, roll-up, pivot.
- Arquitetura de dados moderna: Data Warehouse x Data Lake x
  Lakehouse (camadas Bronze/Silver/Gold, dados brutos para
  ML + dimensional para BI).
- Tipos de fato e dimensão: fato aditivo/semiaditivo/não
  aditivo, dimensão degenerada.
- ETL para modelo dimensional / Data Mart (inclusive
  ingerindo de NoSQL/MongoDB), chave surrogada.
- Mineração: regras de associação (suporte x confiança),
  Sistemas de Suporte à Decisão (SSD).
- Governança de dados: DAMA-DMBOK, Dados Mestres e de
  Referência, boas práticas de mapeamento de fontes.
- Ferramentas: Power BI (drillthrough entre páginas).

## Como a banca arma a pegadinha
- Star x Snowflake invertido: chama de "estrela" a dimensão
  normalizada em várias tabelas (é floco de neve), ou diz
  que Snowflake é o padrão recomendado por Kimball (é o
  Star). Star = desnormalizado, poucos joins, rápido para
  BI; Snowflake = normalizado, economiza espaço, mais joins.
- Absolutos: "ferramentas de BI são incompatíveis com
  tabelas normalizadas", "3FN maximiza performance de
  agregação no DW" — falso; 3FN é para OLTP.
- Confunde suporte com confiança nas regras de associação
  (suporte = frequência do conjunto; confiança = força da
  implicação A→B).
- Troca semiaditivo por aditivo (semiaditivo NÃO soma em
  todas as dimensões, tipicamente não no tempo: saldo,
  estoque).
- Data Lake x DW: diz que Lake substitui DW ou que guarda só
  dado estruturado; Lakehouse é o que combina os dois.

## Como se sair melhor
- Decore o par Kimball: Star = 1 fato + dimensões planas
  (desnormalizadas) = menos joins = mais rápido para BI.
  Snowflake = dimensões normalizadas = mais joins = mais
  lento, porém economiza espaço e ajuda integridade.
- OLAP dice = filtro em MÚLTIPLAS dimensões; slice = filtro
  em UMA; drill-down = mais detalhe; roll-up = agregar.
- Fato: aditivo (soma em tudo), semiaditivo (soma em algumas
  dimensões, não no tempo), não aditivo (razão/percentual).
- Dimensão degenerada = atributo de identificação (nº do
  pedido) que fica na tabela fato, sem dimensão própria.
- Camadas do Lakehouse: Bronze (bruto) → Silver (limpo) →
  Gold (dimensional para BI). ML consome bruto; BI consome
  Gold.
- Gatilho de erro: "sempre", "obrigatório", "incompatível",
  "3FN no DW" — desconfie.
