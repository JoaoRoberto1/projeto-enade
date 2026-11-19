"""Gera folha de identificação e links a partir do registro de publicação da P2."""
from pathlib import Path
import sys,argparse,json
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--dependencias');args=parser.parse_args()
if args.dependencias:sys.path.insert(0,str(Path(args.dependencias).resolve()))
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
for name,file in [('Folha','arial.ttf'),('FolhaBold','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Folha',normal='Folha',bold='FolhaBold')
info=json.loads((ROOT/'evidencias/p2/publicacao.json').read_text(encoding='utf-8'))
out=ROOT/'entregaveis/Entrega_P2_ENADE.pdf';c=canvas.Canvas(str(out),pagesize=A4)
c.setTitle('Entrega P2 — Sistema de Apoio ao ENADE');c.setAuthor('João Roberto de Oliveira Felix; Vinicius Lisboa de Albuquerque')
W,H=A4
navy=colors.HexColor('#102C3E');teal=colors.HexColor('#63D8C5');ink=colors.HexColor('#28414D')
c.setFillColor(navy);c.rect(0,H-188,W,188,fill=1,stroke=0);c.setFillColor(teal);c.rect(0,H-188,7,188,fill=1,stroke=0)
def label(x,y,text,size,bold=False,color=ink):c.setFont('FolhaBold' if bold else 'Folha',size);c.setFillColor(color);c.drawString(x,y,text)
def p(text,y,size=11):
 para=Paragraph(text,ParagraphStyle('p',fontName='Folha',fontSize=size,leading=size*1.45,textColor=ink));_,h=para.wrap(W-100,1000);assert y-h>55;para.drawOn(c,50,y-h);return y-h-15
label(50,H-38,'UNIFOR · REQUISITOS E MODELAGEM DE SISTEMAS',9,True,teal)
label(50,H-82,'Sistema de Apoio',29,True,colors.white);label(50,H-119,'ao ENADE',35,True,colors.white)
label(50,H-158,'TRABALHO P2 / SPRINT 2 / M2',10,True,teal)
y=H-219
y=p('<b>João Roberto de Oliveira Felix</b><br/><b>Vinicius Lisboa de Albuquerque</b>',y,12)
y=p('<b>Sprint:</b> 02/11 a 22/11/2026<br/><b>Prazo no AVA:</b> 23/11/2026 às 00h00 — America/Sao_Paulo',y,10.5)
y=p('<b>Protótipo navegável</b><br/><link href="'+info['url']+'" color="#176b64">'+info['url']+'</link>',y,10.5)
y=p('<b>Repositório — entrega P2</b><br/><link href="'+info['github_p2']+'" color="#176b64">'+info['github_p2']+'</link>',y,10.5)
y=p('<b>O que acompanha a entrega</b><br/>SRS 3.0 com 14 casos de uso; revisão de consistência; cinco diagramas UML; 17 wireframes; protótipo navegável com quatro perfis; capturas e verificações técnicas; tarefas vinculadas ao Milestone M2.',y)
y=p('<b>Como explorar</b><br/>Abrir o protótipo e escolher Estudante. Consultar questões, iniciar um simulado, salvar respostas e finalizar para ver o resultado. Os outros perfis permitem explorar revisão de conteúdo, administração e indicadores fictícios.',y,10.5)
access='Acesso público por link.' if info.get('acesso')=='publico' else 'Acesso privado: liberar o acesso do avaliador antes de enviar este link no AVA.'
y=p('<b>Acesso:</b> '+access+'<br/><b>Natureza:</b> protótipo acadêmico com dados fictícios; validação com usuários e envio no AVA dependem de execução real pelo grupo.',y,9.5)
label(50,34,'Versão de entrega · 19/11/2026',8,color=colors.HexColor('#526A74'));c.save();print(out)
