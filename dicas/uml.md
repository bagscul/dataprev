# uml — como a FGV cobra

## O que mais cai
- Classificar o diagrama em estrutural × comportamental.
- Diagrama de classes: relacionamentos (agregação × composição), herança,
  multiplicidade, visibilidade.
- Casos de uso (include × extend), sequência, atividade, máquina de estados.

## Como a banca arma a pegadinha
- Troca a família do diagrama: diz que "sequência/atividade/estado" é
  estrutural (são comportamentais) ou que "classe" é comportamental.
- Inverte agregação × composição (losango vazio × cheio; parte independente ×
  dependente do todo).
- Inverte include (sempre executa) × extend (opcional/condicional).
- Troca o símbolo (evento início/fim pela espessura da borda; losango de
  gateway × decisão).

## Como se sair melhor
- Estrutural = estrutura estática (Classe, Componente, Implantação/Deployment,
  Pacote, Objeto). Comportamental = dinâmica (Caso de Uso, Sequência,
  Atividade, Estado, Comunicação).
- Classes: losango **vazio** = agregação (parte vive sem o todo); **cheio** =
  composição (parte morre com o todo). Multiplicidade: `1`, `0..1`, `1..*`, `*`.
- Caso de uso: «include» obrigatório, «extend» opcional.
- Detalhe completo em `../resumo/uml.md`.
