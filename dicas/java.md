# java — como a FGV cobra

## O que mais cai
Aviso de amostra: Java apareceu concentrado na prova TJ-RJ
(Analista de Sistemas) e em 1 questão do MPU; na Dataprev 2024
o tema Spring caiu como "programação". Trate o que segue como
os pontos que a FGV efetivamente cobrou, com boa chance de se
repetir no perfil Dev.

- Recursos modernos da linguagem: classes sealed / non-sealed
  / final (quem pode herdar de quem). Threads virtuais x
  threads de plataforma (muitas virtuais montadas sobre poucas
  de plataforma).
- Ecossistema Spring/persistência: leitura de REST controller
  (@RestController, @GetMapping, @PathVariable) e comportamento
  de Map/HashMap (getOrDefault); JPA 2.0 e o problema N+1
  (FetchType + JOIN FETCH); Spring Cloud Eureka (atributo
  lease-expiration); Hibernate Envers (auditoria via Revision
  Listener).
- No edital e provável, mesmo sem ter caído na amostra:
  checked x unchecked exceptions, overload x override,
  Collections (List/Set/Map, ArrayList x LinkedList), interface
  x classe abstrata, generics, equals/hashCode.

## Como a banca arma a pegadinha
- sealed: uma classe sealed exige subclasses declaradas
  (permits ou no mesmo arquivo), e cada subtipo deve ser final,
  sealed ou non-sealed. O distrator diz que final "não pode
  estender sealed" (pode) ou inventa erro de escopo; o erro
  real costuma ser uma sealed sem nenhuma subclasse permitida.
- Threads virtuais: distrator diz que cada virtual = uma de
  plataforma (consumo linear) ou que o nº de plataforma limita
  o de virtuais. O certo: milhares de virtuais compartilham
  uma carrier thread de plataforma.
- JPA N+1: oferece EAGER em tudo ou "deixar o JPA decidir"
  como solução — a resposta é LAZY + JOIN FETCH na consulta.
- Código Spring: getOrDefault com chave inexistente retorna o
  DEFAULT (ex.: 0), não 404/500 nem exceção. A FGV testa se
  você sabe que o Map devolve o default, não erro.
- Nomes de atributo/config (Eureka lease-expiration, Envers
  Revision Listener): distratores trocam por nomes plausíveis
  (heartbeat-interval, interceptor, filtro).

## Como se sair melhor
- sealed = "herança fechada e explícita": permits obrigatório
  (ou tipos no mesmo arquivo); subtipo tem de ser final |
  sealed | non-sealed. non-sealed reabre a hierarquia.
- Virtual thread = leve, muitas por carrier; platform thread =
  1:1 com thread do SO. Virtuais brilham em I/O-bound.
- Par para decorar: checked (Exception, verificada em
  compilação, trata ou declara throws) x unchecked
  (RuntimeException, não obriga tratamento); overload (mesmo
  nome, assinatura diferente, compile-time) x override (mesma
  assinatura na subclasse, runtime, @Override).
- N+1: LAZY para não carregar cedo + JOIN FETCH quando precisar
  da relação numa consulta só.
- Em leitura de código, execute mentalmente linha a linha e
  confie na semântica da API (getOrDefault → default). Gatilhos
  de distrator: "sempre", "independentemente da carga",
  "equivale a uma de plataforma".
