# Backlog priorizado do produto

**Versão 2.0 · 04/11/2026 · 17 histórias propostas · Nenhuma implementação iniciada.**

O backlog descreve o produto futuro. A Sprint 1/M1 possui [planejamento documental separado](../07-sprint/planejamento-m1.md). Prioridades e agrupamentos abaixo não foram aprovados por stakeholders. RF e fontes estão em [requisitos funcionais](../04-requisitos/requisitos-funcionais.md).

## Critério MoSCoW e sequência proposta

- **Must Have:** consulta, prática, feedback e suas dependências de conteúdo e segurança.
- **Should Have:** histórico, transparência de origem, agregados e fórum, após o ciclo principal.
- **Could Have:** busca textual e edição de perfil.
- **Won't Have nesta fase:** qualquer implementação na M1; no recorte inicial do produto ficam de fora app nativo/offline, pagamentos, rankings públicos e correção discursiva. São exclusões explícitas, sem histórias aprovadas ou requisitos artificiais.

FUT-01, FUT-02 e FUT-03 são agrupamentos de sprints futuras sem datas, responsáveis, capacidade ou compromisso de execução. Não equivalem à M1. A ordem numérica dos IDs preserva o pacote anterior; a sequência técnica respeita as dependências.

| ID | Épico | Título | Prioridade | RF | Sprint proposta |
|---|---|---|---|---|---|
| US-001 | EP-001 — Identidade e acesso | Acessar conta | Must Have | RF-001, RF-002 | FUT-01 |
| US-002 | EP-002 — Banco de questões | Consultar e filtrar questões | Must Have | RF-003 | FUT-01 |
| US-003 | EP-003 — Prática e simulados | Praticar uma questão | Must Have | RF-004 | FUT-01 |
| US-004 | EP-004 — Feedback e desempenho | Compreender o gabarito | Must Have | RF-005 | FUT-01 |
| US-005 | EP-003 — Prática e simulados | Configurar simulado | Must Have | RF-006 | FUT-01 |
| US-006 | EP-003 — Prática e simulados | Realizar simulado cronometrado | Must Have | RF-007, RF-020 | FUT-01 |
| US-007 | EP-004 — Feedback e desempenho | Receber resultado do simulado | Must Have | RF-008 | FUT-01 |
| US-008 | EP-005 — Governança de conteúdo | Manter questões e gabaritos | Must Have | RF-013, RF-014 | FUT-01 |
| US-009 | EP-001 — Identidade e acesso | Gerenciar papéis | Must Have | RF-016 | FUT-01 |
| US-010 | EP-004 — Feedback e desempenho | Analisar desempenho por área | Must Have | RF-010 | FUT-01 |
| US-011 | EP-004 — Feedback e desempenho | Rever histórico pessoal | Should Have | RF-009 | FUT-02 |
| US-012 | EP-004 — Feedback e desempenho | Acompanhar agregados do curso | Should Have | RF-015 | FUT-02 |
| US-013 | EP-006 — Discussão pedagógica | Discutir uma questão | Should Have | RF-011 | FUT-02 |
| US-014 | EP-006 — Discussão pedagógica | Moderar discussões | Should Have | RF-012 | FUT-02 |
| US-015 | EP-002 — Banco de questões | Buscar por trecho do enunciado | Could Have | RF-017 | FUT-03 |
| US-016 | EP-005 — Governança de conteúdo | Consultar origem do material | Should Have | RF-018 | FUT-02 |
| US-017 | EP-001 — Identidade e acesso | Editar perfil próprio | Could Have | RF-019 | FUT-03 |

## US-001 — Acessar conta

