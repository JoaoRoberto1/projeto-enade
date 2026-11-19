"""Verifica integridade dos artefatos P2, sem declarar validação de usuários."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import re,json
ROOT=Path(__file__).resolve().parents[1]
srs=(ROOT/'docs/09-srs/SRS.md').read_text(encoding='utf-8')
checks=[]
def check(name,ok,details=''):
 checks.append({'verificacao':name,'resultado':'PASS' if ok else 'FAIL','detalhes':details})
for prefix,count in [('RF',20),('RNF',14),('RN',12),('UC',14)]:
 ids=re.findall(r'^#### ('+prefix+r'-\d{3})\b',srs,re.M)
 check(prefix+' únicos e completos',len(ids)==count and len(set(ids))==count and set(ids)=={f'{prefix}-{i:03d}' for i in range(1,count+1)},str(len(ids)))
for title in ['## 1. Introdução','## 2. Descrição geral','## 3. Requisitos específicos']:
 check('Estrutura SRS: '+title,title in srs)
ucblocks=re.findall(r'^#### (UC-\d{3})[^\n]*\n(.*?)(?=^#### |^### |\Z)',srs,re.M|re.S)
for uid,body in ucblocks:
 check(uid+' completo',all(t in body for t in ['**Atores:**','**Gatilho:**','**Pré-condições:**','**Fluxo principal**','**Alternativas e exceções**','**Pós-condições:**','**Cenário de verificação:**']))
matrix=(ROOT/'docs/10-consistencia/revisao-p2.md').read_text(encoding='utf-8')
rfrows=re.findall(r'^\| (RF-\d{3}) \|',matrix,re.M)
check('Matriz cobre 20 RF',len(rfrows)==20 and len(set(rfrows))==20)
screens=json.loads((ROOT/'docs/11-prototipos/telas.json').read_text(encoding='utf-8'))
check('17 telas com wireframe',len(screens)==17 and all((ROOT/f'prototipo/wireframes/{s["id"]}.svg').is_file() for s in screens))
screenucs=set(re.findall(r'UC-\d{3}',' '.join(s['casos'] for s in screens)))
check('Telas cobrem os 14 UC',screenucs=={f'UC-{i:03d}' for i in range(1,15)})
pumls=list((ROOT/'docs/06-modelagem-uml').rglob('*.puml'))
check('Cinco modelos com SVG e PNG',len(pumls)==5 and all(p.with_suffix('.svg').is_file() and p.with_suffix('.png').is_file() for p in pumls))
usecases=(ROOT/'docs/06-modelagem-uml/casos-de-uso/casos-de-uso.puml').read_text(encoding='utf-8')
check('UC definidos no UML',set(re.findall(r'usecase "(UC-\d{3})',usecases))=={f'UC-{i:03d}' for i in range(1,15)})
check('Quatro atores concretos',all('actor '+a+'\n' in usecases for a in ['Estudante','Professor','Coordenador','Administrador']))
tests=json.loads((ROOT/'evidencias/p2/verificacao-prototipo.json').read_text(encoding='utf-8'))
check('14 cenários do protótipo aprovados',tests.get('resultado')=='PASS' and len(tests['cenarios'])==14 and all(t['resultado']=='PASS' for t in tests['cenarios']))
for pdf in ['SRS_P2_ENADE_v3.pdf','Wireframes_P2_ENADE.pdf','Entrega_P2_ENADE.pdf']:
 p=ROOT/'entregaveis'/pdf;check('PDF: '+pdf,p.is_file() and p.read_bytes().startswith(b'%PDF-'))
docs=[ROOT/'README.md',ROOT/'entregaveis/README.md',ROOT/'referencias/atividade-p2.md',ROOT/'evidencias/p2/README.md']
for directory in ['docs/09-srs','docs/10-consistencia','docs/11-prototipos','docs/12-sprint2','docs/06-modelagem-uml']:
 docs+=list((ROOT/directory).rglob('*.md'))
missing=[]
for p in docs:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  target=target.split(' "',1)[0]
  if urlsplit(target).scheme or target.startswith('#'):continue
  dest=(p.parent/unquote(target.split('#')[0])).resolve()
  if not dest.exists() and dest!=ROOT/'evidencias/p2/verificacao-documental.json':missing.append(p.relative_to(ROOT).as_posix()+' -> '+target)
check('Links locais dos documentos existem',not missing,'; '.join(missing))
bad=[]
for p in (ROOT/'evidencias/p2/prints').glob('*.png'):
 if not p.read_bytes().startswith(b'\x89PNG'):bad.append(p.name)
check('Capturas PNG válidas',not bad and len(list((ROOT/'evidencias/p2/prints').glob('*.png')))>=17)
report={'data_contexto':'2026-11-19','escopo':'Integridade documental e registros técnicos; não validação com stakeholders.','resultado':'PASS' if all(c['resultado']=='PASS' for c in checks) else 'FAIL','verificacoes':checks}
(ROOT/'evidencias/p2/verificacao-documental.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'resultado':report['resultado'],'verificacoes':len(checks),'falhas':[c for c in checks if c['resultado']=='FAIL']},ensure_ascii=True))
raise SystemExit(0 if report['resultado']=='PASS' else 1)
