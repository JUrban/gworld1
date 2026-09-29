#!/usr/bin/env python3
"""Bounded decision controls and independent-verifier fixtures; no proof of Sela."""
from itertools import product
import json
from pathlib import Path
import random
import sys

from f38_bounded_equivalence import bounded_equivalence, one_sided_comparison
from f38_stabilizer_obstruction import (apply, cyclic, compose, identity, inv,
                                       whiteheads)
from f38_primitive_power import nielsen_profile, nielsen, profile_length

OUT = Path('research/certificates/F38-bounded')
OUT.mkdir(exist_ok=False)
(OUT/'versions').mkdir()
for module in list(sys.modules.values()):
    name = getattr(module, '__file__', None)
    if name and Path(name).resolve().parent == Path('scripts').resolve():
        src = Path(name)
        (OUT/'versions'/src.name).write_bytes(src.read_bytes())
records, fixtures, nielsen_rows, rank2_rows = [], [], [], []


def save():
    (OUT/'checks.json').write_text(json.dumps(records, indent=2)+'\n')
    (OUT/'fixtures.g').write_text(
        'F38BoundedFixtures := '+json.dumps(fixtures)+';\n'
        'F38FactorTwists := '+json.dumps(nielsen_rows)+';\n'
        'F38RankTwo := '+json.dumps(rank2_rows)+';\n')


def export(rank, report):
    outcome = report['orbit_check']
    fixtures.append([rank, report['fixed'], report['moved'],
                     1 if outcome['finite'] else 0,
                     outcome['orbit'] if outcome['finite'] else outcome['witness']])


u, v = (1,1,2,2,-1,-2), (1,1,-2,-2,-1,2)
lee = (1,1,2,-1,-2)
comm = (1,2,-1,-2)
cases = [
    ('rank-one-opposite-powers',1,(1,1),(-1,-1,-1),True),
    ('Lee-rank2',2,(1,),lee,True),
    ('Lee-rank3-negative',3,(1,),lee,False),
    ('commutator-primitive-asymmetry',2,(1,),comm,False),
    ('proper-filling-factor',3,u,v,True),
    ('HNN-vertex-filling',3,apply([(1,),(2,1,-2)],u),
                          apply([(1,),(2,1,-2)],v),True),
    ('different-rank3-commutators',3,comm,(1,3,-1,-3),False),
    ('nonminimal-same-primitive-powers',4,(1,2)*2,(1,2)*3,True),
    ('same-commutator-powers',3,comm*2,comm*3,True),
    ('transported-Lee',2,apply([(1,2,2),(2,)],(1,)),
                         apply([(1,2,2),(2,)],lee),True),
]
for label, rank, left, right, expected in cases:
    print('BEGIN',label,flush=True)
    result = bounded_equivalence(rank,left,right)
    assert (result['status']=='boundedly_equivalent') == expected, (label,result)
    records.append(dict(kind='decision',label=label,rank=rank,u=left,v=right,result=result))
    for report in result.get('reports',[]): export(rank,report)
    save()
    print('DECISION',label,result['status'],flush=True)

for label,rank,left,right,expected in [
    ('primitive-to-commutator',2,(1,),comm,True),
    ('commutator-to-primitive',2,comm,(1,),False),
    ('filling-factor-dominates-any-factor-word',3,u,(1,),True),
    ('primitive-does-not-dominate-filling-factor',3,(1,),u,False),
    ('nonsimple-to-outside-factor',3,comm,(3,),False),
]:
    result = one_sided_comparison(rank,left,right)
    assert (result['status']=='bounded_one_side') == expected,(label,result)
    records.append(dict(kind='one-sided',label=label,rank=rank,u=left,v=right,result=result))
    export(rank,result['report']);save()
    print('ONE-SIDED',label,result['status'],flush=True)

invalid = [(0,(1,),(1,)),(2,(),(1,)),(2,(1,-1),(2,)),
           (2,(0,),(1,)),(2,(3,),(1,)),(2,(True,),(1,))]
for args in invalid:
    try: bounded_equivalence(*args)
    except ValueError: pass
    else: raise AssertionError(('invalid input accepted',args))
records.append(dict(kind='invalid-inputs',rejected=len(invalid)))

# The new proper-factor reduction: the two twist profiles cannot both
# vanish on a cyclically reduced word containing the complementary letter.
for rank,b,maxlen in [(3,3,5),(4,3,3),(4,4,3)]:
    alphabet = tuple(range(-rank,0))+tuple(range(1,rank+1))
    words = set()
    def visit(w):
        if w and w[0]!=-w[-1]:words.add(cyclic(w))
        if len(w)==maxlen:return
        for x in alphabet:
            if not w or x!=-w[-1]:visit(w+(x,))
    visit(())
    for word in sorted(words):
        profiles=[nielsen_profile(word,b,a) for a in (1,2)]
        assert all(p['growth']==0 for p in profiles) == all(abs(x)!=b for x in word)
        for a,p in zip((1,2),profiles):
            n=max(2,p['threshold']+1)
            values=[len(cyclic(apply(nielsen(rank,b,a,j)[0],word))) for j in (n,n+1)]
            assert values[1]-values[0]==p['growth']
            assert values==[profile_length(p,j) for j in (n,n+1)]
            nielsen_rows.append([rank,word,b,a,n,values,p['growth']])
    records.append(dict(kind='proper-factor-twists',rank=rank,complement=b,
                        max_cyclic_length=maxlen,cyclic_classes=len(words)))

# Rank-two primitive case: exact word lengths for fixed words in
# <a,bab^-1>, tested under certified ambient automorphisms.
rng=random.Random(9292638)
moves=whiteheads(2)
expressions=[(1,),(2,),(1,2),(1,1,-2),(1,2,-1,-2),(-2,1,2,1)]
for depth in range(13):
    for repetition in range(3):
        alpha=identity(2)
        for _ in range(depth):alpha=compose(rng.choice(moves),alpha)
        A=alpha[0][0];B=alpha[0][1];C=apply(alpha[0],(2,1,-2))
        ell=len(cyclic(A))
        assert len(cyclic(A+inv(C)))==4
        for expr in expressions:
            word=apply(((1,),(2,1,-2)),expr)
            length=len(cyclic(apply(alpha[0],word)))
            assert length<=3*len(expr)*ell
            rank2_rows.append([alpha,expr,word,ell,length])
records.append(dict(kind='rank-two-bound',seed=9292638,automorphisms=39,
                    depth_max=12,word_checks=len(rank2_rows)))

# The identical expression grows under injective non-automorphisms;
# this deliberately rejects the invalid blanket injection replacement.
for n in (2,5,11):
    length=len(cyclic(apply(((1,),(2,)*n),lee)))
    assert length==2*n+3
records.append(dict(kind='injection-boundary',parameters=[2,5,11],
                    comment='Prior Lee pair, not a new universal theorem'))
save()
print('PASS F38 BOUNDED PYTHON',len(fixtures),'orbit fixtures;',
      len(nielsen_rows),'factor twist rows;',len(rank2_rows),'rank-two bounds',flush=True)
