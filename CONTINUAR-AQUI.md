# Continuar de onde paramos — 07/08/2026

Arquivo de retomada. A sessão anterior acabou com duas pendências abertas e
**nada commitado**. Leia as três seções na ordem: estado → pendência 1 →
pendência 2.

---

## 0. Estado do repositório — LEIA PRIMEIRO

**Há trabalho não commitado de dois dias (06 e 07/08).** Antes de qualquer
coisa, rode `git status` e `./valida.py`. Se estiver tudo íntegro, o commit
sugerido é:

```bash
git add -A && git commit -m "subtags viram taxonomia do edital, fraquezas.py e NAV Brasil 2026 importada"
```

O que mudou, em uma linha cada (detalhe completo no `CHANGELOG.md`, entradas de
06 e 07/08 — **leia as duas antes de mexer em qualquer coisa**):

| arquivo | o que é |
|---|---|
| `subtags.py` (novo) | vocabulário fechado de **167 microtópicos**, derivado das seções do `teoria/` e da apostila |
| `fraquezas.py` (novo) | ranqueia microtópicos por erro registrado; `--prompt` monta briefing de geração |
| `GERAR-LOTE-GERAIS.md` (novo) | plano de geração com cotas por microtópico — **as cotas estão desatualizadas**, veja §2 |
| `valida.py` | `sub` obrigatório em questão nova (`SUB_OBRIGATORIA_APOS = 403`, bloqueia); checa subtag no caderno de erros |
| `quiz.py` | escreve `- **sub:**` no caderno; `--tags` lista o vocabulário; filtro por microtópico com fallback por keyword |
| `status.py` | mostra o "ponto fraco" do dia |
| `banco.json` / `banco-provas.json` | 497 questões ganharam `sub`; +89 questões da NAV Brasil |
| `notas/nav-{tec,eng}-mapa.md` (novos) | classificação questão a questão das provas novas |

Números de referência (medidos em 07/08, não precisa remedir):

- `banco.json` 403 · `banco-provas.json` 511 · **901 utilizáveis no quiz**
- 9 provas reais importadas
- `./valida.py`: 0 erros, **172 avisos** — todos da pendência 1

---

## 1. Pendência 1 — explicar as 86 questões novas

### O problema

As 89 questões da NAV Brasil entraram com gabarito oficial, mas **sem `why` e
sem `erradas`**. Todas as outras sete provas do banco têm explicação completa —
é o padrão do repositório, e é o que dá valor ao erro no quiz. Hoje o quiz
corrige, mas não ensina.

São **86 questões** a explicar (as outras 3 dependem de figura e já estão fora
do sorteio). Distribuição:

| bloco | qtd | | bloco | qtd |
|---|---|---|---|---|
| portugues | 20 | | arquitetura | 6 |
| eng-software | 17 | | bi | 3 |
| governanca | 9 | | frontend / atualidades / orfaos | 2 cada |
| rlm | 8 | | java / redes / legislacao | 1 cada |
| banco-dados | 7 | | | |
| seguranca | 7 | | | |

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

> Preciso escrever as explicações (`why` e `erradas`) das 86 questões da NAV
> Brasil 2026 que estão em `banco-provas.json` sem elas (provas `nav-tec` e
> `nav-eng`). Leia antes: `CONTINUAR-AQUI.md` §1, a seção 5 do
> `CONTRIBUINDO-QUESTOES.md` (explicação que reconstrói o raciocínio) e a seção
> "Estilo de questão" do `CLAUDE.md`.
>
> **Trabalhe em lotes de 10 questões, por bloco**, na ordem: eng-software,
> banco-dados, arquitetura, seguranca, governanca, bi, o resto, e português/RLM
> por último. Ao fim de cada lote rode `./valida.py` e me diga quantas faltam.
>
> Regras que valem especificamente aqui:
>
> 1. **O gabarito é oficial da FGV e é intocável.** Se a sua análise discordar
>    da alternativa marcada como correta, **pare e me avise** — não reescreva a
>    explicação para forçar o gabarito, e não altere o campo `ans`. Divergência
>    real vira anotação, não conserto silencioso.
> 2. **`why`:** 1–3 frases, analítico — o conceito que sustenta a resposta, não
>    "a alternativa B está correta". Pode nomear o comportamento da banca.
> 3. **`erradas`:** uma entrada para cada uma das 4 alternativas erradas
>    (chaves são os índices, conferido pelo `valida.py`). Explique o **erro
>    conceitual**, não que "está errada". **Varie a abertura de cada frase** —
>    nada de "Distrator X:" repetido. Nomeie o mecanismo (inversão de par,
>    absoluto, extrapolação, troca de número) tecido na explicação.
> 4. **Não invente.** Estas são questões reais; se um item depende de um dado
>    que você não tem certeza (número de norma, artigo, versão), confira em
>    fonte primária antes — é a regra do `CLAUDE.md`.
> 5. **Aproveite para etiquetar:** se a questão não tiver `sub`, escolha o
>    microtópico do `subtags.py` (`./quiz.py --tags` lista). Não é obrigatório
>    em questão de prova, mas fecha o ciclo do `./fraquezas.py`.
>
> Meta: `./valida.py` sair de 172 avisos para 0.

