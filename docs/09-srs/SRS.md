# Especificação de Requisitos de Software — Sistema de Apoio ao ENADE

**SRS · versão 3.0 · P2 / M2 · 19/11/2026**<br/>
**Autores:** João Roberto de Oliveira Felix e Vinicius Lisboa de Albuquerque<br/>
**Disciplina:** Requisitos e Modelagem de Sistemas — Universidade de Fortaleza (Unifor)

| Controle | Registro |
|---|---|
| Base | P1, versão documental 2.0, commit e810ffd |
| Evolução P2 | Estrutura SRS, 14 casos de uso detalhados, revisão UML e protótipo navegável |
| Sprint acadêmica | M2: 02/11 a 22/11/2026 |
| Preparação registrada | 19/11/2026; não se afirma trabalho executado retroativamente |
| Entrega no AVA | 23/11/2026 às 00h00, America/Sao_Paulo |
| Situação | Especificação proposta; revisão técnica e validação com usuários são atividades distintas |

## 1. Introdução

### 1.1 Propósito

Especificar o comportamento esperado do Sistema de Apoio ao ENADE e fornecer uma base verificável para discutir requisitos, avaliar o protótipo e orientar uma implementação futura. O documento é dirigido ao professor avaliador, integrantes do grupo e representantes dos usuários.

O texto segue a organização acadêmica solicitada da IEEE 830: introdução, descrição geral e requisitos específicos. A IEEE 830-1998 foi substituída pela ISO/IEC/IEEE 29148; sua estrutura é utilizada aqui por exigência da atividade. Não se declara certificação ou conformidade normativa integral.

### 1.2 Escopo do produto e da P2

O produto proposto reúne banco de questões, simulados cronometrados, gabaritos comentados, estatísticas, fórum e autenticação, com administração de conteúdo e usuários. Busca reduzir a dispersão de materiais e oferecer prática com retorno compreensível.

A P2 entrega a especificação, os modelos revisados e um protótipo web navegável. O protótipo usa HTML, CSS e JavaScript com dados fictícios no navegador. Ele demonstra interação e regras selecionadas; o produto futuro exige backend, autenticação real e persistência protegida. Os requisitos de produto abaixo não são certificados pelos testes da demonstração.

Ficam fora do recorte: aplicativo nativo, modo offline de produto, pagamentos, ranking público, correção de respostas discursivas, integração oficial com o Inep, recuperação de senha e operação institucional real.

### 1.3 Definições e abreviaturas

| Termo | Significado neste documento |
|---|---|
| SRS | Especificação de Requisitos de Software |
| RF / RNF / RN | Requisito funcional / não funcional / regra de negócio |
| UC / US / T | Caso de uso / história de usuário / tela de protótipo |
| Stakeholder | Pessoa ou grupo interessado ou afetado pelo sistema |
| Tentativa | Execução individual de uma questão ou de um simulado por um titular |
| Versão | Conjunto preservado de enunciado, alternativas, classificação e gabarito |
| Must / Should / Could | Essencial / importante / desejável no backlog proposto |
| M2 | Marco acadêmico da Sprint 2; não representa implantação de produto |

### 1.4 Referências

