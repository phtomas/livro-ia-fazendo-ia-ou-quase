#!/usr/bin/env python3
"""Verificação de regressão: boxes de prática em capítulos de IA fazendo IA."""
from pathlib import Path
import re, sys
root = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
files = sorted((root/'chapters').glob('*.qmd'))
required = ('**NA PRÁTICA COM A IA**', '**O que testar.', '**Como proceder.', '**Prompt que usaríamos hoje**', '**Por que funciona.', '**Como verificar.')
if not files:
    print('NO-GO: nenhum capítulo encontrado')
    sys.exit(2)
errors = 0
experimentos = 0
for file in files:
    txt = file.read_text(encoding='utf-8')
    pattern = r"(?ms)^:::[ \t]*\{\.na-pratica-com-ia\}[ \t]*\n(.*?)^:::[ \t]*$"
    blocks = re.findall(pattern, txt)
    expblocks = re.findall(r'(?ms)^:::[ \t]*\{\.experimento-do-leitor\}[ \t]*\n(.*?)^:::[ \t]*$', txt)
    experimentos += len(expblocks)
    if not expblocks:
        print(f'ALERTA {file.relative_to(root)}: experimento autônomo do leitor ausente (avaliar pertinência e registrar exceção).')
    else:
        for exp_i, exp in enumerate(expblocks,1):
            if 'EXPERIMENTO DO LEITOR' not in exp:
                errors += 1
                print(f'FAIL {file.relative_to(root)} experimento {exp_i}: marcador explícito ausente')
            else:
                print(f'PASS {file.relative_to(root)} experimento {exp_i}: marcador explícito presente')
    if not blocks:
        print(f'FAIL {file.relative_to(root)}: box NA PRÁTICA COM A IA ausente')
        errors += 1
        continue
    for i,block in enumerate(blocks,1):
        missing = [s for s in required if s not in block]
        if missing:
            print(f'FAIL {file.relative_to(root)} box {i}: ausentes {missing}')
            errors += 1
        else:
            print(f'PASS {file.relative_to(root)} box {i}: 6 marcadores estruturais presentes')
print(f'Experimentos do leitor encontrados: {experimentos}')
print('AVISO: BOX COM IA e EXPERIMENTO DO LEITOR são recursos didáticos DIFERENTES. PASS estrutural não comprova conteúdo nem diagramação.')
sys.exit(1 if errors else 0)
