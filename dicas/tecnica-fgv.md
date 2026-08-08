# Técnica de prova FGV — como atacar QUALQUER questão

Guia transversal (vale para todas as matérias), destilado da resolução de ~500
questões reais da FGV em 7 provas. As dicas por assunto (`--dica <bloco>`)
dizem O QUE cada matéria cobra; este guia diz COMO atacar a questão.

## 1. Leia o COMANDO antes de tudo

O comando é a última linha do enunciado. Erro nº 1 em prova é responder o
oposto do que foi pedido.

- **"Assinale a correta"** × **"assinale a INCORRETA / a que NÃO..."** — a FGV
  usa muito o comando negativo. Circule o "incorreta"/"não" no papel.
- **"Julgue as afirmativas I, II, III"** → resolva cada item isolado como
  V/F, depois case com a alternativa (I e II apenas / I, II e III / etc.).
  Uma afirmativa falsa derruba toda alternativa que a inclua — use isso para
  eliminar em bloco.
- **"(V) (F) (F)"** (sequência) → mesma lógica: acertar 1 ou 2 itens já elimina
  metade das alternativas.

## 2. Os padrões de distrator da FGV (o coração)

A FGV constrói alternativa errada de poucas formas. Reconhecê-las é meio
caminho:

- **Absolutos.** "sempre", "nunca", "exclusivamente", "apenas", "todo",
  "invariavelmente", "impossível", "garante". No mundo técnico quase nada é
  absoluto — a alternativa com absoluto é **quase sempre** o distrator.
- **Inversão de conceitos.** Troca dois conceitos do mesmo par:
  OLTP↔OLAP, PUT↔PATCH, agregação↔composição, checked↔unchecked,
  controlador↔operador, governança↔gestão, IDS↔IPS, SAST↔DAST, TCP↔UDP,
  incidente↔problema, Factory↔Abstract Factory. Se você domina o par lado a
  lado, a inversão salta aos olhos.
- **A "quase certa".** Acerta a primeira metade e erra a segunda ("X é um
  índice bitmap, **adequado para alta cardinalidade**" — bitmap é para
  **baixa**). Leia a alternativa INTEIRA; a FGV esconde o erro no fim.
- **Extrapolação (interpretação).** Em português/inglês, o distrator **diz
  mais do que o texto diz** ou inverte a tese do autor. Se não está sustentado
  no texto, é distrator — não importa se é verdade no mundo.
- **Troca de número.** "5 domínios do COBIT", "4 dimensões do ITIL", "3 formas
  normais", "camada 7 do OSI". A FGV troca o número. Decore as quantidades.
- **Troca de ordem.** Fases do ARIES (Analysis→Redo→Undo), ciclo de vida,
  camadas, formas normais. O distrator embaralha a sequência.
- **Contradição interna.** "SOAP sem contrato formal" (SOAP usa WSDL),
  "microsserviço com banco único compartilhado" (contra o princípio). A
  alternativa se contradiz — descarte.

## 3. Estratégia de resolução

1. **Elimine primeiro os absolutos e as contradições internas** — costumam
   sumir 2 alternativas de cara.
2. **Compare as 2 que sobraram.** A FGV quase sempre deixa uma "quase certa"
   como pegadinha final; a diferença está num detalhe (uma palavra, a segunda
   metade da frase, um número).
3. **Volte ao enunciado** e confirme a escolhida contra o que foi pedido (o
   cenário e o comando), não contra sua memória.
4. **Interpretação:** volte ao TRECHO exato. Nunca responda "pelo que faz
   sentido"; responda pelo que o texto afirma.
5. **Só no chute, empatado: fique com a mais longa.** Medido nas 15 provas FGV
   do `banco-provas.json`: a correta é a alternativa mais longa em **33%** dos
   itens (o acaso é 20%), e o efeito é forte justamente nos blocos técnicos —
   **bi 50%, banco-dados 49%, programação 46%, atualidades 41%**. Em português
   (25%) e inglês (17%) **não vale**: ali a banca nivela o tamanho. Isso é
   desempate de último recurso, depois de esgotar conteúdo e eliminação — não
   é critério de escolha.

## 4. Gestão de tempo (4h, 70 questões)

- **Específicos primeiro.** Valem **2,5×** (75 dos 115 pontos). Comece por eles
  com a cabeça fresca; deixe português/inglês/RLM para depois.
- **Não trave.** Marque a questão difícil, siga, volte no fim. Uma questão de
  RLM não vale mais que uma de eng. de software — e custa mais tempo.
- **Ritmo:** ~3 min por questão em média. Treine com `../quiz.py --simulado`
  (cronometrado, sem feedback até o fim).

## 5. Regras de ouro

- **Filtro travado em FGV.** Cada banca tem uma gramática de pegadinha própria;
  reflexo de CESPE/outra banca atrapalha aqui.
- **Cartão de resposta:** questão com duas marcações ou nenhuma = **zero**.
  Confira. Reserve tempo para preencher.
- **Não mude resposta no chute.** Só troque se tiver um motivo concreto (releu
  e viu o erro), não por insegurança.
- **Anulada acontece.** Se a questão parecer ter duas certas ou nenhuma, marque
  a "menos errada" e siga — não perca tempo brigando com ela.

## 6. Depois da prova simulada

Toda errada vira material de revisão: `../quiz.py --erradas` (repetição
espaçada) e a anotação automática em `../erros/<bloco>.md`. O caderno de erros
é o seu único material nas últimas duas semanas.
