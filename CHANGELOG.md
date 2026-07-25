# Histórico de atualizações

Melhorias no material de estudo (Dataprev 2026, Perfil 3).

## 2026-07-25 — o que era citado mas nunca ensinado (auditoria, Bloco VII/ITEM 7 · P3)

Conceitos que apareciam na lista "o que já caiu" — ou seja, **anunciados como
cobrados** — sem nunca terem sido explicados no corpo do texto. Todos foram
**ensinados**, nenhum removido da lista.

- **Raft** (Cap. 5 e resumo): existia só como "2PC × Raft". Entrou como o que
  é — algoritmo de **consenso**, que resolve problema *diferente* do 2PC: não
  pergunta "todos aceitam efetivar?", e sim "em que **sequência de operações**
  este grupo de réplicas concorda?". Eleição de líder, decisão por **maioria**,
  tolerância a falha (sobrevive à queda do líder). Com o par explícito: o 2PC
  exige **unanimidade** e **bloqueia** se o coordenador cai; o Raft decide por
  **maioria** e continua de pé.
- **X.800** (Cap. 8 e resumo): citado em três camadas, definido em nenhuma.
  Entrou a arquitetura de segurança OSI com os cinco serviços e, sobretudo, o
  corte que a banca cobra — mecanismos **específicos** (cifração, assinatura,
  controle de acesso, integridade, troca de autenticação, preenchimento de
  tráfego, controle de roteamento, notarização) × **disseminados**
  (funcionalidade confiável, rótulos, detecção de eventos, trilha de auditoria,
  recuperação).
- **HMAC em *webhook*** (resumo de segurança): o resumo não tinha **nenhuma**
  menção a HMAC, embora a apostila e a dica tivessem. Entrou com o cenário
  inteiro e as duas armadilhas: HMAC **não** dá confidencialidade nem **não
  repúdio** (chave simétrica — as duas pontas geram o mesmo código).
- ***Taint* × *toleration*** (Cap. 5 e resumo): estavam numa lista de tópicos,
  sem explicação. O par funciona ao contrário do que o nome sugere — o **taint**
  é do **nó** e afasta pods; a **toleration** é do **pod** e o torna *elegível*.
  E tolerar **não é atrair**: quem atrai é *node affinity*.
- **VIEW, GRANT, SAVEPOINT/ROLLBACK TO, Crow's Foot e chave surrogada** (Cap. 6
  e resumo): cinco itens anunciados na lista do bloco de maior peso e nunca
  desenvolvidos. Entraram duas subseções — uma de VIEW (virtual × *materialized*),
  GRANT (é **DCL**, com `WITH GRANT OPTION`) e `ROLLBACK TO` (desfaz parcial, a
  transação **continua aberta**); outra com a tabela de símbolos do **Crow's
  Foot** e sua tradução para DDL (pé de galinha = lado N = FK; círculo = `NULL`;
  traço = `NOT NULL`) e a **chave surrogada** × chave natural.
- **Cloud bursting** já havia sido resolvido no ITEM 6/P1 — verificado, sem ação.
- **As duas listas "já caiu" foram sincronizadas.** A da apostila era mais rica
  em banco de dados e segurança; a do resumo, mais rica em eng. de software e
  arquitetura — **este segundo descompasso foi introduzido pelo próprio P1**,
  que acrescentou os tópicos novos só no `resumo/`. Agora as duas dizem o mesmo.
- **O Cap. 4 ganhou lista "já caiu", que não existia em camada nenhuma.**
  Montada a partir das **33 questões reais** filtráveis por subtag (23
  `padroes-projeto` + 10 `uml`), listando o cenário de cada uma — não uma
  estimativa. Era o único capítulo marcado ALTA PROBABILIDADE sem esse bloco.
- PDF recompilado: **97 → 100 páginas**, zero *overfull*.

## 2026-07-25 — seis imprecisões, duas delas factuais (auditoria, Bloco VII/ITEM 7 · P4)

- **"Cache fica no cliente" estava errado, e o P1 tinha acabado de piorar o
  problema.** A restrição *cacheable* do REST admite cache em
  **intermediários** (proxy, gateway, CDN) — e o Cap. 5 agora tem uma questão
  de CDN, então a formulação antiga treinava o reflexo contrário ao que o
  próprio material passou a ensinar. Reescrito nas três camadas, separando as
  duas coisas que estavam fundidas: o que não pode ficar no servidor é o
  **estado da sessão**, não o cache. O `resumo/`, que omitia a frase, passou a
  trazê-la — as camadas estavam divergentes.
