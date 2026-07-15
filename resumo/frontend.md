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
- **Responsividade:** media queries, unidades relativas (%, em, rem, vw/vh),
  layouts flexíveis (Flexbox, Grid).

Pegadinha: **padding × margin** (interno × externo) é o par que a FGV mais
inverte.

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

Pegadinhas: **Service Worker é da PWA**, não requisito de SPA; "SPA instala no
SO como nativo" é característica de **PWA**; SPA/PWA não "dependem
exclusivamente de framework" (dá para fazer com JS puro).

## 3. Frameworks

| | React | Angular | Vue |
|---|---|---|---|
| Tipo | biblioteca de UI (Meta) | framework completo (Google) | framework progressivo |
| Linguagem | JS/JSX | TypeScript | JS |

Pegadinha: a FGV troca React↔Angular (biblioteca × framework completo) e
atribui TypeScript ao React.

## 4. Ajax e comunicação

- **Ajax:** requisições **assíncronas** ao servidor sem recarregar a página
  (base do comportamento SPA); hoje via `fetch`/XHR, dados em JSON.

## 5. UX, acessibilidade e usabilidade

- **UX (experiência do usuário)** × **UI (interface)**: UX é a experiência
  toda; UI é a camada visual.
- **Usabilidade** (Nielsen): eficiência, eficácia, satisfação, facilidade de
  aprendizado, prevenção de erros.
- **Acessibilidade:** **WCAG** (W3C) — perceptível, operável, compreensível,
  robusto; no Brasil, **eMAG** para governo.
- **Arquitetura de informação:** organização e navegação do conteúdo.
- **CMS (sistema de gestão de conteúdo):** cria/gerencia conteúdo sem código
  (WordPress, portais corporativos, workflow editorial).

## O que já caiu (nossas questões)

SPA × PWA (Service Worker, offline, instalável); box model (padding × margin);
`@import` e responsividade; frameworks (React × Angular). Rode `../quiz.py frontend`.

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
