# Fontes e preservação

Versão documental: 2.0, preparada em **04/11/2026**. A Sprint 1 mantém o período histórico **19/10/2026 a 01/11/2026**.

## Catálogo de fontes

| Código | Fonte consultada | Uso e limite |
|---|---|---|
| F01 | [Apresentação original, 10 páginas](originais/apresentacao-enade.pdf), *Projeto de Extensão — ENADE: Engenharia de Requisitos Aplicada ao Contexto Educacional*. Autoria e data não informadas. | Fonte primária: problema (p. 2), objetivo (p. 3), seis módulos (p. 4), metodologia (p. 6), públicos (p. 7) e caráter conceitual (p. 10). |
| F02 | Instruções da P1 fornecidas pelo solicitante no texto anexado à tarefa, consultadas em 04/11/2026. | Unifor, nota 2,0, oito entregáveis, três diagramas exigidos, período, milestone e colaborador obrigatório. Não é ata de aprovação dos stakeholders. |
| F03 | [Pacote anterior — README](originais/pacote-p1/README.md), [DOCX](originais/pacote-p1/Trabalho_P1_ENADE.docx), [PDF](originais/pacote-p1/Trabalho_P1_ENADE.pdf), [backlog CSV](originais/pacote-p1/backlog_priorizado.csv). | Rascunho reaproveitado; não contém entrevistas realizadas. Não representa a versão atual da entrega. |
| F04 | [Inep — Enade](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade), acesso em 04/11/2026. | Contextualização institucional do exame; não aprova este produto. |
| F05 | [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/), acesso em 04/11/2026. | Referência técnica proposta para acessibilidade, sem alegação de conformidade de software. |
| F06 | [PlantUML — distribuição](https://plantuml.com/download) e [layout Smetana](https://plantuml.com/smetana02), acesso em 04/11/2026. | Renderização local dos diagramas com Java e PlantUML; sem aplicação de produto. |
| F07 | [Qconcursos — página inicial](https://www.qconcursos.com/), acesso em 04/11/2026. | Comparação documental de similares; funcionalidades apresentadas publicamente, sem teste autenticado. |
| F08 | [Estuda.com — página inicial](https://estuda.com/), acesso em 04/11/2026. | Comparação documental de similares; funcionalidades apresentadas publicamente, sem teste autenticado. |

## Precedência e divergências

F01 descreve o projeto amplo, incluindo classes, sequência, atividades, protótipos e apresentação (p. 5), com pesos de avaliação diferentes (p. 8). F02 delimita esta **P1**: casos de uso, componentes e implantação, sem desenvolvimento, e quatro critérios de 0,5 ponto. Para a entrega atual prevalece F02; os itens posteriores não são tarefas concluídas nem promessas da M1.

A menção à IEEE 830 na p. 3 de F01 é uma orientação didática do material. Esta documentação organiza requisitos e rastreabilidade, mas não declara certificação ou conformidade normativa integral.

## Integridade das fontes

Os 17 arquivos do pacote extraído foram comparados com `ENADE_P1_Completo.zip` e são idênticos. O pacote e a apresentação foram copiados sem edição para `originais/`. Os arquivos de Downloads permanecem intactos. O [manifesto SHA-256](manifesto-originais.json) permite verificar cada cópia. Nenhum arquivo anterior do repositório foi substituído: a inspeção inicial encontrou apenas `.git`.

Os documentos históricos podem conter identificadores antigos, links de exemplo e pendências superadas. Avalie a versão atual em [docs](../README.md), sem considerar os originais como segunda linha de base. RF-01…RF-18, RN-01…RN-11 e RNF-01…RNF-11 foram normalizados para três dígitos, mantendo a intenção; PB-01…PB-16 tornaram-se US-001…US-016. Novos detalhamentos são identificados como propostas.

Não foi adicionada licença: não havia licença nem autorização específica para defini-la.
