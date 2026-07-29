# Roteiro de Estudos — Concurso Dataprev 2026 (v3.1)

**Cargo:** Analista de Tecnologia da Informação — Perfil 3: Desenvolvimento de Software
**Localidade:** Natal/RN (20 vagas imediatas, 13 de ampla concorrência)
**Prova:** domingo, 11 de outubro de 2026, das 13h às 17h
**Início dos estudos:** segunda-feira, 27 de julho de 2026 — **é hoje, dia 1 de 77**
**Janela:** 11 semanas exatas (77 dias)
**Atualizado em:** 29/07/2026 (correção pontual na seção 1, ver nota abaixo)

> **29/07 — seção 1 corrigida.** A tabela de distribuição da Dataprev 2024 e as
> duas primeiras conclusões foram reclassificadas questão a questão direto no
> PDF: a versão anterior usava categorias que nem existem como tag no quiz e
> não fechava as 30 questões do bloco específico. O plano de dias (seções 4+)
> não muda.
>
> **v3.1 — o plano de dias não mudou.** As 11 semanas abaixo continuam idênticas
> e batem uma a uma com o `progresso.csv` (é dele que o `./quiz.py --hoje` e o
> `./status.py` leem). O que esta revisão acrescenta é a **seção 3**: o material
> de apoio ficou pronto depois que a v3 foi escrita (apostila de 150 páginas,
> 403 questões originais auditadas, 422 de sete provas reais da FGV) e o roteiro
> ainda não dizia onde cada coisa fica nem quando usar cada uma.
>
> **v3 — replanejado para começar em 27/07.** A v2 partia de 13/07 e tinha 13
> semanas. Esta versão tem 11. **Nada de conteúdo foi cortado**: o que encolheu
> foi a folga de revisita e a semana de consolidação, que estava com seis dias
> só de revisão. A fundação (requisitos, modelagem, SQL, SOLID, ágil) continua
> inteira, e ficou mais densa — as duas primeiras semanas agora carregam o que
> antes se espalhava por quatro.

---

## 1. O que a análise das provas revelou

Não existem provas antigas úteis da Dataprev. As de 2011 e 2012 foram do Instituto Quadrix, banca diferente, tecnologia defasada. A única prova FGV para Dataprev é a de novembro de 2024. Uma amostra só é frágil, então o roteiro se apoia também no comportamento da FGV em provas recentes de TI de outros órgãos.

**Distribuição real do Módulo II na Dataprev 2024 (30 questões, reclassificadas
questão a questão direto no PDF em 29/07/2026 — a versão anterior desta tabela
tinha categorias que nem existem no quiz e não fechava as 30 questões):**

| Bloco | Questões | Pontos |
|---|---|---|
| Engenharia de Software | 9 | 22,5 |
| Banco de Dados / BI | 6 | 15 |
| Programação | 6 | 15 |
| Arquitetura de Software | 4 | 10 |
| Segurança da Informação | 3 | 7,5 |
| Redes de Computadores | 2 | 5 |

**Comportamento da FGV em outras provas de TI:**

| Prova | Data | Blocos dominantes |
|---|---|---|
| MPU, Desenv. de Sistemas | mai/2025 | Português 15, **Banco de Dados 12**, Eng. Software 8 |
| AgSUS, Analista de TI | out/2025 | Português 12, Informática 8, RL 7 |
| TJ-RJ, Analista de Sistemas | jan/2026 | Português 19, Eng. Software 7, **Banco de Dados 7** |

### As cinco conclusões que moldam este roteiro

**1. Engenharia de Software, Banco de Dados/BI e Programação dividem o topo.** Na Dataprev 2024 vieram quase empatados (9, 6 e 6 questões). No MPU o BD disparou na frente de Engenharia de Software. Tratar os três como prioridade, sem eleger vencedor único — e sem esquecer Arquitetura de Software (4 questões, tão relevante quanto Segurança).

