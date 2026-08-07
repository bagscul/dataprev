# Continuar de onde paramos — 07/08/2026 (fim do dia)

Arquivo de retomada. As duas pendências abertas na sessão anterior foram
**fechadas**: as 86 questões da NAV Brasil ganharam explicação, e as duas provas
achadas na busca foram importadas. Sobrou uma pendência nova, herdada da
importação. Leia na ordem: estado → pendência → o que vem depois.

---

## 0. Estado do repositório — LEIA PRIMEIRO

Antes de qualquer coisa, rode `git status` e `./valida.py`.

Números de referência (medidos em 07/08/2026, não precisa remedir):

- `banco.json` 403 · `banco-provas.json` 626 · **1007 utilizáveis no quiz**
- **11 provas reais** importadas
- `./valida.py`: 0 erros, **214 avisos** — todos da pendência abaixo
- `sub` (microtópico): 385 das 1029 questões dos dois bancos (37%)

O que entrou hoje, além das explicações (detalhe completo no `CHANGELOG.md`,
entradas de 07/08 — são três):

| arquivo | o que é |
|---|---|
| `provas/cprm-ads.pdf` + `notas/cprm-ads-mapa.md` | CPRM 2025, Analista em Geociências / ADS — **70 questões, caderno inteiro** |
| `provas/nav-med.pdf` + `notas/nav-med-mapa.md` | NAV Brasil 2026 nível médio, Operador de Torre — **45 de 60** (inglês 20, RLM 15, português 10) |
| `gabaritos/gabarito-definitivo-cprm.pdf` | gabarito **definitivo** do CPRM (08/01/2026) |
| `importar_provas.py` | quatro correções de parser (veja abaixo) |

