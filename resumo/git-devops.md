# Git e DevOps — resumo (Perfil 3)

> **Contexto:** recorte transversal dos blocos `programacao`, `eng-software` e
> `arquitetura`. O edital cita versionamento, integração/entrega contínua e
> containerização. **Prioridade média-alta**: cai pouco em quantidade, mas as
> questões são curtas e de resposta objetiva — bom retorno por hora.

## As três áreas do Git

```
diretório de trabalho  --git add-->  stage (index)  --git commit-->  repositório local
                                                     --git push-->   remoto
```

Quase toda pegadinha do tema mora nessa separação. O `commit` grava **o que
está no stage** — editar um arquivo já versionado e commitar sem `add` não
inclui a alteração.

## Comandos por efeito (é assim que a banca pergunta)

| Comando | O que faz |
|---|---|
| `git clone` | cria a cópia local inicial de um repositório remoto |
| `git add` | leva a alteração para o stage |
| `git commit` | grava no repositório local o que está no stage |
| `git fetch` | traz referências e objetos do remoto **sem** tocar na cópia de trabalho |
| `git pull` | `fetch` + integração automática (merge ou rebase) |
| `git push` | envia commits locais ao remoto |
| `git merge` | une duas linhas criando um **commit de junção** |
| `git rebase` | **reaplica** os commits sobre outra base; histórico linear |
| `git revert` | cria um commit novo que **anula** outro (seguro em branch pública) |
| `git reset --hard` | move a branch e **descarta** alterações locais |
| `git cherry-pick` | copia **commits escolhidos** para a branch atual |

**Regra de ouro do rebase:** ele reescreve commits (novos identificadores). Não
use em branch já compartilhada — é a razão de a banca chamá-lo de "perigoso".

## Fluxos de trabalho

- **Branch por funcionalidade** + *pull request*: revisão antes da integração.
- **Git Flow:** `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`.
- **Trunk-based:** integrações curtas e frequentes direto no tronco; casa melhor
  com integração contínua.

## CI, CD e CD

O trio que a FGV mais troca:

| Prática | Onde termina |
|---|---|
| **Integração contínua (CI)** | integra e **testa** a cada push |
| **Entrega contínua** (*delivery*) | artefato **sempre pronto** para produção; a subida depende de **aprovação manual** |
| **Implantação contínua** (*deployment*) | o artefato aprovado vai a produção **automaticamente** |

Entrega contínua **pressupõe** integração contínua. Se o enunciado mencionar
aprovação humana antes de subir, é *delivery*, não *deployment*.

## DevOps e DevSecOps

- **DevOps:** cultura de aproximar desenvolvimento e operação — automação,
  medição, compartilhamento de responsabilidade pelo que está em produção.
- **DevSecOps:** segurança deslocada para a **esquerda** (*shift left*),
  incorporada ao pipeline desde o início, e não como etapa final de auditoria.

## Contêineres

| Ferramenta | Papel |
|---|---|
| **Docker** | constrói (a partir do `Dockerfile`) e executa a **imagem**, que empacota aplicação + dependências |
| **Docker Compose** | orquestra vários contêineres em **um host** (tipicamente desenvolvimento) |
| **Kubernetes** | orquestra em **cluster**: mantém réplicas, reinicia o que falha, distribui carga, faz *rolling update* |

**Contêiner × máquina virtual:** o contêiner compartilha o **kernel** do
hospedeiro e empacota só o necessário acima dele; a VM carrega um sistema
operacional convidado inteiro sobre o hipervisor. Daí o contêiner subir em
segundos e pesar menos — e daí também o isolamento ser **menor**.
