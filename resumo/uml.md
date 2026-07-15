# UML — resumo (Perfil 3)

> **Contexto:** UML não está listada com todas as letras no edital do Perfil 3
> (aparece explícita no Perfil 2), mas é vizinha de "análise e projeto
> orientados a objetos" e "design de software", que estão. A FGV cobra UML em
> provas de TI com frequência — vale saber o essencial. **Prioridade média.**

## Os 14 diagramas em 2 famílias

| Família | Foca em | Diagramas principais |
|---|---|---|
| **Estruturais** | a estrutura estática | **Classe**, Objeto, Componente, Implantação (deployment), Pacote, Estrutura composta, Perfil |
| **Comportamentais** | o comportamento dinâmico | **Caso de uso**, **Sequência**, **Atividade**, **Estado (máquina de estados)**, Comunicação, Interação geral, Tempo |

Pegadinha: a FGV troca estrutural ↔ comportamental. **Classe** é estrutural;
**sequência, atividade, estado, caso de uso** são comportamentais.

## Diagrama de Classes (o mais cobrado)

Mostra classes, atributos, métodos e **relacionamentos**:

| Relacionamento | Significado | Notação |
|---|---|---|
| **Associação** | ligação entre classes | linha |
| **Agregação** | todo-parte **fraca** (a parte vive sem o todo) | losango **vazio** |
| **Composição** | todo-parte **forte** (a parte morre com o todo) | losango **cheio** |
| **Herança/Generalização** | é-um (subtipo) | seta triângulo vazio |
| **Dependência** | usa temporariamente | seta tracejada |
| **Realização** | implementa interface | tracejada + triângulo |

- **Multiplicidade:** `1`, `0..1`, `1..*`, `*` (muitos).
- **Visibilidade:** `+` público, `-` privado, `#` protegido, `~` pacote.

Pegadinha central: **agregação (losango vazio, parte independente)** ×
**composição (losango cheio, parte dependente)**.

## Casos de Uso (requisitos funcionais)

- **Ator** (boneco), **caso de uso** (elipse), **fronteira do sistema**.
- **«include»**: comportamento **sempre** incluído (obrigatório).
- **«extend»**: comportamento **opcional/condicional**.
- Generalização de atores/casos.

Pegadinha: **include** (sempre executa) × **extend** (às vezes).

## Sequência (interação no tempo)

- **Linhas de vida** (objetos no topo), **mensagens** trocadas na ordem
  temporal (de cima para baixo), **barras de ativação**.
- Mensagem síncrona (seta cheia) × assíncrona (seta aberta) × retorno
  (tracejada).

## Atividade e Estado

- **Atividade:** fluxo de trabalho/algoritmo — nós de ação, decisão (losango),
  **bifurcação/junção** (barra, paralelismo), início/fim. Parecido com
  fluxograma; usado para modelar processos.
- **Máquina de estados:** os **estados** de um objeto e as **transições**
  disparadas por eventos (o objeto reage diferente conforme o estado — casa
  com o padrão State).

## Como se sair melhor

1. **Decore a família de cada diagrama** (estrutural × comportamental) — é a
   pegadinha mais comum.
2. **Diagrama de classes:** memorize agregação × composição (vazio × cheio) e
   as multiplicidades.
3. **Caso de uso:** include (obrigatório) × extend (opcional).
4. Ligue ao resto: caso de uso ↔ requisitos funcionais; classes ↔ OO/SOLID;
   estado ↔ padrão State (`padroes-projeto.md`).

## Alta probabilidade / pesquisa extra

- Diagramas mais cobrados: **Classe, Caso de Uso, Sequência, Atividade.**
- **Deployment** (implantação) e **Componente** aparecem em questões de
  arquitetura.
