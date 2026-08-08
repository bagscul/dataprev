# DATAPREV 2026 — Desenvolvimento de Software

Prova: **11/10/2026, 13h as 17h**. Portoes fecham 12h30.
Lotacao: Natal/RN. 20 vagas imediatas, 13 de ampla concorrencia.

## Rotina diaria

```bash
./status.py          # o que estudar hoje (blocos + atalhos) + como estou
./estudar.sh          # ATALHO PRINCIPAL: abre o(s) capitulo(s) do dia na apostila
                      # (PDF de verdade, zathura) + roda ./quiz.py --hoje no terminal
./estudar.sh --teoria # idem, mas abre teoria/main.pdf (livro-texto) em vez da apostila
./quiz.py --hoje     # so o quiz, sem abrir a apostila
./quiz.py --resumo hoje   # resumo de conteudo dos blocos do dia
./quiz.py --dica hoje     # dica de banca dos blocos do dia
./feito.sh 45 34     # questoes feitas FORA do quiz (plataforma, PDF)
./salvar.sh          # commit + push
```

**`./estudar.sh` e o atalho do dia a dia.** Sem argumento, abre a apostila
(`apostila/main.pdf`) no zathura ja na pagina do(s) capitulo(s) de hoje e
roda `./quiz.py --hoje` no terminal atual. Aceita os mesmos argumentos do
quiz — `./estudar.sh java redes -n 15`, `./estudar.sh --simulado`,
`./estudar.sh --dia ontem` — e repassa o que for do bloco/`--dia`/`--quem`
tambem pra apostila. So funciona em Linux com zathura (WSLg no Windows); pra
so ver onde ler sem abrir PDF, use `./quiz.py --apostila <bloco>`; pra abrir
a apostila sem rodar o quiz, `./apostila.py <bloco>`. Pra abrir o
`teoria/main.pdf` (livro-texto, ver abaixo) em vez da apostila, some `--teoria`
em qualquer um desses tres: `./estudar.sh --teoria java`, `./apostila.py
--teoria java`.

**Apostila x `teoria/`.** A `apostila/` e enxuta de proposito — feita pra
revisar em 10 semanas, com foco em pegadinha de banca. O `teoria/` e um
livro-texto complementar, com a mesma identidade visual mas conteudo de
aprendizado profundo: cada conceito ganha definicao, mecanismo/porque e
exemplo resolvido, sem o filtro "o que cai em prova". Use a apostila pra
revisar o que voce ja sabe; abra o capitulo correspondente do `teoria/`
quando um conceito nao estiver fixado de verdade. Os capitulos e a numeracao
batem entre os dois livros (ex: Capitulo 12 e Governanca nos dois), entao
`--teoria` sempre abre o mesmo assunto que a apostila abriria.

**Tudo puxa do roteiro.** Cada dia tem dois assuntos (um especifico + um
geral, ex: "banco-dados + rlm"). O `--hoje` cobre os dois automaticamente, e
`--resumo hoje` / `--dica hoje` mostram o material desses blocos. Em dia de
**revisao** o `--hoje` refaz o que voce ainda nao fixou (repeticao espacada);
em dia de **simulado**, dispara o simulado cronometrado; em **descanso/prova**,
avisa. O `status.py` mostra o plano com os comandos prontos para copiar.

**Atrasou? Faca um dia passado.** `./quiz.py --dia ontem` (ou `anteontem`,
`-3`, ou `2026-07-29`) roda o plano daquele dia e **credita naquele dia**
(marca como feito, conserta a aderencia) — nao mexe em hoje. Veja o que ficou
em aberto com `./quiz.py --pendentes`.

**Nao quer seguir o roteiro?** Estude o que quiser, quando quiser: `./quiz.py
java redes` (blocos livres), `./quiz.py --prova tjrj2` (uma prova), `./quiz.py
--erradas` (so seus erros). O roteiro e um atalho, nao uma amarra — o registro
cai em hoje.

## Quiz de terminal

