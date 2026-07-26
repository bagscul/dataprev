# Histórico de atualizações

Melhorias no material de estudo (Dataprev 2026, Perfil 3).

## 2026-07-26 — auditoria do repositório inteiro: dois defeitos de importação e o piloto da apostila que ENSINA

Primeira rodada de uma auditoria do repo inteiro, com o plano aprovado item a
item. Três frentes: destravar questão real que estava fora do sorteio por
engano, consertar um casamento de string que sujava um bloco, e começar a
transformar a apostila de mapa de prova em livro-texto. `banco-provas.json`:
**432 → 422** questões (o recorte encolheu de propósito); utilizáveis no quiz:
**735 → 768**. Apostila: **122 → 150 páginas**.

### 45 questões reais estavam trancadas por engano

O `requer_imagem` tirava 51 questões do sorteio. Auditando uma a uma contra o
contexto do casamento, **só 6 dependem mesmo de figura**. A regra antiga era
uma lista de termos (`figura|codigo|esquema|diagrama|comando SQL`) casada em
qualquer lugar do enunciado — então ela pegava:

- **"Código" jurídico:** Código Florestal (`mpu` Q20), Código Penal (`tjrj`
  Q70), Código de Ética (`mpu` Q32, `tjrj` Q30). 7 questões.
- **"imagem" figurada:** "prejudiciais à sua imagem" (`tjrj` Q63), "exportar
  como imagem JPEG" dentro de uma fala (`tjrj2` Q38). 3 questões.
- **"esquema" como termo técnico:** "esquema de relação $R(A,B,C,D,E)$"
  escrito por extenso ali mesmo (`cnsal-bd` Q41/Q46), esquema
  Estrela/Snowflake como conceito (Q51/Q63). 5 questões.
- **Resposta que está nas ALTERNATIVAS:** "assinale o comando SQL que…"
  (`cnsal-ads` Q67, `cnsal-bd` Q42/Q43/Q73). 4 questões.
- **Código que o `pypdf` extraiu direitinho e está no enunciado:** `mpu` Q51
  (numpy), Q59 (`CREATE ROLE`), Q75 (HTML+CSS), Q76 (`sealed`), Q43
  (`SELECT`), `tjrj2` Q55 (`@RestController`). 6 questões perfeitamente
  respondíveis.

