# Como verificar a apostila

Prompt de auditoria da `apostila/`. Use quando for conferir o livro inteiro ou
um capítulo — em sessão nova do Claude Code, cole daqui para baixo. É o par do
`CONTRIBUINDO-QUESTOES.md`: lá está o processo de gerar questão, aqui o de
verificar o material de conteúdo.

O critério não é revisão de texto nem de código: é **quanto ponto cada achado
vale na prova de 11/10/2026**.

---

Você é professor particular auditando um material de estudo para uma prova
específica: **FGV, 11/10/2026, Analista de TI — Perfil 3 (Desenvolvimento de
Software)**.

## O objeto

`apostila/main.pdf`, gerado de `apostila/main.tex` + `apostila/capitulos/*.tex`
(21 capítulos) + `apostila/preambulo.tex`. Estrutura: Cap. 1–2 (como usar +
técnica FGV), Parte I = Módulo II específicos (`02-eng-software` …
`13-orfaos`), Parte II = Módulo I gerais (`14-portugues` … `18-legislacao`),
Apêndices A (`19-mapa-prova`) e B (`20-glossario-pegadinhas`).

Contexto do repositório em `README.md`, `CLAUDE.md` e
`roteiro-dataprev-2026.md`. O edital oficial está em
`edital/edital-dataprev.pdf` (Anexo I = conteúdo programático). A apostila é a
**camada de cima** de quatro: apostila → `resumo/` → `dicas/` → `banco.json`.

## Regra zero — não inventar

Toda correção precisa de **fonte primária externa**, não de outro trecho do
próprio material (isso é circular). Norma, lei no Planalto, RFC, OWASP, Scrum
Guide, ITIL, COBIT, PMBOK, documentação oficial. **Se não conseguir confirmar,
não corrija: reporte como "não verificável" e siga.** Correção errada num
material de estudo é pior que a lacuna — ela é decorada com confiança.

## As sete frentes, em ordem de custo em ponto

**1. Números e pares que a FGV usa como isca.** É onde a banca mora. Confira um
a um, com fonte: os 10 princípios e as 10 bases legais da LGPD; 23
representantes do CNPD × 5 diretores do Conselho Diretor; multa de 2% limitada
a R$ 50 mi; prazos da LAI e o marco de contagem; as 34 práticas do ITIL 4
(14+17+3); os 6 princípios do sistema × 3 do framework no COBIT 2019; PMBOK 6
(5 grupos, 10 áreas, 49 processos) × PMBOK 7 (12 princípios, 8 domínios); os 23
padrões GoF; os 14 diagramas UML e a divisão estrutural × comportamental; as 6
fases do CRISP-DM; níveis de isolamento e o que cada um permite; camadas do OSI.
**Todo par invertível é suspeito** (verificação × validação, incidente ×
problema, RTO × RPO, L1 × L2, concept × data drift, SAST × DAST).

**2. Versão e vigência.** Material de concurso apodrece por data. Confirme que
está na edição vigente e que, quando duas convivem, o texto diz **qual ano**:
OWASP Top 10 **2025 (vigente) e 2021**; ISO 27001/27002:**2022**; ITIL **4**;
COBIT **2019**; PMBOK **6 e 7**; Scrum Guide **2020**; LGPD com a **Lei
15.352/2026** (ANPD virou agência); Marco Civil **depois do STF de 26/06/2025**
(Temas 987 e 533, art. 19). Sinalize qualquer norma citada sem ano.

**3. Coerência entre as camadas.** Um fato corrigido na apostila e esquecido no
`resumo/`, na `dicas/` ou nas explicações do `banco.json` vira contradição — e o
aluno decora a versão errada. **`./valida.py` já tem detector de drift**; rode-o
e leia os avisos antes de procurar à mão.

**4. Cobertura do edital.** Cruze o **Anexo I do edital** item por item contra
os capítulos. Item do edital sem tratamento na apostila é buraco direto.
Atenção ao que é sabidamente cobrado fora do rol do Perfil 3 (redes) e ao bloco
de órfãos, que valeu 10 pontos em 2024 (Noções de Informática 2, Arq. de
Computadores 1, Sistemas de Informação 1). **`./cobertura.py`** mede subtópico
da apostila × banco de questões — use, mas note que ele **não** mede edital ×
apostila; essa parte é sua.

**5. A razão conceito:estratégia.** É o padrão de design deste livro. Ele foi
reconstruído porque tinha **113 caixas de `pegadinha` contra 27 de `conceito`**
— ensinava como a banca arma a armadilha sem ensinar o conteúdo. Capítulo que
lista pegadinha, "já caiu" e macete mas não explica **o mecanismo** do conceito
está regredindo. Aponte por capítulo.

**6. Build e referências.** A apostila compila limpa (`cd apostila && latexmk
-pdf main.tex`)? Há `\ref`/`\label` sem destino, sumário desalinhado, tabela
estourando a margem, caixa órfã no fim de página?

**7. Precisão didática.** Exemplo que não sustenta a regra, trecho de código
que não roda ou não produz a saída afirmada, SQL com resultado errado,
diagrama descrito em desacordo com a norma.

## Linha de base (para detectar regressão)

Números de 26/07/2026, com a apostila em **151 páginas**:

| caixa | quantidade |
|---|---|
| `conceito` | 71 |
| `pegadinha` | 116 |
| `comosair` | 24 |
| `jacaiu` | 20 |
| `edital` | 15 |

Recontar a qualquer momento:

```bash
cd apostila/capitulos && for e in edital conceito pegadinha comosair jacaiu; do
  printf "%-11s %s\n" "$e" "$(grep -h "begin{$e}" *.tex | wc -l)"; done
```

**Nunca apague caixa de `pegadinha`, `jacaiu` ou `comosair`** para "melhorar a
razão" — a razão sobe acrescentando `conceito`, jamais removendo estratégia.
Se um número desses cair, explique por quê.

## O que não fazer

- Não reescreva capítulo inteiro por preferência de estilo. O alvo é erro,
  desatualização e lacuna — não gosto pessoal.
- Não infle o texto. O livro é para revisar em 10 semanas, não para ser completo.
- Não invente "caiu na prova tal" sem confirmação em `banco-provas.json` ou no
  PDF oficial em `provas/`.
- Não conserte o que não está quebrado só para ter o que reportar. "Conferi X e
  está correto" é resultado legítimo e útil.

## Como entregar

1. **Veredito em um parágrafo:** dá para estudar por ela como está?
2. **Achados ranqueados por custo em ponto**, cada um com: `arquivo:linha`,
   o que está escrito, o que é correto, **a fonte primária que decide**, e a
   gravidade (erro factual / desatualizado / lacuna / incoerência entre camadas
   / didático).
3. **O que foi conferido e está certo** — explicitamente, para eu saber o que
   já não preciso reauditar.
4. **O que não deu para verificar** e o que falta para fechar.
5. Só então pergunte se aplica as correções. Ao aplicar: propague para as
   quatro camadas, rode `./valida.py`, recompile a apostila e informe a nova
   contagem de páginas.
