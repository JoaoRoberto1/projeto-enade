# Requisitos funcionais

**Versão 2.0 · 04/11/2026 · 20 requisitos · Nenhum requisito validado com stakeholders.**

Fontes: [catálogo F01–F06](../../referencias/README.md). A indicação de base documental identifica a capacidade descrita; os detalhes desta especificação continuam propostos. Must/Should/Could são prioridades do produto futuro, não implementação na M1. IDs antigos RF-01…RF-18 foram normalizados; RF-019 e RF-020 explicitam perfil e envio de respostas.

Regras: [RN](regras-negocio.md). Qualidade transversal: [RNF](requisitos-nao-funcionais.md). [Rastreabilidade](matriz-rastreabilidade.md).

## RF-001 — Cadastrar conta de estudante

- **Descrição:** Permitir cadastro de estudante com nome de exibição, e-mail de acesso e senha; campos mínimos propostos, sem matrícula obrigatória.
- **Ator:** Estudante.
- **Pré-condições:** Pessoa sem conta para o e-mail informado; serviço disponível.
- **Fluxo principal/comportamento:** Informar os campos; validar formato e preenchimento; verificar unicidade; registrar conta com papel Estudante, sem conceder papel administrativo.
- **Pós-condições:** Conta criada uma única vez ou cadastro recusado sem registro parcial.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Dados válidos criam uma conta Estudante; e-mail já registrado não cria duplicata; campos ausentes recebem indicação específica; cadastro nunca permite selecionar papel privilegiado.
- **Fonte/fundamento:** F01 p. 4; campos e unicidade propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-012.
- **Rastreabilidade:** N-006; UC-013.

## RF-002 — Autenticar e encerrar sessão

- **Descrição:** Autenticar uma conta ativa por credenciais e permitir encerrar a sessão atual.
- **Ator:** Estudante, Professor, Coordenador, Administrador.
- **Pré-condições:** Conta previamente cadastrada e ativa para entrar; sessão válida para sair.
- **Fluxo principal/comportamento:** Receber credenciais; validar conta; iniciar sessão associada aos papéis autorizados; ao sair, invalidar a sessão atual.
- **Pós-condições:** Sessão válida para a conta autenticada ou acesso negado; após saída, sessão inutilizável.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Credenciais corretas permitem acesso; credenciais incorretas ou conta inativa geram mensagem genérica e não criam sessão; uma requisição que reutilize a sessão encerrada é recusada.
- **Fonte/fundamento:** F01 p. 4; encerramento e papéis detalhados propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-012.
- **Rastreabilidade:** N-006; UC-001.

## RF-003 — Consultar e filtrar banco de questões

- **Descrição:** Listar questões publicadas e permitir filtros por ano, curso, área e componente, combinados por interseção.
- **Ator:** Estudante, Professor.
- **Pré-condições:** Usuário autenticado; catálogo disponível, podendo estar vazio.
- **Fluxo principal/comportamento:** Exibir catálogo; escolher valores dos filtros; retornar somente itens publicados que atendam a todos os filtros escolhidos; abrir o enunciado selecionado.
- **Pós-condições:** Lista e detalhes exibidos sem alterar questões ou tentativas.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Uma questão que não satisfaça qualquer filtro não aparece; limpar filtros restaura o catálogo publicado; combinação sem itens mostra lista vazia; rascunhos e arquivadas não aparecem em novas consultas.
- **Fonte/fundamento:** F01 p. 4; combinação e acesso autenticado propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-002, RN-003.
- **Rastreabilidade:** N-001; UC-002.

## RF-004 — Responder questão individual

- **Descrição:** Registrar uma alternativa em uma tentativa individual de estudo de questão objetiva publicada.
- **Ator:** Estudante.
- **Pré-condições:** Estudante autenticado; questão publicada de escolha única; tentativa individual aberta.
- **Fluxo principal/comportamento:** Selecionar alternativa; enviar; validar pertencimento da alternativa; salvar resposta e versão da questão; concluir a tentativa individual.
- **Pós-condições:** Resposta vinculada ao estudante e à versão consultada; feedback liberado conforme RN-006.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Uma alternativa válida é registrada; alternativa de outra questão ou envio sem seleção é recusado; repetição da mesma confirmação não duplica a tentativa; nova prática exige nova tentativa.
- **Fonte/fundamento:** F03 RF-04; proposta derivada do banco de F01 p. 4.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-006, RN-012.
- **Rastreabilidade:** N-002; UC-003.

