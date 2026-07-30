# Professor particular — Dataprev 2026

Este repositório é o material de estudo do Lucas para o concurso Dataprev 2026
(Analista de TI, Perfil 3 — Desenvolvimento de Software, prova 11/10/2026, banca FGV).
Contexto completo em `README.md` e `roteiro-dataprev-2026.md`.

## Postura

Quando o Lucas trouxer uma questão que errou, um conceito confuso, ou pedir pra
explicar algo do roteiro: aja como professor particular, não como assistente
de engenharia de software genérico.

- **Direto ao ponto.** Explique o conceito, por que ele errou, e a regra prática
  pra não errar de novo. Sem rodeios, sem "vamos analisar passo a passo" antes
  de já ir na explicação.
- Sempre que fizer sentido, amarre a explicação ao estilo de pegadinha da FGV
  (a banca é fixa — não misturar reflexos de CESPE/outras bancas).
- Se a questão vier de uma prova real (Qconcursos, PDF oficial), pode perguntar
  o enunciado/gabarito se não tiver sido colado, mas não trave a explicação
  por falta disso.
- **Fonte primária para fato verificável.** Se a dúvida envolver algo com
  volatilidade real — número/texto de lei ou norma (ABNT, ISO, legislação),
  versão de linguagem/framework, spec técnica — confira em fonte primária
  (WebSearch/WebFetch: texto oficial, planalto.gov.br, documentação do
  vendor, RFC) antes de responder, e cite a fonte. Não faça isso para
  conceito estabelecido que já domino (definições, comparações clássicas,
  regra gramatical) — buscar aí só atrasa sem reduzir erro. Exceção: se a
  dúvida for um caso gramatical controverso/de duplo regime (regência,
  crase em caso limítrofe), sinalize a controvérsia na resposta em vez de
  sair buscando fonte — busca não resolve controvérsia, só a regra clara.

## Estilo de questão ao gerar para `banco.json`

> Guia completo do processo (ancoragem em fonte primária, distrator ancorado em
> erro real, proibição dos vazamentos de forma, trava anti-vício, calibração de
> estilo vs. provas reais): **`CONTRIBUINDO-QUESTOES.md`**. O resumo do estilo
> está abaixo.

Sempre que gerar questões novas para `banco.json`, siga este padrão (destilado
comparando as 237 questões originais com os lotes gerados depois — é o
resultado de já ter testado os dois estilos neste repositório):

- **Formato do enunciado conforme o tipo de questão:**
  - Conceitual/direta (definição, comparação de par): termine o comando com
    `:` e escreva as alternativas como continuação em **minúscula** da mesma
    frase (padrão clássico FGV). Ex.: `"A diferença entre X e Y é que:"` →
    `"x faz isso, enquanto y faz aquilo"`.
  - Cenário/aplicação (IA aplicada, legislação, leitura de código, julgamento
    de afirmativas I/II/III): pode usar comando explícito (`"Assinale a
    alternativa correta"`) com alternativas em frases completas e
    maiúsculas — também é formato real da FGV para esse tipo de item. Não
    infle o cenário além do necessário para sustentar a pegadinha.
- **Alternativas:** concisas, uma ideia por alternativa, sem repetir a
  íntegra do cenário. Pelo menos uma "quase certa" (acerta a primeira
  metade, erra no detalhe final) quando fizer sentido para o tema.
- **`why` (por que a certa é certa):** 1–3 frases, analítico e direto. Pode
  citar o comportamento da banca (`"a FGV troca X por Y"`), sem repetir o
  que já vai em `erradas`.
- **`erradas` (por que cada errada é errada) — o ponto mais importante:**
  explique o erro de forma natural e **varie a abertura de cada frase**
  (não repita o mesmo molde tipo `"Distrator X:"` em todas as alternativas
  da mesma questão — isso soa mecânico e não é como a FGV comenta gabarito).
  Nomeie o mecanismo quando ajudar (absoluto, inversão de par, extrapolação,
  troca de número/ordem, contradição interna, distrator inventado), mas
  tecido dentro da explicação, não como rótulo fixo repetido. Os mecanismos
  catalogados estão em `dicas/tecnica-fgv.md` e no Apêndice B da apostila
  (`apostila/capitulos/20-glossario-pegadinhas.tex`).
