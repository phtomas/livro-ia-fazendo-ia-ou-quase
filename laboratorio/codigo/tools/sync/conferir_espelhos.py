#!/usr/bin/env python3
"""Confronta duas árvores locais, sem sincronizar ou modificar as origens.

* Dois diretórios: --canon e --espelho
* Linha-base opcional: --baseline; sem linha-base, não deduz direção das mudanças.
* --snapshot grava um manifesto da origem; --report grava o resultado do confronto.
* Arquivos de saída devem ficar fora das árvores para evitar contaminar o diagnóstico.
* Não segue symlinks; falha fechada se encontrar um.
* Sem rede, Git API, Drive API, IA, deleção ou cópia.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

IGNORAR = {'.git', '_book', '_freeze', '__pycache__', '.quarto', '.venv', 'node_modules', 'dist', '.DS_Store'}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(131072), b''):
            h.update(block)
    return h.hexdigest()


def inventariar(raiz: Path) -> dict[str,str]:
    raiz = raiz.resolve(strict=True)
    if not raiz.is_dir(): raise ValueError('a origem precisa ser diretório')
    saida = {}
    for atual, pastas, arquivos in os.walk(raiz, topdown=True, followlinks=False):
        p = Path(atual)
        for d in list(pastas):
            child = p / d
            if child.is_symlink(): raise ValueError(f'link simbólico recusado: {child.relative_to(raiz)}')
            if d in IGNORAR: pastas.remove(d)
        for nome in arquivos:
            child = p / nome
            if nome in IGNORAR: continue
            if child.is_symlink(): raise ValueError(f'link simbólico recusado: {child.relative_to(raiz)}')
            if not child.is_file(): raise ValueError(f'objeto não regular: {child.relative_to(raiz)}')
            rel = child.relative_to(raiz).as_posix()
            saida[rel] = sha256(child)
    return dict(sorted(saida.items()))


def validar_manifesto(d: object) -> dict[str,str]:
    if not isinstance(d, dict) or d.get('formato') != 'espelhos-v1' or not isinstance(d.get('arquivos'), dict):
        raise ValueError('manifesto de linha-base inválido')
    for nome, hash_ in d['arquivos'].items():
        if not isinstance(nome,str) or nome.startswith('/') or '..' in Path(nome).parts or not isinstance(hash_,str) or len(hash_) != 64 or any(c not in '0123456789abcdef' for c in hash_):
            raise ValueError('entrada inválida no manifesto')
    return d['arquivos']


def classificar(a: dict, b: dict, base: dict|None) -> list[dict]:
    itens = []
    nomes = sorted(set(a)|set(b)|(set(base) if base is not None else set()))
    for p in nomes:
        aa, bb = a.get(p), b.get(p)
        if base is None:
            status = ('IDENTICO' if aa == bb else 'APENAS_CANON' if bb is None else 'APENAS_ESPELHO' if aa is None else 'DIVERGENTE')
        else:
            old = base.get(p)
            if aa == bb: status = 'IDENTICO' if aa is not None else 'REMOVIDO_AMBOS'
            elif aa == old and bb != old: status = 'ALTERADO_ESPELHO'
            elif bb == old and aa != old: status = 'ALTERADO_CANON'
            elif old is None and aa is None: status = 'NOVO_ESPELHO'
            elif old is None and bb is None: status = 'NOVO_CANON'
            else: status = 'CONFLITO_OU_DUAS_MUDANCAS'
        if status == 'REMOVIDO_AMBOS': continue
        itens.append({'arquivo':p,'estado':status,'canon_sha256':aa,'espelho_sha256':bb})
    return itens


def gravar(destino:Path, dados:dict, bases:list[Path]):
    dest = destino.resolve()
    for raiz in bases:
        if dest == raiz or raiz in dest.parents:
            raise ValueError('o relatório/manifesto deve ficar fora das árvores auditadas')
    dest.parent.mkdir(parents=True,exist_ok=True)
    # Substituição atômica do relatório apenas, nunca das origens.
    tmp = dest.with_name(dest.name+'.tmp')
    tmp.write_text(json.dumps(dados,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    os.replace(tmp, dest)


def main(argv=None)->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--canon',type=Path,required=True)
    p.add_argument('--espelho',type=Path)
    p.add_argument('--baseline',type=Path)
    p.add_argument('--snapshot',type=Path,help='grava manifesto da árvore canônica e encerra')
    p.add_argument('--report',type=Path,help='arquivo JSON de comparação')
    args=p.parse_args(argv)
    try:
        raiz=args.canon.resolve(strict=True)
        if args.snapshot:
            if args.espelho or args.report: raise ValueError('snapshot não combina com comparação')
            dados={'formato':'espelhos-v1','origem':'canon','arquivos':inventariar(raiz)}
            gravar(args.snapshot,dados,[raiz])
            print(f"PASS_MANIFESTO: {len(dados['arquivos'])} arquivos")
            return 0
        if not args.espelho or not args.report: raise ValueError('comparação requer --espelho e --report')
        outro=args.espelho.resolve(strict=True)
        if raiz == outro: raise ValueError('as duas árvores não podem ser a mesma')
        a,b=inventariar(raiz),inventariar(outro)
        base=validar_manifesto(json.loads(args.baseline.read_text(encoding='utf-8'))) if args.baseline else None
        registros=classificar(a,b,base)
        pendencias=[x for x in registros if x['estado']!='IDENTICO']
        saida={'formato':'comparacao-v1','modo':'trilateral' if base is not None else 'bilateral',
               'usa_ia':False,'modifica_fontes':False,'arquivos_canon':len(a),'arquivos_espelho':len(b),
               'iguais':sum(x['estado']=='IDENTICO' for x in registros),'pendencias':len(pendencias),
               'estado':'PASS_IDENTICO' if not pendencias else 'RECONCILIACAO_PENDENTE','itens':registros}
        gravar(args.report,saida,[raiz,outro])
        print(f"{saida['estado']}: {saida['iguais']} iguais, {len(pendencias)} pendências")
        return 0 if not pendencias else 1
    except (ValueError,OSError,KeyError,json.JSONDecodeError) as exc:
        print(f'NO_GO: {exc}',file=sys.stderr)
        return 2
if __name__=='__main__':
    raise SystemExit(main())
