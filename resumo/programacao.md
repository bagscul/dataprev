# Programação — resumo (Perfil 3)

> **Edital (Perfil 3):** desenvolvimento em Java/JavaEE/JakartaEE/JPA/
> JavaScript; frameworks JUnit, Hibernate, JSF, Primefaces, **Spring, Spring
> Cloud, Spring Boot**; mobile (Android/iOS); low-code/no-code; análise
> estática (clean code, SonarQube); padrões XML, XSLT, UDDI, REST, JSON;
> DevOps; **Git**; codificação (transacional, analítico, mobile, API); reuso;
> blockchain. (Java em si tem arquivo próprio: `java.md`.)
> **Peso esperado: MÉDIO-ALTO.**

## 1. Ecossistema Spring (cai muito)

| Framework | Papel |
|---|---|
| **Spring** | contêiner de inversão de controle (IoC) e injeção de dependência |
| **Spring Boot** | Spring com autoconfiguração e servidor embutido; elimina config manual e boilerplate |
| **Spring Cloud** | ferramentas para sistemas distribuídos/microsserviços (config, discovery, gateway) |
| **Hibernate** | ORM (mapeamento objeto-relacional), implementa JPA |
| **JUnit** | framework de testes de unidade |

Pegadinhas: Spring Boot **não exige** config manual de servidor (embute
Tomcat); Hibernate é **ORM/persistência**, não é framework de teste; JUnit é
teste, **não** é ORM. Spring Cloud = distribuído; Spring Boot = app individual.

## 2. Formatos de dados: XML, JSON, XSLT

| | XML | JSON |
|---|---|---|
| Estrutura | marcação com tags, verboso | pares chave-valor, leve |
| Uso hoje | legado, config, SOAP | **APIs web**, transporte leve |

- **XSLT:** linguagem que **transforma XML** em outro formato (HTML, XML,
  texto). **Não** transforma JSON.
- **REST** usa JSON tipicamente; **SOAP** usa XML.

Pegadinhas: "XSLT transforma JSON" = falso (é XML); "XML e JSON são
equivalentes/idênticos" = falso; JSON não tem comentários nem tipo date nativo.

## 3. Mobile e low-code

- **Multiplataforma:** **Flutter** (linguagem **Dart**), **React Native**
  (JS), **Xamarin** (.NET), **Ionic** (web). Nativo: **Kotlin/Java**
  (Android), **Swift/Objective-C** (iOS).
- **Low-code/no-code:** desenvolvimento visual, pouca ou nenhuma escrita de
  código; acelera entrega, reduz dependência de dev.

Pegadinha: Flutter = **Dart** (a FGV troca por JS/Kotlin).

## 4. Versionamento com Git

- **Git é distribuído:** cada clone tem o histórico completo (≠ SVN
  centralizado).
- Conceitos: commit, branch, merge, `git pull`/`push`, `git clone`,
  merge × rebase, staging area.

## 5. Qualidade de código

- **Clean Code:** nomes claros, funções curtas, baixo acoplamento.
- **SonarQube:** análise **estática** (sem executar) — code smells, bugs,
  vulnerabilidades, dívida técnica, cobertura.
- **DevOps/CI-CD, reuso, padrões de projeto** permeiam (ver `eng-software.md`
  e `arquitetura.md`).

## 6. Blockchain

- **Cadeia de blocos** encadeados por **hash do bloco anterior** (imutável).
- Cada bloco: hash anterior, timestamp, dados/transações, nonce, raiz de
  Merkle. **O saldo das carteiras NÃO é armazenado no bloco** — é derivado do
  histórico de transações (UTXO no Bitcoin).
- Descentralizado, consenso (PoW/PoS), contratos inteligentes (Ethereum).

Pegadinha 2024: "o que **não** é armazenado no bloco" = **saldo das
carteiras** (é calculado, não guardado).

## O que já caiu (nossas questões)

Spring/Spring Cloud/Spring Boot/Hibernate/JUnit (papéis); XML/XSLT/JSON;
Flutter (Dart); blockchain (o que não fica no bloco); SPA × PWA (ver
`frontend.md`); NumPy view × copy; Kotlin/Swift. Rode `../quiz.py programacao`.

## Pegadinhas da FGV (resumo)

- Trocar papéis do ecossistema Spring (Boot↔Cloud, Hibernate↔JUnit).
- XSLT sobre JSON; XML≡JSON; Flutter em JS.
- Absolutos e "equivalentes/idênticos".
- Ver `../dicas/programacao.md`.

## Alta probabilidade / pesquisa extra

- **Confluent Kafka** (mensageria/streaming) aparece no edital dos perfis
  de infra; conceito de tópicos, produtores/consumidores.
- **API/Swagger (OpenAPI):** documenta e contrata REST; Swagger UI.
- **RPA** (UiPath, Automation Anywhere): automação de tarefas de interface.
- **IA/LLM** entrou no edital — ver `atualidades.md` para os fundamentos.
