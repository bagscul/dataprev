# Redes de Computadores — resumo (FORA do edital do Perfil 3, mas cai)

> **⚠️ Atenção:** Redes de Computadores enquanto disciplina **não está** no
> conteúdo do Perfil 3 (está nos Perfis 2 e 5). Ainda assim, a **Dataprev
> 2024 trouxe 1 questão genuinamente fora do edital** (X.800, arquitetura de
> segurança do modelo OSI) — 2,5 pontos por ignorar. Uma segunda questão
> parece a mesma pegadinha (ambientes de Internet, intranet, extranet e
> portal), mas é o **item 4** do próprio edital de Desenvolvimento de
> Sistemas — não é rede "de fora". Estude o essencial abaixo — é seguro de
> ponto barato.

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

### 5.1 Sub-redes: máscara × hosts utilizáveis

Com **h** bits sobrando para host, **hosts utilizáveis = 2ʰ − 2** (descontam-se
o endereço de **rede** e o de **broadcast**). O prefixo /n deixa h = 32 − n.

| Prefixo | Máscara | Bits de host | Hosts utilizáveis |
|---|---|---|---|
| /24 | 255.255.255.0 | 8 | 254 |
| /25 | 255.255.255.128 | 7 | 126 |
| /26 | 255.255.255.192 | 6 | 62 |
| /27 | 255.255.255.224 | 5 | **30** |
| /28 | 255.255.255.240 | 4 | 14 |

O enunciado dá a necessidade ("no máximo 30 hosts") e pede a máscara: procure
a **menor** sub-rede que **comporta** o número — 30 cabem em /27 exatamente;
/26 (62) desperdiça e /28 (14) não cabe.

**IPv6 — notação simplificada.** Duas regras, nesta ordem: (1) apague os
**zeros à esquerda** de cada grupo (`0DB8` → `DB8`, `0001` → `1`); (2)
substitua **uma única** sequência de grupos inteiramente nulos por `::` — só
uma vez, senão fica ambíguo. Assim
`2001:0DB8:0000:0000:0000:0000:FE00:0001` → `2001:DB8::FE00:1`.

### 5.2 Comutação e encaminhamento (MPLS, VLAN, NAT)

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

## O que já caiu

**Em prova real da FGV:** camada OSI **por função** — sessão e *checkpoints*
na retomada de transferência interrompida —, **rota estática × OSPF** pela
distância administrativa, **ACL Cisco com wildcard mask** e volume anômalo de
handshakes TCP (SYN flood) — **TJ-RJ**. Camada OSI para **diagnosticar** falha
entre servidor e switch; **switch × roteador × hub/repetidor**; **TCP × UDP**
(entrega ordenada e garantida); **RFC 1918 e NAT**; **IPv6** (abreviação do
endereço); **cálculo de sub-rede** a partir de um /24; **MPLS**; meio físico,
topologia e Wi-Fi; **SSH substituindo o Telnet** — **ALERO 2026**. **Internet
× intranet × extranet × portal** e **X.800** (mecanismos de segurança do
modelo OSI) — **Dataprev 2024**.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): **número de porta específico** (80/443, DNS 53, DHCP) — veja a
observação da seção 4, a FGV preferiu raciocínio de rota, camada e ACL; o
**handshake híbrido do TLS**; **firewall stateful × stateless**; e **VLAN**
como segmentação de domínio de broadcast.

Rode `../quiz.py redes`.

## Estratégia

Não vale estudar redes com a profundidade dos Perfis 2/5. Cubra: **OSI/TCP-IP,
equipamentos por camada, TCP×UDP, portas comuns, IP público×privado, IDS×IPS**.
Isso resolve o padrão histórico da FGV para o perfil de desenvolvimento com
pouco tempo investido. Ver `../dicas/redes.md`.
