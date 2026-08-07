# Continuar de onde paramos — 07/08/2026 (fim do dia)

Arquivo de retomada. **Não há dívida técnica aberta** — as quatro provas da
busca da noite foram importadas *e* explicadas no mesmo dia. O que sobra é
trabalho de conteúdo, e o **§1 traz o prompt pronto** para atacá-lo. Leia na
ordem: estado → prompt → detalhe de cada frente → ressalvas.

---

## 0. Estado do repositório — LEIA PRIMEIRO

Antes de qualquer coisa, rode `git status` e `./valida.py`.

Números de referência (medidos em 07/08/2026, não precisa remedir):

- `banco.json` 403 · `banco-provas.json` 700 · **1079 utilizáveis no quiz**
- **15 provas reais** importadas
- `./valida.py`: 0 erros, **2 avisos** — os dois da `nav-tec` Q58 (§3)
- **as 15 provas estão com explicação completa**; a Q58 é a única exceção
- `sub` (microtópico): **533 das 1103** questões dos dois bancos (48%)

O que entrou no dia (detalhe no `CHANGELOG.md`, seis entradas de 07/08): as
provas `cprm-ads` e `nav-med` com suas **106 explicações**; a busca que trouxe
`epe-ti`, `rfb-ana`, `rfb-aud` e `cprm-pesq` (+74 questões, o inglês de 69 para
102); as **73 explicações** dessas quatro; e seis correções no
`importar_provas.py` — quatro pela manhã e mais duas à noite, quando o parser
aprendeu as marcas de texto-base da Receita Federal (`Text I` solto) e do CPRM
("As questões da prova de Língua Inglesa referem-se ao TEXTO a seguir").

Garantias que valem conhecer antes de mexer:

- `./importar_provas.py` **sem argumento** devolve o `banco-provas.json`
  byte-idêntico (conferido depois das explicações). Se parar de devolver, é
  sinal de que alguém consertou dado à mão no JSON em vez de no parser.
- A reimportação **preserva** `ans`, `why`, `erradas`, `anulada` e `sub`.
  **Não preserva `requer_imagem`** — ver a ressalva da Q17, logo abaixo.
- Texto-base: o parser reconhece **seis** marcas. Quatro trazem a contagem na
  própria fórmula; as duas novas (RFB e CPRM) não trazem, e nelas o alcance sai
  da posição — até o próximo marcador, ou até o cabeçalho da seção seguinte.
  Se for mexer nisso, confira o efeito com um diff do `banco-provas.json`
  antes de commitar: na primeira tentativa a regra espalhou o texto da redação
  do CPRM por cima de 30 questões objetivas.

---

## 1. O prompt da próxima conversa

Quatro frentes, em ordem de retorno. **A frente A sozinha já enche uma
conversa** (LaTeX + recompilação); se for fazer A e B no mesmo dia, comece
conversa nova entre elas.

### O prompt

