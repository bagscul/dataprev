# DATAPREV 2026 — Desenvolvimento de Software

Prova: **11/10/2026, 13h as 17h**. Portoes fecham 12h30.
Lotacao: Natal/RN. 20 vagas imediatas, 13 de ampla concorrencia.

## Rotina diaria

```bash
./status.py          # o que estudar hoje + como estou
./quiz.py --hoje     # questoes do bloco de hoje, direto no terminal
# ... plataforma de questoes FGV, anota erros em erros/*.md ...
./feito.sh 45 34     # questoes feitas FORA do quiz (plataforma, PDF)
./salvar.sh          # commit + push
```

## Quiz de terminal

```bash
./quiz.py                  # 10 aleatorias do banco original
./quiz.py java redes -n 15 # blocos especificos
./quiz.py --hoje           # bloco previsto no roteiro para hoje
./quiz.py --erradas        # refaz o que voce errou (originais + provas juntos)
./quiz.py --dica java      # como a FGV cobra esse bloco (sem bloco: lista)
./quiz.py --stats          # desempenho acumulado por bloco
```

Voce responde com a letra; ao errar, o quiz explica por que a correta esta
certa e por que CADA uma das outras esta errada. Ao errar, ele grava
AUTOMATICAMENTE a entrada em `erros/<bloco>.md` (deduplicando por questao —
a mesma errada duas vezes nao vira duas anotacoes). Para nao gravar, use
`--sem-anotar`. No fim mostra os conteudos da sessao e registra no
progresso.csv (entao nao use ./feito.sh para as questoes do quiz).

165 questoes originais em estilo FGV, cobrindo os blocos na proporcao
da prova de 2024. As explicacoes ja vem gravadas no banco: o quiz roda
offline, sem chave de API e sem custo — entao qualquer pessoa com o repo
roda no terminal dela.

**Dicas de banca.** `./quiz.py --dica <bloco>` mostra, para aquele assunto,
o que a FGV mais cobra, como ela arma a pegadinha e como se sair melhor.
Quando voce filtra por um bloco (`./quiz.py java`), o quiz lembra que a dica
existe. Os textos ficam em `dicas/<bloco>.md` — edite a vontade.

Duvida que a explicacao do terminal nao resolve? Cole a questao no Claude
Code (veja `CLAUDE.md`): la da pra perguntar de volta.

### Questoes reais das provas

As provas em `provas/*.pdf` viram banco de questoes:

```bash
./importar_provas.py                       # PDF -> banco-provas.json
./gabarito.py --falta                      # o que ainda esta sem gabarito
./gabarito.py dataprev2024 "1-C 2-A ..."   # cola o gabarito OFICIAL da FGV
./quiz.py --prova dataprev2024             # resolve as questoes reais
./quiz.py --prova todas -n 20              # de todas as provas importadas
```

O caderno de questoes nao traz o gabarito, entao a questao entra com
`ans: null` e **o quiz nao a sorteia ate o gabarito oficial ser preenchido**.
Isso e proposital: gabarito chutado treina o reflexo errado, que e pior do
que nao treinar. Questoes que dependem de figura/codigo (que se perdem na
extracao do PDF) tambem ficam fora do sorteio.

IMPORTANTE: o quiz e complemento, nao substituto. Questoes REAIS da FGV
continuam sendo o treino principal. Provas de banca sao protegidas por
direito autoral: o `banco.json` e original, e o `banco-provas.json` (texto
das provas) fica de uso pessoal, em repo privado — nao publique.

### Adicionar mais questoes (escala sozinho)

O quiz le quantas questoes houver — nada esta preso a um numero fixo.

- **Mais provas:** jogue o PDF em `provas/`, rode `./importar_provas.py`,
  depois `./gabarito.py <prova> "1-C 2-A ..."` com o gabarito oficial.
- **Mais questoes originais:** acrescente objetos a `banco.json` (campos:
  `tag`, `q`, `alts` com 5, `ans` 0-4, e de preferencia `why` + `erradas`).
- **Sempre valide depois:** `./valida.py` checa a integridade dos dois bancos
  (estrutura, gabarito, explicacoes) e aponta o que quebraria o quiz. Erro
  bloqueia; aviso (ex: questao sem explicacao) so avisa — o quiz roda mesmo
  assim, so nao mostra o comentario.

## Instalar no Windows — guia da Geys (do zero)

Boa notícia: o quiz roda **só com o Python** (nada de instalar biblioteca).
Você já tem Python e o Windows Terminal, então é rápido. Siga na ordem.

**1. Confirme que o Python funciona.** Abra o Windows Terminal e digite:

