# Matriz de rastreabilidade

**Versão 2.0 · 04/11/2026 · As ligações documentais não significam aprovação dos requisitos.**

Necessidades: [visão](../01-visao/documento-visao.md). Perfis: [stakeholders](../02-stakeholders/identificacao-stakeholders.md). [RF](requisitos-funcionais.md), [RN](regras-negocio.md), [RNF](requisitos-nao-funcionais.md), [histórias](../05-backlog/backlog-priorizado.md) e [casos de uso](../06-modelagem-uml/casos-de-uso/README.md). Fontes: [catálogo](../../referencias/README.md).

## Necessidade → stakeholder → RF → regra → história → caso de uso

| Necessidade | Stakeholder | RF | Fonte/fundamento | RN | US | UC | Estado |
|---|---|---|---|---|---|---|---|
| N-006 | ST-001 | RF-001 | F01 p. 4; campos e unicidade propostos | RN-012 | US-001 | UC-013 | Proposto; não validado |
| N-006 | ST-001, ST-002, ST-003, ST-004 | RF-002 | F01 p. 4; encerramento e papéis detalhados propostos | RN-012 | US-001 | UC-001 | Proposto; não validado |
| N-001 | ST-001, ST-002 | RF-003 | F01 p. 4; combinação e acesso autenticado propostos | RN-001, RN-002, RN-003 | US-002 | UC-002 | Proposto; não validado |
| N-002 | ST-001 | RF-004 | F03 RF-04; proposta derivada do banco de F01 p. 4 | RN-001, RN-006, RN-012 | US-003 | UC-003 | Proposto; não validado |
| N-003 | ST-001, ST-002 | RF-005 | F01 p. 4; momento de liberação proposto | RN-006, RN-011 | US-004 | UC-004 | Proposto; não validado |
| N-002 | ST-001 | RF-006 | F01 p. 4; parâmetros e seleção propostos | RN-001, RN-002, RN-004, RN-010 | US-005 | UC-005 | Proposto; não validado |
| N-002 | ST-001 | RF-007 | F01 p. 4; prazo no servidor e encerramento propostos | RN-004, RN-007, RN-010 | US-006 | UC-005 | Proposto; não validado |
| N-003 | ST-001 | RF-008 | F03 RF-08; proposta de correção objetiva derivada de F01 p. 4 | RN-001, RN-005, RN-007, RN-010 | US-007 | UC-005 | Proposto; não validado |
| N-004 | ST-001 | RF-009 | F03 RF-09; proposta derivada das estatísticas | RN-009, RN-010 | US-011 | UC-006 | Proposto; não validado |
| N-004 | ST-001 | RF-010 | F01 p. 4; cálculo e população considerados propostos | RN-005, RN-009, RN-010 | US-010 | UC-006 | Proposto; não validado |
| N-005 | ST-001, ST-002 | RF-011 | F01 p. 4; autoria e condições de publicação propostas | RN-006, RN-008, RN-012 | US-013 | UC-007 | Proposto; não validado |
| N-005 | ST-004 | RF-012 | F03 RF-12; proposta de governança do fórum | RN-008, RN-012 | US-014 | UC-011 | Proposto; não validado |
| N-008 | ST-004 | RF-013 | F02; F03 RF-13; operações detalhadas propostas | RN-001, RN-002, RN-003, RN-010, RN-011, RN-012 | US-008 | UC-010 | Proposto; não validado |
| N-007 | ST-002, ST-004 | RF-014 | F03 RF-14; apoio docente em F01 p. 7; fluxo editorial proposto | RN-001, RN-003, RN-010, RN-011, RN-012 | US-008 | UC-008 | Proposto; não validado |
| N-004 | ST-003 | RF-015 | F01 p. 7; F03 RF-15; acesso agregado é proposta | RN-005, RN-009, RN-012 | US-012 | UC-009 | Proposto; não validado |
| N-008 | ST-004 | RF-016 | F02; F03 RF-16; permissões detalhadas propostas | RN-009, RN-012 | US-009 | UC-012 | Proposto; não validado |
| N-001 | ST-001, ST-002 | RF-017 | F03 RF-17; hipótese adicional ao filtro de F01 | RN-002 | US-015 | UC-002 | Proposto; não validado |
| N-001 | ST-001, ST-002 | RF-018 | F03 RF-18; derivação de F01 p. 4 e 10 | RN-003, RN-006, RN-011 | US-016 | UC-002, UC-004 | Proposto; não validado |
| N-006 | ST-001, ST-002, ST-003, ST-004 | RF-019 | F02 solicita tratar gestão de perfil como proposta | RN-012 | US-017 | UC-014 | Proposto; não validado |
| N-002 | ST-001 | RF-020 | F02 e detalhamento proposto de F03 RF-07 | RN-001, RN-007, RN-010, RN-012 | US-006 | UC-005 | Proposto; não validado |