```bash
./quiz.py                  # 10 aleatorias do banco original
./quiz.py java redes -n 15 # blocos especificos
./quiz.py --hoje           # segue o plano do roteiro para hoje
./quiz.py --erradas        # repeticao espacada: so o que voce ainda nao fixou
./quiz.py --simulado       # simulado cronometrado no formato da prova (70q)
./quiz.py --dica java      # como a FGV cobra esse bloco (sem bloco: lista)
./quiz.py --apostila java  # aponta o capitulo da apostila desse bloco
./quiz.py --stats          # desempenho por bloco + causa do erro (conceitual/leitura)
./quiz.py regencia         # microtopico (subtag), atravessando os blocos
```

**Repeticao espacada (`--erradas`).** Nao mostra tudo que voce ja errou um
dia — mostra so o que ainda nao fixou. Uma questao sai do pool quando voce
acerta 2x seguidas desde o ultimo erro; se errar de novo, volta. Assim voce
nao perde tempo revisando o que ja domina.

A saida e **temporaria**: passados **21 dias** sem ver a questao, ela volta ao
pool uma vez (`INTERVALO_REVISAO`, no `quiz.py`). E o que impede que o assunto
fixado em agosto chegue a 11/10 sem nenhuma revisita; acertar de novo empurra o
prazo por mais 21 dias, errar devolve a questao ao regime normal. Quando houver
questao voltando por intervalo, o quiz avisa na abertura da sessao.

**Simulado cronometrado (`--simulado`).** 70 questoes no formato da prova
(gerais peso 1 + especificos peso 2,5, nessa proporcao), especificos primeiro,
SEM correcao ate o fim, com tempo na tela. No final: nota ponderada, projecao
para os 115 pontos, o corte de eliminacao e o desempenho por bloco. As erradas
viram material de `--erradas`. Use `-n` para um simulado menor (ex: `-n 20`).
No roteiro, o dia de **simulado** ja dispara esse modo via `--hoje`.

O sorteio prioriza, dentro de cada bloco, a questao nunca vista ou vista ha
mais tempo (olhando o `historico.json` de qualquer modo do quiz, nao so
simulado) — so repete algo ja visto quando o pool fresco do bloco se esgota.
Quando isso acontece, ou quando um bloco tem menos questoes do que a
proporcao do edital exige, o simulado avisa no terminal qual bloco precisa de
questao nova em `banco.json`.

Voce responde com a letra; ao errar, o quiz explica por que a correta esta
certa e por que CADA uma das outras esta errada. Ao errar, ele grava
AUTOMATICAMENTE a entrada em `erros/<bloco>.md` (deduplicando por questao —
a mesma errada duas vezes nao vira duas anotacoes). Para nao gravar, use
`--sem-anotar`. No fim mostra os conteudos da sessao e registra no
progresso.csv (entao nao use ./feito.sh para as questoes do quiz).

433 questoes originais em estilo FGV (todas com gabarito auditado contra
fonte) + questoes reais de 15 provas da FGV = **~1109 questoes utilizaveis**.
As explicacoes ja vem gravadas no banco: o quiz roda offline, sem chave de
API e sem custo — entao qualquer pessoa com o repo roda no terminal dela.

**Dicas de banca.** `./quiz.py --dica <bloco>` mostra, para aquele assunto,
o que a FGV mais cobra, como ela arma a pegadinha e como se sair melhor.
Quando voce filtra por um bloco (`./quiz.py java`), o quiz lembra que a dica
existe. Os textos ficam em `dicas/<bloco>.md` — edite a vontade.

**Técnica de prova (leia primeiro).** `./quiz.py --dica tecnica-fgv` é o guia
TRANSVERSAL: como atacar qualquer questão da FGV — ler o comando, reconhecer
os padrões de distrator (absolutos, inversao de conceitos, a "quase certa"),
eliminar, e gerir o tempo. Destilado da resolucao de ~500 questoes reais.

**Apostila.** `./quiz.py --apostila <bloco>` (ou `--apostila hoje`) aponta o
capitulo da apostila (`apostila/main.pdf`) daquele assunto — no espirito de
`--dica`/`--resumo`, mas como a apostila e PDF ele indica onde ler, nao imprime
o conteudo. Ao errar no quiz, o caderno de erros ja recebe a referencia do
capitulo automaticamente.

