# Validação dos requisitos

**PENDENTE — coleta de dados reais com stakeholders e validação das propostas.**

## Estados adotados

- **Base documental, detalhamento proposto:** a capacidade aparece em F01/F02, mas os critérios e decisões ainda não foram aprovados por usuários.
- **Proposto — não validado:** inferência ou detalhamento do pacote anterior/da análise atual.
- **Validado / ajustar / rejeitado:** somente após decisão real, com data, papel, versão e evidência.

Revisão técnica de links e diagramas não é validação com stakeholders. Nenhum RF, RNF, RN ou prioridade tem aprovação empírica registrada nesta versão.

## Roteiro da sessão de validação

1. Confirmar problema, escopo e perfis, com atenção a necessidades omitidas.
2. Percorrer consulta de questões, tentativa, encerramento e devolutiva.
3. Discutir alternativas sobre prazo, feedback, privacidade, revisão e fórum.
4. Revisar prioridades MoSCoW e metas de qualidade, considerando esforço e restrições reais.
5. Registrar decisão por item, responsáveis e evidências; manter divergências abertas.

## Decisões prioritárias pendentes

| Código | Decisão necessária | Itens afetados | Papéis a consultar |
|---|---|---|---|
| V-001 | Confirmar escolha única e fórmula de pontuação; tratar itens anulados antes de publicação | RF-004, RF-008; RN-001, RN-005 | ST-001, ST-002 |
| V-002 | Validar duração, expiração, envio simultâneo e adaptações de tempo | RF-006, RF-007, RF-020; RN-004, RN-007; RNF-009 | ST-001, ST-002, ST-004 |
| V-003 | Definir momento de liberação do gabarito | RF-005; RN-006 | ST-001, ST-002 |
| V-004 | Definir autorização de agregados e limite mínimo de grupo | RF-015; RN-009; RNF-012 | ST-003, ST-006 |
| V-005 | Confirmar responsáveis pela revisão e direitos de uso | RF-013, RF-014, RF-018; RN-003, RN-011 | ST-002, ST-004 |
| V-006 | Definir política de convivência e moderação | RF-011, RF-012; RN-008 | ST-001, ST-002, ST-004 |
| V-007 | Negociar metas de desempenho, disponibilidade, recuperação e escala | RNF-002, RNF-003, RNF-008, RNF-013 | ST-004, ST-006 |
| V-008 | Validar cadastro, perfil, retenção e encerramento de conta | RF-001, RF-016, RF-019; RN-012; RNF-012 | ST-001, ST-004, ST-006 |
| V-009 | Confirmar acessibilidade, dispositivos e critérios de usabilidade | RNF-001, RNF-006, RNF-011 | ST-001, ST-006 |

## Modelo de registro de decisão

| Campo | Preenchimento futuro |
|---|---|
| ID do registro / versão avaliada | VAL-[sequencial] / versão real |
| Itens e texto avaliado | Identificadores e alterações propostas |
| Participante / papel / data | Código do participante, perfil e data real |
| Decisão | Validado, ajustar, rejeitado ou pendente |
| Justificativa e divergências | Argumentos reais e alternativas discutidas |
| Evidência | Ata ou retorno verificável com dados pessoais minimizados |
| Impacto | Documentos, histórias e diagramas que precisam mudar |

Sem decisões coletadas, não há linhas de aceite preenchidas. Registrar mudanças no Git preserva o histórico; fechar uma issue de redação não significa aprovar requisitos.
