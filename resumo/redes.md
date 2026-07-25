# Redes de Computadores — resumo (FORA do edital do Perfil 3, mas cai)

> **⚠️ Atenção:** Redes de Computadores **não está** no conteúdo do Perfil 3
> (está nos Perfis 2 e 5). O edital do Perfil 3 só cita HTTPS e SSL/TLS. Mesmo
> assim, a **Dataprev 2024 trouxe ~3 questões de redes** para Desenvolvimento
> de Software (modelo OSI, protocolo, segurança de rede). Ignorar custou 7,5
> pontos. Estude o essencial — é seguro de ponto barato.

## 1. Modelos de referência

**OSI (7 camadas)** — de baixo para cima:

| # | Camada | Função | Exemplos |
|---|---|---|---|
| 1 | Física | bits no meio | cabos, sinais |
| 2 | Enlace | quadros, MAC | switch, Ethernet |
| 3 | Rede | pacotes, IP, roteamento | roteador, IP |
| 4 | Transporte | fim a fim, portas | TCP, UDP |
| 5 | Sessão | diálogo, checkpoints | — |
| 6 | Apresentação | formato, cifra, compressão | TLS (discutível) |
| 7 | Aplicação | serviços ao usuário | HTTP, DNS, SMTP |

**TCP/IP (4 camadas):** Acesso à Rede, Internet (IP), Transporte (TCP/UDP),
Aplicação. Mnemônico OSI: **F**ísica **E**nlace **R**ede **T**ransporte
**S**essão **A**presentação **A**plicação.

Pegadinha: trocar a camada de um elemento (switch=2/enlace, roteador=3/rede);
"sessão" cuida de checkpoints/diálogo.

## 2. Equipamentos

- **Hub** (camada 1, burro, repete para todos) × **Switch** (camada 2, usa
  MAC, comuta para a porta certa) × **Roteador** (camada 3, usa IP, interliga
  redes). Há switch L3 (roteia), mas o par clássico é switch=2, roteador=3.

## 3. TCP × UDP

| | TCP | UDP |
|---|---|---|
| Conexão | orientado a conexão (handshake 3 vias) | sem conexão |
| Confiabilidade | garante entrega e ordem | não garante |
| Uso | web, e-mail, transferência | streaming, DNS, VoIP |

## 4. Protocolos e portas (as que caem)

| Protocolo | Porta | Função |
|---|---|---|
| **HTTP** | 80 | web |
| **HTTPS** | 443 | web seguro (TLS) |
| **FTP** | 21 (20 dados) | transferência |
| **SSH** | 22 | acesso remoto seguro |
| **SMTP** | 25 | envio de e-mail |
| **DNS** | 53 | nomes → IP |
| **POP3 / IMAP** | 110 / 143 | leitura de e-mail |
| **DHCP** | 67/68 | IP automático |

## 5. Endereçamento IP

- **IPv4:** 32 bits. Faixas privadas (**RFC 1918**): 10.0.0.0/8,
  172.16.0.0/12, 192.168.0.0/16.
- **IPv6:** 128 bits; prefixo de sub-rede típico /64.
- **Roteamento:** rota estática × dinâmica (OSPF, RIP, BGP); **distância
  administrativa** desempata a fonte da rota.

## 5.1 Comutação e encaminhamento (MPLS, VLAN, NAT)

- **MPLS (Multiprotocol Label Switching):** encaminha por **rótulos (labels)**
  em vez de olhar o IP de destino a cada salto — por isso é chamado de
  **"camada 2.5"** (opera entre o enlace/L2 e a rede/L3). Cria caminhos (LSP)
  para engenharia de tráfego e QoS.
- **VLAN:** segmenta logicamente a camada 2 (broadcast domains separados no
  mesmo switch físico).
- **NAT:** traduz endereços privados ↔ público (economiza IPv4, oculta a rede
  interna).

Pegadinha: MPLS é **rótulo** ("2.5"), não roteamento IP puro; VLAN segmenta L2.