- **P1:** [Documento de Visão](../01-visao/documento-visao.md), [stakeholders](../02-stakeholders/identificacao-stakeholders.md), [requisitos e matriz](../04-requisitos/matriz-rastreabilidade.md) e [backlog](../05-backlog/backlog-priorizado.md).
- **Fontes originais:** [catálogo e materiais preservados](../../referencias/README.md).
- **Atividade 2:** enunciado fornecido pelo grupo, transcrito em [atividade-p2.md](../../referencias/atividade-p2.md).
- **IEEE 830-1998:** [registro oficial IEEE](https://ieeexplore.ieee.org/document/720574), DOI 10.1109/IEEESTD.1998.88286; organização histórica solicitada na atividade.
- **ISO/IEC/IEEE 29148:2011:** [registro oficial da norma que substituiu a IEEE 830](https://standards.ieee.org/ieee/29148/5289/).
- **Acessibilidade:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), referência de qualidade já adotada na P1.

### 1.5 Organização

A seção 2 delimita contexto, perfis e restrições. A seção 3 especifica interfaces, 20 RF, 14 casos de uso, 12 regras, 14 RNF e informações persistidas. A seção 4 relaciona requisitos, modelos, telas e verificação. Os documentos da P1 são a base histórica; para a P2, prevalecem esta SRS e o registro explícito de decisões.

## 2. Descrição geral

### 2.1 Perspectiva do produto

Sistema web responsivo independente, acessível por navegador de computador ou celular. Na arquitetura-alvo, o cliente se comunica com a aplicação, que controla autorização, tempo e acesso aos dados. O navegador não deve acessar diretamente o banco de produção.

O protótipo é um artefato de avaliação da interação. O armazenamento local e a escolha de perfis demonstrativos não constituem a arquitetura de segurança do produto. Os diagramas distinguem a arquitetura-alvo da implantação estática demonstrativa.

### 2.2 Funções do produto

1. Localizar questões publicadas por classificação e texto, com origem identificada.
2. Praticar individualmente ou configurar e executar simulados com prazo.
3. Receber correção objetiva, comentários e indicadores pessoais.
4. Discutir questões fora da tentativa ativa e moderar com justificativa.
5. Preparar, revisar, publicar e versionar conteúdo.
6. Administrar contas e oferecer agregados somente no escopo autorizado.

### 2.3 Características dos usuários e acesso

| Perfil | Capacidades | Restrições essenciais |
|---|---|---|
| Estudante | Praticar, simular, consultar resultados próprios e discutir | Não publica questões nem acessa resultados alheios |
| Professor | Consultar, discutir e revisar conteúdo autorizado | Não acessa resultados individuais por ser professor |
| Coordenador | Consultar agregados do curso autorizado | Sem nomes, com supressão de grupos pequenos |
| Administrador | Gerenciar catálogo, contas e moderação | Não aprova revisão pedagógica sem papel Professor |

Uma conta pode ter mais de um papel somente por concessão administrativa explícita. O cadastro aberto concede apenas Estudante. A equipe de análise e a instituição são stakeholders, mas não acrescentam papéis de acesso ao produto.

### 2.4 Restrições

- Questões do recorte são objetivas, com uma alternativa correta e pesos unitários.
- Fonte e revisão da versão são necessárias para publicação.
- O prazo da aplicação real é decidido no servidor; encerramento não permite reabertura.
- Política de moderação, retenção, acesso institucional e adaptações de tempo dependem de aprovação.
- Não há pesquisa de campo concluída nem aceite dos stakeholders disponível nesta entrega.
- Os conteúdos do protótipo são autorais didáticos, explicitamente separados de provas oficiais.

### 2.5 Premissas e dependências

O produto depende de conectividade, catálogo elegível, revisão pedagógica e representantes para validar decisões. Provedor, banco, framework de backend, integração institucional e política de primeiro administrador permanecem em aberto. A adoção de HTML/CSS/JavaScript no protótipo não fixa a stack da aplicação futura.

### 2.6 Adiamentos e decisões de demonstração

O protótipo cobre visualmente os quatro perfis e os 14 casos, com simplificações registradas. O formulário limita a duração a 1–180 minutos e a quantidade a 100 itens por conveniência da demonstração; o SRS exige valores positivos e disponibilidade, sem declarar esses máximos como política aprovada. O catálogo inicial contém nove questões publicadas e um rascunho, com quatro alternativas por item. A seleção é determinística, pois aleatoriedade não é requisito da P1.

O painel do coordenador inicia bloqueado. Há um exemplo fictício com curso/período fixos e limiar ilustrativo de 10 estudantes. Seleção real de período, autorização institucional e supressão segura exigem implementação futura. As senhas demonstrativas não são armazenadas; a simulação não coleta credenciais reais.

## 3. Requisitos específicos

### 3.1 Interfaces externas

#### 3.1.1 Interface de usuário

Todas as telas devem ter rótulos claros, ações identificáveis, estado vazio quando aplicável, indicação de erros e confirmação de ações irreversíveis. As telas de respostas devem distinguir seleção de alternativa e confirmação de gravação. Resultados devem trazer valores textuais além de gráficos e cores. A navegação deve funcionar com teclado e em largura móvel; o protótipo é insumo para avaliação, sem declaração de conformidade WCAG.

O [catálogo de telas](../11-prototipos/README.md) identifica T01–T17 e seus casos de uso. [Wireframes](../../prototipo/wireframes.html) e capturas documentam composição e navegação.

#### 3.1.2 Interfaces de hardware, software e comunicação

Na aplicação-alvo, navegador com suporte web atual; HTTPS entre cliente e aplicação; conexão protegida e restrita entre aplicação e banco. Nenhuma API institucional ou autenticação do Inep é assumida. Identificadores e autorização devem ser conferidos no servidor independentemente do que a interface permite selecionar. Contratos REST, endpoints e tecnologias de banco não são definidos pela SRS.

No protótipo, arquivos estáticos e armazenamento local do navegador simulam esses fluxos. Não há transmissão de respostas para um backend acadêmico; a hospedagem apenas entrega os arquivos. A fonte opcional do Google Fonts pode ser substituída pelas fontes locais de fallback.

### 3.2 Requisitos funcionais

Os IDs, prioridades, fundamentos e condições da base P1 foram preservados. O estado proposto permanece: detalhamento técnico não equivale a aceite dos usuários. As subseções seguintes incorporam integralmente a especificação funcional para leitura autossuficiente.

#### RF-001 — Cadastrar conta de estudante

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

#### RF-002 — Autenticar e encerrar sessão

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

#### RF-003 — Consultar e filtrar banco de questões

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

#### RF-004 — Responder questão individual

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

#### RF-005 — Consultar gabarito comentado

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

#### RF-006 — Configurar simulado

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

#### RF-007 — Executar e encerrar simulado cronometrado

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

#### RF-008 — Corrigir simulado e apresentar resultado

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

#### RF-009 — Consultar histórico pessoal

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

#### RF-010 — Visualizar estatísticas pessoais por área

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

#### RF-011 — Ler e publicar discussão por questão

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

#### RF-012 — Moderar discussões

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

#### RF-013 — Administrar questões

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

#### RF-014 — Revisar gabaritos e comentários pedagógicos

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

#### RF-015 — Consultar indicadores agregados do curso

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

#### RF-016 — Administrar contas e papéis

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

#### RF-017 — Pesquisar questões por texto

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

#### RF-018 — Exibir proveniência do conteúdo

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

#### RF-019 — Editar dados do próprio perfil

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

#### RF-020 — Registrar respostas de simulado

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

### 3.3 Especificações dos casos de uso

Os fluxos usam a arquitetura-alvo; cada verificação identifica o limite da simulação. A autenticação é pré-condição das operações restritas. Não se introduz include de login em todas as ações.

#### UC-001 — Autenticar e encerrar sessão

**Atores:** Todos os quatro perfis.<br/>
**Requisitos:** RF-002.<br/>
**Regras:** RN-012.<br/>
**Telas:** T01.<br/>
**Gatilho:** Entrar ou sair da aplicação.<br/>
**Pré-condições:** Conta ativa para entrar; sessão existente para sair.

**Fluxo principal**

1. Usuário informa e-mail e senha.
2. Sistema valida credenciais e situação da conta.
3. Sistema estabelece sessão com os papéis vigentes e abre a área inicial.
4. Usuário solicita saída.
5. Sistema invalida a sessão e retorna ao acesso.

**Alternativas e exceções**

- A1 — Credenciais incorretas ou conta inativa: mostrar mensagem genérica; não criar sessão.
- A2 — Sessão ausente ou expirada: solicitar nova entrada antes de ação restrita.
- A3 — Papel revogado: negar a próxima operação restrita, mesmo com sessão anterior.

**Pós-condições:** Sessão iniciada ou encerrada; falhas não criam sessão.

**Cenário de verificação:** Entrar em cada perfil; sair; tentar rota restrita. No protótipo, usar senha demonstrativa enade2026.

#### UC-002 — Consultar e pesquisar questões

**Atores:** Estudante e Professor.<br/>
**Requisitos:** RF-003, RF-017, RF-018.<br/>
**Regras:** RN-001, RN-002, RN-003.<br/>
**Telas:** T04.<br/>
**Gatilho:** Abrir o banco de questões.<br/>
**Pré-condições:** Sessão válida; catálogo pode estar vazio.

**Fluxo principal**

1. Sistema apresenta somente questões publicadas.
2. Usuário define texto, ano, curso, área e componente.
3. Sistema aplica interseção dos filtros e busca sem distinção de maiúsculas/minúsculas no enunciado.
4. Sistema informa quantidade e permite abrir uma questão.
5. Sistema exibe origem e classificação sem revelar o gabarito.

**Alternativas e exceções**

- A1 — Sem correspondências: mostrar estado vazio e ação para limpar filtros.
- A2 — Texto vazio: desconsiderar o filtro textual.
- A3 — Item arquivado ou rascunho acessado diretamente: negar nova prática.

**Pós-condições:** Consulta apresentada sem alterar conteúdo.

**Cenário de verificação:** Combinar curso e ano; buscar trecho do enunciado; testar lista vazia e limpar filtros.

#### UC-003 — Responder questão individual

**Atores:** Estudante.<br/>
**Requisitos:** RF-004.<br/>
**Regras:** RN-001, RN-006, RN-012.<br/>
**Telas:** T05.<br/>
**Gatilho:** Selecionar uma questão publicada para prática.<br/>
**Pré-condições:** Estudante autenticado; questão elegível; ausência de bloqueio por simulado ativo.

**Fluxo principal**

1. Sistema apresenta enunciado e alternativas sem gabarito.
2. Estudante seleciona uma alternativa.
3. Estudante confirma a resposta.
4. Sistema valida o vínculo da alternativa, fixa a versão e grava uma tentativa individual.
5. Sistema conclui a tentativa e libera o feedback de UC-004.

**Alternativas e exceções**

- A1 — Nenhuma alternativa: indicar necessidade de seleção, sem gravar.
- A2 — Repetição da mesma confirmação: manter uma tentativa lógica.
- A3 — Nova prática: criar outra tentativa somente após comando explícito.
- A4 — Questão presente em simulado ativo: impedir prática paralela que revele a solução.

**Pós-condições:** Uma resposta final ligada ao titular e à versão da questão.

**Cenário de verificação:** Responder; conferir comentário; iniciar nova prática; não incluir prática individual no gráfico de simulados.

#### UC-004 — Consultar gabarito comentado

**Atores:** Estudante; Professor em contexto editorial autorizado.<br/>
**Requisitos:** RF-005, RF-018.<br/>
**Regras:** RN-006, RN-011.<br/>
**Telas:** T05, T08, T14.<br/>
**Gatilho:** Abrir feedback após prática individual, resultado de simulado ou revisão editorial.<br/>
**Pré-condições:** Tentativa do titular concluída; ou papel Professor em revisão autorizada.

**Fluxo principal**

1. Sistema identifica contexto de acesso e autorização.
2. Sistema recupera a versão fixada na tentativa ou o rascunho editorial.
3. Sistema apresenta alternativa correta e explicação pedagógica.
4. Sistema apresenta origem e identificação da revisão da versão.

**Alternativas e exceções**

- A1 — Simulado ativo: não liberar gabarito das questões envolvidas.
- A2 — Questão em branco no simulado encerrado: permitir consultar explicação mesmo sem resposta.
- A3 — Catálogo alterado: apresentar a versão histórica, sem trocar pontuação ou comentário.
- A4 — Professor sem contexto editorial: não usar o papel para acessar resultados individuais alheios.

**Pós-condições:** Feedback exibido sem alterar tentativa ou pontuação.

**Cenário de verificação:** Ver comentários de acertos, erros e omissões; observar origem autoral e preservação da versão.

#### UC-005 — Realizar simulado cronometrado

**Atores:** Estudante.<br/>
**Requisitos:** RF-006, RF-007, RF-008, RF-020.<br/>
**Regras:** RN-001, RN-002, RN-004, RN-005, RN-007, RN-010, RN-012.<br/>
**Telas:** T06, T07, T08.<br/>
**Gatilho:** Solicitar um novo simulado.<br/>
**Pré-condições:** Estudante autenticado; catálogo com questões elegíveis.

**Fluxo principal**

1. Estudante informa filtros, quantidade e duração.
2. Sistema valida valores positivos e disponibilidade de questões distintas.
3. Estudante confirma o início com a configuração exibida.
4. Sistema fixa versões de questões e gabaritos; registra início e prazo.
5. Estudante escolhe uma alternativa e solicita seu registro.
6. Sistema confere titularidade, vínculo e recebimento antes do prazo; confirma somente após gravar.
7. Estudante navega e pode substituir respostas enquanto a tentativa estiver aberta.
8. Estudante pede conclusão; sistema informa omissões e pede confirmação.
9. Confirmação manual ou expiração encerra a tentativa uma única vez.
10. Sistema corrige com o gabarito fixado, apresenta acertos, erros, omissões e percentual; libera comentários.

**Alternativas e exceções**

- A1 — Quantidade maior que o catálogo: informar disponibilidade e manter configuração; não iniciar cronômetro.
- A2 — Quantidade/duração inválidas: sinalizar campo e recusar início.
- A3 — No prazo ou depois: rejeitar envio e manter a última resposta aceita.
- A4 — Cancelar confirmação de conclusão: continuar tentativa com o prazo original.
- A5 — Falha de gravação/rede: não exibir confirmação de salvamento; retentar somente enquanto houver prazo.
- A6 — Recarregar tela: retomar o prazo e os dados da tentativa, sem reiniciar contagem.
- A7 — Repetir encerramento: retornar o mesmo resultado lógico.
- A8 — Tentativa de outro titular ou alternativa estranha: negar operação.

**Pós-condições:** Tentativa encerrada e imutável, resultado reproduzível; omissões contam no total, não como acertos.

**Cenário de verificação:** Configurar, responder e alterar escolha; cancelar/confirmar término; conferir 6/10 = 60,00%; ensaiar expiração. O relógio do navegador simula o fluxo, sem comprovar RNF-009.

#### UC-006 — Consultar histórico e estatísticas pessoais

**Atores:** Estudante.<br/>
**Requisitos:** RF-009, RF-010.<br/>
**Regras:** RN-005, RN-009, RN-010.<br/>
**Telas:** T09.<br/>
**Gatilho:** Abrir Meu desempenho.<br/>
**Pré-condições:** Estudante autenticado; histórico pode estar vazio.

**Fluxo principal**

1. Sistema recupera simulados encerrados do titular.
2. Sistema apresenta histórico em ordem de encerramento decrescente.
3. Sistema agrupa os itens pela área preservada em cada tentativa.
4. Sistema calcula soma de acertos dividida pela soma de itens por área.
5. Sistema apresenta gráfico, contagens e tabela textual; permite abrir um resultado.

**Alternativas e exceções**

- A1 — Sem simulados concluídos: mostrar estado vazio e convite à prática.
- A2 — Área sem itens: exibir sem dados, sem divisão por zero.
- A3 — Acesso a histórico alheio: negar sem retornar dados.
- A4 — Tentativas abertas e práticas individuais: excluir do agregado.

**Pós-condições:** Indicadores pessoais exibidos sem comparação pública de estudantes.

**Cenário de verificação:** Concluir dois simulados com tamanhos diferentes e conferir a agregação ponderada e a tabela textual.

#### UC-007 — Participar da discussão por questão

**Atores:** Estudante e Professor.<br/>
**Requisitos:** RF-011.<br/>
**Regras:** RN-006, RN-008, RN-012.<br/>
**Telas:** T10.<br/>
**Gatilho:** Abrir a discussão vinculada a uma questão.<br/>
**Pré-condições:** Sessão válida; questão publicada; sem bloqueio da questão por simulado ativo do estudante.

**Fluxo principal**

1. Sistema recupera comentários visíveis da questão.
2. Usuário informa texto e solicita publicação.
3. Sistema valida texto não vazio após remover espaços externos.
4. Sistema vincula comentário ao autor, questão e instante.
5. Sistema apresenta a contribuição na discussão da mesma questão.

**Alternativas e exceções**

- A1 — Texto em branco: recusar sem criar comentário.
- A2 — Comentário oculto: não disponibilizar a leitores comuns.
- A3 — Questão no simulado ativo: bloquear discussão.

**Pós-condições:** Comentário publicado ou rejeitado sem registro parcial.

**Cenário de verificação:** Publicar comentário; alternar questão; verificar isolamento e bloqueio durante simulado.

#### UC-008 — Manter e revisar gabaritos

**Atores:** Administrador mantém rascunho; Professor revisa.<br/>
**Requisitos:** RF-014.<br/>
**Regras:** RN-001, RN-003, RN-010, RN-011, RN-012.<br/>
**Telas:** T13, T14.<br/>
**Gatilho:** Encaminhar ou abrir uma versão para revisão.<br/>
**Pré-condições:** Questão em rascunho; perfil autorizado para a operação.

**Fluxo principal**

1. Administrador prepara gabarito e comentário da versão.
2. Professor acessa a revisão pedagógica.
3. Professor confere enunciado, alternativas, gabarito, explicação e origem.
4. Professor aprova a versão.
5. Sistema registra revisor, instante e versão; libera elegibilidade para publicação por UC-010.

**Alternativas e exceções**

- A1 — Professor solicita ajustes: registrar observação e manter publicação bloqueada.
- A2 — Explicação ausente: impedir aprovação.
- A3 — Administrador sem papel Professor: impedir aprovação pedagógica.
- A4 — Edição após aprovação: invalidar a revisão e exigir nova aprovação.

**Pós-condições:** Revisão da versão rastreável, sem publicação automática.

**Cenário de verificação:** Usar Professor para aprovar Q010; usar Administrador para publicar; editar e observar nova revisão pendente.

#### UC-009 — Consultar indicadores agregados

**Atores:** Coordenador.<br/>
**Requisitos:** RF-015.<br/>
**Regras:** RN-005, RN-009, RN-012.<br/>
**Telas:** T15.<br/>
**Gatilho:** Abrir o painel do curso.<br/>
**Pré-condições:** Sessão válida; curso autorizado e limiar institucional configurados.

**Fluxo principal**

1. Sistema verifica autorização e configuração do limiar.
2. Coordenador define curso permitido e período.
3. Sistema seleciona simulados encerrados e agrega itens por área.
4. Sistema suprime grupos abaixo do limiar.
5. Sistema exibe taxas e contagens permitidas sem identificar estudantes.

**Alternativas e exceções**

- A1 — Sem curso autorizado ou limiar: manter painel bloqueado.
- A2 — Curso não autorizado: negar consulta.
- A3 — Grupo pequeno: não exibir nem taxa nem contagem.
- A4 — Nenhum dado elegível: indicar ausência de dados.

**Pós-condições:** Painel agregado restrito; sem links para dados individuais.

**Cenário de verificação:** No protótipo, abrir estado bloqueado e o cenário fictício de curso/período fixos. Seleção real de período e autorização institucional permanecem fora da demonstração.

#### UC-010 — Administrar questões e versões

**Atores:** Administrador.<br/>
**Requisitos:** RF-013.<br/>
**Regras:** RN-001, RN-002, RN-003, RN-010, RN-011, RN-012.<br/>
**Telas:** T12, T13.<br/>
**Gatilho:** Criar, editar, publicar ou arquivar uma questão.<br/>
**Pré-condições:** Administrador autenticado e autorizado.

**Fluxo principal**

1. Administrador abre a gestão e cria ou seleciona um rascunho.
2. Informa enunciado, alternativas, classificação, fonte e gabarito.
3. Sistema grava a versão em rascunho e exige revisão de UC-008.
4. Após aprovação, administrador solicita publicação.
5. Sistema verifica elegibilidade e disponibiliza a versão para novas consultas.
6. Quando solicitado, administrador confirma arquivamento; sistema remove o item de novas consultas.

**Alternativas e exceções**

- A1 — Fonte/classificação/gabarito revisado ausentes: recusar publicação.
- A2 — Edição de versão usada: gerar nova versão e preservar cópias das tentativas.
- A3 — Arquivar: não apagar referências históricas.
- A4 — Papel sem autorização: negar manutenção.

**Pós-condições:** Catálogo atualizado sem alterar resultados antigos.

**Cenário de verificação:** Editar/publicar/arquivar uma questão e comparar o resultado de uma tentativa anterior.

#### UC-011 — Moderar discussões

**Atores:** Administrador.<br/>
**Requisitos:** RF-012.<br/>
**Regras:** RN-008, RN-012.<br/>
**Telas:** T17.<br/>
**Gatilho:** Solicitar ocultação de comentário.<br/>
**Pré-condições:** Administrador autorizado; comentário existente.

**Fluxo principal**

1. Administrador consulta comentários e seu contexto.
2. Informa justificativa conforme a política a aprovar.
3. Solicita ocultação.
4. Sistema oculta o comentário e registra ator, alvo, motivo e instante.

**Alternativas e exceções**

- A1 — Motivo em branco: recusar ocultação.
- A2 — Comentário já oculto: não duplicar o evento lógico.
- A3 — Leitor comum tenta acessar conteúdo oculto: negar.

**Pós-condições:** Comentário invisível para leitores comuns, preservado no contexto administrativo.

**Cenário de verificação:** Ocultar com motivo e voltar ao fórum como estudante; no protótipo, esse controle é apenas local.

#### UC-012 — Administrar contas e papéis

**Atores:** Administrador.<br/>
**Requisitos:** RF-016.<br/>
**Regras:** RN-009, RN-012.<br/>
**Telas:** T16.<br/>
**Gatilho:** Alterar situação ou papéis de uma conta existente.<br/>
**Pré-condições:** Administrador ativo e autorizado; justificativa da concessão/revogação.

**Fluxo principal**

1. Administrador identifica a conta-alvo.
2. Seleciona papéis e situação ativa/inativa.
3. Informa justificativa e confirma.
4. Sistema protege o último administrador ativo.
5. Sistema grava e audita; próximas ações utilizam os papéis vigentes.

**Alternativas e exceções**

- A1 — Remover/desativar último administrador: recusar.
- A2 — Estudante tenta se promover: negar.
- A3 — Revogação com sessão existente: negar a próxima ação restrita.
- A4 — Falha de gravação: preservar permissões anteriores.

**Pós-condições:** Permissões atualizadas sem apagar tentativas ou resultados.

**Cenário de verificação:** Tentar remover último administrador; conceder e revogar um papel em conta fictícia; verificar menu e acesso direto.

#### UC-013 — Cadastrar conta de estudante

**Atores:** Estudante ainda sem conta.<br/>
**Requisitos:** RF-001.<br/>
**Regras:** RN-012.<br/>
**Telas:** T02.<br/>
**Gatilho:** Abrir Criar conta.<br/>
**Pré-condições:** E-mail ainda não utilizado; serviço disponível.

**Fluxo principal**

1. Pessoa informa nome, e-mail e senha.
2. Sistema verifica preenchimento, formato e unicidade.
3. Sistema cria conta somente com papel Estudante.
4. Sistema confirma o cadastro e permite acesso.

**Alternativas e exceções**

- A1 — E-mail duplicado: recusar sem duplicar conta.
- A2 — Campos inválidos: informar o campo e manter dados não sensíveis.
- A3 — Pedido de papel privilegiado no cadastro: ignorar/recusar sem conceder acesso.

**Pós-condições:** Conta de estudante criada ou nenhum registro parcial.

**Cenário de verificação:** No protótipo, cadastrar dados fictícios com senha demonstrativa; verificar ausência de seleção de papel e duplicidade de e-mail.

#### UC-014 — Editar perfil próprio

**Atores:** Todos os quatro perfis.<br/>
**Requisitos:** RF-019.<br/>
**Regras:** RN-012.<br/>
**Telas:** T11.<br/>
**Gatilho:** Abrir Meu perfil.<br/>
**Pré-condições:** Sessão válida e perfil próprio.

**Fluxo principal**

1. Sistema apresenta nome e campos permitidos.
2. Usuário altera nome; estudante pode escolher curso de interesse.
3. Sistema valida nome não vazio.
4. Sistema salva preferências e preserva e-mail, senha, papéis e resultados.

**Alternativas e exceções**

- A1 — Nome só com espaços: recusar.
- A2 — Tentativa de editar outro titular: negar.
- A3 — Curso alterado: não conceder autorização institucional nem reclassificar resultados antigos.

**Pós-condições:** Preferências atualizadas sem mudança de acesso.

**Cenário de verificação:** Alterar nome e verificar topo da tela; confirmar que e-mail e papéis não são editáveis neste fluxo.

### 3.4 Regras de negócio

As regras governam o produto proposto; não representam regras oficiais de cálculo do ENADE.

#### RN-001 — Tipologia objetiva do recorte

- **Descrição:** Uma questão objetiva publicável possui enunciado, alternativas não vazias e exatamente uma alternativa correta. Questões anuladas ou sem gabarito confiável não integram novos simulados.
- **Justificativa:** Tornar a correção proposta determinística; o exame oficial não é reduzido a essa tipologia.
- **Requisitos associados:** RF-003, RF-004, RF-006, RF-008, RF-013, RF-014, RF-020.
- **Exceções/limites:** Outras tipologias exigem regra específica aprovada; rascunhos podem estar incompletos.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-002 — Classificação do catálogo

- **Descrição:** Cada versão publicada informa ano de origem, curso, área e componente (Formação Geral ou Componente Específico); filtros combinados selecionam a interseção desses valores.
- **Justificativa:** Viabilizar organização indicada em F01 p. 4.
- **Requisitos associados:** RF-003, RF-006, RF-013, RF-017.
- **Exceções/limites:** Materiais aplicáveis a mais de um curso podem ter múltiplos vínculos, sem duplicar a mesma questão na tentativa.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-003 — Origem e publicação de conteúdo

- **Descrição:** Publicação depende de fonte identificável e verificação da condição de uso; questão oficial e questão autoral são identificadas separadamente.
- **Justificativa:** Garantir proveniência e impedir atribuição indevida ao Inep.
- **Requisitos associados:** RF-003, RF-013, RF-014, RF-018.
- **Exceções/limites:** Material de origem ou condição de uso não esclarecida permanece rascunho.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-004 — Composição do simulado

- **Descrição:** Quantidade e duração são positivas; há questões publicadas distintas suficientes para os filtros. Duração é fixada no início, incluindo adaptações autorizadas antes da tentativa.
- **Justificativa:** Evitar configuração impossível e mudança arbitrária do prazo.
- **Requisitos associados:** RF-006, RF-007.
- **Exceções/limites:** Adaptação por acessibilidade depende de política aprovada; não implica alteração unilateral durante a tentativa.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-005 — Pontuação e agregação

- **Descrição:** Cada item objetivo tem peso unitário: percentual = 100 × acertos / total de questões, exibido com duas casas decimais. Omissões não são acertos; erros são respostas preenchidas incorretas. Agregados dividem a soma de acertos pela soma de itens.
- **Justificativa:** Propor interpretação verificável do desempenho; não equivale a cálculo oficial do ENADE.
- **Requisitos associados:** RF-008, RF-010, RF-015.
- **Exceções/limites:** Conjunto vazio exibe “sem dados”; não dividir por zero. Pesos diferentes e recálculo por anulação posterior dependem de nova decisão.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-006 — Momento de disponibilização do feedback

- **Descrição:** Prática individual libera gabarito após registrar a resposta; simulado libera somente após encerramento. Discussões das questões do simulado ficam indisponíveis ao estudante durante a tentativa.
- **Justificativa:** Preservar o exercício antes de revelar soluções.
- **Requisitos associados:** RF-004, RF-005, RF-011, RF-018.
- **Exceções/limites:** Professor com permissão de revisão acessa comentário no contexto editorial; isso não concede leitura de resultados individuais de estudantes.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-007 — Prazo e imutabilidade do encerramento

- **Descrição:** Prazo = início no servidor + duração confirmada. Uma resposta só é aceita se recebida antes do prazo e antes do encerramento manual. Ao atingir o prazo, a tentativa está encerrada. A última resposta aceita prevalece; encerramento não admite reabertura nesta proposta.
- **Justificativa:** Evitar disputa entre relógio local, envios concorrentes e correção.
- **Requisitos associados:** RF-007, RF-008, RF-020.
- **Exceções/limites:** Falha de rede não concede tempo adicional automático. Retentativa de envio é possível apenas enquanto houver prazo e não garante registro de envio atrasado.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-008 — Publicação e moderação de comentários

- **Descrição:** Somente contas autenticadas publicam texto não vazio em questões publicadas. Administrador pode ocultar conteúdo com motivo registrado conforme política de convivência ainda a aprovar.
- **Justificativa:** Associar discussão ao contexto pedagógico e possibilitar revisão de moderação.
- **Requisitos associados:** RF-011, RF-012.
- **Exceções/limites:** Conteúdo oculto permanece disponível somente à revisão administrativa autorizada; política não definida impede alegar moderação plenamente especificada.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-009 — Titularidade e acesso a resultados

- **Descrição:** Estudante consulta apenas seus dados individuais. Professor não recebe acesso individual por padrão. Coordenador acessa somente agregados de cursos autorizados, com supressão de grupos abaixo de limiar institucional aprovado.
- **Justificativa:** Conciliar acompanhamento com restrição de exposição.
- **Requisitos associados:** RF-009, RF-010, RF-015, RF-016.
- **Exceções/limites:** Sem autorização ou limiar configurado, painel agregado permanece bloqueado. Exceções de acesso individual exigem nova aprovação documentada.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-010 — Preservação de versões e tentativas

- **Descrição:** Tentativa fixa versões de enunciado, classificação e gabarito no início. Alteração posterior gera nova versão para uso futuro. Questões utilizadas são arquivadas, sem remoção que destrua referências históricas.
- **Justificativa:** Permitir reproduzir correção e estatísticas sem mudanças silenciosas.
- **Requisitos associados:** RF-006, RF-007, RF-008, RF-009, RF-010, RF-013, RF-014, RF-020.
- **Exceções/limites:** Retenção e anonimização de dados pessoais seguem política a validar; preservação lógica não autoriza retenção indefinida de identidade.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-011 — Revisão pedagógica por versão

- **Descrição:** Publicação de questão exige comentário e gabarito aprovados por professor autorizado, com identificação de revisor, data e versão. Alterar conteúdo após revisão exige nova aprovação.
- **Justificativa:** Reduzir risco de feedback incorreto e rastrear responsabilidade.
- **Requisitos associados:** RF-005, RF-013, RF-014, RF-018.
- **Exceções/limites:** Administrador somente revisa pedagogicamente se também possuir papel Professor; esse acúmulo precisa de concessão explícita.
- **Estado de validação:** Proposto — não validado com stakeholders.

#### RN-012 — Contas e permissões

- **Descrição:** Cadastro inicial concede somente papel Estudante. Apenas administrador gerencia papéis; não é permitido remover o último administrador ativo. Cada operação usa permissões vigentes. Perfil próprio não altera papel, senha, e-mail ou acesso institucional.
- **Justificativa:** Evitar autopromoção e perda de administração.
- **Requisitos associados:** RF-001, RF-002, RF-004, RF-011, RF-012, RF-013, RF-014, RF-015, RF-016, RF-019, RF-020.
- **Exceções/limites:** Provisionamento do primeiro administrador ocorre por procedimento institucional futuro; acumular papéis requer autorização, não cadastro aberto.
- **Estado de validação:** Proposto — não validado com stakeholders.

### 3.5 Requisitos não funcionais

Metas herdadas da P1 para negociação e testes futuros. A verificação do protótipo não mede disponibilidade, carga, segurança de servidor ou recuperação. Referências à M1 nas fichas seguintes identificam a origem histórica; as metas continuam pendentes na P2.

#### RNF-001 — Usabilidade

- **Categoria:** Usabilidade.
- **Descrição:** Os fluxos de consulta, início de simulado e consulta de resultado devem ser compreensíveis em computador e celular.
- **Justificativa:** Reduzir esforço de navegação para N-009.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: em sessão futura com pelo menos 5 participantes, 80% ou mais completam cada uma das três tarefas sem intervenção; registrar falhas e tempo sem alegar representatividade estatística.
- **Método de validação:** Teste moderado com tarefas, critérios de sucesso e registro real por participante.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-007, RF-008.

#### RNF-002 — Desempenho

- **Categoria:** Desempenho.
- **Descrição:** Consultas ao catálogo devem responder dentro de uma meta negociada em carga controlada.
- **Justificativa:** Evitar interrupção do estudo por demora, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: p95 de resposta completa até 3 s em 1.000 consultas, após aquecimento, com 100 usuários simultâneos, catálogo de 10.000 questões e rede de 20 Mbps/100 ms de latência. Erros abaixo de 1%; registrar hardware, tamanho das respostas e cenário antes do teste.
- **Método de validação:** Ensaio de carga futuro com percentis e taxa de erro; não executado na M1.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-017.

#### RNF-003 — Disponibilidade

- **Categoria:** Disponibilidade.
- **Descrição:** Disponibilizar os fluxos essenciais conforme objetivo mensal definido.
- **Justificativa:** Permitir continuidade de preparação, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: disponibilidade mensal >= 99,5%, calculada por (minutos totais - minutos indisponíveis) / minutos totais, incluindo manutenção. Sonda a cada minuto testa login, consulta e abertura de simulado; qualquer falha caracteriza minuto indisponível.
- **Método de validação:** Monitoramento futuro, relatório mensal e revisão de incidentes; esta P1 não possui serviço monitorado.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-002, RF-003, RF-007.

#### RNF-004 — Segurança

- **Categoria:** Segurança.
- **Descrição:** Proteger credenciais no armazenamento e trânsito e exigir autorização no servidor para operações restritas.
- **Justificativa:** Impedir exposição de credenciais e acesso indevido, N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: nenhum fluxo autenticado aceita HTTP sem redirecionamento seguro; senhas não aparecem em logs nem em armazenamento reversível; 100% dos cenários negativos da matriz de papéis recusam operações. Algoritmo de hash e parâmetros serão definidos em projeto de segurança posterior.
- **Método de validação:** Inspeção de configuração, armazenamento e logs; testes de autorização e tráfego em implementação futura.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-002, RF-016.

#### RNF-005 — Privacidade e controle de acesso

- **Categoria:** Privacidade e controle de acesso.
- **Descrição:** Restringir resultados individuais ao titular e impedir inferência por acesso direto a identificadores.
- **Justificativa:** Preservar confidencialidade de N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: todos os cenários de tentativa alheia, papel revogado e curso não autorizado são negados, sem retornar corpo com dados do titular; documentação de papéis deve cobrir cada operação sensível.
- **Método de validação:** Revisão da matriz de acesso e testes negativos com duas contas por perfil.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-009, RF-010, RF-015, RF-016.

#### RNF-006 — Acessibilidade

- **Categoria:** Acessibilidade.
- **Descrição:** Adotar como referência proposta WCAG 2.2 nível AA nos fluxos de cadastro, consulta, simulado e resultados.
- **Justificativa:** Reduzir barreiras para N-009; referência técnica F05.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: atender todos os critérios A e AA aplicáveis aos fluxos; testar teclado, ordem de foco, nomes acessíveis, leitor de tela, contraste, mensagens de erro e alternativas textuais de gráficos. Necessidade de ajuste de tempo deve ser resolvida antes de aprovar o fluxo cronometrado.
- **Método de validação:** Auditoria manual e automatizada futura; checklist por critério e teste com usuários. Não se declara conformidade atual.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-003, RF-006, RF-007, RF-010.

#### RNF-007 — Auditabilidade

- **Categoria:** Auditabilidade.
- **Descrição:** Registrar mudanças em questões, gabaritos, permissões e moderação sem senhas ou conteúdo pessoal desnecessário.
- **Justificativa:** Permitir investigar alterações de N-008/N-012.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: cada operação administrativa concluída gera exatamente um evento lógico com ator, ação, alvo, versão e instante; acesso de estudante aos registros administrativos é negado. Prazo de retenção depende de RNF-012.
- **Método de validação:** Inspeção de eventos e testes de repetição e autorização futuros.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-012, RF-013, RF-014, RF-016.

#### RNF-008 — Confiabilidade e recuperação

- **Categoria:** Confiabilidade e recuperação.
- **Descrição:** Preservar dados essenciais mediante cópia protegida e procedimento de restauração verificável.
- **Justificativa:** Reduzir perdas de respostas e conteúdo, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Metas propostas: RPO <= 24 h e RTO <= 4 h em teste de restauração a partir de cópia isolada; conferir quantidade de tentativas e integridade de referências. Capacidade e custo de armazenamento a validar.
- **Método de validação:** Exercício de recuperação futuro com horários reais e comparação de registros; não realizado na M1.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-007, RF-009, RF-013.

#### RNF-009 — Confiabilidade temporal

- **Categoria:** Confiabilidade temporal.
- **Descrição:** Usar o relógio do servidor e transições consistentes para decidir aceitação de respostas e término.
- **Justificativa:** Manter justiça e previsibilidade de N-002.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: manipular o relógio cliente em ±1 h não altera prazo; envios recebidos imediatamente antes do limite são aceitos se a tentativa estiver aberta, e no limite ou depois são recusados; corrida entre envio e encerramento resulta em um estado determinístico.
- **Método de validação:** Simulação controlada de relógios, limite temporal, concorrência e repetição de comandos.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-007, RF-020.

#### RNF-010 — Manutenibilidade

- **Categoria:** Manutenibilidade.
- **Descrição:** Separar interface, decisões de negócio e persistência conforme modelo conceitual, com requisitos ligados às decisões.
- **Justificativa:** Facilitar alteração de regras e conteúdo, N-012.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: revisão arquitetural não identifica regra de pontuação duplicada na interface; cada componente possui responsabilidade documentada; mudança simulada de RN-005 aponta os componentes afetados e seus testes antes de codificar.
- **Método de validação:** Revisão de componentes na M1; futura inspeção de código e análise de impacto.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-008, RF-010, RF-013.

#### RNF-011 — Compatibilidade

- **Categoria:** Compatibilidade.
- **Descrição:** Viabilizar acesso web responsivo em navegadores e dispositivos acordados.
- **Justificativa:** Atender computador e celular de N-009.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: fluxos essenciais funcionam em Chrome, Firefox e Edge no desktop e Chrome Android/Safari iOS, nas versões estáveis e anterior disponíveis na data do teste; registrar versões exatas. Testar larguras de 360 e 1280 px sem perda de ações essenciais.
- **Método de validação:** Matriz de navegadores futura, teste manual e registro de falhas. A arquitetura não exige aplicativo nativo.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-002, RF-003, RF-007, RF-010.

#### RNF-012 — Privacidade e ciclo de vida de dados

- **Categoria:** Privacidade e ciclo de vida de dados.
- **Descrição:** Definir finalidade, acesso, prazo de retenção e destinação para conta, respostas, comentários e auditoria antes da operação real.
- **Justificativa:** Evitar coleta excessiva e retenção indefinida de N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: 100% das categorias documentadas com responsável, finalidade, prazo e procedimento de exclusão ou anonimização; painel agregado bloqueado sem autorização e limiar aprovados; nenhuma entrevista identificável publicada. Prazos e limiar ainda pendentes.
- **Método de validação:** Revisão de governança com instituição; ensaios futuros de retenção e supressão de agregados. Não é declaração de conformidade legal.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-009, RF-011, RF-015, RF-019.

#### RNF-013 — Escalabilidade

- **Categoria:** Escalabilidade.
- **Descrição:** Permitir aumentar a capacidade de processamento sem alterar regras de pontuação ou autorização.
- **Justificativa:** Preparar crescimento possível de N-011 sem impor microserviços.
- **Prioridade:** Could Have.
- **Critério mensurável de verificação:** Meta proposta: ao dobrar de 100 para 200 usuários concorrentes e ampliar capacidade computacional até 2 vezes, manter p95 <= 3 s no cenário de RNF-002, com erros abaixo de 1%, e registrar custo/recursos.
- **Método de validação:** Teste de capacidade futuro com mesmas consultas e conjunto de dados; sem contratação de infraestrutura nesta fase.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-007.

#### RNF-014 — Integridade de dados

- **Categoria:** Integridade de dados.
- **Descrição:** Preservar vínculos entre tentativa, titular, questões, respostas e versões; impedir efeitos duplicados em reenvios.
- **Justificativa:** Garantir coerência histórica de N-011/N-012.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: nenhum resultado referencia questão/versão inexistente; 100 reenvios do mesmo comando lógico de encerramento geram um único resultado; mudança de catálogo não altera resultado histórico; falha durante gravação não deixa confirmação sem registro.
- **Método de validação:** Inspeção do modelo e testes futuros de idempotência, concorrência e falhas de persistência.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-004, RF-007, RF-008, RF-013, RF-020.

### 3.6 Dados e integridade

| Entidade lógica | Informação essencial | Integridade esperada |
|---|---|---|
| Conta | ID, nome, e-mail, situação, papéis | E-mail único; cadastro sem privilégio; credencial protegida no produto |
| Questão/versão | ID, versão, enunciado, alternativas, classificação, origem, situação | Publicada somente após revisão da mesma versão |
| Revisão | Versão, professor, instante, decisão, observação | Alteração de conteúdo exige nova aprovação |
| Tentativa | ID, titular, configuração, início, prazo, estado, versões fixadas | Titularidade, prazo autoritativo e encerramento único |
| Resposta | Tentativa, questão/versão, alternativa, instante de aceite | No máximo uma resposta final aceita por questão |
| Resultado | Tentativa, acertos, erros, omissões, percentual | Soma das categorias igual ao total; cálculo reproduzível |
| Comentário | ID, questão, autor, texto, instante, situação | Texto não vazio; ocultação não apaga o registro administrativo |
| Evento administrativo | Ator, ação, alvo, versão, instante, justificativa | Um evento lógico por ação concluída |

O modelo é lógico: tabelas, índices, transações, duração da retenção e procedimentos de anonimização serão definidos antes da operação real. No protótipo, a cópia das versões dentro de cada tentativa demonstra a preservação, sem comprovar integridade de banco ou concorrência distribuída.

### 3.7 Estados e comportamento temporal

Uma configuração válida permite iniciar uma tentativa **em andamento**. Envio aceito substitui somente a resposta daquela questão. Confirmação manual ou prazo atingido levam a **encerrada**. Cancelar confirmação mantém a tentativa em andamento com o mesmo prazo. Encerrada não retorna a em andamento; nova prática cria outra tentativa.

A condição de aceite do produto é: titular autorizado E questão pertencente à tentativa E alternativa válida E tentativa aberta E recebimento no servidor anterior ao prazo. No instante exato do prazo, o envio é recusado. O produto deve resolver atomicamente concorrência entre resposta e término. O protótipo mostra esse limite com tempo local, que pode ser alterado e não oferece a garantia de RNF-009.

Consulte os diagramas de [estados da tentativa](../06-modelagem-uml/estados-simulado/estados-simulado.svg) e [sequência de resposta](../06-modelagem-uml/sequencia-resposta/sequencia-resposta.svg).

## 4. Rastreabilidade, revisão e validação

### 4.1 Cobertura e critérios de revisão

O [relatório de consistência](../10-consistencia/revisao-p2.md) associa cada RF a caso de uso, regras, telas e verificações. Os identificadores devem existir e ser únicos; os atores devem coincidir entre SRS e UML; ações do protótipo não podem ser descritas como garantias de produção. RF/RNF/RN da P1 mantêm seus IDs para possibilitar análise de impacto.

### 4.2 Verificação técnica e validação com usuários

Revisão técnica verifica documentos, navegação, transições e exemplos determinísticos. Evidências de execução ficam em [evidencias/p2](../../evidencias/p2/README.md). Validação com usuários exige sessão real com participantes, datas, tarefas, observações e decisões; permanece pendente. Não se atribui aprovação ao professor ou a participantes fictícios.

Para a sessão futura: pedir que o participante encontre uma questão, faça um simulado curto e localize seu resultado; registrar dificuldades, tempo e alterações sugeridas; revisar requisitos afetados na matriz; obter decisão real sobre cada pendência.

### 4.3 Pendências para aprovação do produto

- Representantes e coleta real de necessidades; aceite das prioridades e dos fluxos.
- Adaptações de duração, acessibilidade e recuperação após perda de conexão.
- Política de moderação e responsabilidades de revisão de conteúdo.
- Autorização de agregados, limiar de supressão e prevenção de inferência entre consultas.
- Retenção, exclusão/anonimização e exposição do nome do revisor.
- Stack, infraestrutura, segurança, disponibilidade e metas quantitativas de produção.

### 4.4 Gerenciamento de mudanças

Registrar mudança com motivo, fonte, IDs afetados e decisão. Atualizar SRS, matriz, UML, telas e verificação vinculadas na mesma evolução versionada. A conclusão de uma issue documental indica a entrega de seu artefato, não aprovação institucional do produto. O [planejamento da M2](../12-sprint2/planejamento-m2.md) mantém tarefas e evidências de encerramento.