**2. Redes de Computadores não é tão "fora do edital" quanto parece.** Das 2 questões de 2024, só a de X.800/arquitetura de segurança OSI foge de fato do edital do perfil. A outra (ambientes de Internet, intranet, extranet e portal) é o item 4 do próprio edital de Desenvolvimento de Sistemas — só não tem uma disciplina "Redes" com nome próprio. Ainda vale treinar OSI/X.800 à parte: é o ponto realmente cego.

**3. Raciocínio Lógico da FGV é matemática, não lógica formal.** O que caiu foi aritmética, álgebra, estatística, análise combinatória e geometria plana. Só uma questão de proposições. O edital diz literalmente "problemas aritméticos, geométricos e matriciais". Estudar tabela-verdade e parar por aí é um erro.

**4. Inglês vale 12 questões, o mesmo que Português.** Interpretação de texto foi o assunto mais cobrado da prova inteira, nas duas línguas. Para quem lê documentação técnica em inglês, é a disciplina de melhor retorno por hora estudada de toda a prova.

**5. A nota de corte real vai ser alta.** Desenvolvimento de Software teve 6.257 inscritos em 2024, o perfil mais concorrido de 23.423 candidatos. Os 57,5 pontos mínimos do edital são piso de eliminação, não meta. A meta é pontuar alto.

---

## 2. Princípios operacionais

**Questões todos os dias, sem exceção.** Resolver questão não é revisão, é o método de estudo em si. Teoria pura entra apenas quando a taxa de erro num tópico está alta demais para aprender pelos comentários.

**Dois assuntos por dia: um específico e um geral.** Segunda é Português, terça é Inglês, quarta é RLM, quinta é Legislação, sexta é Atualidades. O `./quiz.py --hoje` cobre os dois automaticamente.

**Cada bloco é revisitado.** Nas semanas temáticas (Java, Redes, Segurança, BI, Frontend, Governança) o bloco domina os cinco dias — é assim que se ganha profundidade em bloco novo. O reencontro com o que já passou vem por três vias: as **revisitas** marcadas no plano, os **simulados de domingo** (que sorteiam de tudo) e o `--erradas`, que é repetição espaçada de verdade.

**Filtro de banca travado em FGV.** Cada banca tem uma gramática própria de pegadinha. Treinar com CESPE constrói reflexos que não servem aqui.

**Caderno de erros.** Anotação curta e contínua do que errou e por quê. Na última semana, ele vira o único material de revisão.

**Volume:** comece com 30 a 40 questões/dia e suba conforme o pique. Não persiga número, persiga a digestão dos comentários. Uma hora com 10 questões bem entendidas vale mais que uma hora com 50 chutadas.

**Domingo é dia de simulado cronometrado.** Sempre. 70 questões, 4 horas, sem consulta. São 11 no total — dez aos domingos e o último na quarta da semana da prova.

---

## 3. O material: quatro camadas e um comando por dia

Todo o material do repositório está organizado em quatro camadas, da mais
lenta para a mais rápida. **Elas contam a mesma história** — um fato corrigido
numa tem de descer para as outras, e o `./valida.py` acusa quando não desce.

| Camada | Onde | Para quê | Quando usar |
|---|---|---|---|
| **Apostila** | `apostila/main.pdf` (150 páginas, 21 capítulos) | teoria explicada, com exemplos e caixas de pegadinha | quando erra por **não saber o conceito** |
| **Resumo** | `resumo/<bloco>.md` | o mesmo conteúdo condensado, para reler rápido | revisão de sábado, véspera de simulado |
| **Dicas de banca** | `dicas/<bloco>.md` | como a **FGV** cobra aquele bloco e arma a pegadinha | antes de atacar um bloco novo |
| **Banco de questões** | `banco.json` + `banco-provas.json` | 403 originais auditadas + 422 de sete provas reais | todo dia, é o método de estudo |

As sete provas reais são Dataprev 2024 (70), MPU (70), TJ-RJ 1 e 2 (69 e 70),
CNSAL ADS (63), CNSAL BD (40) e CNSAL Redes (40) — todas FGV. Somando as duas
fontes, são **815 questões sorteáveis** pelo quiz, com gabarito auditado e
explicação de cada alternativa gravada: roda offline, sem custo.