## RF-005 — Consultar gabarito comentado

- **Descrição:** Exibir alternativa correta, explicação pedagógica e referência da versão correspondente à tentativa; professor revisor acessa também o contexto editorial autorizado.
- **Ator:** Estudante, Professor.
- **Pré-condições:** Estudante com tentativa individual respondida ou simulado encerrado; ou professor autorizado para revisão.
- **Fluxo principal/comportamento:** Verificar contexto e autorização; recuperar gabarito e comentário da versão; apresentar explicação e origem.
- **Pós-condições:** Devolutiva exibida sem modificar a resposta ou pontuação registrada.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Simulado em andamento não revela gabarito nem por acesso direto; encerrado permite ver comentários de todas as questões, inclusive não respondidas; tentativa antiga usa sua própria versão; professor sem autorização editorial não contorna a restrição de estudante.
- **Fonte/fundamento:** F01 p. 4; momento de liberação proposto.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-006, RN-011.
- **Rastreabilidade:** N-003; UC-004.

## RF-006 — Configurar simulado

- **Descrição:** Configurar um conjunto de questões objetivas com filtros, quantidade positiva e duração positiva em minutos antes do início.
- **Ator:** Estudante.
- **Pré-condições:** Estudante autenticado; catálogo publicado disponível.
- **Fluxo principal/comportamento:** Informar filtros, quantidade e duração; verificar disponibilidade; selecionar questões distintas; confirmar configuração sem iniciar a contagem antes do comando de início.
- **Pós-condições:** Configuração válida pronta para iniciar ou rejeitada com motivo.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Quantidade maior que o catálogo elegível é recusada sem criar tentativa; zero ou valor negativo de quantidade/duração é recusado; seleção não contém questões repetidas; duração final é confirmada antes do início, incluindo eventual adaptação autorizada.
- **Fonte/fundamento:** F01 p. 4; parâmetros e seleção propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-002, RN-004, RN-010.
- **Rastreabilidade:** N-002; UC-005.

## RF-007 — Executar e encerrar simulado cronometrado

- **Descrição:** Iniciar uma tentativa, apresentar questões e tempo restante e encerrá-la por confirmação do estudante ou expiração.
- **Ator:** Estudante.
- **Pré-condições:** Configuração RF-006 válida; estudante autenticado; início confirmado.
- **Fluxo principal/comportamento:** Fixar questões e gabaritos; registrar início e prazo; exibir cronômetro; aceitar respostas por RF-020; confirmar conclusão manual ou encerrar ao atingir o prazo; acionar RF-008 uma vez.
- **Pós-condições:** Tentativa encerrada com respostas aceitas até o limite e resultado calculável.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Recarregar a tela não reinicia o prazo; relógio local alterado não muda o limite; no instante do prazo a tentativa está encerrada; conclusão manual exige confirmação; reenvio do pedido de conclusão não gera segundo resultado.
- **Fonte/fundamento:** F01 p. 4; prazo no servidor e encerramento propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-004, RN-007, RN-010.
- **Rastreabilidade:** N-002; UC-005.

## RF-008 — Corrigir simulado e apresentar resultado

- **Descrição:** Comparar respostas aceitas com o gabarito fixado e apresentar acertos, erros, omissões e percentual do simulado.
- **Ator:** Estudante.
- **Pré-condições:** Tentativa objetiva encerrada, com pelo menos uma questão e versões preservadas.
- **Fluxo principal/comportamento:** Ler respostas finais; classificar cada questão como acerto, erro ou omissão; calcular percentual segundo RN-005; registrar e apresentar resumo.
- **Pós-condições:** Resultado associado à tentativa, reproduzível a partir dos dados preservados.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Em 10 questões com 6 acertos, 3 erros e 1 omissão, apresentar 60%; a soma das categorias é 10; nova execução da correção não duplica resultados; edição posterior do catálogo não muda a nota histórica.
- **Fonte/fundamento:** F03 RF-08; proposta de correção objetiva derivada de F01 p. 4.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-005, RN-007, RN-010.
- **Rastreabilidade:** N-003; UC-005.

