# Modelagem UML inicial

Três modelos conceituais, versão 2.0 de 04/11/2026. A arquitetura e os papéis são propostos, sem implementação ou implantação.

| Modelo | Explicação e rastreabilidade | Fonte | SVG | PNG |
|---|---|---|---|---|
| Casos de uso | [README](casos-de-uso/README.md) | [PlantUML](casos-de-uso/casos-de-uso.puml) | [SVG](casos-de-uso/casos-de-uso.svg) | [PNG](casos-de-uso/casos-de-uso.png) |
| Componentes | [README](componentes/README.md) | [PlantUML](componentes/componentes.puml) | [SVG](componentes/componentes.svg) | [PNG](componentes/componentes.png) |
| Implantação | [README](implantacao/README.md) | [PlantUML](implantacao/implantacao.puml) | [SVG](implantacao/implantacao.svg) | [PNG](implantacao/implantacao.png) |

## Reprodução local

Foi utilizado Java 8 já disponível e PlantUML **1.2026.9, variante Java 8**, obtido da distribuição oficial e mantido apenas como ferramenta local. O JAR padrão dessa versão requer Java mais recente; use a variante compatível com o ambiente. O layout Smetana é incluído no JAR e dispensa instalação global de Graphviz. Nenhum conteúdo foi enviado a servidor externo de renderização.

Para reproduzir, obtenha o JAR em [PlantUML](https://plantuml.com/download) e passe seu caminho ao script. Na raiz do repositório, em PowerShell:

```powershell
./ferramentas/renderizar-diagramas.ps1 -PlantUmlJar 'C:\caminho\plantuml.jar'
```

O script verifica a sintaxe e gera SVG/PNG. Os binários da ferramenta não são versionados. A renderização valida sintaxe; a consistência conceitual depende também de revisão dos RF/RN e das explicações dos modelos.
