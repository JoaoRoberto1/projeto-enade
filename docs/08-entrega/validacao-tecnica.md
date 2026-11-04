# Validação técnica dos artefatos

Preparação em 04/11/2026. O validador foi executado sem erros após correção de uma ligação ausente entre RF-018 e RN-006 e ajuste da leitura do campo de requisitos das histórias. A verificação é reproduzível pelo script da seção abaixo. Os diagramas passaram pela renderização local com PlantUML 1.2026.9, variante Java 8, usando Smetana, sem erro de sintaxe.

## Resultado e evidências

| Verificação | Resultado observado |
|---|---|
| Estrutura e navegação | Oito entregáveis identificados no README; links relativos verificados |
| Identificadores | 20 RF, 14 RNF, 12 RN, 17 US e 14 UC, sem definições duplicadas |
| Rastreabilidade | 20 linhas de RF; regras recíprocas, histórias e casos de uso cobertos; dependências sem ciclos |
| UML | Três fontes aceitas pelo PlantUML; três SVG e três PNG gerados e inspecionados visualmente |
| Fontes preservadas | 18 cópias com SHA-256 correspondente; 17 arquivos do pacote conferidos contra o ZIP |
| Integridade acadêmica | Coleta, participantes, respostas e aprovações ausentes permanecem pendentes; nenhuma pesquisa fictícia incluída |
| Credenciais | Padrões conhecidos pesquisados e arquivos preparados revisados; nenhum segredo identificado |
| GitHub | 13 issues e M1 criados; convite do professor enviado, aceite pendente; respostas sanitizadas preservadas |

Os detalhes de execução automatizada estão em [resultado das verificações](verificacao-automatizada.json). Alterações posteriores devem repetir a verificação. Os textos originais ficam fora da checagem de referências atuais e de normalização de espaços/finais de linha, porque seus IDs e bytes históricos foram preservados; continuam sujeitos à verificação de integridade dos arquivos. Os arquivos atuais utilizam UTF-8 e finais de linha LF.

## Escopo de verificação

Estrutura, oito entregáveis, links relativos, sequências e referências de identificadores, matriz, relações recíprocas RF/RN, dependências de histórias, fontes e imagens UML, integridade dos originais e padrões conhecidos de credenciais. A inspeção visual confirma legibilidade das imagens, não aprovação dos modelos pelos stakeholders.

## Limites

Não há testes de aplicação ou medição dos RNF porque o trabalho é conceitual. Um scanner de padrões não garante ausência de todo tipo de segredo; a revisão do conteúdo complementa a busca. Não há entrevistas nem aprovações para autenticar. URLs externas e estado do GitHub exigem consultas reais separadas.

## Reprodução

```powershell
python ferramentas/validar-documentacao.py
./ferramentas/renderizar-diagramas.ps1 -PlantUmlJar 'C:\caminho\plantuml-java8-1.2026.9.jar'
git diff --check
git status --short --branch
```
