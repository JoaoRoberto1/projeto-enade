# Revisão de consistência — P2 / M2

**Data do registro:** 19/11/2026. **Base:** P1 em e810ffd; SRS 3.0 e protótipo P2.<br/>
**Natureza:** revisão técnica dos artefatos; não é validação empírica com participantes nem aceite do professor.

## Método e fontes

Comparar os 20 RF, 14 RNF e 12 RN herdados com os 14 casos de uso do SRS, os atores e dependências UML e as 17 telas. Inspecionar políticas de acesso, versões, feedback e tempo. Executar os cenários do protótipo e guardar relatórios reais, com falhas corrigidas antes da evidência final.

- [SRS](../09-srs/SRS.md)
- [Matriz P1 com necessidade, stakeholder e história](../04-requisitos/matriz-rastreabilidade.md)
- [Índice UML](../06-modelagem-uml/README.md)
- [Telas e limites de fidelidade](../11-prototipos/README.md)
- [Resultado da verificação do protótipo](../../evidencias/p2/verificacao-prototipo.json)

## Matriz de cobertura funcional

Os testes PT verificam o comportamento demonstrativo. Uma linha coberta não comprova os requisitos de produção de servidor, rede, segurança ou banco. A ligação abaixo complementa a matriz P1, preservada como base histórica.

| Requisito | Caso de uso | Regras | Telas | Verificação do protótipo |
|---|---|---|---|---|
| RF-001 | UC-013 | RN-012 | T02 | PT-01 |
| RF-002 | UC-001 | RN-012 | T01 | PT-01 |
| RF-003 | UC-002 | RN-001, RN-002, RN-003 | T03, T04 | PT-02 |
| RF-004 | UC-003 | RN-001, RN-006, RN-012 | T05 | PT-03 |
| RF-005 | UC-004 | RN-006, RN-011 | T05, T08, T14 | PT-03, PT-05, PT-06 |
| RF-006 | UC-005 | RN-001, RN-002, RN-004, RN-010 | T03, T06, T07, T08 | PT-04 |
| RF-007 | UC-005 | RN-004, RN-007, RN-010 | T03, T06, T07, T08 | PT-05, PT-06, PT-12 |
| RF-008 | UC-005 | RN-001, RN-005, RN-007, RN-010 | T03, T06, T07, T08 | PT-06 |
| RF-009 | UC-006 | RN-009, RN-010 | T03, T09 | PT-06 |
| RF-010 | UC-006 | RN-005, RN-009, RN-010 | T03, T09 | PT-03, PT-06 |
| RF-011 | UC-007 | RN-006, RN-008, RN-012 | T10 | PT-07 |
| RF-012 | UC-011 | RN-008, RN-012 | T17 | PT-10 |
| RF-013 | UC-010 | RN-001, RN-002, RN-003, RN-010, RN-011, RN-012 | T12, T13 | PT-09 |
| RF-014 | UC-008 | RN-001, RN-003, RN-010, RN-011, RN-012 | T13, T14 | PT-09 |
| RF-015 | UC-009 | RN-005, RN-009, RN-012 | T15 | PT-11 |
| RF-016 | UC-012 | RN-009, RN-012 | T16 | PT-01, PT-10 |
| RF-017 | UC-002 | RN-002 | T03, T04 | PT-02 |
| RF-018 | UC-002, UC-004 | RN-003, RN-006, RN-011 | T03, T04, T05, T08, T14 | PT-03, inspeção das telas |
| RF-019 | UC-014 | RN-012 | T11 | PT-08 |
| RF-020 | UC-005 | RN-001, RN-007, RN-010, RN-012 | T03, T06, T07, T08 | PT-05, PT-12 |

## Achados e decisões de revisão

| ID | Situação encontrada | Tratamento na P2 | Evidência |
|---|---|---|---|
| C-01 | P1 descrevia casos de uso em tabela resumida | Detalhados atores, gatilhos, pré/pós-condições, fluxo principal e exceções dos 14 UC | SRS 3.3 |
| C-02 | Textos UML indicavam ausência de qualquer implementação | Separada arquitetura-alvo da demonstração estática; atualizados componentes e implantação | UML de componentes e implantação |
| C-03 | Envio e término dependem de decisão temporal consistente | Adicionados estados da tentativa e sequência de RF-020; limite de recebimento preservado | Dois diagramas novos; PT-05/06/12 |
| C-04 | Professor e administrador têm responsabilidades diferentes | Aprovação por Professor e publicação por Administrador; editar invalida revisão | UC-008/010; PT-09 |
| C-05 | Feedback pode antecipar a solução em tentativa ativa | Bloqueados prática/discussão e resultado anterior com questão da tentativa ativa | RN-006; PT-05 |
| C-06 | Cronômetro e login do protótipo poderiam parecer controles reais | Limites explícitos no SRS, README do protótipo, telas e diagramas | SRS 2.6 e 3.1; tela Sobre |
| C-07 | Painel agregado depende de decisões institucionais ausentes | Estado inicial bloqueado; exemplo fictício separado, sem nomes e com supressão | UC-009; PT-11 |
| C-08 | Máximos de duração, número de alternativas e dados de exemplo são escolhas de tela | Identificados como convenções demonstrativas, sem alterar silenciosamente as RN da P1 | SRS 2.6 |
| C-09 | Gráfico pode ocultar detalhes do cálculo | Tabela textual e fórmula ponderada; práticas individuais excluídas | RF-010; PT-03/06 |
| C-10 | Coleta e validação não foram realizadas | Mantidas como pendências reais; testes técnicos não foram registrados como entrevistas | SRS 4.2/4.3 |

## RNF: o que a P2 permite verificar

RNF-001/006/011: inspecionar rótulos, estados, navegação e largura móvel é útil, mas não substitui usuários reais, auditoria WCAG nem a matriz completa de navegadores. RNF-010: componentes e rastreabilidade foram revisados; a separação de um backend ainda será projetada. RNF-014: o protótipo demonstra preservação de versões e encerramento local; concorrência, transações e falhas distribuídas não foram testadas.

RNF-002/003/004/005/007/008/009/012/013 permanecem requisitos da aplicação-alvo a negociar e verificar em ambiente apropriado. Controles locais não satisfazem autorização de servidor; cronômetro do navegador não prova confiabilidade temporal; o exemplo agregado não aprova uma política de privacidade.

## Resultado e pendências

Todos os RF possuem caso de uso e tela relacionada; os quatro atores concretos são preservados. As cinco visões UML distinguem objetivos, responsabilidades, ambientes, estados e sequência. A cobertura estática é registrada pelo verificador documental; o resultado de execução está no JSON de evidências.

Permanecem abertas a validação com stakeholders e as decisões institucionais enumeradas no SRS. Aprovar o trabalho acadêmico, aceitar os requisitos e colocar um produto em produção são decisões distintas.
