# Entregáveis complementares

A versão atual é composta pelos documentos Markdown e pelos três conjuntos PlantUML/SVG/PNG acessíveis no [README principal](../README.md). O [checklist](../docs/08-entrega/checklist-entrega.md) informa pendências reais.

[Baixar o relatório PDF da versão 2.0](Trabalho_P1_ENADE_M1_v2.pdf), com **83 páginas**. O relatório consolida os 39 documentos de `docs/` e de orientação sobre evidências/fontes, com sumário navegável e os três diagramas. Tabelas largas são apresentadas como registros rotulados para preservar leitura em A4; o diagrama de implantação recebe uma página A3 horizontal para manter os rótulos legíveis. As pendências reais permanecem explícitas.

O PDF não substitui fontes editáveis, matriz ou evidências. Os arquivos DOCX/PDF em `referencias/originais/pacote-p1/` são históricos e não devem ser enviados como versão atual sem revisar suas diferenças.

Para reproduzir, use Python, as dependências de [requirements-documentacao.txt](../ferramentas/requirements-documentacao.txt) em ambiente local e as fontes Arial do sistema:

```powershell
python ferramentas/gerar-relatorio-pdf.py --font-dir 'C:\Windows\Fonts'
```

O gerador também aceita `--dependencias` para uma pasta instalada com `pip --target`. Ferramentas auxiliares não constituem implementação do produto ENADE.

Nenhum arquivo desta pasta comprova submissão no AVA. Não incluir entrevistas identificáveis ou comprovantes com dados pessoais no repositório público.