**Causa do erro (`--stats`).** Ao errar, o quiz pergunta em uma tecla se foi
erro **conceitual** (nao sabia o conteudo) ou de **leitura/armadilha** (sabia e
caiu na construcao) — Enter pula. O `--stats` separa as duas causas por bloco e
recomenda o caminho certo: erro conceitual manda **reler a apostila + fazer mais
questoes** (nao adianta tecnica se falta conteudo); erro de leitura aponta os
**sete padroes de distrator** (`--dica tecnica-fgv`).

**Resumo de conteudo.** `./quiz.py --resumo <bloco>` mostra o resumo do
assunto — feito a partir do edital (Perfil 3), das dicas, da resolucao das
questoes e de pesquisa em fontes. A visao geral da prova (pesos, estrategia,
alertas de redes fora-do-edital e OWASP 2025 vs 2021) esta em
`resumo/README.md`. Os arquivos ficam em `resumo/<bloco>.md`.

Duvida que a explicacao do terminal nao resolve? Cole a questao no Claude
Code (veja `CLAUDE.md`): la da pra perguntar de volta.

### Onde voce mais erra (microtopicos)

O bloco e grosso demais para mirar estudo: `portugues` sao 90 questoes, e sete
erros seus podem estar em sete assuntos diferentes. Quem tem a granularidade do
erro e a **subtag** — o campo `sub` da questao e a linha `- **sub:**` do caderno
de erros. Sao **168 microtopicos** em `subtags.py` (fonte unica: `quiz.py`,
`valida.py` e `fraquezas.py` leem de la), quase todos derivados das secoes do
`teoria/` e da apostila — a taxonomia do edital, ja auditada. `./quiz.py --tags`
lista todos por bloco. Questao nova do `banco.json` e obrigada a trazer `sub`
(o `./valida.py` bloqueia). Hoje 902 das 1133 questoes dos dois bancos ja tem
`sub` (80%) — 388 das 433 originais e 514 das reais, cobrindo 153 dos 168
microtopicos. As 231 restantes ficaram sem etiqueta **de proposito**: ou nao ha
microtopico que as descreva (trigger, funcao deterministica, apassivacao), ou o
assunto esta fora do edital (direito constitucional e administrativo vindo do
TJRJ/MPU) — etiquete a mao quando esbarrar numa delas.

```bash
./fraquezas.py            # ranking dos microtopicos onde voce mais erra
./fraquezas.py --top 5    # so os cinco piores
./fraquezas.py --sem-sub  # entradas do caderno sem etiqueta (com sugestao)
./fraquezas.py --prompt   # briefing pronto pra gerar questao dos piores
./quiz.py regencia        # treina so aquele microtopico
```

O ranking cruza tres fontes: o **caderno de erros** (quantas vezes voce errou
o assunto), o **historico do quiz** (a causa — conceitual ou armadilha) e os
**dois bancos** (quantas questoes ja cobrem aquilo). Errar 2x um assunto com 5
questoes ou menos no banco acende o alerta `←`: e ali que vale gerar questao
nova, e o `--prompt` ja monta o pedido, inclusive escolhendo o FORMATO pela
causa (erro conceitual pede questao direta de definicao; erro de leitura pede
questao de aplicacao com a quase-certa reforcada).

O ciclo fecha sozinho: ao errar no quiz, a entrada do caderno ja nasce com a
subtag quando a questao tem uma. Questao de prova real nao tem — etiquete a mao
(o `--sem-sub` sugere qual). Microtopico novo nasce de **erro real**: crie em
`subtags.py` e o `./valida.py` cobra qualquer etiqueta fora do vocabulario.

### Questoes reais das provas

As provas em `provas/*.pdf` viram banco de questoes:

```bash
./importar_provas.py                       # PDF -> banco-provas.json
./importar_provas.py --tudo                # idem, trazendo o caderno inteiro
./gabarito.py --falta                      # o que ainda esta sem gabarito
./gabarito.py dataprev2024 "1-C 2-A ..."   # cola o gabarito OFICIAL da FGV
./quiz.py --prova dataprev2024             # resolve as questoes reais
./quiz.py --prova todas -n 20              # de todas as provas importadas
```

