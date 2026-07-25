# Mapa de questões — ALE-RO 2025/2026 (Analista Legislativo TI — ADS, tipo 1 branca)

Fonte: prova FGV, Assembleia Legislativa de Rondônia, Edital 01/2025, cargo
Analista Legislativo — Tecnologia da Informação — Análise e Desenvolvimento de
Sistemas (tarde), 80 questões. Blocos gerais são os rótulos oficiais do caderno.
Dentro de "Conhecimentos Específicos" a coluna sub-bloco é classificação minha
por conteúdo, não da FGV — use como guia de estudo, não como gabarito de
proporção.

## Conhecimentos Gerais

| Bloco oficial | Questões |
|---|---|
| Língua Portuguesa | 1–12 |
| Raciocínio Lógico-matemático | 13–24 |
| Legislação Específica | 25–32 |
| História e Geografia de Rondônia | 33–40 |

## Conhecimentos Específicos (41–80)

| Q | Tema | Sub-bloco (minha leitura) |
|---|---|---|
| 41 | Engenharia de requisitos — conflito de stakeholders, Viewpoint Analysis e negociação | eng-software |
| 42 | GORE, FURPS+, requisito de confidencialidade x desempenho (RNF) | eng-software |
| 43 | Prototipação descartável x evolutiva (refinar requisitos de interface) | eng-software |
| 44 | Análise de requisitos — resolver inconsistências/contradições | eng-software |
| 45 | Validação de requisitos — completude, consistência e compliance | eng-software |
| 46 | RUP — fase de Elaboração (linha de base da arquitetura, mitigar riscos) | eng-software |
| 47 | UML 2.5.1 — Diagrama de Sequência (ordem cronológica de mensagens) | eng-software |
| 48 | UML 2.5.1 — relacionamento Composição (existência dependente) | eng-software |
| 49 | Estrutura de dados — Tabela Hash, busca O(1) médio | programacao |
| 50 | Estrutura de dados — Lista Duplamente Encadeada, inserção/remoção O(1) | programacao |
| 51 | Formas Normais (2FN) e anomalia de atualização | banco-dados |
| 52 | Modelagem ANSI/SPARC — nível conceitual e Diagrama de Classes | banco-dados |
| 53 | Padrão de projeto GoF — Singleton (instância única) | eng-software |
| 54 | Web Services SOAP — WSDL (descrição de interface) | arquitetura |
| 55 | Hardware — CPU executa instruções e cálculos lógico/aritméticos | arquitetura de computadores |
| 56 | Arquitetura de Von Neumann — gargalo do barramento único | arquitetura de computadores |
| 57 | Organização do computador — impressora como dispositivo de Saída | arquitetura de computadores |
| 58 | Soma binária 8 bits sem sinal — overflow/carry | arquitetura de computadores |
| 59 | Complemento de dois — overflow aritmético | arquitetura de computadores |
| 60 | Conversão de base — octal para binário | arquitetura de computadores |
| 61 | Interpretação x compilação (execução linha a linha) | programacao |
| 62 | Procedimento (procedure) x função — bloco sem retorno | programacao |
| 63 | Passagem de parâmetro por referência (endereço de memória) | programacao |
| 64 | Memória ROM — firmware/boot não volátil | arquitetura de computadores |
| 65 | Notação IDEF1X — relacionamento identificador (linha sólida) | banco-dados |
| 66 | Integridade Referencial (chave estrangeira x primária) | banco-dados |
| 67 | SQL — INSERT INTO ... VALUES | banco-dados |
| 68 | CMMI/MPS.BR — nível 4 (medição quantitativa/controle estatístico) | eng-software |
| 69 | Métrica de tamanho — Ponto de Função (independente de linguagem) | eng-software |
| 70 | Tratamento de risco — Modificar o Risco (novos controles) | seguranca |
| 71 | ISO/IEC 27005 — risco residual (após WAF) | seguranca |
| 72 | Controle de acesso lógico — RBAC (baseado em papéis) | seguranca |
| 73 | Continuidade de negócio (PCN) — RTO e RPO | seguranca |
| 74 | Segregação de Funções (SoD) — mitigar conluio/fraude interna | seguranca |
| 75 | ISO/IEC 27002 — responsabilidade do Asset Owner | seguranca |
| 76 | Linux/systemd — systemctl disable (não iniciar no boot) | redes |
| 77 | UML — Diagrama de Objetos para validação/estado em testes | eng-software |
| 78 | Framework de arquitetura corporativa — Zachman (matriz 6x6) | arquitetura |
| 79 | Balanceamento de carga — afinidade de sessão (risco à tolerância a falhas) | arquitetura |
| 80 | Modelo Cascata — risco de late-feedback e custo de retrabalho | eng-software |

## Como usar

Pra revisar por bloco, filtre a tabela acima e abra as questões correspondentes
no PDF da prova (mesma numeração). Cole aqui no chat a que você errou (número +
gabarito, se tiver) que eu explico e já registro em `erros/<bloco>.md`.

Obs.: a Q76 (systemctl/Linux) não tem bloco de Sistemas Operacionais em
`erros/`; deixei em `redes` como bucket de infra/SO — troque pra `orfaos` se
preferir.
