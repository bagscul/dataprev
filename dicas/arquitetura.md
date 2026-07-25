# arquitetura — como a FGV cobra

## O que mais cai
- Nuvem e escalabilidade: vertical (mais recurso na mesma
  instância) x horizontal (mais instâncias) com conta de
  custo-benefício; cloud bursting (estende para nuvem pública
  no pico); cloud-native x híbrida (trade-offs). Muito
  recorrente nas provas recentes (TJ-RJ). Também serverless/
  FaaS (escala de zero, cobrança por tempo consumido, sem
  estado, cold start, limite de tempo) e o par balanceador de
  carga x CDN.
- Camadas lógicas (layers) x camadas físicas (tiers) — o
  português funde as duas em "camada" e a banca explora isso.
- ESB (Enterprise Service Bus): o barramento da SOA, que
  roteia, transforma e orquestra mensagens entre serviços.
- Estilos e integração: cliente-servidor, REST (vantagens/
  desvantagens: sem estado de sessão no servidor, respostas
  cacheáveis, interface uniforme) x SOAP/WSDL; SOA e Web Services com
  baixo acoplamento e interoperabilidade; hexagonal (portas e
  adaptadores) x microsserviços x monólito.
- DDD: Aggregates (garantem consistência das mudanças),
  Repository, Factory, Entidades/Objetos de Valor, Linguagem
  Onipresente (Ubiquitous Language), eventos de domínio
  imutáveis. Apareceu em MPU e TJ-RJ.
- Containers/orquestração: Kubernetes (taints/tolerations,
  distribuições RKE1/RKE2/K3s/EKS, Rancher), hipervisor Tipo
  1 x Tipo 2 x contêiner. Mensageria: RabbitMQ (entrega,
  filas duráveis, publisher confirms).
- Servidor web x servidor de aplicação; armazenamento de
  objetos (flat namespace, API REST). Fundamentos de SO
  (paginação/memória virtual, E/S bloqueante, troca de
  contexto) entram como "arquitetura" na FGV.
- Design x Arquitetura de software (alto nível x baixo nível).

## Como a banca arma a pegadinha
- Inverte os pares clássicos: servidor web (páginas/HTTP,
  estático e dinâmico) x servidor de aplicação (lógica de
  negócio); alto nível = arquitetura/estrutura x baixo nível
  = detalhe/método — o distrator troca as definições.
- REST: atribui a ele características de SOAP/RPC (sessão no
  servidor, estado por cliente, XML/WSDL) ou diz que cache
  "mantém dados atualizados". REST é stateless: o ESTADO DE
  SESSÃO é que não fica no servidor.
- Cache: o distrator diz que em REST o cache "fica só no
  cliente". A restrição cacheable admite cache em
  INTERMEDIÁRIOS (proxy, gateway, CDN) — é exatamente o que
  permite a CDN existir.
- SOA/baixo acoplamento: distrator diz que mudança em um
  serviço "se reflete diretamente no outro" (isso é ALTO
  acoplamento) ou propõe SOAP sem contrato / monólito.
- DDD: troca o papel dos blocos — diz que Repository instancia
  por métodos externos, que Aggregate expõe referência a cada
  entidade interna, ou que modelo de domínio é acoplado ao
  armazenamento. Aggregate protege invariantes, não expõe.
- Escalabilidade: chama "adicionar recursos à instância" de
  horizontal, ou "adicionar instâncias" de vertical.
- Layers x tiers: define layer como "distribuição entre
  máquinas" e tier como "agrupamento de responsabilidades" —
  invertido. Ou usa o absoluto "três camadas lógicas são
  NECESSARIAMENTE três nós físicos". Ou casa MVC com tiers.
- Serverless: cada distrator nega uma característica — "não
  há servidor" (há, do provedor), "o estado permanece entre
  chamadas" (é sem estado), "a primeira invocação tem a mesma
  latência" (ignora o cold start), "não há limite de tempo por
  execução" (há, e é o que o desaconselha para job longo).
- Balanceador x CDN: troca os papéis (diz que a CDN distribui
  requisição dinâmica e o balanceador replica estático na
  borda) ou declara um dos dois redundante.
- ESB: oferece siglas de outra prateleira — ETL, CDN, DNS,
  VPN — para o item que descreve o barramento da SOA.

## Como se sair melhor
- Vertical = SCALE UP (uma máquina maior); horizontal = SCALE
  OUT (mais máquinas). Na conta de custo, some capacidade das
  novas instâncias e compare o preço.
- REST: stateless, respostas cacheáveis (no cliente OU em
  intermediários), interface uniforme, escala porque o
  servidor não guarda estado de sessão. SOAP: contrato
  WSDL/XML, mais pesado, RPC. WSDL válido tem <wsdl:service>/
  <wsdl:port>/<wsdl:binding>.
- DDD lado a lado: Aggregate = fronteira de consistência;
  Repository = coleção/persistência do agregado; Factory =
  criação; Ubiquitous Language = vocabulário comum
  domínio↔código; eventos de domínio = imutáveis (fato
  passado).
- Baixo acoplamento = mudança em um serviço NÃO obriga mudança
  no outro. Se a alternativa vende "reflete diretamente",
  descarte.
- Layer = responsabilidade no CÓDIGO; tier = nó onde RODA.
  Três layers cabem num tier só, e a aplicação segue
  monolítica.
- Balanceador x CDN, guie-se pelo sintoma do enunciado:
  "instâncias sobrecarregadas" → balanceador; "lentidão para
  usuário distante / arquivo estático" → CDN. São gargalos
  diferentes, então somam.
- Gatilhos: "sempre", "exclusivamente", "elimina a necessidade
  de", "idêntico ao".
