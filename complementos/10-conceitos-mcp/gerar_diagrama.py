#!/usr/bin/env python3
"""Gera do zero um mapa SVG de 10 conceitos MCP; sem importar gráficos de terceiros."""
from xml.etree.ElementTree import Element, SubElement, tostring
from pathlib import Path
from html import escape
R=Path(__file__).parent
W,H=1600,2240
svg=Element('svg', {'xmlns':'http://www.w3.org/2000/svg','viewBox':f'0 0 {W} {H}','width':str(W),'height':str(H),'role':'img','aria-labelledby':'title desc'})
SubElement(svg,'title',{'id':'title'}).text='10 conceitos essenciais de MCP: arquitetura, dados, ferramentas e segurança'
SubElement(svg,'desc',{'id':'desc'}).text='Mapa de estudo autoral do Model Context Protocol, com fluxo host, cliente e servidor; dez conceitos; transportes e camada de segurança.'

def add(tag,attrs={},text=None,parent=svg):
    e=SubElement(parent,tag,{k:str(v) for k,v in attrs.items()})
    if text is not None:e.text=str(text)
    return e

def rect(x,y,w,h,fill,rad=0,stroke='none',sw=1):return add('rect',{'x':x,'y':y,'width':w,'height':h,'rx':rad,'fill':fill,'stroke':stroke,'stroke-width':sw})
def line(x1,y1,x2,y2,color='#657484',sw=3,dash=None):
    d={'x1':x1,'y1':y1,'x2':x2,'y2':y2,'stroke':color,'stroke-width':sw,'stroke-linecap':'round'}
    if dash:d['stroke-dasharray']=dash
    return add('line',d)
def txt(x,y,s,size=25,color='#142e3d',weight=400,anchor='start',family="DejaVu Sans"):
    return add('text',{'x':x,'y':y,'font-size':size,'fill':color,'font-family':family,'font-weight':weight,'text-anchor':anchor},s)
def circ(x,y,r,fill,stroke='none',sw=1):return add('circle',{'cx':x,'cy':y,'r':r,'fill':fill,'stroke':stroke,'stroke-width':sw})
def path(d,stroke='#284e5f',sw=4,fill='none'):return add('path',{'d':d,'stroke':stroke,'stroke-width':sw,'fill':fill,'stroke-linejoin':'round','stroke-linecap':'round'})
def arrow(x1,y,x2,color='#29607b'):
    line(x1,y,x2,y,color,6);path(f'M{x2-14},{y-13} L{x2},{y} L{x2-14},{y+13}',color,6)

def capsule(x,y,label,colorbg,color='#1d3a50',font=23,padx=18):
    width=max(125,len(label)*font*0.57+padx*2)
    rect(x,y,width,43,colorbg,21)
    txt(x+width/2,y+29,label,font,color,700,'middle')
    return width

rect(0,0,W,H,'#f3f6f6')
rect(0,0,W,155,'#0a283a')
rect(0,153,W,5,'#e2b96b')
txt(60,72,'10 CONCEITOS DE MCP',59,'#ffffff',800)
txt(62,119,'Entenda as peças antes de conectar ferramentas à IA',25,'#c5dcdf')
rect(1202,35,333,78,'#174658',16,stroke='#43788b',sw=2)
txt(1368,68,'GUIA VISUAL',22,'#e8cb91',800,'middle')
txt(1368,94,'revisão 2026-07',20,'#d4e8e9',500,'middle')

txt(60,206,'01  COMO AS PEÇAS SE ENCAIXAM',31,'#195968',800)
# system overview
boxY=232;boxH=295
for x,w,t,sub,accent in [(60,465,'HOST','Aplicação com a IA', '#d7eaf1'),(577,402,'CLIENTE','Conexão gerenciada pelo host','#e3def6'),(1031,509,'SERVIDOR','Disponibiliza capacidades','#dcece3')]:
    rect(x,boxY+5,w,boxH,'#dfe8e7',22)
    rect(x,boxY,w,boxH,'#ffffff',22,stroke='#bbd1d1',sw=2)
    rect(x,boxY,w,67,accent,22)
    rect(x,boxY+46,w,21,accent)
    txt(x+28,boxY+43,t,31,'#11364a',800)
    txt(x+26,boxY+101,sub,23,'#596c73')