**A rotina de um dia comum**, na ordem:

```bash
./status.py                      # o que é hoje e como está a aderência
./quiz.py --dica <bloco>         # 2 min: como a FGV cobra isso
./quiz.py --hoje                 # o específico + o geral do dia
./quiz.py --erradas              # fecha o dia com repetição espaçada
```

O `--resumo <bloco>` e o `--apostila <bloco>` entram **só quando a taxa de erro
do bloco está alta** — teoria é remédio, não rotina. `./feito.sh 45 34` registra
o que você resolveu fora do quiz (plataforma, PDF); as questões do próprio quiz
já entram sozinhas.

**Atrasou um dia?** `./quiz.py --dia ontem` roda o plano daquele dia e credita
nele, sem sujar o de hoje. `./quiz.py --pendentes` lista o que ficou aberto.
Atraso não se recupera dobrando o dia seguinte — se acumular mais de três dias,
sacrifique as revisitas, nunca os simulados de domingo.

**Caderno de erros:** `erros/<bloco>.md`. O quiz grava sozinho quando você erra,
mas o que vem de fora (prova em PDF, questão de plataforma) tem de entrar na
mão, no mesmo formato. Na semana 11 esse arquivo é o único material que sobra.

---

## 4. Bloco 1 — Fundação (Semanas 1 a 3 | 27/07 a 16/08)

As três semanas que sustentam o resto. Eng. de Software e Banco de Dados valem, juntos, mais de um terço do Módulo II — e Programação/Arquitetura entram já apoiados neles.

### Semana 1 — 27/07 a 02/08 · Eng. de Software + Banco de Dados

| Dia | Conteúdo |
|---|---|
| Seg 27/07 | **Eng. de Software:** ciclo de vida, processos de software, modelos de desenvolvimento. **Português:** interpretação de texto |
| Ter 28/07 | **Eng. de Software:** engenharia de requisitos (classificação, processo, elicitação, validação). **Inglês:** reading comprehension (diagnóstico do seu nível) |
| Qua 29/07 | **Banco de Dados:** modelo conceitual, lógico e físico; entidade-relacionamento. **RLM:** aritmética e problemas |
| Qui 30/07 | **Banco de Dados:** normalização (1FN a 3FN), integridade referencial. **Legislação:** LGPD, capítulos I e II (texto seco da lei) |
| Sex 31/07 | **Eng. de Software:** metodologias ágeis — Scrum, Kanban, XP, Lean. **Atualidades e IA:** conceitos de IA, aprendizado de máquina |
| Sáb 01/08 | Revisão do caderno de erros da semana + questões mistas |
| **Dom 02/08** | **Simulado 1** (70 questões, cronometrado) + correção comentada |

### Semana 2 — 03/08 a 09/08 · SQL e Programação

| Dia | Conteúdo |
|---|---|
| Seg 03/08 | **Banco de Dados:** SQL — DDL, DML, joins, subconsultas. **Português:** sintaxe (período composto, orações) |
| Ter 04/08 | **Banco de Dados:** SQL avançado, agregações, views, controle da transação. **Inglês:** verbos e tempos verbais |
| Qua 05/08 | **Programação:** orientação a objetos (classes, herança, polimorfismo, encapsulamento). **RLM:** álgebra e proporções |
| Qui 06/08 | **Programação:** SOLID. **Legislação:** LGPD, capítulos III e IV |
| Sex 07/08 | **Eng. de Software:** testes — unitários, integração, TDD, BDD. **Atualidades:** modelos generativos e modelos de linguagem |
| Sáb 08/08 | Revisão + refazer questões erradas da semana 1 |
| **Dom 09/08** | **Simulado 2** + correção |

### Semana 3 — 10/08 a 16/08 · Padrões e Arquitetura

