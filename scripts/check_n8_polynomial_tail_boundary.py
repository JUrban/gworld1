#!/usr/bin/env python3
"""Four exact group products show why 2s>n cannot be weakened to 2s>=n."""
import json,time
from fractions import Fraction as Q
from pathlib import Path
from check_n8_polynomial_group_tail import Group
from n8_weighted_automorphisms import add

start=time.monotonic()
# Only products are needed, so no full Hall basis is constructed here.
m=Group.__new__(Group);m.rank=2;m.degree=25;m.weights=(1,4)
m.one={():Q(1)};m.letters=[{(i,):Q(1)} for i in range(2)]
a,e=map(m.exp,m.letters)
def iterate(x,n,bracket):
    for _ in range(n):x=bracket(m.letters[0] if bracket==m.bracket else a,x)
    return x
y=iterate(e,6,m.comm);u=iterate(e,4,m.comm);v=iterate(e,13,m.comm)
print('Actual weighted group words built',flush=True)
f00=m.comm(a,y);f10=m.comm(m.mul(a,u),y)
f01=m.comm(a,m.mul(y,v));f11=m.comm(m.mul(a,u),m.mul(y,v))
mixed=add(add(add(f11,f10,-1),f01,-1),f00)
U=iterate(m.letters[1],4,m.bracket);V=iterate(m.letters[1],13,m.bracket)
expected=m.bracket(U,V)
assert mixed==expected and mixed and all(m.weight(w)==25 for w in mixed)
assert all(n.denominator==1 for n in mixed.values())
out=Path('research/certificates/N8-polynomial-group-tail/boundary25')
out.mkdir(parents=True,exist_ok=False)
data=dict(weights=[1,4],class_bound=25,p=1,q=10,s=7,iterations=[4,13],
 mixed=[[list(w),int(n)] for w,n in sorted(mixed.items())],seconds=time.monotonic()-start)
(out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(out/'fixtures.g').write_text('N8PolynomialTailBoundary := '+json.dumps([data['iterations'],data['mixed']])+';\n')
print('PASS N8 polynomial tail boundary: four actual group products; nonzero weight25 mixed term;',len(mixed),'coefficients',flush=True)