# host diagram
rect(93,354,185,118,'#f0f7fc',13,stroke='#9bbcca',sw=2)
circ(133,385,13,'#286a89');rect(115,400,36,34,'#89bccd',8)
txt(167,388,'IA / agente',24,'#16485e',700)
txt(167,424,'decide',20,'#517585')
rect(307,363,187,95,'#f8f9fb',13,stroke='#b3c1cf',sw=2)
txt(399,397,'Clientes',26,'#304c64',700,'middle');txt(399,430,'MCP',27,'#304c64',800,'middle')
arrow(276,411,302,'#427990')
# Client diagram
rect(615,359,329,104,'#f2f0fc',13,stroke='#c5b7ea',sw=2)
txt(780,395,'1 conexão lógica',25,'#514a82',700,'middle')
txt(780,428,'por servidor atendido',22,'#625d8b',400,'middle')
# server diagram
for i,(title,tag,bg) in enumerate([('TOOLS','AÇÕES','#d0ede2'),('RESOURCES','DADOS','#d9e8f1'),('PROMPTS','MODELOS','#f8e8c8')]):
    x=1058+i*158
    rect(x,359,146,104,'#fff',12,stroke='#cbd8d9',sw=2)
    rect(x+10,370,126,33,bg,8)
    txt(x+73,393,title,16,'#173b48',800,'middle')
    txt(x+73,434,tag,22,'#264654',700,'middle')
arrow(529,390,570,'#427990');arrow(983,390,1024,'#427990')
rect(62,547,1477,55,'#e5f3ee',12)
txt(84,584,'Fluxo: pessoa → host com LLM → cliente MCP → servidor → recursos ou ações autorizadas',25,'#1f5b53',700)

txt(60,652,'02  DEZ CONCEITOS, SEM CONFUNDIR FUNÇÕES',32,'#195968',800)