> Leia primeiro: este arquivo (`CONTINUAR-AQUI.md`) inteiro, o `CLAUDE.md` e,
> conforme a frente, o `CONTRIBUINDO-QUESTOES.md` (frente B) ou o
> `VERIFICAR-APOSTILA.md` (frente A). Rode `git status` e `./valida.py` antes
> de mexer em qualquer coisa. Os números do §0 foram medidos em 07/08/2026 —
> não precisa remedir.
>
> **FRENTE A — escrever a teoria que falta (maior retorno).** As 74 questões
> importadas em 07/08 cobram três assuntos que **não existem em nenhuma das
> quatro camadas** (apostila, `teoria/`, `resumo/`, `dicas/`). Hoje, se eu
> errar essas questões, o quiz explica mas não há onde estudar. Verificado por
> grep nas quatro camadas, não por suposição:
>
> 1. **Catálogo de ataques e de malware** — capítulo 07 (segurança). O
>    capítulo se organiza por conceito (tríade, criptografia, TLS, controle de
>    acesso, OWASP, X.800, riscos, continuidade, detecção) e **não tem seção de
>    tipos de ataque**: XSS e SQLi só aparecem de passagem dentro do OWASP, e
>    MitM e session hijacking não aparecem em lugar nenhum. Escreva a seção
>    cobrindo: **CSRF**, **MitM**, **replay**, **session hijacking**, **spear
>    phishing** (× phishing × spam), a **família DDoS** (Ping of Death,
>    Slowloris, Smurf, Teardrop, UDP storm) e a **família de malware** (worm,
>    spyware, trojan, backdoor, rabbit, ransomware). Âncoras reais já no banco:
>    `cprm-ads` Q40, Q41 e Q61, e `epe-ti` Q59.
>    **Cuidado que já custou análise:** o CSRF **não** entra na tabela do OWASP
>    Top 10 — ele saiu da lista em 2017 e foi absorvido pelo Broken Access
>    Control. A tabela 2025/2021 da apostila está **correta**; não mexa nela.
>    O CSRF entra como *ataque*, não como categoria.
> 2. **Complexidade ciclomática (McCabe)** — capítulo 02 (eng. de software),
>    com exemplo resolvido. Âncora: `epe-ti` Q79, que pede o cálculo. A regra
>    que a questão cobra: pontos de decisão + 1, e o `senão` final **não conta**
>    (não testa nada, só recolhe o caso restante).
> 3. **Code smells nomeados** — capítulo 02. Hoje "code smell" aparece como
>    conceito genérico; faltam **Feature Envy**, **Data Clumps** e os
>    **bloaters** com suas refatorações. Âncora: `epe-ti` Q77.
>
> Opcional, de menor valor: **JMeter** (Sampler, Thread Group com ramp-up,
> Timer, Assertion) numa caixa `jacaiu` — âncora `epe-ti` Q80. O conceito de
> teste de carga e estresse já está no capítulo 02; falta só a ferramenta.
>
> Regras da frente A, todas do `CLAUDE.md`:
> - o que entrar na apostila **desce** para `resumo/<bloco>.md` e
>   `dicas/<bloco>.md` — senão o `./valida.py` acusa drift;
> - o `teoria/` ganha a versão didática do mesmo conteúdo (caixas `conceito`,
>   `cuidado`, `regrapratica`, `exemplo`), **sem** as caixas de banca
>   (`pegadinha`, `comosair`, `jacaiu`, `peso`), que são exclusivas da apostila;
> - se acrescentar ou remover capítulo, confira a numeração: o `teoria/main.tex`
>   fixa `\setcounter{chapter}{2}` para bater com a apostila;
> - ao terminar: `cd apostila && latexmk -pdf main.tex`, o mesmo em `teoria/`,
>   conferir que não sobrou overfull/underfull nem referência quebrada no
>   `main.log`, e rodar `./valida.py`.
>
> **FRENTE B — fechar o déficit de questões (30).** Faltam **18 de inglês** e
> **12 de atualidades**; português, RLM e legislação já estão no azul e **não
> devem entrar no lote**. O plano e o rateio por microtópico estão no
> `GERAR-LOTE-GERAIS.md`, com as cotas já corrigidas para os números de hoje.
> Em inglês, mire `julgamento-afirmativas` e `verbos-modais`, que têm uma
> questão cada; em atualidades, `atualidades-socioambiental` tem três. Toda
> questão nova nasce com `sub` (o `./valida.py` bloqueia sem), e o padrão de
> enunciado, distrator e `erradas` está no §5 do `CONTRIBUINDO-QUESTOES.md`.
>
> **FRENTE C — etiquetar o resto do banco.** `sub` está em **533 de 1103**
> (48%); as ~570 sem etiqueta são quase todas questões de prova. O
> `subtags.py` já expõe `sugerir(texto)`, então dá para fazer uma passada
> automática propondo etiqueta e revisar só as duvidosas — não etiquete no
> escuro, porque a etiqueta errada distorce o ranking do `./fraquezas.py`.
> É a frente mais adiável: nenhum simulado deixa de rodar por falta de `sub`.
>
> **FRENTE D — vigiar dois gabaritos.** O do `nav-med` (prova de 02/08/2026) é
> **preliminar**: quando sair o definitivo, reconferir as 45 questões e checar
> anulações. E a `nav-tec` Q58 é divergência real registrada (§3) — se o
> definitivo mudar para **E**, basta escrever a explicação e o `./valida.py`
> zera os 2 avisos. Os dois em <https://conhecimento.fgv.br/concursos/navbrasil26>.
>
> **O que NÃO fazer**, tudo já decidido e medido:
> - não mexer na tabela OWASP da apostila (está correta, inclusive na ausência
>   do CSRF);
> - não gerar questão de português, RLM ou legislação — os três estão acima da
>   demanda dos 10 simulados;
> - não marcar `requer_imagem` à mão no JSON: o campo **não** sobrevive à
>   reimportação (o conserto é no `importar_provas.py`, veja o §3);
> - não alterar `ans` para acomodar análise própria — divergência de gabarito
>   vira anotação, como a `nav-tec` Q58;
> - não caçar mais provas antes de gerar: só sobrou a **PM-SP Aluno-Oficial
>   2025**, que não é da área de tecnologia e cuja contagem de inglês nunca foi
>   confirmada. Vale só se a frente B não fechar o déficit.