- **Épico:** EP-001 — Identidade e acesso.
- **História:** Como estudante, quero cadastrar minha conta, entrar e sair com segurança, para manter meu acesso pessoal ao estudo.
- **Critérios de aceitação:** Dados válidos criam uma conta Estudante; e-mail já registrado não cria duplicata; campos ausentes recebem indicação específica; cadastro nunca permite selecionar papel privilegiado. Credenciais corretas permitem acesso; credenciais incorretas ou conta inativa geram mensagem genérica e não criam sessão; uma requisição que reutilize a sessão encerrada é recusada.
- **Prioridade:** Must Have.
- **Justificativa:** Sustenta tentativas e resultados pessoais.
- **Dependências:** nenhuma história anterior; política de cadastro a validar.
- **Requisitos relacionados:** RF-001, RF-002.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-002 — Consultar e filtrar questões

- **Épico:** EP-002 — Banco de questões.
- **História:** Como estudante, quero consultar questões por ano, curso, área e componente, para encontrar conteúdo pertinente à minha preparação.
- **Critérios de aceitação:** Uma questão que não satisfaça qualquer filtro não aparece; limpar filtros restaura o catálogo publicado; combinação sem itens mostra lista vazia; rascunhos e arquivadas não aparecem em novas consultas.
- **Prioridade:** Must Have.
- **Justificativa:** Ataca diretamente a dispersão de materiais.
- **Dependências:** US-001, US-008.
- **Requisitos relacionados:** RF-003.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-003 — Praticar uma questão

- **Épico:** EP-003 — Prática e simulados.
- **História:** Como estudante, quero responder uma questão objetiva individual, para verificar minha compreensão.
- **Critérios de aceitação:** Uma alternativa válida é registrada; alternativa de outra questão ou envio sem seleção é recusado; repetição da mesma confirmação não duplica a tentativa; nova prática exige nova tentativa.
- **Prioridade:** Must Have.
- **Justificativa:** Oferece prática simples antes do simulado.
- **Dependências:** US-002.
- **Requisitos relacionados:** RF-004.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-004 — Compreender o gabarito

- **Épico:** EP-004 — Feedback e desempenho.
- **História:** Como estudante, quero consultar gabarito comentado no momento permitido, para entender o raciocínio da solução.
- **Critérios de aceitação:** Simulado em andamento não revela gabarito nem por acesso direto; encerrado permite ver comentários de todas as questões, inclusive não respondidas; tentativa antiga usa sua própria versão; professor sem autorização editorial não contorna a restrição de estudante.
- **Prioridade:** Must Have.
- **Justificativa:** Feedback pedagógico é parte central do problema.
- **Dependências:** US-003, US-008.
- **Requisitos relacionados:** RF-005.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-005 — Configurar simulado

- **Épico:** EP-003 — Prática e simulados.
- **História:** Como estudante, quero escolher filtros, quantidade e duração do simulado, para praticar conteúdos adequados ao meu contexto.
- **Critérios de aceitação:** Quantidade maior que o catálogo elegível é recusada sem criar tentativa; zero ou valor negativo de quantidade/duração é recusado; seleção não contém questões repetidas; duração final é confirmada antes do início, incluindo eventual adaptação autorizada.
- **Prioridade:** Must Have.
- **Justificativa:** Prepara a jornada de prática temporizada.
- **Dependências:** US-002.
- **Requisitos relacionados:** RF-006.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-006 — Realizar simulado cronometrado

- **Épico:** EP-003 — Prática e simulados.
- **História:** Como estudante, quero enviar respostas e acompanhar o prazo do simulado, para praticar com limite de tempo previsível.
- **Critérios de aceitação:** Recarregar a tela não reinicia o prazo; relógio local alterado não muda o limite; no instante do prazo a tentativa está encerrada; conclusão manual exige confirmação; reenvio do pedido de conclusão não gera segundo resultado. Envio recebido no prazo ou depois dele é recusado; alternativa alheia e tentativa de outro titular são recusadas; repetir o mesmo envio não cria respostas duplicadas; falha de rede não mostra confirmação de gravação; nova escolha aceita antes do prazo substitui a anterior.
- **Prioridade:** Must Have.
- **Justificativa:** É uma das capacidades centrais dos slides.
- **Dependências:** US-005.
- **Requisitos relacionados:** RF-007, RF-020.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-007 — Receber resultado do simulado

