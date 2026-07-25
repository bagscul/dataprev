# Legislação (Segurança da Informação e Proteção de Dados) — resumo

> **Edital (Módulo I, 5 questões):** Lei 12.527/2011 (LAI) caps I–V + Decretos
> 7.724 e 7.845; Lei 12.737/2012 (Delitos Informáticos) art. 2º; Lei
> 12.965/2014 (Marco Civil) cap. II Seção I e cap. III Seções I e II; Lei
> 13.709/2018 (LGPD) caps I, II, III, IV, VII, VIII, IX.
> **A FGV adora prazo, competência e a distinção controlador × operador.**

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
- **ANPD** (autarquia) **fiscaliza e sanciona**; o **CNPD** (Conselho) é
  **consultivo** (propõe diretrizes). Não confunda os papéis.
- **Sanções:** advertência; **multa simples de até 2% do faturamento**,
  limitada a **R$ 50 milhões por infração**; publicização; bloqueio/eliminação
  dos dados. Exige processo administrativo.

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

## O que já caiu (nossas questões)

Controlador × operador; bases legais da LGPD; ANPD × CNPD; prazos da LAI
(reservada/secreta/ultrassecreta); guarda de registros no Marco Civil (1 ano /
6 meses); art. 19 e responsabilidade do provedor; invasão de dispositivo
independe de rede. Rode `../quiz.py legislacao`.

## Pegadinhas da FGV (resumo)

- Trocar prazos (LAI, Marco Civil) e competências (ANPD × CNPD).
- Dizer que consentimento é a única base legal da LGPD.
- Cobrar o art. 19 na **redação antiga** — hoje mudou (veja o alerta acima).
- Inverter controlador × operador.
- Ver `../dicas/legislacao.md`.

## Alta probabilidade / pesquisa extra

- **GDPR** (regulamento europeu) aparece como paralelo à LGPD.
- **Decretos 7.724 (LAI) e 7.845 (credenciamento de segurança).**
- Atenção a **novas decisões do STF/ANPD em 2026** — legislação é o bloco que
  mais muda; confira antes da prova.
