# Mapa de questões — EPE 2024 (Analista de Gestão Corporativa – TI / Soluções, tipo 1)

Fonte: prova FGV, Empresa de Pesquisa Energética (EPE), Edital 02/2024, cargo
Analista de Gestão Corporativa — Tecnologia da Informação, **Perfil 2:
Soluções** (tarde), 80 questões, aplicada em **01/09/2024**. Caderno original
`agc-ti-solucoescns006-tipo-1.pdf`. Gabarito **definitivo** (01/10/2024):
`gabaritos/gabarito-definitivo-epe.pdf`, tabela "Analista de Gestão Corporativa
- Tecnologia da Informação - **Perfil 2: Soluções** - TIPO 1".

> A data que vale é a do gabarito: **01/09/2024**. A página do concurso na FGV
> exibe 03/09/2024, que é a data de divulgação do caderno.

**Por que esta prova entrou:** é a prova de TI mais alinhada ao Perfil 3 da
Dataprev que ainda tinha inglês no Módulo I — cargo de tecnologia, nível
superior, 2024. O inglês (10 questões) ataca o único déficit que restava; os 42
específicos aproveitados são quase um espelho do edital da Dataprev
(desenvolvimento ágil, DevOps, nuvem, banco de dados, segurança, Python,
JavaScript, HTML5, testes, Power BI).

## Recorte

| Bloco oficial | Questões | destino |
|---|---|---|
| Língua Portuguesa | 1–10 | **descartar** (sem déficit; Q1 depende de charge) |
| Língua Inglesa | 11–20 | **importar** |
| Noções de Administração Pública | 21–28 | **descartar** (fora do edital) |
| Valor Público Gerado pela EPE | 29–35 | **descartar** (institucional da EPE) |
| Conhecimentos Específicos | 36–80 | **importar**, menos 37, 38, 39 e 75 |

Descartes dentro dos específicos: **Q37** (Decreto 6.021/2007, CGPAR — é
governança de estatal, fora do edital), **Q38** (Microsoft 365) e **Q39**
(Excel), que são Informática de escritório — bloco que o Perfil 3 não tem.
**Q75 (árvore binária de busca) foi ANULADA** pela banca e por isso fica de
fora; as outras duas anuladas do caderno, Q3 e Q9, são de português e já
estavam descartadas.

## Conhecimentos Específicos (36–80)

| Q | Tema | Sub-bloco (minha leitura) |
|---|---|---|
| 36 | Objetivos do processamento distribuído | arquitetura |
| 40 | Diagrama entidade-relacionamento | banco-dados |
| 41 | Protocolos da camada de aplicação | redes |
| 42 | eXtreme Programming (XP) | eng-software |
| 43 | Metodologias de desenvolvimento — paradigmas | eng-software |
| 44 | DevOps: colaboração entre desenvolvimento e operações | eng-software |
| 45 | BDD — Desenvolvimento Orientado por Comportamento | eng-software |
| 46 | Relação PRODUCAO — dependências e chaves | banco-dados |
| 47 | Propriedades ACID | banco-dados |
| 48 | SQL ANSI e seus subconjuntos (DDL, DML, DCL) | banco-dados |
| 49 | Sincronização entre data warehouse e fontes (ETL) | bi |
| 50 | Arquiteturas de armazenamento e análise de dados | bi |
| 51 | Conceitos de DevOps (V/F) | eng-software |
| 52 | Plataforma de desenvolvimento como serviço | arquitetura |
| 53 | Desempenho em picos de acesso (escalabilidade) | arquitetura |
| 54 | Computação em nuvem — abstração do hardware | arquitetura |
| 55 | Desafios da computação em nuvem | arquitetura |
| 56 | Desenvolvimento seguro no ciclo de vida | seguranca |
| 57 | Escolha de algoritmo de criptografia | seguranca |
| 58 | Códigos maliciosos e malwares (V/F) | seguranca |
| 59 | Ataque em Internet Banking autenticado | seguranca |
| 60 | Assinatura digital e certificação digital | seguranca |
| 61 | Design thinking | eng-software |
| 62 | Histórias de usuário em projetos ágeis | eng-software |
| 63 | MVP × protótipo | eng-software |
| 64 | Comunicação entre componentes na nuvem (APIs) | arquitetura |
| 65 | Arquitetura MVC | arquitetura |
| 66 | Frameworks e boas práticas de arquitetura | arquitetura |
| 67 | Garbage collection mark-and-sweep | programacao |
| 68 | JavaScript — Set e coleções | frontend |
| 69 | Python 3.11 — dict comprehension | programacao |
| 70 | Python 3.11 — laço e lista | programacao |
| 71 | HTML5 — elemento de divisão em seções | frontend |
| 72 | Tecnologias para grande volume de dados | bi |
| 73 | Tipos de dado adquiridos em projeto (vídeo, foto, tabela) | bi |
| 74 | Power BI | bi |
| 76 | Estruturas de dados — listas ordenadas e não ordenadas | programacao |
| 77 | Code smells | eng-software |
| 78 | Teste de regressão | eng-software |
| 79 | Métricas de qualidade de software | eng-software |
| 80 | Testes de carga | eng-software |

**Notas de classificação:**

- **68 (JavaScript) vai para `frontend`**, e não para `programacao`: no
  repositório o JavaScript vive no bloco de frontend, junto de HTML/CSS e dos
  frameworks. Já **69 e 70 (Python)** e **67 (garbage collection)** são
  linguagem/execução genéricas e ficam em `programacao`.
- **49, 50, 72, 73 e 74 vão para `bi`** — é o bloco mais magro do Módulo II
  (37 questões), e as cinco cobrem ETL, arquitetura analítica, big data e
  ferramenta de visualização.
- **36, 52, 53, 54, 55, 64, 65 e 66 vão para `arquitetura`**: nuvem,
  escalabilidade, integração por API e padrões arquiteturais são o recorte de
  "arquitetura de software" do edital, não o de arquitetura de computadores.
