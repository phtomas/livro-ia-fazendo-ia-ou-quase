#!/usr/bin/env python3
"""Gera blocos DOCX de revisão a partir de fontes QMD SEM editar o manuscrito.

Necessita pandoc (>=3) e python-docx. Uso:
  python scripts/gerar_blocos_docx.py A --out Bloco_A.docx --apply
  python scripts/gerar_blocos_docx.py B --dry-run
O artefato DOCX é apenas interface de revisão; a fonte canônica continua no Git/Quarto.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
CAPS={
    'A':['index.qmd',*[f'chapters/{n:02d}-' for n in range(1,5)]],
    'B':[f'chapters/{n:02d}-' for n in range(5,9)],
    'C':[f'chapters/{n:02d}-' for n in range(9,13)],
    'D':[f'chapters/{n:02d}-' for n in range(13,17)],
    'E':[f'chapters/{n:02d}-' for n in range(17,22)],
    'F':['appendices/10-principios.qmd','appendices/glossario.qmd','references.qmd']
}
# Mantém a numeração GLOBAL mesmo quando o DOCX contém apenas um bloco.
# A: capítulos 1–4; B: 5–8; C: 9–12; D: 13–16; E: 17–21.
NUMBER_OFFSETS={'A':0,'B':4,'C':8,'D':12,'E':16,'F':0}

def fontes(root:Path,bloco:str)->list[Path]:
    result=[]
    for pattern in CAPS[bloco]:
        if pattern.endswith('-'):
            found=sorted(root.glob(pattern+'*.qmd'))
            if len(found)!=1:raise ValueError(f'Esperado um arquivo para {pattern}: {len(found)}')
            result+=found
        else:
            f=root/pattern
            if not f.is_file():raise FileNotFoundError(f)
            result.append(f)
    return result

def referencia_docx(dest:Path)->None:
    from docx import Document
    from docx.shared import Pt,Cm,RGBColor
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    d=Document();sec=d.sections[0]
    sec.page_width=Cm(16);sec.page_height=Cm(23)
    sec.top_margin=Cm(2);sec.bottom_margin=Cm(1.9);sec.left_margin=Cm(2.2);sec.right_margin=Cm(1.9)
    n=d.styles['Normal'];n.font.name='Liberation Serif';n.font.size=Pt(11);n.font.color.rgb=RGBColor(29,35,43)
    n.paragraph_format.line_spacing=1.15;n.paragraph_format.space_after=Pt(6)
    for name,size in [('Title',21),('Heading 1',16),('Heading 2',12.5),('Heading 3',11.5)]:
        s=d.styles[name];s.font.name='Liberation Sans';s.font.size=Pt(size);s.font.bold=True
        s.font.color.rgb=RGBColor(30,56,83)
        s.paragraph_format.keep_with_next=True;s.paragraph_format.space_before=Pt(14);s.paragraph_format.space_after=Pt(6)
    for name,color in [('Bloco Pratica IA','EAF1F6'),('Bloco Experimento','F1F4EB'),('Cartao Conceito','F3F5F6')]:
        s=d.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH);s.base_style=n
        s.font.name='Liberation Serif';s.font.size=Pt(10)
        s.paragraph_format.left_indent=Cm(.25);s.paragraph_format.right_indent=Cm(.25)
        s.paragraph_format.space_after=Pt(3)
        ppr=s.element.get_or_add_pPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),color);ppr.append(sh)
    footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run('IA fazendo IA — ou quase | Bloco de revisão — não é prova de impressão')
    footer.style=n
    d.save(dest)

def ajustar_numeracao_word(dest:Path,bloco:str)->None:
    """Corrige o limite do Pandoc DOCX: --number-offset é ignorado pelo writer DOCX.

    Não edita títulos do manuscrito QMD; atualiza somente números de estilo
    SectionNumber nos headings do Word para manter 5.1, 5.2... no bloco B.
    """
    import re
    from docx import Document
    offset=NUMBER_OFFSETS[bloco]
    if not offset or bloco=='F':return
    d=Document(dest)
    changed=0
    for para in d.paragraphs:
        if not para.style.name.startswith('Heading'):continue
        if not para.runs:continue
        run=para.runs[0]
        # Pandoc escreve w:rStyle=SectionNumber mesmo quando o estilo não
        # consta em styles.xml; python-docx retorna Default Paragraph Font.
        style_tag=run._r.rPr.rStyle if run._r.rPr is not None else None
        if style_tag is None or style_tag.val!='SectionNumber':
            continue
        match=re.fullmatch(r'(\d+)(\.\d+(?:\.\d+)*)?',run.text.strip())
        if not match:continue
        run.text=str(int(match.group(1))+offset)+(match.group(2) or '')
        changed+=1
    if not changed:raise RuntimeError('DOCX sem numeração reconhecida: Pandoc mudou o formato')
    d.save(dest)

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bloco',choices=list(CAPS))
    parser.add_argument('--out',type=Path)
    run=parser.add_mutually_exclusive_group()
    run.add_argument('--apply',action='store_true',help='gerar Word')
    run.add_argument('--dry-run',action='store_true',help='mostrar entradas sem gravar (padrão)')
    args=parser.parse_args()
    src=fontes(ROOT,args.bloco)
    out=args.out or (ROOT/'dist'/f'Bloco_{args.bloco}_revisao.docx')
    print('Bloco',args.bloco, 'entradas:',*(str(p.relative_to(ROOT)) for p in src),sep='\n - ')
    print('Saída:',out)
    if not args.apply:return 0
    if shutil.which('pandoc') is None:parser.error('pandoc não disponível')
    out.parent.mkdir(parents=True,exist_ok=True)
    ref=out.parent/'.referencia_blocos.docx'
    referencia_docx(ref)
    cmd=['pandoc',*[str(x) for x in src],'-f','markdown+fenced_divs+raw_tex','-t','docx','-s',
         '--number-sections','--top-level-division=chapter',
         '--number-offset='+str(NUMBER_OFFSETS[args.bloco]),
         '--citeproc','--bibliography=references.bib','--csl=estilo-referencias.csl','--resource-path=.',
         '--lua-filter=filters/docx_blocos.lua']
    if args.bloco!='F':cmd+=['--lua-filter=filters/docx_sem_referencias.lua']
    cmd+=['--reference-doc='+str(ref),'-o',str(out)]
    subprocess.run(cmd,cwd=ROOT,check=True)
    ajustar_numeracao_word(out,args.bloco)
    print('DOCX gerado:',out)
    return 0

if __name__=='__main__':raise SystemExit(main())