Reimportar e seguro: rodar `./importar_provas.py` com o banco atual devolve o
arquivo **byte-identico**. Ele preserva gabarito, explicacoes e o marcador de
anulada, e mantem o **recorte** da prova — das 80 questoes da ALERO ficaram so
as de TI, e as descartadas nao voltam sozinhas (use `--tudo` se quiser o
caderno inteiro). A `tag` vem sempre de `notas/<prova>-mapa.md`: para
reclassificar uma questao, edite o mapa, nao o JSON, senao a reimportacao
desfaz.

O caderno de questoes nao traz o gabarito, entao a questao entra com
`ans: null` e **o quiz nao a sorteia ate o gabarito oficial ser preenchido**.
Isso e proposital: gabarito chutado treina o reflexo errado, que e pior do
que nao treinar. Questoes que dependem de figura/codigo (que se perdem na
extracao do PDF) tambem ficam fora do sorteio.

IMPORTANTE: o quiz e complemento, nao substituto. Questoes REAIS da FGV
continuam sendo o treino principal. Provas de banca sao protegidas por
direito autoral: o `banco.json` e original, e o `banco-provas.json` (texto
das provas) fica de uso pessoal, em repo privado — nao publique.

### Adicionar mais questoes (escala sozinho)

O quiz le quantas questoes houver — nada esta preso a um numero fixo.

- **Mais provas:** jogue o PDF em `provas/`, rode `./importar_provas.py`,
  depois `./gabarito.py <prova> "1-C 2-A ..."` com o gabarito oficial.
- **Mais questoes originais:** acrescente objetos a `banco.json` (campos:
  `tag`, `q`, `alts` com 5, `ans` 0-4, e de preferencia `why` + `erradas`).
- **Sempre valide depois:** `./valida.py` checa a integridade dos dois bancos
  (estrutura, gabarito, explicacoes) e aponta o que quebraria o quiz. Erro
  bloqueia; aviso (ex: questao sem explicacao) so avisa — o quiz roda mesmo
  assim, so nao mostra o comentario.

## Instalar no Windows — guia da Geys (do zero)

Boa notícia: o quiz roda **só com o Python** (nada de instalar biblioteca).
Você já tem Python e o Windows Terminal, então é rápido. Siga na ordem.

**1. Confirme que o Python funciona.** Abra o Windows Terminal e digite:

```powershell
python --version
```

Tem que aparecer algo como `Python 3.12.x`. Se der erro, tente `py --version`
— se esse funcionar, use `py` no lugar de `python` no resto do guia.

**2. Pegue a pasta do estudo.** São duas formas; escolha uma:

- **Mais simples (sem instalar nada):** peça pro Lucas te mandar a pasta
  compactada (`.zip`) pelo WhatsApp/Drive/pendrive. Salve em algum lugar fácil,
  tipo `Documentos`, e **extraia** (botão direito → Extrair tudo). Vai virar
  uma pasta chamada `dataprev`.
- **Recomendada (pra receber as questões novas que o Lucas adicionar):**
  instale o **Git para Windows** (baixe em git-scm.com, avance tudo no
  instalador). Peça pro Lucas te adicionar como colaboradora no repositório.
  Depois, no Windows Terminal:
  ```powershell
  cd Documentos
  git clone https://github.com/bagscul/dataprev.git
  ```
  Quando o Lucas adicionar questões, você atualiza com `git pull` (passo 5).

**3. Entre na pasta pelo terminal.** No Windows Terminal:

```powershell
cd Documentos\dataprev
```

(dica: no Windows 11 você pode abrir a pasta no Explorer, clicar com o botão
direito dentro dela e escolher "Abrir no Terminal" — já cai no lugar certo.)

**4. Rode o quiz.** No Windows o comando é `python quiz.py` (com o `--quem geys`
pra o seu progresso ficar separado do do Lucas):

```powershell
python quiz.py --quem geys --hoje
python quiz.py --quem geys --dica java
python quiz.py --quem geys --stats
```

Na primeira vez ele cria o `progresso-geys.csv` só seu. Pronto — é isso.

