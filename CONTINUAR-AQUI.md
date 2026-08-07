# Continuar de onde paramos — 07/08/2026 (noite, depois da importação)

Arquivo de retomada. As quatro provas verificadas na busca da noite **foram
importadas**, e o inglês quase fechou: falta 18 de 51. Sobrou a pendência de
sempre depois de importar — as **73 questões novas estão sem explicação**.
Leia na ordem: estado → pendência → o que vem depois.

---

## 0. Estado do repositório — LEIA PRIMEIRO

Antes de qualquer coisa, rode `git status` e `./valida.py`.

Números de referência (medidos em 07/08/2026, não precisa remedir):

- `banco.json` 403 · `banco-provas.json` 700 · **1080 utilizáveis no quiz**
- **15 provas reais** importadas
- `./valida.py`: 0 erros, **148 avisos** — 73 questões novas sem explicação
  (a pendência do §1) mais os 2 da `nav-tec` Q58 (§3)
- `sub` (microtópico): **467 das 1029** questões dos dois bancos (45%)

O que entrou no dia (detalhe no `CHANGELOG.md`, cinco entradas de 07/08): as
provas `cprm-ads` e `nav-med`, as quatro correções do `importar_provas.py`, as
**106 explicações** que fecharam a pendência daquelas duas e, à noite, a busca
que trouxe `epe-ti`, `rfb-ana`, `rfb-aud` e `cprm-pesq` (+74 questões, o
inglês de 69 para 102).

Garantias que valem conhecer antes de mexer:

- `./importar_provas.py` **sem argumento** devolve o `banco-provas.json`
  byte-idêntico (conferido depois das explicações). Se parar de devolver, é
  sinal de que alguém consertou dado à mão no JSON em vez de no parser.
- A reimportação **preserva** `ans`, `why`, `erradas`, `anulada` e `sub`.
  **Não preserva `requer_imagem`** — ver a ressalva da Q17, logo abaixo.

---

## 1. Pendência — explicar as 73 questões novas

As quatro provas entraram com **gabarito definitivo** mas **sem `why` e sem
`erradas`**. É a mesma situação das duas importações anteriores, e o mesmo
caminho de saída. Distribuição:

| bloco | qtd | | bloco | qtd |
|---|---|---|---|---|
| inglês | 33 | | banco-dados | 4 |
| eng-software | 12 | | programação | 4 |
| arquitetura | 8 | | frontend | 2 |
| BI | 5 | | redes | 1 |
| segurança | 5 | | | |

Para listar as pendentes a qualquer momento:

```bash
python3 -c "
import json
b=json.load(open('banco-provas.json',encoding='utf-8'))
f=[q for q in b if q.get('ans') is not None and not q.get('requer_imagem')
   and not q.get('anulada') and not (q.get('why','').strip() and q.get('erradas'))]
print(len(f)); [print(q['prova'], q['num'], q['tag']) for q in f[:10]]"
```

**Como fazer**, que é o que funcionou nas duas vezes anteriores: lotes de 10
por bloco, começando pelos **específicos da `epe-ti`** (36–80: são de cargo de
TI de 2024 e batem no seu Módulo II), depois o **inglês** das quatro. Ao fim de
cada lote, `./valida.py`. As regras estão na seção 5 do
`CONTRIBUINDO-QUESTOES.md` e em "Estilo de questão" do `CLAUDE.md`; o gabarito
é oficial e **intocável** — divergência vira anotação, como a `nav-tec` Q58.

Uma questão de figura na faixa nova: `epe-ti` Q58 (malwares) saiu do sorteio
sozinha, marcada pelo importador. Não há o que editar nela.

---

## 2. Depois da pendência — falta pouco, e só de dois blocos

Medido contra a demanda de **10 simulados** do roteiro (cada um: 40 gerais na
proporção do edital + 30 específicos):

| bloco | pool | precisa | falta |
|---|---|---|---|
| inglês | **102** | 120 | +18 |
| atualidades | 48 | 60 | +12 |
| português | 129 | 120 | ok |
| RLM | 65 | 50 | ok |
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

**Depois de importar, explique no mesmo dia.** As duas últimas importações
deixaram 86 e 106 questões sem `why`/`erradas` para o dia seguinte. O caminho
que funcionou nas duas vezes: lotes de 10 por bloco, começando pelos
específicos (maior retorno), atualidades depois, português por último; a cada
lote, `./valida.py`.

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

> **`cprm-ads` Q17 depende da figura e não está marcada como tal.** São as 17
> caixas cúbicas empilhadas: o enunciado cita "a Figura", mas o importador não
> extraiu a imagem nem ligou o `requer_imagem`. A explicação já está escrita
> pelo caminho que a questão pede (contar as 12 caixas visíveis e subtrair de
> 17), só que no quiz o item aparece sem o desenho. Como `requer_imagem` **não
> sobrevive à reimportação**, o conserto é na regra do `importar_provas.py`, e
> não à mão no JSON.

> **`cprm-ads` Q59 — nomenclatura frouxa da banca.** O objeto que comporta
> ilhas (polígonos) e boias (pontos) é uma **coleção heterogênea** do Oracle
> Spatial (`SDO_GTYPE` terminado em 4, COLLECTION); "multipolígono" é
> homogêneo por definição. A alternativa marcada é a única viável, o `ans` não
> foi tocado e a explicação usa o nome correto. Não gere questão nova a partir
> dela — banco geoespacial está fora do edital.

**Limitação conhecida do extrator:** `pdftotext`/`pypdf` não preserva
sublinhado, então questões que dizem "o termo sublinhado" perdem a marcação
(português da `nav-tec` Q6/Q17/Q19 e do `nav-med` Q1 e Q6). As explicações
dessas questões foram escritas cobrindo **todas** as alternativas, o que
mantém o item utilizável — faça o mesmo nas próximas.

**Gabaritos preliminares:** todo o `nav-med` (prova de 02/08/2026) está com
gabarito preliminar. Quando sair o definitivo, reconferir as 45 e verificar se
alguma foi anulada. O do `cprm-ads` já é o **definitivo** (08/01/2026).