### Contexto útil para explicar

- `notas/nav-tec-mapa.md` e `notas/nav-eng-mapa.md` já trazem o **tema de cada
  questão** classificado por conteúdo — use como ponto de partida.
- As provas em PDF estão em `provas/nav-tec.pdf` e `provas/nav-eng.pdf`; o
  gabarito oficial, em `gabaritos/nav-brasil-gabaritos-publicacao-v2.pdf`.
- Questão boa para conferir se o alinhamento gabarito↔alternativa está certo:
  `nav-eng` Q42 é **Adapter** (gabarito B), `nav-eng` Q62 é **Gestão de
  Incidentes** (B), `nav-tec` Q65 é **perda total no RAID 0** (B).

---

## 2. Pendência 2 — procurar mais provas da FGV de nível superior

### Onde o déficit está hoje

Medido contra a demanda de **10 simulados** do roteiro (cada um: 40 gerais na
proporção do edital + 30 específicos):

| bloco | pool | precisa | falta |
|---|---|---|---|
| inglês | 53 | 120 | **+67** |
| atualidades | 37 | 60 | +23 |
| português | 110 | 120 | +10 |
| RLM | 43 | 50 | +7 |
| legislação | 67 | 50 | ok |
| **todo o Módulo II** | — | — | **ok, déficit zero** |

**Consequência prática:** procurar prova por causa do Módulo II não vale mais a
pena — já está coberto. O alvo é **inglês**, e depois atualidades.

### O prompt

> Preciso achar mais provas da FGV para importar, mirando o Módulo I do meu
> edital (Dataprev 2026, Perfil 3 — prova em 11/10/2026). Leia
> `CONTINUAR-AQUI.md` §2 antes, para não refazer busca que já foi feita.
>
> Prioridade absoluta: **língua inglesa**. Depois: atualidades/IA. Português e
> RLM já estão quase resolvidos e o Módulo II está coberto — não gaste busca
> neles.
>
> **Prefira provas de cargos de tecnologia / desenvolvimento / software /
> computação.** Além de o Módulo II sair calibrado no meu assunto, o inglês
> dessas provas vem com vocabulário técnico — que é o que a Dataprev cobra
> (leitura de manual, documentação de API e artigo de TI), e não o inglês
> comercial ou geral. Ordem de prioridade:
>
> 1. **cargo de TI + tem inglês** — é o alvo; é exatamente o perfil da Dataprev
>    2024, que já está no banco e é a prova mais valiosa que tenho;
> 2. **tem inglês, mas o cargo não é de TI** — serve, com a ressalva de que o
>    vocabulário é de outro domínio (foi o caso da NAV Brasil);
> 3. **cargo de TI sem inglês** — retorno baixo agora, porque o Módulo II já
>    não tem déficit. Só vale se a prova for muito recente, e aí por calibração
>    de estilo, não por volume.
>
> Lugares onde a FGV costuma cobrar TI em nível superior, para orientar a
> varredura: Dataprev, Serpro, analista de TI de tribunais (TJ, TRT, TRE),
> assembleias legislativas, agências reguladoras, MPU/MPE, bancos públicos e
> prefeituras de capital.
>
> Critérios: banca **FGV** (o repositório é calibrado só para ela), **nível
> superior** de preferência, prova **já aplicada com gabarito oficial
> publicado**, e caderno em PDF baixável.
>
> **Método — vá pelos editais no site da FGV, não por notícia de cursinho.**
> Percorra os concursos já aplicados em <https://conhecimento.fgv.br/concursos>,
> e para cada um abra o **edital** e leia a tabela de composição da prova antes
> de decidir se vale baixar o caderno. Notícia erra: nesta sessão uma delas deu
> "inglês 20, RLM 15" como se fosse do nível superior do NAV Brasil, e o edital
> mostrou que era do nível médio — o nível superior não tem inglês nenhum.
>
> Para cada prova que passar no filtro, me diga: nome, data de aplicação,
> quantas questões de cada disciplina do meu Módulo I, e os links do caderno e
> do gabarito.

### Detalhes operacionais do site da FGV (custaram tempo na sessão passada)

- As páginas de concurso (`conhecimento.fgv.br/concursos/<slug>`) são
  **renderizadas por JavaScript**: buscar o conteúdo delas com WebFetch volta
  vazio. Use busca restrita ao domínio (`allowed_domains`) para achar o link
  direto do PDF, e então baixe o PDF.
