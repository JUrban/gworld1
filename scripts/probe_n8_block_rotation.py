#!/usr/bin/env python3
"""Bounded modular probe: can a multilinear Lie tensor be block-cyclic invariant?"""
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

records=[]
for n,shift in [(4,2),(6,2),(6,3)]:
    pivots={};count=0
    for perm in permutations(range(n-1)):
        vector={};count+=1
        for w,c in nested(perm+(n-1,)).items():
            rotated=w[shift:]+w[:shift]
            vector[w]=(vector.get(w,0)+c)%P
            vector[rotated]=(vector.get(rotated,0)-c)%P
        vector={w:c for w,c in vector.items() if c}
        while vector:
            row=min(vector);a=vector[row]
            if row not in pivots:
                inv=pow(a,-1,P);pivots[row]={w:c*inv%P for w,c in vector.items()};break
            for w,c in pivots[row].items():
                v=(vector.get(w,0)-a*c)%P
                if v:vector[w]=v
                else:vector.pop(w,None)
    record=dict(degree=n,shift=shift,prime=P,columns=count,modular_rank=len(pivots))
    records.append(record);print(json.dumps(record),flush=True)
path=Path('research/certificates/N8-block-rotation-probe.json')
assert not path.exists();path.write_text(json.dumps(records,indent=2)+'\n')
print('PASS N8 block-rotation bounded probe')
