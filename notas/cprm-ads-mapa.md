# Mapa de questões — CPRM 2025 (Analista em Geociências – ADS, tipo 1)

Fonte: prova FGV, Serviço Geológico do Brasil (CPRM), Edital 01/2025, cargo
Analista em Geociências – Análise e Desenvolvimento de Sistemas (manhã), 70
questões, aplicada em **30/11/2025**. Caderno original
`analista-em-geociencias-analise-e-desenvolvimento-de-sistemas-cns02e02-tipo-1.pdf`.
Gabarito **definitivo** (publicado em 08/01/2026):
`gabaritos/gabarito-definitivo-cprm.pdf`, primeira tabela do bloco "Análise e
Desenvolvimento de Sistemas – **1** – Turno Manhã".

> A data de aplicação corrigida é **30/11/2025** — é o que diz o cabeçalho de
> todas as páginas do gabarito definitivo ("prova aplicada no dia 30/11/2025").
> O `CONTINUAR-AQUI.md` §2 registrava 02/12/2025, que era a data do
> comunicado, não a da prova.

**Por que esta prova entrou:** é o alvo descrito na pendência 2 — **cargo de
TI** com bloco de **atualidades** no Módulo I, que é o segundo bloco mais
escasso do banco. As dez questões de atualidades caem exatamente onde faltava
(ética da IA pela UNESCO, ODS/Agenda 2030, geopolítica de minerais
estratégicos). Os 40 específicos são de Análise e Desenvolvimento de Sistemas,
o mesmo perfil da Dataprev.

**Recorte: o caderno inteiro.** Diferente da NAV Brasil, aqui não há nada a
descartar — não existe bloco de "Informática" nem de legislação genérica
(direito constitucional/administrativo). A única questão de lei do caderno é a
Q38, sobre **anonimização na LGPD**, que é conteúdo do edital da Dataprev.

## Conhecimentos Gerais (1–30)

| Bloco oficial | Questões |
|---|---|
| Língua Portuguesa | 1–10 |
| Raciocínio Lógico Matemático | 11–20 |
| Atualidades | 21–30 |

