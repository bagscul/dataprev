# frontend — como a FGV cobra

Frontend na FGV é conceitual e prático ao mesmo tempo:
metade é distinguir tecnologias (SPA x PWA, frameworks,
mobile) e metade é LER código HTML/CSS/JS e dizer a saída.
Não dá pra decorar só conceito — treine ler snippet.

## O que mais cai
- SPA x PWA: o par que a FGV mais explora.
- Ler HTML+CSS e prever a renderização (pseudo-elementos
  ::before/::after, content, attr(), flex-direction).
- React: função certa para um objetivo (createPortal para
  renderizar fora da hierarquia normal do DOM).
- Mobile multiplataforma x nativo: Flutter, React Native,
  Kotlin/Swift.
- Acessibilidade WCAG (POUR: perceptível, operável,
  compreensível, robusto).

## Como a banca arma a pegadinha
- Inverte o que é Service Worker: quem depende dele para
  cache/offline/notificações e instalação é a PWA, NÃO a
  SPA. Alternativa que dá Service Worker à SPA é falsa
  (caiu assim no Dataprev 2024).
- Confunde a essência de cada uma: SPA = uma única página
  que atualiza sem recarregar (foco em navegação fluida);
  PWA = web app instalável no SO, funciona offline, parece
  nativo. A PWA pode ser instalada; a SPA roda no navegador.
- Diz que ambas "dependem exclusivamente de framework JS"
  — falso, é distrator recorrente.
- Flutter: a chave é a LINGUAGEM. Flutter = Dart. Se a
  alternativa amarrar Flutter a JS/TS, está errada. React
  Native = JS; Ionic = web; Xamarin = C#.
- Mobile nativo: Android = Kotlin (antes Java), iOS =
  Swift (antes Objective-C). A FGV troca os pares.
- CSS: flex-direction: row-reverse INVERTE a ordem visual;
  ::before insere ANTES, ::after DEPOIS; content: attr(x)
  imprime o VALOR do atributo x. Combine os três para achar
  a saída — a FGV monta a pegadinha exatamente nessa soma.
- React: oferece nomes inventados/parecidos (preRender,
  preloadModule) no lugar de createPortal.

## Como se sair melhor
- Decore a tabela SPA x PWA: Service Worker, offline,
  instalável e "parece nativo" são atributos da PWA.
- Em questão de código CSS, resolva no papel elemento por
  elemento: aplique o pseudo-elemento, resolva o attr(),
  e só então aplique a direção do flex.
- Fixe pares mobile: Dart→Flutter, Kotlin→Android,
  Swift→iOS.
- WCAG operável: preferir rótulos/labels bem associados aos
  campos e várias formas de entrada além do teclado; fugir
  de "submissão automática ao focar" (viola previsibilidade).
