# Como contribuir questões para `banco.json`

Guia obrigatório para toda questão **original** nova (não vale para
`banco-provas.json`, que é texto real de prova). Destilado da auditoria do
banco (Bloco V) comparando as originais com as questões reais da FGV.

> **Os números de calibração deste guia apodrecem.** Os que aparecem abaixo
> foram remedidos em **26/07/2026**, sobre 403 questões originais e 422 reais.
> Antes de agir sobre qualquer percentual daqui, refaça a medição — as funções
> `_metricas()` e `avisos_forma()` do `valida.py` fazem o cálculo, e basta
> aplicá-las a `banco.json` e a `banco-provas.json` separadamente. Corrigir um
> vício que já foi corrigido piora o banco.
Complementa a seção "Estilo de questão" do `CLAUDE.md` — aqui está o processo
inteiro; lá, o resumo do estilo.

> **Regra zero — não inventar.** Não crie questão, dado, número, artigo de lei,
> versão de norma ou "já caiu em tal prova" sem base verificável. Se faltar
> base, **pare e avise o Lucas** em vez de preencher com plausível. Gabarito ou
> explicação errada treina o reflexo errado — é pior que não ter a questão.

## 1. Ancoragem em fonte primária (não no resumo do repo)

A resposta tem de sair de uma **fonte externa canônica**, não de um trecho do
`resumo/` ou da `apostila/`. Antes de fixar o gabarito, confira contra:

- **Norma/lei:** o texto do artigo (LGPD 13.709/2018, MCI 12.965/2014, LAI
  12.527/2011, Lei 12.737/2012), e a jurisprudência quando ela mudou a regra
  (ex.: STF 26/06/2025, Temas 987 e 533, sobre o art. 19).
- **Padrão técnico:** RFC (ex.: 1918 para faixas privadas), OWASP Top 10 **2025**
  (a edição vigente) e **2021** (a que a Dataprev 2024 cobrou e que ancora as
  questões já no banco), GoF (os 23 padrões), UML 2.x, SQL padrão.
  > **OWASP: diga a edição no enunciado.** Desde a publicação final da Top
  > 10:2025 (jan/2026) convivem duas numerações válidas, e elas divergem em
  > posição *e* em nome (o SSRF virou parte do A01; A09 trocou *Monitoring* por
  > *Alerting*). Questão que só diz "segundo o OWASP Top 10" e cobra **posição
  > ou nome de categoria** fica ambígua — nomeie o ano, como fazem a #272
  > ("Na classificação do OWASP Top 10 2021…") e a #274. A #37 pode ficar sem
  > ano porque pede o **conceito** (injeção), que é categoria nas duas edições.
- **Framework oficial:** ITIL 4 (SVS, cadeia de valor, 7 princípios), COBIT 2019
  (EDM + APO/BAI/DSS/MEA), PMBOK (grupos de processo × áreas), Scrum Guide atual.
- **Edital do Perfil 3** para saber o recorte cobrado.

Se a única "fonte" da resposta for uma frase do próprio material de estudo, a
questão é **circular** — reancorе na fonte primária ou descarte.

O `why` pode comentar o comportamento da banca ("a FGV troca X por Y"), mas
**não** use "caiu na Dataprev 2024" como se fosse prova de nada, a menos que
esteja confirmado em `banco-provas.json`/PDF oficial.

## 2. Distrator ancorado em erro conceitual real

Cada uma das 4 erradas deve corresponder a uma **confusão que um candidato
realmente comete** — não a enchimento óbvio. Puxe o mecanismo dos sete padrões
de distrator (`dicas/tecnica-fgv.md`, Cap. 2 da apostila) e do glossário de
pares que a FGV inverte (Apêndice B, `20-glossario-pegadinhas.tex`) ou de
`erros/*.md`:

- inversão de par (LEFT/RIGHT, WHERE/HAVING, verificação/validação, incidente/problema…)
- troca de acrônimo (ACID↔CAP, CID↔ACID, EDM↔PBRM)
- absoluto (sempre/nunca/exclusivamente/garante) — ver regra 3
- extrapolação além do enunciado
- troca de número/ordem (prazos LAI, portas, fórmula de PA)
- contradição interna / distrator inventado

**Meta:** no máximo **2** distratores por questão podem ser de "enchimento"
(termo inventado, absurdo). Se 3+ das 4 erradas forem elimináveis sem saber o
conteúdo, a questão virou de duas alternativas — reforce os distratores. Inclua
pelo menos uma **"quase certa"** (acerta a primeira metade, erra no detalhe
final) quando o tema permitir.

