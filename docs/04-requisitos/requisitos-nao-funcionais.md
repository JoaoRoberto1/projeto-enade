# Requisitos não funcionais

**Versão 2.0 · 04/11/2026 · 14 requisitos · Todas as metas são propostas e estão sujeitas a validação.**

Nenhum indicador de produto foi medido nesta etapa documental. Critérios quantitativos abaixo são cenários candidatos para tornar a discussão verificável, não garantias de atendimento. Fontes: [F01/F03](../../referencias/README.md), hipóteses de análise e [WCAG 2.2](https://www.w3.org/TR/WCAG22/) para RNF-006.

## RNF-001 — Usabilidade

- **Categoria:** Usabilidade.
- **Descrição:** Os fluxos de consulta, início de simulado e consulta de resultado devem ser compreensíveis em computador e celular.
- **Justificativa:** Reduzir esforço de navegação para N-009.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: em sessão futura com pelo menos 5 participantes, 80% ou mais completam cada uma das três tarefas sem intervenção; registrar falhas e tempo sem alegar representatividade estatística.
- **Método de validação:** Teste moderado com tarefas, critérios de sucesso e registro real por participante.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-007, RF-008.

## RNF-002 — Desempenho

- **Categoria:** Desempenho.
- **Descrição:** Consultas ao catálogo devem responder dentro de uma meta negociada em carga controlada.
- **Justificativa:** Evitar interrupção do estudo por demora, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: p95 de resposta completa até 3 s em 1.000 consultas, após aquecimento, com 100 usuários simultâneos, catálogo de 10.000 questões e rede de 20 Mbps/100 ms de latência. Erros abaixo de 1%; registrar hardware, tamanho das respostas e cenário antes do teste.
- **Método de validação:** Ensaio de carga futuro com percentis e taxa de erro; não executado na M1.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-017.

## RNF-003 — Disponibilidade

- **Categoria:** Disponibilidade.
- **Descrição:** Disponibilizar os fluxos essenciais conforme objetivo mensal definido.
- **Justificativa:** Permitir continuidade de preparação, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: disponibilidade mensal >= 99,5%, calculada por (minutos totais - minutos indisponíveis) / minutos totais, incluindo manutenção. Sonda a cada minuto testa login, consulta e abertura de simulado; qualquer falha caracteriza minuto indisponível.
- **Método de validação:** Monitoramento futuro, relatório mensal e revisão de incidentes; esta P1 não possui serviço monitorado.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-002, RF-003, RF-007.

## RNF-004 — Segurança

- **Categoria:** Segurança.
- **Descrição:** Proteger credenciais no armazenamento e trânsito e exigir autorização no servidor para operações restritas.
- **Justificativa:** Impedir exposição de credenciais e acesso indevido, N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: nenhum fluxo autenticado aceita HTTP sem redirecionamento seguro; senhas não aparecem em logs nem em armazenamento reversível; 100% dos cenários negativos da matriz de papéis recusam operações. Algoritmo de hash e parâmetros serão definidos em projeto de segurança posterior.
- **Método de validação:** Inspeção de configuração, armazenamento e logs; testes de autorização e tráfego em implementação futura.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-002, RF-016.

## RNF-005 — Privacidade e controle de acesso

- **Categoria:** Privacidade e controle de acesso.
- **Descrição:** Restringir resultados individuais ao titular e impedir inferência por acesso direto a identificadores.
- **Justificativa:** Preservar confidencialidade de N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: todos os cenários de tentativa alheia, papel revogado e curso não autorizado são negados, sem retornar corpo com dados do titular; documentação de papéis deve cobrir cada operação sensível.
- **Método de validação:** Revisão da matriz de acesso e testes negativos com duas contas por perfil.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-009, RF-010, RF-015, RF-016.

## RNF-006 — Acessibilidade

- **Categoria:** Acessibilidade.
- **Descrição:** Adotar como referência proposta WCAG 2.2 nível AA nos fluxos de cadastro, consulta, simulado e resultados.
- **Justificativa:** Reduzir barreiras para N-009; referência técnica F05.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: atender todos os critérios A e AA aplicáveis aos fluxos; testar teclado, ordem de foco, nomes acessíveis, leitor de tela, contraste, mensagens de erro e alternativas textuais de gráficos. Necessidade de ajuste de tempo deve ser resolvida antes de aprovar o fluxo cronometrado.
- **Método de validação:** Auditoria manual e automatizada futura; checklist por critério e teste com usuários. Não se declara conformidade atual.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-003, RF-006, RF-007, RF-010.

## RNF-007 — Auditabilidade

- **Categoria:** Auditabilidade.
- **Descrição:** Registrar mudanças em questões, gabaritos, permissões e moderação sem senhas ou conteúdo pessoal desnecessário.
- **Justificativa:** Permitir investigar alterações de N-008/N-012.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: cada operação administrativa concluída gera exatamente um evento lógico com ator, ação, alvo, versão e instante; acesso de estudante aos registros administrativos é negado. Prazo de retenção depende de RNF-012.
- **Método de validação:** Inspeção de eventos e testes de repetição e autorização futuros.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-012, RF-013, RF-014, RF-016.

## RNF-008 — Confiabilidade e recuperação

- **Categoria:** Confiabilidade e recuperação.
- **Descrição:** Preservar dados essenciais mediante cópia protegida e procedimento de restauração verificável.
- **Justificativa:** Reduzir perdas de respostas e conteúdo, N-011.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Metas propostas: RPO <= 24 h e RTO <= 4 h em teste de restauração a partir de cópia isolada; conferir quantidade de tentativas e integridade de referências. Capacidade e custo de armazenamento a validar.
- **Método de validação:** Exercício de recuperação futuro com horários reais e comparação de registros; não realizado na M1.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-007, RF-009, RF-013.

## RNF-009 — Confiabilidade temporal

- **Categoria:** Confiabilidade temporal.
- **Descrição:** Usar o relógio do servidor e transições consistentes para decidir aceitação de respostas e término.
- **Justificativa:** Manter justiça e previsibilidade de N-002.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: manipular o relógio cliente em ±1 h não altera prazo; envios recebidos imediatamente antes do limite são aceitos se a tentativa estiver aberta, e no limite ou depois são recusados; corrida entre envio e encerramento resulta em um estado determinístico.
- **Método de validação:** Simulação controlada de relógios, limite temporal, concorrência e repetição de comandos.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-007, RF-020.

## RNF-010 — Manutenibilidade

- **Categoria:** Manutenibilidade.
- **Descrição:** Separar interface, decisões de negócio e persistência conforme modelo conceitual, com requisitos ligados às decisões.
- **Justificativa:** Facilitar alteração de regras e conteúdo, N-012.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: revisão arquitetural não identifica regra de pontuação duplicada na interface; cada componente possui responsabilidade documentada; mudança simulada de RN-005 aponta os componentes afetados e seus testes antes de codificar.
- **Método de validação:** Revisão de componentes na M1; futura inspeção de código e análise de impacto.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-008, RF-010, RF-013.

## RNF-011 — Compatibilidade

- **Categoria:** Compatibilidade.
- **Descrição:** Viabilizar acesso web responsivo em navegadores e dispositivos acordados.
- **Justificativa:** Atender computador e celular de N-009.
- **Prioridade:** Should Have.
- **Critério mensurável de verificação:** Meta proposta: fluxos essenciais funcionam em Chrome, Firefox e Edge no desktop e Chrome Android/Safari iOS, nas versões estáveis e anterior disponíveis na data do teste; registrar versões exatas. Testar larguras de 360 e 1280 px sem perda de ações essenciais.
- **Método de validação:** Matriz de navegadores futura, teste manual e registro de falhas. A arquitetura não exige aplicativo nativo.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-002, RF-003, RF-007, RF-010.

## RNF-012 — Privacidade e ciclo de vida de dados

- **Categoria:** Privacidade e ciclo de vida de dados.
- **Descrição:** Definir finalidade, acesso, prazo de retenção e destinação para conta, respostas, comentários e auditoria antes da operação real.
- **Justificativa:** Evitar coleta excessiva e retenção indefinida de N-010.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: 100% das categorias documentadas com responsável, finalidade, prazo e procedimento de exclusão ou anonimização; painel agregado bloqueado sem autorização e limiar aprovados; nenhuma entrevista identificável publicada. Prazos e limiar ainda pendentes.
- **Método de validação:** Revisão de governança com instituição; ensaios futuros de retenção e supressão de agregados. Não é declaração de conformidade legal.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-001, RF-009, RF-011, RF-015, RF-019.

## RNF-013 — Escalabilidade

- **Categoria:** Escalabilidade.
- **Descrição:** Permitir aumentar a capacidade de processamento sem alterar regras de pontuação ou autorização.
- **Justificativa:** Preparar crescimento possível de N-011 sem impor microserviços.
- **Prioridade:** Could Have.
- **Critério mensurável de verificação:** Meta proposta: ao dobrar de 100 para 200 usuários concorrentes e ampliar capacidade computacional até 2 vezes, manter p95 <= 3 s no cenário de RNF-002, com erros abaixo de 1%, e registrar custo/recursos.
- **Método de validação:** Teste de capacidade futuro com mesmas consultas e conjunto de dados; sem contratação de infraestrutura nesta fase.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-003, RF-007.

## RNF-014 — Integridade de dados

- **Categoria:** Integridade de dados.
- **Descrição:** Preservar vínculos entre tentativa, titular, questões, respostas e versões; impedir efeitos duplicados em reenvios.
- **Justificativa:** Garantir coerência histórica de N-011/N-012.
- **Prioridade:** Must Have.
- **Critério mensurável de verificação:** Meta proposta: nenhum resultado referencia questão/versão inexistente; 100 reenvios do mesmo comando lógico de encerramento geram um único resultado; mudança de catálogo não altera resultado histórico; falha durante gravação não deixa confirmação sem registro.
- **Método de validação:** Inspeção do modelo e testes futuros de idempotência, concorrência e falhas de persistência.
- **Estado de aprovação:** Proposto — não aprovado; não implementado e não medido.
- **Requisitos relacionados:** RF-004, RF-007, RF-008, RF-013, RF-020.