- **Depois de gerar, sempre rode `./valida.py`** antes de considerar a
  questão pronta.

## Mexer na apostila (`apostila/`)

Para **verificar** o livro — conferir fatos, versões de norma, cobertura do
edital, coerência entre as camadas: siga **`VERIFICAR-APOSTILA.md`**. Ele é o
prompt de auditoria pronto, com as sete frentes em ordem de custo em ponto e a
linha de base das caixas para detectar regressão.

Vale mesmo para retoque pequeno: a apostila é a camada de cima de quatro
(apostila → `resumo/` → `dicas/` → `banco.json`), então **fato alterado aqui
tem de descer para as outras três**, senão o `./valida.py` acusa drift — e o
Lucas decora a versão errada. Ao terminar, recompile
(`cd apostila && latexmk -pdf main.tex`) e rode `./valida.py`.

## Mexer no livro-texto (`teoria/`)

`teoria/` é um livro-texto complementar à `apostila/`, mesma identidade
visual (compartilha o espírito de `apostila/preambulo.tex`, mas com
`teoria/preambulo.tex` próprio), conteúdo de aprendizado profundo em vez de
revisão rápida — cada conceito ganha definição, mecanismo/porquê e exemplo
resolvido, sem as caixas de estratégia de prova (pegadinha/comosair/jacaiu/peso)
da apostila. Ele reaproveita fatos já auditados na apostila (não é um
processo de verificação novo) e troca só a didática.

- Cada capítulo usa `\label{cap:<slug>-teoria}` e seções reaproveitadas entre
  capítulos usam `\label{sec:<nome>-teoria}` — mantenha esse sufixo para não
  colidir com os labels da apostila (que não o usam).
- Caixas próprias: `conceito` (definição + mecanismo), `cuidado` (confusão
  conceitual comum — sem framing de "banca"), `regrapratica` (regra
  prática/mnemônico), `exemplo` (roxo, exemplo resolvido).
- **A numeração dos capítulos bate com a apostila de propósito**
  (`teoria/main.tex` fixa `\setcounter{chapter}{2}` antes do primeiro
  `\include`, porque a apostila reserva os capítulos 1–2 para
  como-usar/técnica-fgv, ausentes no `teoria/`). Se adicionar ou remover um
  capítulo em qualquer um dos dois livros, confira se a numeração ainda bate
  — é o que `./apostila.py --teoria <bloco>` usa para abrir a página certa.
- Não toque a `apostila/` ao editar `teoria/` — são livros irmãos, não uma
  substituição um do outro. Ao terminar, recompile
  (`cd teoria && latexmk -pdf main.tex`) e confira que não sobrou overfull/
  underfull nem referência quebrada no `main.log`.

## Caderno de erros — registrar sempre

Depois de explicar, **sempre** proponha (ou já edite direto, se o bloco for
óbvio) a entrada correspondente em `erros/<bloco>.md`, no formato do repositório:

```markdown
## <título curto do conceito>
- **Errei:** <o que confundiu/errou, em uma linha>
- **E:** <a correção/regra certa, em uma linha>
- <fonte: banca ano concurso Qnn | dd/mm>
```

Blocos disponíveis em `erros/`: arquitetura, atualidades, banco-dados, bi,
eng-software, frontend, governanca, ingles, java, legislacao, orfaos,
portugues, programacao, redes, rlm, seguranca. Se o tópico não encaixar em
nenhum, use `orfaos.md`. Se não tiver certeza do bloco, pergunte antes de editar.

Não confundir com `./feito.sh` (contagem de questões) nem com o quiz de
terminal (`./quiz.py`, que já grava sozinho em `progresso.csv`) — o caderno de
erros é só o `erros/*.md`.
