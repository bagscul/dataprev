# Histórico de atualizações

Melhorias no material de estudo (Dataprev 2026, Perfil 3).

## 2026-07-16 — auditoria das novas, reforço de blocos e resumo de órfãos

- **Auditoria independente das 72 questões originais novas** (as 52 + 20 de
  reforço): cada uma resolvida do zero contra fonte. **Zero gabaritos errados.**
- **Reforço dos blocos mais magros:** +10 Java e +10 Governança (originais,
  validadas). Java 19→29, Governança 18→28.
- **`resumo/orfaos.md`** (novo): administração de BD (DBA) — ARIES/WAL,
  tablespaces, backup incremental×diferencial, otimizador — que o resumo de
  banco-dados (focado em modelagem/SQL) não detalhava, + temas coringa.
- **Dicas de padrões-projeto e UML** (antes só tinham resumo).
- Contagens atualizadas: **237 originais + 7 provas reais = ~616 utilizáveis.**

## 2026-07-15 (tarde) — +3 provas reais e questões novas nos temas fracos

- **3 provas ALERO 2026 (FGV)** importadas com gabarito oficial e explicações
  validadas: `cnsal-ads` (Análise e Desenvolvimento de Sistemas), `cnsal-bd`
  (Banco de Dados), `cnsal-redes` (Infraestrutura de Redes). **+120 questões
  reais utilizáveis.** Módulo comum (Q1-40) mantido uma vez; trivia estadual
  de Rondônia descartada.
- **Análise de gaps** e geração de **52 questões originais** (estilo FGV,
  gabarito validado) para os temas fracos/zerados: Padrões de Projeto (GoF),
  UML, frontend, atualidades/IA e inglês.
- Banco agora: **217 originais + ~380 de prova = ~596 questões utilizáveis.**
- `valida.py` sem erros.

## 2026-07-15 — provas, dicas, resumos e ferramentas de estudo

Grande atualização. Em ordem do que foi feito:

### Provas reais viraram banco de questões

- **`importar_provas.py`**: extrai as questões dos PDFs em `provas/`
  (Dataprev 2024, MPU 2025, TJ-RJ 2026 ×2) para `banco-provas.json`.
- **`gabarito.py`**: preenche o gabarito **oficial** da FGV. Questão sem
  gabarito **não** entra no sorteio (gabarito chutado treina reflexo errado).
  Os 4 gabaritos definitivos foram carregados (todos tipo 1 – branca).
- **259 questões reais utilizáveis**, cada uma com explicação de *cada*
  alternativa errada, validada contra fonte. 5 anuladas e 25 que dependem de
  figura ficam fora do sorteio.
- Jogue: `./quiz.py --prova dataprev2024` ou `--prova todas`.

### Auditoria das 165 questões originais

- Cada questão original foi resolvida do zero contra fonte primária.
  Nenhum gabarito estava errado; **3 explicações foram corrigidas** (OWASP
  2021, Marco Civil pós-STF de jun/2025, referência de perfil).

### Explicações e caderno de erros automático

- Ao errar, o quiz explica **por que cada alternativa errada está errada**
  (offline, sem custo — as explicações vêm gravadas no banco).
- O erro é gravado **automaticamente** em `erros/<bloco>.md`, com dedup por
  questão. Desliga com `--sem-anotar`.

### Dicas de banca — `--dica <bloco>`

- 16 guias em `dicas/`: o que a FGV mais cobra em cada assunto, como arma a
  pegadinha e como se sair melhor. Ancorados nas provas reais.

### Resumo de conteúdo — `--resumo <bloco>`

- 15 arquivos em `resumo/` (um por bloco) + visão geral, cobrindo o edital do
  Perfil 3, integrando dicas + questões resolvidas + pesquisa em fonte.
- Alertas: **redes** cai fora do edital do Perfil 3; **OWASP 2025** mudou o
  ranking; **IA** entrou nas gerais; estrutura oficial da prova (Módulo I 40 ×
  peso 1 + Módulo II 30 × peso 2,5 = 115 pontos).

### Integração com o roteiro

- **`--hoje`** cobre os **dois blocos do dia** (específico + geral) e mostra os
  atalhos de dica/resumo de cada um. Dias especiais: **revisão** dispara a
  repetição espaçada, **simulado** dispara o modo cronometrado, descanso/prova
  avisam.
- **`--dia ontem`** (ou `anteontem`, `-3`, `AAAA-MM-DD`): faz o plano de um dia
  atrasado e credita **naquele** dia (conserta a aderência).
- **`--pendentes`**: lista os dias de roteiro em aberto.
- O painel **`status.py`** mostra o plano do dia com os comandos prontos.

### Repetição espaçada — `--erradas`

- Agora é repetição espaçada de verdade (estilo Leitner): a questão sai do pool
  quando você acerta 2× seguidas desde o último erro; se errar de novo, volta.
  Não revisa mais o que já foi fixado.

### Simulado cronometrado — `--simulado`

- 70 questões no formato da prova (gerais peso 1 + específicos peso 2,5, na
  proporção do edital), específicos primeiro, **sem feedback até o fim**,
  cronometrado. No fim: nota ponderada, projeção para os 115 pontos, corte de
  eliminação e desempenho por bloco. `-n` escala o tamanho.

### Estudo em dupla e escalabilidade

- **`--quem <nome>`**: progresso separado por pessoa (roteiro compartilhado).
  O README tem um guia de instalação no Windows para a Geys.
- **`valida.py`**: confere a integridade dos dois bancos ao adicionar questões.
- Guia no README de como adicionar mais provas e mais questões geradas.

## 2026-07-13 — setup inicial

- Roteiro de 13 semanas, painel (`status.py`), caderno de erros (`erros/`),
  quiz de terminal (`quiz.py`) com 165 questões originais estilo FGV.