## 6. Tipos de rede corporativa

| Tipo | Quem acessa |
|---|---|
| **Internet** | rede **pública global**, aberta |
| **Intranet** | rede **interna** da organização, restrita a quem está dentro |
| **Extranet** | acesso **controlado a externos** (parceiros, fornecedores, clientes) |
| **Portal** | ponto **único de acesso** que agrega serviços e sistemas |

Pegadinha: inverter os três papéis é o distrator clássico — chamar intranet de
"rede pública global", extranet de "só interna", Internet de "rede restrita".
A extranet é o meio-termo: **externo, mas autorizado**. Ver `arquitetura.md`.

## 7. Segurança de rede (interface com Segurança da Informação)

- **Firewall** (filtra tráfego), **proxy**, **VPN** (IPsec, SSL VPN).
- **IDS** (detecta/alerta) × **IPS** (bloqueia). Ver `seguranca.md`.
- **NAT** traduz endereços; **VLAN** segmenta a camada 2.

### 7.1 Firewall stateful × stateless

| | **Stateless** (filtro de pacotes) | **Stateful** (com estado) |
|---|---|---|
| O que olha | cada pacote **isoladamente**: IP de origem/destino, porta, protocolo | o pacote **no contexto da sessão** |
| Como decide | só pela regra estática | mantém uma **tabela de estado** das conexões ativas |
| Efeito prático | para liberar a resposta é preciso escrever a regra de volta à mão | a resposta de conexão iniciada de dentro já é aceita |

Os dois atuam nas camadas 3 e 4. Quem sobe para a camada 7 (inspeciona o
conteúdo da aplicação) é o **NGFW** ou o **WAF** — outra coisa.

Pegadinha: o distrator descreve o **stateless** e chama de stateful ("analisa
apenas os cabeçalhos de cada pacote isoladamente"). Outro: dizer que o
stateful "atua **exclusivamente** na camada de aplicação".

### 7.2 SSH × Telnet e o handshake do TLS

- **Telnet** (porta **23**) trafega **tudo em texto claro**, inclusive a senha
  do administrador. O **SSH** (porta **22**) faz a mesma administração remota
  **cifrando toda a comunicação, inclusive a autenticação**. O motivo da
  substituição é **criptografia**, não velocidade.
- No **HTTPS**, o TLS usa criptografia **híbrida** — e a divisão de trabalho é
  o que a FGV cobra:
  - **Assimétrica, só no handshake:** o certificado autentica o **servidor** e
    o par de chaves serve para as pontas **acordarem a chave simétrica de
    sessão**.
  - **Simétrica, no resto:** cifra todo o volume de dados da sessão, porque é
    **muito mais rápida**.
- A assimétrica é lenta demais para o tráfego inteiro; a simétrica sozinha não
  resolveria *como* combinar a chave por um canal inseguro. Daí o híbrido.

Pegadinha: dizer que a assimétrica "cifra todo o tráfego da sessão" (não: ela
só **troca a chave**), que "autentica o usuário final por login e senha" (não:
autentica o **servidor**, por certificado) ou que "dispensa certificados". Em
SSH, o distrator inverte o motivo — "é mais rápido por não usar criptografia"
descreve o **Telnet**.

## O que já caiu (nossas questões)

Camada OSI de sessão (checkpoints); switch × roteador × hub; TCP × UDP;
portas; RFC 1918; IPv6 128 bits; roteamento estático × OSPF (distância
administrativa); ACL Cisco (wildcard mask). Rode `../quiz.py redes`.

## Estratégia

Não vale estudar redes com a profundidade dos Perfis 2/5. Cubra: **OSI/TCP-IP,
equipamentos por camada, TCP×UDP, portas comuns, IP público×privado, IDS×IPS**.
Isso resolve o padrão histórico da FGV para o perfil de desenvolvimento com
pouco tempo investido. Ver `../dicas/redes.md`.