---

## 2. Detalhe da frente B — o déficit de questões

Medido contra a demanda de **10 simulados** do roteiro (cada um: 40 gerais na
proporção do edital + 30 específicos):

| bloco | pool | precisa | falta |
|---|---|---|---|
| inglês | **102** | 120 | +18 |
| atualidades | 48 | 60 | +12 |
| português | 129 | 120 | ok |
| RLM | 64 | 50 | ok |
| legislação | 68 | 50 | ok |
| **todo o Módulo II** | — | — | **ok, déficit zero** |

O déficit total caiu de 63 para **30**. Duas saídas:

1. **Mais provas** — o que sobrou é fino. A única pista aberta é a **PM-SP
   Aluno-Oficial 2025** (13/07/2025, tem inglês, nível superior, mas não é
   área de tecnologia e a contagem segue não confirmada). Os outros dois
   cadernos de TI da EPE 2024 (Infraestrutura e Segurança, Ciência de Dados)
   **não trazem inglês novo** — o Módulo I é o mesmo do caderno de Soluções,
   conferido —, mas os específicos são diferentes e alimentariam `bi` e
   `seguranca`.
2. **Gerar questão de inglês e de atualidades.** O plano está em
   `GERAR-LOTE-GERAIS.md`, com o
   aviso no topo: as cotas de lá são de antes das importações, e português e
   RLM têm de sair do lote. A metodologia e o rateio por microtópico continuam
   valendo. Em inglês, `julgamento-afirmativas` e `verbos-modais` saíram do
   zero (uma questão cada, vindas do `nav-med`), e `compreensao-global-ingles`
   e `vocabulario-contexto` são os mais fartos — mire nos dois primeiros.

### Já verificado e descartado — não repita

Além do que já constava (CNU 2025 sem inglês, INB 2026 sem prova aplicada,
BNDES que é Cesgranrio, PSS IBGE de nível médio, SEEC-RN de professor de
inglês, CGE-SP TI sem Módulo I, cadernos de Analista do CPRM que não sejam
ADS), a busca de 07/08 à noite fechou mais estas:

| prova | por quê |
|---|---|
| **Dataprev 2024 — os outros 14 cadernos** | seria o ideal (mesma empresa, mesma banca), mas **o Módulo I é idêntico** ao do caderno que já temos. Conferido baixando quatro deles — Análise de Negócio (CNS001), Segurança Cibernética (CNS005), Advocacia (CNS007) e Analista de Processamento (CNS013): mesmo texto de inglês e de atualidades, todos do turno da **tarde**. Importar qualquer um cria 40 duplicatas |
| EPE 2022 | não tem caderno de TI (só Pesquisa Energética e Gestão Corporativa–RH), e é prova de 2022 |
| AgSUS 2025 — Analista de Gestão em TI | cargo de TI, mas o Módulo I é português 12, informática 8 e RLM 7: **sem inglês** |
| PM-SP Aluno-Oficial 2025 | tem inglês e é nível superior, mas não é área de tecnologia e a quantidade de questões segue não confirmada. Fica como último recurso, se as quatro acima não bastarem |

### Regras de importação — não repita erros já cometidos

1. **Filtre "Legislação" de concurso genérico.** A legislação do edital é
   LGPD, Marco Civil e LAI. A de quase todo concurso é direito constitucional
   e administrativo — fora do edital. O banco já carrega 42 questões assim,
   vindas do TJRJ/MPU.
2. **Filtre "Informática"** (Word, navegador, planilha): o Perfil 3 não tem
   esse bloco.
3. **Cheque se o Módulo I se repete entre cadernos do mesmo concurso.** Na NAV
   Brasil os dois cadernos de nível superior tinham as **mesmas 40 questões**
   de conhecimentos básicos.
4. **Classifique por conteúdo, não pelo rótulo da banca.** A `nav-tec` Q33
   estava sob "Informática" e cobrava impacto da IA nas ocupações; a
   `cprm-ads` Q45 está em "Conhecimentos Específicos" e é fundamentos de IA.
   As duas viraram `atualidades`.

### Fluxo de importação

```bash
# 1. PDF em provas/<nome-curto>.pdf (nome curto: vira o id da questão)
# 2. classifique e escreva notas/<nome>-mapa.md (veja notas/cprm-ads-mapa.md de modelo)
./importar_provas.py                 # SEM argumento: reescreve o arquivo inteiro
# 3. remova do banco-provas.json o que ficou fora do recorte
./gabarito.py <nome> "1-C 2-A ..."   # gabarito OFICIAL, nunca chutado
./valida.py
```