- **Épico:** EP-004 — Feedback e desempenho.
- **História:** Como estudante, quero consultar acertos, erros, omissões e percentual ao encerrar, para avaliar minha tentativa.
- **Critérios de aceitação:** Em 10 questões com 6 acertos, 3 erros e 1 omissão, apresentar 60%; a soma das categorias é 10; nova execução da correção não duplica resultados; edição posterior do catálogo não muda a nota histórica.
- **Prioridade:** Must Have.
- **Justificativa:** Completa o ciclo de prática e retorno.
- **Dependências:** US-006, US-008.
- **Requisitos relacionados:** RF-008.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-008 — Manter questões e gabaritos

- **Épico:** EP-005 — Governança de conteúdo.
- **História:** Como administrador, quero gerenciar versões de questões e submeter comentários à revisão do professor, para oferecer material confiável para estudo.
- **Critérios de aceitação:** Publicação sem gabarito revisado ou classificação é recusada; arquivada sai de novos simulados; alterar questão já usada cria outra versão, preservando a tentativa anterior; estudante não pode publicar. Administrador sem papel de professor não simula aprovação pedagógica; gabarito sem explicação não é aprovável; edição após revisão exige nova revisão; tentativas antigas mantêm o gabarito fixado.
- **Prioridade:** Must Have.
- **Justificativa:** Consulta e correção dependem de conteúdo elegível.
- **Dependências:** US-001, US-009.
- **Requisitos relacionados:** RF-013, RF-014.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-009 — Gerenciar papéis

- **Épico:** EP-001 — Identidade e acesso.
- **História:** Como administrador, quero conceder e revogar papéis de contas, para limitar operações às pessoas autorizadas.
- **Critérios de aceitação:** Estudante não consegue promover a própria conta; revogação impede a próxima operação restrita mesmo em sessão existente; remoção/desativação do último administrador ativo é recusada; mudança não apaga resultados.
- **Prioridade:** Must Have.
- **Justificativa:** Dependência de segurança da administração.
- **Dependências:** US-001.
- **Requisitos relacionados:** RF-016.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-010 — Analisar desempenho por área

- **Épico:** EP-004 — Feedback e desempenho.
- **História:** Como estudante, quero consultar gráfico e tabela de meus resultados por área, para identificar conteúdos que exigem revisão.
- **Critérios de aceitação:** Área com 3 acertos em 5 itens mostra 60%; ao agregar tentativas usar soma dos acertos dividida pela soma dos itens, sem média simples de percentuais; área sem itens mostra “sem dados”; tentativas abertas e práticas individuais ficam fora do cálculo proposto.
- **Prioridade:** Must Have.
- **Justificativa:** Atende à necessidade explícita de estatísticas.
- **Dependências:** US-007.
- **Requisitos relacionados:** RF-010.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-01, planejamento futuro não aprovado.

## US-011 — Rever histórico pessoal

- **Épico:** EP-004 — Feedback e desempenho.
- **História:** Como estudante, quero consultar simulados anteriores e seus detalhes, para acompanhar minha evolução.
- **Critérios de aceitação:** A lista vazia informa ausência de simulados; tentativas em andamento não são tratadas como resultado final; alterar o identificador de uma tentativa não permite acessar histórico alheio.
- **Prioridade:** Should Have.
- **Justificativa:** Complementa a devolutiva principal sem impedir uma primeira prática.
- **Dependências:** US-007.
- **Requisitos relacionados:** RF-009.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-02, planejamento futuro não aprovado.

## US-012 — Acompanhar agregados do curso

