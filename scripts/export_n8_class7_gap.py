#!/usr/bin/env python3
"""Translate exact JSON certificates to GAP syntax; no mathematical calculation."""
import json
from pathlib import Path
p=Path('research/certificates/N8-class7')
checks=json.loads((p/'checks.json').read_text())
quadratics=json.loads((p/'quadratics.json').read_text())
kernel=json.loads((p/'degree6-minor.json').read_text())

def gap(value):
    if value is None:return 'fail'
    if isinstance(value,bool):return str(value).lower()
    if isinstance(value,list):return '['+','.join(map(gap,value))+']'
    return str(value)

arithmetic=[];groups=[]
for c in checks['arithmetic']+[q['certificate'] for q in quadratics]:
    arithmetic.append([c[k] for k in ('matrix','D','S','T','coefficients',
                                     'rank','candidates','period','chosen')])
for q in quadratics:
    c=q['certificate']
    groups.append([q[k] for k in ('word','x0','y0','vector','kernel','u','v','axes','samples')]
                  +[c['coefficients'],[list(v) for v in zip(*c['matrix'])]])
# The basis itself is taken from the exact Hall words stored by the run.
# Recover it from the same deterministic Hall construction in a separately
# recorded mathematical check, rather than doing unrecorded work here.
words=json.loads((p/'hall7.json').read_text())
(p/'quadratic-fixtures.g').write_text(
    'N8C7Arithmetic := '+gap(arithmetic)+';\n'+
    'N8C7Quadratics := '+gap(groups)+';\n'+
    'N8C7Hall7 := '+gap(words)+';\n'+
    'N8C7Minor := '+gap([kernel['hall_basis'][str(d)] for d in (2,3,4)])+';\n')
print('Exported',len(arithmetic),'arithmetic and',len(groups),'group certificates')