Todas as dez de português se apoiam em um mesmo texto ("O Brasil na crise do
clima", de Dimas Ramalho), impresso uma única vez antes da Q1. Como o quiz
sorteia item solto, cada enunciado precisa se sustentar sozinho — e aqui isso
acontece naturalmente, porque a FGV recolocou o trecho analisado dentro de cada
comando ("No trecho '...', assinale..."). Só a Q1 e a Q6 falam do texto como um
todo (estratégia argumentativa do 1º parágrafo; função de linguagem
predominante).

## Conhecimentos Específicos (31–70)

| Q | Tema | Sub-bloco (minha leitura) |
|---|---|---|
| 31 | Munging — ofuscar endereço de e-mail contra coletor automático | seguranca |
| 32 | Retrocesso binário exponencial no CSMA/CD | redes |
| 33 | Camadas do TCP/IP × protocolo de cada uma | redes |
| 34 | Nível de RAID que não usa striping | orfaos |
| 35 | Backup — cópia física × cópia lógica | orfaos |
| 36 | AES — estágios, chave expandida e simetria da decriptografia | seguranca |
| 37 | Data warehouse — característica que não é típica | bi |
| 38 | LGPD — conceito de dado anonimizado | legislacao |
| 39 | Governança de dados — papel dos criadores de dados | governanca |
| 40 | DDoS — PoD, Slowloris, Smurf, Teardrop e UDP storm | seguranca |
| 41 | Spear phishing × MitM, replay e session hijacking | seguranca |
| 42 | Big Data — qual "V" não existe | bi |
| 43 | Modelagem multidimensional — esquema galáxia (fatos que dividem dimensões) | bi |
| 44 | Dashboards de BI e operações OLAP (drill-down, roll-up) | bi |
| 45 | Teste de Turing Total × Teste de Turing original | atualidades |
| 46 | Complexidade de caso médio O(n log n) — merge sort | programacao |
| 47 | Restrição de integridade implícita do modelo relacional | banco-dados |
| 48 | Atributo que integra superchave mínima (atributo principal) | banco-dados |
| 49 | Tuning de consulta — prática que piora o desempenho | banco-dados |
| 50 | DDL de duas tabelas + consulta SQL — grau, chave e junção | banco-dados |
| 51 | Sistemas operacionais — UNIX, Windows, Linux e Android | orfaos |
| 52 | O que é uma aplicação Web | arquitetura |
| 53 | Servidores de aplicação — Tomcat, WildFly, GlassFish, WebSphere | java |
| 54 | JEE — Servlets, ciclo de vida do JSP e papel no MVC | java |
| 55 | WCAG — os quatro princípios da acessibilidade | frontend |
| 56 | SOA — WSDL, UDDI, SOAP e acoplamento fraco | arquitetura |
| 57 | JDBC — tipos de driver, MVC e Class.forName | java |
| 58 | Caso de uso formal — o que é a precondição | eng-software |
| 59 | Oracle Spatial — modelar ilhas e boias (geometria heterogênea) | banco-dados |
| 60 | ISO 27001 — as dez cláusulas do sistema de gestão | seguranca |
| 61 | Definição de malware — worm, spyware, trojan, backdoor, rabbit | seguranca |
| 62 | Manifesto Ágil — o valor que não está lá | eng-software |
| 63 | Modelagem de requisitos — modelo orientado a fluxos | eng-software |
| 64 | Arquitetura limpa (Robert C. Martin) e testabilidade | arquitetura |
| 65 | Padrões GoF — Singleton, Factory Method, Strategy, Observer, Decorator | eng-software |
| 66 | Quais estilos são arquitetura em camadas | arquitetura |
| 67 | Microsserviços — em que camada mora a descoberta de serviços | arquitetura |
| 68 | Arquitetura de aplicação web — níveis físicos × divisões lógicas | arquitetura |
| 69 | ITIL SVS — cadeia de valor de serviço | governanca |
| 70 | PMBOK 6ª ed. — definição de projeto e partes interessadas | governanca |

**Notas de classificação:**

- **34 e 35 vão para `orfaos`** pelo mesmo critério já aplicado à `nav-tec` Q65
  (RAID 0): RAID, backup físico/lógico e sistemas operacionais são arquitetura
  de **computadores**, não a "arquitetura de software" do Perfil 3. O
  `importar_provas.py` já resolve isso sozinho quando o rótulo é "arquitetura
  de computadores", mas aqui o rótulo é explícito no mapa.
- **45 (Teste de Turing Total) é `atualidades`**, não `orfaos`: o Módulo I do
  Perfil 3 cobre fundamentos de IA, e o microtópico `fundamentos-ia` vive nesse
  bloco. Classificação por conteúdo, não pelo rótulo "Conhecimentos
  Específicos" do caderno — a mesma regra que trouxe a `nav-tec` Q33.
- **50 depende de figura:** o `CREATE TABLE` das duas tabelas e a consulta SQL
  saíram do PDF como imagem. Fica fora do sorteio.
- **17 também depende de figura**, e escapou da heurística: o enunciado diz "A
  Figura **mostra** como 17 caixas cúbicas foram organizadas", e a lista de
  dêixis do importador só previa o particípio ("mostrada"). Saiu do sorteio em
  07/08/2026 por exceção declarada no `importar_provas.py`
  (`DEPENDE_DE_FIGURA_MANUAL`) — a explicação continua gravada, com o caminho
  que a questão pede: contar as 12 caixas visíveis e subtrair de 17.
- **59** é de banco de dados geoespacial (Oracle Spatial), fora do edital da
  Dataprev — entra em `banco-dados` porque o mecanismo cobrado (modelar uma
  coleção heterogênea de geometrias) é de modelagem, mas não gere questão nova
  a partir dela.
