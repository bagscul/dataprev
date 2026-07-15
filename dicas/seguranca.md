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
- OWASP Top 10:2021 — identificar item que É/NÃO é categoria.
- ISO/IEC 27001:2022 — categoria de cada controle.
- OpenID Connect (OIDC): claims do ID Token (iat, exp, sub,
  jti). Autenticação x autorização.
- X.800 — mecanismos de segurança OSI (específicos x
  disseminados).
- Cripto/integridade: HMAC em webhook (autenticidade +
  integridade da mensagem). Simétrica x assimétrica,
  hash x cifra.

## Como a banca arma a pegadinha
- OWASP 2021: mistura itens que NÃO são da lista web —
  "proteção da cadeia de suprimentos", "ambiente de
  engenharia", "treinamento operacional" são de CI/CD e
  SSDF, não OWASP. O item real do exemplo era SSRF
  (A10:2021).
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

## Como se sair melhor
- CIA: Confidencialidade = quem VÊ; Integridade = dado
  ÍNTEGRO/não alterado; Disponibilidade = ACESSÍVEL. Mapeie
  o verbo do cenário (visualizar/alterar/indisponível).
- Controle de acesso, decore a frase-chave: MAC = rótulos e
  classificações impostos pelo sistema; DAC = o proprietário
  concede; RBAC = permissões por função/cargo.
- OWASP Top 10:2021, âncoras seguras: A01 Broken Access
  Control (o nº1), A03 Injection, A10 SSRF. Se a opção fala
  em "cadeia de suprimentos/pipeline/treinamento", é
  distrator de outro framework.
- ISO 27001:2022 tem 4 categorias de controle:
  organizacional, PESSOAL, FÍSICA, TECNOLÓGICA. Trabalho
  remoto = pessoal; mídia de armazenamento = física;
  criptografia = tecnológica; políticas = organizacional.
- OIDC: iat = issued at (emissão); exp = expiração; sub =
  subject (usuário). HMAC = chave simétrica → autenticidade
  e integridade (não confidencialidade).
- Gatilho: "sempre isento", "SSL mais seguro", claim trocado
  — releia com calma.