```powershell
python --version
```

Tem que aparecer algo como `Python 3.12.x`. Se der erro, tente `py --version`
— se esse funcionar, use `py` no lugar de `python` no resto do guia.

**2. Pegue a pasta do estudo.** São duas formas; escolha uma:

- **Mais simples (sem instalar nada):** peça pro Lucas te mandar a pasta
  compactada (`.zip`) pelo WhatsApp/Drive/pendrive. Salve em algum lugar fácil,
  tipo `Documentos`, e **extraia** (botão direito → Extrair tudo). Vai virar
  uma pasta chamada `dataprev`.
- **Recomendada (pra receber as questões novas que o Lucas adicionar):**
  instale o **Git para Windows** (baixe em git-scm.com, avance tudo no
  instalador). Peça pro Lucas te adicionar como colaboradora no repositório.
  Depois, no Windows Terminal:
  ```powershell
  cd Documentos
  git clone https://github.com/bagscul/dataprev.git
  ```
  Quando o Lucas adicionar questões, você atualiza com `git pull` (passo 5).

**3. Entre na pasta pelo terminal.** No Windows Terminal:

```powershell
cd Documentos\dataprev
```

(dica: no Windows 11 você pode abrir a pasta no Explorer, clicar com o botão
direito dentro dela e escolher "Abrir no Terminal" — já cai no lugar certo.)

**4. Rode o quiz.** No Windows o comando é `python quiz.py` (com o `--quem geys`
pra o seu progresso ficar separado do do Lucas):

```powershell
python quiz.py --quem geys --hoje
python quiz.py --quem geys --dica java
python quiz.py --quem geys --stats
```

Na primeira vez ele cria o `progresso-geys.csv` só seu. Pronto — é isso.

**5. (Só se usou o Git) Receber as questões novas.** Sempre que o Lucas
avisar que adicionou questões, dentro da pasta:

```powershell
git pull
```

> **Importante:** no Windows, em TODOS os comandos deste README troque
> `./quiz.py` por `python quiz.py`. O `./` é coisa de Linux/Mac; no Windows
> não funciona. O resto dos argumentos (`--hoje`, `--dica`, `--erradas`…) é igual.

## Estudando em dupla

Cada pessoa tem seu proprio progresso, no mesmo repo:

```bash
./quiz.py --quem geys --hoje    # roda como a Geys  (no Windows: python quiz.py ...)
./quiz.py --quem geys --stats   # desempenho so dela
```

O roteiro (datas, foco de cada dia) e compartilhado. Os contadores nao:
na primeira vez, `progresso-<nome>.csv` e criado a partir do roteiro com
tudo zerado, e o historico vai para `historico-<nome>.json`. Sem `--quem`,
roda como Lucas (`progresso.csv`), como sempre foi.

O caderno de erros em `erros/*.md` e compartilhado de proposito — errar
junto e ver o erro do outro e parte do metodo.

## Como anotar um erro

Em `erros/<bloco>.md`, tres linhas. O "errei" e a parte que importa:

```markdown
## SOLID — principio da segregacao de interface
- **Errei:** confundi ISP com SRP
- **E:** ISP = interface pequena e especifica; SRP = classe com uma responsabilidade
- FGV 2024 Dataprev Q47 | 24/07
```

## Regras que o roteiro assume

- Questao **todo dia**, sem excecao. Resolver questao e o metodo, nao a revisao.
- Filtro de banca travado em **FGV**. Outra banca constroi reflexo errado.
- Nenhum topico mais de 2 dias seguidos; revisitar em ate 15 dias.
- Simulado **domingo, 13h**, cronometrado. Mesmo horario da prova.
- No simulado: **especificos primeiro** (valem 2,5x), gerais depois.

## Onde a prova se decide

| Bloco (Dataprev 2024) | Questoes | Pontos |
|---|---|---|
| Engenharia de Software | 10 | 25 |
| Programacao | 4 | 10 |
| Banco de Dados / BI | 4 | 10 |
| Seguranca | 3 | 7,5 |
| Redes (fora do edital!) | 3 | 7,5 |
| Arquitetura de Software | 2 | 5 |

Eng. de Software e Banco de Dados sao o eixo duplo da FGV em TI.
Redes caiu mesmo sem estar no conteudo do perfil 3.

## Pendencias

- [ ] Inscricao (ate 06/08, 16h)
- [ ] Boleto R$ 110,00 (ate 07/08)
- [ ] Confirmar com a FGV se Ciencia da Computacao vale como
      "graduacao em TI" sem pos de 360h — concursodataprev26@fgv.br
