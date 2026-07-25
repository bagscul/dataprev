# Git e DevOps — como a FGV cobra

Subtag transversal: as questões continuam nos blocos `programacao`,
`eng-software` e `arquitetura`. Rode com `./quiz.py git-devops`.

## O que mais cai

1. **Comando × efeito.** A banca descreve uma situação ("quer atualizar a
   branch mantendo o histórico linear") e pede o comando. Decore o efeito, não
   a sintaxe: `merge` cria commit de junção; `rebase` reescreve os commits sobre
   a nova base; `revert` cria um commit que anula outro; `reset --hard` descarta
   trabalho; `cherry-pick` copia commits escolhidos.
2. **As três áreas.** Diretório de trabalho → *stage* (index) → repositório
   local → remoto. Quase toda pegadinha de Git mora aqui: `add` move para o
   stage, `commit` grava o que está no stage, `push` envia ao remoto.
3. **`fetch` × `pull`.** `fetch` traz sem integrar; `pull` = `fetch` + `merge`
   (ou `rebase`). Se o enunciado disser "sem alterar a cópia de trabalho", é
   `fetch`.
4. **Entrega × implantação contínua.** Integração contínua = integrar e testar
   a cada push. Entrega contínua (*delivery*) = artefato sempre pronto, subida
   com **aprovação manual**. Implantação contínua (*deployment*) = vai a
   produção **sozinho**. A FGV troca os dois últimos o tempo todo.
5. **Contêiner × orquestrador.** Docker constrói e executa a imagem;
   Kubernetes mantém réplicas, reinicia o que falha e distribui carga. Docker
   Compose orquestra em **um** host, tipicamente em desenvolvimento.

## Como a pegadinha é armada

- **Inversão de par:** `merge`↔`rebase`, `fetch`↔`pull`, delivery↔deployment,
  Docker↔Kubernetes. É o padrão mais frequente do tema.
- **Justificativa colada no comando errado:** a alternativa descreve
  corretamente o efeito de um comando, mas dá o nome de outro. Leia a
  justificativa antes de aceitar o nome.
- **Absoluto plantado:** "o rebase deve *sempre* ser usado", "o pull *nunca*
  altera arquivos". Rebase em branch compartilhada é problema justamente por
  reescrever histórico já publicado.

## Como se sair melhor

Ao ler a questão, pergunte **quem faz o quê**: quem cria commit, quem toca a
cópia de trabalho, quem vai ao remoto, quem decide subir para produção. A
resposta quase sempre se resolve nessa separação, sem precisar da sintaxe.
