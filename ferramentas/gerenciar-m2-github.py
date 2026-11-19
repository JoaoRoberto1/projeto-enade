"""Registra tarefas M2 no GitHub; usa credencial existente do Git somente em memória."""
from pathlib import Path
import argparse,json,os,subprocess,urllib.request,urllib.error

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--preparar',action='store_true')
parser.add_argument('--encerrar',action='store_true')
parser.add_argument('--commit')
args=parser.parse_args()
REPO='JoaoRoberto1/projeto-enade';BASE='/repos/'+REPO;BRANCH='feat/m2-srs-prototipo'
env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='never')
r=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\npath='+REPO+'.git\n\n',capture_output=True,text=True,env=env,cwd=ROOT,timeout=30,check=True)
cred=dict(line.split('=',1) for line in r.stdout.splitlines() if '=' in line)
if not cred.get('password'):raise SystemExit('Credencial GitHub não disponível.')
headers={'Authorization':'Bearer '+cred['password'],'User-Agent':'ENADE-P2-documentacao','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
record={'data_contexto':'2026-11-19','repositorio':REPO,'branch':BRANCH,'consultas':[]}
dest=ROOT/'evidencias/github/estado-m2.json'
if dest.exists():record=json.loads(dest.read_text(encoding='utf-8'))
def save():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def api(path,method='GET',body=None):
 data=json.dumps(body,ensure_ascii=False).encode('utf-8') if body is not None else None
 req=urllib.request.Request('https://api.github.com'+path,data=data,headers={**headers,'Content-Type':'application/json'},method=method)
 try:
  with urllib.request.urlopen(req,timeout=40) as response:
   raw=response.read();record.setdefault('consultas',[]).append({'metodo':method,'endpoint':path,'http':response.status,'data_servidor':response.headers.get('Date')});save();return json.loads(raw) if raw else None
 except urllib.error.HTTPError as exc:raise RuntimeError(f'GitHub {method} {path}: HTTP {exc.code}') from None
def pages(path):
 result=[];page=1
 while True:
  batch=api(path+('&' if '?' in path else '?')+f'per_page=100&page={page}');result.extend(batch)
  if len(batch)<100:return result
  page+=1

repo=api(BASE)
record['repositorio_publico']=not repo['private']
issues=pages(BASE+'/issues?state=all')
milestones=pages(BASE+'/milestones?state=all')
tasks=[]
for p in sorted((ROOT/'docs/12-sprint2/issues').glob('M2-*.md')):
 text=p.read_text(encoding='utf-8');title=text.splitlines()[0].removeprefix('# ')
 tasks.append({'title':title,'text':text,'path':p.relative_to(ROOT).as_posix()})
matches=[m for m in milestones if m['title']=='M2' or m['title'].startswith('M2 —')]
if len(matches)>1:raise SystemExit('Mais de um milestone M2 encontrado; revisar antes de alterar.')
milestone=matches[0] if matches else None
if args.preparar:
 if not milestone:milestone=api(BASE+'/milestones','POST',{'title':'M2 — Sprint 2: SRS, Consistência e Protótipos','description':'Trabalho P2 — Requisitos e Modelagem de Sistemas, Unifor. Período acadêmico 02/11 a 22/11/2026. Registro da preparação em 19/11/2026. Entrega no AVA até 23/11 às 00h00 (America/Sao_Paulo). Validação com usuários e submissão no AVA não são presumidas.','due_on':'2026-11-23T02:59:59Z'})
 for task in tasks:
  existing=[i for i in issues if 'pull_request' not in i and i['title']==task['title']]
  if existing:continue
  body=task['text'].replace('../../../','https://github.com/'+REPO+'/blob/'+BRANCH+'/')
  created=api(BASE+'/issues','POST',{'title':task['title'],'body':body,'milestone':milestone['number'],'labels':['documentation']});issues.append(created)
if not milestone:raise SystemExit('M2 não existe. Executar primeiro com --preparar.')
if args.encerrar:
 if not args.commit:raise SystemExit('--encerrar exige --commit publicado.')
 remote=api(BASE+'/commits/'+args.commit)
 if remote['sha']!=args.commit:raise SystemExit('SHA completo esperado.')
 branch=api(BASE+'/branches/'+BRANCH.replace('/','%2F'))
 if branch['commit']['sha']!=args.commit:raise SystemExit('Commit não é o HEAD publicado da branch P2.')
 tests=json.loads((ROOT/'evidencias/p2/verificacao-prototipo.json').read_text(encoding='utf-8'))
 docs=json.loads((ROOT/'evidencias/p2/verificacao-documental.json').read_text(encoding='utf-8'))
 if tests['resultado']!='PASS' or docs['resultado']!='PASS':raise SystemExit('Verificações devem estar aprovadas antes de encerrar.')
 for task in tasks:
  selected=next((i for i in issues if i.get('title')==task['title'] and 'pull_request' not in i),None)
  if not selected:raise SystemExit('Issue não encontrada: '+task['title'])
  if selected['state']=='closed':continue
  body=task['text'].replace('../../../','https://github.com/'+REPO+'/blob/'+BRANCH+'/')
  body+='\n\n## Evidência de conclusão técnica\n\nArtefato entregue e versionado no commit ['+args.commit[:7]+'](https://github.com/'+REPO+'/commit/'+args.commit+'). Verificações: [documentação](https://github.com/'+REPO+'/blob/'+BRANCH+'/evidencias/p2/verificacao-documental.json) e [protótipo](https://github.com/'+REPO+'/blob/'+BRANCH+'/evidencias/p2/verificacao-prototipo.json).\n\nConclusão desta tarefa não declara entrevistas, aceite institucional ou submissão no AVA.\n'
  api(BASE+'/issues/'+str(selected['number']),'PATCH',{'body':body,'state':'closed','state_reason':'completed'})
 record['commit_entrega']=args.commit
issues=pages(BASE+f'/issues?milestone={milestone["number"]}&state=all')
record['milestone']={k:milestone.get(k) for k in ['number','title','html_url','state','due_on','created_at']}
record['issues']=[{k:i.get(k) for k in ['number','title','html_url','state','state_reason','created_at','closed_at']} for i in issues if 'pull_request' not in i]
record['conclusao']='Registro real de tarefas documentais e do protótipo. Envio no AVA e validação com usuários não foram executados por este script.'
save()
print(json.dumps({'milestone':record['milestone']['html_url'],'issues':len(record['issues']),'fechadas':sum(i['state']=='closed' for i in record['issues'])},ensure_ascii=True))