- **O edital do Cap. 6 estava atribuído ao perfil errado.** Lido o
  `edital/edital-dataprev.pdf`: a lista de banco de dados (modelagem,
  normalização, SQL ANSI, administração de dados, backup) e os **SGBD
  nomeados** — Oracle 19C, MySQL, PostgreSQL, MongoDB, MS-SQL Server 2019 —
  são o item 7 do **PERFIL 2** (pág. 27). O **Perfil 3** (pág. 29) **não tem
  disciplina de Banco de Dados**: o assunto entra por Inteligência de Negócios
  (*data warehouse* com ETL e OLAP, *data mining*) e pelo item 20 de
  Desenvolvimento de Sistemas ("Análise de Dados e Big Data"). As caixas de
  edital da apostila e do resumo diziam "Edital (Perfil 3)" sobre conteúdo do
  Perfil 2. Reescritas com o recorte verdadeiro — e o peso do bloco passou a
  ser justificado pelo que ele é: **ALTO por evidência de prova** (a FGV cobrou
  BD no Perfil 3 da Dataprev 2024, como cobrou redes), não por peso de edital.
- **DDD: afirmação sem lastro removida.** A apostila dizia que o DDD "casou com
  microsserviços no TJ-RJ e no MPU". Busca em `banco-provas.json`: DDD caiu
  mesmo nas duas provas — **MPU Q71** (gabarito: o *Aggregate* garante a
  consistência das mudanças) e **TJ-RJ 2 Q36** (gabarito: eventos de domínio
  são imutáveis) —, mas **nenhuma das duas questões menciona microsserviços**.
  Trocado pelo que é verificável, com o gabarito de cada uma. O `resumo/`, que
  citava só o TJ-RJ, foi completado.
- **`dicas/uml.md`: "losango de gateway × decisão" era erro de notação.**
  Gateway é **BPMN**; em UML o losango é nó de decisão/merge do diagrama de
  atividade. Virou contraste explícito entre as duas notações, com remissão à
  dica de BPMN — de erro passou a conteúdo útil.
- **SOLID ficou consultável onde é usado.** O Cap. 4 manda "ligue ao SOLID" e a
  dica manda ligar padrões a SOLID/GRASP, mas os cinco princípios só eram
  definidos no Cap. 10 (Java). Entrou uma caixa compacta no Cap. 4 e no
  `resumo/padroes-projeto.md`, com remissão ao tratamento completo — sem
  duplicar o detalhe de Java. (SOLID é item 16 do **Perfil 2**; a remissão diz
  isso.)
- **As duas menores dicas do repositório reforçadas.** `dicas/padroes-projeto.md`
  **26 → 92 linhas** (o gatilho de enunciado dos 23 padrões um a um, a contagem
  5/7/11 com o Interpreter, os quatro pares que decidem a questão, a ligação com
  SOLID e com o Spring) e `dicas/uml.md` **25 → 54** (as duas famílias com o
  atalho de classificação, realização × dependência, componentes × implantação,
  a seta da generalização e o losango UML × BPMN). Eram as menores do repo para
  um capítulo marcado ALTA PROBABILIDADE com 33 questões via subtag.
- PDF recompilado: **97 páginas**, zero *overfull*, referências cruzadas novas
  (`sec:nuvem`, `cap:java`) resolvidas.

## 2026-07-25 — material para as 15 questões órfãs (auditoria, Bloco VII/ITEM 7 · P1)

O achado de maior impacto da varredura do Grupo A: **15 questões do banco cujo
assunto não existia no capítulo do próprio bloco**. Ao errar, o quiz manda ler
o capítulo — e o capítulo não cobria o tema. Escrito o conteúdo nas **três
camadas** (apostila, resumo e dicas), sem criar nenhuma questão nova e sem
tocar no `banco.json`.

- **Engenharia de Software (Cap. 3), 6 tópicos.** Seção nova **"Maturidade de
  processo: CMMI e MPS.BR"** (os cinco níveis por estágios, com o 3 = Definido
  e a medição quantitativa só no 4; as duas representações, por estágios ×
  contínua; e os sete níveis do MPS.BR **de G até A**, contra o distrator que
  faz a escala começar no A). **Modelo V** pareando fase e nível de teste
  (requisitos ↔ aceitação, arquitetural ↔ integração). Seção nova
  **"Manutenção de software"** com os quatro tipos da ISO/IEC 14764 e o
  critério que resolve a questão: a **causa** da alteração — troca de versão do
  SGBD é **adaptativa**, não corretiva. **Cobertura de caixa-branca**
  (comandos × decisões × caminhos, e a regra de que 100% de decisões implica
  100% de comandos, nunca o contrário, com o caso do `if` sem `else`).
  **Testes de desempenho** (carga × estresse × volume, mais fumaça na tabela de
  níveis). E os **três compromissos do Scrum Guide 2020** pareados com os três
  artefatos — os nomes já apareciam soltos em "alta probabilidade", sem nunca
  serem chamados de compromissos nem ligados aos artefatos, que é exatamente o
  que a questão cobra.
- **Banco de Dados (Cap. 6), 3 tópicos.** Subseção **"Do MER para o
  relacional"** (1:1, 1:N com FK no lado N, **N:M por tabela associativa**) e
  **entidade fraca × entidade associativa** (chave do proprietário + chave
  parcial). Seção nova **"Concorrência: níveis de isolamento"**, logo depois do
  ACID — o "I" estava lá sem desdobramento: os três fenômenos e a tabela dos
  quatro níveis do padrão SQL, com o trade-off isolamento × concorrência.
  Subseção **gatilho × procedimento armazenado** (quem dispara: o SGBD por
  evento × a aplicação por chamada).
