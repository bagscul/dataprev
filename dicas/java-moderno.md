# Java moderno (17/21 LTS) — como a FGV cobra

Subtag transversal: as questões continuam no bloco `java`. Rode com
`./quiz.py java-moderno`. Complementa `./quiz.py --dica java`.

O edital 2026 cita Java como linguagem-base, e as versões LTS em uso são a 17 e
a 21. O que entrou nelas é material novo de banca — e banca gosta de material
novo, porque o candidato ainda decorou a versão antiga.

## O que mais cai

1. **`var` é inferência, não tipagem dinâmica.** O compilador deduz o tipo do
   inicializador e o **fixa**. Só vale para variável local (e parâmetro de
   lambda): em atributo de instância ou parâmetro de método, não compila.
2. **`record`.** Portador de dados transparente: o compilador gera construtor
   canônico, acessadores, `equals`, `hashCode` e `toString`; os campos são
   finais. É implicitamente **final** e estende `java.lang.Record` — logo **não
   pode estender outra classe** (implementar interface, pode).
3. **`sealed` + `permits`.** Fecha a hierarquia para que o compilador consiga
   verificar a exaustividade de um `switch` sobre tipos. Cada subtipo permitido
   tem de ser `final`, `sealed` ou `non-sealed`. O `permits` pode ser omitido se
   os subtipos estiverem **no mesmo arquivo**.
4. **`switch` com seta (`->`).** Executa só o ramo correspondente: acabou o
   `break` e acabou o *fall-through*.
5. **Threads virtuais (Java 21).** Gerenciadas pela JVM sobre poucas *carrier
   threads*. Ao bloquear em E/S, a virtual é desmontada e libera a thread do
   sistema operacional. Ganho em carga **dominada por espera**, não em cálculo.

## As duas armadilhas de threads virtuais

- **Pinning.** Bloquear dentro de um bloco `synchronized` prende a thread
  virtual ao carregador, que deixa de ser liberado — o ganho evapora. A
  recomendação é trocar por `ReentrantLock` nas seções que bloqueiam.
- **Pool.** O modelo é **uma thread virtual por tarefa**, porque criá-la é
  barato. Continuar submetendo a um pool fixo devolve o gargalo que a migração
  queria eliminar.

## Como a pegadinha é armada

- **Confundir concorrência com paralelismo:** "executa em mais núcleos do que a
  máquina tem". Threads virtuais aumentam quantas tarefas ficam em andamento,
  não a capacidade de cálculo.
- **Trocar `final` por `abstract`:** dizer que o `record` é abstrato, ou que a
  classe `sealed` "substitui o `final`". Selado permite herança — só que apenas
  pelos tipos autorizados.
- **Inverter a regra do `permits`:** "pode ser omitido quando os subtipos estão
  em outro arquivo". É o contrário.