A regra nova exige três coisas. **Dêixis** junto do termo ("observe o diagrama
abaixo") — sem ela, "código"/"esquema"/"diagrama" é só vocabulário técnico.
**Ausência do artefato no próprio enunciado** — se o `SELECT` veio junto, a
questão se sustenta. E **alternativa vazia** como sinal estrutural, o único
caso que dispensa a lista de termos: é o da `mpu` Q41, cujas alternativas são
símbolos BPMN que viraram imagem.

Ficam fora do sorteio 6: `mpu` 41/52/63/64/67 e `dataprev2024` 49. Nesta
última conferi direto no PDF — o código Java da questão de Liskov **não está
na camada de texto**, é imagem mesmo, não há o que recuperar.

### A chave `"bi"` casava DENTRO de outra palavra

O `tag_de()` resolvia o rótulo do mapa por substring pura. Resultado:
`"Noções de Sustentabilidade"` (sustenta**bi**lidade) e `"Noções de Direitos
Humanos e Fundamentais e de Acessibilidade"` (acessi**bi**lidade) mandavam as
questões **16–25 do MPU** para Business Intelligence. Dez questões de direito
ambiental e direitos humanos entravam em `./quiz.py bi` — e, como `bi` não
está em `GERAIS`, **valiam 2,5× no `--simulado`**, inflando a projeção de
nota. O BI real do corpus era 15 questões, não 25.

A busca agora é por palavra inteira. E as dez saem também do recorte:
Sustentabilidade e Direitos Humanos não estão no edital do Perfil 3 — é ruído
de outro perfil, mesmo critério já aplicado à História e Geografia de Rondônia
da ALERO.

### As 41 questões destravadas ganharam explicação

Efeito colateral do item anterior, resolvido no mesmo lote: as questões que
estavam fora do sorteio nunca tinham passado pela auditoria, então entraram sem
`why` nem `erradas`. O quiz as corrigia e não comentava — o oposto do método,
já que a `erradas` é justamente o que se lê ao errar. As 41 ganharam explicação
ancorada no gabarito oficial (`banco-dados` 11, `legislacao` 7, `programacao`
6, `eng-software` 5, `seguranca` 5, `bi` 2, `orfaos` 2, `java` 2, `frontend`
1). Com isso o `valida.py --strict` volta à lista de avisos do baseline: 1
aviso (a `mpu` Q41 documentada) + 1 de forma (a #41 preservada de propósito).

Duas anotações que valem por si:

- **`cnsal-bd` Q41 (chave candidata + forma normal).** O gabarito C acerta a
  forma normal — 3FN e não BCNF —, mas a alternativa lista **só duas das três
  chaves candidatas**: falta BC, e o fecho confirma ($BC \to DE$, e $D \to A$
  fecha o resto). Isso não é preciosismo: é justamente BC que torna B primo;
  pelas duas chaves que a alternativa cita, $A \to B$ seria dependência parcial
  e a relação nem chegaria à 2FN. A explicação registra a inconsistência em vez
  de fingir que a alternativa fecha.
- **`cnsal-redes` Q43 (Decorators do Python).** A explicação diz na cara que o
  `@` do Python não é o Decorator do GoF — a armadilha de garimpo já catalogada
  no repositório, agora ensinada no ponto exato em que ela aparece.

### Legislação — o último capítulo da frente, e duas conferências que mudaram o plano

**146 → 150 páginas. Legislação: 1:12,35 → 1:0,66.** Era a pior razão restante
do livro, e a recomendação registrada era fazer só as bases legais e os agentes
da LGPD, porque ali o "conceito" é o texto da lei. Duas conferências mudaram o
recorte antes de escrever uma linha.

**Primeira: o corpus real de legislação não são 47 questões, são 8.** Das 47 com
a tag em `banco-provas.json`, **39 são de outro perfil** — organização do TJ-RJ,
estatuto do MPU, Estatuto da Pessoa com Deficiência, licitação, servidor
público, direito constitucional. Nada disso está no edital do Perfil 3. O que
sobra são as cinco da Dataprev 2024 (LAI, art. 154-A, sanções do Marco Civil,
sanções da LGPD, ANPD × CNPD) e três do TJ-RJ (princípio da adequação, art. 20 /
explicabilidade, IA generativa × LGPD). E o cruzamento é revelador: **o que já
estava bem ensinado é exatamente o que a banca já cobrou** (LAI e adequação são
as melhores partes do capítulo). O buraco estava em **sanções** — duas das cinco
questões da Dataprev — e nos agentes/ANPD.

**Segunda: o recorte de capítulos do edital não é o que se supunha.** O edital
pede LGPD caps. I, II, III, IV, VII, VIII e IX. Isso **exclui o Capítulo VI**
("Dos agentes de tratamento", arts. 37–45), onde moram o encarregado do art. 41
e a responsabilidade civil solidária do art. 42 — ou seja, dos "agentes de
tratamento" da recomendação antiga só entram as **definições do art. 5º**
(Capítulo I). E **inclui o Capítulo VII** ("Da segurança e das boas práticas",
arts. 46–51), que **não existia em camada nenhuma do repositório** e é
justamente a parte da lei que um desenvolvedor implementa. Mesma conferência no
Marco Civil: o recorte é cap. II Seção I e cap. III Seções I e II, o que inclui
o **art. 12** (sanções) e deixa o art. 19 **fora** — o capítulo já gasta uma
página e meia com ele, e não recebeu uma palavra a mais.

Sete inserções, todas dentro de seções existentes (nenhum `\section` novo, logo
nenhum risco de *drift*):

- **Agentes de tratamento.** O papel vem do **poder de decisão**, não do acesso:
  a empresa que hospeda o banco e emprega os programadores pode ter menos
  obrigações que o órgão que nunca abriu o sistema. E a trava do **art. 5º, IX** —
  agentes de tratamento são **o controlador e o operador**, só os dois; o
  **encarregado não é agente de tratamento**, é o telefone, não o responsável.
  O exemplo mostra o papel mudando: a operadora que decide sozinha reaproveitar
  a base vira **controladora daquele tratamento**.
- **Bases legais: o art. 7º e o art. 11 são listas diferentes.** O mecanismo não
  é decorar dez itens, é saber que dado sensível tem lista **própria e menor** —
  e que **legítimo interesse e proteção do crédito não estão nela**. Guardar o
  CPF por contrato é art. 7º; guardar a digital para liberar a catraca é art. 11,
  II, "g".
- **Decisão automatizada (art. 20)** — desfaz uma inversão de camada: o `resumo/`
  tinha seção e a apostila tinha uma linha. Inclui a trava da redação antiga: o
  texto de 2018 dizia revisão "**por pessoa natural**", a **Lei 13.853/2019**
  retirou a expressão e o §3º que a reporia foi **vetado**. Hoje a lei **não
  exige** revisor humano — e material desatualizado ensina o contrário.
- **Capítulo VII, a LGPD que o desenvolvedor implementa** (ausente do repo
  inteiro): *privacy by design* com texto de lei (art. 46, §2º — segurança
  **desde a concepção do produto até a execução**), sigilo que **sobrevive ao
  término** do tratamento (art. 47), comunicação de incidente **à ANPD e ao
  titular** quando houver **risco ou dano relevante** (art. 48) e programa de
  governança em privacidade (art. 50).
- **Sanções da LGPD (art. 52) como regime, não como tabela de multa.** Rito com
  ampla defesa, de forma gradativa, isolada ou cumulativa; os **onze parâmetros**
  de dosimetria (nacionalidade não é um deles — foi distrator); **órgão público
  não leva multa** (§3º); a multa vai para o **Fundo de Defesa de Direitos
  Difusos** (§5º), **não** para o titular lesado; vazamento individual admite
  **conciliação direta** (§7º, que foi o gabarito).
- **ANPD × CNPD.** Os dois colegiados que a banca troca: **Conselho Diretor** =
  órgão máximo de direção **da própria ANPD** (5 diretores, mandato de 4 anos) ×
  **CNPD** = conselho **consultivo** com 23 representantes que **integra a
  estrutura da ANPD** (art. 55-C, II) — daí o distrator invertido "a ANPD é uma
  das integrantes do CNPD".
- **Marco Civil, art. 12** — o `jacaiu` já creditava isso à Dataprev 2024 e o
  corpo nunca ensinou. As quatro sanções, isoladas ou cumulativas, e o par
  numérico que a banca troca: **MCI até 10%** do faturamento do grupo econômico
  no Brasil **no último exercício, sem teto nominal**, contra **LGPD até 2% com
  teto de R$ 50 milhões por infração**. O distrator da prova trocava a janela
  ("média dos últimos três exercícios").

**Atualização legislativa que o repositório não tinha.** A **Lei nº 15.352, de
25/02/2026** (conversão da MP 1.317/2025) deu nova redação ao art. 55-A: a sigla
continua ANPD, mas o nome passou a **Agência** Nacional de Proteção de Dados —
autarquia de natureza especial **vinculada ao Ministério da Justiça e Segurança
Pública**, com autonomia funcional, técnica, decisória, administrativa e
financeira, **nos termos da Lei 13.848/2019**, a lei das agências reguladoras. O
material descrevia o desenho da Lei 14.460/2022. A trajetória inteira entrou no
capítulo, porque é dela que saem os distratores: *órgão* ligado à Presidência
(2018–2019, natureza declaradamente transitória) → *autarquia de natureza
especial* (2022) → *agência* vinculada ao Ministério da Justiça (2026).

Tudo ancorado no texto consolidado do Planalto, artigo por artigo. Uma anotação
para quem for conferir: **a página da LGPD no Planalto cita "Lei 15.452" na
redação do art. 55-A, e é erro de digitação deles** — a Lei 15.452/2026 acrescenta
um artigo ao Código de Trânsito. A correta é a **15.352/2026**.

**A atualização foi propagada para as outras camadas** num lote curto logo em
seguida: `resumo/legislacao.md` e `dicas/legislacao.md` ganharam o novo desenho
da ANPD e a distinção Conselho Diretor × CNPD, e a `erradas` da alternativa (A)
da Dataprev 2024 Q40 — que parava na Lei 14.460/2022 — passou a citar também a
15.352/2026. Editar `why`/`erradas` no `banco-provas.json` **é seguro**: ao
contrário da `tag`, esses campos são carregados do arquivo anterior pelo
`importar_provas.py` (linhas 389–390), e a reimportação foi conferida —
continua devolvendo o arquivo **byte-idêntico**.

Contrato aditivo cumprido: `conceito` **1 → 9** no capítulo (62 → 70 no livro);
`pegadinha` 7, `jacaiu` 1 e `comosair` 1 **inalteradas**, `PISO_CAIXAS` intocado
em 116/20/24. `./valida.py --strict` com a **lista de avisos idêntica** ao
baseline e sem linha `[drift]`. Os 13 *overfull hbox* do livro continuam 13, com
o mesmo máximo de 17,3pt.

### Apostila fase 3, lote 3 — frontend, e a fase fecha

**145 → 146 páginas.** Era o capítulo de menor déficit do livro (1:1,88), já
tinha boa prosa e duas caixas de conceito de leitura de código, então foi
cirúrgico: três inserções, todas no que ele **citava e não ensinava**.
**Frontend: 1:1,88 → 1:0,69.**

**HTML semântico como decisão, não decoração** — o capítulo listava as tags e
parava ali. Quem lê o *papel* do bloco são programas (leitor de tela, buscador,
comportamento de teclado nativo), e é daí que vem a regra número um do ARIA, que
o capítulo já ensinava adiante sem essa âncora. **CSR × SSR × SSG e a
*hydration*** estavam no "alta probabilidade" e não eram ensinados em lugar
nenhum, apesar de serem a consequência direta da SPA — que o próprio capítulo
chama de "coração deste bloco": entraram pelo *onde e quando* o HTML é gerado,
com o preço de cada estratégia, a *hydration* como costura entre SSR e SPA
(incluindo a janela em que a página **parece pronta e não responde ao clique**)
e o aviso de que SSR/CSR e PWA são **eixos independentes**, que é onde vive o
distrator do item real de SPA × PWA. E **UX × usabilidade × acessibilidade**, que
eram um *bullet* de uma linha cada, com as duas relações que resolvem o item: UX
**contém** usabilidade (e a UI é só a camada visual), e acessibilidade **não é
caso particular** de usabilidade — as duas se cruzam, não se contêm. Mais a
diferença de natureza: usabilidade é objetivo de qualidade; acessibilidade é
requisito normativo (WCAG como critério técnico, eMAG como modelo do governo
brasileiro derivado dele, LBI como obrigação em serviço público).

**Fecho da fase 3.** O Módulo II inteiro está agora em ≈1:1 ou melhor:
eng-software 1:0,80, padrões+UML 1:1,04, arquitetura 1:1,12, banco de dados
1:0,72, BI 1:0,82, segurança 1:1,35, programação 1:0,80, Java 1:0,76, frontend
1:0,69, governança 1:0,79. Redes ficou em 1:2,46 **de propósito** (passe curto:
fora do edital do Perfil 3, 1 questão na Dataprev 2024) e órfãos não foi tocado
por decisão de escopo --- é conteúdo fora do perfil por definição, e a própria
caixa do capítulo manda não gastar tempo nele. Caixas ao fim das três fases:
`conceito` **27 → 62**; `pegadinha` 113 → 116 (as três a mais são de seções
novas: gestão de riscos, RUP e estruturas de dados); `jacaiu` e `comosair`
**nos mesmos 20 e 24 do início** --- o contrato aditivo cumprido em 13
capítulos. O livro foi de 87 a 146 páginas, dentro do alvo de ~155 e longe do
teto de 175.

Sobra uma decisão: **`18-legislacao`** (1:14,26, a pior razão restante). O número
é tentador, mas ali o "conceito" é o texto da lei, e apostila não substitui lei
--- provavelmente só as bases legais e os agentes da LGPD. *(Resolvida logo
adiante, e o recorte saiu maior do que essa previsão — ver a seção de
legislação acima.)*

### Apostila fase 3, lote 2 — Java, governança e o passe curto de redes

**140 → 145 páginas.**

**Java (1:3,54 → 1:0,76).** O capítulo cobria bem os pares que a FGV inverte e
não ensinava os fundamentos que sustentam esses pares — os quatro pilares de OO
eram **uma linha** num capítulo cujo edital pede análise e projeto orientados a
objetos. Entraram os pilares pelo que cada um esconde (com as duas confusões que
a banca explora: encapsulamento não é gerar *getter*/*setter* para tudo, e o
polimorfismo cobrado é o de sobrescrita, resolvido em *runtime*); o **exemplo
trabalhado da violação de Liskov** (Quadrado × Retângulo), com o critério
prático — não exigir mais, não entregar menos, não quebrar invariante — e a nota
de que o compilador já barra três violações na sobrescrita e **não** barra a
quebra semântica, que é justamente onde a banca cobra; o **contrato
`equals`/`hashCode`**, ou seja, por que o objeto "desaparece" do `HashSet`
quando se sobrescreve um e se esquece o outro (com a quase-certa de que
`TreeSet`/`TreeMap` não usam `hashCode`, e sim `compareTo`); a **JVM em duas
ideias** — *bytecode*, de onde realmente vem o *write once, run anywhere*, e a
divisão *stack* × *heap*, que amarra a passagem por valor e a pilha da seção
nova de estruturas de dados —, mais o GC pelo critério de **alcançabilidade**; e
o **stream como pipeline preguiçoso**, com os três fatos que a banca vira
alternativa (sem operação terminal nada executa, a fonte não muda, o stream é de
uso único). Era um *bullet* de meia linha.

**Governança (1:5,31 → 1:0,79).** **Governança × gestão** entrou como a linha
que organiza o capítulo — a pergunta de cada lado, os verbos, quem responde e o
teste prático, incluindo o ponto em que a banca planta a dúvida: *monitorar*
está nos dois lados, com objetos diferentes. **Incidente × problema ×
requisição × mudança** era chamado pela própria pegadinha de a troca nº 1 do
tema e não estava ensinado no corpo: entrou com a âncora de que incidente se
mede em tempo de restauração (contorno serve, e **fecha** o incidente com o
problema ainda aberto). Mais **por que a 6ª virou 7ª no PMBOK** (processo →
princípio, com *tailoring*), os **três gateways do BPMN com as duas semânticas**
— divisão e junção, e é a junção, que quase ninguém estuda, que a FGV cobra — e
o significado de "serviço" e "cocriação de valor" na ITIL 4, que é o que explica
a troca de *processo* por *prática*.

**Redes — passe curto, deliberado (1:583 → 1:2,46).** Não se persegue 1:1 aqui:
redes está fora do edital do Perfil 3 e valeu 1 questão na Dataprev 2024.
Entrou **uma** caixa, no ponto que a prova real cobra duas vezes (TJ-RJ e ALERO
2026): **encapsulamento** — cada camada resolve um problema e acrescenta o
próprio cabeçalho, o nome do PDU denuncia a camada (segmento, pacote, quadro) e
o critério de decisão é por **função**, que é como a FGV pergunta. Mais o
mapeamento OSI 7 × TCP/IP 4.

Caixas: `conceito` **52 → 60**. `pegadinha`, `jacaiu` e `comosair` intactas
(116/20/24) — nenhuma caixa de banca nova neste lote, então o piso do
`valida.py` não muda.

### Apostila fase 3, lote 1 — programação, padrões+UML e BI

Ordem por **impacto na nota** (peso da Dataprev 2024 × déficit de conceito), não
por facilidade. **132 → 140 páginas.**

**Programação (1:2,46 → 1:0,80).** Peso 6 na Dataprev 2024, o segundo maior
específico. O achado do capítulo é grande: a caixa "já caiu" credita **13 das
23 questões reais do bloco** a estruturas de dados (ALERO 2026), e o corpo do
capítulo não ensinava nenhuma delas — nem a apostila, nem
`resumo/programacao.md`. Entrou uma **seção nova**, tratada como o que a banca
de fato cobra: **contrato de custo**, porque o enunciado dá o requisito
("inserção e remoção frequentes no meio", "busca por chave em tempo
constante"), nunca o nome da estrutura. Vetor × lista encadeada como troca
recíproca (e o $O(1)$ da lista pressupondo o ponteiro em mãos); hash × árvore
balanceada com a regra de que **não competem pela mesma vaga** — faixa e
listagem ordenada são árvore, mesmo com o $O(1)$ do hash na tela; busca binária
só sobre coleção ordenada. Mais o **exemplo trabalhado de por que o hash
degrada**: fator de carga, as duas famílias de colisão (encadeamento separado
deixa o $\alpha$ passar de 1; endereçamento aberto é o que o limita a 1) e o
laço de realimentação da sondagem linear que produz o **agrupamento primário**
— resposta literal de uma questão real.

Também entraram **IoC e injeção de dependência** pelo nó que elas desfazem (com
o detalhe que separa quem entendeu: o escopo *singleton* do Spring não é o
Singleton do GoF) e os **quatro fatos da linguagem** que decidem qualquer item
de leitura de código — compilada × interpretada × *bytecode* com o Java no
meio, passagem por valor reduzida à pergunta certa ("esta linha reatribui ou
muta?"), imutabilidade e por que só tupla serve de chave de dicionário, e *duck
typing*.

**Padrões + UML (1:5,21 → 1:1,04).** O capítulo era um catálogo de tabelas.
Entrou **o que os 23 padrões têm em comum** — isolar o que varia atrás de uma
interface estável, preferindo composição a herança — e o **critério das três
famílias** pelo que cada uma isola. O **exemplo trabalhado do `if` gigante ao
Strategy** nomeia o que se ganhou (Open/Closed, Dependency Inversion) e fecha
com o contraste Strategy × State pela pergunta de **quem decide a troca**.
GRASP era nove nomes sem uma linha de explicação: ganhou Information Expert e
Creator. E, do lado da UML, os **quatro diagramas de interação** (sequência,
comunicação, tempo, visão geral) — que o capítulo não distinguia e que são
exatamente os distratores da questão real de sequência — mais a **sintaxe fina
do diagrama de classes**: valor *default* de atributo, extremidade de
associação representável como atributo e associação qualificada, os três itens
de leitura de diagrama do MPU.

**BI (1:3,53 → 1:0,82).** Começa pela pergunta que fundou o assunto — *por que
não rodar o relatório direto no banco do sistema?* — e pelas três respostas que
aparecem uma a uma nos cenários: concorrência, história e integração. A
**arquitetura de BI ponta a ponta** o edital pede com esse nome e o capítulo não
tinha: fontes → extração → *staging* → transformação → DW → OLAP →
visualização, com OLAP e visualização marcados como **consumo**, não
transformação. O ETL ganhou **o que pertence a cada fase**, com a regra prática
de que tarefa que *decide* algo sobre o conteúdo é Transform (a ALERO cobrou
isso literalmente). **Inmon × Kimball** estava no "alta probabilidade" e nunca
tinha sido ensinado: entrou por quem se constrói primeiro e pelo risco
espelhado de cada um (o projeto que não chega ao usuário × o silo por falta de
dimensão conformada). Fecha com o **esquema estrela de vendas montado na frente
do leitor** — a ordem das quatro decisões, o que a tabela fato contém (só chave
estrangeira e medida numérica, mais a dimensão degenerada) e a contagem de
*joins* estrela × floco de neve.

Caixas: `conceito` **43 → 52**. `jacaiu` e `comosair` intactas (20/24). A
`pegadinha` a mais (115 → 116) é da seção nova de estruturas de dados, e o piso
do `valida.py` subiu junto.

### Apostila fase 2 — arquitetura, segurança e eng-software

Calibrada depois do piloto: banco de dados sozinho cresceu 5 páginas, e
replicar aquela densidade nos 11 capítulos restantes levaria o livro a ~180.
Estes três somaram **5 páginas no total** — o piloto era o caso extremo (1:14);
estes estavam em 1:5,5 e 1:7,7, e o de engenharia de software já era o melhor
servido do livro.

**Arquitetura (1:5,5 → 1:1,18).** O capítulo já tinha boa prosa fora das
caixas, então foi cirúrgico: os estilos como **sequência histórica** (cada um
nasceu resolvendo a dor do anterior, e é a dor do enunciado que aponta o
estilo); **o preço dos microsserviços**, que é o que falta para responder aos
cenários em que eles são a resposta *errada*; **o que REST é de verdade**
(recurso, representação, interface uniforme) com o encadeamento que a FGV cobra
— sem estado → qualquer instância serve → escala horizontal; **IaaS/PaaS/SaaS
pela linha de responsabilidade**, incluindo a responsabilidade compartilhada em
segurança; e por que transação distribuída é difícil, amarrado ao CAP.

**Segurança (1:7,7 → 1:1,52).** A **tríade CIA como critério de classificação**
do capítulo inteiro, com o mapa controle → pilar e o ponto que separa quem
entendeu: os três competem entre si. **Assimétrica: a mesma matemática, dois
usos opostos** — a tabela das duas direções, a lógica de cada uma em uma frase,
e as duas notas que a banca cobra (assina-se o *hash*; o TLS usa assimétrica só
para combinar a chave simétrica de sessão). E **gestão de riscos** ganhou seção
própria: o edital pede "ameaça, vulnerabilidade, impacto" e o capítulo não
ensinava nenhum dos três.

**Eng-software (1:1,3 → 1:0,70).** Preenchimento cirúrgico, como planejado.
**CMMI**: o que é maturidade de processo, que problema ele resolveu, como se
reconhece cada nível na prática — com o corte 2 → 3 — e por que existem duas
representações. **APF**: o que o Ponto de Função mede e por que independe de
linguagem, os cinco tipos em dois grupos, e os dois critérios de classificação
(ALI × AIE pela manutenção; SE × CE pelo dado derivado). **RUP**: o capítulo o
citava no "já caiu" e no "nosso banco" e **não o ensinava em lugar nenhum** —
entraram os dois eixos, as quatro fases com seus marcos e a âncora de que risco
e arquitetura vivem na Elaboração.

Caixas no fim das duas fases: `conceito` **27 → 43**. `jacaiu` e `comosair`
intactas (20/24). As duas `pegadinha` a mais (113 → 115) são de conteúdo novo —
gestão de riscos e RUP, seções que não existiam. O piso do `valida.py` subiu
junto.

### A apostila começa a ensinar — capítulo-piloto de Banco de Dados

A apostila era um mapa de prova excelente e um livro-texto ruim: dizia o que
cai e como a banca inverte, mas não ensinava o conceito. A proporção
denunciava — **113 caixas de "como a FGV arma a pegadinha" contra 27 de "o que
é isso"**, quatro para um a favor do truque, com o ambiente que existe para
ensinar (`conceito`) sendo o menos usado do documento.

O buraco não era uniforme, e é isso que definiu o piloto. **Banco de dados
tinha 1 caixa de conceito, de 11 linhas, contra 11 pegadinhas e 153 linhas de
estratégia — razão 1:14** — sendo a outra metade do eixo duplo e o segundo
maior peso. Normalização inteira eram 18 linhas: uma tabela de quatro linhas e
um parágrafo. Se o formato funciona no pior caso, funciona em qualquer um.

Cada seção agora tem cinco tempos: **por que a coisa existe** e que problema
resolve; o **conceito com o mecanismo**, não a glosa de uma linha; **exemplo
concreto**; **ligação com o conceito vizinho**; e só então as caixas de banca.
O que entrou:

- **Dependência funcional** como a ferramenta que sustenta tudo — 2FN, 3FN e
  BCNF são a mesma frase ficando mais rigorosa.
- **Decomposição passo a passo**, com tabela desnormalizada de verdade, as
  três anomalias que ela causa e a quebra 1FN → 2FN → 3FN feita na frente do
  leitor. Mais o procedimento de achar chave candidata a partir de $F$, que é
  o formato em que a FGV cobra (`cnsal-bd` Q41/Q46).
- **Ordem lógica de execução do `SELECT`**, que explica de uma vez três
  pegadinhas diferentes (o `WHERE` não vê apelido, `WHERE` × `HAVING`, e o
  porquê de cada uma).
- **ACID na transferência bancária**, com as quatro letras num cenário só, o
  par Consistência × Isolamento e o falso amigo do "C" do CAP.
- **CAP pelo cenário do cabo cortado**: por que só existem duas saídas, por
  que "2 de 3" é simplificação e por que um monolito não é "CA".
- **O que um índice é** e por que tem tipos — B+ Tree, hash e bitmap saem da
  troca leitura/escrita e das duas perguntas que decidem.
- Ações referenciais, os três níveis de modelagem pelo critério do que já foi
  decidido, e por que OLTP e OLAP são separados.

Capítulo: 460 → 780 linhas. Razão conceito:estratégia de **1:13,9 para
1:0,81**. **Zero deleções** em `pegadinha`/`jacaiu`/`comosair` — o livro segue
com 113/20/24, e só `conceito` subiu (27 → 34).

**A trava que garante isso** entrou no `valida.py` (item D do drift): o piso
das três caixas é verificado a cada rodada. Se um total cair, sai aviso — a
frente de aprofundamento é aditiva por contrato, não por promessa.

### Atrito e dívida

- **`./feito.sh` jogava fora a sessão anterior.** Fazia `= q`, não `+= q`:
  20 questões de manhã e 30 à noite terminavam o dia com 30 registradas, sem
  aviso. Somar virou o padrão; `--set` substitui. De quebra, o `csv` escrevia
  CRLF num arquivo LF — marcar um dia reescrevia as 92 linhas do
  `progresso.csv`.
- **`apostila` e `status` saem do schema documentado**: 0 de 356 questões cada
  um. O `apostila` nunca fez falta porque o `ref_apostila()` já cai no mapa
  bloco→capítulo; o `status` era instrumento da auditoria, que acabou. O
  `valida.py` continua aceitando os dois.
- **`sub` vira regra** (58 de 356, o único com uso real): todo lote novo
  preenche quando couber. Sem passe retroativo.

## 2026-07-25 — lote de 20 questões nos recortes finos + os textos-base perdidos

Primeiro lote guiado por **questões por ponto de prova** em vez de volume, e o
primeiro em que questão de interpretação parte de **texto real** buscado na
web, não de texto autoral. `banco.json`: **336 → 356**. Apostila: **121 → 122**
páginas.

**A prioridade mudou por causa de um defeito, não da tabela.** Inglês já era o
bloco mais fino (2,5 questões por ponto), mas as **12 questões reais** do bloco
— todas da Dataprev 2024, a única prova do corpus com Língua Inglesa — tinham
sido importadas **sem os textos-base**. O `parsear()` só reconhece item
numerado, então os três TEXTs da prova não viravam questão: eles grudavam na
**última alternativa da questão anterior**. A alternativa (E) da Q12
(português) carregava **3.963 caracteres** de um anúncio de e-book em inglês, e
a (E) da Q18 trazia o texto do Gizmodo inteiro. Do outro lado, a Q14 (`"What
information is in TEXT?"`, 28 caracteres) e a Q21 eram **literalmente
irrespondíveis** — e o quiz as sorteava, porque tinham gabarito e não estavam
marcadas como dependentes de figura.

- **`importar_provas.py` — `textos_base()`.** O marcador (`"Use the following
  TEXT to answer the next six questions."`) diz quantas questões o texto cobre;
  o corpo vai dali até a primeira linha que seja só um número. O texto é
  **prefixado no enunciado de cada questão do grupo**, porque o quiz sorteia
  itens soltos e cada um precisa se sustentar sozinho — mesma decisão já tomada
  nas questões de inglês do `banco.json`. O `requer_imagem` continua sendo
  calculado sobre o enunciado, não sobre o texto.
- **`CABECALHO_SECAO`** — irmã da correção do rodapé. Título de seção sozinho na
  linha (`Língua Inglesa`, `Raciocínio Lógico Matemático`, `Atualidades`,
  `Legislação Específica`, `MÓDULO II`…) agora encerra a alternativa corrente.
  Casa a **linha inteira** de propósito: "Legislação", "Módulo" e "Realização"
  aparecem dentro de alternativas legítimas ("Bugs por Módulo.", "A realização
  de entrevistas…") e não podem cortar. Os títulos que o PDF quebra em duas ou
  três linhas entram pela primeira linha, que já basta.
- **23 questões corrigidas, nenhuma perdida.** 12 ganharam o texto-base
  (Dataprev 2024 Q13–Q24) e 11 tiveram um rabicho de cabeçalho retirado da
  alternativa (Dataprev Q12/Q18/Q24/Q30/Q35, MPU Q20/Q25/Q35/Q40, ALERO Q12/Q24,
  TJ-RJ Q20 nas duas provas). Reimportar continua devolvendo o arquivo
  **byte-idêntico**, e `tag`/`ans`/`why`/`erradas` não foram tocados.

**As 20 questões novas.** Critério de escolha: termo presente em prova real da
FGV e ausente do `banco.json`.

- **Inglês, 8** (dois textos reais, 4 eixos cada — ideia central, anáfora,
  conectivo, vocabulário em contexto). O perfil de fonte veio do que a FGV
  usou de fato na Dataprev 2024: página da **Amazon**, post do **Gizmodo** e
  abstract do **ACM** — jornalismo técnico, descrição de produto e resumo
  acadêmico, nunca literatura. Escolhidos: um abstract do **arXiv**
  (Becker *et al.*, `arXiv:2507.09089`, 12/07/2025 — o RCT em que a IA
  *atrasou* devs experientes em 19%, contra previsão de −24%) e um post do
  **Cisco Talos** (Johnson, 22/04/2026 — primeira vez que o Talos IR documenta
  uso de uma ferramenta de IA por adversário em campanha de *phishing*, contra
  administração pública). Fonte completa no `why` da primeira questão de cada
  texto. O erro do original ("since at May 2023") foi **preservado**.
- **Programação, 6 — estruturas de dados**, que tinham **zero** questões nossas
  contra ~13 reais: tabela hash (agrupamento primário sob fator de carga alto;
  encadeamento separado × endereçamento aberto), árvore balanceada para
  consulta por faixa, pilha × fila, pré-requisito de ordenação da busca
  binária, vetor × lista encadeada. A ALERO 2026 é a maior fonte do bloco (13
  das 23 reais) e **não estava creditada** na caixa `jacaiu` de programação —
  resquício do conserto de rótulo do commit `9e8a260`. Corrigido.
- **Eng-software, 6 — subtópico, não volume** (o bloco já tinha 53 originais;
  só parece fino porque vale 25 pontos). **APF** era o buraco gritante: 7 itens
  reais contra 1 nosso. Entraram ALI × AIE pelo critério da manutenção, EE/CE/SE
  pela intenção do processo, APF × LOC × story point; mais partição de
  equivalência × valor limite, estratégias de implantação (*blue-green* ×
  *canary* × *rolling* × *feature toggle*) e um item de **comando negativo**
  sobre fase × disciplina no RUP.

Métricas do lote (`./valida.py --novas 20`): correta-mais-longa **5%** (alvo
≤6%), absoluto-só-no-distrator **0**, razão máxima correta/erradas **1,13**
(limite 1,7), gabarito **4/4/4/4/4** — a distribuição do banco segue uniforme
(A–D 71, E 72). Redes ficou de fora por estar fora do edital do Perfil 3;
português, porque 79 das suas 90 questões já são reais, com texto íntegro.

## 2026-07-25 — fechamento do ITEM 7: as 11 caixas `jacaiu` do GRUPO A

Encerra a varredura dos 18 blocos. As **35 caixas "O que já caiu"** das duas
camadas (17 na apostila, 18 no `resumo/`) agora separam **o que caiu em prova
real da FGV**, com a sigla, do que é **previsão do edital no nosso banco** —
o rótulo `preambulo.tex:101` diz "O que já caiu nas provas", mas as caixas
eram preenchidas a partir do `banco.json`. Cada item foi conferido contra as
**432 questões reais** de `banco-provas.json`. Apostila: **119 → 121 páginas**.

O Grupo A concentra os específicos (26 eng-software, 34 arquitetura, 25
banco-dados, 38 segurança, mais ~30 questões de "órfãos" que são engenharia de
software, UML e modelagem disfarçadas). É o grupo **com mais lastro real** —
e, por isso mesmo, o de **maior subcrédito**.

- **Alegações falsas** (zero ocorrência nas 432 reais), retiradas do parágrafo
  de prova real: em eng-software, **Sprint Review × Retrospective** e os **três
  compromissos do Scrum** — "Definition of Done" só existe na *nossa* `erradas`
  da Dataprev Q69 —, mais modelo V, tipos de manutenção, cobertura de comandos
  × decisões e estresse × carga; em padrões de projeto, **22 dos 23 padrões**;
  em arquitetura, **ESB**, **API gateway** (só no nosso `why` da Dataprev Q41),
  **Raft**, layers × tiers como par, e serverless/FaaS e CDN, que só apareceram
  como nome de produto entre distratores; em banco de dados, os **níveis de
  isolamento** e seus fenômenos; em segurança, **SAST × DAST**.
- **Padrões de projeto é o achado mais duro:** de 18 alegações, **uma** tem
  lastro — o **Singleton** da ALERO 2026 (cache com instância única), cujo
  enunciado fala em "classificação GoF", o que salva a tabela das três
  famílias. A caixa ganhou o aviso dos **quatro falsos positivos** que uma
  busca por palavra-chave produz: o `Decorators (@)` do Python, o "Portas e
  Adaptadores" da arquitetura hexagonal, os "proxy" das questões de rede e o
  MVC, que só aparece *descrito* numa alternativa, nunca nomeado.
- **UML é o oposto:** a caixa creditava as 10 questões como nossas e omitia
  **quatro reais** — diagrama de **sequência** (com comunicação, timing e visão
  geral de interação como distratores), **composição**, **casos de uso +
  diagrama de objetos** (ALERO 2026, sempre com "UML 2.5.1" no enunciado) e
  leitura de **diagrama de classes** (MPU). Generalização/especialização caiu
  pelo lado do modelo ER.
- **Segurança tinha o maior buraco: 28 das 38 questões reais** ficavam de fora
  — RBAC, segregação de funções, ISO 27002/27001, gestão de risco e risco
  residual, a família de *malware* inteira, DDoS e SYN flood, spoofing,
  NGFW/WAF/proxy/VPN, simétrica × assinatura digital sobre ICP, as etapas de
  resposta a incidentes e os *claims* do OIDC (que o Grupo A já tinha
  ensinado).
- **Arquitetura ganhou uma seção nova:** **11 das 34** questões com essa tag
  são **arquitetura de computadores e SO** (Von Neumann, ULA, overflow ×
  carry, MMU/TLB, tabela de páginas, DMA), vindas de provas de outro perfil e
  **fora do edital do Perfil 3**. Ficam registradas com a orientação explícita
  de não gastar tempo nelas, em vez de sumirem da conta.
- **Carry-over do Grupo C corrigido:** a caixa de órfãos listava em "ainda não
  visto na amostra" dois pares que **caíram** na Dataprev 2024 sob outra tag —
  **servidor web × servidor de aplicação** (Q50) e
  **internet/intranet/extranet/portal** (Q44).

Também acertei duas contagens da auditoria: `banco-dados` tem **25** questões
reais (não 24) e `seguranca` tem **38** (o 43 era pré-retag, antes de os cinco
itens de LGPD/LAI virarem `legislacao`).

### Os três resíduos, fechados na sequência

- **Retag: 11 questões de arquitetura de _computadores_ saíram de
  `arquitetura`.** Deixá-las ali inflava o bloco em 32% e distorcia a leitura
  do que a FGV cobra de arquitetura de _software_: **34 → 23** questões reais.
  Foram para `orfaos` (**57 → 68** — de quebra, o "56" que a caixa declarava
  também estava errado). Trocada só a `tag`, por `(prova, num)`; o `id` do
  histórico é `prova:num`, então nada no progresso depende disso.
- **52 alternativas carregavam o rodapé do PDF.** Fui atrás do aviso do
  `mpu Q41` e o que apareceu foi um defeito sistemático da importação: o
  extrator emenda o rodapé da página seguinte na **última** alternativa. Junto
  vinham cabeçalhos de seção e, em três casos, o enunciado **inteiro** da prova
  discursiva — a alternativa E da `tjrj2 Q70` tinha 1322 caracteres, dos quais
  98 eram a alternativa. Importa além da sujeira: alternativa poluída fica
  muito mais longa que as irmãs, que é o mesmo vazamento de forma caçado no
  Bloco VI, agora do lado das provas reais — as que servem de padrão-ouro de
  estilo quando geramos questão nova.
- **O `mpu Q41` continua fora do sorteio, e está certo.** As cinco alternativas
  são símbolos BPMN; conferi no PDF e as linhas "(A)" a "(E)" são vazias lá
  também. Não há texto a restaurar — o que dava para limpar era o rodapé. O
  aviso do `valida.py` é a descrição correta de uma questão que depende de
  imagem, não um defeito.
- **Aviso de forma: 9 questões → 1.** As 8 questões cuja correta era ≥1,7× a
  média das erradas foram niveladas **por baixo** (enriquecer o distrator-âncora,
  nunca encurtar a correta): #73, #189, #81, #152, #110, #44, #55 e #49. A #41
  (drill-down) fica como está — é falso positivo preservado de propósito, do
  tipo "nomeie o termo", em que a correta é maior só porque a palavra é maior.

**Novo baseline do `./valida.py --strict`:** ainda sai **1**, agora com dois
avisos, ambos intencionais — o `mpu Q41` (questão de imagem) e a #41 (falso
positivo preservado).

### O importador: cinco defeitos, e o corpus reclassificado

Limpar os dados não bastava — o `importar_provas.py` reintroduzia tudo na
próxima importação, e pior, **desfazia retag**. Consertados: (1) o filtro de
rodapé era *case-sensitive*, e `FGV CONHECIMENTO` nunca casava com
`FGV Conhecimento`; (2) a alternativa atravessava a virada de página e engolia
cabeçalho de seção, o nome da organizadora e o enunciado da prova discursiva —
agora corta na quebra, o que revelou mais 6 resíduos, incluindo **1191
caracteres do texto de leitura seguinte** colados na alternativa E da
`dataprev2024 Q20`; (3) o número da questão agora tem de ser o **próximo da
sequência**, senão um "2" solto numa questão de RLM abria questão fantasma;
(4) a `tag` se resolvia pela **ordem do dicionário**, então
`"Legislação (Segurança da Informação...)"` caía em `seguranca`; (5) reimportar
**ressuscitava as 97 questões descartadas de propósito** (432 → 529), agora
travado por padrão, com `--tudo` para o caderno inteiro.

**A regra que fica: a `tag` de prova real vem de `notas/<prova>-mapa.md`, nunca
do JSON.** Editar o JSON direto é desfeito na reimportação — foi assim que o
retag do Grupo C (Dataprev Q36–Q40) ficou exposto sem ninguém notar.

E aí apareceu o defeito de fundo: **o rótulo de sub-bloco dos mapas da ALERO
usava o _slug_** (`banco-dados`, `eng-software`), que a tabela de tags não
reconhecia — então **47 questões caíam em `orfaos` por engano**. Corrigido, o
corpus muda de forma:

| bloco | antes | depois |
|---|---|---|
| `banco-dados` | 25 | **59** — o maior bloco específico |
| `eng-software` | 26 | **39** |
| `orfaos` | 68 | **21** |

Isso desmonta a leitura que o Grupo C tinha registrado ("órfãos é o bloco com
mais questões reais, maioria esmagadora DBA"): aquilo era **sintoma do bug**.
Com a classificação certa, `orfaos` vira o que o nome promete — 21 questões em
duas famílias, **arquitetura de computadores/SO** (11) e **administração e
direito público do MPU** (10), **nenhuma delas conteúdo do Perfil 3**. O
conteúdo de administração física continua sendo ensinado no capítulo de órfãos,
com remissão a partir de banco de dados.

**Garantia:** `./importar_provas.py` sobre o banco atual devolve o arquivo
**byte-idêntico**, e as 432 questões batem com o PDF em `q`, `alts` e `tag`.

**Aviso que veio junto: volume de material ≠ peso de prova.** O primeiro
reflexo ao ver `banco-dados` em 59 é estudar mais BD. A distribuição por prova
diz o contrário — **28 das 59** vêm de uma prova só, a da ALERO para o perfil
*Banco de Dados*, e **17 das 38** de segurança vêm da ALERO de *Redes*. Fora
das provas de outro perfil, BD cai para 30 e segurança para 19. Já
**engenharia de software é o único bloco forte em _todas_ as provas** (13 / 9 /
10 / 7) — não depende de nenhuma. As caixas dos três blocos passaram a dizer
isso explicitamente, e a Dataprev 2024 continua sendo a referência de peso: BD
e BI somaram 4 questões, segurança 3. **O roteiro não muda** — a conclusão nº 1
já tratava engenharia de software e BD como eixo duplo, sem eleger vencedor.

## 2026-07-25 (madrugada) — varredura do GRUPO C (auditoria, ITEM 7 · P0–P4)

Sete blocos varridos contra as 112 questões que os alimentam: **legislação,
redes, português, RLM, inglês, atualidades e órfãos**. É o grupo dos **gerais**
— e o achado que muda a leitura do conjunto é que, ao contrário do Grupo B,
**a maioria das alegações de "já caiu" aqui é verdadeira**: os blocos gerais
têm lastro real em prova. O problema é outro — **subcrédito** e camadas
desalinhadas. Apostila: **112 → 119 páginas**.

- **P0 · a dica de RLM contradizia as outras três camadas.** Abria com *"na
  FGV, RLM é MATEMÁTICA, não lógica formal"* e tratava tabela-verdade como
  resíduo de 1 questão, enquanto a apostila, o resumo e o Apêndice A já
  alertavam que o **edital 2026 põe a lógica formal em quatro dos cinco
  itens**. Era a única camada ainda na versão pré-edital. E a ALERO 2026
  confirma o alerta: **lógica proposicional encadeada e argumentação caíram
  lá**. Junto, a contagem que não fechava dentro do próprio capítulo (`\peso`
  dizia 5 questões, o *comosair* dizia "~6").
- **P1a · 14 questões sem apoio em camada nenhuma.** Entraram de fato:
  **handshake híbrido do TLS** (assimétrica só para acordar a chave de sessão),
  **SSH × Telnet** — a palavra "Telnet" não existia em lugar nenhum do repo — e
  **firewall stateful × stateless** em redes; **dado pessoal sensível** (o rol
  fechado do art. 5º, II) e a **neutralidade de rede** definida de fato (art.
  9º) em legislação; **juros simples × compostos**, **PA pelo termo geral**,
  **produto de matrizes**, **inclusão-exclusão**, **mediana/moda** e **desvio
  padrão** em RLM — a tabela de prioridades já listava esses tópicos e nenhum
  era ensinado; **concordância verbal dos impessoais** e **por que / porque /
  por quê / porquê** em português; **ESG por extenso** (a sigla aparecia 6×
  sem nunca ser expandida), **viés × variância** e as **métricas de
  classificação** em atualidades.
- **P1b · órfãos é o bloco mais transversal do repo.** Cinco das oito questões
  apontam para conteúdo que mora, com razão, em outro capítulo — e o Cap. 14
  não remetia a nenhum. Entrou um **mapa de remissões dirigidas** (mesma
  solução do Grupo B), com 2PC, RPA e low-code definidos ali mesmo. Nos
  capítulos de destino: o Cap. 5 ganhou o corte **Java EE** do par servidor web
  × servidor de aplicação (container web **e** container EJB), e o Cap. 6
  passou a separar o **trio clássico** dos Vs do Big Data (Volume, Velocidade,
  Variedade) das **extensões** — as duas camadas só diziam "5 V", e a
  quase-certa da questão é montada trocando um membro do trio por um V de
  extensão.
- **P2 · quatro quebras de contenção.** Os **princípios da LGPD** estavam só na
  dica — e caíram no TJ-RJ: o enunciado descrevia *"compatível com os fins
  informados, de acordo com o contexto"* e o gabarito era **adequação**,
  armadilha para quem decorou só "finalidade". A **desclassificação na LAI**
  idem, e os quatro distratores da Dataprev 2024 moram exatamente ali. O
  **art. 20 / explicabilidade** entrou no resumo de legislação — é o P2
  **herdado do Grupo A**, agora executado, e as duas afirmações da dica
  ("visto no TJ-RJ") foram conferidas e são verdadeiras. E o
  `resumo/orfaos.md` ganhou a **seção de IA/ML** que faltava, justo no tema
  que o bloco declara quente.
- **P4 · as 7 caixas `jacaiu` separam prova real do nosso banco.** Três
  alegações falsas, todas em legislação: **controlador × operador**, **bases
  legais da LGPD** e **guarda de registros do Marco Civil** não aparecem em
  nenhuma das 432 questões reais (a Q40 da Dataprev é ANPD × CNPD; a Q38 é
  *sanções*, não guarda). Os prazos numéricos da LAI também não — caiu a
  **classificação**, não os 5/15/25. Em atualidades, "viés algorítmico" saiu da
  lista: o viés do TJ-RJ é o **estatístico** do trade-off. O resto era
  subcrédito: **órfãos** é o bloco com mais questões reais do corpus (56, quase
  todas DBA da ALERO 2026) e não creditava nenhuma; **português** tem 67 e só
  listava as 12 da Dataprev. **P3:** o `resumo/orfaos.md` não tinha seção "O
  que já caiu" nenhuma — as duas listas não podiam bater quando uma não
  existia.
- **Correção de tag em `banco-provas.json`.** As cinco questões de LGPD/LAI/
  Marco Civil da Dataprev 2024 (Q36–Q40) estavam como `seguranca`. A estrutura
  da prova confirma o conserto: agora o **Módulo I fecha em 40** questões e o
  Módulo II em 30 — os 70 do edital. Antes, `legislacao` tinha zero.
- **Buraco que a própria auditoria abriu:** ao creditar **cálculo de sub-rede**
  como prova real (ALERO 2026), ficou visível que nenhuma camada ensinava.
  Entrou a tabela prefixo/máscara/hosts úteis (2ʰ − 2) e a notação simplificada
  do IPv6, que também caiu lá.

Nenhuma questão nova. `./valida.py --strict` idêntico ao baseline em todos os
commits.

## 2026-07-25 (noite) — varredura do GRUPO B (auditoria, ITEM 7 · P0–P4)

Cinco blocos varridos contra as 110 questões que os alimentam: **programação,
Java, frontend, BI e governança**. O achado dominante foi o inverso do Grupo A:
em três recortes (`git-devops`, `java-moderno`, `leitura-codigo`) a **apostila
estava mais fina que o resumo**, quebrando a contenção dica ⊂ resumo ⊂ apostila
justo na camada para onde o quiz manda quem erra. Apostila: **100 → 112
páginas**.

- **P0 · PHP 8 fora do lugar.** O item de funções de sessão (`session_start`,
  `session_destroy`, `session_regenerate_id`) estava dentro da seção "Python
  aplicado a dados" do Cap. 9. Não era só rótulo errado: conferida a origem, o
  item de PHP vem do **TJ-RJ**, enquanto todo o resto da seção vem do **MPU**.
  Virou `\subsection` própria, como o `resumo/` já fazia.
- **P1 · 13 questões sem apoio em nenhuma camada.** Entraram de fato:
  **granularidade (o grão da fato)**, **SCD tipos 1/2/3** (com o porquê da
  chave *surrogate*) e as **6 fases do CRISP-DM** em BI; **Daily Scrum de 15
  min** (fixos, independentes do tamanho da Sprint), **tripla restrição** e
  **lead time × cycle time** (com a âncora da palavra *solicitação*) em
  governança; **ARIA** (com a regra nº 1: não usar ARIA), **Flexbox 1D × Grid
  2D**, **especificidade de seletores** e **escopo de `var` × `let`** em
  frontend; **interface × classe abstrata** (o corte é construtor e atributo de
  instância, já que o Java 8 deu método `default` à interface), **`String`
  imutável / `StringBuilder`** e as **anotações de Spring e JPA** em Java.
- **P1 · a apostila alcançou o resumo.** O Cap. 9 tinha 5 linhas de Git; agora
  tem as três áreas, a tabela comando × efeito, **`fetch` × `pull`**, o trio
  **CI / entrega contínua / implantação contínua** e contêineres. A seção de
  Python ganhou `max(dic, key=)` e fatiamento; o Cap. 10, `record` e `var` com
  conteúdo (antes eram duas palavras num *bullet*).
- **P1 · remissões dirigidas.** O `ref_apostila()` usa a `tag`, nunca a `sub` —
  então quem erra uma questão de SOLID, GoF ou REST marcada como `programacao`
  cai no Cap. 9, que não cobre nenhum dos três. Entrou um bloco apontando cada
  tema para o capítulo certo (e **idempotência**, que faltava em todas as
  camadas, foi definida ali).
- **P2 · nove inversões dica → resumo desfeitas**, no mesmo padrão do Grupo A:
  tipos de fato, suporte × confiança, camadas Bronze/Silver/Gold, DAMA-DMBOK e
  *drillthrough* em BI; os **12 princípios do PMBOK 7 pelo nome**, o
  **propósito de cada prática ITIL** que a banca troca e os **componentes** do
  COBIT em governança; `createPortal` em frontend.
- **P3 · três itens citados em "o que já caiu" e nunca ensinados.**
  **`@import`**, **lead time × cycle time** e **relacional × multidimensional**
  apareciam nas duas listas sem existir no corpo de nenhuma camada. Os três
  foram ensinados (o `@import` com o motivo de ser distrator de media query, e
  o modelo multidimensional com ROLAP/MOLAP/HOLAP), e as **cinco duplas de
  listas** foram sincronizadas.
- **P4 · a caixa "já caiu" dizia mais do que podia.** O ambiente da apostila é
  rotulado *"O que já caiu nas provas"*, mas era preenchido a partir do
  `banco.json`. Conferindo item a item contra `banco-provas.json` (432 questões,
  7 provas), tinham **zero ocorrência em prova real**: checked × unchecked,
  `==` × `equals`, ArrayList/LinkedList, ordem de catch/`finally`, *pinning*,
  box model/`box-sizing`, React × Angular, `key`/`useState`, `@import` e lead
  time × cycle time. Pior: `dicas/java.md` já era honesta ("mesmo sem ter caído
  na amostra") e a apostila a contradizia. As cinco caixas — e as cinco do
  `resumo/` — passaram a **separar o que caiu em prova real, com a sigla**
  (Dataprev 2024, TJ-RJ, MPU, ALERO 2026), **do que é questão nossa**.
- **P4 · miudezas.** "Aparece nas duas provas de TI" em `dicas/bi.md` estava
  vencido (o corpus foi de 2 para 7 provas); a chave surrogada estava creditada
  ao bloco errado; e a regra de que **diferir só no tipo de retorno não é
  sobrecarga, é erro de compilação** entrou no Cap. 10, que a cobrava sem
  enunciar.

`./valida.py --strict` sai 0, com os mesmos 2 avisos pré-existentes
(`mpu Q41` fora do sorteio e as 9 questões de correta longa). Banco não tocado:
336 + 432.

## 2026-07-25 — desfeita a inversão de camada (auditoria, Bloco VII/ITEM 7 · P2)

Em quatro blocos, conteúdo existia só em `dicas/` — a camada **rasa** — e
faltava no `resumo/`, a **profunda**, invertendo o modelo dica ⊂ resumo ⊂
apostila. Tudo promovido para o `resumo/`. Nenhum `.tex` tocado, logo sem
recompilação.

- **Engenharia de Software.** **Decodificação de EE/SE/CE/ALI/AIE** — o resumo
  só listava as siglas dentro da tabela de Ponto de Função, e a banca dá telas
  pedindo a classificação: entrou a tabela com o gatilho de cada uma e os dois
  cortes que decidem a questão (**SE × CE** pela existência de cálculo; **ALI ×
  AIE** por quem *mantém* o dado). **Tipos de RNF** (produto, organizacional,
  externo) com exemplo de enunciado para cada. **Como contar RF e RNF** num
  texto longo, incluindo a armadilha da frase que só descreve contexto e não é
  requisito nenhum. E uma seção de vizinhos do edital: **BPMN** (raias,
  *handoff*, gateway exclusivo × paralelo — com a remissão ao losango da UML,
  que é outra coisa), **CBOK**, **SNAP** (mede o não funcional, é
  *complementar* à APF, não substituta) e **GitLab CI** (`.gitlab-ci.yml`,
  *stages* × *jobs*, variáveis protegidas).
- **Banco de Dados.** **`LIMIT`/`OFFSET`** com a conta da paginação (`LIMIT 10
  OFFSET 20` = linhas 21–30) e o alerta de que sem `ORDER BY` não há ordem
  garantida; **`DISTINCT`** atuando sobre a linha inteira; **anti-join** nas
  três formas equivalentes, com o motivo de preferir `NOT EXISTS` (o `NOT IN`
  quebra com `NULL`); e **MongoDB** com a tabela de tradução do vocabulário
  (tabela→*collection*, linha→*document*) e o operador **`$size`**, que filtra
  por número **exato** de elementos de um array.
- **Segurança.** **Os quatro *claims* do OIDC** em tabela (`iat`, `exp`, `sub`,
  `jti`) — a apostila mandava decorar os quatro, o resumo não os trazia —, com
  o par que se confunde (`sub` = quem é o usuário; `jti` = qual é o token). O
  **mapeamento dos 4 temas da 27002:2022 a exemplos concretos**: o resumo tinha
  só a contagem (37/8/14/34), e a questão dá um controle e pede o tema — com o
  critério que separa *pessoas* de *organizacional*. E o **SSDF** (NIST SP
  800-218) com seus quatro grupos, explicando por que "cadeia de suprimentos",
  "ambiente de engenharia" e "treinamento" aparecem como distrator em questão
  de OWASP.
- **Arquitetura.** **DDD detalhado** em tabela, bloco a bloco, cada linha
  trazendo *o erro que a FGV insere* — porque nas duas provas em que o tema
  caiu os distratores eram os outros blocos com o papel adulterado. **RabbitMQ:
  *publisher confirms*** (produtor→broker) × ***consumer acknowledgements***
  (broker→consumidor), e o trio necessário para sobreviver a um restart (fila
  durável + mensagem persistente + confirmação), já que nenhum dos três sozinho
  resolve. **Elementos do WSDL** em tabela, com a espinha que resolve o item:
  `portType` = **o quê**, `binding` = **como**, `service`/`port` = **onde**.
- Três itens da lista original do P2 já haviam sido resolvidos pelo P3 —
  **HMAC**, **VIEW** e **chave surrogada** — e dois pelo P1/P3 —
  **RKE/K3s/Rancher** e **armazenamento de objetos**. Conferidos antes de
  escrever, para não duplicar.

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
