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

No mundo Java a distinção fica literal: o servidor de aplicação implementa a
especificação **Java EE/Jakarta EE** completa — traz o **container web**
(Servlet/JSP) **e mais** o **container EJB** para os componentes de negócio,
além de transações distribuídas, JMS e injeção de dependência. O Tomcat é
servidor web + container web, mas não é servidor de aplicação completo: não
tem container EJB.

Pegadinha: a FGV troca os papéis ("servidor web processa lógica de negócio").
O **web** recebe a requisição HTTP; o **de aplicação** roda a regra de negócio.
Outros distratores do par: o de aplicação "é **sempre** mais leve" (é o
oposto), "dispensa a JVM" (roda sobre ela), "não suporta HTTP" (suporta — ele
contém o container web). O "sempre" já entrega o primeiro.

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
- **Os elementos do WSDL** (a FGV mostra um trecho e pergunta o que falta ou o
  que é inválido), do abstrato para o concreto:

  | Elemento | O que declara |
  |---|---|
  | `<wsdl:types>` | os **tipos de dado** usados (em XML Schema) |
  | `<wsdl:message>` | as **mensagens** trocadas (na 2.0 some, absorvido pelos tipos) |
  | `<wsdl:portType>` | as **operações** disponíveis — a interface **abstrata** (chamado `interface` na 2.0) |
  | `<wsdl:binding>` | **como** as operações trafegam: protocolo e formato concretos (SOAP/HTTP) |
  | `<wsdl:service>` | o **serviço**, que agrupa uma ou mais `<wsdl:port>` |
  | `<wsdl:port>` | o **endereço** (URL) onde o binding está publicado |

  Guarde a espinha: **portType = o quê** (abstrato) · **binding = como**
  (protocolo) · **service/port = onde** (endereço). O distrator troca essas
  três camadas de lugar — dizer que o `binding` informa a URL, ou que o
  `service` lista as operações.
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
- **RabbitMQ — garantia de entrega, nas duas pontas.** Do **produtor** para o
  broker: ***publisher confirms*** — o broker devolve um `ack` dizendo que
  assumiu a mensagem (sem isso, o `publish` é "atirar e esquecer" e a mensagem
  pode se perder antes de ser gravada). Do broker para o **consumidor**:
  ***consumer acknowledgements*** — a mensagem só sai da fila quando o
  consumidor confirma o processamento. Para sobreviver a um restart do broker é
  preciso o trio: **fila durável**, **mensagem persistente** e **confirmação**.
  Nenhum dos três sozinho resolve, e é exatamente aí que o distrator mora.

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

## O que já caiu

**Em prova real da FGV:** servidor web × de aplicação; SOA e web services
(baixo acoplamento); arquitetura hexagonal × microsserviços — a afirmativa
falsa é justamente "microsserviços compartilham o mesmo banco"; **design ×
arquitetura** (amplo/estrutural contra detalhado/específico) — **Dataprev
2024**, que também cobrou internet/intranet/extranet/portal, ali como item de
*redes*. Escalabilidade horizontal × vertical **com cálculo de
custo-benefício**; **REST stateless** (a escalabilidade vem da ausência de
estado no servidor); **taints/tolerations** no Kubernetes; **cloud bursting**;
container × VM em cenário de latência e isolamento; **object storage** de
espaço de nomes plano; cloud-native × híbrida; cliente-servidor à Sommerville
(o modelo é **lógico**); **WSDL** como descrição do web service; RabbitMQ e a
entrega *exactly-once* — **TJ-RJ**. **DDD** depois da modelagem do domínio e
escolha de distribuição do Kubernetes sob o Rancher — **MPU**. Balanceador de
carga com **afinidade de sessão** (e o preço que ela cobra em tolerância a
falhas), framework de arquitetura corporativa por *views* e *viewpoints*,
**VDI**, PaaS gerenciado, **paravirtualização** com *hypercalls*,
responsabilidade compartilhada em SaaS e **WSDL** de novo — **ALERO 2026**.

**Fora do edital, mas presente na amostra:** 11 das 34 questões tagueadas
`arquitetura` são **arquitetura de computadores e sistema operacional** — Von
Neumann e seu gargalo, ULA e unidade de controle, *overflow* × *carry*,
conversão de base, ROM e firmware, ciclo busca-decodificação-execução, MMU/TLB
e *thrashing*, tabela de páginas, DMA. Vieram de provas de outro perfil (ALERO
2026 e TJ-RJ); o edital do Perfil 3 fala em arquitetura *de software*. Saiba
que existem, não gaste tempo nelas.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): **ESB** como barramento da SOA; **API gateway**; **Raft** (o 2PC, esse
sim, caiu na ALERO 2026 pelo lado de banco distribuído); layers × tiers como
par; serverless/FaaS e CDN como item próprio — os dois só apareceram como nome
de produto entre distratores.

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
- **DDD (Domain-Driven Design)** — modelar o software a partir do **domínio**,
  em conversa com o especialista de negócio. Os blocos que a banca cobra:

  | Bloco | O que é — e o erro que a FGV insere |
  |---|---|
  | **Aggregate** | **fronteira de consistência**: um conjunto de objetos tratado como unidade, com uma **raiz** que é o único ponto de entrada. Ele **protege invariantes** e **não expõe** referência a cada entidade interna — o distrator diz o contrário |
  | **Repository** | dá acesso ao agregado **como se fosse uma coleção**, escondendo a persistência. Não é "retornar classes para o cliente instanciar por métodos externos" |
  | **Factory** | encapsula a **criação** de objeto/agregado complexo — criação, não estratégia de armazenamento |
  | **Entidade × Objeto de Valor** | entidade tem **identidade** que persiste no tempo; objeto de valor é definido **só pelos seus atributos** e é intercambiável |
  | **Ubiquitous Language** | **vocabulário único** entre domínio e código: o termo do negócio vira o nome da classe. Não é "expressar o modelo como fábricas encapsuladas por objetos de valor" |
  | **Bounded context** | a **fronteira** dentro da qual um termo tem um significado só; contextos diferentes podem usar a mesma palavra com sentidos distintos |
  | **Eventos de domínio** | registram **algo que já aconteceu** — por isso são **imutáveis** |

  Caiu no **MPU 2025** (gabarito: o *Aggregate* garante a consistência das
  mudanças num modelo de associações complexas) e no **TJ-RJ 2** (gabarito:
  eventos de domínio são ordinariamente imutáveis, por registrarem algo já
  ocorrido). Note o padrão: nas duas, os distratores eram os **outros blocos
  com o papel adulterado** — vale ler cada alternativa perguntando "esse bloco
  faz mesmo isso?".
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
