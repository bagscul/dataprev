# Frontend — resumo (Perfil 3)

> **Edital (Perfil 3):** tecnologias e práticas frontend web — HTML, CSS, UX,
> Ajax, frameworks (**VueJS, Angular, React**); padrões de frontend; **SPA e
> PWA**; UX (sistemas de gestão de conteúdo, arquitetura de informação,
> portais, workflow, acessibilidade, usabilidade).
> **Peso esperado: MÉDIO.**

## 1. HTML e CSS

- **HTML:** estrutura/semântica (tags semânticas: `header`, `nav`, `main`,
  `article`, `section`, `footer`).
- **CSS:** apresentação. **Box model:** content → **padding** (interno,
  dentro da borda) → **border** → **margin** (externo, fora da borda).
- **Responsividade:** **media queries** (estilo conforme a característica do
  dispositivo, tipicamente a largura da tela), unidades relativas (%, em, rem,
  vw/vh), layouts flexíveis.
- **Flexbox × Grid:** Flexbox é **unidimensional** (um eixo por vez, linha *ou*
  coluna); Grid é **bidimensional** (linhas *e* colunas). Grid para a estrutura
  da página, Flexbox para alinhar dentro de cada área.
- **Especificidade:** `id` (100) > classe/atributo/pseudoclasse (10) >
  elemento (1). A ordem de declaração só desempata especificidades **iguais**.
- **`@import` × `<link>`:** os dois trazem CSS externo, mas o `@import` é
  resolvido dentro do CSS e em série (bloqueia a cascata); `<link>` baixa em
  paralelo e é o recomendado. **`@import` não é mecanismo de responsividade** —
  é distrator recorrente em questão de media query.

Pegadinha: **padding × margin** (interno × externo) é o par que a FGV mais
inverte. Duas outras: "a última regra declarada sempre vence" (só entre
especificidades iguais) e trocar Flexbox por Grid.

## 2. SPA × PWA (o coração deste bloco)

| | **SPA** (Single Page Application) | **PWA** (Progressive Web App) |
|---|---|---|
| O que é | app numa única página; troca conteúdo **sem recarregar** | site que se comporta como app nativo |
| Chave | roteamento no cliente, sem full reload | **Service Worker**, offline, **instalável** |
| Depende de | JS no navegador | recursos web progressivos |

- **SPA:** uma página, JavaScript atualiza o conteúdo sem recarregar (React,
  Angular, Vue).
- **PWA:** usa **Service Worker** para **cache, offline e notificações**, e
  pode ser **instalada** no dispositivo como app nativo.
- **Service Worker:** script que roda **em segundo plano**, separado da
  página, como **proxy** entre a aplicação e a rede. Não acessa o DOM
  diretamente e **exige HTTPS** (só `localhost` é exceção). O **manifest**
  (`manifest.json`) é o outro pilar — nome, ícones e modo de exibição que
  permitem a instalação.

Pegadinhas: **Service Worker é da PWA**, não requisito de SPA; "SPA instala no
SO como nativo" é característica de **PWA**; SPA/PWA não "dependem
exclusivamente de framework" (dá para fazer com JS puro).

## 3. Frameworks

| | React | Angular | Vue |
|---|---|---|---|
| Tipo | biblioteca de UI (Meta) | framework completo (Google) | framework progressivo |
| Linguagem | JS/JSX | TypeScript | JS |

Pegadinha: a FGV troca React↔Angular (biblioteca × framework completo) e
atribui TypeScript ao React. Em item de React, cuidado com nomes
inventados/parecidos (`preRender`, `preloadModule`) no lugar de
**`createPortal`** — a função certa para renderizar um componente **fora da
hierarquia normal do DOM** (caiu no MPU).

## 4. Ajax e comunicação

- **Ajax:** requisições **assíncronas** ao servidor sem recarregar a página
  (base do comportamento SPA); hoje via `fetch`/XHR, dados em JSON.

## 5. UX, acessibilidade e usabilidade

- **UX (experiência do usuário)** × **UI (interface)**: UX é a experiência
  toda; UI é a camada visual.
- **Usabilidade — duas listas, não misture.** Os **cinco atributos de
  Nielsen** são **facilidade de aprendizado** (*learnability*), **eficiência**,
  **memorabilidade**, **erros** (poucos e recuperáveis) e **satisfação**. A
  **ISO 9241-11** usa outro trio: **eficácia**, **eficiência** e
  **satisfação**, sempre *num contexto de uso declarado*. "Eficácia" é da ISO;
  "memorabilidade" é de Nielsen — a banca cobra qual lista é de quem.
- **Acessibilidade:** **WCAG** (W3C) — quatro princípios **POUR**:
  perceptível, operável, compreensível, robusto. Níveis de conformidade **A**
  (mínimo), **AA** (o exigido na maioria das normas e contratos públicos) e
  **AAA** (máximo). No Brasil, **eMAG** para governo.
- **ARIA** (*Accessible Rich Internet Applications*): atributos (`role`,
  `aria-label`, `aria-hidden`, `aria-live`) que dão **semântica** a elementos
  **dinâmicos** ou sem tag nativa, para o leitor de tela anunciar função, nome
  e estado. **Regra nº 1 do ARIA: não usar ARIA** — havendo elemento HTML
  nativo com a semântica certa (`<button>`, `<nav>`, `<label>`), use o nativo.
- **Arquitetura de informação:** organização e navegação do conteúdo.
- **CMS (sistema de gestão de conteúdo):** cria/gerencia conteúdo sem código
  (WordPress, portais corporativos, workflow editorial).

## O que já caiu

**Em prova real da FGV:** leitura de HTML+CSS prevendo a renderização
(pseudo-elementos, `content`, `attr()`, `flex-direction`), a função certa do
React (`createPortal`) e WCAG na prática (associar rótulos aos campos,
princípio **operável**) — **MPU**; SPA × PWA, com Service
Worker/offline/instalável — **Dataprev 2024**.

**No nosso banco** (previsto pelo edital, ainda não visto na amostra de
provas): box model (padding × margin, `box-sizing`); especificidade de
seletores; Flexbox × Grid; media queries; escopo de `var` × `let` em laço;
frameworks (React × Angular); `key` em listas e `useState`
assíncrono/*batched*; ARIA; UX × UI; Ajax; CMS.

Rode `../quiz.py frontend` e `../quiz.py leitura-codigo`.

## Pegadinhas da FGV (resumo)

- Atribuir Service Worker à SPA; dizer que SPA instala como nativo.
- Inverter padding↔margin; React↔Angular.
- "Depende exclusivamente de framework".
- Ver `../dicas/frontend.md`.

## Alta probabilidade / pesquisa extra

- **HTTPS, SSL/TLS** estão no edital do frontend também — ver `seguranca.md`.
- **SSR × CSR** (renderização no servidor × no cliente); **hydration**.
- **Web Components**, **micro-frontends** (tendência arquitetural).
- **Core Web Vitals** (performance percebida) e acessibilidade como requisito
  legal em serviços públicos (Lei Brasileira de Inclusão).
