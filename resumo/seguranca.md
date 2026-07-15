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

Pegadinha: hash não é cifra reversível; confidencialidade = cifra (não hash);
assina-se com a **privada**, verifica-se com a **pública**.

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
  **OpenID Connect** (sobre OAuth2) faz autenticação.
- **SSO (Single Sign-On):** um login para vários sistemas.

Pegadinha: MAC = **rótulos** e regra central; DAC = dono decide. OAuth2 é
autorização, não autenticação.

## 5. OWASP Top 10 — **2021 E 2025** (leia os dois)

O edital aponta para o projeto OWASP (sem fixar ano). A Dataprev 2024 cobrou
o **2021**; mas o **2025** saiu em nov/2025. Sabendo os dois, você cobre
qualquer recorte.

**OWASP Top 10:2021** (referência das nossas questões):

1. A01 **Broken Access Control** (subiu para o topo)
2. A02 **Cryptographic Failures** (era "Sensitive Data Exposure")
3. A03 **Injection** (SQLi, e **XSS foi absorvido aqui** — CWE-79)
4. A04 Insecure Design (novo em 2021)
5. A05 Security Misconfiguration
6. A06 Vulnerable and Outdated Components
7. A07 Identification and Authentication Failures
8. A08 Software and Data Integrity Failures
9. A09 Security Logging and Monitoring Failures
10. A10 **Server-Side Request Forgery (SSRF)**

**OWASP Top 10:2025** (o que mudou):

- A01 **Broken Access Control** segue em 1º (e **absorveu o SSRF**).
- A02 **Security Misconfiguration** subiu de 5º para 2º.
- A03 **Software Supply Chain Failures** (novo; expande "Componentes
  vulneráveis").
- **Cryptographic Failures caiu para 4º; Injection para 5º.**
- A10 **Mishandling of Exceptional Conditions** (novo; erro/fail-open).

Pegadinha 2024: descrever "injeção" citando SQL → categoria **Injection**;
lembrar que em 2021 **XSS entrou em Injection** (era categoria própria até
2017). Se a prova disser "2025", troque o ranking conforme acima.

## 6. Desenvolvimento seguro

- **SDL (Security Development Lifecycle):** segurança em todo o ciclo.
- **SAST (estática):** analisa o **código-fonte** sem executar (caixa-branca).
- **DAST (dinâmica):** testa a **aplicação em execução** (caixa-preta).
- **IAST:** combina os dois em runtime instrumentado.
- **DevSecOps:** segurança automatizada no pipeline CI/CD.

Pegadinha: **SAST × DAST** (código parado × app rodando).

## 7. Detecção e resposta

- **IDS** (detecção): **alerta** sobre intrusão, passivo.
- **IPS** (prevenção): **bloqueia** ativamente (inline).
- **SIEM:** correlaciona logs/eventos para detecção e resposta.

## O que já caiu (nossas questões)

Controle de acesso mandatório (rótulos); OWASP Top 10:2021 (categoria válida);
X.800 mecanismos de segurança; SSL × TLS; tríade CIA; IDS × IPS; SAST × DAST;
modelo de responsabilidade compartilhada em nuvem. Rode `../quiz.py seguranca`.

## Pegadinhas da FGV (resumo)

- Inverter: simétrica↔assimétrica, SAST↔DAST, IDS↔IPS, DAC↔MAC, SSL↔TLS,
  hash↔cifra reversível, autenticação↔autorização (OAuth2).
- Ranking OWASP errado ou mistura de ano.
- Absolutos ("hash descriptografa", "SSL mais seguro que TLS").
- Ver `../dicas/seguranca.md`.

## Alta probabilidade / pesquisa extra

- **ISO/IEC 27002:2022:** **93 controles** em **4 temas** — organizacionais
  (37), pessoas (8), físicos (14), tecnológicos (34). A 27001:2022 é o
  **SGSI** (requisitos, Anexo A); a 27002 é o **guia de controles**.
- **NIST Cybersecurity Framework 1.1:** funções Identify, Protect, Detect,
  Respond, Recover (o 2.0 acrescentou **Govern**).
- **Gestão de risco (ISO 27005/31000):** risco = f(ameaça, vulnerabilidade,
  impacto); tratamento: mitigar, transferir, aceitar, evitar.
- **STRIDE** (modelagem de ameaças): Spoofing, Tampering, Repudiation,
  Information disclosure, Denial of service, Elevation of privilege.
