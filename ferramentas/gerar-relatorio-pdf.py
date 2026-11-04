"""Consolida os Markdown atuais em PDF complementar, sem alterar suas fontes."""
from pathlib import Path
from urllib.parse import urlsplit, quote
import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', default='C:/Windows/Fonts', help='Pasta contendo arial.ttf, arialbd.ttf e ariali.ttf')
parser.add_argument('--dependencias', help='Pasta opcional de bibliotecas Python instaladas com pip --target')
args = parser.parse_args()
if args.dependencias:
    sys.path.insert(0, str(Path(args.dependencias).resolve()))
import markdown
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, NextPageTemplate, Table, TableStyle, Image
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/JoaoRoberto1/projeto-enade/blob/docs/m1-requirements-and-uml/'
font_dir = Path(args.font_dir)
for name, file in [('Doc', 'arial.ttf'), ('DocBold', 'arialbd.ttf'), ('DocItalic', 'ariali.ttf'), ('DocBoldItalic', 'arialbi.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / file)))
pdfmetrics.registerFontFamily('Doc', normal='Doc', bold='DocBold', italic='DocItalic', boldItalic='DocBoldItalic')
styles = getSampleStyleSheet()
for name in styles.byName:
    styles[name].fontName = 'Doc'
styles['BodyText'].fontSize = 9
styles['BodyText'].leading = 13
styles['BodyText'].spaceAfter = 6
for level in range(1, 5):
    s = styles[f'Heading{level}']
    s.fontName = 'DocBold'
    s.textColor = colors.HexColor('#18384c')
    s.spaceBefore = 12
    s.spaceAfter = 7
styles['Heading1'].fontSize = 18
styles['Heading1'].leading = 22
styles['Heading2'].fontSize = 13
styles['Heading2'].leading = 17
small = ParagraphStyle('SmallDoc', parent=styles['BodyText'], fontSize=7.5, leading=10)
cellstyle = ParagraphStyle('CellDoc', parent=styles['BodyText'], fontSize=8, leading=11, spaceAfter=2)
cover = ParagraphStyle('CoverDoc', parent=styles['Title'], fontName='DocBold', fontSize=26, leading=32, textColor=colors.HexColor('#18384c'), alignment=TA_CENTER)

width, height = A4
usable_w, usable_h = width - 88, height - 100
wide_width, wide_height = landscape(A3)

class Report(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(path, pagesize=A4, leftMargin=44, rightMargin=44, topMargin=48, bottomMargin=52, title='Sistema de Apoio ao ENADE — P1 / M1 — versão 2.0', author='João Roberto de Oliveira Felix; Vinicius Lisboa de Albuquerque')
        self.addPageTemplates(PageTemplate(id='normal', frames=Frame(44,52,usable_w,usable_h,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0), onPage=self.decorate))
        self.addPageTemplates(PageTemplate(id='wide', pagesize=landscape(A3), frames=Frame(44,52,wide_width-88,wide_height-100,id='widebody',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0), onPage=self.decorate))
    def decorate(self, canvas, doc):
        if doc.page == 1:
            self.draw_cover(canvas)
            return
        canvas.saveState()
        canvas.setFont('Doc', 8)
        canvas.setFillColor(colors.HexColor('#52616b'))
        page_width, page_height = canvas._pagesize
        canvas.drawString(44, page_height-28, 'UNIFOR  |  Requisitos e Modelagem de Sistemas  |  P1 / M1')
        canvas.drawString(44, 28, 'Versão 2.0 • 04/11/2026 • Propostas para validação')
        canvas.drawRightString(page_width-44, 28, str(doc.page))
        canvas.restoreState()
    def draw_cover(self, canvas):
        canvas.saveState()
        navy = colors.HexColor('#102C3E')
        teal = colors.HexColor('#63D8C5')
        paper = colors.HexColor('#F5F6F2')
        muted = colors.HexColor('#C3D1D8')
        canvas.setFillColor(paper)
        canvas.rect(0, 0, width, height, stroke=0, fill=1)
        canvas.setFillColor(navy)
        canvas.rect(0, 316, width, height-316, stroke=0, fill=1)
        canvas.setFillColor(teal)
        canvas.rect(0, 316, 8, height-316, stroke=0, fill=1)
        canvas.setFillColor(colors.white)
        canvas.setFont('DocBold', 12)
        canvas.drawString(54, 782, 'UNIVERSIDADE DE FORTALEZA')
        canvas.setFont('Doc', 10)
        canvas.setFillColor(muted)
        canvas.drawString(54, 762, 'Requisitos e Modelagem de Sistemas')
        canvas.setStrokeColor(colors.HexColor('#365366'))
        canvas.line(54, 731, width-54, 731)
        canvas.setFont('DocBold', 10)
        canvas.setFillColor(teal)
        canvas.drawString(54, 695, 'TRABALHO P1  /  SPRINT 1  /  M1')
        canvas.setFillColor(colors.white)
        canvas.setFont('DocBold', 36)
        canvas.drawString(54, 620, 'Sistema de Apoio')
        canvas.setFont('DocBold', 54)
        canvas.drawString(54, 558, 'ao ENADE')
        canvas.setFillColor(teal)
        canvas.rect(54, 529, 62, 4, stroke=0, fill=1)
        canvas.setFont('Doc', 15)
        canvas.setFillColor(muted)
        canvas.drawString(54, 492, 'Elicitação de requisitos')
        canvas.drawString(54, 469, 'e modelagem UML inicial')
        canvas.setStrokeColor(colors.HexColor('#365366'))
        canvas.setLineWidth(1)
        canvas.line(364, 388, 432, 421)
        canvas.line(432, 421, 500, 388)
        canvas.line(364, 388, 500, 388)
        for x, y in ((364,388),(432,421),(500,388)):
            canvas.setFillColor(navy)
            canvas.circle(x, y, 7, stroke=1, fill=1)
            canvas.setFillColor(teal)
            canvas.circle(x, y, 2, stroke=0, fill=1)
        canvas.setFont('DocBold', 8)
        canvas.setFillColor(teal)
        canvas.drawString(54, 365, 'PERÍODO ACADÊMICO')
        canvas.setFont('Doc', 11)
        canvas.setFillColor(colors.white)
        canvas.drawString(54, 345, '19 de outubro a 1º de novembro de 2026')
        canvas.setFillColor(colors.HexColor('#54706C'))
        canvas.setFont('DocBold', 9)
        canvas.drawString(54, 264, 'AUTORES')
        canvas.setFillColor(navy)
        canvas.setFont('DocBold', 14)
        canvas.drawString(54, 232, 'João Roberto de Oliveira Felix')
        canvas.drawString(54, 205, 'Vinicius Lisboa de Albuquerque')
        canvas.setStrokeColor(colors.HexColor('#CDD9D4'))
        canvas.line(54, 171, width-54, 171)
        canvas.setFillColor(colors.HexColor('#54706C'))
        canvas.setFont('Doc', 9)
        canvas.drawString(54, 145, 'Versão 2.0  •  04 de novembro de 2026')
        canvas.drawString(54, 128, 'Documentação acadêmica — proposta para validação')
        canvas.setFillColor(colors.HexColor('#246C68'))
        canvas.setFont('Doc', 9)
        repo_url = 'https://github.com/JoaoRoberto1/projeto-enade'
        canvas.drawString(54, 103, repo_url)
        canvas.linkURL(repo_url, (54, 100, 54 + pdfmetrics.stringWidth(repo_url, 'Doc', 9), 114), relative=0, thickness=0)
        canvas.setFillColor(navy)
        canvas.setFont('DocBold', 11)
        canvas.drawString(54, 61, 'FORTALEZA — CE')
        canvas.setFont('Doc', 11)
        canvas.drawRightString(width-54, 61, '2026')
        canvas.restoreState()
    def afterFlowable(self, flowable):
        if getattr(flowable, '_doc_title', False):
            key = flowable._doc_key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.getPlainText(), key, 0, False)
            self.notify('TOCEntry', (0, flowable.getPlainText(), self.page, key))

def inline(element, path):
    out = html.escape(element.text or '')
    for child in element:
        content = inline(child, path)
        if child.tag in ('strong', 'b'):
            out += '<b>' + content + '</b>'
        elif child.tag in ('em', 'i'):
            out += '<i>' + content + '</i>'
        elif child.tag == 'a':
            url = child.get('href', '')
            if not urlsplit(url).scheme and not url.startswith('#'):
                target = (path.parent / url.split('#', 1)[0]).resolve()
                url = BASE + quote(target.relative_to(ROOT).as_posix())
            if url.startswith('#'):
                out += content
            else:
                out += '<link href="' + html.escape(url, quote=True) + '" color="#16668e">' + content + '</link>'
        elif child.tag == 'code':
            out += '<font face="Doc">' + content + '</font>'
        elif child.tag == 'br':
            out += '<br/>'
        elif child.tag != 'img':
            out += content
        out += html.escape(child.tail or '')
    return out

story = [Spacer(1, 1), PageBreak(), Paragraph('Sumário', styles['Heading1'])]
toc = TableOfContents()
toc.levelStyles = [ParagraphStyle('TOC0Doc', fontName='Doc', fontSize=9, leading=13, spaceBefore=4, leftIndent=0, firstLineIndent=0)]
story += [toc]

def convert(element, path):
    tag = element.tag
    if tag in ('h1','h2','h3','h4','h5','h6'):
        level = min(int(tag[1]), 4)
        paragraph = Paragraph(inline(element,path), styles[f'Heading{level}'])
        if tag == 'h1':
            paragraph._doc_title = True
            paragraph._doc_key = path.relative_to(ROOT).as_posix().replace('/','_')
        story.append(paragraph)
    elif tag == 'p':
        images = element.findall('img')
        if images:
            for img in images:
                source = path.parent / img.get('src')
                if source.suffix == '.svg': source = source.with_suffix('.png')
                im = Image(str(source))
                wide = path.parent.name == 'implantacao'
                image_width = wide_width-88 if wide else usable_w
                scale = min(image_width/im.imageWidth, (usable_h-85)/im.imageHeight, 1)
                im.drawWidth,im.drawHeight=im.imageWidth*scale,im.imageHeight*scale
                story.extend([im,Spacer(1,8)])
                if wide:
                    story.extend([NextPageTemplate('normal'),PageBreak()])
        else:
            story.append(Paragraph(inline(element,path),styles['BodyText']))
    elif tag in ('ul','ol'):
        for n,li in enumerate(element.findall('li'),1):
            story.append(Paragraph((f'{n}. ' if tag=='ol' else '• ')+inline(li,path),styles['BodyText']))
    elif tag == 'table':
        rows=element.findall('.//tr')
        if not rows:return
        cells=[[inline(c,path) for c in row if c.tag in ('th','td')] for row in rows]
        # Tabelas largas viram registros rotulados para manter leitura em A4.
        if len(cells[0]) >= 5:
            heads=cells[0]
            for row in cells[1:]:
                text='<br/>'.join(f'<b>{h}:</b> {v}' for h,v in zip(heads,row))
                story.append(Paragraph(text,cellstyle));story.append(Spacer(1,6))
        else:
            data=[[Paragraph(c,cellstyle) for c in row] for row in cells]
            table=Table(data,colWidths=[usable_w/len(cells[0])]*len(cells[0]),repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dce7ed')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f3f6f8')]),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.25,colors.HexColor('#ccd5dc')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([table,Spacer(1,8)])
    elif tag == 'pre':
        text=''.join(element.itertext())
        # Linhas de comando longas são quebradas apenas na visualização do PDF.
        for line in text.splitlines():
            story.append(Paragraph(html.escape(line).replace(' ','&#160;'),small))
    else:
        for child in element: convert(child,path)