## 3. Proibição dos vazamentos de forma

Um gerador de IA vaza a forma: dá pra acertar pela mecânica da alternativa, sem
saber o conteúdo. `valida.py` (função `avisos_forma`) monitora isso no banco
inteiro. Numa questão nova, respeite:

- **A correta não pode ser a mais longa.** Medido em 26/07/2026: o banco está em
  **4%** e a prova real da FGV, em **33%**. Ou seja, o problema histórico
  (62%) **já foi corrigido** — não alongue distrator para "consertar" o que não
  está quebrado. O que se exige da questão nova é só não ser mais um caso: se a
  correta ficou a mais longa do item, encurte-a ou alongue os distratores.
- **Absoluto não só no distrator.** Se usar "sempre/nunca/apenas", não deixe
  esse termo aparecer *só* nas erradas — senão "elimine a que tem absoluto"
  resolve. Ou tire o absoluto, ou coloque um numa alternativa que não seja errada por causa dele.
- **Sem reuso literal do enunciado** na alternativa correta (não copie o trecho
  que já entrega a resposta).
- **Varie a posição do gabarito.** A distribuição do `ans` já foi uniformizada
  (A–E ≈ 20% cada); não concentre em B/D. Rode `valida.py` e veja o aviso de
  "gabarito concentrado".

## 4. Proporção de cenário aplicado (calibração 8.2)

As provas reais da FGV têm enunciado **~2,3× mais longo** que o banco (mediana
de **61 palavras contra 27**, medido em 26/07/2026) e são **mais aplicadas**:
~32% de definição direta contra ~58% no banco (essa última razão é da auditoria
original e **não foi remedida**). Ao criar questão nova:

- Prefira **cenário/aplicação** (um contexto curto que sustente a pegadinha) a
  definição pura, principalmente nos blocos de peso alto (eng-software,
  banco-dados, arquitetura, segurança). Não infle o cenário além do necessário.
- Formato do enunciado por tipo:
  - **Conceitual/direta:** comando termina em `:` e alternativas em minúscula,
    continuando a frase (padrão clássico FGV). Use com parcimônia — o banco já
    tem definição direta demais.
  - **Cenário/julgamento I-II-III/leitura de código/legislação:** comando
    explícito ("Assinale a alternativa correta"), alternativas em frases
    completas e maiúsculas.
- **Comando negativo** ("Assinale a INCORRETA", "a que **NÃO**…", "EXCETO"): a
  FGV real usa em **2,2%** dos itens e o banco, em **2,0%** — a defasagem
  histórica foi fechada. Continue usando o formato, mas **sem forçar**: um lote
  pequeno com muitos negativos distorce o conjunto.
- Mantenha os pontos fortes já alinhados ao real: itens de **leitura de código**
  (Java/JS/CSS/SQL) e de **julgamento de afirmativas I/II/III**.

## 5. Explicação que reconstrói o raciocínio

- `why` (1–3 frases): **por que a correta é certa**, de forma analítica — o
  conceito, não só "é a alternativa A". Pode nomear o comportamento da banca.
- `erradas` (o mais importante — é o que se lê ao errar): para **cada** errada,
  explique o **erro conceitual**, não só afirme que está errada. **Varie a
  abertura** de cada frase (nada de "Distrator X:" repetido); teça o mecanismo
  dentro da explicação. Ensinar o conceito > apontar que a opção é falsa.

## 6. Trava anti-vício (respondível por quem domina o conteúdo)

Teste final antes de aceitar a questão: **quem domina o conteúdo mas ignora toda
técnica de eliminação consegue responder?** Se a questão só é respondível pela
mecânica (a correta é a mais longa, a única sem absoluto, a única sem inversão
de par), ela treina o vício, não o conhecimento. Reescreva até que o
conhecimento do tema — e não a forma das alternativas — seja o caminho para a
resposta.

## 7. Antes de commitar

- Rode **`./valida.py`** — erro bloqueia; aviso de forma é sinal de alerta sobre
  a questão nova.
- Registre o aprendizado do erro, quando houver, em `erros/<bloco>.md`.
- **Preencha o `sub`** — desde 06/08/2026 ele é **obrigatório** em questão nova
  do `banco.json` e o `./valida.py` **bloqueia** sem ele (veja abaixo).

## Schema

```json
{
  "tag": "<bloco>",
  "sub": ["uml"],               // OBRIGATORIO em questao nova (o valida.py bloqueia)
  "q": "<enunciado>",
  "alts": ["<a>", "<b>", "<c>", "<d>", "<e>"],
  "ans": 0,
  "why": "<por que a correta é certa>",
  "erradas": {"1": "<...>", "2": "<...>", "3": "<...>", "4": "<...>"}
}
```

