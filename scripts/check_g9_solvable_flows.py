#!/usr/bin/env python3
"""Noncommutative deck-group controls for the general unfolding theorem."""
from pathlib import Path
import json,random
from g9_solvable_flows import SolvableFlows
from g9_flow_unfolding import unfold,strict_halfspace,flow,inverse

out=Path('research/certificates/G9-solvable-extension');out.mkdir(parents=True,exist_ok=True)
assert not (out/'checks.json').exists()
rng=random.Random(929260955);fixtures=[];checked=[];relations=[]


def comm(u,v):return inverse(u)+inverse(v)+u+v


for rank,depth,bound in [(2,2,7),(2,3,7),(3,3,5),(2,4,5)]:
    group=SolvableFlows(rank);count=0;noncommuting=0;words=0;samples=[]
    def inspect(w):
        global count,noncommuting
        if not strict_halfspace(rank,w):return
        u,spans,_=unfold(rank,w);g=group.word(depth,w);h=group.word(depth,u)
        assert group.decode(depth,h,spans)==g
        assert group.endpoint(depth-1,g[1],group.zero(depth-1))==g[0]
        reflected=tuple(-s if abs(s)==1 else s for s in w)
        assert group.reflect(depth,g)==group.word(depth,reflected)
        assert group.mul(depth,g,group.inv(depth,g))==group.zero(depth)
        if depth==2:assert g[1]==flow(rank,w)
        if depth>=3:
            a=group.gen(depth-1,1);b=group.gen(depth-1,2)
            assert group.mul(depth-1,a,b)!=group.mul(depth-1,b,a)
            noncommuting+=1
        count+=1
        record=[rank,depth,w,u,spans,g,h]
        if len(samples)<12:samples.append(record)
        else:
            j=rng.randrange(count)
            if j<len(samples):samples[j]=record
    def visit(w):
        global words
        words+=1;inspect(w)
        if len(w)==bound:return
        for a in tuple(range(1,rank+1))+tuple(range(-rank,0)):
            if not w or a!=-w[-1]:visit(w+(a,))
    visit(())
    # Strict paths with downward pieces, horizontal loops and genuine relations.
    a=(1,);b=(2,);u=comm(a,b);v=comm(u,inverse(a)+u+a)
    controls=[(1,)*7+v+(-1,)*5+(2,)+(1,)*3+(-2,)+(-1,)*2+(1,),
              (1,)*5+(2,3,-2,-3) if rank==3 else (1,)*5+(2,1,-2,-1)]
    for _ in range(20):
        w=[];height=0
        for i in range(24):
            options=[s for s in tuple(range(1,rank+1))+tuple(range(-rank,0)) if height+(s if abs(s)==1 else 0)>0]
            s=rng.choice(options);w.append(s);height+=s if abs(s)==1 else 0
        controls.append(tuple(w))
    for w in controls:
        inspect(w)
        if depth==3:
            z,spans,_=unfold(rank,w);fixtures.append([rank,depth,w,z,spans,group.word(depth,w),group.word(depth,z)])
    if depth==3:fixtures.extend(samples)
    checked.append(dict(rank=rank,derived_length=depth,exhaustive_radius=bound,words=words,unfoldings=count,noncommutative_deck_checks=noncommuting))
    print(checked[-1])
    # Limit cache use between suites.
    for method in ['zero','gen','mul','inv','reflect','word']:getattr(group,method).cache_clear()

group=SolvableFlows(2);w=(1,2,-1,-2)
for depth in range(1,4):
    g=group.word(depth,w);nextg=group.word(depth+1,w)
    assert g==group.zero(depth) and nextg!=group.zero(depth+1)
    relations.append(dict(trivial_derived_length=depth,nontrivial_derived_length=depth+1,word=w,length=len(w)))
    w=comm(w,(-1,)+w+(1,))
data=dict(seed=929260955,suites=checked,derived_relations=relations,gap_fixtures=fixtures)
(out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(out/'fixtures.g').write_text('G9SolvableFixtures := '+json.dumps(fixtures)+';\n'+'G9SolvableRelations := '+json.dumps([[r['trivial_derived_length'],r['word']] for r in relations])+';\n')
print('GAP_FIXTURES',len(fixtures),'RELATION_LENGTHS',[r['length'] for r in relations])
print('PASS G9 SOLVABLE FLOWS')
