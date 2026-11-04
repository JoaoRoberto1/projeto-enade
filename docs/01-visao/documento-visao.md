# Documento de visão — Sistema de Apoio ao ENADE

**Versão:** 2.0 · **Data de preparação:** 04/11/2026 · **Estado:** especificação documental para validação.
**Fontes:** [F01, F02, F03 e F04](../../referencias/README.md). Nenhuma entrevista ou aprovação é presumida.

## 1. Identificação do projeto

Universidade de Fortaleza (Unifor), disciplina Requisitos e Modelagem de Sistemas, Atividade 1 — Trabalho P1 (2,0 pontos). Sprint 1 / M1, de 19/10/2026 a 01/11/2026. Integrantes: **João Roberto de Oliveira Felix** e **Vinicius Lisboa de Albuquerque**. Matrículas: **PENDENTE — informar no AVA, se exigidas**. A elaboração atual ocorre após o período histórico, sem retroagir datas de execução.

## 2. Introdução

Este documento delimita o problema educacional, o público e a proposta de um sistema web/mobile de preparação para o ENADE. A M1 produz os instrumentos de elicitação, uma especificação inicial rastreável e modelos UML. O conteúdo serve à discussão com stakeholders e à avaliação acadêmica; não é uma aplicação implantada nem uma linha de base aprovada.

## 3. Contextualização do ENADE

O Exame Nacional de Desempenho dos Estudantes integra a avaliação da educação superior brasileira e avalia o desempenho dos estudantes em relação à formação de seus cursos. O sistema proposto apoia o estudo; não realiza inscrição no exame, não substitui procedimentos do Inep e não emite resultados oficiais. Referências: F01, p. 2, e [portal do Inep](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade).

## 4. Problema identificado

Segundo F01, p. 2, os estudantes têm dificuldade de preparação diante de materiais pouco organizados, falta de simulados práticos e feedback insuficiente. A dispersão exige procurar questões em fontes diferentes e dificulta selecionar conteúdos do curso. Sem devolutiva por área, o estudante pode repetir exercícios sem reconhecer lacunas. Essas consequências são hipóteses analíticas coerentes com o problema; sua frequência e intensidade ainda dependem de coleta real.

## 5. Justificativa

Concentrar questões classificadas, prática temporizada e explicações pode tornar o estudo mais orientado. A engenharia de requisitos reduz ambiguidades antes de qualquer implementação: determina quem pode consultar resultados, quando liberar o gabarito e como preservar tentativas. Validar essas decisões nesta etapa evita que uma solução tecnicamente executável deixe de atender às necessidades pedagógicas ou de acessibilidade.

## 6. Objetivo geral

Especificar, por elicitação e modelagem inicial, um sistema de apoio ao ENADE que permita estudar questões organizadas, realizar simulados cronometrados e interpretar o próprio desempenho.

## 7. Objetivos específicos

1. Identificar os stakeholders e as necessidades documentadas, distinguindo hipóteses de evidências de campo.
2. Preparar entrevistas e questionário para investigar hábitos, barreiras, expectativas e restrições.
3. Definir RF, RNF e regras verificáveis, com origem, prioridade e estado explícitos.
4. Priorizar a jornada de consulta, prática e feedback no backlog do produto.
5. Modelar casos de uso, componentes e implantação conceitual, vinculados aos requisitos.
6. Organizar a M1 no repositório com referências, evidências reais e pendências de entrega.

## 8. Público-alvo

Estudantes de graduação são os usuários primários. Professores apoiam a qualidade pedagógica; coordenadores acompanham necessidades do curso; administradores mantêm conteúdos e acessos. Equipe de análise e instituição de ensino são stakeholders complementares de organização e governança. Os papéis estão detalhados no [mapa de stakeholders](../02-stakeholders/identificacao-stakeholders.md).

## 9. Necessidades dos usuários

| ID | Necessidade | Stakeholders | Fundamento e limite |
|---|---|---|---|
| N-001 | Encontrar questões relevantes ao curso, ano, área e componente. | ST-001, ST-002 | F01, p. 2 e 4; critérios detalhados a validar. |
| N-002 | Praticar com tempo delimitado e respostas registradas. | ST-001 | F01, p. 4; encerramento e pontuação propostos. |
| N-003 | Compreender as respostas com explicações pedagógicas. | ST-001, ST-002 | F01, p. 4; momento de liberação proposto. |
| N-004 | Identificar dificuldades por área e acompanhar evolução. | ST-001, ST-003 | F01, p. 4 e 7; histórico e agregação propostos. |
| N-005 | Discutir dúvidas associadas às questões. | ST-001, ST-002 | F01, p. 4; moderação proposta. |
| N-006 | Acessar uma conta e controlar o próprio perfil. | ST-001, ST-004 | Cadastro/autenticação em F01, p. 4; perfil proposto. |
| N-007 | Garantir coerência pedagógica dos comentários e gabaritos. | ST-002 | Apoio docente em F01, p. 7; revisão editorial proposta. |
| N-008 | Manter catálogo e permissões de forma controlada. | ST-004 | F02 e papel administrativo de F01; operações propostas. |
| N-009 | Estudar com diferentes dispositivos e tecnologias assistivas. | ST-001, ST-006 | Hipótese de inclusão; F01, p. 3 e 7, e referência F05. |
| N-010 | Evitar exposição indevida de dados de estudo. | ST-001, ST-003, ST-006 | Hipótese de privacidade derivada de contas/resultados. |
| N-011 | Preservar respostas e manter acesso previsível. | ST-001, ST-004 | Hipótese de qualidade operacional. |
| N-012 | Evoluir regras e conteúdos com consistência. | ST-004, ST-005 | Hipótese de manutenção e controle de mudanças. |

