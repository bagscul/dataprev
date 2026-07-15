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

## O que já caiu (nossas questões)

Redes neurais como o que "aprende com dados e melhora"; supervisionado × não
supervisionado; viés-variância, regularização L1/L2, over/underfitting; concept
drift × data drift; MLOps; métrica MAE (nas provas de IA do TJ-RJ);
sustentabilidade e data centers (Dataprev). Rode `../quiz.py atualidades`.

## Pegadinhas da FGV (resumo)

- Trocar supervisionado ↔ não supervisionado.
- Absolutos em itens de atualidades ("invariavelmente").
- Confundir IA/ML/Deep Learning (hierarquia).
- Ver `../dicas/atualidades.md`.

## Alta probabilidade / pesquisa extra

- **Métricas de ML:** classificação (acurácia, precisão, recall, F1, matriz
  de confusão); regressão (MAE, RMSE, R²).
- **Overfitting** (decora o treino, vai mal em dados novos) × **underfitting**
  (simples demais); combate: regularização, validação cruzada, mais dados.
- **Viés × variância:** trade-off central.
- Acompanhe **notícias de IA e regulação de 2026** — é conteúdo vivo.