Atenção: `./importar_provas.py` **com** argumento sobrescreve o
`banco-provas.json` só com as provas passadas. Rode sempre sem argumento.
Confira o **tipo** do caderno contra o **tipo** da tabela do gabarito antes de
colar: no CPRM as tabelas se chamam "ADS – 1" e "ADS – 2", e a "1" é a TIPO 1.

**Depois de importar, explique no mesmo dia.** Duas importações deixaram 86 e
106 questões sem `why`/`erradas` para o dia seguinte; a terceira (as quatro
provas de 07/08 à noite) foi explicada na mesma sessão e é o padrão a seguir. O
caminho que funcionou nas três vezes: lotes de 10 por bloco, começando pelos
**específicos** (maior retorno), atualidades depois, inglês e RLM na sequência,
português por último; a cada lote, `./valida.py`.

E confira o texto-base antes de escrever: foi ao explicar o inglês da Receita
Federal que apareceu a lacuna do parser. Se o enunciado disser "Based on Text
I" e o texto não estiver no campo `q`, o conserto é no `importar_provas.py`.

---

## 3. Ressalvas registradas — não são bugs a consertar às pressas

> **`nav-tec` Q58 — divergência real de gabarito, não conserto silencioso.**
> O enunciado descreve dependência transitiva (`Nome_Fabricante` →
> `ID_Fabricante` → `ID_Veiculo`) e pede o que remover para atingir a 3FN: é a
> letra **E**. O gabarito oficial marca **C** ("superchave que viola as
> invariantes da FNBC"), que não descreve o caso. Conferido que o caderno é
> TIPO 1 e o gabarito lido é o do TIPO 1. O `ans` **não** foi alterado e a
> questão segue sem explicação — são os 2 avisos do `./valida.py`. O gabarito
> publicado é o **preliminar**; quando sair o definitivo, reconferir em
> <https://conhecimento.fgv.br/concursos/navbrasil26>. Se mudar para E, basta
> escrever a explicação; se continuar C, a questão vale como anotada.

> **`cprm-ads` Q17 — resolvida em 07/08, e o modo de resolver vale de exemplo.**
> A questão das 17 caixas empilhadas depende do desenho, mas escapava da regra
> (diz "**A Figura mostra**", e a lista de dêixis só tinha o particípio). Virou
> **exceção declarada** no `importar_provas.py`, em `DEPENDE_DE_FIGURA_MANUAL`,
> e não regra nova: acrescentar os verbos no presente trancaria a `nav-med` Q23,
> a `nav-med` Q30 e a `nav-eng` Q70, que se sustentam sozinhas. Se aparecer um
> segundo caso, compare os dois antes de generalizar — regra ajustada a um
> exemplo só costuma custar caro aqui (a versão antiga da heurística trancava
> 51 questões, 45 delas sem necessidade).

> **`cprm-ads` Q59 — nomenclatura frouxa da banca.** O objeto que comporta
> ilhas (polígonos) e boias (pontos) é uma **coleção heterogênea** do Oracle
> Spatial (`SDO_GTYPE` terminado em 4, COLLECTION); "multipolígono" é
> homogêneo por definição. A alternativa marcada é a única viável, o `ans` não
> foi tocado e a explicação usa o nome correto. Não gere questão nova a partir
> dela — banco geoespacial está fora do edital.

**Marcação da banca — parcialmente recuperada em 07/08.** O `pypdf` não
preserva sublinhado, mas no PDF ele é um retângulo fino desenhado sob a
palavra, e o **PyMuPDF** lê esses desenhos: o importador agora restaura o
grifo entre `«…»`. São **18 das 42** questões que citam a marcação — entre elas
a `dataprev2024` Q16 (`«Thus,»`), a `nav-med` Q1 (os três verbos) e a Q5
(`«À medida em que»`).

As outras 24 seguem sem marca, e há uma regra a respeitar se for mexer nisso:
**ou todas as alternativas recebem marca, ou nenhuma recebe.** Marcação parcial
é pior que nenhuma — na `cnsal-ads` Q7 a única alternativa que ficaria sem
grifo era justamente o gabarito. Para essas, o caminho continua sendo a
explicação cobrindo **todas** as alternativas, que é o que mantém o item
utilizável.

**Gabaritos preliminares:** todo o `nav-med` (prova de 02/08/2026) está com
gabarito preliminar. Quando sair o definitivo, reconferir as 45 e verificar se
alguma foi anulada. O do `cprm-ads` já é o **definitivo** (08/01/2026).
