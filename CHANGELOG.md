# Histórico de atualizações

Melhorias no material de estudo (Dataprev 2026, Perfil 3).

## 2026-08-07 — déficit de questões zerado (+30) e o banco etiquetado de 48% para 80%

Duas frentes fechadas no mesmo dia: a **B** (o buraco de pool para os 10
simulados) e a **C** (a etiquetagem do acervo). A **D** foi verificada e segue
aberta por fato externo.

**Frente B — as 30 que faltavam.** Inglês foi de 102 para **120** e atualidades,
de 48 para **60**: exatamente a demanda de 10 simulados. Português, RLM e
legislação não receberam questão nenhuma, porque já estavam acima da demanda.
O déficit do Módulo I, que era de 137 em julho e de 30 na véspera, é **zero**.

As 18 de inglês nasceram de **cinco textos-base novos**, escritos aqui (não são
trecho de publicação real), todos sobre TI e serviço público: modernização de
legado, identidade digital, formato aberto em contratação, green software e
divisão digital. Cada texto sustenta 3–4 itens respondíveis só com ele. O rateio
mirou os microtópicos magros: **verbos-modais** saiu de 1 para 6 questões, e o
formato variou de propósito entre o item que pede o **valor** do modal (`may` →
possibilidade, `should` → recomendação, `will` → certeza, `cannot` →
impossibilidade) e o que pede a **substituição** sem mudança de sentido (`must`
→ `has to`), que é como a FGV alterna.

As 12 de atualidades saíram todas de **fonte primária conferida no dia**, e é o
que as torna caras de refazer:

- **AI Act, o adiamento que quase todo resumo erra.** O Regulamento (UE)
  2026/1744, de 08/07/2026 (o *Digital Omnibus on AI*, publicado no JO em
  24/07), empurrou as obrigações de alto risco do **Anexo III para 02/12/2027**
  e do **Anexo I para 02/08/2028** — mas **não** tocou no art. 50: transparência
  segue valendo desde **02/08/2026**, e as proibições do art. 5º, desde
  02/02/2025. A pegadinha montada é justamente o "adiaram tudo".
- **PL 2338/2023 continua em tramitação**, conferido no dado aberto da Câmara
  (situação "Aguardando Parecer", movimentação de 17/06/2026) — a questão que já
  existia no banco segue correta.
- **COP30 (Belém, 11/2025):** a decisão do *Mutirão Global* **não menciona
  combustíveis fósseis** e convoca esforços para ao menos **triplicar o
  financiamento de adaptação até 2035**, além do horizonte de US$ 1,3 tri/ano.
- **TFFF:** não é fundo de doação. É *blended finance* — o capital é investido e
  o **rendimento** paga valor fixo por hectare de floresta em pé, com ao menos
  **20% aos povos indígenas e comunidades locais**.
- **Resolução CVM 244, de 29/05/2026:** revogou o art. 2º da Resolução CVM 193 e
  **acabou com a obrigatoriedade** do relatório de sustentabilidade (ISSB) que
  valeria a partir dos exercícios iniciados em 2026. Quem optar publica por no
  mínimo três exercícios; a partir de 2027, quem não publicar tem de justificar
  em comunicado ao mercado.

O `./valida.py --novas 30` acusou "correta é a mais longa" em 15 das 30 (o
esperado é ~20%) — vazamento de forma clássico de texto gerado. Corrigido item a
item, encurtando a correta ou alongando o distrator: **5 de 30**, e os cinco
restantes são empate de comprimento em alternativa de uma palavra ("ability." ×
"possibility.") ou de número, onde não há o que ajustar.

**Frente C — 902 de 1133 questões etiquetadas (80%).** Eram 533 de 1103 (48%).
A passada automática propõe, mas **as 345 propostas foram revisadas à mão, uma a
uma** — e a revisão pagou: **34 trocas** e **23 descartes**. O que a keyword
errou é instrutivo, porque é o mesmo par que a FGV inverte: a questão do
**teorema CAP** casou com `propriedades-acid`, a do **DIP/SOLID** casou com
`ecossistema-spring`, a de **Flutter/Dart** com `diagrama-classes`, a de
**LIMIT/OFFSET** com `arquitetura-computadores-so`.

Dois recortes do casamento tiveram de mudar, e ficam registrados no
`CONTRIBUINDO-QUESTOES.md`:

1. **texto-base envenena tanto quanto distrator.** Casando no enunciado inteiro,
   um item de inglês que pede *the main purpose of the text* virava
   `verbos-modais` por causa de um "can" perdido no meio do texto. Agora o
   casamento usa só o **comando** (o bloco depois do texto-base).
2. **`comando-negativo` não é etiqueta de estudo.** Ele vence em qualquer item
   que diga "assinale a INCORRETA" e enterra o conteúdo real. Ficou fora da
   automação.

Os 23 descartes são deliberados: ou o vocabulário não tem microtópico que
descreva (stored procedure, função determinística, apassivação, decorator do
Python — que não é o padrão GoF), ou o assunto está **fora do edital** (mandado
de segurança, improbidade administrativa, herdados do TJRJ/MPU). Etiqueta errada
distorce o `./fraquezas.py`; ausência, não.

**Microtópico novo: `ataques-malware`** (168 no vocabulário). Ele não foi
inventado para a etiquetagem — é a seção que a frente A escreveu na apostila e
no `teoria/` no mesmo dia, e sem ela 12 questões reais sobre spoofing, DDoS,
Teardrop, phishing, ransomware e keylogger não tinham onde ser etiquetadas.
Com ele, o `SUB_OBRIGATORIA_APOS` do `valida.py` caiu de 403 para **395**.

**Frente D — verificada, segue aberta.** A página do concurso da NAV Brasil
publicou até agora apenas o gabarito **preliminar** (03/08), com recursos
encerrados em 04/08; não há definitivo. A `nav-tec` Q58 continua como
divergência anotada, e são os 2 avisos que o `./valida.py` mostra.

## 2026-08-07 — a teoria que faltava: ataques, malware, ciclomática e code smells

As 74 questões importadas na véspera cobravam três assuntos que **não existiam
em nenhuma das quatro camadas**. O quiz explicava a questão, mas não havia onde
estudar o conteúdo. Fechado agora, nas quatro.

**1. Catálogo de ataques e de malware** (Cap. 7). O capítulo se organizava por
conceito — tríade, criptografia, TLS, controle de acesso, OWASP, X.800, riscos,
continuidade, detecção — e não tinha seção de **tipos de ataque**: XSS e SQLi
só apareciam de passagem dentro do OWASP; MitM e session hijacking, em lugar
nenhum. A seção nova cobre, em quatro blocos:

- **sessão e canal:** CSRF, XSS, MitM, replay, session hijacking, cada um com o
  traço que só ele tem e a defesa correspondente;
- **engenharia social:** spam × phishing × spear phishing, mais whaling,
  vishing/smishing e pharming;
