# GitHub e acesso do professor

Repositório existente: [JoaoRoberto1/projeto-enade](https://github.com/JoaoRoberto1/projeto-enade). A configuração pública original foi preservada. Branch de trabalho: `docs/m1-requirements-and-uml`.

## Consulta inicial

Em 04/11/2026, a API autenticada confirmou permissão administrativa da conta configurada e repositório sem issues ou milestones. `gh` não está instalado; a consulta utilizou a credencial do Git em memória. Nenhum token foi incluído nos documentos.

## Configuração e evidência real

- Milestone [M1 — Sprint 1: Elicitação e Modelagem Inicial](https://github.com/JoaoRoberto1/projeto-enade/milestone/1), aberto, com data final histórica 01/11/2026.
- [13 issues publicadas](../../docs/07-sprint/issues/README.md), todas abertas, com labels e sem responsáveis atribuídos.
- Professor `marcelobezerra-dotcom`: **convite enviado; aceite pendente**.
- Confirmação final de vínculo: HTTP **404**; consta em convites pendentes: **sim**.
- Evidência: [resumo sanitizado das respostas da API](estado-api.json), incluindo identificadores reais e códigos HTTP. Não contém credenciais e não é um print.

O repositório pertence a uma conta pessoal. O convite padrão concede colaboração com escrita, sem administração; essa configuração foi mantida conforme o modelo do GitHub. Leitura pública já era possível, mas não substitui a confirmação de colaboração. **Não se declara aceite do convite enquanto a API não confirmar o vínculo.**

## Publicação da branch

Branch publicada: [docs/m1-requirements-and-uml](https://github.com/JoaoRoberto1/projeto-enade/tree/docs/m1-requirements-and-uml). A [verificação da publicação](publicacao.json) confirmou o primeiro commit `62223e143cb0e2f4baf09383c950ba14f7ca889d` no remoto e a igualdade do README local/remoto. Consolidações posteriores podem ser consultadas no histórico da branch.

Como o repositório não tinha commits nem uma `main` existente, o GitHub passou a informar a branch documental como padrão após o primeiro push. Nenhuma `main` foi criada ou sobrescrita; não houve merge nem push forçado. A visibilidade pública preexistente foi preservada. O professor pode ler os documentos pelo link público; o vínculo de colaborador ainda depende do aceite do convite.


## Como verificar e obter evidência real

1. Abra o repositório autenticado como administrador e acesse **Settings → Collaborators** ou a área equivalente de acesso.
2. Localize `marcelobezerra-dotcom`. Verifique se há convite pendente ou acesso como colaborador ativo.
3. Capture a tela real mostrando repositório, usuário e estado. Oculte tokens e informações pessoais desnecessárias.
4. Salve a imagem nesta pasta como `convite-marcelobezerra-dotcom.png` ou `acesso-marcelobezerra-dotcom.png`, identificando data real na descrição do arquivo.
5. Confirme novamente o estado após eventual aceite. Convite enviado não é convite aceito.

Consulta via GitHub CLI, quando disponível e autenticado:

```powershell
gh api repos/JoaoRoberto1/projeto-enade/collaborators/marcelobezerra-dotcom
gh api repos/JoaoRoberto1/projeto-enade/invitations
gh issue list --repo JoaoRoberto1/projeto-enade --state all
gh api 'repos/JoaoRoberto1/projeto-enade/milestones?state=all'
```

O endpoint específico de colaboração retorna 204 quando o vínculo existe e 404 quando não existe, conforme a [documentação oficial do GitHub](https://docs.github.com/en/rest/collaborators/collaborators#check-if-a-user-is-a-repository-collaborator). Uma confirmação textual/JSON real da API não é uma captura de tela. Nenhum print foi fabricado.