**5. (Só se usou o Git) Receber as questões novas.** Sempre que o Lucas
avisar que adicionou questões, dentro da pasta:

```powershell
git pull
```

> **Importante:** no Windows, em TODOS os comandos deste README troque
> `./quiz.py` por `python quiz.py`. O `./` é coisa de Linux/Mac; no Windows
> não funciona. O resto dos argumentos (`--hoje`, `--dica`, `--erradas`…) é igual.

## Estudando em dupla

Cada pessoa tem seu proprio progresso, no mesmo repo:

```bash
./quiz.py --quem geys --hoje    # roda como a Geys  (no Windows: python quiz.py ...)
./quiz.py --quem geys --stats   # desempenho so dela
```

O roteiro (datas, foco de cada dia) e compartilhado. Os contadores nao:
na primeira vez, `progresso-<nome>.csv` e criado a partir do roteiro com
tudo zerado, e o historico vai para `historico-<nome>.json`. Sem `--quem`,
roda como Lucas (`progresso.csv`), como sempre foi.

O `status.py` (painel de acompanhamento) acompanha o mesmo `--quem`, e tem
um modo de comparacao lado a lado:

```bash
./status.py --quem geys        # painel completo dela (aderencia, sequencia, blocos)
./status.py --quem geys hoje   # so o conteudo de hoje, do lado dela
./status.py --vs geys          # lucas x geys lado a lado, bloco a bloco
```

O `--vs` mostra quem esta na frente em cada bloco (diferenca >= 10 pontos) e
lista os blocos em que os DOIS estao abaixo de 60% — esses sao os bons
candidatos pra estudar junto em vez de sozinho.

O caderno de erros em `erros/*.md` e compartilhado de proposito — errar
junto e ver o erro do outro e parte do metodo.

## Como anotar um erro

Em `erros/<bloco>.md`, tres linhas. O "errei" e a parte que importa:

```markdown
## SOLID — principio da segregacao de interface
- **Errei:** confundi ISP com SRP
- **E:** ISP = interface pequena e especifica; SRP = classe com uma responsabilidade
- FGV 2024 Dataprev Q47 | 24/07
```

## Regras que o roteiro assume

- Questao **todo dia**, sem excecao. Resolver questao e o metodo, nao a revisao.
- Filtro de banca travado em **FGV**. Outra banca constroi reflexo errado.
- Dois assuntos por dia: um **especifico** + um **geral** (seg Portugues, ter
  Ingles, qua RLM, qui Legislacao, sex Atualidades).
- Nas semanas tematicas o bloco domina os 5 dias; o reencontro vem pelas
  **revisitas** marcadas, pelos **simulados** e pelo `--erradas`.
- Simulado **domingo, 13h**, cronometrado. Mesmo horario da prova. Sao 10 no
  total — nove aos domingos e o ultimo na sexta da semana da prova.
- No simulado: **especificos primeiro** (valem 2,5x), gerais depois.

## Onde a prova se decide

| Bloco (Dataprev 2024) | Questoes | Pontos |
|---|---|---|
| Engenharia de Software | 9 | 22,5 |
| Banco de Dados / BI | 6 | 15 |
| Programacao | 6 | 15 |
| Arquitetura de Software | 4 | 10 |
| Seguranca | 3 | 7,5 |
| Redes | 2 | 5 |

(Reclassificado questao a questao direto no PDF de `provas/dataprev2024.pdf`
em 29/07/2026 — a tabela anterior tinha 4 categorias que nem existem como tag
no quiz e nao fechava as 30 questoes do bloco especifico.)

Eng. de Software, Banco de Dados/BI e Programacao dividem o topo da FGV em TI
(9/6/6, praticamente empatados). So 1 das 2 questoes de Redes e realmente
"fora do edital" (X.800/OSI) — a outra (ambientes Internet/intranet/extranet)
e o item 4 do proprio edital de Desenvolvimento de Sistemas.

## Pendencias

- [x] ~~Inscricao~~ — feita
- [ ] Confirmar com a FGV se Ciencia da Computacao vale como
      "graduacao em TI" sem pos de 360h — concursodataprev26@fgv.br