- **Arquitetura (Cap. 5), 4 tópicos.** **ESB** finalmente explicado — "barramento
  de mensagens" estava na lista de estilos desde sempre, a sigla nunca. Subseção
  **layers × tiers** (três camadas lógicas cabem num nó físico só, e a aplicação
  segue monolítica). **Serverless/FaaS** (escala de zero, cobrança por consumo,
  sem estado, *cold start*, limite de tempo por execução — cada distrator da
  questão nega uma dessas). E **balanceador × CDN** como gargalos diferentes que
  se somam.
- **Segurança (Cap. 8), 1 tópico.** Seção nova **"Continuidade de negócio: RTO ×
  RPO"**. O par existia **só** em `orfaos`, mas a questão é etiquetada
  `seguranca` — quem errava era mandado para o capítulo errado. Entrou com
  MTBF/MTTR/SLA (as siglas vizinhas que a banca oferece junto) e um ponteiro
  cruzado em `resumo/orfaos.md`, para as duas camadas não divergirem depois.
- PDF recompilado: **88 → 97 páginas**, sem nenhum *overfull*. `./valida.py`
  segue nos dois avisos pré-existentes, e o detector de drift ficou silencioso —
  toda seção nova da apostila entrou com eco no `resumo/` correspondente.

## 2026-07-25 — Interpreter e OWASP 2025 (auditoria, Bloco VII/ITEM 7 · P0)

- **Faltava o Interpreter.** A apostila e o resumo afirmavam "comportamentais
  (11)" — e diziam que o número é cobrado direto —, mas as tabelas listavam
  **10**. O 11º padrão não existia em nenhuma camada nem no banco (`grep` sem um
  único hit). Entrou nas duas tabelas com intenção e gatilho no mesmo formato
  das outras linhas, mais a observação de que é justamente o que some da lista
  de quem conta de cabeça. Criacionais (5) e estruturais (7) já estavam certos.
- **OWASP: a edição vigente passou a ser a 2025.** O repositório se contradizia
  — o guia de questões e o `valida.py` tratavam a 2021 como "a numeração
  vigente", enquanto a apostila e o resumo já ensinavam as duas. Verificado em
  owasp.org: a **2025 é a versão corrente** (8ª da série), o SSRF foi absorvido
  pelo A01 e a lista das dez confere com o que estava escrito. Duas correções
  de fato:
  - **a data estava errada**: nov/2025 foi o *release candidate*; a versão final
    saiu em **jan/2026** (data de fonte secundária, não do owasp.org);
  - **as posições 6–9 do 2025 estavam em branco** e faltavam as **três
    renomeações** — A07 perdeu o "Identification and", A08 trocou "and" por
    "or", A09 trocou *Monitoring* por *Alerting*. É pegadinha pronta: oferecer o
    nome de 2021 num item que diz 2025.
- **Camadas alinhadas:** tabela lado a lado 2025 × 2021 completa nas dez
  posições (apostila e resumo), `dicas/seguranca.md` deixou de falar só em 2021,
  e `resumo/README.md` + `README.md` perderam a data errada. PDF recompilado
  (87 → **88 páginas**).
- **`valida.py`:** fato canônico novo, "OWASP Top 10 2025", declarado em
  `apostila`/`resumo`/`dicas`. O **banco fica de fora de propósito** — suas
  questões de OWASP nomeiam a edição de 2021 no enunciado, que é o comportamento
  correto agora que duas numerações válidas convivem.
- **`CONTRIBUINDO-QUESTOES.md`:** questão nova de OWASP tem de **dizer o ano**
  quando cobra posição ou nome de categoria (#272 e #274 fazem certo; a #37 pode
  ficar sem ano porque pede o conceito, que é categoria nas duas edições).

## 2026-07-25 — IA aplicada, ESG e Python para dados nas camadas (auditoria, Bloco VII/ITEM 6)

- **Buraco que o detector de drift do ITEM 5 não pegava.** A checagem 1 varre só
  `\section{}` da apostila; conteúdo que mora em `\subsection` fica invisível a
  ela. Foi assim que estes quatro descompassos passaram — todos encontrados na
  leitura manual, não pela ferramenta.
