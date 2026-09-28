#!/usr/bin/env python3
"""Exact rank-two class-seven tests and certificates for independent checking."""
import json,random,time
from pathlib import Path
from sympy import Matrix
from n8_class7_rank2 import (Magnus,decide_class7_rank2,polynomial_lattice,
                             integer_roots)
from n8_central import bracket
from n8_ia_orbits import wcomm,wpow

SEED=9282621
rng=random.Random(SEED)
out=Path(__file__).resolve().parents[1]/'research/certificates/N8-class7'
assert not (out/'checks.json').exists()
records=[];witnesses=[];steps=[];quadratics=[];arithmetic=[]

def save():
    (out/'checks.json').write_text(json.dumps(dict(seed=SEED,records=records,
                                                 arithmetic=arithmetic),indent=2)+'\n')
    (out/'fixtures.g').write_text('N8C7Witnesses := '+json.dumps(witnesses)+';\n'
                                +'N8C7Steps := '+json.dumps(steps)+';\n')
    (out/'quadratics.json').write_text(json.dumps(quadratics,indent=2)+'\n')

for coeff,roots in [([1,0,0],[]),([0,2,0],[0]),([1,2,0],[]),
                   ([-4,1,2],[-2,2]),([-2,1,2],[]),([0,0,1],[0,1]),
                   ([0,0,-1],[0,1]),([6,-4,2],[2,3])]:
    assert integer_roots(coeff)==roots,(coeff,integer_roots(coeff),roots)

examples=[([[2,0]],[[0,-4],[0,1],[0,2]],True),
          ([[2,0]],[[0,-2],[0,1],[0,2]],False),
          ([[2,0]],[[1,-4],[0,1],[0,2]],False),
          ([[4]],[[1],[1],[0]],True),
          ([[4]],[[1],[0],[2]],False),
          ([[4]],[[1],[0],[1]],True),
          ([[2,0]],[[0,1],[0,0],[0,0]],False),
          ([[0,0]],[[0,0],[0,0],[0,0]],True)]
for i,(columns,coeff,expected) in enumerate(examples):
    k,certificate=polynomial_lattice(columns,coeff)
    assert (k is not None)==expected,(i,k,certificate)
    arithmetic.append(certificate)

m=Magnus(2,7)
# A concrete degree-six minor proves [L3,L3] intersects [L2,L4] trivially.
lie=lambda d:[m.layer(h['value'],d) for h in m.bydegree[d]]
columns=[bracket(m,lie(3)[0],lie(3)[1])]+[bracket(m,lie(2)[0],v) for v in lie(4)]
words=sorted(set().union(*(set(v) for v in columns)))
matrix=Matrix([[v.get(w,0) for v in columns] for w in words])
_,rows=matrix.T.rref();minor=matrix[list(rows),:]
assert len(rows)==4 and minor.det()!=0
(out/'degree6-minor.json').write_text(json.dumps(dict(
    hall_basis={str(d):[h['word'] for h in m.bydegree[d]] for d in (2,3,4)},
    tensor_words=[[i+1 for i in words[j]] for j in rows],
    minor=[list(map(int,minor.row(j))) for j in range(4)],
    determinant=int(minor.det())),indent=2)+'\n')

def check(word,kind,expected=None,**extra):
    start=time.monotonic();audit=[]
    result=decide_class7_rank2(m,word,audit)
    if expected is not None:assert result['answer']==expected,(kind,word,result)
    if result['answer']:witnesses.append([2,7,word,result['x'],result['y']])
    for row in audit:
        if row['kind']=='quadratic':quadratics.append(dict(word=word,**row))
        else:steps.append([2,row['degree'],word,row['x'],row['y'],
                           row['axes'],row['soluble']])
    row=dict(test=kind,answer=result['answer'],word=word,result=result,
             seconds=round(time.monotonic()-start,3),**extra)
    records.append(row);save()
    print(json.dumps({k:v for k,v in row.items() if k not in ('word','result')}),flush=True)

def higher(word,start,stop):
    word=list(word)
    for d in range(start,stop+1):
        for h in rng.sample(m.bydegree[d],min(2,len(m.bydegree[d]))):
            word+=wpow(h['word'],rng.choice((-1,0,1)))
    return word

for p,q in [(1,2),(1,3),(1,4),(2,3),(1,5),(2,4),(3,3),(1,6),(2,5),(3,4)]:
    for scale in (1,2):
        x=wpow(m.bydegree[p][0]['word'],scale)
        y=wpow(m.bydegree[q][-1]['word'],3 if scale==2 else 1)
        x=higher(x,p+1,7-q);y=higher(y,q+1,7-p)
        check(wcomm(x,y),'constructed_positive',True,p=p,q=q,scale=scale)

# This direction has the genuine nonzero degree-six correction kernel.
for scale in (1,2,3):
    for k in (-2,1,3):
        x=wpow([1],scale)+wpow(m.bydegree[2][0]['word'],k)
        y=wpow(m.bydegree[4][0]['word'],scale)
        y=higher(y,5,6)
        check(wcomm(x,y),'quadratic_direction_positive',True,scale=scale,k=k)

for degree in (3,4,5):
    for case in range(8):
        y=m.bydegree[degree-1][case%len(m.bydegree[degree-1])]['word']
        word=wcomm([1],y)
        for layer in range(degree+1,8):
            word+=wpow(rng.choice(m.bydegree[layer])['word'],rng.choice((-2,-1,1,2)))
        check(word,'middle_perturbation',leading=degree,case=case)

# Central perturbations keep the degree-six affine system soluble in the
# kernel direction and therefore exercise the actual quadratic test.
base=wcomm([1],m.bydegree[4][0]['word'])
for case in range(10):
    word=base+wpow(m.bydegree[7][case]['word'],rng.choice((-2,-1,1,2)))
    check(word,'quadratic_central_perturbation',case=case)

a,b=[2],[1]
for _ in range(4):a=wcomm([1],a);b=wcomm([2],b)
check(a+b,'negative_class5_quotient',False)
check([1],'abelian_boundary',False)
check([],'identity_boundary',True)
check(wcomm([1],[2]),'degree_two_dispatch',True)
assert any(not r['answer'] for r in records if 'perturbation' in r['test'])
assert quadratics
assert any(q['certificate']['chosen'] is None for q in quadratics)
assert any(any(q['certificate']['coefficients'][2]) for q in quadratics)
assert any(r.get('selected_residue',0)>0 for a in records for r in a['result'].get('trace',[]))
print('PASS N8 rank2 class7:',len(records),'targets;',len(witnesses),
      'witnesses;',len(steps),'linear steps;',len(quadratics),'quadratic branches;',
      len(arithmetic),'arithmetic controls')
