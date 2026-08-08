# Prompt pronto — lote de 400 questões para os blocos GERAIS

> **ARQUIVO ENCERRADO — o déficit é zero desde 07/08/2026.** As 30 questões que
> faltavam (18 de inglês, 12 de atualidades) foram geradas naquele dia: o pool
> hoje é **inglês 120, atualidades 60, português 129, RLM 64, legislação 68**,
> contra uma demanda de 120/60/120/50/50 para os 10 simulados. **Não gere lote
> de gerais** sem antes remedir — hoje só sobraria trabalho. O que continua
> valendo aqui é a **metodologia**: como dimensionar cota por microtópico, e as
> cinco regras do prompt (fonte primária com data para atualidades, conta
> conferida em RLM, texto-base próprio em inglês). O registro do que foi gerado
> está no `CHANGELOG.md` de 07/08.

Cole o conteúdo da seção "O prompt" numa conversa nova do Claude Code, dentro
deste repositório. O resto do arquivo é a memória de **por que** este lote existe
e com que números ele foi dimensionado — leia antes de mudar as cotas.

## Por que só os gerais

> **As cotas deste arquivo estão desatualizadas.** Elas foram dimensionadas
> antes das importações de 07/08/2026, que trouxeram 237 questões de blocos
> gerais em seis provas (NAV Brasil, CPRM ADS e Pesquisador, EPE e as duas da
> Receita Federal). **Português, RLM e legislação saíram do déficit** e não
> precisam de questão nova nenhuma; o buraco caiu de 137 para **30**, dividido
> entre inglês e atualidades. A metodologia e o rateio por microtópico
> continuam válidos — recalcule as cotas antes de usar, e deixe no lote apenas
> esses dois blocos.

Medido em 07/08/2026 **depois de todas as importações do dia**, contra a
demanda de **10 simulados** do roteiro (cada um com 70 questões: 40 gerais na
proporção do edital + 30 específicos):

| bloco | por simulado | precisa (10×) | pool hoje | déficit |
|---|---|---|---|---|
| inglês | 12 | 120 | 102 | **+18** |
| atualidades | 6 | 60 | 48 | **+12** |
| português | 12 | 120 | 129 | −9 |
| RLM | 5 | 50 | 65 | −15 |
| legislação | 5 | 50 | 68 | −18 |

A tabela original, que gerou as cotas abaixo, era esta (inglês 53, português
90, atualidades 35, RLM 35, legislação 66 — déficit somado de 137).

Os **específicos não têm déficit**: rateando a distribuição real da Dataprev 2024
(30 questões do Módulo II, Apêndice A) pelos blocos do repo, o pior caso é
arquitetura em −1 e eng-software em −4; banco-dados sobra 47. Gerar específico
agora seria trabalho sem retorno.

A conta do déficit é de **questões distintas**: o `montar_simulado()` prioriza
quem nunca apareceu e só repete quando o pool fresco do bloco acaba — é ele que
avisa "pool curto" no fim do simulado.

> **100 por bloco passa da paridade de propósito.** Fechar o buraco exigiria
> 67+30+25+15 = 137. Com 100 em cada, inglês fica em 153 para uma demanda de 120
> e RLM em 135 para 50. A folga é o que permite 10 simulados sem repetir e ainda
> sobra para o quiz diário. Se quiser encolher, corte proporcionalmente **de
> baixo para cima** na tabela de cotas — os microtópicos zerados vêm primeiro.

## As cotas por microtópico

Não é "gere 100 de inglês": dentro de cada bloco a distribuição hoje é torta, e
há microtópico com **zero** questão. As cotas abaixo já corrigem isso (o número
entre parênteses é quantas existem hoje).

**Inglês — 100.** Precisa de ~30 textos-base novos; a FGV pendura 3–4 itens no
mesmo texto, e o banco já faz assim (o texto vai inline no campo `q`).

| microtópico | hoje | gerar |
|---|---|---|
| `julgamento-afirmativas` | 0 | 20 |
| `conectivos` | 2 | 20 |
| `verbos-modais` | 6 | 15 |
| `vocabulario-contexto` | 14 | 15 |
| `referencia-pronominal-ingles` | 12 | 15 |
| `compreensao-global-ingles` | 15 | 15 |

**Português — 100.** Só 11 das 90 atuais são originais: o bloco vive de prova
real, e é por isso que 57 estão sem `sub`.

| microtópico | hoje | gerar | | microtópico | hoje | gerar |
|---|---|---|---|---|---|---|
| `crase` | 0 | 12 | | `reescrita-significacao` | 1 | 8 |
| `pontuacao` | 0 | 12 | | `referenciacao` | 2 | 6 |
| `ortografia` | 0 | 10 | | `conectivos` | 1 | 6 |
| `concordancia-verbal` | 1 | 10 | | `interpretacao-texto` | 4 | 6 |
| `concordancia-nominal` | 1 | 10 | | `classes-palavras` | 10 | 4 |
| `colocacao-pronominal` | 1 | 8 | | os 4 do caderno¹ | — | 8 |

¹ `regencia`, `oracoes-subordinadas`, `pronomes-relativos`, `pessoas-do-discurso`
— 2 cada. São erros registrados em `erros/portugues.md`: gere mirando o erro
exato anotado lá, e leia a linha `- **E:**` da entrada antes de escrever.

**RLM — 100.**