- **`resumo/atualidades.md` (92 → 157 linhas).** Duas seções novas:
  - **"IA aplicada — os cenários que a FGV monta"**: o edital pede *fundamentos
    e aplicações*, e o material só tinha fundamento. Tabela dos quatro cenários
    (triagem/priorização → classificação supervisionada; detecção de fraude →
    não supervisionado + concept drift; chatbot com LLM → alucinação e validação
    humana; score algorítmico → viés que reproduz desigualdade histórica),
    ancorada no **art. 20 da LGPD** (revisão de decisão automatizada), mais as
    quatro pegadinhas do formato — decisão sem revisão humana vendida como boa
    prática, "neutro porque não usa raça/gênero" (ignora as variáveis **proxy**),
    explicabilidade trocada por acurácia, e LLM como fonte infalível;
  - **"Interseção IA × ESG"**: fatia de TI × resfriamento no consumo do data
    center, **PUE** (energia total ÷ energia da TI, quanto mais perto de 1,0
    melhor), dependência de matriz fóssil e a discussão de divulgação obrigatória
    do impacto ambiental, com três pegadinhas — o número inflado em relação ao
    texto-base e os dois absolutos simétricos ("usa majoritariamente energia
    limpa" × "IA é incompatível com sustentabilidade").
- **`dicas/atualidades.md` (64 → 124 linhas).** O mesmo conteúdo destilado nas
  quatro seções que a dica já tinha, e um **aviso de calibração**: IA é o único
  conteúdo do repositório sem lastro em prova passada da FGV — a banca nunca
  cobrou IA na Dataprev antes de 2026. O que se diz sobre o *formato* dos itens
  de IA é **projeção, não histórico observado**; a aposta é item introdutório
  (definição, tipos de aprendizado, viés, alucinação), porque pegadinha
  sofisticada a banca só monta depois de anos calibrando o tema.
- **`resumo/programacao.md` (116 → 156 linhas).** Seção 7, **"Python aplicado a
  dados"** — o bloco não é só Java, e o resumo não tinha nada de Python: NumPy
  `view` × `copy` em tabela (buffer compartilhado × independente, `.base`
  apontando para o original × `None`), shape 1-D `(3,)`, `max(dic)` (compara
  chaves) × `max(dic, key=dic.get)` (compara valores, devolve a chave),
  fatiamento com fim exclusivo, compreensão × expressão geradora e o `explode`
  do matplotlib. **PHP 8** ficou com rótulo próprio, fora do Python.
- **`dicas/programacao.md` (54 → 66 linhas).** `max` com e sem `key=` e
  fatiamento, com as duas armadilhas correspondentes: a alternativa com a chave
  certa e o valor errado, e a que inclui o índice final do fatiamento.
- Nada removido: as duas deleções do diff são reflow de linhas de "o que já
  caiu" que ganharam itens. `./valida.py` silencioso (só os dois avisos
  pré-existentes: `mpu Q41` e as 9 questões de forma herdadas).

## 2026-07-25 — detector de drift entre as camadas (auditoria, Bloco VII/ITEM 5)

- **`valida.py` passa a avisar quando as camadas saem de sincronia** (apostila →
  resumo → dicas → banco). A repetição entre elas é intencional; o que não pode é
  uma camada avançar e a outra ficar para trás. Três checagens, nenhuma bloqueia:
  1. **seção nova na apostila sem eco no `resumo/` do bloco** — varre os
     `\section` dos 18 capítulos contra o resumo correspondente (o Cap. 4 aponta
     para `padroes-projeto` e `uml`);
  2. **fato canônico que sumiu de uma camada** — tabela declarativa
     `FATOS_CANONICOS` com 18 entradas (data do STF 26/06/2025, OWASP 2021, ISO
     27002:2022, COBIT 2019, ITIL 4, números das leis, RFC 1918, Java 17/21…).
     A camada esperada é **declarada por fato**, não universal: o corte de 57,5
     não pertence às dicas, a data da prova não pertence ao banco;
  3. **contagem de questões declarada no README × banco real.**
- **Três descompassos encontrados e corrigidos:**
  - `resumo/redes.md` não tinha a seção **"Tipos de rede corporativa"** que existe
    na apostila — entrou o quadro Internet × intranet × extranet × portal, com a
    inversão dos três papéis, que é o distrator clássico;
  - **os 23 padrões do GoF** (5 criacionais, 7 estruturais, 11 comportamentais)
    não apareciam em nenhuma camada de estudo — o Cap. 4 listava as três famílias
    sem nunca dizer o número, que a FGV cobra direto. Acrescentado na apostila e
    no `resumo/padroes-projeto.md`; PDF recompilado (87 páginas);
  - `README.md` e `resumo/README.md` ainda diziam **"237 questões originais /
    ~616 utilizáveis"** — hoje são 336 e ~715. É exatamente o tipo de defasagem
    que a checagem 3 passa a pegar sozinha.
- Custo: +0,2 s no `./valida.py`. Detector **silencioso** depois das correções.

## 2026-07-25 — subtags, limiares de forma e acentuação (auditoria, Bloco VII/2-4)

- **Subtags (`sub`) — o Cap. 4 deixa de ser cego ao filtro do quiz.** Padrões de
  projeto e UML tinham `dicas/`, `resumo/` e capítulo próprio, mas nenhuma questão
  filtrável: `./quiz.py padroes-projeto` não devolvia nada. Agora `./quiz.py uml`,
  `padroes-projeto`, `java-moderno`, `git-devops` e `leitura-codigo` funcionam.
  **58 questões marcadas; nenhuma trocou de `tag`** — a subtag é um campo novo e
  opcional, porque a `tag` alimenta o roteiro, o `progresso.csv`, o peso do
  simulado, o `erros/<tag>.md`, o `--stats` e o `historico.json`.
