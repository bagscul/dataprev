# seguranca — como a FGV cobra

## O que mais cai
- Tríade CIA: cenário → associar ao princípio afetado.
  Confidencialidade (acesso indevido/visualização),
  Integridade (alteração indevida de dados), Disponibilidade
  (indisponível/fora do ar). Aparece como associação e como
  "regra geral x específica".
- Controle de acesso: DAC (discricionário), MAC (mandatório
  = rótulos de segurança comparados a autorizações), RBAC
  (por papéis). Distratores: privilégio mínimo, entrada
  confiável.
- LGPD (13.709/2018): aplicabilidade (quem está isento/não),
  anonimização, princípios. Fronteira com Legislação.
- OWASP Top 10 — identificar item que É/NÃO é categoria.
  ATENÇÃO ao ano: a edição VIGENTE é a Top 10 de 2025 (final
  em jan/2026); a 2021 é a que a Dataprev 2024 cobrou e a que
  ancora nossas questões. Duas numerações válidas convivem —
  veja qual o enunciado cita antes de contar posição.
- ISO/IEC 27001:2022 — categoria de cada controle.
- OpenID Connect (OIDC): claims do ID Token (iat, exp, sub,
  jti). Autenticação x autorização.
- X.800 — mecanismos de segurança OSI (específicos x
  disseminados).
- Cripto/integridade: HMAC em webhook (autenticidade +
  integridade da mensagem). Simétrica x assimétrica,
  hash x cifra.
- Continuidade de negócio: RTO (tempo fora do ar) x RPO
  (dado que se aceita perder), com MTBF/MTTR/SLA como
  siglas vizinhas oferecidas junto.

## Como a banca arma a pegadinha
- OWASP 2021: mistura itens que NÃO são da lista web —
  "proteção da cadeia de suprimentos", "ambiente de
  engenharia", "treinamento operacional" são de CI/CD e
  SSDF, não OWASP. O item real do exemplo era SSRF
  (A10:2021). Cuidado: em 2025 a cadeia de suprimentos DE
  SOFTWARE virou categoria própria (A03) — o que não faz
  desse distrator um item de 2021.
- Mistura de ano: a 2025 tem duas categorias novas (A03
  Software Supply Chain Failures, A10 Mishandling of
  Exceptional Conditions), absorveu o SSRF no A01 e
  RENOMEOU três — A07 perdeu o "Identification and", A08
  trocou "and" por "or", A09 trocou MONITORING por
  ALERTING. Oferecer o nome de 2021 num item que diz 2025
  (ou o contrário) é pegadinha pronta.
- MAC x DAC: descreve rótulos de segurança comparados a
  autorizações (isso é MAC/mandatório) e oferece
  discricionário como pegadinha. DAC = dono decide; MAC =
  sistema/rótulo decide; RBAC = papel decide.
- CIA: troca a ordem na associação; "restringir quem vê" é
  confidencialidade, não integridade; "ficar no ar" é
  disponibilidade.
- OIDC: troca os claims — iat (emitido em), exp (expira),
  sub (identificador do usuário), jti (id do token). Pede um
  e oferece os outros.
- LGPD: distratores com isenção condicionada ("desde que...")
  ou observância parcial; costuma ser total observância.
- SSL "mais seguro que TLS" (invertido).
- RTO x RPO: o cenário dá os dois números na ordem "fica
  fora X, perde Y" e a alternativa INVERTE as siglas. Ou
  oferece MTBF/MTTR (médias observadas) e SLA (acordo
  contratual) como se fossem objetivos de plano.

## Como se sair melhor
- CIA: Confidencialidade = quem VÊ; Integridade = dado
  ÍNTEGRO/não alterado; Disponibilidade = ACESSÍVEL. Mapeie
  o verbo do cenário (visualizar/alterar/indisponível).
- Controle de acesso, decore a frase-chave: MAC = rótulos e
  classificações impostos pelo sistema; DAC = o proprietário
  concede; RBAC = permissões por função/cargo.
- OWASP Top 10:2021, âncoras seguras: A01 Broken Access
  Control (o nº1), A03 Injection, A10 SSRF. Se a opção fala
  em "pipeline/treinamento", é distrator de outro framework.
- OWASP Top 10 de 2025, âncoras seguras: A01 Broken Access
  Control segue no topo (e engoliu o SSRF), A02 Security
  Misconfiguration (subiu de 5º), A03 Software Supply Chain
  Failures e A10 Mishandling of Exceptional Conditions (as
  duas novas). O topo não muda de dono; o que muda é o resto.
- RTO x RPO, ancore numa letra: o T de RTO é TEMPO (quanto
  o serviço fica fora); o P de RPO é PONTO no tempo, ou
  seja, DADO. É o RPO que dita de quanto em quanto tempo o
  backup roda.
- ISO 27001:2022 tem 4 categorias de controle:
  organizacional, PESSOAL, FÍSICA, TECNOLÓGICA. Trabalho
  remoto = pessoal; mídia de armazenamento = física;
  criptografia = tecnológica; políticas = organizacional.
- OIDC: iat = issued at (emissão); exp = expiração; sub =
  subject (usuário). HMAC = chave simétrica → autenticidade
  e integridade (não confidencialidade).
- Gatilho: "sempre isento", "SSL mais seguro", claim trocado
  — releia com calma.