| microtópico | hoje | gerar | | microtópico | hoje | gerar |
|---|---|---|---|---|---|---|
| `probabilidade` | 0 | 12 | | `progressoes` | 1 | 8 |
| `porcentagem` | 0 | 12 | | `equivalencias-logicas` | 1 | 8 |
| `conjuntos-inclusao-exclusao` | 0 | 10 | | `argumentacao-validade` | 1 | 8 |
| `analise-combinatoria` | 1 | 10 | | `quantificadores` | 1 | 8 |
| `juros-simples-compostos` | 1 | 10 | | `razao-proporcao` | 2 | 6 |
| `matrizes` | 0 | 8 | | | | |

**Atualidades — 100.**

| microtópico | hoje | gerar | | microtópico | hoje | gerar |
|---|---|---|---|---|---|---|
| `atualidades-socioambiental` | 0 | 20 | | `llms-generativos` | 5 | 10 |
| `ia-aplicada-cenarios` | 1 | 15 | | `vies-variancia` | 5 | 8 |
| `metricas-ml` | 2 | 12 | | `ia-esg` | 6 | 6 |
| `etica-ia` | 3 | 12 | | `fundamentos-ia` | 7 | 5 |
| `regulacao-ia` | 3 | 12 | | | | |

---

## O prompt

> Estou ampliando o `banco.json` para cobrir a demanda de 10 simulados. O plano,
> as cotas por microtópico e a medição que as justifica estão em
> **`GERAR-LOTE-GERAIS.md`** — leia esse arquivo primeiro, e depois
> **`CONTRIBUINDO-QUESTOES.md`** (processo completo) e a seção "Estilo de questão"
> do `CLAUDE.md`.
>
> Gere **100 questões para cada um dos quatro blocos gerais** — inglês,
> português, RLM e atualidades — respeitando a cota por microtópico da tabela.
> Total: 400.
>
> **Trabalhe em lotes de 25 questões**, de um microtópico por vez. Ao fim de cada
> lote: rode `./valida.py --novas 25`, corrija o que ele acusar, e só então siga
> para o próximo. Não emende os 400 antes de validar — aviso de forma
> (correta mais longa, gabarito concentrado, absoluto só no distrator) só é
> barato de corrigir enquanto o lote é pequeno.
>
> Regras que este lote específico exige, além do guia:
>
> 1. **`sub` é obrigatório** e o `./valida.py` bloqueia sem ele. Use o valor
>    exato da cota; `./quiz.py --tags` lista o vocabulário. Uma questão só entra
>    com a `tag` do bloco (`ingles`, `portugues`, `rlm`, `atualidades`) — a
>    `tag` nunca vira o microtópico.
>
> 2. **RLM: a conta tem que fechar.** Antes de escrever as alternativas, resolva
>    o item e confira o resultado; ponha o cálculo no `why`, em uma linha, para
>    ser auditável depois. Os distratores devem ser os **erros de conta reais**
>    (esquecer de dividir pelo total, somar taxas em vez de compor, trocar
>    permutação por combinação) — não números aleatórios. Gabarito de RLM errado
>    é o pior defeito possível: treina a conta errada.
>
> 3. **Atualidades: fonte primária com data.** Regulação de IA, ESG e pauta
>    socioambiental mudam de status; confirme em fonte oficial (texto do PL/lei,
>    site do órgão, documento da COP) antes de fixar o gabarito, e cite no `why`
>    o que está **em vigor** contra o que está **em tramitação** — é exatamente aí
>    que a FGV arma a pegadinha. Se um fato não puder ser confirmado, troque o
>    tema em vez de escrever o plausível.
>
> 4. **Inglês: ~30 textos-base novos**, cada um com 3–4 itens, no formato que o
>    banco já usa (texto inline no `q`, entre aspas, precedido de "Read the text
>    below and answer the question."). Escreva os textos você mesmo, sobre temas
>    de TI e serviço público — não copie trecho de publicação real. Cada item
>    pendurado num texto tem que ser respondível **só com aquele texto**.
>
> 5. **Português: idem para os textos.** `crase`, `pontuacao`, `ortografia`,
>    `concordancia-*` e `colocacao-pronominal` cabem em frase solta (formato
>    clássico FGV, comando terminando em `:`); `interpretacao-texto`,
>    `referenciacao` e `reescrita-significacao` precisam de um parágrafo-base.
>
> 6. **Não repita o que já existe.** Antes de escrever um microtópico, rode
>    `./quiz.py <microtópico>` para ver o que o banco já cobre daquele assunto,
>    e escolha ângulos diferentes.
>
> Ao terminar tudo: rode `./valida.py` (tem que fechar "tudo integro"),
> `./valida.py --novas 100` para medir o vazamento de forma do lote grande, e
> me diga quantas ficaram em cada microtópico contra a cota.

---

## Depois do lote

- `banco.json` sai de 403 para ~803 questões. **Nada a fazer no
  `SUB_OBRIGATORIA_APOS`** (403): as novas entram todas com `sub` porque a
  validação bloqueia — o número só desce quando o acervo *antigo* for etiquetado.
- Reveja `./fraquezas.py`: com o pool novo, a coluna `banco` muda e microtópico
  que hoje aparece com 2–3 questões sai da faixa de alerta.
- O contador de questões no `README.md` é conferido pelo `valida.py`
  (aviso de drift `[drift] README.md diz 'N questoes originais'`) — atualize.