> **Dois campos saíram daqui: `apostila` e `status`.** Eram opcionais e
> terminaram com **0 de 390** questões cada um. O `apostila` (ex.: `"§10.5"`)
> nunca fez falta porque o `ref_apostila()` do `quiz.py` já cai no mapa
> bloco→capítulo quando o campo não existe; o `status` (`ok`/`revisar`/
> `ambigua`/…) era instrumento da auditoria do banco, que terminou. O
> `valida.py` continua aceitando os dois sem reclamar, então nada quebra se
> você quiser usá-los um dia — mas campo documentado que ninguém preenche é
> dívida, e a documentação deixa de pedir os dois.

`ans` é 0–4; as chaves de `erradas` são os índices das 4 alternativas que **não**
são o gabarito. Blocos (`tag`) disponíveis: os mesmos de `erros/`.

### Campo `sub` (subtag) — recorte de estudo, não bloco

`sub` é a lista de **microtópicos** da questão — o recorte fino, dentro do
bloco. O vocabulário é **fechado, tem 167 valores e vive em `subtags.py`**
(fonte única, lida por `quiz.py`, `valida.py` e `fraquezas.py`). Duas origens:

- **derivada** (150) — é uma seção de `teoria/capitulos/*.tex`, ou da apostila
  nos capítulos em que ela é mais detalhada. Ou seja: a taxonomia do edital que
  já foi auditada, não um recorte inventado na hora;
- **curada** (14) — nasceu de **erro real** no caderno (`regencia`,
  `pessoas-do-discurso`, `comando-negativo`…), com nome e keywords à mão,
  normalmente mais finas que a seção correspondente do livro. Cinco delas
  (`padroes-projeto`, `uml`, `java-moderno`, `git-devops`, `leitura-codigo`)
  têm `dicas/<nome>.md` e `resumo/<nome>.md` próprios; as demais caem no
  arquivo do bloco que cobre o assunto.

`./quiz.py --tags` lista os 167 agrupados por bloco, com a contagem de questões
já etiquetadas — é a referência para escolher o valor.

**Obrigatoriedade.** Questão nova do `banco.json` **tem** que trazer `sub`: o
`valida.py` bloqueia (erro, não aviso) a partir do índice
`SUB_OBRIGATORIA_APOS`, hoje 403. O acervo anterior a esse índice ainda está
sendo etiquetado; conforme for, **baixe o número** — em 0, a regra vale para o
banco inteiro. Subtag fora do vocabulário continua sendo aviso, não bloqueio.

**Estado do acervo (06/08/2026):** 303 de 403 no `banco.json` e 194 de 422 no
`banco-provas.json` têm `sub` — 497 de 825 (60%), cobrindo 134 dos 167
microtópicos. As etiquetas vieram de casamento de palavra-chave sobre
**enunciado + alternativa correta + `why`**, com um mínimo de evidência; o que
não atingiu o mínimo ficou **sem** etiqueta de propósito. Precisão aferida à
mão em amostra: ~94%. Duas consequências práticas: (a) etiqueta errada existe e
é para ser corrigida quando você topar com ela estudando; (b) o que está sem
`sub` não é "erro do script", é falta de evidência — etiquete à mão.

> **Por que não casar no texto inteiro.** A primeira tentativa incluía as
> alternativas erradas e as explicações delas, e etiquetou a questão de
> **cascata** como `metodos-ageis`: numa questão boa da FGV os distratores são
> justamente os conceitos vizinhos, então eles envenenam a etiqueta. Se for
> reetiquetar algo, mantenha esse recorte.

A `tag` **continua sendo o bloco** e é ela que alimenta o roteiro, o
`progresso.csv`, o peso do simulado (geral × específico), o `erros/<tag>.md`, o
`--stats` e o `historico.json`. A `sub` afeta o **filtro do quiz**
(`./quiz.py normalizacao`), o `--dica`/`--resumo`/`--apostila` e o ranking do
`./fraquezas.py`. Por isso nunca troque a `tag` de uma questão para criar um
recorte: acrescente `sub`.

**Microtópico novo:** primeiro procure a seção correspondente no `teoria/` — se
existe, use o nome dela. Só escreva um recorte à mão quando o erro real não
couber em nada e o livro tratar o assunto de passagem. Em qualquer caso, `kw`
**distintivas**: keyword genérica infla a contagem de cobertura e faz o
`./fraquezas.py` achar que o assunto já está coberto.
