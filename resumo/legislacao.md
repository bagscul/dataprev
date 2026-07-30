# Legislação (Segurança da Informação e Proteção de Dados) — resumo

> **Edital (Módulo I, 5 questões):** Lei 12.527/2011 (LAI) caps I–V + Decretos
> 7.724 e 7.845; Lei 12.737/2012 (Delitos Informáticos) art. 2º; Lei
> 12.965/2014 (Marco Civil) cap. II Seção I e cap. III Seções I e II; Lei
> 13.709/2018 (LGPD) caps I, II, III, IV, VII, VIII, IX.
> **Na amostra de provas** (nosso recorte de edital): classificação na LAI,
> invasão de dispositivo (art. 154-A), sanções do Marco Civil, sanções da LGPD
> e ANPD × CNPD (Dataprev 2024); princípio da adequação, explicabilidade da
> decisão automatizada (art. 20) e IA generativa × LGPD (TJ-RJ). A banca cita o
> número e a data da lei no enunciado — o que ela cobra é competência, prazo e
> papel.

## ⚠️ Atualização crítica: Marco Civil, art. 19 (pós-STF, jun/2025)

Em **26/06/2025** o STF (Temas 987 e 533) declarou o **art. 19
parcialmente/progressivamente inconstitucional**. Mudou a regra de
responsabilidade dos provedores por conteúdo de terceiros:

- **Antes:** o provedor só respondia se descumprisse **ordem judicial
  específica** de remoção (exceção: conteúdo íntimo não consentido, art. 21,
  bastava notificação).
- **Agora:** a regra geral passou a ser **notice-and-takedown** — a
  **notificação extrajudicial** já pode responsabilizar o provedor pela maioria
  dos conteúdos ilícitos. **Ordem judicial só permanece obrigatória para
  crimes contra a honra** (calúnia, injúria, difamação).

Para uma prova de 2026, saiba as duas versões e que a regra **mudou**. (Fonte:
STF, notícias 26/06/2025.)

## LGPD (Lei 13.709/2018)

- **Dado pessoal** (art. 5º, I) = informação relacionada a pessoa natural
  **identificada ou identificável** (nome, endereço, telefone, e-mail, placa,
  CPF). **Dado pessoal sensível** (art. 5º, II) é um rol **fechado e menor**:
  origem racial ou étnica, convicção religiosa, opinião política, filiação a
  sindicato ou a organização de caráter religioso/filosófico/político, dado
  referente à **saúde** ou à **vida sexual**, dado **genético** ou
  **biométrico** vinculado a pessoa natural. Sensível tem regime **mais
  restrito** (art. 11), não proibição.
- **Controlador** decide sobre o tratamento (finalidade e meios);
  **operador** trata em nome do controlador. **Encarregado (DPO)** é o canal
  com titulares e ANPD. — a FGV troca controlador × operador.
- **Bases legais (art. 7º):** consentimento **não** é a única; há **10** bases
  (cumprimento de obrigação legal, execução de contrato, legítimo interesse,
  proteção da vida, tutela da saúde, políticas públicas, etc.).
- **Direitos do titular (art. 18):** confirmação, acesso, correção,
  anonimização/bloqueio/eliminação, portabilidade, informação sobre
  compartilhamento, revogação do consentimento.
- **ANPD** **fiscaliza, regulamenta e sanciona**; o **CNPD** (Conselho) é
  **consultivo** — propõe diretrizes, sugere ações à ANPD e dissemina. Não
  confunda os papéis, nem os **dois colegiados**: o **Conselho Diretor** é a
  direção da própria ANPD (**5 diretores**, mandato de 4 anos); o **CNPD** tem
  **23 representantes** e **integra a estrutura da ANPD** (art. 55-C, II) — não
  o contrário.
- **Atualização de 2026 — a ANPD virou agência.** A **Lei nº 15.352, de
  25/02/2026** (conversão da MP 1.317/2025) deu nova redação ao art. 55-A: a
  sigla continua **ANPD**, mas o nome passou a **Agência** Nacional de Proteção
  de Dados — **autarquia de natureza especial vinculada ao Ministério da
  Justiça e Segurança Pública**, com autonomia funcional, técnica, decisória,
  administrativa e financeira, **nos termos da Lei 13.848/2019** (lei das
  agências reguladoras). A trajetória é de onde saem os distratores: *órgão*
  ligado à **Presidência da República** (2018–2019, natureza declaradamente
  transitória) → *autarquia de natureza especial* (**Lei 14.460/2022**) →
  *agência* vinculada ao **Ministério da Justiça** (2026).
- **Por que a ANPD virou agência — o ECA Digital (fora do rol do edital, mas
  colado na ANPD).** A **Lei nº 15.211/2025** (Estatuto Digital da Criança e do
  Adolescente), em vigor desde **17/03/2026**, entregou à ANPD a competência de
  regulamentar e fiscalizar as obrigações das plataformas — e foi essa
  atribuição nova que motivou a transformação em agência. O edital não lista
  essa lei, mas ela é o contexto de qualquer item sobre o desenho atual da
  ANPD. O mínimo a saber: **verificação de idade confiável** (autodeclaração
  não basta), **conta de menor de 16 anos vinculada a responsável** com
  supervisão parental, **vedação de publicidade comportamental** dirigida a
  criança e adolescente, e sanções de advertência, **multa de até R$ 50 milhões
  por infração** e suspensão ou proibição da atividade.