- Editais, cadernos e gabaritos ficam todos sob
  `https://conhecimento.fgv.br/sites/default/files/concursos/<arquivo>.pdf`.
- O WebFetch não lê o texto desses PDFs (voltam como binário), **mas salva o
  arquivo em disco** e informa o caminho. Use `pdftotext -layout <arquivo>` e
  leia o texto — foi assim que a composição do NAV Brasil foi conferida.
- No edital, a tabela de composição está no **item 9** ("O quadro a seguir
  apresenta as disciplinas e o número de questões para os cargos de nível
  superior"). O conteúdo programático por cargo está no **Anexo II**.
- Cuidado com o nome do cargo na busca: o edital do NAV Brasil escreve
  "Engenheiro Software", sem o "de" — procurar por "engenheiro de software" não
  achava nada.

### O que já foi verificado — não repita

**Achado e ainda não baixado (melhor retorno disponível):**

- **NAV Brasil 2026, caderno de NÍVEL MÉDIO** — cargo *Técnico de Navegação
  Aérea – Operador de Torre de Controle*, 60 questões: **inglês 20**, RLM 15,
  português 10. Mesma aplicação de 02/08/2026 cujos cadernos de nível superior
  já foram importados. Levaria inglês de 53 → 73, e zeraria português e RLM.
  Página: <https://conhecimento.fgv.br/concursos/navbrasil26> · gabaritos:
  <https://conhecimento.fgv.br/sites/default/files/concursos/nav-brasil-gabaritos-publicacao-v2.pdf>
  *Ressalva:* é nível médio, então o texto é mais simples que o da sua prova;
  o inglês é de comércio exterior/logística, não de TI. As habilidades cobradas
  (skimming, scanning, inferência, sinonímia, coesão) são as mesmas.

**Já verificado e descartado:**

| prova | por quê |
|---|---|
| CNU 2025 (FGV) | não tem inglês; conhecimentos gerais são português + direito + realidade brasileira |
| INB 2026 (FGV) | tem 10 de inglês para nível superior, mas **o edital ainda não saiu** — prova não aplicada |
| BNDES | último concurso foi **Cesgranrio**, não FGV |
| PSS IBGE (FGV) | é FGV mesmo (PSS nº 04/2025, provas em 2026), mas APM e SCQ são **nível médio** e não têm inglês |
| SEEC-RN 2025 — Professor de Inglês | inglês avançado/pedagógico, calibração errada para o seu exame |
| PM-SP Aluno-Oficial 2025 (FGV, 13/07/2025) | **tem prova de inglês** — não cheguei a confirmar quantas questões. Vale checar |

### Regras de importação — não repita erros já cometidos

1. **Filtre "Legislação" de concurso genérico.** A legislação do seu edital é
   LGPD, Marco Civil e LAI. A de quase todo concurso é direito constitucional
   e administrativo — conteúdo fora do edital. O banco já carrega 42 questões
   assim vindas do TJRJ/MPU, e elas ficaram sem microtópico justamente por isso.
   Na NAV Brasil eu descartei 7 por esse motivo.
2. **Filtre "Informática"** (Word, navegador, planilha): o Perfil 3 não tem
   esse bloco.
3. **Cheque se o Módulo I se repete entre cadernos do mesmo concurso.** Na NAV
   Brasil os dois cadernos de nível superior tinham as **mesmas 40 questões**
   de conhecimentos básicos — importar os dois criaria 40 duplicatas. Confirme
   comparando o texto e os gabaritos antes de importar.
4. **Classifique por conteúdo, não pelo rótulo da banca.** Na NAV Brasil a Q33
   estava sob "Informática" mas cobrava impacto da IA nas ocupações — é
   `atualidades`, o bloco mais escasso. Só apareceu lendo questão por questão.

### Fluxo de importação

```bash
# 1. PDFs em provas/<nome-curto>.pdf (nome curto: vira o id da questão)
# 2. classifique e escreva notas/<nome>-mapa.md (veja notas/nav-tec-mapa.md de modelo)
./importar_provas.py                 # SEM argumento: reescreve o arquivo inteiro
# 3. remova do banco-provas.json o que ficou fora do recorte
./gabarito.py <nome> "1-C 2-A ..."   # gabarito OFICIAL, nunca chutado
./valida.py
```

Atenção: `./importar_provas.py` com argumento **sobrescreve** o
`banco-provas.json` só com as provas passadas. Rode sempre sem argumento.

---

## 3. Depois das duas pendências

Quando inglês e atualidades forem o que sobrou, o plano de geração está em
`GERAR-LOTE-GERAIS.md` — mas **as cotas de lá estão desatualizadas**: foram
dimensionadas antes da importação da NAV Brasil, quando faltavam 137 questões e
o alvo era 100 por bloco. Hoje faltam 107, quase tudo inglês. Recalcule antes
de usar; a metodologia e as cotas por microtópico continuam válidas.
