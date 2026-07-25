# atualidades — como a FGV cobra

## O que mais cai
- Na Dataprev 2024 foram 5 questões (Q31-35) e o viés é
  claríssimo: SOCIOAMBIENTAL. Sustentabilidade, meio ambiente,
  ESG, desigualdade, proteção de dados aparecem quase sempre.
- Temas concretos vistos nas provas FGV do edital:
  - Fóruns/cúpulas internacionais (G20 no Brasil, presidência
    rotativa, "Mundo Justo e Planeta Sustentável", combate às
    desigualdades).
  - Impacto ambiental da tecnologia (consumo de energia de
    data centers, pegada de carbono do digital).
  - Art. 225 da Constituição (direito ao meio ambiente
    equilibrado), racismo ambiental, justiça socioambiental.
  - Proteção de dados / LGPD aplicada a caso real (uso indevido
    de dados de consumidores, publicidade direcionada).
  - No MPU: A3P, Política Nacional sobre Mudança do Clima (Lei
    12.187/2009), Protocolo de Quioto, mudanças climáticas
    (enchentes RS, incêndios) — mesma pegada verde.
- IA entrou no edital em 2026 e responde por metade do bloco.
  O que se espera:
  - Fundamentos: hierarquia IA > ML > Deep Learning; tipos de
    aprendizado (supervisionado/não supervisionado/reforço);
    LLM, Transformer, RAG, alucinação, fine-tuning, embeddings.
  - Ajuste e métricas: viés x variância (alto viés =
    underfitting; alta variância = overfitting), acurácia
    enganosa em base desbalanceada, precisão x recall, F1 como
    média HARMÔNICA, ROC/AUC; MAE/RMSE/R² na regressão.
  - ESG por extenso: Environmental, Social and Governance —
    AMBIENTAL, SOCIAL e GOVERNANÇA.
  - Ética e governança: viés algorítmico, explicabilidade,
    responsabilização, LGPD no treino e na inferência, AI Act
    (baseado em risco) e o PL 2338/2023.
  - IA APLICADA em cenário: triagem/priorização, detecção de
    fraude, chatbot ao cidadão, score de crédito/benefício —
    e o art. 20 da LGPD (revisão de decisão automatizada).
  - O cruzamento IA x ESG: energia de data center, PUE,
    matriz fóssil, divulgação do impacto ambiental.

## Formato típico
- Quase nunca é "qual a capital de X". A FGV dá um TEXTO-base e
  manda JULGAR afirmativas:
  - "Está correto o que se afirma em: I / II / I e II / I,II,III".
  - Colunas de V/F: "As afirmativas são, respectivamente,
    V-F-V".
- Ou seja, você precisa avaliar CADA item isoladamente e
  depois casar com a combinação da resposta.
- ATENÇÃO — a parte de IA é o ÚNICO conteúdo do repositório sem
  calibração em prova passada da FGV: a banca nunca cobrou IA na
  Dataprev antes de 2026. Tudo que segue sobre o FORMATO dos
  itens de IA é PROJEÇÃO, não histórico observado. A incerteza é
  de formato, não de valor: por ser tema novo, o mais provável é
  item introdutório/conceitual (definição, tipos de aprendizado,
  o que é LLM, viés, alucinação) — pegadinha sofisticada a banca
  só monta depois de anos calibrando. Domine o fundamento em vez
  de decorar um desenho de questão hipotético.

## Como a banca arma a pegadinha
- Item com ABSOLUTO ou termo radical é quase sempre FALSO:
  "todos os avanços tecnológicos representam INVARIAVELMENTE
  benefícios para o meio ambiente" — o "invariavelmente" já
  entrega que é falso.
- Item que mantém "a lógica de consumo do atual modelo
  econômico" e ainda promete "justiça social para todos" —
  contradição plantada; desenvolvimento sustentável PEDE mudar
  o modelo. Falso.
- Item com dado numérico inflado/inventado ("data centers =
  metade do consumo dos ecossistemas digitais" quando o texto
  disse ~2% da eletricidade mundial). Confira o número CONTRA
  o texto-base.
- Item "bonzinho" mas falso: destino de dados "para pesquisas
  que democratizam remédios baratos" — soa nobre, mas não é o
  que a denúncia trata (uso indevido/comercialização). A banca
  usa a alternativa moralmente simpática como isca.
