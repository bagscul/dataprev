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
  O barramento dessa arquitetura é o **ESB (Enterprise Service Bus)**: o
  intermediário que **roteia**, **transforma** (converte formato/protocolo
  entre sistemas que não se falam) e **orquestra** as mensagens entre os
  serviços. Concentra a inteligência da integração — e, em troca, vira ponto
  único de falha. É a diferença de filosofia para os microsserviços, que
  preferem canais burros e serviços espertos.
- **Microsserviços:** serviços pequenos, autônomos, **implantáveis
  independentemente**, cada um com **seu próprio banco** (não compartilham
  base — isso reduz acoplamento). Comunicação leve (REST/mensageria).
- **Arquitetura hexagonal (Ports & Adapters):** separa a **lógica de negócio**
  do mundo externo por **portas** (interfaces) e **adaptadores**; permite
  trocar UI/BD/serviços sem tocar no núcleo.

Pegadinhas: "microsserviços compartilham o mesmo banco" = **falso** (aumenta
acoplamento, contra o princípio); "monólito não pode ser distribuído" = falso.
Num item que descreve "o barramento que intermedeia, roteia e transforma
mensagens entre serviços", a resposta é **ESB** — os distratores são siglas de
outras prateleiras (ETL move dados para o DW, CDN entrega estático, DNS
resolve nome, VPN faz túnel).

### 2.1 Camadas lógicas (layers) × camadas físicas (tiers)

Duas coisas diferentes que o português funde em "camada":

| | O que descreve |
|---|---|
| **Layer** (lógica) | como as **responsabilidades** do software estão organizadas: apresentação, negócio, persistência |
| **Tier** (física) | em **quantos nós** o software está implantado: máquinas, processos, servidores |

Uma não obriga a outra: dá para ter **três layers em um único tier** — as três
responsabilidades separadas no código, tudo no mesmo processo, e a aplicação
segue **monolítica**. O inverso também: cliente-servidor em dois tiers pode
manter apresentação e negócio bem separados logicamente.

Pegadinhas: definir layer como "distribuição entre máquinas" e tier como
"agrupamento de responsabilidades" (invertido); o absoluto "três camadas
lógicas são **necessariamente** implantadas em três nós"; e dizer que o MVC
corresponde aos três tiers — MVC é organização, não implantação.

## 3. Integração: REST × SOAP, Web Services

| | REST | SOAP |
|---|---|---|
| Estilo | arquitetural, sobre HTTP | protocolo baseado em XML |
| Formato | JSON (comum), leve | XML (envelope), verboso |
| Contrato | OpenAPI/Swagger | WSDL |
| Estado | **stateless** | pode ter padrões WS-* |
| Vantagem | leve, escala, independe de plataforma | contratos formais, WS-Security |

- **REST é stateless:** cada requisição carrega tudo; o servidor não guarda
  **estado de sessão** → escala horizontalmente sem afinidade de sessão.
- ***Cacheable* é outra restrição:** a resposta se declara cacheável ou não, e
  quem a guarda pode ser o **cliente** *ou* um **intermediário** — proxy,
  gateway, CDN. Cache no caminho é **permitido** pelo REST; é o que deixa uma
  CDN servir o estático de um nó próximo do usuário. Não confunda: o que não
  pode ficar no servidor é o **estado da sessão**, não o cache.
- **API Gateway:** ponto único de entrada dos microsserviços (roteamento,
  autenticação, rate limit, agregação).
- **Métodos HTTP:** GET (ler), POST (criar), **PUT (substituir inteiro)**,
  **PATCH (atualizar parcial)**, DELETE. Códigos: 200 OK, 201 Created, 204
  No Content, 400, 401, 403, 404, 500.
- **UDDI:** diretório (legado) para **descoberta/registro** de web services
  SOAP, junto do WSDL (contrato) e SOAP (mensagem). Trio clássico WS-*:
  **SOAP + WSDL + UDDI**.
