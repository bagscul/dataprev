# redes — como a FGV cobra

## O que mais cai
- Modelo OSI por FUNÇÃO, não por número: cenário descreve o
  comportamento e pede a camada. Ex.: checkpoints no fluxo +
  controle de diálogo (simplex/half/full-duplex) = camada de
  Sessão.
- TCP: three-way handshake — o que ele faz de fato
  (sincronizar números de sequência). TCP x UDP.
- Roteamento IPv4: rota estática x OSPF, distância
  administrativa, escolha de rota. Aparece com tabela de
  rotas real (Cisco IOS).
- ACL Cisco e máscara curinga (wildcard mask) — cálculo de
  bits para casar hosts específicos (ex.: último octeto
  ímpar).
- Tipos de rede: Internet x intranet x extranet x portal
  (nível de acesso e público-alvo).
- SSL x TLS x HTTPS (fronteira com segurança).
- X.800 — mecanismos de segurança OSI (fronteira com
  segurança).
- Observação: número de porta específico NÃO apareceu na
  amostra; a FGV preferiu raciocínio de rota, camada e ACL.
  Está no edital, mas priorize os padrões acima.

## Como a banca arma a pegadinha
- Absolutos em roteamento: "OSPF SEMPRE tem prioridade sobre
  rota estática", "roteador faz load balancing AUTOMÁTICO",
  "descarta por rotas conflitantes". A regra real é
  determinística: menor distância administrativa vence.
- Troca a camada OSI: oferece Transporte/Enlace/Apresentação
  quando a função descrita é de Sessão (diálogo, checkpoint).
- TCP handshake: distratores dizem que ele "autentica
  dispositivos", "negocia segurança" ou "controla fluxo" —
  não; ele SINCRONIZA números de sequência (SYN/SYN-ACK/ACK).
- Inverte intranet/extranet/Internet: chama intranet de
  "rede pública global", extranet de "só interna", Internet
  de "rede restrita".
- SSL "mais seguro/moderno que TLS" — invertido; TLS
  sucedeu e corrigiu o SSL.

## Como se sair melhor
- Decore a distância administrativa (Cisco): conectada 0,
  estática 1, OSPF 110, RIP 120. MENOR vence. Com duas rotas
  default, ganha a estática (1) sobre OSPF (110).
- OSI de cima pra baixo: Aplicação, Apresentação, Sessão,
  Transporte, Rede, Enlace, Física. Sessão = diálogo e
  sincronização (checkpoints); Transporte = fim-a-fim,
  portas, TCP/UDP; Rede = IP/roteamento; Enlace = MAC/quadro.
- Wildcard mask = inverso da máscara; bit 0 = "tem que
  bater", bit 1 = "ignora". Para casar só ímpares, o bit
  menos significativo do octeto precisa estar fixo em 1 →
  wildcard 0.0.0.254 (deixa livres os demais bits, fixa o
  último). Confira montando os bits, não de cor.
- TCP = confiável, orientado a conexão, handshake, sequência;
  UDP = sem conexão, rápido, sem garantia. Handshake existe
  só no TCP.
- Extranet = tecnologia da Internet com acesso CONTROLADO a
  parceiros externos autorizados (o meio-termo).
