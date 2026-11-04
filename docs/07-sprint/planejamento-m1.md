# Planejamento da Sprint 1 — M1

**Período histórico:** 19/10/2026 a 01/11/2026. **Preparação desta versão:** 04/11/2026.
**Milestone pretendido:** M1 — Sprint 1: Elicitação e Modelagem Inicial. A data histórica será preservada.

## Objetivo da Sprint

Produzir e organizar visão, stakeholders, elicitação, requisitos, regras, backlog e três modelos UML para avaliação da P1. Não desenvolver software. O [backlog do produto](../05-backlog/backlog-priorizado.md) descreve trabalho futuro e não mede progresso de implementação na M1.

## Tarefas e saídas

| ID local | Tarefa | Saída principal | Dependências | Estado documental |
|---|---|---|---|---|
| M1-01 | Elaborar Documento de Visão | [Visão](../01-visao/documento-visao.md) | Fontes | Redigido; validação pendente |
| M1-02 | Identificar Stakeholders | [Stakeholders](../02-stakeholders/identificacao-stakeholders.md) | M1-01 | Perfis identificados; representantes pendentes |
| M1-03 | Preparar Roteiro de Entrevistas | [Roteiro](../03-elicitacao/roteiro-entrevistas.md) e questionário | M1-02 | Instrumentos preparados |
| M1-04 | Executar e Registrar Entrevistas | [Resultados](../03-elicitacao/resultados-entrevistas.md) | M1-03, participantes reais | Coleta e análise empírica pendentes |
| M1-05 | Documentar Requisitos Funcionais | [RF](../04-requisitos/requisitos-funcionais.md) | M1-01; revisar após M1-04 | 20 propostas documentadas |
| M1-06 | Documentar Requisitos Não Funcionais | [RNF](../04-requisitos/requisitos-nao-funcionais.md) | M1-01; revisar após M1-04 | 14 propostas documentadas |
| M1-07 | Especificar Regras de Negócio | [RN](../04-requisitos/regras-negocio.md) | M1-05; revisar após M1-04 | 12 propostas documentadas |
| M1-08 | Priorizar Backlog | [Backlog](../05-backlog/backlog-priorizado.md) | M1-05 a M1-07 | 17 histórias; prioridade não validada |
| M1-09 | Elaborar Diagrama de Casos de Uso | [Casos de uso](../06-modelagem-uml/casos-de-uso/README.md) | M1-05, M1-07 | Modelo proposto |
| M1-10 | Elaborar Diagrama de Componentes | [Componentes](../06-modelagem-uml/componentes/README.md) | M1-05 a M1-07 | Modelo proposto |
| M1-11 | Elaborar Diagrama de Implantação | [Implantação](../06-modelagem-uml/implantacao/README.md) | M1-06, M1-10 | Modelo proposto |
| M1-12 | Revisar Documentação e Rastreabilidade | [Matriz](../04-requisitos/matriz-rastreabilidade.md) e relatório técnico | M1-01 a M1-11 | Revisão técnica; validação humana pendente |
| M1-13 | Preparar Entrega no AVA | [Checklist](../08-entrega/checklist-entrega.md) | M1-12, GitHub e acesso do professor | Submissão depende do grupo |

Os IDs acima são locais, não números de issues. A [relação de issues](issues/README.md) preserva os números reais retornados pelo GitHub. Ninguém foi atribuído automaticamente como responsável. Uma tarefa preparada não é necessariamente encerrada; critérios de validação e coleta permanecem abertos.

## Critérios acadêmicos

| Critério da P1 (F02) | Valor | Evidências a avaliar |
|---|---|---|
| Clareza da visão do problema | 0,5 | Problema, necessidades, objetivos e limites |
| Qualidade da elicitação | 0,5 | Técnicas, instrumentos, dados reais e análise; coleta ainda pendente |
| Qualidade dos requisitos | 0,5 | Especificação, regras, critérios e rastreabilidade |
| Modelagem UML | 0,5 | Casos de uso, componentes e implantação consistentes |

Não se estima nota nem se presume aprovação. Os pesos do projeto amplo em F01 diferem dos da P1; a divergência está registrada em [referências](../../referencias/README.md).
