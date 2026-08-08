# Continuar de onde paramos — 07/08/2026 (fim do dia, segunda sessão)

Arquivo de retomada. **As frentes A, B e C estão fechadas**; a D depende de um
fato externo que ainda não saiu. Não há dívida técnica aberta. Leia na ordem:
estado → o que fazer a seguir → ressalvas.

> **A, B e C: FEITAS.** A **A** (a teoria que faltava: catálogo de ataques e de
> malware, complexidade ciclomática, code smells, JMeter) entrou nas quatro
> camadas. A **B** zerou o déficit de questões: inglês 102 → **120** e
> atualidades 48 → **60**, exatamente a demanda dos 10 simulados. A **C** levou
> a etiquetagem `sub` de 48% para **80%** do acervo, com revisão à mão das 345
> propostas. Detalhe das três no `CHANGELOG.md` (duas entradas de 07/08).
>
> **Sobra a frente D**, que não é trabalho: é espera. Ver §2.

---

## 0. Estado do repositório — LEIA PRIMEIRO

Antes de qualquer coisa, rode `git status` e `./valida.py`.

Números de referência (medidos em 07/08/2026, não precisa remedir):

- `banco.json` **433** · `banco-provas.json` 700 · **1109 utilizáveis no quiz**
- **15 provas reais** importadas, todas com explicação completa
- `./valida.py`: 0 erros, **2 avisos** — os dois da `nav-tec` Q58 (§3) — mais
  **6 avisos de forma** que nasceram em 08/08 com o piso novo do `longa_min`:
  não são regressão, são o diagnóstico do vazamento invertido (o banco está em
  5% de correta-mais-longa contra 33% da prova real). Somem sozinhos conforme os
  próximos lotes entrarem na faixa 18–28%; ver `CONTRIBUINDO-QUESTOES.md` §3
- `sub` (microtópico): **902 das 1133** questões dos dois bancos (**80%**),
  cobrindo 153 dos **168** microtópicos
- pool por bloco geral: inglês **120**, atualidades **60**, português 129,
  RLM 64, legislação 68 — **déficit zero** contra os 10 simulados

Garantias que valem conhecer antes de mexer:

- `./importar_provas.py` **sem argumento** devolve o `banco-provas.json`
  idêntico — conferido de novo depois da etiquetagem, que gravou `sub` em 514
  questões de prova. Se parar de devolver, é sinal de que alguém consertou dado
  à mão no JSON em vez de no parser.
- A reimportação **preserva** `ans`, `why`, `erradas`, `anulada` e `sub`.
  **Não preserva `requer_imagem`** — ver a ressalva da Q17, no §3.
- Texto-base: o parser reconhece **seis** marcas. Quatro trazem a contagem na
  própria fórmula; as duas mais novas (RFB e CPRM) não trazem, e nelas o alcance
  sai da posição. Se for mexer nisso, confira o efeito com um diff do
  `banco-provas.json` antes de commitar: na primeira tentativa a regra espalhou
  o texto da redação do CPRM por cima de 30 questões objetivas.
- `SUB_OBRIGATORIA_APOS` (no `valida.py`) caiu de 403 para **395**: questão
  nova sem `sub` é erro, não aviso.

---

## 1. O que fazer a seguir

Não há frente grande em aberto. O que resta é estudo e manutenção, em ordem de
retorno:

1. **Estudar** — é a única frente que importa agora. `./quiz.py`, e ao errar,
   a entrada em `erros/<bloco>.md` (o quiz já grava sozinho). Com 80% do banco
   etiquetado, o `./fraquezas.py` finalmente enxerga o acervo inteiro: o ranking
   dele passou a ser confiável para escolher o que revisar.
2. **Frente D — vigiar dois gabaritos** (§2). Custa dois minutos por vez e não
   depende de nada aqui dentro.
3. **As 231 questões ainda sem `sub`** — resto duro de propósito, não descuido.
   São de dois tipos: (a) assunto que o vocabulário não descreve (stored
   procedure, função determinística, apassivação, decorator do Python); (b)
   assunto **fora do edital**, herdado do TJRJ e do MPU (direito constitucional
   e administrativo — o banco carrega 42 questões assim). Microtópico novo
   **nasce de erro real ou de seção existente no livro** (foi assim que o
   `ataques-malware` nasceu, da seção que a frente A escreveu); não invente
   recorte só para zerar o percentual.
4. **Mais provas, só se aparecer prova nova.** A busca já esgotou o que havia:
   sobrou apenas a **PM-SP Aluno-Oficial 2025**, que não é da área de tecnologia
   e cuja contagem de inglês nunca foi confirmada — e com o déficit zerado, ela
   perdeu o motivo de existir. Os outros dois cadernos de TI da EPE 2024
   (Infraestrutura e Segurança; Ciência de Dados) **não trazem inglês novo** (o
   Módulo I é o mesmo do caderno de Soluções, conferido), mas os específicos
   são diferentes e alimentariam `bi` e `seguranca` — é a única pista com
   retorno real, se um dia fizer falta.

**O que NÃO fazer**, tudo já decidido e medido:

- **não gerar questão de blocos gerais**: os cinco estão em cima ou acima da
  demanda dos 10 simulados. O `GERAR-LOTE-GERAIS.md` está marcado como
  encerrado no topo — leia o aviso antes de reabrir;
- não mexer na tabela OWASP da apostila (está correta, inclusive na ausência do
  CSRF, que saiu da lista em 2017 e vive dentro do A01);
