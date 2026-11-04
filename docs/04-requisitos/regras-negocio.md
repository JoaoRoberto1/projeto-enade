# Regras de negócio

**Versão 2.0 · 04/11/2026 · 12 regras propostas, não validadas.**

As regras expressam condições e políticas do produto proposto, não normas oficiais do ENADE. RF descrevem as capacidades que obedecem a essas condições. Base: [F01, F02 e F03](../../referencias/README.md); RN-002 deriva diretamente da classificação de F01, e as demais formalizam hipóteses do recorte.

## RN-001 — Tipologia objetiva do recorte

- **Descrição:** Uma questão objetiva publicável possui enunciado, alternativas não vazias e exatamente uma alternativa correta. Questões anuladas ou sem gabarito confiável não integram novos simulados.
- **Justificativa:** Tornar a correção proposta determinística; o exame oficial não é reduzido a essa tipologia.
- **Requisitos associados:** RF-003, RF-004, RF-006, RF-008, RF-013, RF-014, RF-020.
- **Exceções/limites:** Outras tipologias exigem regra específica aprovada; rascunhos podem estar incompletos.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-002 — Classificação do catálogo

- **Descrição:** Cada versão publicada informa ano de origem, curso, área e componente (Formação Geral ou Componente Específico); filtros combinados selecionam a interseção desses valores.
- **Justificativa:** Viabilizar organização indicada em F01 p. 4.
- **Requisitos associados:** RF-003, RF-006, RF-013, RF-017.
- **Exceções/limites:** Materiais aplicáveis a mais de um curso podem ter múltiplos vínculos, sem duplicar a mesma questão na tentativa.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-003 — Origem e publicação de conteúdo

- **Descrição:** Publicação depende de fonte identificável e verificação da condição de uso; questão oficial e questão autoral são identificadas separadamente.
- **Justificativa:** Garantir proveniência e impedir atribuição indevida ao Inep.
- **Requisitos associados:** RF-003, RF-013, RF-014, RF-018.
- **Exceções/limites:** Material de origem ou condição de uso não esclarecida permanece rascunho.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-004 — Composição do simulado

- **Descrição:** Quantidade e duração são positivas; há questões publicadas distintas suficientes para os filtros. Duração é fixada no início, incluindo adaptações autorizadas antes da tentativa.
- **Justificativa:** Evitar configuração impossível e mudança arbitrária do prazo.
- **Requisitos associados:** RF-006, RF-007.
- **Exceções/limites:** Adaptação por acessibilidade depende de política aprovada; não implica alteração unilateral durante a tentativa.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-005 — Pontuação e agregação

- **Descrição:** Cada item objetivo tem peso unitário: percentual = 100 × acertos / total de questões, exibido com duas casas decimais. Omissões não são acertos; erros são respostas preenchidas incorretas. Agregados dividem a soma de acertos pela soma de itens.
- **Justificativa:** Propor interpretação verificável do desempenho; não equivale a cálculo oficial do ENADE.
- **Requisitos associados:** RF-008, RF-010, RF-015.
- **Exceções/limites:** Conjunto vazio exibe “sem dados”; não dividir por zero. Pesos diferentes e recálculo por anulação posterior dependem de nova decisão.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-006 — Momento de disponibilização do feedback

- **Descrição:** Prática individual libera gabarito após registrar a resposta; simulado libera somente após encerramento. Discussões das questões do simulado ficam indisponíveis ao estudante durante a tentativa.
- **Justificativa:** Preservar o exercício antes de revelar soluções.
- **Requisitos associados:** RF-004, RF-005, RF-011, RF-018.
- **Exceções/limites:** Professor com permissão de revisão acessa comentário no contexto editorial; isso não concede leitura de resultados individuais de estudantes.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-007 — Prazo e imutabilidade do encerramento

- **Descrição:** Prazo = início no servidor + duração confirmada. Uma resposta só é aceita se recebida antes do prazo e antes do encerramento manual. Ao atingir o prazo, a tentativa está encerrada. A última resposta aceita prevalece; encerramento não admite reabertura nesta proposta.
- **Justificativa:** Evitar disputa entre relógio local, envios concorrentes e correção.
- **Requisitos associados:** RF-007, RF-008, RF-020.
- **Exceções/limites:** Falha de rede não concede tempo adicional automático. Retentativa de envio é possível apenas enquanto houver prazo e não garante registro de envio atrasado.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-008 — Publicação e moderação de comentários

- **Descrição:** Somente contas autenticadas publicam texto não vazio em questões publicadas. Administrador pode ocultar conteúdo com motivo registrado conforme política de convivência ainda a aprovar.
- **Justificativa:** Associar discussão ao contexto pedagógico e possibilitar revisão de moderação.
- **Requisitos associados:** RF-011, RF-012.
- **Exceções/limites:** Conteúdo oculto permanece disponível somente à revisão administrativa autorizada; política não definida impede alegar moderação plenamente especificada.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-009 — Titularidade e acesso a resultados

- **Descrição:** Estudante consulta apenas seus dados individuais. Professor não recebe acesso individual por padrão. Coordenador acessa somente agregados de cursos autorizados, com supressão de grupos abaixo de limiar institucional aprovado.
- **Justificativa:** Conciliar acompanhamento com restrição de exposição.
- **Requisitos associados:** RF-009, RF-010, RF-015, RF-016.
- **Exceções/limites:** Sem autorização ou limiar configurado, painel agregado permanece bloqueado. Exceções de acesso individual exigem nova aprovação documentada.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-010 — Preservação de versões e tentativas

- **Descrição:** Tentativa fixa versões de enunciado, classificação e gabarito no início. Alteração posterior gera nova versão para uso futuro. Questões utilizadas são arquivadas, sem remoção que destrua referências históricas.
- **Justificativa:** Permitir reproduzir correção e estatísticas sem mudanças silenciosas.
- **Requisitos associados:** RF-006, RF-007, RF-008, RF-009, RF-010, RF-013, RF-014, RF-020.
- **Exceções/limites:** Retenção e anonimização de dados pessoais seguem política a validar; preservação lógica não autoriza retenção indefinida de identidade.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-011 — Revisão pedagógica por versão

- **Descrição:** Publicação de questão exige comentário e gabarito aprovados por professor autorizado, com identificação de revisor, data e versão. Alterar conteúdo após revisão exige nova aprovação.
- **Justificativa:** Reduzir risco de feedback incorreto e rastrear responsabilidade.
- **Requisitos associados:** RF-005, RF-013, RF-014, RF-018.
- **Exceções/limites:** Administrador somente revisa pedagogicamente se também possuir papel Professor; esse acúmulo precisa de concessão explícita.
- **Estado de validação:** Proposto — não validado com stakeholders.

## RN-012 — Contas e permissões

- **Descrição:** Cadastro inicial concede somente papel Estudante. Apenas administrador gerencia papéis; não é permitido remover o último administrador ativo. Cada operação usa permissões vigentes. Perfil próprio não altera papel, senha, e-mail ou acesso institucional.
- **Justificativa:** Evitar autopromoção e perda de administração.
- **Requisitos associados:** RF-001, RF-002, RF-004, RF-011, RF-012, RF-013, RF-014, RF-015, RF-016, RF-019, RF-020.
- **Exceções/limites:** Provisionamento do primeiro administrador ocorre por procedimento institucional futuro; acumular papéis requer autorização, não cadastro aberto.
- **Estado de validação:** Proposto — não validado com stakeholders.