## RF-009 — Consultar histórico pessoal

- **Descrição:** Listar simulados encerrados do próprio estudante por data de encerramento decrescente e permitir consultar seus detalhes.
- **Ator:** Estudante.
- **Pré-condições:** Estudante autenticado; existência de tentativas não é obrigatória.
- **Fluxo principal/comportamento:** Identificar titular; recuperar tentativas encerradas; apresentar data, filtros, duração efetiva e resultado; abrir detalhes escolhidos.
- **Pós-condições:** Histórico pessoal exibido sem disponibilizar dados de outro estudante.
- **Prioridade:** Should Have.
- **Critérios de aceitação:** A lista vazia informa ausência de simulados; tentativas em andamento não são tratadas como resultado final; alterar o identificador de uma tentativa não permite acessar histórico alheio.
- **Fonte/fundamento:** F03 RF-09; proposta derivada das estatísticas.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-009, RN-010.
- **Rastreabilidade:** N-004; UC-006.

## RF-010 — Visualizar estatísticas pessoais por área

- **Descrição:** Apresentar gráficos e tabela textual de desempenho por área a partir dos simulados encerrados do estudante.
- **Ator:** Estudante.
- **Pré-condições:** Estudante autenticado; histórico pode estar vazio.
- **Fluxo principal/comportamento:** Agrupar itens de simulados encerrados por área da versão usada; somar acertos e total de itens; calcular taxa ponderada; exibir gráfico, legenda, contagens e tabela.
- **Pós-condições:** Indicadores exibidos com população e período identificados; nenhuma comparação pública individual.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Área com 3 acertos em 5 itens mostra 60%; ao agregar tentativas usar soma dos acertos dividida pela soma dos itens, sem média simples de percentuais; área sem itens mostra “sem dados”; tentativas abertas e práticas individuais ficam fora do cálculo proposto.
- **Fonte/fundamento:** F01 p. 4; cálculo e população considerados propostos.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-005, RN-009, RN-010.
- **Rastreabilidade:** N-004; UC-006.

## RF-011 — Ler e publicar discussão por questão

- **Descrição:** Exibir a discussão de uma questão e registrar comentários textuais de usuários autenticados.
- **Ator:** Estudante, Professor.
- **Pré-condições:** Usuário autenticado; questão publicada; acesso ao fórum fora da execução de um simulado.
- **Fluxo principal/comportamento:** Abrir discussão; exibir comentários visíveis; digitar texto; validar conteúdo não vazio; publicar com autoria de exibição, questão e data.
- **Pós-condições:** Comentário associado à questão ou recusado sem publicação.
- **Prioridade:** Should Have.
- **Critérios de aceitação:** Texto apenas com espaços é recusado; comentário publicado aparece somente na questão escolhida; comentário oculto não aparece; durante simulado em andamento a discussão das questões da tentativa não é disponibilizada para evitar revelação de respostas.
- **Fonte/fundamento:** F01 p. 4; autoria e condições de publicação propostas.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-006, RN-008, RN-012.
- **Rastreabilidade:** N-005; UC-007.

## RF-012 — Moderar discussões

- **Descrição:** Ocultar comentário com justificativa e registrar a ação administrativa.
- **Ator:** Administrador.
- **Pré-condições:** Administrador autenticado e autorizado; comentário existente.
- **Fluxo principal/comportamento:** Selecionar comentário; informar motivo conforme política aprovada; confirmar ocultação; registrar autor da ação, momento e motivo.
- **Pós-condições:** Comentário invisível no fórum comum; registro preservado para revisão autorizada.
- **Prioridade:** Should Have.
- **Critérios de aceitação:** Motivo em branco impede ocultação; usuário não administrador não executa a ação; a mesma ocultação não multiplica eventos de mudança; conteúdo oculto fica inacessível aos leitores comuns também por acesso direto.
- **Fonte/fundamento:** F03 RF-12; proposta de governança do fórum.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-008, RN-012.
- **Rastreabilidade:** N-005; UC-011.

## RF-013 — Administrar questões