## Qualidade transversal

RNF não são ações de atores. A ligação abaixo indica capacidades afetadas e componente responsável, sem inventar um caso de uso para cada atributo de qualidade.

| RNF | Necessidade / stakeholder | RF afetados | Componentes | Fonte e estado |
|---|---|---|---|---|
| RNF-001 | N-009 / ST-001 | RF-003, RF-007, RF-008 | Interface | F03/hipótese de análise; proposta não validada |
| RNF-002 | N-011 / ST-001, ST-004 | RF-003, RF-017 | Questões, persistência | F03/hipótese de análise; proposta não validada |
| RNF-003 | N-011 / ST-004 | RF-002, RF-003, RF-007 | Todos os componentes | F03/hipótese de análise; proposta não validada |
| RNF-004 | N-010 / ST-001, ST-004 | RF-001, RF-002, RF-016 | Autenticação, persistência | F03/hipótese de análise; proposta não validada |
| RNF-005 | N-010 / ST-001, ST-003 | RF-009, RF-010, RF-015, RF-016 | Autenticação, estatísticas | F03/hipótese de análise; proposta não validada |
| RNF-006 | N-009 / ST-001, ST-006 | RF-001, RF-003, RF-006, RF-007, RF-010 | Interface, simulados | F05 e hipótese técnica; proposta não validada |
| RNF-007 | N-008, N-012 / ST-004, ST-005 | RF-012, RF-013, RF-014, RF-016 | Questões, fórum, autenticação | F03/hipótese de análise; proposta não validada |
| RNF-008 | N-011 / ST-004 | RF-007, RF-009, RF-013 | Persistência e infraestrutura conceitual | F03/hipótese de análise; proposta não validada |
| RNF-009 | N-002 / ST-001 | RF-007, RF-020 | Simulados | F03/hipótese de análise; proposta não validada |
| RNF-010 | N-012 / ST-005 | RF-008, RF-010, RF-013 | Todos os componentes | F03/hipótese de análise; proposta não validada |
| RNF-011 | N-009 / ST-001 | RF-002, RF-003, RF-007, RF-010 | Interface | F03/hipótese de análise; proposta não validada |
| RNF-012 | N-010 / ST-001, ST-006 | RF-001, RF-009, RF-011, RF-015, RF-019 | Autenticação, estatísticas, persistência | F03/hipótese de análise; proposta não validada |
| RNF-013 | N-011 / ST-004 | RF-003, RF-007 | Aplicação, persistência | F03/hipótese de análise; proposta não validada |
| RNF-014 | N-011, N-012 / ST-004, ST-005 | RF-004, RF-007, RF-008, RF-013, RF-020 | Simulados, correção, persistência | F03/hipótese de análise; proposta não validada |

## Lacunas e revisão de integridade

- Todos os RF da versão atual possuem fundamento documental ou hipótese declarada, história e caso de uso. Fonte documental não equivale a evidência de entrevista.
- Todas as RN são vinculadas aos RF que condicionam. O detalhamento de permissões e governança exige validação; não há política institucional aprovada anexada.
- Todos os RNF têm critérios de verificação propostos. Metas de produto não foram testadas nesta P1.
- As 17 histórias estão ligadas a RF; exclusões Won't Have não recebem relações artificiais.
- RF-015 depende de autorização institucional e limiar de agregação ainda indefinidos. O fluxo foi especificado para permanecer bloqueado até a decisão.
- A política de moderação, retenção, duração adaptada e revisão editorial permanece pendente. Consultar [registro de decisões](../03-elicitacao/validacao-requisitos.md).
- A comparação automática de IDs/links e cobertura é registrada em [validação técnica](../08-entrega/validacao-tecnica.md); ela não verifica a veracidade de futuros depoimentos nem substitui revisão humana.
