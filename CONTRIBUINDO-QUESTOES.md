# Como contribuir questões para `banco.json`

Guia obrigatório para toda questão **original** nova (não vale para
`banco-provas.json`, que é texto real de prova). Destilado da auditoria do
banco (Bloco V) comparando as 259 originais com 379 questões reais da FGV.
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

- **A correta não pode ser a mais longa.** Alvo do banco ~20%; hoje está em 62%.
  Encurte a correta ou alongue os distratores até ficarem de tamanho parecido.
- **Absoluto não só no distrator.** Se usar "sempre/nunca/apenas", não deixe
  esse termo aparecer *só* nas erradas — senão "elimine a que tem absoluto"
  resolve. Ou tire o absoluto, ou coloque um numa alternativa que não seja errada por causa dele.
- **Sem reuso literal do enunciado** na alternativa correta (não copie o trecho
  que já entrega a resposta).
- **Varie a posição do gabarito.** A distribuição do `ans` já foi uniformizada
  (A–E ≈ 20% cada); não concentre em B/D. Rode `valida.py` e veja o aviso de
  "gabarito concentrado".

## 4. Proporção de cenário aplicado (calibração 8.2)

As provas reais da FGV têm enunciado ~2,4× mais longo que o banco (mediana 59
palavras × 19) e são **mais aplicadas**: ~32% de definição direta contra ~58%
no banco. Ao criar questão nova:

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
- Use mais **comando negativo** ("Assinale a INCORRETA", "a que **NÃO**…",
  "EXCETO"): a FGV real usa ~4% dos itens; o banco quase não usa (1). É um tipo
  de item legítimo e sub-representado.
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
- **Preencha o `sub`** sempre que a questão tiver um recorte transversal (veja
  abaixo). É o único campo opcional que ganha uso de verdade — os outros dois
  saíram da documentação por não terem nenhum.

## Schema

```json
{
  "tag": "<bloco>",
  "sub": ["uml"],               // opcional (subtag) — preencha quando couber
  "q": "<enunciado>",
  "alts": ["<a>", "<b>", "<c>", "<d>", "<e>"],
  "ans": 0,
  "why": "<por que a correta é certa>",
  "erradas": {"1": "<...>", "2": "<...>", "3": "<...>", "4": "<...>"}
}
```

> **Dois campos saíram daqui: `apostila` e `status`.** Eram opcionais e
> terminaram com **0 de 356** questões cada um. O `apostila` (ex.: `"§10.5"`)
> nunca fez falta porque o `ref_apostila()` do `quiz.py` já cai no mapa
> bloco→capítulo quando o campo não existe; o `status` (`ok`/`revisar`/
> `ambigua`/…) era instrumento da auditoria do banco, que terminou. O
> `valida.py` continua aceitando os dois sem reclamar, então nada quebra se
> você quiser usá-los um dia — mas campo documentado que ninguém preenche é
> dívida, e a documentação deixa de pedir os dois.

`ans` é 0–4; as chaves de `erradas` são os índices das 4 alternativas que **não**
são o gabarito. Blocos (`tag`) disponíveis: os mesmos de `erros/`.

### Campo `sub` (subtag) — recorte de estudo, não bloco

`sub` é uma **lista opcional** que dá um recorte transversal à questão sem tirá-la
do bloco. Vocabulário fechado (validado por `valida.py`, sem bloquear):
`padroes-projeto`, `uml`, `java-moderno`, `git-devops`, `leitura-codigo`.

A `tag` **continua sendo o bloco** e é ela que alimenta o roteiro, o
`progresso.csv`, o peso do simulado (geral × específico), o `erros/<tag>.md`, o
`--stats` e o `historico.json`. A `sub` só afeta o **filtro do quiz**
(`./quiz.py uml`) e o `--dica`/`--resumo`/`--apostila`. Por isso nunca troque a
`tag` de uma questão para criar um recorte: acrescente `sub`.

**Regra do lote novo:** toda questão gerada daqui em diante preenche a `sub`
quando o tema couber num dos cinco recortes. Hoje são 58 de 356, e o último
lote não acrescentou nenhuma — foi assim que `./quiz.py uml` virou um filtro
que devolve menos do que existe. **Não há passe retroativo** nas questões
antigas: o trabalho é grande e o ganho, marginal.
