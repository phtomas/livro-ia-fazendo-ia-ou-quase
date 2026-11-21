#!/usr/bin/env python3
"""laboratório de IA - Cinco Sistemas de IA: núcleo determinístico e demonstrativo.

Este projeto NÃO implementa um modelo de linguagem nem conecta serviços reais.
Nenhuma chamada de rede, gravação em calendários, processamento financeiro
ou operação sobre documentos privados acontece aqui.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parent
DADOS = ROOT / 'dados'
STOPWORDS = set('o a os as de do da dos das em no na um uma que qual como para por se e ou foi deve sao eh aonde'.split())

def palavras(texto: str) -> list[str]:
    s = unicodedata.normalize('NFKD', texto.lower())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return [x for x in re.findall(r'[a-z0-9]+', s) if len(x) > 2 and x not in STOPWORDS]

def carregar_documentos() -> dict[str, str]:
    return {p.name: p.read_text(encoding='utf-8') for p in sorted(DADOS.glob('*.txt')) if not p.name.startswith('fatura-')}

def recuperar(pergunta: str, docs: dict[str,str] | None = None, top_k: int=2) -> list[dict]:
    docs = carregar_documentos() if docs is None else docs
    q = set(palavras(pergunta))
    if not q: return []
    achados = []
    for nome, texto in docs.items():
        t = Counter(palavras(texto))
        score = sum(min(3, t[p]) for p in q)
        if score: achados.append({'fonte': nome, 'pontos_lexicais': score, 'trecho': texto.strip()[:500]})
    return sorted(achados,key=lambda x:(-x['pontos_lexicais'],x['fonte']))[:top_k]

def responder_documento(pergunta: str) -> dict:
    trechos=recuperar(pergunta)
    if not trechos:
        return {'estado':'SEM_EVIDENCIA','resposta':'Não encontrei evidência nos documentos de demonstração.','fontes': []}
    return {'estado':'TRECHOS_RECUPERADOS_SEM_GERACAO','resposta':'Consulte os trechos abaixo; este protótipo ainda não produz resposta por LLM.','fontes':trechos}

def ler_moeda(valor: str) -> str:
    numero=valor.strip().replace('R$','').replace(' ','').replace('.','').replace(',','.')
    try:
        val=Decimal(numero)
        if val < 0: raise ValueError('valor negativo')
        return str(val.quantize(Decimal('0.01')))
    except (InvalidOperation,ValueError):
        raise ValueError('Moeda inválida: '+valor)

def extrair_fatura(texto: str) -> dict:
    regras={'fornecedor':r'Fornecedor:\s*(.+)', 'numero':r'Número:\s*(\S+)',
            'data':r'Data:\s*(\d\d/\d\d/\d{4})',
            'total':r'Total:\s*(R\$\s*[\d.,]+)', 'imposto':r'Imposto:\s*(R\$\s*[\d.,]+)'}
    bruto={k:(m.group(1).strip() if (m:=re.search(p,texto,re.I)) else None) for k,p in regras.items()}
    ausentes=[k for k,v in bruto.items() if not v]
    out={'dados':bruto, 'campos_ausentes':ausentes, 'estado':'REVISAR' if ausentes else 'EXTRAIDO_PENDENTE_VALIDACAO'}
    if not ausentes:
        try:
            out['dados']['total_brl'] = ler_moeda(bruto['total'])
            out['dados']['imposto_brl'] = ler_moeda(bruto['imposto'])
            datetime.strptime(bruto['data'],'%d/%m/%Y')
            if Decimal(out['dados']['imposto_brl']) > Decimal(out['dados']['total_brl']):
                raise ValueError('Imposto maior que total')
            out['estado']='VALIDADO_ESTRUTURALMENTE_PENDENTE_REVISAO_HUMANA'
        except ValueError as e: out['estado']='ERRO_VALIDACAO';out['erro']=str(e)
    return out

def recepcionista_simulada(transcricao: str, autorizacao: bool=False) -> dict:
    # Não realiza chamada externa, mesmo com autorização explícita: apenas proposta.
    return {'transcricao':transcricao, 'intencao':'agendamento' if any(w in palavras(transcricao) for w in ['marcar','agendar','reservar']) else 'outro',
            'aprovacao_solicitada':True,'aprovacao_recebida':bool(autorizacao),
            'efeito_externo':False,'estado':'SIMULACAO_SEM_CALENDARIO'}

def comparar_fontes(afirmacoes: list[dict]) -> dict:
    # Sinalizador didático: diferenças numéricas não são automaticamente contradição.
    nums=[set(re.findall(r'\b\d+\b',a['texto'])) for a in afirmacoes]
    diferente= len(afirmacoes)>1 and len(set(tuple(sorted(n)) for n in nums))>1
    return {'estado':'DIVERGENCIA_NUMERICA_PARA_REVISAO' if diferente else 'SEM_DIVERGENCIA_NUMERICA_DETECTADA',
            'fontes':afirmacoes,'nota':'A comparação é lexical; uma pessoa precisa verificar contexto, data e validade.'}

def avaliar_casos(casos: list[dict]) -> dict:
    itens=[]
    for c in casos:
        achados=recuperar(c['pergunta'],top_k=c.get('top_k',2))
        fontes=[x['fonte'] for x in achados]
        passou=c['fonte_esperada'] in fontes
        itens.append({'id':c['id'],'pergunta':c['pergunta'],'fonte_esperada':c['fonte_esperada'],
                      'fontes_retornadas':fontes,'passou':passou})
    n=len(itens)
    return {'nome':'hit_at_k_de_recuperacao_lexical','total':n,'aprovados':sum(x['passou'] for x in itens),
            'hit_at_k':round(sum(x['passou'] for x in itens)/n,3) if n else None,
            'escopo':'somente conjunto sintético; NÃO mede veracidade da resposta gerada',
            'executado_em':datetime.now(timezone.utc).isoformat(), 'casos':itens}

def diagnostico()->dict:
    # Inspeção somente leitura; não instala nem modifica nada.
    memoria_mib=None
    try:
        import os
        memoria_mib=round(os.sysconf('SC_PAGE_SIZE')*os.sysconf('SC_PHYS_PAGES')/(1024*1024))
    except Exception: pass
    gpu={'disponivel': False, 'detalhes':'nvidia-smi indisponível'}
    if shutil.which('nvidia-smi'):
        try:
            r=subprocess.run(['nvidia-smi','--query-gpu=name,memory.total,driver_version','--format=csv,noheader'],capture_output=True,text=True,timeout=8)
            gpu={'disponivel':r.returncode==0,'detalhes':r.stdout.strip() or r.stderr.strip()}
        except Exception as e:gpu['detalhes']=str(e)
    return {'sistema':platform.platform(),'python':platform.python_version(),'ram_detectada_mib':memoria_mib,
            'gpu_nvidia':gpu,'uso_da_rede':'nenhum','status':'LEVANTAMENTO_LOCAL_NAO_CERTIFICA_HARDWARE'}

def main():
    p=argparse.ArgumentParser(description='laboratório de IA - protótipo didático sem uso de rede')
    sub=p.add_subparsers(dest='comando',required=True)
    sub.add_parser('diagnostico')
    d=sub.add_parser('documentos'); d.add_argument('pergunta')
    v=sub.add_parser('voz');v.add_argument('transcricao')
    f=sub.add_parser('fatura');f.add_argument('--arquivo',default=str(DADOS/'fatura-exemplo.txt'))
    s=sub.add_parser('pesquisa');s.add_argument('--arquivo',default=str(DADOS/'fontes-pesquisa.json'))
    e=sub.add_parser('avaliar');e.add_argument('--casos',default=str(DADOS/'casos-avaliacao.json'));e.add_argument('--saida',default='')
    args=p.parse_args()
    if args.comando=='diagnostico':r=diagnostico()
    elif args.comando=='documentos':r=responder_documento(args.pergunta)
    elif args.comando=='voz':r=recepcionista_simulada(args.transcricao)
    elif args.comando=='fatura':r=extrair_fatura(Path(args.arquivo).read_text(encoding='utf-8'))
    elif args.comando=='pesquisa':r=comparar_fontes(json.loads(Path(args.arquivo).read_text(encoding='utf-8')))
    else:
        r=avaliar_casos(json.loads(Path(args.casos).read_text(encoding='utf-8')))
        if args.saida:
            out=Path(args.saida);out.parent.mkdir(parents=True,exist_ok=True)
            out.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(r,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
