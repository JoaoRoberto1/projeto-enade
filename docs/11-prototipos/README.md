# Protótipo navegável e wireframes — P2

**Trilha ENADE** é o nome de interface do Sistema de Apoio ao ENADE. O protótipo é web responsivo, com quatro perfis fictícios e dados locais.

- [Código e entrada local](../../prototipo/index.html)
- [Wireframes e mapa de navegação](../../prototipo/wireframes.html)
- [SRS com casos de uso](../09-srs/SRS.md)
- [Revisão de consistência](../10-consistencia/revisao-p2.md)
- [Evidências de execução](../../evidencias/p2/README.md)

## Como executar e demonstrar

Na raiz do repositório, executar `python -m http.server 8765 --directory prototipo` e abrir `http://localhost:8765`. Os arquivos não exigem compilação ou dependências de runtime. A fonte externa é opcional e possui fallback local.

1. Na tela inicial, escolher **Estudante** nos perfis demonstrativos.
2. Consultar o banco e praticar uma questão; confirmar resposta para ver o comentário.
3. Abrir **Simulados**, configurar quantidade e duração, salvar respostas e finalizar.
4. Consultar resultado, comentários e **Meu desempenho**.
5. Sair e entrar como **Professor** para revisar o rascunho Q010; depois como **Administrador** para publicá-lo.
6. Entrar como **Coordenador** e comparar o painel bloqueado com o exemplo fictício agregado.

Para reiniciar, entrar em **Sobre este protótipo → Reiniciar demonstração**. A confirmação apaga somente dados desta demonstração no navegador. A senha demonstrativa das contas é `enade2026`; nenhuma senha é armazenada. Não usar dados pessoais reais.

## Catálogo de telas

As rotas usam fragmentos `#/...`. Simulado e resultado dependem do ID criado ao iniciar uma tentativa; acessar uma rota genérica sem ID não fornece dados de terceiros. As áreas administrativas exigem o perfil demonstrativo correspondente.

| Tela | Nome | Rota | Casos de uso |
|---|---|---|---|
| T01 | Acesso | `#/login` | UC-001 |
| T02 | Cadastro | `#/cadastro` | UC-013 |
| T03 | Visão geral | `#/inicio` | UC-002, UC-005, UC-006 |
| T04 | Banco de questões | `#/questoes` | UC-002 |
| T05 | Prática e comentário | `#/questao/Q001` | UC-003, UC-004 |
| T06 | Configurar simulado | `#/configurar` | UC-005 |
| T07 | Responder simulado | `#/simulado` | UC-005 |
| T08 | Resultado | `#/resultado` | UC-004, UC-005 |
| T09 | Meu desempenho | `#/desempenho` | UC-006 |
| T10 | Discussão | `#/discussao/Q001` | UC-007 |
| T11 | Meu perfil | `#/perfil` | UC-014 |
| T12 | Gestão de questões | `#/administracao` | UC-010 |
| T13 | Editar rascunho | `#/editar/Q010` | UC-008, UC-010 |
| T14 | Revisão pedagógica | `#/revisao` | UC-008, UC-004 |
| T15 | Indicadores do curso | `#/indicadores` | UC-009 |
| T16 | Contas e permissões | `#/usuarios` | UC-012 |
| T17 | Moderação | `#/moderacao` | UC-011 |

## Decisões visuais e estados

Interface em azul escuro e verde, tipografia legível e menu consistente. A jornada principal ocupa o centro da interface. Existem estados vazios, mensagens de erro, feedback de gravação local, confirmação de término, alerta de tempo, acesso restrito e bloqueio de indicadores. Controles têm rótulos; gráficos têm tabela textual; o menu se adapta ao celular. A revisão completa WCAG e testes com usuários permanecem pendentes.

## Limites de fidelidade

- Login, papéis, auditoria, respostas e prazo são simulados no cliente; não são controles de segurança de produto.
- O armazenamento é local, compartilhado pelos perfis fictícios daquele navegador. Outros dispositivos não recebem os dados.
- Questões demonstrativas são autorais, com quatro alternativas; não representam questões oficiais ou revisão pedagógica real.
- O relógio local persiste o prazo ao recarregar, mas não resiste à alteração do relógio pelo usuário.
- O painel agregado usa dados fixos, curso/período fixos e limiar de exemplo; não agrega pessoas reais.
- Não foram implementados backend, gestão real de senha, APIs institucionais, carga, backup, operação offline de produto ou garantia de concorrência distribuída.
- O conteúdo do SRS descreve a aplicação-alvo. Testar o protótipo não confirma todos os critérios de aceitação do produto.

O link de publicação e as capturas verificadas são registrados no [guia de entrega](../12-sprint2/entrega-ava.md).