- **Sanções (art. 52):** são **nove** em vigor (incisos I–VI e X–XII; VII–IX
  vetados) — advertência; **multa simples de até 2% do faturamento**, limitada
  a **R$ 50 milhões por infração**; multa diária; publicização; bloqueio;
  eliminação; suspensão parcial do banco de dados; suspensão da atividade; e
  proibição parcial ou total. Exige processo administrativo, com ampla defesa.
  - **Gradação (§6º, I):** as três últimas (X, XI, XII) só depois de já
    imposta, no mesmo caso, ao menos uma das sanções dos **incisos II a VI**
    (multa simples, multa diária, publicização, bloqueio ou eliminação).
    **Advertência não conta** — é o distrator pronto ("já houvera advertência,
    logo pôde suspender": não pôde).
- **Comunicação de incidente (art. 48):** o **controlador** comunica **à ANPD
  e ao titular** o incidente que possa acarretar **risco ou dano relevante**.
  A **lei** diz "prazo razoável"; a **Resolução CD/ANPD nº 15/2024** fixou
  **3 dias úteis** do conhecimento, para os dois destinatários, e **5 anos**
  de guarda do registro de todo incidente (inclusive dos não comunicados).
  Não são as 72h do GDPR, e o critério não é "ser dado sensível".
- **LGPD aplicada a IA:** explicabilidade em decisão automatizada (art. 20),
  anonimização, *scraping* — os três já cobrados no TJ-RJ.

### Princípios (art. 6º) — o trio que a FGV confunde

São **dez**: finalidade, adequação, necessidade, livre acesso, qualidade dos
dados, transparência, segurança, prevenção, não discriminação, e
responsabilização e prestação de contas. Três são o alvo preferido da banca,
porque parecem sinônimos e não são:

| Princípio | O que exige |
|---|---|
| **Finalidade** | propósitos **legítimos, específicos e explícitos**, **informados ao titular**, sem tratamento posterior incompatível |
| **Adequação** | **compatibilidade** do tratamento com as finalidades informadas, **conforme o contexto** |
| **Necessidade** | tratamento **limitado ao mínimo** indispensável para a finalidade (pertinente, proporcional, não excessivo) |

Âncora pela palavra-chave: **finalidade** = *para quê* (e avisou);
**adequação** = *combina com* o que foi avisado; **necessidade** = *o mínimo*.

Pegadinha: no TJ-RJ a FGV descreveu literalmente "o tratamento seja
**compatível com os fins informados ao titular, de acordo com o contexto**" e
ofereceu finalidade, prevenção, **adequação**, necessidade e transparência —
gabarito **adequação**. Quem decorou só "finalidade" errou, porque a palavra
"fins" está no enunciado de propósito.

### Decisão automatizada (art. 20)

O titular tem direito a **solicitar revisão** de decisões tomadas
**unicamente** com base em tratamento automatizado que afetem seus
interesses, incluindo as destinadas a definir perfil pessoal, profissional, de
consumo e de crédito. O **controlador deve fornecer informações claras e
adequadas sobre os critérios e procedimentos** usados na decisão, observados
os segredos comercial e industrial — é a base legal da **explicabilidade** em
IA, e ancora todos os cenários de IA aplicada do bloco de
[atualidades](atualidades.md).

**Cuidado com a redação antiga:** o texto original de 2018 previa revisão
**"por pessoa natural"**. A Lei 13.853/2019 retirou essa expressão, e o
parágrafo que a reintroduziria (§3º) foi **vetado** — veto mantido pelo
Congresso. Hoje a lei **não exige revisor humano**; alternativa que exige
"revisão por pessoa natural" está errada.

## Marco Civil (Lei 12.965/2014) — guarda de registros

- **Registros de conexão:** guarda obrigatória por **1 ano** (provedor de
  conexão).
- **Registros de acesso a aplicações:** **6 meses** (provedor de aplicação).
- Princípios: neutralidade de rede, privacidade, liberdade de expressão.

**Neutralidade de rede (art. 9º).** O responsável pela transmissão, comutação
ou roteamento deve **tratar de forma isonômica quaisquer pacotes de dados, sem
distinção por conteúdo, origem e destino, serviço, terminal ou aplicação**. O
provedor não pode degradar, priorizar nem bloquear tráfego por causa *do que*
ele carrega ou *de quem* vem. Discriminação só nas **exceções do §1º**:
requisitos técnicos indispensáveis e priorização de **serviços de emergência**,
mediante regulamentação.

Pegadinha: os distratores descrevem o que a lei proíbe com cara de eficiência
operacional — "priorizar quem paga mais", "bloquear aplicações de
concorrentes", "monitorar o conteúdo dos pacotes para fins comerciais",
"reduzir a velocidade de vídeo no pico para aliviar a rede". O último é o mais
perigoso: soa técnico, mas é discriminação **por aplicação**, fora do §1º.

## LAI (Lei 12.527/2011) — prazos de sigilo

| Classificação | Prazo máximo de restrição |
|---|---|
| **Reservada** | 5 anos |
| **Secreta** | 15 anos |
| **Ultrassecreta** | 25 anos (prorrogável **uma vez**) |

- Regra geral: **publicidade é a regra; sigilo é exceção.**
- Prazos contam da **data de produção** da informação.
- Informação sobre **violação de direitos humanos** por agente público **não**
  pode ser objeto de restrição de acesso.
- **Transparência ativa** (o órgão publica de ofício, ex: portal) ×
  **passiva** (o cidadão pede via e-SIC).

**Desclassificação e reavaliação.** A classificação **não é definitiva nem
discricionária**:
- **Findo o prazo** (ou consumado o evento do termo final), a informação
  torna-se **automaticamente** de acesso público — **não** é preciso
  procedimento próprio nem decisão específica para liberar.
- A lei permite **desclassificar** **e também reduzir o prazo**. A reavaliação
  cabe à **autoridade classificadora ou a autoridade hierarquicamente
  superior**, **de ofício ou mediante provocação**.
- Classificar é ato vinculado a balizas legais (grau, prazo máximo,
  competência por autoridade), não escolha livre do agente.

Pegadinha: na Dataprev 2024 os distratores da LAI foram exatamente esses —
trocar os nomes dos graus ("ultrassigilosas, sigilosas ou reservadas"), dizer
que classificar é **discricionário** "porquanto a lei não prevê balizas",
exigir "procedimento próprio e decisão específica" para o acesso findo o prazo
(é automático) e afirmar que a lei permite desclassificar **mas não** reduzir
prazo (permite as duas).

**Decretos que o edital cita (regulamentam a LAI no Executivo federal):**
- **Decreto 7.724/2012:** regulamenta a LAI — procedimentos de acesso, e-SIC,
  prazos de resposta ao pedido (**20 dias**, prorrogáveis por **10**),
  recursos, transparência ativa, competências de classificação.
- **Decreto 7.845/2012:** procedimentos de **credenciamento de segurança** e
  tratamento de **informação classificada** (custódia, acesso, controle).

## Delitos Informáticos (Lei 12.737/2012, art. 154-A do CP)

- Crime de **invasão de dispositivo informático**. **Independe** de o
  dispositivo estar conectado à rede (a conexão não é elementar do tipo).
- Aumento de pena conforme o sujeito passivo (autoridades) e o prejuízo.
  (A pena exata foi alterada pela Lei 14.155/2021 — foque no conceito.)

## O que já caiu

**Em prova real da FGV:** **ANPD × CNPD** — o gabarito foi justamente "o CNPD
tem atribuição de *sugerir ações* a serem realizadas pela ANPD";
**classificação na LAI** (nomes dos graus, decisão *vinculada* a balizas,
acesso automático findo o prazo, desclassificação *e* redução de prazo);
**sanções administrativas da LGPD** (parâmetros de dosimetria, destino da
arrecadação das multas); **sanções do Marco Civil** (advertência com prazo
para adoção de medidas); **invasão de dispositivo** do art. 154-A — não exige
conexão à rede, e o aumento de pena varia com o sujeito passivo — **Dataprev
2024**. **Princípio da adequação** (o enunciado descreve "compatível com os
fins informados, de acordo com o contexto"); **explicabilidade da decisão
automatizada**, com a redação do art. 20; **IA generativa × LGPD**, incluindo
raspagem da web — **TJ-RJ**.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): controlador × operador; as dez bases legais; dado pessoal sensível;
os prazos numéricos da LAI (5/15/25); transparência ativa × passiva; guarda de
registros no Marco Civil (1 ano / 6 meses); neutralidade de rede; e todo o
regime do art. 19 pós-STF de 26/06/2025 (notice-and-takedown, exceção dos
crimes contra a honra, dever proativo, repercussão geral).

Rode `../quiz.py legislacao`.

## Pegadinhas da FGV (resumo)

- Trocar prazos (LAI, Marco Civil) e competências (ANPD × CNPD).
- Trocar os princípios entre si — "fins informados" puxa para finalidade, mas
  quem fala em *compatibilidade* e *contexto* é a **adequação**.
- Dizer que consentimento é a única base legal da LGPD.
- Cobrar o art. 19 na **redação antiga** — hoje mudou (veja o alerta acima).
- Inverter controlador × operador.
- Ver `../dicas/legislacao.md`.

## Alta probabilidade / pesquisa extra

- **GDPR** (regulamento europeu) aparece como paralelo à LGPD.
- **Decretos 7.724 (LAI) e 7.845 (credenciamento de segurança).**
- Atenção a **novas decisões do STF/ANPD em 2026** — legislação é o bloco que
  mais muda; confira antes da prova.
