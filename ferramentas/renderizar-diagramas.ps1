param(
    [Parameter(Mandatory = $true)]
    [string]$PlantUmlJar
)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$jarPath = (Resolve-Path -LiteralPath $PlantUmlJar).Path
$diagramFiles = Get-ChildItem -LiteralPath (Join-Path $repoRoot 'docs/06-modelagem-uml') -Filter '*.puml' -Recurse
foreach ($diagram in $diagramFiles) {
    & java '-Djava.awt.headless=true' -jar $jarPath -charset UTF-8 -checkonly $diagram.FullName
    if ($LASTEXITCODE -ne 0) { throw "Sintaxe inválida: $($diagram.FullName)" }
    foreach ($format in @('-tsvg', '-tpng')) {
        & java '-Djava.awt.headless=true' -jar $jarPath -charset UTF-8 $format $diagram.FullName
        if ($LASTEXITCODE -ne 0) { throw "Falha na renderização: $($diagram.FullName)" }
    }
}
Write-Output "Validados e renderizados: $($diagramFiles.Count) diagramas."