- **`banco.json`: 331 → 336.** Cinco questões de Java moderno (threads virtuais e
  suas duas armadilhas — *pinning* em `synchronized` e pool fixo —, `record`,
  `sealed`/`permits`, `var`/text block/`switch` com seta), para a subtag
  `java-moderno` nascer com 8 questões em vez de 3.
- **`dicas/` e `resumo/` novos** para `java-moderno`, `git-devops` e
  `leitura-codigo` (os outros dois já existiam), fechando o `--dica`/`--resumo`
  dessas subtags.
- **Limiares de forma do `valida.py` por escopo.** O limiar global único era cego
  a regressão: com o banco em 3%, um lote de 60 questões 100% enviesadas levava o
  global a 18% — silencioso. Agora são três escopos: global (0,25/0,08/0,30), por
  bloco com n≥12 (0,35/0,25/0,45) e janela das 30 últimas (0,30/0,20/0,45), mais
  a flag `--novas N`. O ponto de detecção caiu de "nunca" para **12 questões**.
  `--strict` passou a incluir os avisos de forma no código de saída (portão
  pré-commit); sem ele, nada bloqueia o quiz.
- **Índices do `valida.py` agora são 1-based**, alinhados a como as questões são
  referidas no resto do repositório. As referências herdadas do Bloco VI estavam
  deslocadas em −1.
- **Acentuação normalizada nas questões #228–#237** (governança: PMBOK, ITIL 4,
  COBIT 2019, BPMN, Scrum/Kanban), que tinham sido escritas sem acento nenhum.
  Passe mecânico com trava dupla: `strip_accents(novo)` tem de devolver o texto
  anterior campo a campo, e o comprimento de cada alternativa não pode mudar — o
  que garante que nenhum vazamento de forma foi reintroduzido.

## 2026-07-25 — questões para os buracos de cobertura (auditoria, Bloco VII/ITEM 1)

- **banco.json: 259 → 331 questões.** Cinco lotes gerados a partir do relatório de
  cobertura, priorizados pelo peso do Apêndice A e por evidência de que a FGV
  cobra o tema (termo ausente do banco original × presente em prova real).
- **LOTE 1 (22):** arquitetura 7, segurança 8, banco de dados 7. Fecha buracos que
  estavam em ZERO no banco: SOAP/WSDL (cai na Dataprev 2024 Q45), IaaS/PaaS/SaaS,
  serverless, balanceador × CDN, layers × tiers, ISO 27001 × 27002 e a estrutura
  da 27002:2022, RBAC/ABAC/MAC/DAC, OIDC/SAML/JWT, OWASP A01 e A10, RTO × RPO,
  níveis de isolamento, trigger × procedure, entidade fraca, especialização
  total/sobreposta, NOT IN com NULL e particionamento × sharding × replicação.
- **LOTE 2 (14):** eng-software. Seis GoF que só existiam como distrator (Facade,
  Template Method, Command, Chain of Responsibility, classificação dos 23, State ×
  Strategy), UML (componentes × implantação; realização × dependência), CMMI e
  MPS.BR, modelo V, tipos de manutenção, cobertura de comandos × decisões, teste
  de estresse × carga e os três compromissos do Scrum Guide.
- **LOTE 3 (13):** os dois blocos gerais com menor oferta por ponto de prova. RLM
  ganhou geometria plana e estatística descritiva (média/mediana/moda, desvio
  padrão) — o Apêndice A registra que 2024 cobrou os dois e o banco tinha zero — e
  juros simples × compostos. Inglês ganhou dois textos originais, com quatro itens
  cada (ideia central, referência pronominal, conectivo e vocabulário em contexto).
- **LOTE 4 (12):** Git além do clone (merge × rebase, área de stage, fetch × pull),
  Python aplicado a dados (dicionário com `key=`, fatiamento e compreensão),
  entrega × implantação contínua, Docker × Kubernetes, e BI (granularidade da fato,
  medida semiaditiva, SCD tipo 2, fases do CRISP-DM, clusterização × associação).
- **LOTE 5 (11):** **Língua Portuguesa saiu de zero questões originais.** Era o
  maior descompasso do banco: 12 questões de prova (mesmo peso do Inglês) servidas
  só pelas provas reais. Entraram um texto original com quatro itens de
  interpretação e sete de norma-padrão (crase, concordância verbal, regência,
  pontuação, porquês, conjunção concessiva e colocação pronominal).
- **Calibração:** mediana do enunciado subiu de 19 para 41 palavras (provas reais:
  59), com cenário aplicado no lugar de definição pura.
- **Vazamentos de forma preservados em zero:** nas 72 questões novas, a correta é a
  mais longa em 4 (6%) e não há uma única com termo absoluto só no distrator.
  Gabarito do banco ficou uniforme (A–E com 66/67 cada).