| Dia | Conteúdo |
|---|---|
| Seg 10/08 | **Programação:** padrões de projeto (criacionais, estruturais, comportamentais). **Português:** morfologia e classes de palavras |
| Ter 11/08 | **Programação:** GRASP, clean code, análise estática, SonarQube. **Inglês:** pronomes e conectivos |
| Qua 12/08 | **Arquitetura:** monolítica × microsserviços, arquitetura em camadas, SOA. **RLM:** análise combinatória |
| Qui 13/08 | **Arquitetura:** hexagonal, API gateway, containers, REST × SOAP. **Legislação:** Marco Civil da Internet |
| Sex 14/08 | **Programação:** JSON, XML, XSLT, REST, Web Services, Swagger, mensageria. **Atualidades:** ética, governança e privacidade em IA |
| Sáb 15/08 | Revisão + caderno de erros acumulado |
| **Dom 16/08** | **Simulado 3** + correção |

---

## 5. Bloco 2 — Carga máxima (Semanas 4 a 9 | 17/08 a 27/09)

### Semana 4 — 17/08 a 23/08 · Java

Seu maior gargalo, vindo de Python e Node. O objetivo não é virar dev Java, é reconhecer sintaxe, anotações e a responsabilidade de cada peça do ecossistema numa questão de múltipla escolha.

| Dia | Conteúdo |
|---|---|
| Seg 17/08 | **Java:** sintaxe, tipos, coleções, tratamento de exceções. **Português:** pontuação e crase |
| Ter 18/08 | **Java EE / Jakarta EE:** EJB, servlets, container web. **Inglês:** substantivos e compostos |
| Qua 19/08 | **JPA e Hibernate:** ORM, mapeamento, ciclo de vida da entidade. **RLM:** estatística básica |
| Qui 20/08 | **Spring:** Spring Boot, injeção de dependência, anotações. **Legislação:** LAI (Lei 12.527 e decretos) |
| Sex 21/08 | **Spring Cloud, JUnit, JSF, Primefaces.** **Atualidades:** IA aplicada a negócios e políticas públicas |
| Sáb 22/08 | Revisão pesada de Java + caderno de erros |
| **Dom 23/08** | **Simulado 4** + correção |

### Semana 5 — 24/08 a 30/08 · Redes e protocolos

O bloco que o edital do perfil 3 mal menciona e que caiu com 3 questões em 2024.

| Dia | Conteúdo |
|---|---|
| Seg 24/08 | **Redes:** modelo OSI, camadas, encapsulamento. **Português:** concordância verbal e nominal |
| Ter 25/08 | **Redes:** TCP/IP, protocolos de aplicação (HTTP, DNS, SMTP, FTP, SSH). **Inglês:** vocabulário técnico em contexto |
| Qua 26/08 | **Protocolos seguros:** HTTPS, SSL/TLS, handshake, certificados. **RLM:** matrizes e problemas matriciais |
| Qui 27/08 | **Segurança:** criptografia simétrica e assimétrica, hash, assinatura digital. **Legislação:** Lei de Delitos Informáticos (12.737) |
| Sex 28/08 | **Segurança de redes:** firewall, VPN, segurança na internet. **Atualidades:** viés socioambiental |
| Sáb 29/08 | Revisão + refazer erradas de Java |
| **Dom 30/08** | **Simulado 5** + correção |

### Semana 6 — 31/08 a 06/09 · Segurança da informação

| Dia | Conteúdo |
|---|---|
| Seg 31/08 | **Segurança:** políticas, CID (confidencialidade, integridade, disponibilidade), ISO 27001:2022. **Português:** regência verbal e nominal |
| Ter 01/09 | **Segurança:** ISO 27002:2022, gerência de riscos (ameaça, vulnerabilidade, impacto). **Inglês:** voz passiva e modais |
| Qua 02/09 | **Segurança:** controle de acesso, OAuth2, SSO. **RLM:** geometria plana |
| Qui 03/09 | **Segurança:** OWASP Top 10 (**2025 vigente e 2021**), SDL, SAST e DAST. **Legislação:** revisita LGPD + a ANPD como agência (Lei 15.352/2026) |
| Sex 04/09 | **Eng. de Software:** revisita testes + DevOps, DevSecOps, Git. **Atualidades:** tipos de aprendizado e métricas de avaliação |
| Sáb 05/09 | Revisão + caderno de erros |
| **Dom 06/09** | **Simulado 6** + correção |

