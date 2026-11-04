"""Verifica artefatos documentais; não testa um produto nem valida entrevistas."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = []

def check(condition, message):
    (checks if condition else errors).append(message)

def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')

def ids(text, prefix):
    return set(re.findall(r'\b' + prefix + r'-\d{3}\b', text))

files = {
    'RF': ('docs/04-requisitos/requisitos-funcionais.md', 20),
    'RNF': ('docs/04-requisitos/requisitos-nao-funcionais.md', 14),
    'RN': ('docs/04-requisitos/regras-negocio.md', 12),
    'US': ('docs/05-backlog/backlog-priorizado.md', 17),
}
catalog = {}
blocks = {}
for prefix, (file, count) in files.items():
    text = read(file)
    heads = re.findall(r'^## (' + prefix + r'-\d{3}) — ', text, re.M)
    expected = {f'{prefix}-{n:03d}' for n in range(1, count + 1)}
    check(len(heads) == len(set(heads)), f'{prefix}: definições sem duplicação')
    check(set(heads) == expected, f'{prefix}: sequência completa ({count})')
    catalog[prefix] = set(heads)
    chunks = re.split(r'^## (' + prefix + r'-\d{3}) — ', text, flags=re.M)
    blocks[prefix] = dict(zip(chunks[1::2], chunks[2::2]))

uc_text = read('docs/06-modelagem-uml/casos-de-uso/casos-de-uso.puml')
uc = re.findall(r'usecase "(UC-\d{3})', uc_text)
catalog['UC'] = set(uc)
check(len(uc) == len(set(uc)) == 14, 'UC: 14 definições únicas')
matrix = read('docs/04-requisitos/matriz-rastreabilidade.md')
matrix_rows = [line for line in matrix.splitlines() if line.startswith('| N-')]
check(len(matrix_rows) == 20, 'Matriz: uma linha por RF')
for rf_id, block in blocks['RF'].items():
    rows = [r for r in matrix_rows if rf_id in ids(r, 'RF')]
    check(len(rows) == 1, f'{rf_id}: linha de rastreabilidade única')
    if len(rows) == 1:
        row = rows[0]
        for field in ('N-', 'ST-', 'RN-', 'US-', 'UC-'):
            check(field in row, f'{rf_id}: ligação {field} presente')
        check(ids(row, 'RN') == ids(block, 'RN'), f'{rf_id}: regras coerentes com matriz')
        check(ids(row, 'UC') == ids(block, 'UC'), f'{rf_id}: casos de uso coerentes com matriz')
    for rn in ids(block, 'RN'):
        check(rf_id in ids(blocks['RN'].get(rn, ''), 'RF'), f'{rf_id} / {rn}: ligação recíproca')
    check(bool(ids(block, 'UC')), f'{rf_id}: caso de uso indicado')
    check('**Fonte/fundamento:**' in block, f'{rf_id}: fonte indicada')
for rn_id, block in blocks['RN'].items():
    check(bool(ids(block, 'RF')), f'{rn_id}: vinculado a RF')
    for rf_id in ids(block, 'RF'):
        check(rn_id in ids(blocks['RF'].get(rf_id, ''), 'RN'), f'{rn_id} / {rf_id}: ligação recíproca')

graph = {}
for us_id, block in blocks['US'].items():
    related = re.search(r'^- \*\*Requisitos relacionados:\*\* (.+)$', block, re.M)
    refs = ids(related.group(1), 'RF') if related else set()
    check(bool(refs), f'{us_id}: requisito associado')
    for rf_id in refs:
        row = next((r for r in matrix_rows if rf_id in ids(r, 'RF')), '')
        check(us_id in ids(row, 'US'), f'{us_id} / {rf_id}: matriz coerente')
    graph[us_id] = ids(block, 'US')
def visit(node, trail):
    if node in trail:
        errors.append('Ciclo de dependências: ' + ' -> '.join(trail + [node]))
        return
    for other in graph.get(node, set()):
        visit(other, trail + [node])
for node in graph:
    visit(node, [])

active_md = [p for p in ROOT.rglob('*.md') if not any(part in ('.git', 'originais') for part in p.relative_to(ROOT).parts)]
link_count = 0
secret_patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{30,}', r'AKIA[A-Z0-9]{16}', r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----']
for p in active_md:
    text = p.read_text(encoding='utf-8')
    for prefix, valid in catalog.items():
        unknown = ids(text, prefix) - valid
        check(not unknown, f'{p.relative_to(ROOT)}: referências {prefix} válidas')
    for match in re.finditer(r'!?\[[^\]\n]*\]\(([^\n)]+)\)', text):
        url = match.group(1).strip().strip('<>')
        if urlsplit(url).scheme or url.startswith('#'):
            continue
        target = unquote(url.split('#', 1)[0])
        if target:
            link_count += 1
            check((p.parent / target).resolve().exists(), f'Link: {p.relative_to(ROOT)} -> {target}')
    check('\ufffd' not in text, f'{p.relative_to(ROOT)}: sem caractere inválido de decodificação')

manifest = json.loads(read('referencias/manifesto-originais.json'))
for item in manifest:
    p = ROOT / item['arquivo']
    check(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == item['sha256'], 'Original preservado: ' + item['arquivo'])

for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.relative_to(ROOT).parts:
        continue
    check(p.stat().st_size > 0, 'Arquivo não vazio: ' + p.relative_to(ROOT).as_posix())
    if p.suffix in ('.md', '.puml', '.csv', '.json', '.yml', '.yaml', '.ps1'):
        text = p.read_text(encoding='utf-8-sig')
        for pattern in secret_patterns:
            check(not re.search(pattern, text), 'Sem padrão de segredo: ' + p.relative_to(ROOT).as_posix())

for p in (ROOT / 'docs/06-modelagem-uml').rglob('*.puml'):
    text = p.read_text(encoding='utf-8')
    check(text.count('@startuml') == 1 and text.count('@enduml') == 1, 'Delimitadores UML: ' + p.name)
    svg, png = p.with_suffix('.svg'), p.with_suffix('.png')
    check(svg.exists() and png.exists(), 'Imagens existentes: ' + p.name)
    if svg.exists():
        root = ET.parse(svg).getroot()
        check(root.tag.endswith('svg') and 'Syntax Error' not in svg.read_text(encoding='utf-8'), 'SVG válido: ' + svg.name)
    if png.exists():
        raw = png.read_bytes()
        check(raw.startswith(b'\x89PNG\r\n\x1a\n') and all(v > 100 for v in struct.unpack('>II', raw[16:24])), 'PNG válido: ' + png.name)

readme = read('README.md')
check(all(f'| {n} |' in readme for n in range(1, 9)), 'README: oito entregáveis identificados')
check(len(list((ROOT / 'docs/07-sprint/issues').glob('M1-*.md'))) == 13, 'Treze textos de issues')
check('PENDENTE — coleta de dados reais' in read('docs/03-elicitacao/resultados-entrevistas.md'), 'Entrevistas: pendência explícita')
check(len(read('evidencias/entrevistas/modelo-registro.csv').splitlines()) == 1, 'Instrumento de entrevista não contém respostas fabricadas')

result = {'verificacoes_aprovadas': len(checks), 'erros': errors, 'links_relativos': link_count, 'arquivos_markdown_atuais': len(active_md), 'originais_preservados': len(manifest), 'contagens': {k: len(v) for k, v in catalog.items()}, 'limites': 'Não verifica URLs externas, validade empírica, aprovação humana, conformidade de produto ou sintaxe completa PlantUML; esta última requer o renderizador.'}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