- **Swagger / OpenAPI:** o **OpenAPI** é a especificação padrão para
  **documentar e contratar APIs REST** (endpoints, parâmetros, respostas);
  **Swagger** é o conjunto de ferramentas (Swagger UI, editor, codegen) em
  cima dela. É o "WSDL do REST".

Pegadinha: **PUT × PATCH** (substituição total × parcial); SOAP "sem contrato
formal" contradiz o próprio SOAP (usa WSDL); UDDI é **descoberta**, WSDL é
**contrato**, SOAP é a **mensagem**.

## 3.1 Mensageria (comunicação assíncrona)

Desacopla produtor e consumidor: quem envia não espera quem processa.

| Modelo | Como funciona | Exemplo |
|---|---|---|
| **Fila (queue)** | mensagem consumida por **um** consumidor (point-to-point) | RabbitMQ, SQS |
| **Publish/Subscribe (tópico)** | mensagem entregue a **vários** assinantes | Kafka, SNS |

- **Apache Kafka:** plataforma de **streaming** de eventos — produtores
  publicam em **tópicos** (particionados), consumidores leem em **grupos**;
  guarda o log de eventos (permite reprocessar). Alta vazão, escalável.
- Benefícios: desacoplamento, absorção de picos (buffer), resiliência.
- **Broker** é o intermediário (Kafka, RabbitMQ). Casa com **microsserviços**
  e com o padrão **Saga** (eventos de compensação) e **Event Sourcing**.

Pegadinha: fila (**um** consumidor) × tópico/pub-sub (**vários**); mensageria é
**assíncrona** (≠ chamada REST síncrona).

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
  **Cloud bursting:** estende para a nuvem pública no pico.
- **Serverless / FaaS (Function as a Service):** o código é publicado como
  **função** e o provedor a executa **por evento**. Não é "sem servidor" — é o
  **cliente que não gerencia** servidor. O que se cobra: escala **de zero** a
  muitas execuções conforme os eventos; **cobrança pelo tempo e pelos recursos
  consumidos**; execução **sem estado** entre invocações (estado vai para fora);
  **cold start** (latência maior na primeira invocação após ociosidade); e
  **limite de tempo por execução**, que o desaconselha para processamento longo
  e contínuo.
- **Balanceador de carga × CDN:** atacam gargalos **diferentes** e por isso se
  somam. O **balanceador** reparte requisições entre as instâncias (resolve
  **sobrecarga de processamento**); a **CDN** replica o conteúdo **estático**
  em pontos de presença e entrega do nó mais próximo (resolve **latência
  geográfica**).
- **Containers (Docker) × VM:** container compartilha o **kernel** do SO
  (leve, rápido); VM tem SO convidado completo sobre um hipervisor (isola
  mais, pesa mais). **Kubernetes** orquestra containers.
- **Hipervisor Tipo 1** (bare-metal, roda direto no hardware: ESXi, Hyper-V,
  KVM) × **Tipo 2** (hosted, roda sobre um SO: VirtualBox, VMware Workstation).
- **Virtualização total** (SO convidado não sabe que é virtual) ×
  **paravirtualização** (SO convidado é modificado e coopera com o hipervisor
  — mais rápido). **VDI** = virtualização de desktops entregues remotamente.

Pegadinha: "adicionar recursos à instância" é **vertical**, jamais
horizontal; container ≠ VM (kernel compartilhado × SO próprio).

Em **serverless**, cada distrator nega uma característica: "não há servidor, o
código roda no dispositivo que dispara o evento" (há servidor, do provedor);
"o estado da execução anterior permanece" (é sem estado); "a latência da
primeira invocação é igual às demais" (ignora o cold start); "remove o limite
de tempo por execução" (o limite existe). Em **balanceador × CDN**, a inversão
troca os papéis ou declara um deles redundante — guie-se pelo sintoma:
"instâncias sobrecarregadas" → balanceador; "lentidão para usuários distantes
/ arquivos estáticos" → CDN.