### Semana 7 — 07/09 a 13/09 · Business Intelligence

| Dia | Conteúdo |
|---|---|
| Seg 07/09 | **BI:** conceitos, fundamentos, arquitetura de BI, sistemas de suporte à decisão. **Português:** coesão, coerência e conectivos |
| Ter 08/09 | **BI:** data warehouse, modelagem dimensional, star e snowflake. **Inglês:** inferência e ideia principal |
| Qua 09/09 | **BI:** ETL e ELT, OLAP e suas operações, cubos. **RLM:** probabilidade |
| Qui 10/09 | **BI:** data mining, data lake, big data, CRISP-DM. **Legislação:** revisita Marco Civil e LAI |
| Sex 11/09 | **Banco de Dados:** revisita completa (é eixo duplo, precisa de rodadas frequentes). **Atualidades:** interseção IA e ESG |
| Sáb 12/09 | Revisão + refazer erradas de Segurança |
| **Dom 13/09** | **Simulado 7** + correção |

### Semana 8 — 14/09 a 20/09 · Frontend, mobile e web

Bloco que em 2024 caiu dentro de "Programação", com 4 questões. Não é periférico.

| Dia | Conteúdo |
|---|---|
| Seg 14/09 | **Frontend:** HTML, CSS, box model, Flexbox e Grid, Ajax. **Português:** semântica, sinonímia e ambiguidade |
| Ter 15/09 | **Frontend:** React, Angular, VueJS, SPA e PWA. **Inglês:** false friends e phrasal verbs |
| Qua 16/09 | **Mobile:** Android e iOS, low-code e no-code. **RLM:** revisita aritmética e álgebra |
| Qui 17/09 | **UX:** acessibilidade (WCAG), usabilidade, arquitetura da informação, CMS, portais, workflow. **Legislação:** revisão geral |
| Sex 18/09 | **Eng. de Software:** revisita (requisitos + metodologias ágeis). **Atualidades** |
| Sáb 19/09 | Revisão + caderno de erros |
| **Dom 20/09** | **Simulado 8** + correção |

### Semana 9 — 21/09 a 27/09 · Governança e métricas

| Dia | Conteúdo |
|---|---|
| Seg 21/09 | **Governança:** gerenciamento de projetos — PMBOK **6ª e 7ª edições**, tradicional, híbrido e ágil. **Português:** ortografia e acentuação |
| Ter 22/09 | **Governança:** ITIL 4 — SVS, cadeia de valor, 7 princípios, as 34 práticas. **Inglês:** referência pronominal e coesão |
| Qua 23/09 | **Governança:** COBIT 2019, gestão de riscos. **RLM:** simulado só de RLM |
| Qui 24/09 | **BPMN** e modelagem de processos + **Métricas:** Ponto de Função, Story Points. **Legislação:** revisão geral |
| Sex 25/09 | **Arquitetura (revisita):** nuvem, containers, mensageria, transações distribuídas. **Atualidades** |
| Sáb 26/09 | Revisão + refazer erradas de Java e Redes |
| **Dom 27/09** | **Simulado 9** + correção |

---

## 6. Bloco 3 — Varredura e reta final (Semanas 10 a 11 | 28/09 a 11/10)

### Semana 10 — 28/09 a 04/10 · Os órfãos do edital + consolidação

Os itens que ninguém estuda e que a FGV cobra. Foi assim que Blockchain pegou o pessoal em 2024. Na Dataprev 2024 esse bloco valeu **10 pontos** (Noções de Informática 2, Arq. de Computadores 1, Sistemas de Informação 1).

