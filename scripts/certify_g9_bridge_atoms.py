#!/usr/bin/env python3
"""Explicit rank-two atom alphabet and exact lower growth bound."""
import json
from collections import Counter
from pathlib import Path
from g9_flow_unfolding import flow,rational_code_bound

OUT=Path('research/certificates/G9-bridge-atoms')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'certificate.json').exists(),'Preserve old evidence'
bound=14
atoms={};visited=0;bridges=0


def visit(w,x,maximum):
    global visited,bridges
    if w:
        visited+=1
        if x==maximum:
            bridges+=1
            f=flow(2,w)
            crossing=Counter(v[0] for v,j,c in f if j==0)
            # Algebraic total across every intermediate cut must be one.
            if not any(crossing[h]==1 for h in range(1,x)):
                old=atoms.get(f)
                if old is None or len(w)<len(old):atoms[f]=w
    if len(w)==bound:return
    for s in (1,-1,2,-2):
        if w and s==-w[-1]:continue
        nx=x+(s if abs(s)==1 else 0)
        if nx>0:visit(w+(s,),nx,max(maximum,nx))


visit((),0,0)
words=sorted(atoms.values(),key=lambda w:(len(w),w))
counts=Counter(map(len,words))
independent=json.loads(Path('results/g9-bridge-atoms-r2-n14-v1/stdout.log').read_text().splitlines()[0])
assert [counts[n] for n in range(bound+1)]==independent['irreducible_counts']
assert visited==independent['halfspace_words'] and bridges==independent['bridge_words']
lower=rational_code_bound(counts,denominator=1000000000)
assert lower['numerator']>2638158531
data=dict(rank=2,max_length=bound,strict_halfspace_words=visited,
          bridge_words=bridges,distinct_atom_elements=len(words),
          counts_by_minimum_bridge_length=[counts[n] for n in range(bound+1)],
          lower_bound=lower,word_certificates=words,
          comparison_source='results/g9-bridge-atoms-r2-n14-v1/stdout.log')
(OUT/'certificate.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'fixtures.g').write_text('G9AtomWords := '+json.dumps(words)+';\n'+
    'G9AtomCounts := '+json.dumps([counts[n] for n in range(bound+1)])+';\n'+
    'G9AtomLower := '+json.dumps([lower['numerator'],lower['denominator']])+';\n')
print('words',visited,'bridges',bridges,'atoms',len(words),'counts',dict(counts))
print('certified rational lower',lower['numerator'],'/',lower['denominator'])
print('PASS G9 BRIDGE ATOM CERTIFICATE')