cards=[
 ('01','HOST','Onde a IA é usada','O aplicativo coordena a conversa, os clientes MCP','e as permissões de acesso.','APP', '#d9eaf4'),
 ('02','CLIENTE','Ponte lógica','Componente do host que fala com determinado','servidor e troca mensagens MCP.','LINK','#e9e4fb'),
 ('03','SERVIDOR','Capacidades expostas','Programa local ou remoto que oferece ferramentas,','recursos e modelos de prompt.','SRV','#dcefe5'),
 ('04','TOOLS / FERRAMENTAS','Executar operações','Permitem solicitar ações: consultar, criar, editar.','O host controla autorização e execução.','ACT','#f9e7ca'),
 ('05','RESOURCES / RECURSOS','Consultar informações','Conteúdo acessível por URI: arquivo, documento,','esquema, tabela. Nem tudo é carregado sozinho.','DOC','#e0eff7'),
 ('06','PROMPTS','Reutilizar instruções','Modelos parametrizados de interação. Podem ser','oferecidos pela interface; “/” não é obrigatório.','TXT','#f1e3f8'),
 ('07','TRANSPORTE','Por onde as mensagens passam','Local: stdio. Remoto: Streamable HTTP.','Não confunda transporte com formato dos dados.','NET','#e5f3e7'),
 ('08','JSON-RPC 2.0','Formato das chamadas','Métodos, parâmetros, IDs, respostas e erros.','Exemplo: tools/list e tools/call.','RPC','#e2e9fc'),
 ('09','AUTORIZAÇÃO','Quem pode fazer o quê','Servidores HTTP protegidos usam controles como','OAuth. Conexões locais requerem cuidados próprios.','LOCK','#fcebd4'),
 ('10','REGISTRY / CATÁLOGO','Encontrar servidores','Facilita descoberta e metadados; uma listagem','não certifica segurança nem qualidade.','IDX','#e0eee9'),
]
# 5 rows 2 cols; y 682, row height 260
for index,(num,title,subtitle,line1,line2,ico,bg) in enumerate(cards):
    row=index//2;col=index%2
    x=60+col*755;y=684+row*252;w=724;h=226
    rect(x+5,y+7,w,h,'#e1e9e8',20)
    rect(x,y,w,h,'#ffffff',20,stroke='#d1dfe0',sw=2)
    rect(x+16,y+20,72,56,bg,12)
    txt(x+52,y+59,num,29,'#143b4d',800,'middle')
    txt(x+107,y+57,title,26 if len(title)>18 else 29,'#132e44',800)
    txt(x+29,y+111,subtitle,23,'#0e6970',800)
    txt(x+29,y+152,line1,20,'#354b58')
    txt(x+29,y+182,line2,20,'#354b58')
    # mini icon at bottom right
    rect(x+w-112,y+84,80,112,bg,12)
    if ico=='APP':
        rect(x+w-94,y+112,43,34,'none',5,stroke='#427d96',sw=3);line(x+w-91,y+149,x+w-55,y+149,'#427d96',3)
    elif ico=='LINK':
        circ(x+w-84,y+130,12,'none','#7469ae',4);circ(x+w-56,y+159,12,'none','#7469ae',4);line(x+w-77,y+141,x+w-64,y+148,'#7469ae',4)
    elif ico=='SRV':
        for yy in [112,143]:rect(x+w-99,y+yy,55,20,'none',4,stroke='#3f8d78',sw=3)
    elif ico=='ACT':
        path(f'M{x+w-93},{y+128} L{x+w-73},{y+150} L{x+w-46},{y+116}', '#b6802d',5)
    elif ico=='DOC':
        rect(x+w-90,y+110,43,67,'none',3,stroke='#3b7192',sw=3);line(x+w-82,y+128,x+w-55,y+128,'#3b7192',3);line(x+w-82,y+140,x+w-55,y+140,'#3b7192',3)
    elif ico=='TXT':
        for yy in [117,134,151]:line(x+w-96,y+yy,x+w-49,y+yy,'#806da4',3)
    elif ico=='NET':
        circ(x+w-83,y+118,9,'#57a58d');circ(x+w-53,y+160,9,'#57a58d');line(x+w-80,y+129,x+w-56,y+148,'#57a58d',4)
    elif ico=='RPC':
        txt(x+w-72,y+149,'{}',35,'#536da7',800,'middle')
    elif ico=='LOCK':
        rect(x+w-91,y+141,50,37,'none',4,stroke='#be832f',sw=4);path(f'M{x+w-82},{y+141} v-12 a16,16 0 0 1 32,0 v12','#be832f',4)
    elif ico=='IDX':
        for yy in [114,135,156]:
            circ(x+w-91,y+yy,4,'#3c8e7b');line(x+w-80,y+yy,x+w-48,y+yy,'#3c8e7b',3)

# bottom strip at y 1950
rect(58,1970,1484,145,'#0d3241',19)
txt(91,2022,'EXEMPLO: UMA FERRAMENTA DE DESENHO CAD',28,'#f4dc9a',800)
txt(91,2063,'Pedido → aplicativo host → cliente MCP → servidor CAD → resultado → validação',24,'#eaf5f5')
txt(91,2095,'O modelo solicita; o ambiente executa; a pessoa confere. Nenhum acesso é automático.',19,'#bcd8df')
# footer
txt(61,2165,'Base técnica: Model Context Protocol · versão 2026-07-28 · desenho didático original',18,'#456772')
txt(61,2203,'IA fazendo IA — ou quase  |  Complemento do Laboratório Vivo',20,'#163b4b',700)

xml='<?xml version="1.0" encoding="UTF-8"?>\n'+tostring(svg,encoding='unicode')
out=R/'assets'/'mapa-10-conceitos-mcp.svg';out.write_text(xml,encoding='utf-8')
print('Wrote',out,'bytes',out.stat().st_size)