| Dia | Conteúdo |
|---|---|
| Seg 28/09 | **Blockchain. Transações distribuídas. RPA.** **Português:** revisão de interpretação e sintaxe |
| Ter 29/09 | **Arquitetura de computadores** (UC × ULA, ciclo de instrução, pipeline, hierarquia de memória) e **sistemas de informação** (SPT, SIG, SAD, ERP, CRM, SCM). **Inglês:** revisão de leitura técnica |
| Qua 30/09 | **Ambientes** internet, extranet, intranet e portal. **Servidores** web × aplicação. **Padrões de reuso, UDDI, design de software.** IA/ML aplicado. **RLM:** lógica proposicional e sequências |
| Qui 01/10 | Revisão dos 3 tópicos com pior taxa de acerto histórica (`./quiz.py --stats` aponta) |
| Sex 02/10 | **Eixo duplo:** revisão intensiva de Eng. de Software e Banco de Dados |
| Sáb 03/10 | Varredura final: reler o Anexo I do edital item por item + caderno de erros integral |
| **Dom 04/10** | **Simulado 10** + correção |

### Semana 11 — 05/10 a 11/10 · Reta final

| Dia | Conteúdo |
|---|---|
| Seg 05/10 | Revisão leve: Segurança, Redes e Arquitetura |
| Ter 06/10 | Revisão leve: as quatro leis no texto seco (LGPD, LAI, Marco Civil, delitos informáticos) e Inglês (leitura de textos técnicos) |
| **Qua 07/10** | **Simulado 11** — o último. Depois disso, nada de simulado |
| Qui 08/10 | Caderno de erros. **Atualidades e IA:** notícias das últimas semanas (essa disciplina recompensa quem está atualizado, não quem estudou em julho) |
| Sex 09/10 | Lives de revisão de véspera (Estratégia e Gran costumam fazer, e valem questão "de graça"). **Parar de estudar conteúdo novo** |
| Sáb 10/10 | Descanso. Separar documentos e material. Dormir cedo |
| **Dom 11/10** | **PROVA — 13h às 17h. Portões fecham 12h30** |

---

## 7. Checklist do dia da prova

- Chegar com 1h30 de antecedência. **Portões fecham às 12h30, sem exceção**
- Documento de identidade original com foto. CPF e certidão de nascimento **não** são aceitos
- Comprovante de inscrição ou de pagamento
- Caneta esferográfica de tinta azul ou preta, **de material transparente** (itens 9.10 e 10.1 — é o corpo da caneta que tem de ser transparente, não a tinta). Leve uma reserva, também transparente
- **Proibido, sob pena de eliminação** (item 10.13): relógio de qualquer espécie, celular e eletrônicos, **lápis, lapiseira (grafite), corretor líquido e/ou borracha**, boné/chapéu/gorro, óculos escuros
- Lanche e bebida só em embalagem transparente e sem rótulo
- Permanência mínima obrigatória: **2 horas**
- Caderno de questões só pode ser levado se você sair nos **últimos 30 minutos**
- Haverá detector de metais na entrada da sala e dos sanitários

---

## 8. Pendências administrativas

> **Inscrição feita.** ✔

| Item | Prazo |
|---|---|
| **Confirmar o requisito de formação com a FGV** | **esta semana (até 31/07)** |
| Colação de grau | dezembro/2026 |
| Certidão de conclusão (UERN) | logo após colar grau |
| Solicitação do diploma registrado | quanto antes após a colação |

**Confirmar com a FGV** (concursodataprev26@fgv.br ou 0800 591 3078) se o
diploma de Ciência da Computação é aceito como "graduação em Tecnologia da
Informação" sem exigir pós-graduação de 360h. O edital não explicita isso, e é
a única incerteza real de requisito no seu caso. É a **única pendência com
risco de eliminar**, então não vale deixar rolando: manda o e-mail na primeira
semana e guarda a resposta por escrito — resposta de telefone não serve de
prova em recurso. Se a FGV responder que exige a pós, ainda dá tempo de
planejar; em setembro, não.