- `./valida.py`: 0 erros; nenhum aviso novo de forma.

## 2026-07-25 — fim dos vazamentos de forma no banco (auditoria, Bloco VI/A)

- **A correta deixou de ser a mais longa.** Era o vazamento mais grave do banco:
  dava para acertar pela mecânica da alternativa, sem saber o conteúdo. Passou de
  **160/259 (62%) para 6/259 (2%)** — e os 6 restantes são falsos-positivos
  estruturais (itens do tipo "nomeie o termo", em que a correta é maior só porque
  a *palavra* é maior, e itens I/II/III, em que o "apenas" é sintaxe do formato).
- **Termo absoluto só no distrator: 81/259 (31%) → 1.** Onde a explicação da
  errada *ensina* o absoluto como pista ("note o 'exclusivamente'"), o distrator
  foi preservado e a correta ganhou um absoluto **legítimo** — verdadeiro pelo
  conteúdo, não pela forma (ex.: "o IPS atua **sempre** em linha", "a seta da
  generalização **sempre** aponta para a superclasse"). Assim "elimine a que tem
  absoluto" para de funcionar sem estragar o comentário do gabarito.
- **Correta ≥1,8× a média das erradas:** 86 questões → 1.
- **Como foi feito:** nivelando por baixo, não só encurtando a correta. Os
  distratores já estavam ancorados em erro conceitual real — só curtos demais;
  cada distrator-âncora foi enriquecido até a frase completa do conceito errado
  que já representava. Efeito colateral: distratores mais fortes.
- **Itens de sigla nivelados** (ESB, SIEM, MVC, JAD, ANPD): a correta vinha com
  sigla + significado por extenso e as erradas com a sigla nua — outro tell.
  Agora todas as alternativas trazem o nome completo.
- **166 questões tiveram alternativas reescritas. Nenhum gabarito, enunciado ou
  tag foi alterado** (conferido por diff contra o commit anterior); dois campos
  `erradas` (#78, #141) foram ajustados porque citavam literalmente o texto que
  mudou. Todo conteúdo aparado da alternativa correta continua no `why`.
- `./valida.py` sem os dois avisos sistêmicos de forma.

## 2026-07-24 (noite) — auditoria do banco: gabarito, estilo e ferramentas

- **Gabarito reembaralhado (Bloco I):** a posição da correta estava concentrada
  (era B ≈ 71%); agora A–E ≈ 20% cada. Três `why` posicionais reescritos.
- **`valida.py` — checagens de forma (`avisos_forma`):** avisa (sem bloquear)
  quando o banco de questões geradas vaza a forma — correta sempre a mais longa,
  termo absoluto só no distrator, gabarito concentrado numa posição.
- **`cobertura.py` (novo):** cruza os subtópicos da apostila (`\section`/
  `\subsection`) com o texto dos dois bancos e aponta buracos de cobertura.
- **Auditoria de estilo e explicações (Bloco V):** as 259 questões originais
  foram lidas contra fonte — **zero gabaritos errados**, explicações fortes.
  Medida a divergência de estilo vs. as provas reais da FGV (enunciado ~⅓ do
  tamanho; definição direta demais nos lotes antigos; comando negativo
  sub-representado). Quatro questões reforçadas: **#57** (Marco Civil — enunciado
  agora explicita "redação original do art. 19", desambiguando do regime
  pós-STF), **#33** (tríade CID), **#162** (3 Vs do Big Data) e **#205** (ESG)
  tiveram distratores de enchimento trocados por "quase-certas" ancoradas em
  erro conceitual real.
- **`valida.py` — campo opcional `status`:** marcação de auditoria por questão
  (`ok`/`revisar`/`ambigua`/`distrator-fraco`/`explicacao-fraca`/
  `estilo-divergente`), validada sem bloquear.
- **`CONTRIBUINDO-QUESTOES.md` (novo):** guia obrigatório para toda questão nova
  — ancoragem em fonte primária, distrator ancorado em erro real, proibição dos
  vazamentos de forma, trava anti-vício e proporção de cenário calibrada.
- **`.gitignore`:** passa a ignorar os artefatos de build do LaTeX
  (`.aux`/`.log`/`.toc` etc.).

## 2026-07-24 (tarde) — calibração do roteiro e da apostila (auditoria, Bloco IV)

- **Roteiro calibrado aos pesos (Semana 10):** Governança 5→4 dias, Arquitetura
  2→3. Arquitetura era o único bloco ranqueado "alto" no Apêndice A com
  alocação mínima (empatada com Redes, que está fora do edital). BPMN +
  métricas (PF/Story Points) foram fundidos num dia; a sexta virou revisita de
  Arquitetura. Prazo intacto: plano de 13 semanas, em dia (11 restantes).
  Redes mantida no mínimo (não zerada); Java preservado por gargalo pessoal.
- **Cap. 18 (IA) — aviso de incerteza de FORMATO:** caixa no início do capítulo
  deixando claro que é o único sem calibração em provas anteriores da FGV (IA
  entrou no edital só em 2026). Enquadrado como incerteza de formato, não de
  valor: recomenda dominar fundamentos em vez de antecipar o desenho da questão.
- **Cap. 4 (Arquitetura) — bloco final vira síntese:** o "Como se sair melhor"
  repetia quase literalmente as caixas de escalabilidade/REST/SOAP; reescrito
  como síntese operacional curta que preserva o único conteúdo novo (gatilhos
  de distrator) e remete às caixas vermelhas. O bloco análogo de Banco de Dados
  foi avaliado e **mantido** (funciona como flashcard de fixação dos 4 pares).
- **Cap. 2 (Técnica FGV):** título da caixa corrigido de "seis" para "sete"
  padrões de distrator — a enumeração já listava os sete (o 7º, contradição
  interna, já estava lá); só o rótulo estava defasado.
- PDF recompilado (87 páginas).

## 2026-07-24 — quiz ligado à apostila + estatística de erro por causa

- **`--apostila <bloco>` (novo):** aponta o capítulo da apostila
  (`apostila/main.pdf`) do bloco, no molde de `--dica`/`--resumo` (aceita
  `--apostila hoje`; sem argumento, lista os capítulos). Mapa `tag→capítulo`
  (número impresso = arquivo + 1). `padroes-projeto`/`uml` caem no Cap. 4,
  separado de `arquitetura` (Cap. 5).
- **Referência da apostila no caderno de erros:** ao errar, a entrada
  automática em `erros/<bloco>.md` passa a trazer `Apostila Cap. N`. Novo campo
  **opcional** `apostila` na questão (ex. `"§10.5"`) refina para `Cap. N §X`;
  sem ele, degrada para `Cap. N — Título`.
- **Estatística de erro por causa:** ao errar, o quiz captura em uma tecla se o
  erro foi **conceitual** (não sabia) ou de **leitura/armadilha** (sabia e caiu)
  — gravado como campo opcional `causa` no `historico.json` (a causa é da
  tentativa, não da questão). O `--stats` mostra as duas colunas por bloco.
- **Trava anti-vício no `--stats`:** erro majoritariamente conceitual num bloco
  manda **reler a Apostila Cap. N + mais questões** e NÃO menciona técnica de
  eliminação; só o erro de leitura aponta os sete padrões de distrator (Cap. 2).
- **`valida.py`:** valida `apostila` como campo opcional e faz checagem leve dos
  `historico*.json` (avisa, sem bloquear, `causa` com valor inválido). Dados
  antigos sem os campos novos continuam válidos.

## 2026-07-22 — apostila definitiva em PDF + 22 questões novas (IA, leitura ativa, Marco Civil)

- **`apostila/` (novo):** apostila definitiva em LaTeX, compilada em
  `apostila/main.pdf` (87 páginas) — 21 capítulos cobrindo os dois módulos da
  prova, montados a partir do roteiro, dos resumos, das dicas de banca e do
  banco de questões. Cada capítulo tem ficha do edital, peso esperado, e
  caixas de conceito/pegadinha/como-se-sair-melhor/o-que-já-caiu. Apêndices:
  mapa de pesos e glossário de ~70 pares que a FGV inverte.
- **Reforço de conteúdo na apostila:** IA aplicada a negócios/políticas
  públicas e interseção IA×ESG (Cap. 18); seções de "Leitura Ativa de
  Código" em Programação, Java e Frontend (Caps. 9–11); atualização crítica
  do Marco Civil art. 19 pós-STF (jun/2025) com tabela antes/depois e caixa
  dedicada de distratores (Cap. 19).
- **`banco.json`: +22 questões originais** (237 → 259) nos mesmos três
  temas: IA aplicada/viés algorítmico/ESG (`atualidades`), leitura ativa de
  código em CSS/JS/React/Java (`frontend`, `java`), e a mudança do art. 19
  do Marco Civil (`legislacao`). Todas validadas com `./valida.py`.
- **`CLAUDE.md`:** nova seção "Estilo de questão ao gerar para banco.json",
  destilando o padrão de questão mais próximo da FGV (formato do enunciado,
  como variar a abertura de cada `erradas` sem virar molde repetitivo).

## 2026-07-16 — auditoria das novas, reforço de blocos e resumo de órfãos

- **Auditoria independente das 72 questões originais novas** (as 52 + 20 de
  reforço): cada uma resolvida do zero contra fonte. **Zero gabaritos errados.**
- **Reforço dos blocos mais magros:** +10 Java e +10 Governança (originais,
  validadas). Java 19→29, Governança 18→28.
- **`resumo/orfaos.md`** (novo): administração de BD (DBA) — ARIES/WAL,
  tablespaces, backup incremental×diferencial, otimizador — que o resumo de
  banco-dados (focado em modelagem/SQL) não detalhava, + temas coringa.
- **Dicas de padrões-projeto e UML** (antes só tinham resumo).
- Contagens atualizadas: **237 originais + 7 provas reais = ~616 utilizáveis.**

## 2026-07-15 (tarde) — +3 provas reais e questões novas nos temas fracos

- **3 provas ALERO 2026 (FGV)** importadas com gabarito oficial e explicações
  validadas: `cnsal-ads` (Análise e Desenvolvimento de Sistemas), `cnsal-bd`
  (Banco de Dados), `cnsal-redes` (Infraestrutura de Redes). **+120 questões
  reais utilizáveis.** Módulo comum (Q1-40) mantido uma vez; trivia estadual
  de Rondônia descartada.
- **Análise de gaps** e geração de **52 questões originais** (estilo FGV,
  gabarito validado) para os temas fracos/zerados: Padrões de Projeto (GoF),
  UML, frontend, atualidades/IA e inglês.
- Banco agora: **217 originais + ~380 de prova = ~596 questões utilizáveis.**
- `valida.py` sem erros.

## 2026-07-15 — provas, dicas, resumos e ferramentas de estudo

Grande atualização. Em ordem do que foi feito:

### Provas reais viraram banco de questões

- **`importar_provas.py`**: extrai as questões dos PDFs em `provas/`
  (Dataprev 2024, MPU 2025, TJ-RJ 2026 ×2) para `banco-provas.json`.
- **`gabarito.py`**: preenche o gabarito **oficial** da FGV. Questão sem
  gabarito **não** entra no sorteio (gabarito chutado treina reflexo errado).
  Os 4 gabaritos definitivos foram carregados (todos tipo 1 – branca).
- **259 questões reais utilizáveis**, cada uma com explicação de *cada*
  alternativa errada, validada contra fonte. 5 anuladas e 25 que dependem de
  figura ficam fora do sorteio.
- Jogue: `./quiz.py --prova dataprev2024` ou `--prova todas`.

### Auditoria das 165 questões originais

- Cada questão original foi resolvida do zero contra fonte primária.
  Nenhum gabarito estava errado; **3 explicações foram corrigidas** (OWASP
  2021, Marco Civil pós-STF de jun/2025, referência de perfil).

### Explicações e caderno de erros automático

- Ao errar, o quiz explica **por que cada alternativa errada está errada**
  (offline, sem custo — as explicações vêm gravadas no banco).
- O erro é gravado **automaticamente** em `erros/<bloco>.md`, com dedup por
  questão. Desliga com `--sem-anotar`.

### Dicas de banca — `--dica <bloco>`

- 16 guias em `dicas/`: o que a FGV mais cobra em cada assunto, como arma a
  pegadinha e como se sair melhor. Ancorados nas provas reais.

### Resumo de conteúdo — `--resumo <bloco>`

- 15 arquivos em `resumo/` (um por bloco) + visão geral, cobrindo o edital do
  Perfil 3, integrando dicas + questões resolvidas + pesquisa em fonte.
- Alertas: **redes** cai fora do edital do Perfil 3; **OWASP 2025** mudou o
  ranking; **IA** entrou nas gerais; estrutura oficial da prova (Módulo I 40 ×
  peso 1 + Módulo II 30 × peso 2,5 = 115 pontos).

### Integração com o roteiro

- **`--hoje`** cobre os **dois blocos do dia** (específico + geral) e mostra os
  atalhos de dica/resumo de cada um. Dias especiais: **revisão** dispara a
  repetição espaçada, **simulado** dispara o modo cronometrado, descanso/prova
  avisam.
- **`--dia ontem`** (ou `anteontem`, `-3`, `AAAA-MM-DD`): faz o plano de um dia
  atrasado e credita **naquele** dia (conserta a aderência).
- **`--pendentes`**: lista os dias de roteiro em aberto.
- O painel **`status.py`** mostra o plano do dia com os comandos prontos.

### Repetição espaçada — `--erradas`

- Agora é repetição espaçada de verdade (estilo Leitner): a questão sai do pool
  quando você acerta 2× seguidas desde o último erro; se errar de novo, volta.
  Não revisa mais o que já foi fixado.

### Simulado cronometrado — `--simulado`

- 70 questões no formato da prova (gerais peso 1 + específicos peso 2,5, na
  proporção do edital), específicos primeiro, **sem feedback até o fim**,
  cronometrado. No fim: nota ponderada, projeção para os 115 pontos, corte de
  eliminação e desempenho por bloco. `-n` escala o tamanho.

### Estudo em dupla e escalabilidade

- **`--quem <nome>`**: progresso separado por pessoa (roteiro compartilhado).
  O README tem um guia de instalação no Windows para a Geys.
- **`valida.py`**: confere a integridade dos dois bancos ao adicionar questões.
- Guia no README de como adicionar mais provas e mais questões geradas.

## 2026-07-13 — setup inicial

- Roteiro de 13 semanas, painel (`status.py`), caderno de erros (`erros/`),
  quiz de terminal (`quiz.py`) com 165 questões originais estilo FGV.