## 6. Transações distribuídas

- **2PC (Two-Phase Commit):** coordenador + participantes; exige
  **unanimidade** (todos confirmam) para commit. Bloqueante.
- **Saga:** sequência de transações locais com **compensação** em caso de
  falha (padrão para microsserviços).
- **Raft:** algoritmo de **consenso** — resolve problema *diferente* do 2PC.
  Não pergunta "todos aceitam efetivar esta transação?", e sim "em que
  **sequência de operações** este grupo de réplicas concorda?". Funciona por
  **eleição de líder** (o líder ordena e replica o *log*) e decide por
  **maioria** (quórum), o que o torna **tolerante a falhas**: sobrevive à
  queda da minoria, inclusive do líder, substituído por nova eleição. É o que
  sustenta o *etcd* (e, por tabela, o Kubernetes).

Pegadinha — **2PC × Raft** é o par do bloco: o 2PC é *commit atômico*, exige
**unanimidade** e **bloqueia** se o coordenador cair (ponto único de falha); o
Raft é *consenso*, decide por **maioria** e **continua funcionando** com a
minoria fora. Trocar "unanimidade" por "maioria" de um para o outro é o
distrator pronto, e "o 2PC tolera a falha do coordenador" é falso.

## O que já caiu (nossas questões)

Servidor web × de aplicação; SOA e web services (baixo acoplamento, REST);
arquitetura hexagonal × microsserviços (não compartilham banco); internet/
extranet/intranet/portal; escalabilidade horizontal × vertical (com cálculo
de custo-benefício); REST stateless; container × VM; API gateway; taints/
tolerations no Kubernetes; cloud bursting; 2PC × Raft; ESB como barramento da
SOA; layers × tiers; serverless/FaaS; balanceador × CDN.
Rode `../quiz.py arquitetura`.

## Pegadinhas da FGV (resumo)

- Inverter: web↔aplicação, horizontal↔vertical, PUT↔PATCH, container↔VM,
  intranet↔extranet, SOA↔monólito.
- Absolutos e contradições internas ("SOAP sem contrato", "microsserviço com
  banco único compartilhado").
- Cenário com números de custo (escolher a opção de melhor custo-benefício).
- Ver `../dicas/arquitetura.md`.

## Alta probabilidade / pesquisa extra

- **12-Factor App** (boas práticas de app nativa de nuvem).
- **DDD (Domain-Driven Design):** bounded context, agregados, Repository,
  Factory, Ubiquitous Language, eventos de domínio imutáveis. Caiu no **MPU
  2025** (gabarito: o *Aggregate* garante a consistência das mudanças num
  modelo de associações complexas) e no **TJ-RJ 2** (gabarito: eventos de
  domínio são ordinariamente imutáveis, por registrarem algo já ocorrido).
- **Service mesh** (Istio) × API gateway: mesh cuida da comunicação
  serviço-a-serviço (leste-oeste); gateway cuida da entrada (norte-sul).
- **IaC (Infraestrutura como Código):** Terraform, Ansible — provisiona
  ambiente de forma declarativa e versionada.
- **Kubernetes — *taint* × *toleration*:** o par de **repulsão**, e funciona
  ao contrário do que o nome sugere. O **taint** vai no **nó** e *afasta* pods
  ("não me escalone nada, a menos que aceite esta marca"); a **toleration** vai
  no **pod** e diz "eu *tolero* essa marca", tornando-o *elegível* àquele nó.
  Serve para reservar nós especiais (GPU, banco, nó mestre). Cuidado: tolerar
  **não é atrair** — o pod que tolera *pode* ir para lá, não *tem* que ir; quem
  atrai é *node affinity*/*nodeSelector*. Distribuições: RKE1/RKE2/K3s/EKS,
  Rancher.
- **Armazenamento de objetos:** *flat namespace* (sem hierarquia de pastas
  real), acesso por API REST.
