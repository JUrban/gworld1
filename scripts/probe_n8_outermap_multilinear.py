#!/usr/bin/env python3
"""Exact modular ranks of the natural outer-slot map on multilinear Lie pieces.

A full column rank over F_p proves full column rank over Q for that degree.
Lower modular rank alone does not prove a rational kernel. No assertion is made
in unchecked degrees. Basis: right-nested brackets ending in the final letter.
"""
from itertools import permutations
import json
from pathlib import Path
P=1000003
def nested(word):
    if len(word)==1:return {word:1}
    out={}
    for w,c in nested(word[1:]).items():
        a=(word[0],)+w;b=w+(word[0],)
        out[a]=out.get(a,0)+c;out[b]=out.get(b,0)-c
    return {w:c for w,c in out.items() if c}
def outer(poly):
    out={}
    for w,c in poly.items():
        rev=(w[-1],)+w[1:-1]+(w[0],)
        out[w]=(out.get(w,0)+c)%P;out[rev]=(out.get(rev,0)+c)%P
    return {w:c for w,c in out.items() if c}
records=[]
for n in range(3,8):
    pivots={};columns=0;pivot_rows=[]
    for perm in permutations(range(n-1)):
        vec=outer(nested(perm+(n-1,)));columns+=1
        while vec:
            row=min(vec);a=vec[row]
            if row not in pivots:
                inverse=pow(a,-1,P)
                pivots[row]={k:v*inverse%P for k,v in vec.items()}
                pivot_rows.append(list(row));break
            old=pivots[row]
            for k,v in old.items():
                z=(vec.get(k,0)-a*v)%P
                if z:vec[k]=z
                else:vec.pop(k,None)
    record={'degree':n,'prime':P,'columns':columns,'modular_rank':len(pivots),
            'full_column_rank':len(pivots)==columns,'pivot_rows':pivot_rows}
    records.append(record)
    print(json.dumps({k:v for k,v in record.items() if k!='pivot_rows'}),flush=True)
path=Path('research/certificates/N8-outermap-multilinear.json')
if path.exists():raise SystemExit('Refusing to overwrite existing probe certificate')
path.write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 multilinear modular rank probe')
