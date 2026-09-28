#!/usr/bin/env python3
"""Recorded checks of penultimate-layer lifting and its finite branch list."""
import json
import random
import time
from pathlib import Path
from n8_penultimate import Magnus, decide_penultimate, mixed_candidates, equal_candidates
from n8_central import bracket
from n8_ia_orbits import wcomm, wpow, ONE
from n8_class5 import solve as solve5

SEED = 9282618
rng = random.Random(SEED)
out = Path(__file__).resolve().parents[1]/'research/certificates/N8-penultimate'
out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
records, witnesses, branches = [], [], []


def save(row):
    records.append(row)
    (out/'checks.json').write_text(json.dumps(dict(seed=SEED,records=records),indent=2)+'\n')
    (out/'fixtures.g').write_text('N8PenWitnesses := '+json.dumps(witnesses)+';\n'
                                +'N8PenBranches := '+json.dumps(branches)+';\n')
    print(json.dumps({k:v for k,v in row.items() if k not in ('word','result')}),flush=True)


def check(m,word,kind,expected=None,compare=False,**extra):
    started=time.monotonic()
    ans=decide_penultimate(m,word)
    if expected is not None:
        assert ans['answer']==expected,(m.rank,m.degree,kind,ans)
    if compare:
        old=solve5(word,m.rank)
        assert ans['answer']==old['answer'],(m.rank,kind,word,ans,old)
    if ans['answer']:
        witnesses.append([m.rank,m.degree,word,ans['x'],ans['y']])
    if not ans.get('delegated_central'):
        for record in ans['trace']:
            p,q=record['p'],record['q']
            x=m.collect(m.lift(record['C'],p))[0]
            y=m.collect(m.lift(record['D'],q))[0]
            branches.append([m.rank,m.degree,word,x,y,
                             [h['word'] for h in m.bydegree[p+1]],
                             [h['word'] for h in m.bydegree[q+1]],record['soluble']])
    save(dict(test=kind,rank=m.rank,degree=m.degree,answer=ans['answer'],
              seconds=round(time.monotonic()-started,3),word=word,result=ans,**extra))
    return ans


def perturb(m,word,degree):
    answer=list(word)
    for h in rng.sample(m.bydegree[degree],min(2,len(m.bydegree[degree]))):
        answer+=wpow(h['word'],rng.choice((-1,1)))
    return answer


for rank,degree in [(2,c) for c in range(4,10)]+[(3,5),(3,6),(3,7)]:
    started=time.monotonic();m=Magnus(rank,degree)
    save(dict(test='build',rank=rank,degree=degree,seconds=round(time.monotonic()-started,3)))
    for p in range(1,(degree-1)//2+1):
        q=degree-1-p
        for scale in (1,2):
            x=wpow(m.bydegree[p][0]['word'],scale)
            y=wpow(m.bydegree[q][-1]['word'],3 if scale==2 else 1)
            x=perturb(m,x,p+1);y=perturb(m,y,q+1)
            word=wcomm(x,y)
            check(m,word,'constructed_positive',True,
                  compare=degree==5,source_p=p,source_q=q,source_scale=scale)
    # Negative already in the quotient of class degree-1: an independent
    # metabelian Eisenstein obstruction, inherited by the full target.
    if rank==2 and degree>=5:
        a,b=[2],[1]
        for _ in range(degree-2):
            a=wcomm([1],a);b=wcomm([2],b)
        word=a+wpow(b,-2)+m.bydegree[degree][0]['word']
        check(m,word,'negative_leading_Eisenstein',False,compare=degree==5)
    # Independent top-layer perturbations: their leading term IS a bracket.
    # GAP will separately decide every central subgroup-membership branch.
    base=wcomm([1],m.bydegree[degree-2][-1]['word'])
    for case in range(3 if rank==2 else 2):
        word=base+wpow(m.bydegree[degree][case]['word'],1)
        check(m,word,'central_perturbation',compare=degree==5,case=case)

# Direct tests of the finite leading-factor enumeration. Unequal weights
# must retain nonprimitive scale allocations, not just primitive C.
m=Magnus(3,6)
for p,q in [(1,4),(2,3)]:
    c=m.layer(m.bydegree[p][0]['value'],p)
    d=m.layer(m.bydegree[q][-1]['value'],q)
    w=bracket(m,{t:2*n for t,n in c.items()},{t:3*n for t,n in d.items()})
    pairs=mixed_candidates(m,w,p,q)
    cc=m.coordinates({t:2*n for t,n in c.items()},p)
    dd=m.coordinates({t:3*n for t,n in d.items()},q)
    assert (cc,dd) in pairs
    for a,b in pairs:
        assert bracket(m,m.layer(m.lift(a,p),p),m.layer(m.lift(b,q),q))==w
    save(dict(test='all_mixed_scalings',rank=3,degree=6,p=p,q=q,branches=len(pairs)))

# Index six has 1+2+3+6=12 sublattices of Z^2. Every oriented HNF basis
# must occur, not merely one factorization of the same exterior tensor.
c=m.layer(m.bydegree[2][0]['value'],2)
d=m.layer(m.bydegree[2][1]['value'],2)
w=bracket(m,{t:6*n for t,n in c.items()},d)
pairs=equal_candidates(m,w,2)
assert len(pairs)==12
assert len({tuple(a+b) for a,b in pairs})==12
for a,b in pairs:
    assert bracket(m,m.layer(m.lift(a,2),2),m.layer(m.lift(b,2),2))==w
save(dict(test='all_equal_HNF_sublattices',rank=3,degree=6,index=6,branches=12))

assert any(not r['answer'] for r in records if r['test']=='central_perturbation')
assert any(not b[-1] for b in branches)
print('PASS N8 penultimate checks:',len(records),'records;',len(witnesses),
      'positive witnesses;',len(branches),'central membership branches')