- **família DDoS:** SYN flood, Ping of Death, Smurf, Teardrop, Slowloris, UDP
  flood/storm e HTTP flood, cada um pelo recurso que esgota;
- **família de malware:** vírus, worm, trojan, spyware, backdoor, rabbit,
  ransomware, rootkit e bot.

O fio condutor das quatro é o formato que a banca usa: o **carrossel**, em que
cada alternativa recebe a definição do vizinho (é literalmente o que a
`cprm-ads` faz nas Q40, Q41 e Q61). Contra carrossel não adianta reconhecer o
nome — a apostila ancora cada um num traço único, e as duas perguntas que
fecham o malware são "replica sozinho?" e "para onde?".

Um cuidado que custou análise: o **CSRF não entra na tabela do OWASP**. Ele
saiu da lista em 2017 e desde 2021 está *dentro* de A01 Broken Access Control —
confirmado na página oficial da categoria, que cita a CWE-352 entre as fraquezas
notáveis. A tabela 2025/2021 da apostila estava correta e não foi tocada; o
CSRF entrou como **ataque**, não como categoria.

**2. Complexidade ciclomática de McCabe** (Cap. 2), com exemplo resolvido. A
fórmula formal ($V(G) = E - N + 2P$), a prática (pontos de decisão + 1), a
lista do que conta (incluindo cada `&&`/`||`, por curto-circuito) e do que não
conta — o `else`/`senão` final, que não testa nada. O exemplo é a função da
`epe-ti` Q79, contada linha a linha até o 5, com os dois erros que a banca
planta como alternativa: contar o `senão` (dá 6) e esquecer o +1 (dá 4).

