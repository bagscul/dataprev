# uml — como a FGV cobra

## O que mais cai
- Classificar o diagrama em estrutural × comportamental. É o item mais
  frequente do assunto: dá o nome do diagrama e pede a família (ou o
  contrário).
- Diagrama de classes: relacionamentos (agregação × composição), herança,
  multiplicidade, visibilidade.
- Casos de uso (include × extend), sequência, atividade, máquina de estados.
- Os pares que exigem ler a NOTAÇÃO, não só o nome: realização (implementa
  interface) × dependência (usa temporariamente); componentes (peças de
  software e suas interfaces) × implantação/deployment (nós físicos onde as
  peças rodam).
- A contagem: são **14 diagramas** na UML 2.x, 7 estruturais + 7
  comportamentais.

## Como a banca arma a pegadinha
- Troca a família do diagrama: diz que "sequência/atividade/estado" é
  estrutural (são comportamentais) ou que "classe" é comportamental.
- Inverte agregação × composição (losango vazio × cheio; parte independente ×
  dependente do todo).
- Inverte include (sempre executa) × extend (opcional/condicional).
- Troca o símbolo do evento de início/fim pela espessura da borda.
- Mistura UML com BPMN no losango: em **UML** (diagrama de atividade) o
  losango é **nó de decisão** (saída condicional) ou de **junção/merge**; em
  **BPMN** o losango é **gateway** (exclusivo, paralelo, inclusivo). São
  notações diferentes — o enunciado que fala em "gateway" está em BPMN, não em
  UML. BPMN tem dica própria em `../dicas/eng-software.md`.
- Inverte a seta da generalização: ela aponta SEMPRE da subclasse para a
  superclasse, nunca o contrário.
- Troca componentes × implantação: chama de "componentes" o diagrama que
  mostra servidores/nós (é implantação) ou vice-versa.
- Confunde realização (tracejada + triângulo, implementa interface) com
  dependência (tracejada com seta aberta, uso temporário).

## Como se sair melhor
- Estrutural = estrutura estática (Classe, Componente, Implantação/Deployment,
  Pacote, Objeto, Estrutura composta, Perfil). Comportamental = dinâmica
  (Caso de Uso, Sequência, Atividade, Estado, Comunicação, Interação geral,
  Tempo).
- Atalho para a família: se o nome do diagrama sugere ALGO ACONTECENDO no
  tempo (sequência, atividade, estado, comunicação, tempo), é
  comportamental. Se sugere uma PEÇA (classe, componente, pacote, objeto,
  nó), é estrutural.
- Classes: losango **vazio** = agregação (parte vive sem o todo); **cheio** =
  composição (parte morre com o todo). Multiplicidade: `1`, `0..1`, `1..*`, `*`.
- Visibilidade: `+` público, `-` privado, `#` protegido, `~` pacote.
- Caso de uso: «include» obrigatório, «extend» opcional.
- Linha tracejada = relação "fraca": com triângulo é realização (implementa
  interface); com seta aberta é dependência (usa).
- Sequência responde "em que ORDEM as mensagens trocam"; atividade responde
  "qual o FLUXO de trabalho, com decisões e paralelismo"; estado responde
  "por quais SITUAÇÕES um objeto passa".
- Detalhe completo em `../resumo/uml.md`.
