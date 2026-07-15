# Resumo da prova — Dataprev 2026, Perfil 3 (Desenvolvimento de Software)

Material de estudo condensado, montado a partir de **quatro fontes**: o
conteúdo programático do edital (Anexo I), as dicas de banca (`../dicas/`), a
resolução das 424 questões que temos (`../banco.json` + `../banco-provas.json`)
e pesquisa em fontes primárias (normas, docs oficiais). Um arquivo por bloco;
este índice é o mapa estratégico.

## Como a prova é montada (oficial, edital 2026)

Prova objetiva, **11/10/2026, 13h–17h**, 70 questões, 5 alternativas, uma
correta. Portões fecham 12h30. Sem consulta. Questão com duas marcações ou
nenhuma = zero.

| Módulo | Disciplina | Questões | Peso | Pontos |
|---|---|---:|---:|---:|
| I — Gerais | Língua Portuguesa | 12 | 1 | 12 |
| I — Gerais | Língua Inglesa | 12 | 1 | 12 |
| I — Gerais | Raciocínio Lógico Matemático | 5 | 1 | 5 |
| I — Gerais | Atualidades **e Inteligência Artificial** | 6 | 1 | 6 |
| I — Gerais | Legislação (Seg. Informação e Proteção de Dados) | 5 | 1 | 5 |
| **II — Específicos** | **Conhecimentos Específicos** | **30** | **2,5** | **75** |
| | **Total** | **70** | | **115** |

**A prova se decide no Módulo II.** 30 questões a 2,5 pontos = 75 dos 115
pontos (**65% da nota**). Errar um específico custa 2,5× errar um geral.
Eliminação: mínimo 57,5 pontos no total (piso legal; a nota de corte real
para Desenvolvimento de Software é bem mais alta — foi o perfil mais
concorrido em 2024).

## Onde a prova provavelmente se concentra (estimativa)

O edital lista os 30 específicos como bloco único, sem subdividir. A
estimativa abaixo vem da Dataprev 2024 (as 30 específicas daquela prova) e da
ênfase do edital 2026 — use como guia de prioridade, não como garantia.

| Bloco (arquivo) | Peso esperado | Por quê |
|---|---|---|
| [eng-software](eng-software.md) | **muito alto** | Foi o maior bloco em 2024 (~10 q). Requisitos, ágil, testes, ponto de função caem sempre. |
| [banco-dados](banco-dados.md) | **alto** | Eixo duplo com Eng. Software. No MPU superou tudo. SQL, normalização, NoSQL. |
| [arquitetura](arquitetura.md) | alto | Microsserviços, REST×SOAP, nuvem, containers, hexagonal. |
| [seguranca](seguranca.md) | alto | ISO 27001/27002:2022, OWASP, OAuth2/SSO, SAST/DAST. |
| [programacao](programacao.md) | médio-alto | Spring, XML/JSON/REST, DevOps, Git, mobile, low-code. |
| [bi](bi.md) | médio | DW, OLAP, ETL, data mining — costuma vir junto com BD. |
| [governanca](governanca.md) | médio | ITIL 4, COBIT 2019, Scrum/Kanban, BPMN. |
| [frontend](frontend.md) | médio | SPA×PWA, React/Angular/Vue, HTTPS/TLS. |
| [java](java.md) | médio | Linguagem-base do edital, mas caiu pouco na amostra. |

## ⚠️ Dois alertas que valem pontos

**1. Redes cai mesmo fora do edital do Perfil 3.** Redes de Computadores
está nos Perfis 2 e 5, **não** no 3. Ainda assim, a Dataprev 2024 trouxe ~3
questões de redes (OSI, protocolo, segurança de rede) para Desenvolvimento de
Software. O edital 2026 do Perfil 3 só cita HTTPS, SSL/TLS. **Não ignore
redes** — veja [redes](redes.md). Ignorar isso custou 7,5 pontos em 2024.

**2. OWASP: 2021 vs 2025.** A Dataprev 2024 cobrou o **OWASP Top 10:2021**.
Mas em **novembro/2025 saiu o OWASP Top 10:2025**, com mudanças grandes
(Security Misconfiguration subiu para A02, "Software Supply Chain Failures"
entrou como A03, SSRF foi absorvido em A01 Broken Access Control, e surgiu
A10 "Mishandling of Exceptional Conditions"). O edital 2026 aponta para a
página do projeto (sem fixar ano). **Saiba as duas listas** — detalhe em
[seguranca](seguranca.md).

## IA entrou nas gerais (novo em 2026)

A disciplina antes chamada "Atualidades" agora é **"Atualidades e Inteligência
Artificial"** (6 questões) e o edital pede fundamentos de IA: conceitos,
aprendizado de máquina, modelos generativos e de linguagem (LLMs), e **ética,
governança e privacidade em IA**. Isso é conteúdo novo e de retorno alto —
veja [atualidades](atualidades.md).

## Como usar este material

1. **Leia o resumo do bloco** antes de atacar as questões dele.
2. **Resolva as questões:** `../quiz.py <bloco>` (ou `--prova` para as reais).
3. **Veja a dica de banca:** `../quiz.py --dica <bloco>` — como a FGV pega.
4. **Revise o que errou:** os erros vão sozinhos para `../erros/<bloco>.md`.

Ordem de prioridade sugerida: comece pelos blocos "muito alto"/"alto" da
tabela acima — é onde os 2,5 pontos por questão se acumulam.

## Índice

**Específicos (Módulo II):**
[eng-software](eng-software.md) ·
[arquitetura](arquitetura.md) ·
[programacao](programacao.md) ·
[java](java.md) ·
[frontend](frontend.md) ·
[banco-dados](banco-dados.md) ·
[bi](bi.md) ·
[seguranca](seguranca.md) ·
[governanca](governanca.md)

**Referência de projeto/OO (dentro de Desenvolvimento de Sistemas):**
[padroes-projeto](padroes-projeto.md) ·
[uml](uml.md)

**Gerais (Módulo I):**
[portugues](portugues.md) ·
[ingles](ingles.md) ·
[rlm](rlm.md) ·
[atualidades](atualidades.md) (+ IA) ·
[legislacao](legislacao.md)

**Fora do edital, mas cai:** [redes](redes.md)