**3. Code smells nomeados** (Cap. 2). Antes, "code smell" aparecia só como
conceito genérico. Agora estão as cinco famílias do catálogo de Fowler e Beck
(bloaters, couplers, change preventers, dispensables, OO abusers) e a
refatoração canônica dos três que a FGV já nomeou: Long Method → Extract
Method, **Data Clumps** → Extract Class/Introduce Parameter Object, **Feature
Envy** → Move Method. A pegadinha registrada é a da `epe-ti` Q77: vender o
cheiro como boa prática ("repetir o mesmo grupo de variáveis melhora a
legibilidade"), que é a definição literal de Data Clumps.

**4. JMeter**, numa caixa `jacaiu` (Cap. 2), âncora `epe-ti` Q80 — Sampler,
Thread Group com ramp-up, Timer, Assertion e Listener, com o ramp-up desmentindo
a afirmativa de que os usuários virtuais sobem todos ao mesmo tempo.

**Duas correções de fato encontradas de passagem**, ambas por contagem no banco:
a caixa `jacaiu` de segurança dizia **38 questões** em prova real (são **56**, e
17 delas seguem sendo da ALERO) e afirmava que **nenhuma** das 432 questões
citava SAST/DAST — hoje são 700 questões, e o par já caiu na NAV Brasil 2026 e
na EPE 2024, sempre em cenário de esteira CI/CD.

O `teoria/` recebeu a versão didática dos mesmos conteúdos (com `conceito`,
`cuidado`, `regrapratica` e `exemplo` — sem caixas de banca), incluindo dois
exemplos que a apostila não comporta: por que o Slowloris derruba um servidor
de uma máquina só, e como reconhecer Feature Envy contando de qual classe vêm
os dados que o método consome. Apostila em **166 páginas**, teoria em **190**,
as duas compilando sem overfull/underfull nem referência quebrada;
`./valida.py` sem drift entre as camadas.

## 2026-08-07 — o sublinhado da banca volta ao quiz, e a Q17 do CPRM sai do sorteio

Duas correções no `importar_provas.py`, as duas sobre o mesmo tema: o que a
camada de texto do PDF joga fora.

**1. A marcação da banca, recuperada.** A FGV sublinha o termo que a questão
manda analisar ("assinale a opção em que o termo sublinhado…", "o elemento
destacado em…"). Nem o `pypdf` nem o `pdftotext` preservam sublinhado, então
esse termo chegava ao quiz indistinguível do resto da frase — e a questão
virava adivinhação. São **42 questões** que citam a marcação, quase todas de
português, o bloco mais pesado do Módulo I.

No PDF o sublinhado não é atributo de fonte: é um retângulo fino desenhado sob
a palavra. O **PyMuPDF** lê esses desenhos, e o texto recortado logo acima de
cada reta é exatamente o trecho grifado. Agora ele volta ao banco entre
`«…»` — e o ganho aparece justo onde doía: a `dataprev2024` Q16 recuperou o
`«Thus,»` do "underlined linker", a `nav-med` Q1 recuperou os três verbos
(`«realizou,»`, `«foi presidida»`, `«contou»`), a `nav-med` Q5 recuperou o
`«À medida em que»` e a `dataprev2024` Q9, o `«de modo que»`.

**Placar: 18 das 42** — 7 com a marca nas alternativas e 11 no enunciado ou no
texto-base. As outras 24 ficaram como estavam, e três travas explicam por quê:

- **só a questão que pede a marca é marcada.** A FGV sublinha por ênfase em
  muito lugar, e marcar tudo trocaria 42 questões por 351: borda de tabela e
  régua de rodapé entram como falso sublinhado (a `cnsal-ads` Q51 chegou a
  receber `«Título_PL»` e `«150»`, que são células de uma tabela).
- **a marca tem de identificar um trecho só.** Um grifo curto da Q9 ("de um",
  "alguns") casava em dezenas de outras questões; vale apenas a marca que
  aparece em **um único** campo do caderno.
- **ou todas as alternativas, ou nenhuma.** Esta é a mais importante:
  marcação parcial é *pior* que nenhuma. Em 18 questões o recorte só recuperava
  parte dos grifos — e na `cnsal-ads` Q7 a única alternativa que ficaria sem
  marca era exatamente o gabarito. O candidato acertaria pelo artefato, não
  pelo português. Nessas, o texto fica como veio.

**2. `cprm-ads` Q17 fora do sorteio.** A questão das 17 caixas empilhadas
depende do desenho, mas escapava da regra: ela diz "**A Figura mostra** como…",
e a lista de dêixis só tinha o particípio ("mostrada"), não a forma do
presente. Virou exceção declarada no código (`DEPENDE_DE_FIGURA_MANUAL`), e
não regra nova — acrescentar os verbos no presente trancaria outras três
questões que se sustentam sozinhas: a `nav-med` Q23 traz os pontos A(3,1) e
B(6,3) no próprio texto, a `nav-med` Q30 teve a tabela transcrita na extração,
e a `nav-eng` Q70 **narra** o diagrama BPMN por escrito, sem imprimi-lo. Dá
para calibrar um regex de três condições que acerte só a Q17, mas seria regra
ajustada a um único exemplo; enquanto o caso for um, a lista é mais honesta —
e, por morar no parser e não no JSON, sobrevive à reimportação.

Conferido por diff nas duas mudanças: 19 questões alteradas ao todo, `ans`,
`why`, `erradas` e `sub` preservados, e o importador continua devolvendo o
arquivo byte-idêntico. Com a Q17 fora do sorteio, o pool utilizável passa de
1080 para **1079** (RLM: 65 → 64).

## 2026-08-07 — as 73 questões novas explicadas e o parser aprendendo a quinta e a sexta marca de texto-base

Fecha a pendência aberta pela importação da EPE, da Receita Federal e do CPRM
Pesquisador. `./valida.py` volta a **2 avisos** — os dois da `nav-tec` Q58, a
divergência de gabarito registrada. **Todas as 15 provas reais do banco estão
com explicação completa.**

| lote | qtd |
|---|---|
| específicos da `epe-ti` (36–80) — eng. de software, arquitetura/nuvem, banco de dados, BI, segurança, Python, JavaScript, HTML5 | 40 |
| inglês da `epe-ti` (11–20) | 10 |
| inglês da `rfb-ana` (16–25) | 10 |
| inglês da `rfb-aud` (11–18) | 8 |
| inglês da `cprm-pesq` (11–15) | 5 |

**Conserto no `importar_provas.py`, achado no meio do trabalho:** as questões
de inglês da Receita Federal entraram **sem o texto-base**. O parser só
reconhecia texto anunciado por fórmula ("Use the following TEXT to answer the
next six questions"), e a RFB não anuncia nada — imprime só `Text I` e emenda o
texto. O CPRM, por sua vez, usa uma sexta forma, em português ("As questões da
prova de Língua Inglesa referem-se ao TEXTO a seguir"). Agora as duas são
reconhecidas, e como nenhuma delas informa **quantas** questões o texto cobre,
o alcance passou a sair da posição: cada texto vale até a questão anterior ao
próximo marcador, e o último vale até o cabeçalho da seção seguinte.

Duas armadilhas apareceram no caminho, e as duas viraram regra no código:

- **a redação do CPRM também abre com "TEXTO I"** — e, sem corte, o texto da
  discursiva era prefixado nas 30 questões objetivas do começo do caderno. Além
  do corte pelo cabeçalho (`Redação`, `Prova Discursiva`, `Rascunho`), há uma
  trava geral: a questão que abre o grupo tem de vir **depois** das já vistas.
- **o pôster e o cartum da NAV Brasil delimitam grupo mesmo sem texto.** Na
  primeira versão da função, o `Text I` da `nav-med` se espalhou por cima das
  questões do pôster (Q51–Q56), porque as marcas sem prosa eram descartadas
  antes de servirem de fronteira. Agora elas entram na lista como divisor, e
  só não produzem texto.

Resultado da mudança, conferido por diff antes de commitar: **33 questões
ganharam o texto-base** (`rfb-ana` 16–25, `rfb-aud` 11–18, `cprm-pesq` 11–15 e,
de brinde, as 10 de português do `cprm-ads`, que se apoiam em "O Brasil na
crise do clima"). Nenhuma questão encolheu, nenhuma mudou de `requer_imagem` e
`ans`, `why` e `sub` seguem preservados. `./importar_provas.py` continua
devolvendo o arquivo byte-idêntico.

A etiquetagem por microtópico subiu de 467 para **533 das 1103** (48%).

## 2026-08-07 — EPE 2024, as duas da Receita Federal e o CPRM Pesquisador: +74 questões e o inglês quase fecha

As quatro provas verificadas na busca da noite entraram. Pool utilizável de
1007 para **1080**, e o número de provas reais vai de 11 para **15**.

| prova | recorte | aproveitado |
|---|---|---|
| `epe-ti` — EPE 2024, Analista de Gestão Corporativa – TI / Soluções (01/09/2024) | inglês 11–20 + específicos 36–80 | **51** |
| `rfb-ana` — Receita Federal 2023, Analista-Tributário, manhã (19/03/2023) | inglês 16–25 | **10** |
| `rfb-aud` — Receita Federal 2023, Auditor-Fiscal, manhã (19/03/2023) | inglês 11–18 | **8** |
| `cprm-pesq` — CPRM 2025, Pesquisador em Geociências / Hidrogeologia (30/11/2025) | inglês 11–15 | **5** |

Todos os gabaritos são **definitivos**. Alinhamento gabarito↔alternativa
conferido resolvendo item por item em cada caderno: `crave` → *yearn for*
(`cprm-pesq` Q13), oposto de `quietness` → *loudness* (`rfb-ana` Q18),
`garnering` → *storing grains* (`rfb-aud` Q12).

**O inglês era o alvo e quase fechou:**

| bloco | antes | agora | precisa | falta |
|---|---|---|---|---|
| inglês | 69 | **102** | 120 | +18 |
| atualidades | 48 | 48 | 60 | +12 |

Os 41 específicos da EPE são bônus — o Módulo II já não tinha déficit, mas é
prova de **cargo de TI de 2024** e o conteúdo é quase um espelho do edital:
eng. de software 12 (XP, DevOps, BDD, design thinking, code smells, testes,
métricas), arquitetura 8 (nuvem, escalabilidade, API, MVC), BI 5 (ETL, big
data, Power BI), segurança 5, banco de dados 4, programação 4 (Python,
estruturas de dados, garbage collection), frontend 2 (JavaScript, HTML5) e
redes 1. O BI, que era o bloco mais magro do Módulo II, sobe de 37 para 42.

**Descartes registrados nos mapas:** português e RLM das quatro provas (sem
déficit); administração pública, valor público da EPE, contabilidade,
auditoria, economia, direito tributário, metodologia científica, estatística e
hidrogeologia (fora do edital); Informática de escritório da EPE — Q38
(Microsoft 365) e Q39 (Excel), pela regra 2. Fora também a **Q75 da EPE,
anulada** pela banca.

**Pendência herdada:** as 73 questões novas entraram com gabarito oficial mas
sem `why`/`erradas` — `./valida.py` passa de 2 para **148 avisos**. Mesma
situação das duas importações anteriores, e o mesmo caminho de saída: lotes de
10 por bloco, específicos primeiro.

## 2026-08-07 — as 106 questões do CPRM e do `nav-med` ganham explicação (`valida.py`: 214 → 2 avisos)

Fecha a pendência aberta pela importação da manhã. As **106 questões
explicáveis** das duas provas novas passam a ter `why` e `erradas` completos —
o banco volta ao padrão de **todas** as provas reais explicadas, com a única
exceção conhecida (`nav-tec` Q58, divergência de gabarito registrada e não
consertada).

Ordem de trabalho, do maior para o menor retorno:

| lote | o que entrou | qtd |
|---|---|---|
| específicos do `cprm-ads` (31–70) | segurança, arquitetura, banco de dados, BI, eng. de software, java, redes, governança, LGPD | 39 |
| atualidades (`cprm-ads` 21–30) | o bloco mais escasso do banco | 10 |
| inglês (`nav-med` 41–60) | as 16 que não dependem de figura | 16 |
| RLM (`cprm-ads` 11–20, `nav-med` 21–33) | | 22 |
| português (`cprm-ads` 1–10, `nav-med` 1–10) | | 19 |

**Fonte primária antes de escrever**, como manda o `CLAUDE.md`: as dez de
atualidades eram o ponto mais exposto. Conferidos o acordo de minerais
EUA–Ucrânia (assinado em **30/04/2025**, com lítio e titânio entre os minerais
críticos nomeados), o poço **Bumerangue** da bp (Bacia de Santos, anúncio de
**04/08/2025**, lâmina d'água de 2.372 m), o **Jabuti Acadêmico 2025** de
História e Arqueologia (Lilia Moritz Schwarcz, *Imagens da branquitude*) e o
**art. 12 da LGPD**, que a Q38 cobra quase ao pé da letra.

**82 questões de prova ganharam `sub` de quebra** — a etiquetagem subiu de 385
para **467** das 1.029 (45%). Saíram do zero três microtópicos:
`backup-recuperacao` (cprm Q35), `atualidades-socioambiental` (ODS, marco
temporal, pré-sal) e, em inglês, `julgamento-afirmativas` e `verbos-modais`.

Nenhuma divergência nova com o gabarito definitivo do CPRM. Duas observações
que ficam registradas:

- **`cprm-ads` Q17 depende da figura** (as 17 caixas empilhadas) e o
  importador não a marcou como tal — o enunciado cita "a Figura", mas a
  imagem não foi extraída. A explicação foi escrita mesmo assim, pelo caminho
  que a questão pede (contar as 12 visíveis e subtrair de 17), mas no quiz o
  item aparece sem o desenho. Conserto de verdade é no `importar_provas.py`,
  não à mão no JSON.
- **`cprm-ads` Q59** (Oracle Spatial) tem nomenclatura frouxa no gabarito: o
  objeto que comporta ilhas (polígonos) e boias (pontos) é uma **coleção
  heterogênea** (`SDO_GTYPE` terminado em 4, COLLECTION), não um
  "multipolígono", que por definição é homogêneo. A alternativa marcada é a
  única viável e o `ans` não foi tocado; a explicação usa o nome correto.

## 2026-08-07 — CPRM 2025 e NAV Brasil nível médio importadas: +115 questões, o inglês sobe 30%

As duas provas verificadas na busca da véspera entraram no banco. Pool
utilizável de 901 para **1007**, e o número de provas reais vai de 9 para
**11**.

**CPRM 2025 — Analista em Geociências / Análise e Desenvolvimento de
Sistemas** (`cprm-ads`), aplicada em **30/11/2025**, gabarito **definitivo**
(08/01/2026, nenhuma questão anulada neste caderno). Entrou o **caderno
inteiro, 70 questões** — é a primeira prova importada sem nada a descartar:
não tem bloco de "Informática" nem legislação genérica, e a única questão de
lei (Q38, anonimização na LGPD) é conteúdo do edital. Vale por três motivos:
é **cargo de TI**, traz **10 de atualidades** (o segundo bloco mais escasso —
ética da IA pela UNESCO, ODS/Agenda 2030, minerais estratégicos) e os 40
específicos são de ADS, o mesmo perfil da Dataprev.

> Correção de data: a busca tinha registrado 02/12/2025, que era a data do
> comunicado. O cabeçalho do gabarito definitivo diz **30/11/2025**.

**NAV Brasil 2026 — nível médio, Operador de Torre de Controle**
(`nav-med`), aplicada em 02/08/2026. Entraram **45 das 60**: inglês 41–60,
RLM 21–35 e português 1–10. Ficaram de fora as 10 de legislação/ética
(direito administrativo e Código de Ética da estatal) e as 5 de Informática —
e aqui, ao contrário da `nav-tec` Q33, **nenhuma das cinco se disfarçava de
atualidades**: era Excel, Chrome e memória cache mesmo. É a única fonte
recente da FGV com 20 questões de inglês; a ressalva é que o caderno é de
nível médio e o vocabulário é de aviação, não de TI.

Efeito no déficit do Módulo I, medido contra os 10 simulados do roteiro:

| bloco | antes | agora | precisa | falta |
|---|---|---|---|---|
| inglês | 53 | **69** | 120 | +51 |
| atualidades | 37 | **48** | 60 | +12 |
| português | 110 | **129** | 120 | ok |
| RLM | 43 | **65** | 50 | ok |

Português e RLM saíram do vermelho. **Só sobraram inglês e atualidades**, 63
questões ao todo — antes eram 107 espalhadas por quatro blocos.

**Quatro correções no `importar_provas.py`**, todas achadas por estas provas e
todas com efeito retroativo:

- **texto-base em português.** O marcador só era reconhecido em inglês, então
  o "Atenção! O texto a seguir refere-se às duas próximas questões" da
  `nav-tec` passava batido — o texto grudava na alternativa (E) da questão
  anterior e as questões do grupo ficavam sem ele. Era exatamente o defeito
  corrigido **à mão** no JSON na véspera, que a próxima reimportação teria
  desfeito em silêncio;
- **segunda fórmula em inglês.** A NAV Brasil escreve "Read Text IV and answer
  the four questions that follow it", e não "Use the following TEXT..." como a
  Dataprev 2024. Sem isso, os quatro textos de leitura do `nav-med` não se
  ligavam a nenhuma das 20 questões de inglês;
- **cabeçalho "Informática"** entrou na lista de títulos de seção — é o outro
  conserto manual da véspera (`nav-tec` Q28), agora reproduzível a partir do
  PDF;
- **pôster e cartum contam como figura.** "The word 'because' in this poster"
  não casa a regra geral (o dêitico está no demonstrativo, não numa palavra de
  apontamento), mas sem a imagem a questão não existe. Quatro questões do
  `nav-med` saíram do sorteio por isso — e as duas do mesmo grupo que se
  sustentam sozinhas (analogia `height : high`, apóstrofo de posse) ficaram.

Com isso `./importar_provas.py` volta a ser idempotente: reimportar as 9
provas antigas devolve o mesmo conteúdo, sem desfazer conserto nenhum.

**Pendência herdada:** as 115 questões novas entraram com gabarito oficial mas
sem `why`/`erradas` — `./valida.py` passa de 2 para 214 avisos. Mesma situação
da NAV Brasil na véspera, e o mesmo caminho de saída.

## 2026-08-07 — as 86 questões da NAV Brasil ganham explicação (`valida.py`: 172 → 2 avisos)

As 89 questões importadas da NAV Brasil entraram com gabarito oficial mas sem
`why` e sem `erradas` — o quiz corrigia, e não ensinava. Agora **85 das 86
explicáveis** têm explicação completa, no padrão do resto do banco: `why`
analítico e uma entrada de `erradas` para cada alternativa incorreta, com o
mecanismo do distrator tecido na frase (inversão de par, absoluto,
extrapolação, quase-certa). Todas ganharam `sub`, com duas exceções de RLM
(problema de álgebra de dígitos e de idades) para as quais o vocabulário de
`subtags.py` não tem microtópico — melhor sem etiqueta do que com etiqueta
errada poluindo o `./fraquezas.py`.

**Uma questão ficou de fora, de propósito:** `nav-tec` Q58 (3FN). O gabarito
oficial da FGV (TIPO 1, conferido no PDF) marca **C** — "superchave que viola
as invariantes lógicas da Forma Normal de Boyce-Codd" —, mas o enunciado
descreve dependência transitiva (`Nome_Fabricante` → `ID_Fabricante` →
`ID_Veiculo`), que é a letra **E**. O `ans` não foi alterado e a questão segue
sem explicação para não ensinar a versão errada. O gabarito publicado ainda é o
**preliminar**; vale reconferir quando sair o definitivo.

Dois defeitos de importação corrigidos no caminho: o texto-base compartilhado
pelas questões 4–5 e 6–7 de português tinha ficado grudado na alternativa (E)
da questão anterior, deixando quatro itens sem o texto que eles pedem para
serem respondidos; e o cabeçalho de seção "Informática" do PDF havia colado na
última alternativa da Q28 de RLM.

## 2026-08-07 — NAV Brasil 2026 importada: +89 questões reais e o Módulo II fecha o déficit

Duas provas da FGV aplicadas em **02/08/2026** (NAV Brasil, Edital 01/2026):
`nav-tec` (Analista de Tecnologia) e `nav-eng` (Engenheiro Software) — este
último é o cargo mais próximo do Perfil 3 que a FGV aplicou recentemente,
exigia Engenharia da Computação e cobra projeto, teste e revisão de código.

Entraram **89 das 140** questões. As 51 que ficaram de fora:

- **40** — o Módulo I do `nav-eng` é **idêntico** ao do `nav-tec` (conferido
  linha a linha no PDF, e os dois gabaritos batem exatamente nas questões 1–40).
  Importar dos dois criaria 40 duplicatas competindo no sorteio do simulado;
- **7** — "Legislação" do caderno é direito constitucional/administrativo e
  ética (licitação, processo administrativo). A legislação do edital é LGPD,
  Marco Civil e LAI. Importar repetiria o problema que o banco já tem: 42
  questões de `legislacao` vindas do TJRJ/MPU são de direito administrativo;
- **4** — "Informática" (Word, Chrome, planilha): o Perfil 3 não tem esse bloco.

Um achado que valeu a leitura: a **questão 33 é rotulada "Informática" pela
banca**, mas cobra o impacto da IA nas ocupações (estudo do MTE) — isso é
`atualidades` no edital do Lucas, justamente o bloco mais escasso. Entrou pelo
conteúdo, não pelo rótulo.

Resultado: pool utilizável de 815 para **901**. O **Módulo II zerou o déficit**
em todos os blocos, e o Módulo I caiu de 137 para 107 questões faltando
(inglês 67, atualidades 23, português 10, RLM 7).

**Pendência:** as 89 questões entraram sem `why`/`erradas` — todas as outras
sete provas do banco têm explicação, então o `./valida.py` agora acusa 172
avisos. O quiz roda, mas não explica ao errar.

## 2026-08-06 — subtags viram taxonomia do edital (167), `sub` obrigatório e 497 questões etiquetadas

O vocabulário de 14 microtópicos não cobria o banco: `rlm`, `redes`, `bi`,
`legislação` e mais seis blocos não tinham nenhum valor aplicável. Em vez de
inventar ~150 nomes, o vocabulário foi **derivado das seções de
`teoria/capitulos/*.tex`** (e da apostila nos capítulos em que ela é mais
detalhada) — a taxonomia que já passou por auditoria. Sobre isso entrou uma
camada de curadoria explícita (77 renomeações, 10 fusões, 2 descartes: `800`
virou `x800-osi`, `art` virou `marco-civil-art19`, `regencia-verbal-nominal`
fundiu na `regencia` já curada) e 4 microtópicos escritos à mão para buracos que
o livro não seccionava — `sql-consultas`, `modelos-de-processo`,
`direitos-do-titular`, `normalizacao`. Total: **167**.

As keywords extraídas do LaTeX eram cegas (`HashMap` não estava em
`colecoes-java`), então as 167 listas foram **reescritas à mão**. Ganho duplo: a
etiquetagem melhora e a estimativa de cobertura do `./fraquezas.py` fica honesta
para sempre.

**497 das 825 questões (60%) ganharam `sub`** por casamento de palavra-chave.
Duas decisões que valem registro:

- o casamento olha **enunciado + alternativa correta + `why`**, nunca as erradas.
  A primeira tentativa usava o texto inteiro e etiquetou a questão de **cascata**
  como `metodos-ageis` — numa questão boa da FGV os distratores são os conceitos
  vizinhos, e eles envenenam a etiqueta;
- abaixo de um mínimo de evidência a questão fica **sem** `sub`. Medindo à mão
  por faixa, o casamento fraco acertava ~1 em 3; rótulo errado é pior que rótulo
  nenhum, porque corrompe a sessão `./quiz.py <microtópico>` e a contagem de
  cobertura. Precisão da faixa gravada, aferida em amostra: ~94%.

Fecha com a obrigatoriedade: `SUB_OBRIGATORIA_APOS` (403) faz o `valida.py`
**bloquear** questão nova sem `sub`. O número é um índice porque questão nova é
sempre anexada ao fim — conforme o acervo antigo for etiquetado, ele baixa; em 0,
a regra vale para o banco inteiro. `./quiz.py --tags` passou a listar o
vocabulário inteiro por bloco (é a referência para escolher o valor), e
`comando-negativo` ganhou `escopo: enunciado`: as palavras dele ("incorreta",
"exceto") aparecem o tempo todo dentro das explicações das erradas, e sem isso
ele casava com meio banco — chegou a etiquetar uma questão de IPv6.

## 2026-08-06 — `./fraquezas.py`: ranking de microtópicos para mirar a geração de questão

Faltava granularidade para responder "gere mais questões do que eu mais erro".
O bloco (`tag`) é grosso demais — `portugues` são 90 questões, e os sete erros
registrados no caderno estavam em sete assuntos diferentes (regência, orações
subordinadas, referenciação, pessoas do discurso…). As três fontes de sinal
existiam mas não se conversavam: o `historico.json` indexa por questão (não por
conceito), o caderno de erros é prosa, e a `sub` cobria só cinco recortes de TI
— nenhum nos blocos onde ele mais erra.

O vocabulário das subtags saiu de duas cópias (`valida.py` e `quiz.py`) para
uma fonte única, **`subtags.py`**, que ganhou nove microtópicos derivados um a
um das entradas que já estavam no caderno, mais `kw` distintivas e o campo
`blocos` — sem esse recorte a contagem de cobertura inflava com português solto
em questão de TI ("alta coesão", "integridade referencial", o COMMIT do banco).

O **`./fraquezas.py`** cruza as três fontes: erros vêm do caderno (é lá que o
erro está etiquetado, pela nova linha `- **sub:**`), a causa vem do histórico
do quiz pela junção no marcador `<!-- auto <id> -->`, e a cobertura vem dos dois
bancos. `--prompt` monta o briefing de geração já escolhendo o FORMATO pela
causa, na mesma trava anti-vício do `--stats`: erro conceitual pede questão
direta de definição, erro de leitura pede aplicação com a quase-certa reforçada.

Encaixes no que já existia: o `quiz.py` escreve a linha `- **sub:**` sozinho
quando a questão errada tem etiqueta; `--dica`/`--resumo`/`--apostila` de um
microtópico caem no arquivo do bloco que cobre o assunto (Cap. 2 entrou no mapa
para `comando-negativo`); `./quiz.py <microtópico>` cai na busca por
palavra-chave enquanto não houver questão etiquetada; e o `./valida.py` passou a
cobrar etiqueta fora do vocabulário também no caderno de erros.

## 2026-07-29 — README/roteiro: reclassifica a distribuição da Dataprev 2024 e adiciona o `./estudar.sh`

A tabela "Onde a prova se decide" (README) e a "Distribuição real do Módulo
II" (roteiro, seção 1) tinham duas fontes divergentes por trás: uma vinha de
`notas/dataprev2024-mapa.md` (que já avisa, no topo, para não ser usada como
gabarito de proporção) e a outra de uma classificação mais antiga com 9
categorias, três delas (Noções de Informática, Arquitetura de Computadores,
Sistemas de Informação) sem tag nenhuma no quiz. As 30 questões específicas
foram relidas uma a uma direto no PDF (`provas/dataprev2024.pdf`) contra o
texto do edital: Engenharia de Software 9, Banco de Dados/BI 6, Programação
6, Arquitetura de Software 4, Segurança 3, Redes 2 — fecha as 30. O achado
extra: das 2 questões "de rede", só a de X.800/OSI é realmente fora do
edital; a outra (Internet/intranet/extranet/portal) é o item 4 do próprio
edital de Desenvolvimento de Sistemas, então a alegação "Redes cai fora do
edital" valia só pra 1 questão, não 3. `roteiro-dataprev-2026.md` ganhou uma
nota de revisão datada; o plano de dias (seções 4+) não mudou.

Também documentado no README: `./estudar.sh`, criado em `fa53f7f` (depois da
última revisão do README) e hoje apontado pelo próprio `status.py` como o
atalho principal do dia — abre a apostila no zathura + roda o quiz.

## 2026-07-26 — auditoria da apostila: fecha 10 achados, dois deles erros factuais

Auditoria completa pelo `VERIFICAR-APOSTILA.md` (sete frentes). Veredito: dava
para estudar pela apostila como estava, mas com **dois erros que valem ponto**.

### Os dois erros factuais

**1. O Perfil 3 TEM Banco de Dados no edital.** A caixa `edital` do capítulo
5 (e o `resumo/banco-dados.md`) afirmava que o Perfil 3 "não tem Banco de
Dados como disciplina" e que a lista fechada era do Perfil 2. Falso: o Anexo I
traz, dentro de `PERFIL 3: DESENVOLVIMENTO DE SOFTWARE`, uma disciplina
`BANCO DE DADOS` com **17 itens**. Consequência de cobertura: **metadados**
(item 5) e **avaliação de modelos de dados** (item 16) não tinham uma linha
sequer no livro — ganharam subseção própria (§4.1.1 do resumo, duas caixas de
conceito na apostila). O que é mesmo do Perfil 2 (SGBD nomeados, item 7.1;
administração/backup, item 8) ficou dito com o número do item.

**2. LGPD art. 52, §6º — advertência não abre as três últimas sanções.** O
livro dizia que suspensão do banco, suspensão da atividade e proibição (X, XI,
XII) exigem "ao menos uma das anteriores" imposta antes. A lei exige uma dos
**incisos II a VI** (multa simples, multa diária, publicização, bloqueio,
eliminação) — a **advertência, inciso I, não conta**. Era distrator pronto da
banca ("já houvera advertência, logo pôde suspender") e o material mandava
marcar certo.

### Desatualizações e lacunas fechadas

- **Prazo de incidente (art. 48).** A lei diz "prazo razoável", mas a
  **Resolução CD/ANPD nº 15/2024** já fixou **3 dias úteis** (ANPD e titular)
  e **5 anos** de guarda do registro. O livro tratava "prazo com número" como
  distrator — hoje a alternativa com os 3 dias úteis é a verdadeira.
- **COBIT 2019:** faltavam os **6 princípios do sistema de governança** e os
  **3 do framework** — o número que a FGV troca. **ITIL 4:** as 34 práticas
  agora vêm com a repartição **14 + 17 + 3**.
- **Verificação × validação:** o par já tinha caído (ALERO 2026) e não estava
  explicado em nenhuma das quatro camadas — só citado na lista de "já caiu".
  Ganhou subseção, entrada no Apêndice B e duas questões.
- **Regulação de IA:** AI Act é **Regulamento (UE) 2024/1689, em vigor desde
  01/08/2024**; o PL 2338/2023 **ainda é projeto** (aprovado só no Senado, em
  10/12/2024). O corte cobrado é o *estado* de cada norma.
- **Critério de aprovação:** o edital exige, cumulativamente, 57,5 pontos **e
  não zerar nenhuma disciplina** (9.17). A segunda condição não aparecia — e
  ela mata a estratégia de abandonar um bloco do Módulo I.

### Precisão didática

Nielsen (aprendizado, eficiência, **memorabilidade**, erros, satisfação) foi
separado da ISO 9241-11 (**eficácia**, eficiência, satisfação); o alias no
`WHERE` deixou de ser chamado de "erro de sintaxe"; a duração de 4h da prova
passou a vir marcada como suposição (**o edital não a declara** — ele fixa só
portões às 12h30, permanência mínima de 2h e caderno nos últimos 30 min); e a
leitura do Crow's Foot trocou "de fora/de dentro", ambíguo em português, por
"o que encosta na entidade é o máximo".

### Razão conceito:estratégia

`13-orfaos` estava em 1 conceito para 4 pegadinhas, com a seção de IA/ML
reduzida a lista de pares sem mecanismo. Ganhou duas caixas de conceito
explicando **por que** a penalidade L1 zera e a L2 não, e **o que** muda em
cada tipo de drift. Nenhuma caixa de `pegadinha`, `jacaiu` ou `comosair` foi
removida.

### O guia de questões estava calibrado por números velhos

Ao verificar as 13 questões novas contra o banco e contra as provas reais,
apareceu um problema no próprio `CONTRIBUINDO-QUESTOES.md`: ele mandava
corrigir vícios **que já haviam sido corrigidos**. Dizia que a correta era a
mais longa em **62%** dos itens (está em **4%**; a prova real da FGV é que está
em 33%) e que o comando negativo era sub-representado (banco em **2,0%**, real
em **2,2%** — a defasagem fechou). Seguir o guia ao pé da letra hoje levaria a
alongar distratores e a forçar itens negativos sem necessidade, degradando o
banco. Os percentuais foram remedidos, datados, e o guia ganhou um aviso no
topo com o procedimento de remedição (`_metricas()` e `avisos_forma()` do
`valida.py`, aplicados a `banco.json` e `banco-provas.json` separadamente).

As 13 questões novas, por sua vez, não têm vício de forma: 0% de "correta é a
mais longa", 0% de absoluto só no distrator, gabarito espalhado em A–E, e o
`avisos_forma` não acusa nada nem na janela de 30 nem no escopo restrito às 13.
O enunciado ficou com mediana de 45 palavras contra 27 do banco e 61 do real —
mais perto da prova, que é o que a calibração 8.2 pede.

### Números

| | antes | depois |
|---|---|---|
| páginas | 151 | **158** |
| `conceito` | 71 | **78** |
| `pegadinha` | 116 | **119** |
| `comosair` / `jacaiu` / `edital` | 24 / 20 / 15 | 24 / 20 / 15 |
| `banco.json` | 390 | **403** |
| Apêndice B (pares) | 69 | **83** |

As 13 questões novas cobrem o conteúdo acrescentado e os três subtópicos que
o `cobertura.py` apontava como rasos: **blockchain** (1 questão sob a tag),
**TCP × UDP** (2) e **JSF/Primefaces** (0). `./valida.py` íntegro; compilação
sem `LaTeX Warning` e sem referência indefinida, e **sem nenhuma caixa
`Overfull` nova** (13 antes, 13 depois — as mesmas, nos mesmos capítulos).

## 2026-07-26 — roteiro v3: replanejado para começar em 27/07, em 11 semanas

Inscrição feita — a pendência saiu do `README.md` e do roteiro. E o cronograma
foi refeito para partir de **amanhã, 27/07**, em vez de 13/07.

### 13 semanas viraram 11, sem perder conteúdo

De 27/07 (segunda) a 11/10 (domingo da prova) são **exatamente 77 dias = 11
semanas**, sem sobra nem falta. O que encolheu **não foi a fundação**: foram a
folga de revisita e a antiga semana 12, que tinha seis dias só de revisão. A
v2 gastava quatro semanas no Bloco 1; a v3 faz em três, mais densas.

Nada de conteúdo saiu. Conferido item a item contra a v2 — requisitos,
modelagem, SQL, SOLID, padrões, testes, DevOps/Git, JSON/XML/REST/mensageria,
UX/CMS, reuso/UDDI e a varredura do Anexo I continuam todos no plano. As quatro
leis entram nas cinco primeiras quintas, antes de qualquer revisita.

| | v2 | v3 |
|---|---|---|
| Início | 13/07 | **27/07** |
| Semanas | 13 | **11** |
| Simulados | 14 | **11** (dez aos domingos + o último na quarta da prova) |
| Bloco 1 (Fundação) | 4 semanas | 3 |
| Bloco 2 (Carga máxima) | 6 semanas | 6 |
| Bloco 3 (Varredura + reta final) | 3 semanas | 2 |

Dias de conteúdo por bloco: eng-software 7, segurança 6, banco-dados 5,
programação 5, java 5, bi 4, frontend 4, governança 4, arquitetura 3, redes 3,
órfãos 3 — o eixo duplo no topo, como o Apêndice A manda.

### O `progresso.csv` foi regerado, e os dois arquivos são checados um contra o outro

O CSV é o que a tooling lê (`status.py`, `quiz.py --hoje`, `--pendentes`,
`garantir_csv`), e o markdown é o que você lê — escritos separadamente, eles
podem divergir em silêncio. Cross-check rodado: **77 dias em cada, mesmas datas
na mesma ordem, dia da semana correto em todos, 11 simulados nos dois**. O
`--pendentes` volta a dizer "em dia com o roteiro", porque o plano começa amanhã.

### Um princípio que estava mentindo

O `README.md` afirmava "nenhum tópico mais de 2 dias seguidos" — e a v2 já
contrariava isso, com semanas temáticas de cinco dias em Java, Redes, Segurança,
BI, Frontend e Governança. O texto agora descreve o que o plano faz de verdade:
na semana temática o bloco domina, e o reencontro vem pelas revisitas marcadas,
pelos simulados de domingo e pelo `--erradas`.

## 2026-07-26 — review do repo: o buraco de 10 pontos, um bug que falsificava o relatório de cobertura, e a Lei 15.352 conferida na fonte

Review completo do repositório, fechando os gaps, defeitos e riscos que ele
apontou. `banco.json`: **356 → 390** questões; utilizáveis no quiz: **768 →
802**. Apostila: **150 → 151 páginas**.

### O risco número 1 era só risco: a Lei 15.352/2026 está certa

A atualização da ANPD estava afirmada em quatro camadas (apostila, resumo,
dicas, `banco-provas.json`) com trava no `valida.py` — e a trava garante
consistência interna, não veracidade. Conferido na fonte: a **Lei 15.352, de
25/02/2026** existe, veio do **PLV 13/2025, originado da MP 1.317/2025**, e o
art. 55-A tem a redação que o material descreve, **inclusive o "nos termos da
Lei nº 13.848, de 25 de junho de 2019"**. Nada a corrigir.

O que a conferência revelou foi outra coisa: **o ECA Digital não existia no
repo** (`grep` não achava uma menção). A **Lei 15.211/2025**, em vigor desde
**17/03/2026**, é *a razão* de a ANPD ter virado agência — foi ela que lhe deu
a competência de regulamentar as plataformas. Entrou nas três camadas de
conteúdo, rotulada como **fora do rol do edital**, no mesmo espírito com que o
material trata redes.

### O buraco de 10 pontos: "Temas coringa genuínos"

O `cobertura.py` apontava esse subtópico com **0 questões** — o único
DESCOBERTO do livro. Ele cobre justamente **Noções de Informática (2q) +
Arquitetura de Computadores (1q) + Sistemas de Informação (1q)** da Dataprev
2024: 4 questões, **10 pontos**, sem uma única questão para treinar. Entraram 5
(SPT × SIG × SAD × SIE, UC × ULA, hierarquia de memória, ERP × CRM × SCM,
pipeline como ganho de vazão e não de latência).

### O relatório de cobertura estava mentindo em 12% das keywords

Investigando por que as questões novas não registravam, apareceu um bug no
`cobertura.py`: a apostila escreve lista de definição como `\textbf{Termo:}`,
com o **dois-pontos dentro das chaves**, e o extrator guardava a keyword como
`"arquitetura de computadores:"`. Com a pontuação colada, ela só casaria com
uma questão que também tivesse o `:` ali — ou seja, nunca. Eram **313 de 2.698
keywords (12%)** mortas, subcontando a cobertura do livro inteiro. Corrigido o
`strip`, os subtópicos DESCOBERTOS do material caíram de 1 para **0**.

### Inglês: o pool mais fino contra o peso

12 pontos, empatado com Português como maior disciplina isolada, e só 37
questões utilizáveis — das quais as 26 originais rodavam sobre **7 textos-base**
(4 questões cada). Na segunda passada você reconhece o texto, não treina
interpretação. Entraram **4 textos novos × 4 questões** (observabilidade,
privacy by design, acessibilidade, dívida técnica), no formato da casa: ideia
principal, referência pronominal, conectivo e vocabulário em contexto.

### Frontend e governança, os dois menores pools de específicos

6 de frontend (CORS, localStorage × sessionStorage × cookie, CSR × SSR,
`position: absolute`, delegação de eventos, `v-if` × `v-show`) e 7 de
governança (SLA × OLA × contrato de apoio, os 6+3 princípios do COBIT 2019,
**PMBOK 7** — que o material só cobria na 6ª edição —, artefatos e compromissos
do Scrum, resposta a riscos, pool × lane, as 34 práticas do ITIL 4).

### O `valida.py` pegou o lote novo duas vezes

Vale registrar, porque é o argumento a favor de rodá-lo sempre: das 34 questões
geradas, ele acusou **absoluto só em distrator em 8** ("elimine a que tem
`apenas`" resolveria sem saber o conteúdo) e **correta mais longa em 43%** da
janela. Os dois vazamentos foram corrigidos — ora tirando o absoluto incidental,
ora pondo um legítimo na correta; ora encurtando a correta, ora engordando o
distrator mais forte.

### Dois ajustes no próprio `valida.py`

- **Ratio com piso.** O aviso "correta ≥1,7× a média das erradas" acusava a #41,
  cujas alternativas são termos secos (`dice`, `slice`, `drill-down`, `pivot`,
  `roll-up`): 10 contra média 5,25 dá 1,9× com **5 caracteres** de diferença.
  Não havia o que encurtar. Agora o ratio só mede quando as erradas já são
  frases e a correta tem folga real em caracteres.
- **Aviso permanente saiu do balde dos acionáveis.** A `mpu` Q41 tem as
  alternativas em **figura** (notação BPMN); ela já está fora do sorteio e nunca
  vai ter texto. Ficava na lista de avisos a cada execução, ensinando a ignorar
  a lista. Virou uma linha própria, discreta, rotulada como esperada.

### Caderno de erros: a única anotação manual estava errada

`erros/portugues.md` tinha uma correção embolada ("a oração principal é a que
não possui o conectivo ou na reduzida é a que não encontra-se no verbo
nominal") e com erro de próclise no meio. Num caderno de Português, correção
errada re-ensina o erro a cada revisão. Reescrita a partir da fonte (FGV
Dataprev 2024 Q1), e desdobrada em **duas** entradas, porque eram duas lições:
o par **substantiva subjetiva × adjetiva** e o **comando negativo** — a questão
pedia a INCORRETA e foi marcada uma afirmativa verdadeira.

### Miudezas

- `resumo/seguranca.md`: a seção **5.1 (X.800)** estava depois da 6. Reordenada.
  (Nos outros cinco resumos as seções `X.1` já estavam no lugar certo — o
  relatório inicial do review exagerou nesse item.)
- Contagens propagadas em `README.md`, `resumo/README.md` e
  `CONTRIBUINDO-QUESTOES.md`.

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

### Três incoerências que o capítulo de legislação deixou para trás

Fechado o capítulo, sobraram três pontas soltas — nenhuma de conteúdo novo,
todas de **coerência**: o material dizendo uma coisa em um lugar e outra dois
parágrafos abaixo. **150 páginas, sem alteração na contagem.**

**"A FGV adora a distinção controlador × operador" era palpite, não dado.** A
frase estava no `\peso` de abertura do capítulo, no blockquote do edital em
`resumo/legislacao.md` e sob "O que mais cai" em `dicas/legislacao.md` — e
contradizia a `jacaiu` do próprio capítulo, que põe o par em "no nosso banco
(previsto pelo edital, ainda não visto na amostra de provas)". A `jacaiu` está
certa: nas 422 questões reais **os dois termos nunca aparecem juntos**. Há
quatro ocorrências isoladas e metade nem é LGPD — em `cnsal-ads` Q47
"controlador" é objeto de um diagrama de sequência e em `cnsal-bd` Q61
"operador" é operador lógico de `WHERE`. Nos dois hits de LGPD o termo aparece
sozinho, dentro de outro assunto (`dataprev2024` Q39, conciliação do art. 52,
§7º; `tjrj1` Q61, art. 20). No lugar do palpite entrou o que a banca de fato
cobrou nas 8 questões do nosso recorte: classificação na LAI, art. 154-A,
sanções do Marco Civil, sanções da LGPD e ANPD × CNPD (Dataprev 2024);
princípio da adequação, art. 20 e IA generativa × LGPD (TJ-RJ). O par
controlador × operador **continua no material** — é edital, e o nosso banco o
cobra —, agora rotulado como o que é: previsto, sem precedente da banca.

**O detector de drift não protegia a atualização de 2026.** O `FATOS_CANONICOS`
do `valida.py` guardava o STF de 26/06/2025 nas quatro camadas, mas a Lei
15.352/2026 tinha acabado de entrar em três camadas **sem trava nenhuma** — se
alguém reescrevesse uma delas e a ANPD voltasse a ser só "autarquia", nada
avisaria. Exatamente o buraco que o ITEM 5 criou o detector para tapar. Entrou
como `("ANPD agencia (Lei 15.352/2026)", r"15\.?352", ("apostila", "resumo",
"dicas"))` — três camadas, não quatro, porque `_texto_camadas()` monta `"banco"`
lendo só o `banco.json` e a citação nova vive no `banco-provas.json`. Conferido
nas três, e conferido que na quarta não casaria.

**O mapa que abre a `\section{LGPD}` tinha ficado atrás do próprio capítulo.**
O `itemize` ainda dizia "ANPD (autarquia)" e listava **cinco** sanções,
enquanto as subseções logo abaixo já ensinavam *Agência* vinculada ao MJSP e o
regime completo do art. 52. O `itemize` **não foi apagado** — a redundância
entre mapa e desenvolvimento é repetição espaçada, é de propósito. Os dois
bullets só foram alinhados: a ANPD ganhou o desenho de 2026 e as sanções
passaram a ser as **nove em vigor** (incisos I--VI e X--XII; VII--IX vetados),
com a nota de que suspensão parcial, suspensão da atividade e proibição só
vêm depois de outra sanção no mesmo caso concreto (§6º). Reconferido no
Planalto: os incisos X a XII foram vetados em 2018 e **promulgados depois**,
pela Lei 13.853/2019.

Caixas do livro inalteradas — `conceito` 70, `pegadinha` 116, `jacaiu` 20,
`comosair` 24, `edital` 15. `./valida.py --strict` com a lista de avisos
idêntica ao baseline e sem `[drift]`; 13 *overfull hbox*, máximo 17,3pt.

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
