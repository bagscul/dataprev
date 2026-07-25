# Segurança da Informação — resumo (Perfil 3)

> **Edital (Perfil 3):** políticas e procedimentos de segurança; **ISO/IEC
> 27001:2022 e 27002:2022**; confidencialidade, integridade e disponibilidade;
> mecanismos de segurança (controle de acesso, **OAuth2, SSO**); gestão de
> riscos (ameaça, vulnerabilidade, impacto); **SDL** e **OWASP Top 10**;
> análise estática e dinâmica de código (**SAST e DAST**). Também: HTTPS,
> SSL/TLS.
> **Peso esperado: ALTO.**

## 1. Tríade CIA (a base de tudo)

- **Confidencialidade:** só quem tem direito acessa (cifra, controle de acesso).
- **Integridade:** dado não é alterado indevidamente (hash, assinatura).
- **Disponibilidade:** acessível quando necessário (redundância, backup).
- Complementos: autenticidade, não repúdio, legalidade.

## 2. Criptografia

| | Simétrica | Assimétrica (chave pública) |
|---|---|---|
| Chaves | uma chave secreta compartilhada | par: pública + privada |
| Velocidade | rápida | lenta |
| Uso | cifrar volume de dados | troca de chave, assinatura |
| Exemplos | AES, DES/3DES | RSA, ECC |

- **Hash** (MD5, SHA-256): resumo de tamanho fixo, **unidirecional**; garante
  **integridade**, não confidencialidade (não "descriptografa"). MD5 e SHA-1
  são considerados fracos.
- **Assinatura digital:** hash do documento cifrado com a **chave privada**
  do emissor → garante autenticidade, integridade e não repúdio.
- **Certificado digital / ICP-Brasil:** vincula identidade a uma chave
  pública, emitido por uma AC (Autoridade Certificadora).
- **TDE (Transparent Data Encryption):** cifra os dados **em repouso** (arquivos
  do banco/disco) de forma transparente à aplicação — protege contra roubo do
  arquivo físico, não contra acesso lógico autorizado.
- **Esteganografia** ≠ criptografia: **oculta a existência** da mensagem
  (esconde dado dentro de imagem/áudio); a criptografia oculta o **conteúdo**,
  não o fato de haver mensagem.
- **HMAC** (*Hash-based Message Authentication Code*): hash **combinado a uma
  chave secreta compartilhada**. Como só quem tem a chave produz o código, ele
  entrega **integridade** *e* **autenticidade**. Não entrega
  **confidencialidade** (a mensagem viaja legível) nem **não repúdio** (a
  chave é *simétrica* — as duas pontas geram o mesmo código).

**HMAC no cenário do *webhook*.** Um sistema externo envia uma chamada HTTP de
notificação e é preciso garantir que veio mesmo do parceiro e não foi
adulterada. Resposta: assinar o corpo com **HMAC** usando um segredo combinado,
e o receptor recalcular e comparar. Hash puro não serve (qualquer um
recalcula); cifrar o corpo resolveria confidencialidade, que não é o problema.

Pegadinha: hash não é cifra reversível; confidencialidade = cifra (não hash);
assina-se com a **privada**, verifica-se com a **pública**; esteganografia
esconde a existência, cifra esconde o conteúdo. No HMAC, as duas armadilhas
são vendê-lo como **confidencialidade** e como **não repúdio** — para o não
repúdio é preciso **assinatura digital** com chave *privada*, que só o emissor
possui. O corte: chave *simétrica* → autenticidade + integridade; chave
*privada* → acrescenta o não repúdio.

## 3. HTTPS, SSL e TLS

- **HTTPS = HTTP sobre TLS/SSL.** Confidencialidade + integridade +
  autenticação do servidor.
- **TLS substitui o SSL:** corrige vulnerabilidades das versões antigas do
  SSL. SSL está obsoleto; TLS 1.2/1.3 é o atual. Não é "SSL mais seguro que
  TLS" nem "intercambiáveis".

## 4. Controle de acesso

| Política | Base da decisão |
|---|---|
| **DAC** (discricionário) | dono do recurso concede acesso |
| **MAC** (mandatório) | **rótulos de segurança** comparados com autorizações; regra central, o usuário não decide |
| **RBAC** (por papéis) | acesso via papéis/funções |
| **ABAC** (por atributos) | atributos de usuário/recurso/contexto |

