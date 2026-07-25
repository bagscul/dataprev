# Atualidades e Inteligência Artificial — resumo

> **Edital (Módulo I, 6 questões — NOVO em 2026):** (1) tópicos atuais de
> segurança, transportes, política, economia, sociedade, educação, saúde,
> cultura, tecnologia, energia, relações internacionais, **desenvolvimento
> sustentável e ecologia**; (2) **Inteligência Artificial: fundamentos e
> aplicações** — conceitos de IA, aprendizado de máquina, modelos generativos
> e de linguagem (LLMs), **ética, governança e privacidade em IA**.
> **Novidade importante:** IA saiu do específico e entrou nas gerais.

## Parte 1 — Atualidades (viés socioambiental)

A FGV puxa fortemente para **sustentabilidade, meio ambiente, ESG** e temas
socioambientais, e costuma cobrar no formato **julgar afirmativas** (V/F, "está
correto o que se afirma em I, II, III").

Temas quentes prováveis (2025–2026):
- **Sustentabilidade e clima:** COPs, transição energética, ESG,
  descarbonização; impacto ambiental de **data centers** (consumo de energia
  e água — tema que já caiu na Dataprev 2024).
- **Cidades-esponja**, racismo ambiental, justiça climática.
- **Economia e tecnologia:** IA na economia, empregos, regulação de
  plataformas; geopolítica (guerras, BRICS, G20).
- **Brasil:** políticas públicas, marcos regulatórios recentes.

Pegadinha de atualidades: o item com **absoluto** ("invariavelmente",
"todos", "sempre", "nunca") costuma ser o falso.

## Parte 2 — Fundamentos de IA (novo, alto retorno)

### Conceitos

- **IA:** sistemas que executam tarefas que exigiriam inteligência humana.
- **Machine Learning (ML):** subcampo em que o sistema **aprende de dados** e
  melhora com a experiência, sem ser explicitamente programado.
- **Deep Learning:** ML com **redes neurais profundas** (muitas camadas).
- Relação: IA ⊃ ML ⊃ Deep Learning.

### Tipos de aprendizado

| Tipo | Dados | Objetivo | Exemplos |
|---|---|---|---|
| **Supervisionado** | rotulados | prever rótulo | classificação, regressão |
| **Não supervisionado** | sem rótulo | achar estrutura | clustering (K-Means), associação, PCA |
| **Por reforço** | recompensa/punição | política ótima | agentes, jogos |

Pegadinha: supervisionado usa dados **rotulados**; não supervisionado, **sem
rótulo**. A FGV troca os dois. "Aprende com os dados e melhora ao longo do
tempo" = **redes neurais/ML**, não lógica booleana nem programação linear.

### Modelos generativos e LLMs

- **Modelos generativos:** geram conteúdo novo (texto, imagem) aprendido da
  distribuição dos dados.
- **LLM (Large Language Model):** modelo de linguagem treinado em texto massivo
  (arquitetura **Transformer**, mecanismo de **atenção**); gera/entende
  linguagem. Ex.: família GPT, Claude, Gemini.
- **RAG (Retrieval-Augmented Generation):** combina o LLM com busca em base
  externa para respostas mais atuais e fundamentadas.
- **Alucinação:** o modelo gera resposta plausível porém incorreta.
- **Prompt, fine-tuning, embeddings** são conceitos recorrentes.

### Ética, governança e privacidade em IA

- **Viés algorítmico** (dados enviesados → decisão injusta), transparência/
  explicabilidade, responsabilização.
- **Privacidade:** IA e LGPD (dados pessoais em treino e inferência).
- **Regulação:** discussões de marco legal da IA (Brasil PL 2338/2023; **AI
  Act** europeu, baseado em risco).

### IA aplicada — os cenários que a FGV monta

O edital não pede só teoria: pede **fundamentos e aplicações**. Ou seja, a
mesma pergunta técnica pode vir embrulhada num **cenário** (um órgão público,
um banco, uma prefeitura), e o que se cobra é reconhecer o conceito por trás
da situação. É o mesmo estilo de pegadinha por cenário de `governanca.md` e
`seguranca.md`, agora aplicado a IA.

| Cenário | Conceito que ele testa |
|---|---|
| **Triagem/priorização** (fila de posto de saúde, concessão de benefício, análise de currículos) | **classificação supervisionada** (o rótulo é conhecido: aprovado/negado, prioritário/não) + direito a **explicação e revisão humana** |
| **Detecção de fraude ou anomalia** (glosa de conta pública, benefício, transação suspeita) | em geral **não supervisionado**/semissupervisionado — o padrão fraudulento muda com o tempo (**concept drift**) e caso rotulado é raro |
| **Chatbot de atendimento ao cidadão com LLM** | a resposta pode **alucinar**; decisão que afeta direito exige **validação humana**, não a saída do modelo sozinha |
| **Score algorítmico** (crédito, seguro, benefício) | **viés algorítmico**: se o dado de treino reflete desigualdade histórica, o modelo a **reproduz e amplifica** |

**Base legal que ancora tudo isso — LGPD, art. 20:** o titular tem direito a
**solicitar revisão** de decisão tomada unicamente com base em tratamento
automatizado que afete seus interesses, incluindo as decisões destinadas a
definir seu perfil pessoal, profissional, de consumo e de crédito.

Pegadinhas de IA aplicada:
- O cenário descreve um sistema que **decide sozinho, sem revisão humana**, e a
  alternativa chama isso de boa prática — descarte.
- "O modelo é neutro porque **não usa** raça/gênero diretamente" — falso:
  variáveis **proxy** (CEP, escola, histórico de consumo) recriam o viés por
  via indireta. É o distrator da "neutralidade tecnológica".
- **Explicabilidade ≠ acurácia:** um modelo pode acertar muito e explicar mal
  (caixa-preta). A banca cobra exatamente essa tensão.
- Tratar chatbot/LLM como fonte **definitiva e infalível** — ignora o risco de
  alucinação, cuja mitigação (revisão humana, RAG com fonte oficial, escopo
  restrito) é o ponto da questão.

### Interseção IA × ESG — energia e governança

É o cruzamento mais provável do bloco em 2026, porque une os dois assuntos que
a banca mais repete: o viés socioambiental da Parte 1 e a IA da Parte 2.

- **Consumo de um data center:** a maior fatia vai para a **infraestrutura de
  TI** (processamento, ~metade do consumo); a segunda maior é o
  **resfriamento/ar-condicionado**. Refrigerar é, depois de processar, o maior
  custo energético de treinar e rodar modelos em escala.
- **PUE (Power Usage Effectiveness):** métrica-padrão de eficiência de data
  center = **energia total ÷ energia usada só pela TI**. Quanto mais próximo de
  **1,0**, mais eficiente. Regulações recentes (ex.: diretiva europeia) já
  fixam metas de PUE para data centers novos.
- **Matriz energética:** boa parte da eletricidade que alimenta data centers no
  mundo ainda vem de **fontes fósseis** — por isso a expansão acelerada de IA
  pressiona diretamente as metas de descarbonização.
- **Governança:** reguladores discutem exigir **divulgação pública** do impacto
  ambiental (energia, água, emissões) de produtos e serviços de IA —
  transparência como instrumento de política pública, não boa vontade.

Pegadinhas:
- O texto-base cita um número e a alternativa o **infla ou distorce** — releia
  o texto-base, nunca confie no número de memória.
- "A infraestrutura de IA usa **majoritariamente** energia limpa/renovável" —
  distrator otimista, salvo se o próprio texto-base afirmar isso.
- Armadilha inversa: "IA é **incompatível** com sustentabilidade" também é
  absoluto demais. O texto costuma apresentar o **dilema** (benefício
  tecnológico *e* custo ambiental), não um veredito fechado.

## O que já caiu (nossas questões)

Redes neurais como o que "aprende com dados e melhora"; supervisionado × não
supervisionado; viés-variância, regularização L1/L2, over/underfitting; concept
drift × data drift; MLOps; métrica MAE (nas provas de IA do TJ-RJ);
sustentabilidade e data centers (Dataprev); viés algorítmico em decisão
automatizada; direito à revisão humana (LGPD, art. 20). Rode
`../quiz.py atualidades`.

## Pegadinhas da FGV (resumo)

- Trocar supervisionado ↔ não supervisionado.
- Absolutos em itens de atualidades ("invariavelmente").
- Confundir IA/ML/Deep Learning (hierarquia).
- Chamar de neutro o modelo que não usa o atributo sensível — ignora o proxy.
- Confundir **explicabilidade** com **acurácia**.
- Ver `../dicas/atualidades.md`.

## Alta probabilidade / pesquisa extra

- **Métricas de ML:** classificação (acurácia, precisão, recall, F1, matriz
  de confusão); regressão (MAE, RMSE, R²).
- **Overfitting** (decora o treino, vai mal em dados novos) × **underfitting**
  (simples demais); combate: regularização, validação cruzada, mais dados.
- **Viés × variância:** trade-off central.
- Acompanhe **notícias de IA e regulação de 2026** — é conteúdo vivo.