- O item VERDADEIRO costuma ser o mais moderado e alinhado ao
  senso socioambiental (impacto negativo + positivo da
  tecnologia; racismo ambiental atinge populações negras e
  pobres).
- Em IA, o par mais fácil de inverter é supervisionado (dados
  ROTULADOS) x não supervisionado (SEM rótulo). "Aprende com os
  dados e melhora ao longo do tempo" = redes neurais/ML, nunca
  lógica booleana ou programação linear.
- Inverte viés x variância: diz que ALTO VIÉS causa overfitting
  ou que ALTA VARIÂNCIA é modelo simples demais. Âncora: viés
  alto = o modelo é burro (underfit); variância alta = o modelo
  decorou (overfit). Regularização combate a VARIÂNCIA.
- Em métricas, chama F1 de "média aritmética" de precisão e
  recall (é HARMÔNICA), troca precisão por recall na definição,
  ou vende acurácia alta como bom modelo sem olhar o
  balanceamento da base (spam, fraude, doença rara).
- No ESG, troca o G de GOVERNANÇA por "Gestão"/"Global"/
  "Growth", ou o S de Social por "Sustentável" —
  sustentabilidade é o guarda-chuva, não a letra.
- Em cenário de IA aplicada, quatro traps se repetem:
  - o sistema DECIDE SOZINHO, sem revisão humana, e a
    alternativa vende isso como boa prática — descarte: a LGPD
    (art. 20) garante revisão de decisão automatizada;
  - "o modelo é neutro porque não usa raça/gênero diretamente"
    — falso: variáveis PROXY (CEP, escola, consumo) recriam o
    viés por via indireta. É a "neutralidade tecnológica";
  - trocar EXPLICABILIDADE por ACURÁCIA — o modelo pode acertar
    muito e explicar mal (caixa-preta); são coisas distintas;
  - chatbot/LLM tratado como fonte definitiva e infalível —
    ignora a alucinação, que é justamente o que se pede mitigar.
- No cruzamento IA x ESG, dois traps de energia:
  - "a infraestrutura de IA usa MAJORITARIAMENTE energia limpa"
    — distrator otimista, salvo se o texto-base disser isso;
  - "IA é INCOMPATÍVEL com sustentabilidade" — armadilha
    inversa, absoluta do mesmo jeito. O texto apresenta o
    DILEMA (ganho tecnológico e custo ambiental), não veredito.

## Como se sair melhor
- Trate como prova de interpretação: a maioria das respostas
  está no PRÓPRIO texto-base. Releia antes de julgar cada item.
- Marque como falso todo item com "sempre, nunca, apenas,
  invariavelmente, exclusivamente, todos" — o mundo real de
  meio ambiente/política raramente é absoluto.
- Desconfie de item que contradiz o consenso ESG (sustentável
  = mudar consumo, incluir os vulneráveis, reduzir emissões).
- Julgue item por item e só então escolha a combinação; não
  chute a letra pela "cara". Se dois itens você tem certeza,
  as combinações de resposta já eliminam metade das opções.
- Acompanhe: cúpulas do Brasil (G20, COP/clima), LGPD/ANPD em
  casos noticiados, energia e IA/data centers, desigualdade.
- Em IA, fixe a hierarquia numa frase: IA contém ML, que contém
  Deep Learning. Metade dos itens conceituais mora aí.
- Diante de um cenário aplicado, pergunte-se primeiro: o rótulo
  já existe? Se sim (aprovado/negado, prioritário/não), é
  classificação SUPERVISIONADA. Se não (achar o que destoa),
  puxa para NÃO supervisionado — é o desenho de detecção de
  fraude e anomalia.
- Sempre que o cenário afetar direito do cidadão (benefício,
  crédito, emprego), procure a alternativa que preserva a
  REVISÃO HUMANA. A que automatiza sem ela é a errada.
- Em energia de data center, a ordem é: infraestrutura de TI
  (processamento) primeiro, RESFRIAMENTO em segundo. PUE =
  energia total dividida pela energia só da TI — quanto mais
  perto de 1,0, mais eficiente.
- Número em item de IA/ESG: confira SEMPRE contra o texto-base.
  A banca infla o dado do próprio texto, e ele nunca precisa
  ser lembrado de memória.
