# Arquitetura de Software — resumo (Perfil 3)

> **Edital (Perfil 3):** arquitetura de software; interoperabilidade;
> arquitetura e linguagem orientada a serviços; web services; mensageria;
> API, Swagger; arquitetura orientada a objetos; aplicações para ambiente
> web; servidor de aplicações × servidor web; internet/extranet/intranet/
> portal; arquitetura hexagonal, microsserviços (orquestração e API gateway),
> containers; transações distribuídas.
> **Peso esperado: ALTO.** Nuvem, REST×SOAP, microsserviços e containers são
> recorrentes.

## 1. Servidor web × servidor de aplicação

| | Servidor **web** | Servidor de **aplicação** |
|---|---|---|
| Função | atende HTTP, serve conteúdo estático/dinâmico | executa **lógica de negócio**, integra com BD |
| Exemplos | Apache, NGINX | JBoss/WildFly, WebLogic, Tomcat (parcial) |

Pegadinha: a FGV troca os papéis ("servidor web processa lógica de negócio").
O **web** recebe a requisição HTTP; o **de aplicação** roda a regra de negócio.

## 2. Estilos de arquitetura

- **Monolítica:** tudo num artefato único, implantado junto. Simples de
  começar; acopla e dificulta escalar partes isoladas.
- **Cliente-servidor, N camadas, P2P, barramento de mensagens.**
- **SOA (orientada a serviços):** serviços reutilizáveis, contrato explícito,
  baixo acoplamento, interoperabilidade. Web services são a tecnologia comum.
- **Microsserviços:** serviços pequenos, autônomos, **implantáveis
  independentemente**, cada um com **seu próprio banco** (não compartilham
  base — isso reduz acoplamento). Comunicação leve (REST/mensageria).
- **Arquitetura hexagonal (Ports & Adapters):** separa a **lógica de negócio**
  do mundo externo por **portas** (interfaces) e **adaptadores**; permite
  trocar UI/BD/serviços sem tocar no núcleo.

Pegadinhas: "microsserviços compartilham o mesmo banco" = **falso** (aumenta
acoplamento, contra o princípio); "monólito não pode ser distribuído" = falso.

## 3. Integração: REST × SOAP, Web Services

| | REST | SOAP |
|---|---|---|
| Estilo | arquitetural, sobre HTTP | protocolo baseado em XML |
| Formato | JSON (comum), leve | XML (envelope), verboso |
| Contrato | OpenAPI/Swagger | WSDL |
| Estado | **stateless** | pode ter padrões WS-* |
| Vantagem | leve, escala, independe de plataforma | contratos formais, WS-Security |

- **REST é stateless:** cada requisição carrega tudo; o servidor não guarda
  sessão → escala horizontalmente sem afinidade de sessão.
- **API Gateway:** ponto único de entrada dos microsserviços (roteamento,
  autenticação, rate limit, agregação).
- **Mensageria** (Kafka, filas): comunicação **assíncrona** e desacoplada.
- **Métodos HTTP:** GET (ler), POST (criar), **PUT (substituir inteiro)**,
  **PATCH (atualizar parcial)**, DELETE. Códigos: 200 OK, 201 Created, 204
  No Content, 400, 401, 403, 404, 500.

Pegadinha: **PUT × PATCH** (substituição total × parcial); SOAP "sem contrato
formal" contradiz o próprio SOAP (usa WSDL).

## 4. Ambientes de rede corporativa

| Termo | Alcance |
|---|---|
| **Internet** | rede pública global |
| **Intranet** | rede interna da organização (só funcionários) |
| **Extranet** | acesso controlado a parceiros/clientes externos autorizados |
| **Portal** | ponto único que centraliza informação/serviços |

Pegadinha: trocar intranet↔extranet↔internet. Extranet = interno **+**
parceiros externos autorizados.

## 5. Nuvem e escalabilidade

- **Modelos de serviço:** **IaaS** (infra), **PaaS** (plataforma), **SaaS**
  (software pronto). Regra: quanto mais "as a Service", menos você gerencia.
- **Modelos de implantação:** privada, pública, híbrida.
- **Escalabilidade horizontal (scale out):** **adicionar instâncias/nós**.
- **Escalabilidade vertical (scale up):** **adicionar recursos à instância**
  existente (mais CPU/RAM).
- **Elasticidade:** ajustar capacidade automaticamente conforme a demanda.
- **Containers (Docker) × VM:** container compartilha o **kernel** do SO
  (leve, rápido); VM tem SO convidado completo sobre um hipervisor (isola
  mais, pesa mais). **Kubernetes** orquestra containers.

Pegadinha: "adicionar recursos à instância" é **vertical**, jamais
horizontal; container ≠ VM (kernel compartilhado × SO próprio).

## 6. Transações distribuídas

- **2PC (Two-Phase Commit):** coordenador + participantes; exige
  **unanimidade** (todos confirmam) para commit. Bloqueante.
- **Saga:** sequência de transações locais com **compensação** em caso de
  falha (padrão para microsserviços).

## O que já caiu (nossas questões)

Servidor web × de aplicação; SOA e web services (baixo acoplamento, REST);
arquitetura hexagonal × microsserviços (não compartilham banco); internet/
extranet/intranet/portal; escalabilidade horizontal × vertical (com cálculo
de custo-benefício); REST stateless; container × VM; API gateway; taints/
tolerations no Kubernetes; cloud bursting; 2PC × Raft. Rode `../quiz.py arquitetura`.

## Pegadinhas da FGV (resumo)

- Inverter: web↔aplicação, horizontal↔vertical, PUT↔PATCH, container↔VM,
  intranet↔extranet, SOA↔monólito.
- Absolutos e contradições internas ("SOAP sem contrato", "microsserviço com
  banco único compartilhado").
- Cenário com números de custo (escolher a opção de melhor custo-benefício).
- Ver `../dicas/arquitetura.md`.

## Alta probabilidade / pesquisa extra

- **12-Factor App** (boas práticas de app nativa de nuvem).
- **DDD (Domain-Driven Design):** bounded context, agregados — casou com
  microsserviços no TJ-RJ.
- **Service mesh** (Istio) × API gateway: mesh cuida da comunicação
  serviço-a-serviço (leste-oeste); gateway cuida da entrada (norte-sul).
- **IaC (Infraestrutura como Código):** Terraform, Ansible — provisiona
  ambiente de forma declarativa e versionada.
