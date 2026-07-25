# banco-dados — como a FGV cobra

## O que mais cai
- SQL na prática: SELECT/WHERE, JOIN vs NOT EXISTS (registros
  sem correspondência), DISTINCT, LIMIT/OFFSET, VIEW como
  tabela virtual, DDL (DROP, CREATE com FK), GRANT de
  privilégios, SAVEPOINT/ROLLBACK TO.
- Relacional x multidimensional (OLTP x OLAP) — questão quase
  garantida, ver bloco BI também.
- NoSQL: quando usar, tipos (documento, grafo, chave-valor),
  MongoDB (query, $size, relation/table/collection x
  MySQL), banco orientado a grafos (nós e arestas).
- ETL x ELT (onde a transformação ocorre) — apareceu como
  "assinale a INCORRETA".
- Modelagem: álgebra relacional (seleção = WHERE, projeção =
  colunas), Crow's Foot → DDL, integridade referencial,
  constraints, chave surrogada. Do MER ao relacional: 1:N põe
  FK no lado N, N:M vira TABELA ASSOCIATIVA. Entidade fraca
  (chave do proprietário + chave parcial) x associativa.
- Transações: os quatro níveis de isolamento do padrão SQL e
  os fenômenos que cada um admite (leitura suja, não
  repetível, fantasma).
- Código no servidor: gatilho (o SGBD dispara por evento) x
  procedimento armazenado (a aplicação chama).
- Teorema CAP (CP sacrifica disponibilidade em partição),
  desnormalização intencional em DW.

## Como a banca arma a pegadinha
- Absolutos denunciam o distrator: "NoSQL segue ESTRITAMENTE
  ACID", "NoSQL usa SEMPRE modelo relacional", "dados SEMPRE
  em grafos", "desnormalização é requisito OBRIGATÓRIO".
  FGV adora "sempre/apenas/nunca/estritamente" — quase
  sempre é a errada.
- Inversão OLTP/OLAP: troca relacional↔multidimensional
  ("relacional é usada em OLAP, multidimensional em OLTP") —
  está invertido.
- ETL x ELT: inverte quem transforma antes/depois do
  carregamento, ou diz que ELT é melhor para volume pequeno.
- Confunde desnormalização (otimiza LEITURA analítica) com
  otimização de escrita, ou chama tabela plana de "floco de
  neve" (é estrela).
- CAP: distratores oferecem cenários que priorizam
  disponibilidade/velocidade (AP) para uma escolha CP.
- SQL: pega quem confunde WHERE (linhas) com projeção
  (colunas), ou NOT EXISTS/anti-join com JOIN comum.
- N:M: oferece "FK em uma das duas tabelas" (isso é 1:N) ou
  "coluna multivalorada nas duas" (viola a 1FN).
- Entidade fraca: a quase-certa diz que ela DISPENSA a chave
  do proprietário — é o oposto. Ou chama de forte porque tem
  atributos próprios (força = identificar-se sozinha).
- Isolamento: diz que READ UNCOMMITTED é o mais restritivo
  (é o mais permissivo) ou que REPEATABLE READ elimina o
  fantasma (elimina a não repetível). E o absoluto invertido
  "quanto mais isolamento, mais concorrência".
- Trigger x procedure: atribui ao procedimento o disparo
  automático pelo SGBD, ou ao gatilho a chamada por CALL.

## Como se sair melhor
- Memorize lado a lado: OLTP = transacional, normalizado,
  escrita, linha; OLAP = analítico, dimensional, leitura,
  cubo/agregação. ETL = transforma ANTES (DW tradicional);
  ELT = carrega e transforma no destino (nuvem, grande
  volume).
- Desnormalização = menos joins, mais espaço, risco de
  anomalia de atualização — objetivo é leitura, não escrita.
- CAP: em partição, ou C ou A. Cenário de registro
  oficial/consistência crítica (sentença, transação) = CP.
- NoSQL: BASE, alta disponibilidade e escalabilidade
  horizontal; ruim para ERP/CRM fortemente relacional.
- Álgebra: seleção (σ) = WHERE = linhas; projeção (π) =
  colunas. Chave surrogada = chave artificial no DW.
- Isolamento, marque pelo OBJETO: linha que muda de valor =
  não repetível; linha NOVA que aparece na mesma faixa =
  fantasma; dado ainda não confirmado = leitura suja. Só o
  SERIALIZABLE barra os três.
- Trigger x procedure, o gatilho do enunciado é "SEM depender
  de a aplicação lembrar" → trigger. Se o texto diz que
  alguém CHAMA a rotina, é procedimento armazenado.
- Leia palavra por palavra os comandos SQL; a FGV troca uma
  cláusula só (LIMIT/OFFSET, DISTINCT, ILIKE) e testa
  leitura de código.