## 10. Solução proposta

Um ambiente acessível por computador e celular reúne o banco de questões, simulados, gabaritos comentados, estatísticas, fórum e autenticação. O estudante seleciona conteúdos, pratica e recebe devolutiva. A administração mantém o catálogo; professores podem revisar explicações mediante autorização proposta. A coordenação poderá consultar agregados somente após decisão sobre autorização e proteção de grupos pequenos.

## 11. Escopo do sistema

O produto é especificado em nível conceitual. O recorte inicial proposto de simulados usa questões objetivas de alternativa única para viabilizar critérios inequívocos de correção. Não se afirma que essa tipologia represente toda a prova oficial. Conteúdos discursivos e outras tipologias exigem decisão futura. A referência web/mobile admite inicialmente interface web responsiva; aplicativo nativo permanece uma alternativa não aprovada.

## 12. Funcionalidades contempladas

Cadastro e autenticação; consulta com filtros; prática individual proposta; configuração e execução de simulados; envio de respostas; correção objetiva proposta; gabarito comentado; estatísticas por área; histórico proposto; discussões por questão; manutenção de conteúdo e permissões; edição limitada de perfil proposta. Ver [RF](../04-requisitos/requisitos-funcionais.md) e [backlog](../05-backlog/backlog-priorizado.md).

## 13. Funcionalidades fora do escopo

Desenvolvimento frontend/backend, APIs executáveis, banco de dados operacional, hospedagem de aplicação e testes de produto na M1. Também não estão aprovados inscrição oficial no ENADE, emissão de notas oficiais, pagamentos, rankings públicos, integração institucional automática, aplicativo nativo, funcionamento offline ou correção automática de respostas discursivas. Protótipos e demais diagramas citados no projeto geral ficam fora deste recorte da P1.

## 14. Premissas

O grupo terá acesso a representantes reais dos públicos; materiais poderão ser utilizados com origem identificada e permissões verificadas; haverá disponibilidade para revisão pedagógica; regras de acesso aos resultados serão acordadas antes de implementação. São condições a confirmar, não compromissos já obtidos de participantes ou da instituição.

## 15. Restrições

A P1 é documental, com quatro critérios de 0,5 ponto. A data final histórica da M1 é 01/11/2026. Não há tecnologia, capacidade de hospedagem, orçamento, metas operacionais ou participantes formalmente aprovados. Dados identificáveis de entrevistas não devem integrar o repositório público. A documentação não adota licença sem autorização.

## 16. Riscos identificados

| Risco | Efeito | Tratamento proposto | Estado |
|---|---|---|---|
| Ausência de entrevistas | Solução baseada somente em hipóteses | Aplicar roteiros e devolver a síntese aos participantes | Coleta pendente |
| Prazo da M1 já encerrado | Entrega fora do período informado | Registrar datas reais e consultar a situação no AVA | Submissão pendente |
| Gabaritos incorretos | Feedback pedagógico inadequado | Revisão docente e versionamento de conteúdo | Política proposta |
| Exposição de resultados | Uso inadequado de dados pessoais | Acesso individual e agregados condicionados | Governança pendente |
| Simulado inconsistente após edição | Resultado não reproduzível | Fixar versões de questões/gabaritos por tentativa | Regra proposta |
| Expansão indevida do escopo | Prejuízo à qualidade dos entregáveis | Separar M1 documental e produto futuro | Separação documentada |
| Falta de acessibilidade | Exclusão de participantes | Validar fluxos com teclado e tecnologia assistiva | Meta proposta |

## 17. Benefícios esperados

Espera-se facilitar a localização de material, apoiar estudo com foco nas dificuldades e estimular discussão pedagógica. Para o grupo, espera-se uma especificação revisável e rastreável. Não há evidência empírica de aumento de notas, adesão ou satisfação, e nenhum percentual de melhoria é afirmado.

## 18. Critérios de sucesso

Para a preparação documental: oito entregáveis localizáveis; cada RF ligado a fonte, necessidade, história e caso de uso; RNF mensuráveis; três diagramas renderizados; links válidos; ausência de afirmações falsas de conclusão. Para a conclusão acadêmica: entrevistas reais, validação registrada, identificação do grupo, acesso do professor e submissão efetiva. Para o produto futuro: êxito nas tarefas de estudo e adequação pedagógica a medir em avaliação posterior; metas dependem dos stakeholders.

## 19. Glossário

| Termo | Definição adotada |
|---|---|
| ENADE | Exame Nacional de Desempenho dos Estudantes. |
| Stakeholder | Parte interessada que influencia ou é afetada pelo projeto. |
| RF / RNF / RN | Requisito funcional / não funcional / regra de negócio. |
| M1 | Marco acadêmico da Sprint 1, com entregas documentais. |
| Simulado / tentativa | Conjunto selecionado para prática / execução específica desse conjunto por um estudante. |
| Formação geral / componente específico | Classificação adotada no material-base para organização das questões. |
| Gabarito comentado | Alternativa correta acompanhada de explicação pedagógica revisada. |
| MoSCoW | Priorização em Must Have, Should Have, Could Have e Won't Have nesta fase. |
| Versão da questão | Registro estável de enunciado, alternativas, classificação e gabarito usado em uma tentativa. |

## 20. Referências

Consultar o [catálogo de fontes e divergências](../../referencias/README.md). F01 sustenta o problema e os seis módulos; F02 define a P1; F03 fornece o rascunho reaproveitado; F04 contextualiza o exame. Detalhamentos analíticos são propostas até aprovação registrada.