- não marcar `requer_imagem` à mão no JSON: o campo **não** sobrevive à
  reimportação (o conserto é no `importar_provas.py`, veja o §3);
- não alterar `ans` para acomodar análise própria — divergência de gabarito
  vira anotação, como a `nav-tec` Q58;
- não etiquetar `sub` no escuro. A passada automática do dia 07/08 propôs 345
  etiquetas e **34 estavam erradas** — e erradas no pior lugar, no par que a FGV
  inverte (CAP virando `propriedades-acid`, DIP virando `ecossistema-spring`).
  Etiqueta errada distorce o `./fraquezas.py`; ausência, não.

---

## 2. Frente D — os dois gabaritos a vigiar

Único item aberto, e depende da FGV, não do repositório.

- **`nav-med`** (prova de 02/08/2026): todo o caderno está com gabarito
  **preliminar**. Quando sair o definitivo, reconferir as 45 questões e checar
  anulações.
- **`nav-tec` Q58**: divergência real registrada (§3). Se o definitivo mudar
  para **E**, basta escrever a explicação e o `./valida.py` zera os 2 avisos.

Os dois em <https://conhecimento.fgv.br/concursos/navbrasil26>. **Conferido em
07/08/2026 (fim do dia): só há o gabarito preliminar, publicado em 03/08, com
recursos encerrados em 04/08.** Não adianta reconferir de hora em hora — vale
olhar uma vez por semana.

O do `cprm-ads` já é o **definitivo** (08/01/2026), não precisa vigiar.

---

## 3. Ressalvas registradas — não são bugs a consertar às pressas

> **`nav-tec` Q58 — divergência real de gabarito, não conserto silencioso.**
> O enunciado descreve dependência transitiva (`Nome_Fabricante` →
> `ID_Fabricante` → `ID_Veiculo`) e pede o que remover para atingir a 3FN: é a
> letra **E**. O gabarito oficial marca **C** ("superchave que viola as
> invariantes da FNBC"), que não descreve o caso. Conferido que o caderno é
> TIPO 1 e o gabarito lido é o do TIPO 1. O `ans` **não** foi alterado e a
> questão segue sem explicação — são os 2 avisos do `./valida.py`. Quando sair o
> definitivo: se mudar para E, basta escrever a explicação; se continuar C, a
> questão vale como anotada.

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
> Spatial (`SDO_GTYPE` terminado em 4, COLLECTION); "multipolígono" é homogêneo
> por definição. A alternativa marcada é a única viável, o `ans` não foi tocado
> e a explicação usa o nome correto. Não gere questão nova a partir dela —
> banco geoespacial está fora do edital.

**Marcação da banca — parcialmente recuperada em 07/08.** O `pypdf` não
preserva sublinhado, mas no PDF ele é um retângulo fino desenhado sob a
palavra, e o **PyMuPDF** lê esses desenhos: o importador restaura o grifo entre
`«…»`. São **18 das 42** questões que citam a marcação — entre elas a
`dataprev2024` Q16 (`«Thus,»`), a `nav-med` Q1 (os três verbos) e a Q5
(`«À medida em que»`).

As outras 24 seguem sem marca, e há uma regra a respeitar se for mexer nisso:
**ou todas as alternativas recebem marca, ou nenhuma recebe.** Marcação parcial
é pior que nenhuma — na `cnsal-ads` Q7 a única alternativa que ficaria sem
grifo era justamente o gabarito. Para essas, o caminho continua sendo a
explicação cobrindo **todas** as alternativas, que é o que mantém o item
utilizável.

---

## 4. Se for gerar questão nova mesmo assim

Duas coisas aprendidas no lote de 07/08, que economizam retrabalho:

1. **Rode `./valida.py --novas <N>` a cada lote pequeno.** O lote de 30 saiu com
   "correta é a mais longa" em **15 de 30** (o esperado é ~20%) — é o vazamento
   de forma típico de texto gerado, e sai barato de corrigir enquanto o lote é
   pequeno: encurte a correta ou alongue um distrator. Ficou em 5 de 30, e os
   cinco restantes são empate de comprimento em alternativa de uma palavra, onde
   não há o que ajustar.
   **Correção de 08/08:** 5 de 30 é *baixo demais*, não "ótimo". O alvo é a faixa
   **18–28%**, e o banco inteiro havia caído a 5% (java, legislação, arquitetura,
   redes e RLM em 0%) porque a regra só tinha teto. A prova real da FGV está em
   33%, então banco em 0% ensina o reflexo invertido. O `valida.py` ganhou piso
   (`longa_min`) e agora acusa os dois lados — não "conserte" mais um lote
   encurtando a correta por reflexo; só mexa quando ela for verbosa de fato
   (é o aviso de ratio ≥1,7× que aponta isso).
2. **Atualidades exige fonte primária com data, e ela muda.** No lote de 07/08,
   três fatos tinham virado no semestre: o AI Act foi **alterado** pelo
   Regulamento (UE) 2026/1744 (alto risco do Anexo III adiado para 02/12/2027,
   mas transparência do art. 50 valendo desde 02/08/2026); a **CVM 244**
   (29/05/2026) acabou com a obrigatoriedade do relatório ISSB que valeria em
   2026; e o **PL 2338/2023** segue em tramitação na Câmara (dado aberto,
   17/06/2026). Resumo de terceiro não pega nenhum dos três a tempo.