**As quatro correções do `importar_provas.py`** importam para quem for mexer
nele: (1) o marcador de texto-base agora é reconhecido **em português**
("Atenção! O texto a seguir refere-se às duas próximas questões"); (2) e na
segunda fórmula em inglês da FGV ("Read Text IV and answer the four questions
that follow it"); (3) "Informática" entrou na lista de cabeçalhos de seção; (4)
pôster e cartum passaram a contar como figura. As duas primeiras e a terceira
**reproduzem no parser** os consertos que na véspera tinham sido feitos à mão
no JSON — e que a próxima reimportação teria desfeito em silêncio.

**Bug corrigido no caminho, vale conhecer:** o importador **não preservava o
campo `sub`**. Como a subtag de questão de prova é etiquetada à mão, qualquer
`./importar_provas.py` apagava as 82 etiquetas existentes sem avisar (foi o que
aconteceu nesta sessão; foram restauradas do git). Agora `sub` sobrevive à
reimportação, junto com `ans`, `why`, `erradas` e `anulada`.

**Garantia restabelecida:** `./importar_provas.py` (sem argumento) devolve o
`banco-provas.json` **byte-idêntico**. Se algum dia parar de devolver, é sinal
de que alguém consertou dado à mão no JSON em vez de no parser — procure a
diferença antes de commitar.

---

## 1. Pendência — explicar as 115 questões novas

Mesma situação da NAV Brasil na véspera, e o mesmo caminho de saída: as 115
questões entraram com **gabarito oficial** mas **sem `why` e sem `erradas`**.
Todas as outras nove provas do banco têm explicação completa — é o padrão do
repositório, e é o que dá valor ao erro no quiz. Hoje o quiz corrige, mas não
ensina.

São **106 questões a explicar** (as outras 9 dependem de figura e já estão fora
do sorteio). Distribuição:

| bloco | qtd | | bloco | qtd |
|---|---|---|---|---|
| português | 19 | | governança | 3 |
| RLM | 22 | | orfãos | 3 |
| inglês | 16 | | java | 3 |
| atualidades | 11 | | redes | 2 |
| segurança | 6 | | legislação / programação / frontend | 1 cada |
| arquitetura | 6 | | | |
| banco-dados | 4 | | | |
| BI | 4 | | | |
| eng-software | 4 | | | |

Para listar as pendentes a qualquer momento:

```bash
python3 -c "
import json
b=json.load(open('banco-provas.json',encoding='utf-8'))
f=[q for q in b if q.get('ans') is not None and not q.get('requer_imagem')
   and not q.get('anulada') and not (q.get('why','').strip() and q.get('erradas'))]
print(len(f)); [print(q['prova'], q['num'], q['tag']) for q in f[:10]]"
```

### O prompt

> Preciso escrever as explicações (`why` e `erradas`) das 106 questões que
> estão em `banco-provas.json` sem elas (provas `cprm-ads` e `nav-med`). Leia
> antes: `CONTINUAR-AQUI.md` §1, a seção 5 do `CONTRIBUINDO-QUESTOES.md`
> (explicação que reconstrói o raciocínio) e a seção "Estilo de questão" do
> `CLAUDE.md`.
>
> **Trabalhe em lotes de 10 questões, por bloco.** Comece pelos **específicos
> do `cprm-ads`** (31–70: segurança, arquitetura, banco-dados, BI,
> eng-software, java, redes) — são as de maior retorno, porque é cargo de TI e
> conteúdo do meu Módulo II. Depois **atualidades** (as 10 do CPRM + a Q45 do
> Teste de Turing Total), que é o bloco mais escasso. Inglês e RLM depois, e
> português por último. Ao fim de cada lote rode `./valida.py` e me diga
> quantas faltam.
>
> Regras que valem especificamente aqui:
>
> 1. **O gabarito é oficial da FGV e é intocável.** O do `cprm-ads` é o
>    **definitivo**; o do `nav-med` ainda é o **preliminar**. Se a sua análise
>    discordar da alternativa marcada como correta, **pare e me avise** — não
>    reescreva a explicação para forçar o gabarito, e não altere o campo `ans`.
>    Divergência real vira anotação, não conserto silencioso (o modelo é a
>    `nav-tec` Q58, §3 abaixo).
> 2. **`why`:** 1–3 frases, analítico — o conceito que sustenta a resposta, não
>    "a alternativa B está correta". Pode nomear o comportamento da banca.
> 3. **`erradas`:** uma entrada para cada uma das 4 alternativas erradas
>    (chaves são os índices, conferido pelo `valida.py`). Explique o **erro
>    conceitual**, não que "está errada". **Varie a abertura de cada frase** —
>    nada de "Distrator X:" repetido. Nomeie o mecanismo (inversão de par,
>    absoluto, extrapolação, troca de número) tecido na explicação.
> 4. **Não invente.** Estas são questões reais; se um item depende de um dado
>    que você não tem certeza (número de norma, artigo, versão, prêmio de 2025),
>    confira em fonte primária antes — é a regra do `CLAUDE.md`. As dez de
>    atualidades do CPRM são o caso mais exposto a isso: falam de acordo
>    EUA–Ucrânia, Declaração de Johanesburgo do BRICS, Lei 14.701, Oscar 2025 e
>    Prêmio Jabuti 2025.
> 5. **Aproveite para etiquetar:** escolha o microtópico do `subtags.py`
>    (`./quiz.py --tags` lista). Não é obrigatório em questão de prova, mas
>    fecha o ciclo do `./fraquezas.py` — e o `atualidades-socioambiental` e o
>    `backup-recuperacao`, que hoje têm **zero** questão, finalmente têm
>    candidatas.

### Contexto útil para explicar

- `notas/cprm-ads-mapa.md` e `notas/nav-med-mapa.md` trazem o **tema de cada
  questão** classificado por conteúdo, e as notas de classificação explicam por
  que RAID/backup/SO foram para `orfaos` e por que o Teste de Turing Total foi
  para `atualidades`.
- Os PDFs estão em `provas/cprm-ads.pdf` e `provas/nav-med.pdf`; os gabaritos
  em `gabaritos/gabarito-definitivo-cprm.pdf` (bloco "Análise e Desenvolvimento
  de Sistemas – **1** – Turno Manhã") e
  `gabaritos/nav-brasil-gabaritos-publicacao-v2.pdf` (Operador de Torre é a
  **primeira** tabela).
- Questões boas para conferir se o alinhamento gabarito↔alternativa continua
  certo: `cprm-ads` Q34 é **RAID 1** (o nível sem striping, gabarito B), Q46 é
  **merge sort** (D), Q43 é **esquema galáxia** (D); `nav-med` Q24 dá **2h30**
  (C) e Q47 é **present perfect passivo** (C).

---

## 2. Depois da pendência — o buraco que sobrou é só inglês

Medido contra a demanda de **10 simulados** do roteiro (cada um: 40 gerais na
proporção do edital + 30 específicos), **depois** das importações de hoje:

| bloco | pool | precisa | falta |
|---|---|---|---|
| inglês | 69 | 120 | **+51** |
| atualidades | 48 | 60 | +12 |
| português | 129 | 120 | ok |
| RLM | 65 | 50 | ok |
| legislação | 68 | 50 | ok |
| **todo o Módulo II** | — | — | **ok, déficit zero** |

O déficit total caiu de 107 para **63**, e agora está concentrado em dois
blocos em vez de quatro. **Português e RLM saíram do vermelho** — não gaste
mais busca nem geração neles.

Duas saídas, e a segunda é a que rende mais agora:

1. **Mais provas.** O prompt de busca e tudo o que já foi verificado e
   descartado ficam no `CHANGELOG.md` (entrada de 07/08, "busca de provas
   FGV"). Duas pistas ainda abertas: o caderno de **Pesquisador em Geociências**
   do mesmo CPRM (mais 5 de inglês, e o edital diz no item 12.2 que o Módulo I
   é comum a todas as áreas de Pesquisador, então basta um caderno) e a
   **PM-SP Aluno-Oficial 2025** (13/07/2025, tem prova de inglês, não cheguei a
   confirmar quantas questões). O caminho rápido é pedir ao WebFetch a lista de
   cadernos de `conhecimento.fgv.br/concursos/<slug>` — a página abre normal —
   e conferir a composição no **item 9** do edital.
2. **Gerar questão de inglês.** O plano está em `GERAR-LOTE-GERAIS.md`, com o
   aviso no topo: as cotas de lá são de antes das importações, e português e RLM
   têm de sair do lote. A metodologia e o rateio por microtópico continuam
   valendo — e em inglês o `julgamento-afirmativas` ainda tem **zero** questão.

### Regras de importação — não repita erros já cometidos

1. **Filtre "Legislação" de concurso genérico.** A legislação do seu edital é
   LGPD, Marco Civil e LAI. A de quase todo concurso é direito constitucional
   e administrativo — conteúdo fora do edital. O banco já carrega 42 questões
   assim vindas do TJRJ/MPU. Descartei 7 na NAV Brasil superior e 10 no médio
   por esse motivo.
2. **Filtre "Informática"** (Word, navegador, planilha): o Perfil 3 não tem
   esse bloco.
3. **Cheque se o Módulo I se repete entre cadernos do mesmo concurso.** Na NAV
   Brasil os dois cadernos de nível superior tinham as **mesmas 40 questões**
   de conhecimentos básicos. No CPRM, o Módulo I do Analista varia por área — e
   o do Pesquisador é comum a todas. Confirme comparando o texto e os gabaritos
   antes de importar.
4. **Classifique por conteúdo, não pelo rótulo da banca.** Na NAV Brasil
   superior a Q33 estava sob "Informática" mas cobrava impacto da IA nas
   ocupações; no CPRM a Q45 está em "Conhecimentos Específicos" mas é
   fundamentos de IA. As duas viraram `atualidades`. Só aparece lendo questão
   por questão — no `nav-med`, ao contrário, as cinco de Informática eram
   Informática mesmo.

### Fluxo de importação

```bash
# 1. PDF em provas/<nome-curto>.pdf (nome curto: vira o id da questão)
# 2. classifique e escreva notas/<nome>-mapa.md (veja notas/cprm-ads-mapa.md de modelo)
./importar_provas.py                 # SEM argumento: reescreve o arquivo inteiro
# 3. remova do banco-provas.json o que ficou fora do recorte
./gabarito.py <nome> "1-C 2-A ..."   # gabarito OFICIAL, nunca chutado
./valida.py
```

Atenção: `./importar_provas.py` com argumento **sobrescreve** o
`banco-provas.json` só com as provas passadas. Rode sempre sem argumento.
Confira o **tipo** do caderno contra o **tipo** da tabela do gabarito antes de
colar: no CPRM as tabelas se chamam "ADS – 1" e "ADS – 2", e a "1" é a TIPO 1
(conferido resolvendo a Q12 e a Q13 de RLM à mão).

---

## 3. Divergência de gabarito ainda aberta

> **`nav-tec` Q58 — divergência real, não conserto silencioso.**
> O enunciado descreve dependência transitiva (`Nome_Fabricante` →
> `ID_Fabricante` → `ID_Veiculo`) e pede o que remover para atingir a 3FN: isso
> é a letra **E**. O gabarito oficial da FGV marca **C** ("superchave que viola
> as invariantes da Forma Normal de Boyce-Codd"), que não descreve o caso.
> Conferido: o caderno é TIPO 1 e o gabarito lido é o do TIPO 1 (as demais
> questões da mesma faixa batem), então não é desalinhamento de importação. O
> `ans` **não** foi alterado e a questão segue sem explicação — são 2 dos avisos
> do `./valida.py`. O gabarito publicado é o **preliminar**
> (`nav-brasil-gabaritos-publicacao-v2.pdf`); quando sair o definitivo, reconferir
> em <https://conhecimento.fgv.br/concursos/navbrasil26> — se mudar para E, é só
> escrever a explicação; se continuar C, a questão vale como anotada.

O mesmo vale, em menor grau, para todo o `nav-med`: o gabarito é **preliminar**
(prova de 02/08/2026). Quando o definitivo sair, vale reconferir as 45 e
verificar se alguma foi anulada.

**Limitação conhecida:** o `pdftotext`/`pypdf` não preserva sublinhado, então
questões que dizem "o termo sublinhado" perdem a marcação (português da
`nav-tec` Q6/Q17/Q19 e do `nav-med` Q1 e Q6). As explicações da NAV superior
foram escritas cobrindo as cinco alternativas, o que mantém o item utilizável —
faça o mesmo nas novas.
