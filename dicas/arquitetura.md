# arquitetura — como a FGV cobra

## O que mais cai
- Nuvem e escalabilidade: vertical (mais recurso na mesma
  instância) x horizontal (mais instâncias) com conta de
  custo-benefício; cloud bursting (estende para nuvem pública
  no pico); cloud-native x híbrida (trade-offs). Muito
  recorrente nas provas recentes (TJ-RJ).
- Estilos e integração: cliente-servidor, REST (vantagens/
  desvantagens: sem estado no servidor, cache no cliente,
  interface uniforme) x SOAP/WSDL; SOA e Web Services com
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
  "mantém dados atualizados". REST é stateless; estado fica no
  cliente.
- SOA/baixo acoplamento: distrator diz que mudança em um
  serviço "se reflete diretamente no outro" (isso é ALTO
  acoplamento) ou propõe SOAP sem contrato / monólito.
- DDD: troca o papel dos blocos — diz que Repository instancia
  por métodos externos, que Aggregate expõe referência a cada
  entidade interna, ou que modelo de domínio é acoplado ao
  armazenamento. Aggregate protege invariantes, não expõe.
- Escalabilidade: chama "adicionar recursos à instância" de
  horizontal, ou "adicionar instâncias" de vertical.

## Como se sair melhor
- Vertical = SCALE UP (uma máquina maior); horizontal = SCALE
  OUT (mais máquinas). Na conta de custo, some capacidade das
  novas instâncias e compare o preço.
- REST: stateless, cache no cliente, interface uniforme,
  escala porque o servidor não guarda sessão. SOAP: contrato
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
- Gatilhos: "sempre", "exclusivamente", "elimina a necessidade
  de", "idêntico ao".