- **Épico:** EP-004 — Feedback e desempenho.
- **História:** Como coordenador, quero consultar indicadores autorizados por área do curso, para planejar apoio pedagógico sem expor indivíduos.
- **Critérios de aceitação:** Curso fora da autorização é recusado; painel não contém links a estudantes; grupo abaixo do limiar não exibe contagem nem taxa; limiar ausente mantém painel bloqueado; cálculo usa a mesma fórmula ponderada de RF-010.
- **Prioridade:** Should Have.
- **Justificativa:** Depende de governança e utilidade dos indicadores.
- **Dependências:** US-009, US-010.
- **Requisitos relacionados:** RF-015.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-02, planejamento futuro não aprovado.

## US-013 — Discutir uma questão

- **Épico:** EP-006 — Discussão pedagógica.
- **História:** Como estudante, quero ler e publicar comentários vinculados às questões, para trocar dúvidas e explicações.
- **Critérios de aceitação:** Texto apenas com espaços é recusado; comentário publicado aparece somente na questão escolhida; comentário oculto não aparece; durante simulado em andamento a discussão das questões da tentativa não é disponibilizada para evitar revelação de respostas.
- **Prioridade:** Should Have.
- **Justificativa:** Módulo previsto, sequenciado após consulta, prática e feedback.
- **Dependências:** US-002, US-014.
- **Requisitos relacionados:** RF-011.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-02, planejamento futuro não aprovado.

## US-014 — Moderar discussões

- **Épico:** EP-006 — Discussão pedagógica.
- **História:** Como administrador, quero ocultar comentários com justificativa, para aplicar a política de convivência.
- **Critérios de aceitação:** Motivo em branco impede ocultação; usuário não administrador não executa a ação; a mesma ocultação não multiplica eventos de mudança; conteúdo oculto fica inacessível aos leitores comuns também por acesso direto.
- **Prioridade:** Should Have.
- **Justificativa:** Deve estar disponível antes da abertura do fórum.
- **Dependências:** US-009.
- **Requisitos relacionados:** RF-012.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-02, planejamento futuro não aprovado.

## US-015 — Buscar por trecho do enunciado

- **Épico:** EP-002 — Banco de questões.
- **História:** Como estudante, quero buscar texto nos enunciados junto com os filtros, para localizar uma questão conhecida.
- **Critérios de aceitação:** Busca por “cidadania” encontra enunciado que contenha “Cidadania”; termo vazio equivale à consulta sem texto; termo e filtros sem coincidência retornam lista vazia; não pesquisa conteúdo de rascunhos.
- **Prioridade:** Could Have.
- **Justificativa:** Conveniência adicional; filtros atendem à necessidade inicial.
- **Dependências:** US-002.
- **Requisitos relacionados:** RF-017.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-03, planejamento futuro não aprovado.

## US-016 — Consultar origem do material

- **Épico:** EP-005 — Governança de conteúdo.
- **História:** Como estudante, quero ver a fonte da questão e a revisão do comentário, para distinguir conteúdo oficial e autoral.
- **Critérios de aceitação:** Questão sem fonte não é publicável; material autoral não recebe identificação de prova oficial; origem aparece antes da resposta sem revelar gabarito; referência do comentário acompanha a versão exibida.
- **Prioridade:** Should Have.
- **Justificativa:** Transparência visível complementa a origem já exigida na publicação.
- **Dependências:** US-002, US-004, US-008.
- **Requisitos relacionados:** RF-018.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-02, planejamento futuro não aprovado.

## US-017 — Editar perfil próprio

- **Épico:** EP-001 — Identidade e acesso.
- **História:** Como estudante, quero editar meu nome de exibição e curso de interesse, para manter minhas preferências de uso atualizadas.
- **Critérios de aceitação:** Nome vazio é recusado; conta alheia não pode ser editada; alteração do curso de interesse não concede acesso a indicadores nem altera classificação de tentativas antigas; este fluxo não altera senha, e-mail ou papel.
- **Prioridade:** Could Have.
- **Justificativa:** Personalização não impede a jornada principal.
- **Dependências:** US-001.
- **Requisitos relacionados:** RF-019.
- **Estado:** Proposta para validação; não implementada.
- **Sprint proposta:** FUT-03, planejamento futuro não aprovado.
