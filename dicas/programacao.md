# programacao — como a FGV cobra

## O que mais cai
- Papéis de frameworks: Spring (núcleo/IoC), Spring Boot
  (autoconfiguração, servidor embutido), Spring Cloud
  (sistemas distribuídos/microsserviços), Hibernate (ORM/
  persistência), JUnit (teste de unidade). A FGV pede quem faz
  o quê e troca os papéis entre eles.
- Formatos de dados: XML, XSLT (transforma XML, não JSON),
  JSON (leve, usado em APIs). Diferenças de expressividade e
  uso.
- Web/mobile: SPA (uma página, sem recarregar) x PWA
  (instalável, Service Workers, offline); Flutter usa Dart;
  linguagens nativas — Kotlin (Android) e Swift (iOS).
- Python aplicado a dados (MPU cobrou forte): NumPy view()
  (compartilha buffer, .base aponta para o original) x copy()
  (cópia independente, .base = None); matplotlib.pyplot
  (parâmetro explode destaca fatia da pizza).
- PHP 8: funções de sessão (session_start, session_destroy,
  session_regenerate_id). Conceitos de IA (redes neurais como
  o que "aprende com dados"), blockchain (o que o bloco
  guarda). Leitura de código pequeno é comum.

## Como a banca arma a pegadinha
- Troca papéis de framework: "JUnit é ORM", "Hibernate é
  framework de teste", "Spring Boot exige Tomcat/JBoss
  standalone", "Spring só serve monólito". Uma frase, um papel
  invertido.
- XSLT: diz que transforma JSON (é XML); ou que XML e JSON são
  "estritamente equivalentes"/XML "mais compacto que JSON".
- SPA x PWA: atribui Service Workers/offline à SPA (é da PWA),
  ou diz que ambas "dependem exclusivamente" de framework JS.
- NumPy: inverte view/copy — diz que copy compartilha base ou
  que view tem base None; ou erra o shape (array 1-D é
  (3,), não (3,1)).
- Distrator de definição decorada: pede o framework Dart e
  oferece React Native (JS), Xamarin (C#), Ionic — que não são
  Dart.

## Como se sair melhor
- Fixe uma frase por framework: Boot = configura e sobe
  sozinho (servidor embarcado); Cloud = distribuído/service
  discovery; Hibernate = objeto↔tabela; JUnit = testa;
  Spring = container/injeção.
- NumPy: copy() = independente, .base None; view() = mesma
  memória, .base é o array-fonte; alterar antes do view()
  reflete no view. Shape de vetor 1-D termina em vírgula: (3,).
- Nativo mobile: Kotlin/Android, Swift/iOS (Objective-C e Java
  são os antigos). Multiplataforma Dart = Flutter.
- SPA = sem reload, roda no navegador; PWA = instalável, cache/
  offline via Service Worker, cara de app nativo.
- Gatilhos: "exclusivamente", "sempre", "estritamente
  equivalentes", "elimina a necessidade". Em código, leia
  linha a linha — a FGV muda um parâmetro só.