- **Descrição:** Cadastrar rascunhos, editar conteúdo, publicar versões revisadas e arquivar questões.
- **Ator:** Administrador.
- **Pré-condições:** Administrador autorizado; classificações e origem informadas para publicação.
- **Fluxo principal/comportamento:** Criar ou editar rascunho; registrar enunciado, alternativas, classificação e fonte; vincular revisão de gabarito; publicar versão elegível; arquivar quando necessário.
- **Pós-condições:** Versão publicada disponível para novas consultas ou arquivada sem destruir referências históricas.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Publicação sem gabarito revisado ou classificação é recusada; arquivada sai de novos simulados; alterar questão já usada cria outra versão, preservando a tentativa anterior; estudante não pode publicar.
- **Fonte/fundamento:** F02; F03 RF-13; operações detalhadas propostas.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-002, RN-003, RN-010, RN-011, RN-012.
- **Rastreabilidade:** N-008; UC-010.

## RF-014 — Revisar gabaritos e comentários pedagógicos

- **Descrição:** Permitir que professor autorizado revise a alternativa correta e a explicação; permitir ao administrador manter o rascunho e publicar após revisão.
- **Ator:** Professor, Administrador.
- **Pré-condições:** Questão em rascunho; conta com permissão editorial correspondente.
- **Fluxo principal/comportamento:** Administrador prepara gabarito/comentário; professor registra revisão aprovada ou ajustes; sistema vincula revisor, data e versão; administrador publica via RF-013 quando elegível.
- **Pós-condições:** Revisão rastreável para a versão; qualquer alteração de conteúdo invalida a aprovação dessa nova versão.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Administrador sem papel de professor não simula aprovação pedagógica; gabarito sem explicação não é aprovável; edição após revisão exige nova revisão; tentativas antigas mantêm o gabarito fixado.
- **Fonte/fundamento:** F03 RF-14; apoio docente em F01 p. 7; fluxo editorial proposto.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-003, RN-010, RN-011, RN-012.
- **Rastreabilidade:** N-007; UC-008.

## RF-015 — Consultar indicadores agregados do curso

- **Descrição:** Consultar totais e taxas por área do curso sob sua autorização, sem nomes ou resultados individuais.
- **Ator:** Coordenador.
- **Pré-condições:** Coordenador autenticado; escopo institucional e limiar de grupo pequeno aprovados e configurados; caso contrário, recurso indisponível.
- **Fluxo principal/comportamento:** Verificar curso autorizado; selecionar período; agregar simulados encerrados; suprimir grupos abaixo do limiar; exibir contagens e taxas sem identificação pessoal.
- **Pós-condições:** Painel agregado exibido apenas dentro do escopo permitido.
- **Prioridade:** Should Have.
- **Critérios de aceitação:** Curso fora da autorização é recusado; painel não contém links a estudantes; grupo abaixo do limiar não exibe contagem nem taxa; limiar ausente mantém painel bloqueado; cálculo usa a mesma fórmula ponderada de RF-010.
- **Fonte/fundamento:** F01 p. 7; F03 RF-15; acesso agregado é proposta.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-005, RN-009, RN-012.
- **Rastreabilidade:** N-004; UC-009.

## RF-016 — Administrar contas e papéis

- **Descrição:** Atribuir e revogar papéis de contas existentes e ativar ou desativar acesso administrativo conforme autorização.
- **Ator:** Administrador.
- **Pré-condições:** Administrador autenticado; conta-alvo existente; concessão justificada.
- **Fluxo principal/comportamento:** Selecionar conta; consultar papéis atuais; confirmar mudança; verificar proteção do último administrador; registrar ação e aplicar permissões vigentes.
- **Pós-condições:** Papéis atualizados e auditados; próximas operações obedecem à autorização atual.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Estudante não consegue promover a própria conta; revogação impede a próxima operação restrita mesmo em sessão existente; remoção/desativação do último administrador ativo é recusada; mudança não apaga resultados.
- **Fonte/fundamento:** F02; F03 RF-16; permissões detalhadas propostas.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-009, RN-012.
- **Rastreabilidade:** N-008; UC-012.

## RF-017 — Pesquisar questões por texto

