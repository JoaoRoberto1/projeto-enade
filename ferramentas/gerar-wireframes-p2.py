"""Gera wireframes vetoriais editáveis, independentes do protótipo de alta fidelidade."""
from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
screens=json.loads((ROOT/'docs/11-prototipos/telas.json').read_text(encoding='utf-8'))
dest=ROOT/'prototipo/wireframes'
dest.mkdir(exist_ok=True)

def rect(x,y,w,h,fill='#fff',stroke='#909090',radius=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'
def text(x,y,s,size=18,bold=False):
    return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="#333" font-weight="{700 if bold else 400}">{escape(s)}</text>'
def line(x,y,w): return f'<line x1="{x}" y1="{y}" x2="{x+w}" y2="{y}" stroke="#a8a8a8" stroke-width="5"/>'
def button(x,y,label,w=180):return rect(x,y,w,44,'#e8e8e8')+text(x+14,y+28,label,16,True)
def inputbox(x,y,label,w=360):return text(x,y,label,16)+rect(x,y+12,w,44,'#fafafa')

for s in screens:
    sid=s['id'];parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc"><title id="title">{escape(sid+" — "+s["titulo"])}</title><desc id="desc">{escape(s["conteudo"])}</desc>',rect(0,0,1200,800,'#fff','#fff')]
    if sid in ['T01','T02']:
        parts += [rect(20,20,500,760,'#f0f0f0'),text(65,90,'TRILHA ENADE',26,True),text(65,330,'Área de apresentação',28,True),line(65,375,355),line(65,400,315),line(65,425,340),text(600,100,s['titulo'],30,True)]
        y=180
        if sid=='T02':parts.append(inputbox(600,y,'Nome de exibição',480));y+=100
        parts += [inputbox(600,y,'E-mail demonstrativo',480),inputbox(600,y+100,'Senha demonstrativa',480),button(600,y+190,'Criar conta' if sid=='T02' else 'Entrar',480),text(600,y+270,'Dados fictícios / mensagem de erro',17)]
        if sid=='T01':parts += [button(600,575,'Estudante',225),button(855,575,'Professor',225),button(600,640,'Coordenador',225),button(855,640,'Administrador',225)]
    else:
        parts += [rect(20,20,200,760,'#f0f0f0'),text(40,65,'TRILHA ENADE',20,True)]
        for i,label in enumerate(['Visão geral','Banco de questões','Simulados','Desempenho','Áreas do perfil','Meu perfil']):parts += [text(40,140+i*55,label,16)]
        parts += [rect(240,20,940,64,'#fafafa'),text(265,61,'Identificação / perfil / sair',17),text(265,140,s['titulo'],30,True),text(265,177,s['casos'],16)]
        if sid=='T03':
            parts += [rect(260,210,890,190,'#f3f3f3'),text(285,255,'Convite para continuar o estudo',23,True),line(285,290,530),button(285,330,'Começar simulado',220)]
            for i,label in enumerate(['Questões disponíveis','Simulados concluídos','Aproveitamento']):parts += [rect(260+i*302,425,285,95),text(275+i*302,460,label,16),text(275+i*302,495,'Valor / estado vazio',17)]
            parts += [rect(260,545,430,195),text(280,580,'Áreas para praticar',20,True),rect(715,545,435,195),text(735,580,'Último resultado',20,True)]
        elif sid in ['T04','T06']:
            parts += [rect(260,210,890,240),inputbox(280,250,'Busca / curso / ano',390),inputbox(715,250,'Área / componente',410)]
            if sid=='T06':parts += [inputbox(280,355,'Quantidade',240),inputbox(550,355,'Duração',240),button(820,367,'Iniciar simulado',300)]
            else:parts += [button(280,365,'Aplicar filtros'),button(490,365,'Limpar filtros')]
            for i in range(2):parts += [rect(260+i*455,475,435,235),text(280+i*455,515,'Orientações / questão',22,True),line(280+i*455,555,350),line(280+i*455,582,305),button(280+i*455,635,'Praticar / informação',300)]
        elif sid in ['T05','T07','T14']:
            parts += [rect(260,210,615,530),text(280,250,'Classificação e enunciado',22,True),line(280,290,550),line(280,320,505)]
            for i in range(4):parts += [rect(280,350+i*57,570,43,'#fafafa'),text(295,378+i*57,f'{chr(65+i)}. Alternativa',17)]
            parts += [button(280,615,'Salvar / confirmar',235),button(535,615,'Próxima / ajustar',235),text(280,705,'Origem / comentário após resposta',17),rect(900,210,250,530),text(920,255,'Contexto',22,True),text(920,305,'Prazo / revisão',17),text(920,350,'Navegação / estado',17),button(920,620,'Finalizar / aprovar',210)]
        elif sid in ['T08','T09','T15']:
            parts += [rect(260,210,890,180,'#f0f0f0'),text(285,255,'Resumo / resultado / estado bloqueado',24,True)]
            for i,label in enumerate(['Acertos','Erros','Em branco']):parts += [text(285+i*260,320,label,20,True),text(285+i*260,355,'Valor / sem dados',17)]
            parts += [rect(260,420,890,280),text(285,460,'Comentários / histórico / tabela de indicadores',22,True)]
            for i in range(4):parts.append(line(285,505+i*40,700-i*55))
            parts.append(button(260,720,'Continuar / nova prática',280))
        elif sid in ['T02','T11','T13']:
            parts += [rect(260,210,890,530)]
            for i,label in enumerate(['Nome / título','Informações permitidas / enunciado','Classificação / campo restrito','Origem / comentário']):parts.append(inputbox(285,255+i*100,label,830))
            parts.append(button(285,675,'Salvar alterações',250))
        else:
            for i in range(3):parts += [rect(260,210+i*155,890,135),text(285,250+i*155,'Conteúdo / identificação / situação',20,True),line(285,285+i*155,540),button(920,265+i*155,'Ação',195)]
            parts += [text(285,720,'Justificativa, mensagem de erro ou campo de contribuição',17)]
    parts += [text(30,790,sid+' · Wireframe de baixa fidelidade · '+s['casos'],14),'</svg>']
    (dest/f'{sid}.svg').write_text(''.join(parts),encoding='utf-8')

cards='\n'.join(f'<article id="{s["id"]}"><header><span>{s["id"]}</span><h2>{escape(s["titulo"])}</h2></header><img src="wireframes/{s["id"]}.svg" alt="{escape(s["conteudo"])}"><p>{escape(s["conteudo"])}</p><p class="meta">{escape(s["casos"])}</p></article>' for s in screens)
html='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Wireframes — Trilha ENADE P2</title><style>
*{box-sizing:border-box}body{margin:0;font:16px/1.6 Arial,sans-serif;background:#f1f4f5;color:#1b3039}main{max-width:1320px;margin:auto;padding:35px 30px}h1{font-size:34px;margin:10px 0}h2{font-size:22px;margin:0}a{color:#176f60}nav{display:flex;gap:18px;flex-wrap:wrap;margin:22px 0}.intro{max-width:850px}.flow{padding:20px;background:white;border:1px solid #d5dfe1;border-radius:10px;margin:22px 0}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}article{background:white;border:1px solid #d5dfe1;border-radius:12px;padding:20px}article header{display:flex;gap:15px;align-items:center}article header span{font-size:14px;color:#596b72}img{width:100%;height:auto;border:1px solid #e4e8e9;margin-top:18px}.meta{font-size:14px;color:#596b72}button{background:#173a40;color:white;border:0;padding:11px 18px;border-radius:7px;font:inherit;cursor:pointer}@media(max-width:760px){.grid{grid-template-columns:1fr}main{padding:22px 16px}}@media print{@page{size:A4 landscape;margin:13mm}body{background:white}.no-print{display:none}.intro-page{break-after:page}.grid{display:block}article{break-after:page;border:0;padding:0}article img{width:80%;max-height:145mm;object-fit:contain}article p{margin:3px 0}article:last-child{break-after:auto}}
</style></head><body><main><section class="intro-page"><p class="meta">TRABALHO P2 · REQUISITOS E MODELAGEM DE SISTEMAS</p><h1>Primeiro a estrutura. Depois a experiência.</h1><p class="intro">Wireframes de baixa fidelidade do Sistema de Apoio ao ENADE. Representam a organização das telas, seus controles e os caminhos de navegação; a aparência final está no protótipo navegável.</p><p>João Roberto de Oliveira Felix<br>Vinicius Lisboa de Albuquerque</p><nav class="no-print"><a href="index.html">Abrir protótipo navegável</a><a href="https://github.com/JoaoRoberto1/projeto-enade/tree/feat/m2-srs-prototipo">Repositório no GitHub</a><button onclick="window.print()">Imprimir wireframes</button></nav><div class="flow"><b>Jornada de estudo:</b> T01 Acesso → T03 Visão geral → T04 Banco → T05 Prática e feedback.<br><b>Jornada de simulado:</b> T03 → T06 Configuração → T07 Respostas → T08 Resultado → T09 Desempenho.<br><b>Jornada editorial:</b> T12 Gestão → T13 Rascunho → T14 Revisão → T12 Publicação.<br><b>Outros fluxos:</b> T02 Cadastro; T10 Discussão; T11 Perfil; T15 Indicadores; T16 Permissões; T17 Moderação.</div><p class="meta">As setas indicam navegação. Erros, bloqueios, confirmações e estados vazios estão descritos no SRS e demonstrados na interface. Simulado e resultado precisam de uma tentativa iniciada.</p></section><div class="grid">'''+cards+'''</div></main></body></html>'''
(ROOT/'prototipo/wireframes.html').write_text(html,encoding='utf-8')
print(f'{len(screens)} wireframes SVG e índice HTML gerados.')