ordered = [
    '01-visao/documento-visao.md',
    '02-stakeholders/identificacao-stakeholders.md',
    '03-elicitacao/planejamento-elicitacao.md',
    '03-elicitacao/roteiro-entrevistas.md',
    '03-elicitacao/questionario.md',
    '03-elicitacao/resultados-entrevistas.md',
    '03-elicitacao/validacao-requisitos.md',
    '04-requisitos/requisitos-funcionais.md',
    '04-requisitos/requisitos-nao-funcionais.md',
    '04-requisitos/regras-negocio.md',
    '04-requisitos/matriz-rastreabilidade.md',
    '05-backlog/backlog-priorizado.md',
    '05-backlog/definicao-pronto.md',
    '06-modelagem-uml/README.md',
    '06-modelagem-uml/casos-de-uso/README.md',
    '06-modelagem-uml/componentes/README.md',
    '06-modelagem-uml/implantacao/README.md',
    '07-sprint/planejamento-m1.md',
    '07-sprint/relatorio-sprint1.md',
    '07-sprint/issues/README.md',
    *[f'07-sprint/issues/M1-{n:02d}.md' for n in range(1,14)],
    '08-entrega/checklist-entrega.md',
    '08-entrega/instrucoes-ava.md',
    '08-entrega/validacao-tecnica.md',
]
files = [ROOT/'docs'/p for p in ordered]
files += [ROOT/'evidencias/entrevistas/README.md',ROOT/'evidencias/github/README.md',ROOT/'referencias/README.md']
for path in files:
    if path.parent.name == 'implantacao':
        story.append(NextPageTemplate('wide'))
    story.append(PageBreak())
    rendered=markdown.markdown(path.read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
    root=ET.fromstring('<root>'+rendered+'</root>')
    for element in root: convert(element,path)
    story.append(Paragraph('Fonte editável: <link href="'+BASE+quote(path.relative_to(ROOT).as_posix())+'">'+html.escape(path.relative_to(ROOT).as_posix())+'</link>',small))
destination=ROOT/'entregaveis/Trabalho_P1_ENADE_M1_v2.pdf'
Report(str(destination)).multiBuild(story)
print(f'PDF gerado: {destination} ({len(files)} documentos consolidados).')