- **Descrição:** Pesquisar trecho do enunciado das questões publicadas, combinado com os filtros do catálogo.
- **Ator:** Estudante, Professor.
- **Pré-condições:** Usuário autenticado; catálogo disponível.
- **Fluxo principal/comportamento:** Informar trecho; comparar ignorando diferenças entre maiúsculas e minúsculas; aplicar interseção com filtros; retornar resultados.
- **Pós-condições:** Resultados apresentados sem alterar catálogo ou dados pessoais.
- **Prioridade:** Could Have.
- **Critérios de aceitação:** Busca por “cidadania” encontra enunciado que contenha “Cidadania”; termo vazio equivale à consulta sem texto; termo e filtros sem coincidência retornam lista vazia; não pesquisa conteúdo de rascunhos.
- **Fonte/fundamento:** F03 RF-17; hipótese adicional ao filtro de F01.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-002.
- **Rastreabilidade:** N-001; UC-002.

## RF-018 — Exibir proveniência do conteúdo

- **Descrição:** Apresentar fonte da questão e, quando o gabarito for liberado, responsabilidade e data da revisão do comentário.
- **Ator:** Estudante, Professor.
- **Pré-condições:** Questão publicada; acesso ao comentário condicionado à RN-006.
- **Fluxo principal/comportamento:** Mostrar origem, ano, curso/área e identificação de material oficial ou autoral; junto ao comentário, mostrar atribuição do revisor segundo política de exposição aprovada.
- **Pós-condições:** Usuário distingue origem da questão e autoria/revisão pedagógica.
- **Prioridade:** Should Have.
- **Critérios de aceitação:** Questão sem fonte não é publicável; material autoral não recebe identificação de prova oficial; origem aparece antes da resposta sem revelar gabarito; referência do comentário acompanha a versão exibida.
- **Fonte/fundamento:** F03 RF-18; derivação de F01 p. 4 e 10.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-003, RN-006, RN-011.
- **Rastreabilidade:** N-001; UC-002, UC-004.

## RF-019 — Editar dados do próprio perfil

- **Descrição:** Permitir editar o nome de exibição da própria conta; estudante também pode indicar curso de interesse sem obter novas permissões.
- **Ator:** Estudante, Professor, Coordenador, Administrador.
- **Pré-condições:** Usuário autenticado; perfil próprio.
- **Fluxo principal/comportamento:** Abrir perfil; editar campos permitidos; validar nome não vazio; salvar; manter e-mail, papéis e autorizações fora desse fluxo.
- **Pós-condições:** Preferências de exibição atualizadas; dados de tentativas e papéis preservados.
- **Prioridade:** Could Have.
- **Critérios de aceitação:** Nome vazio é recusado; conta alheia não pode ser editada; alteração do curso de interesse não concede acesso a indicadores nem altera classificação de tentativas antigas; este fluxo não altera senha, e-mail ou papel.
- **Fonte/fundamento:** F02 solicita tratar gestão de perfil como proposta.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-012.
- **Rastreabilidade:** N-006; UC-014.

## RF-020 — Registrar respostas de simulado

- **Descrição:** Registrar e substituir a alternativa escolhida de cada questão enquanto a tentativa estiver aberta e dentro do prazo.
- **Ator:** Estudante.
- **Pré-condições:** Estudante titular; tentativa em andamento; questão pertencente à tentativa.
- **Fluxo principal/comportamento:** Selecionar alternativa; enviar; conferir autorização, versão e horário de recebimento no servidor; confirmar gravação; permitir alteração até o encerramento.
- **Pós-condições:** Última resposta aceita por questão fica associada à tentativa; envio rejeitado não altera a resposta válida anterior.
- **Prioridade:** Must Have.
- **Critérios de aceitação:** Envio recebido no prazo ou depois dele é recusado; alternativa alheia e tentativa de outro titular são recusadas; repetir o mesmo envio não cria respostas duplicadas; falha de rede não mostra confirmação de gravação; nova escolha aceita antes do prazo substitui a anterior.
- **Fonte/fundamento:** F02 e detalhamento proposto de F03 RF-07.
- **Estado de validação:** Proposto — não validado; capacidade com base documental quando indicada na fonte.
- **Regras relacionadas:** RN-001, RN-007, RN-010, RN-012.
- **Rastreabilidade:** N-002; UC-005.
