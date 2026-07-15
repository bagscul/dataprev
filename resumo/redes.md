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

## 6. Segurança de rede (interface com Segurança da Informação)

- **Firewall** (filtra tráfego), **proxy**, **VPN** (IPsec, SSL VPN).
- **IDS** (detecta/alerta) × **IPS** (bloqueia). Ver `seguranca.md`.
- **NAT** traduz endereços; **VLAN** segmenta a camada 2.

## O que já caiu (nossas questões)

Camada OSI de sessão (checkpoints); switch × roteador × hub; TCP × UDP;
portas; RFC 1918; IPv6 128 bits; roteamento estático × OSPF (distância
administrativa); ACL Cisco (wildcard mask). Rode `../quiz.py redes`.

## Estratégia

Não vale estudar redes com a profundidade dos Perfis 2/5. Cubra: **OSI/TCP-IP,
equipamentos por camada, TCP×UDP, portas comuns, IP público×privado, IDS×IPS**.
Isso resolve o padrão histórico da FGV para o perfil de desenvolvimento com
pouco tempo investido. Ver `../dicas/redes.md`.