- **Menor privilégio:** só o acesso necessário.
- **OAuth2:** protocolo de **autorização** delegada (tokens); ≠ autenticação.
  **OpenID Connect** (sobre OAuth2) faz autenticação, e entrega o **ID Token**
  (um JWT). **Decore os quatro *claims*** — a banca pede um e oferece os
  outros:

  | *Claim* | Significado |
  |---|---|
  | **`iat`** | *issued at* — quando o token foi **emitido** |
  | **`exp`** | *expiration* — quando **expira** |
  | **`sub`** | *subject* — o **identificador do usuário** |
  | **`jti`** | *JWT ID* — identificador **único do token** |

  Os dois que mais se confundem: `sub` diz **quem é o usuário**, `jti` diz
  **qual é o token**. E `iat` (emissão) × `exp` (expiração).
- **SSO (Single Sign-On):** um login para vários sistemas.

Pegadinha: MAC = **rótulos** e regra central; DAC = dono decide. OAuth2 é
autorização, não autenticação.

## 5. OWASP Top 10 — **2025 (vigente) E 2021** (leia os dois)

O edital aponta para o projeto OWASP (sem fixar ano), e hoje existem **duas
numerações válidas**. A **edição vigente é a 2025** — oitava da série, com
*release candidate* em nov/2025 e versão final publicada em **jan/2026**. A
**2021** é a que a Dataprev 2024 cobrou e a que ancora as questões deste
material. Sabendo as duas, você cobre qualquer recorte — e, ao ler o enunciado,
**confira qual ano ele cita** antes de contar posição.

| # | **Top 10:2025** (vigente) | **Top 10:2021** (Dataprev 2024) |
|---|---|---|
| 1 | **Broken Access Control** (absorveu o SSRF) | **Broken Access Control** |
| 2 | **Security Misconfiguration** (subiu de 5º) | **Cryptographic Failures** (era "Sensitive Data Exposure") |
| 3 | **Software Supply Chain Failures** (novo) | **Injection** (SQLi; **XSS absorvido aqui** — CWE-79) |
| 4 | Cryptographic Failures (caiu de 2º) | Insecure Design (novo em 2021) |
| 5 | Injection (caiu de 3º) | Security Misconfiguration |
| 6 | Insecure Design | Vulnerable and Outdated Components |
| 7 | Authentication Failures | Identification and Authentication Failures |
| 8 | Software **or** Data Integrity Failures | Software **and** Data Integrity Failures |
| 9 | Security Logging and **Alerting** Failures | Security Logging and **Monitoring** Failures |
| 10 | **Mishandling of Exceptional Conditions** (novo; erro/fail-open) | **Server-Side Request Forgery (SSRF)** |

**O que mudou de 2021 para 2025:** duas categorias **novas** (A03 Software
Supply Chain Failures, que expande "componentes vulneráveis", e A10 Mishandling
of Exceptional Conditions) e uma **consolidação** (o SSRF, A10 em 2021, foi
absorvido pelo Broken Access Control). Três categorias só **mudaram de nome**:
A07 perdeu o "Identification and"; A08 trocou "and" por "or"; A09 trocou
**Monitoring** por **Alerting**.

Pegadinha 2024: descrever "injeção" citando SQL → categoria **Injection**;
lembrar que em 2021 **XSS entrou em Injection** (era categoria própria até
2017). As renomeações são pegadinha pronta: "Security Logging and
**Monitoring**" num item que diz 2025, ou "Authentication Failures" num item
que diz 2021. Se a prova disser "2025", troque o ranking conforme a tabela.

## 6. Desenvolvimento seguro

- **SDL (Security Development Lifecycle):** segurança em todo o ciclo.
- **SAST (estática):** analisa o **código-fonte** sem executar (caixa-branca).
- **DAST (dinâmica):** testa a **aplicação em execução** (caixa-preta).
- **IAST:** combina os dois em runtime instrumentado.
- **DevSecOps:** segurança automatizada no pipeline CI/CD.

Pegadinha: **SAST × DAST** (código parado × app rodando).

