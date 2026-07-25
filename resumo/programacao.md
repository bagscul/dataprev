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

| Abordagem | O que é | Ferramentas / linguagem |
|---|---|---|
| **Nativo** | app específico para cada SO | Android: **Kotlin/Java**; iOS: **Swift/Objective-C** |
| **Multiplataforma (cross)** | um código para vários SO | **Flutter** (Dart), **React Native** (JS), Xamarin (.NET), Ionic (web) |
| **Híbrido** | web dentro de um contêiner nativo (WebView) | Ionic, Cordova |
| **PWA** | web instalável, offline | ver `frontend.md` |

- **Flutter = Dart** (a FGV troca por JS/Kotlin); **React Native = JavaScript**
  (renderiza componentes nativos, ≠ WebView do híbrido).
- Trade-off: nativo dá melhor desempenho/acesso ao hardware; cross reduz custo
  e tempo (um código só).
- **Low-code/no-code:** desenvolvimento visual, pouca ou nenhuma escrita de
  código; acelera entrega e permite "citizen developers", mas limita
  customização e pode gerar lock-in na plataforma.

## 3.1 Java EE / web server-side (JSF, Primefaces)

- **JSF (JavaServer Faces):** framework de UI **baseado em componentes**,
  server-side, orientado a eventos; segue o padrão **MVC**. Ciclo de vida de
  requisição com fases (restore view, apply values, validation, update model,
  invoke application, render response).
- **Primefaces:** biblioteca de **componentes ricos** para JSF (tabelas,
  gráficos, ajax pronto).
- **JSP/Servlet:** camada web mais antiga do Java EE (Servlet processa a
  requisição; JSP gera a view). JSF é a evolução baseada em componentes.

Pegadinha: JSF é **server-side baseado em componentes** (≠ SPA client-side como
React); Primefaces é biblioteca de componentes **de JSF**, não framework à
parte.

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

## 7. Python aplicado a dados

O bloco não é só Java: a FGV mostra um trecho curto de Python e pergunta a
**saída**. A técnica de resolver está em `leitura-codigo.md`; o conteúdo é este.

**NumPy — referência × cópia (a armadilha central):**

| | `a.view()` | `a.copy()` |
|---|---|---|
| Buffer | **compartilha** o de `a` | **independente** |
| `.base` | aponta para o array original | **`None`** |
| Alterar `a[0]` depois | **reflete** no view | não reflete |

- Shape de vetor 1-D termina em vírgula: **`(3,)`**, não `(3,1)`.

**Dicionário:**

- `max(dic)` compara as **chaves**; `max(dic, key=dic.get)` compara os
  **valores** e devolve a **chave** vencedora (não o valor).

**Listas:**

- Fatiamento `lista[a:b]` inclui `a` e **exclui** `b` — `nums[1:4]` devolve
  três elementos.
- Índice negativo conta do fim; `-1` é o último.
- Compreensão e expressão geradora: `sum(n for n in nums if n % 2 == 0)` soma
  só os que passam no filtro.

**Gráficos:** em `matplotlib.pyplot`, o parâmetro **`explode`** destaca (afasta)
uma fatia da pizza.

**PHP 8** (não é Python, mas cai no mesmo tipo de item de função): funções de
sessão — `session_start`, `session_destroy`, `session_regenerate_id`.

Pegadinhas: inverter `view`/`copy` (dizer que `copy` compartilha a base, ou que
`view` tem `.base = None`); errar o shape do 1-D; fatiamento que "inclui" o
índice final; alternativa que traz a **chave certa com o valor errado** no
`max` com `key=`.

## O que já caiu (nossas questões)

Spring/Spring Cloud/Spring Boot/Hibernate/JUnit (papéis); XML/XSLT/JSON;
Flutter (Dart); blockchain (o que não fica no bloco); SPA × PWA (ver
`frontend.md`); NumPy view × copy; Kotlin/Swift; Python — `max(dic, key=)` e
fatiamento com fim exclusivo. Rode `../quiz.py programacao`.

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