## 5.1 X.800 — a arquitetura de segurança OSI

Recomendação da ITU-T que dá o **vocabulário** de segurança usado por normas e
por bancas. Divide o assunto em **ataques**, **serviços** e **mecanismos** — e
o que a FGV cobra é a divisão dos mecanismos.

**Os cinco serviços:** autenticação, controle de acesso, confidencialidade,
integridade e **não repúdio** (disponibilidade entra como categoria adicional).

| Mecanismos | Quais são |
|---|---|
| **Específicos** (ligados a uma camada e a um serviço) | cifração (*encipherment*), assinatura digital, controle de acesso, integridade de dados, troca de autenticação, **preenchimento de tráfego** (*traffic padding*), controle de roteamento, **notarização** |
| **Disseminados** (*pervasive*, não específicos de camada) | funcionalidade confiável, **rótulos de segurança**, detecção de eventos, **trilha de auditoria** de segurança, recuperação de segurança |

Pegadinha: a troca é sempre entre as duas colunas — oferecer **trilha de
auditoria** ou **rótulo de segurança** como "específico" (são
**disseminados**), ou **cifração**/**notarização** como "disseminado" (são
**específicos**). O critério: específico implementa *um serviço* numa
*camada*; disseminado é de gestão e vale para o sistema inteiro.
**Preenchimento de tráfego** e **controle de roteamento** surpreendem — são
específicos, e servem à confidencialidade do *fluxo*, não do conteúdo.

## 6.1 Continuidade de negócio: RTO × RPO

Os dois objetivos que o plano de continuidade fixa para cada serviço crítico.
Guarde pela **unidade do que se perde**:

| Sigla | Nome | O que limita |
|---|---|---|
| **RTO** | Recovery **Time** Objective | **TEMPO**: quanto o serviço pode ficar indisponível até ser restabelecido |
| **RPO** | Recovery **Point** Objective | **DADO**: até que ponto no passado se aceita perder informação |

É o **RPO** que determina a **frequência do backup**: aceitar perder no máximo
15 minutos de dado obriga a proteger os dados a cada 15 minutos. O RTO cobra da
infraestrutura de recuperação (redundância, sítio alternativo, restauração).

**As siglas vizinhas que a banca oferece junto:**

- **MTBF** (Mean Time Between Failures): tempo **médio entre** falhas —
  métrica de confiabilidade, não objetivo de plano.
- **MTTR** (Mean Time To Repair): tempo **médio de reparo**.
- **SLA** (Service Level Agreement): o **acordo** de nível de serviço —
  compromisso contratual, não a métrica em si.

Pegadinha: o cenário dá dois números na ordem "pode ficar fora X, pode perder
Y" e a alternativa **inverte as siglas**. Ancore numa letra: **T** de RTO é
**Tempo**; **P** de RPO é **Ponto** no tempo (*dado*). Backup incremental ×
diferencial está em [orfaos](orfaos.md).

## 7. Detecção e resposta

- **IDS** (detecção): **alerta** sobre intrusão, passivo.
- **IPS** (prevenção): **bloqueia** ativamente (inline).
- **SIEM:** correlaciona logs/eventos para detecção e resposta.

**Resposta a incidentes (NIST SP 800-61) — a ordem cai:**
1. **Preparação** (antes de tudo: time, ferramentas, políticas).
2. **Detecção e Análise** (identificar e entender o incidente).
3. **Contenção, Erradicação e Recuperação** (isolar, remover a causa,
   restaurar serviços/backups).
4. **Atividade pós-incidente / Lições Aprendidas** (documentar, prevenir
   recorrência — realimenta a Preparação).

Pegadinha: depois de conter e erradicar vem **recuperação + lições
aprendidas** (a etapa que "fecha" o ciclo); detecção e análise vêm **antes**
da contenção.

## O que já caiu

**Em prova real da FGV:** é o bloco com mais questões reais dos específicos
(38), e a lista abaixo é quase toda verdadeira. Controle de acesso
**mandatório** (comparação de rótulos); **OWASP Top 10:2021**, identificar a
categoria válida (gabarito: SSRF, o A10 — as demais alternativas descreviam
*práticas*, não vulnerabilidades); **X.800** (mecanismo específico ×
disseminado); **SSL × TLS** — **Dataprev 2024**. Tríade **CIA** em associação
de colunas; modelo de **responsabilidade compartilhada** (PaaS); **HMAC** em
webhook; o *claim* `sub` do OIDC para rastreabilidade; aplicabilidade da LGPD a
empresa privada — **TJ-RJ**. Anonimização como tratamento que rompe a
associação ao titular; tipo de controle na ISO 27001; o *claim* `iat` do OIDC —
**MPU**. **RTO × RPO** saindo de uma BIA; **IDS × IPS** (o que *age*, não só
detecta); SSL/TLS; responsabilidade compartilhada em SaaS; **RBAC**; segregação
de funções; proprietário do ativo na 27002; tratamento de risco e risco
residual; matriz 5×5 com WAF; criptografia simétrica × assinatura digital sobre
ICP; a família de *malware* inteira (*worm*, *ransomware*, *spyware* +
*keylogger*, *phishing*); DDoS e SYN *flood*; *spoofing* de MAC/IP; NGFW, WAF,
proxy e VPN; e as etapas de **resposta a incidentes** (contenção, depois
recuperação e lições aprendidas) — **ALERO 2026**, que sozinha respondeu por 17
questões de segurança.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): **SAST × DAST** — nenhuma das 432 questões reais cita qualquer um dos
dois. Continua valendo o estudo: é par de edital e a FGV adora inverter
estático com dinâmico.

Rode `../quiz.py seguranca`.

## Pegadinhas da FGV (resumo)

- Inverter: simétrica↔assimétrica, SAST↔DAST, IDS↔IPS, DAC↔MAC, SSL↔TLS,
  hash↔cifra reversível, autenticação↔autorização (OAuth2).
- Ranking OWASP errado ou mistura de ano.
- Absolutos ("hash descriptografa", "SSL mais seguro que TLS").
- Ver `../dicas/seguranca.md`.

## Alta probabilidade / pesquisa extra

- **ISO/IEC 27002:2022:** **93 controles** em **4 temas** — organizacionais
  (37), pessoas (8), físicos (14), tecnológicos (34). A 27001:2022 é o
  **SGSI** (requisitos, Anexo A); a 27002 é o **guia de controles**. A questão
  não pede o número: dá um **exemplo de controle** e pede o tema. Mapeie assim:

  | Exemplo no enunciado | Tema |
  |---|---|
  | política de segurança, gestão de ativos, contrato com fornecedor, resposta a incidente | **Organizacional** |
  | **trabalho remoto**, triagem/contratação, conscientização e treinamento, processo disciplinar | **Pessoas** |
  | **mídia de armazenamento**, perímetro e entrada, mesa limpa, cabeamento, descarte de equipamento | **Físico** |
  | **criptografia**, cópia de segurança, registro de logs, gestão de vulnerabilidade técnica, código seguro | **Tecnológico** |

  A confusão que a banca monta é entre **pessoas** e **organizacional**: se o
  controle recai sobre **o comportamento de um indivíduo** (trabalho remoto,
  treinamento), é *pessoas*; se é **regra/estrutura da organização** (política,
  contrato), é *organizacional*.
- **SSDF (NIST SP 800-218,** *Secure Software Development Framework***):**
  práticas de desenvolvimento seguro organizadas em **quatro grupos** —
  **PO** (*Prepare the Organization*), **PS** (*Protect the Software*), **PW**
  (*Produce Well-Secured Software*) e **RV** (*Respond to Vulnerabilities*). É
  o framework que trata de **cadeia de suprimentos, ambiente de engenharia e
  treinamento** — itens que a FGV oferece como distrator em questão de **OWASP
  Top 10**, que é lista de **vulnerabilidades web**, não de práticas de
  processo.
- **NIST Cybersecurity Framework 1.1:** funções Identify, Protect, Detect,
  Respond, Recover (o 2.0 acrescentou **Govern**).
- **Gestão de risco (ISO 27005/31000):** risco = f(ameaça, vulnerabilidade,
  impacto); tratamento: mitigar, transferir, aceitar, evitar.
- **STRIDE** (modelagem de ameaças): Spoofing, Tampering, Repudiation,
  Information disclosure, Denial of service, Elevation of privilege.
