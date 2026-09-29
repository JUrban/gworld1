#!/usr/bin/env python3
"""Bounded exhaustive flow/bridge audit and small certified growth bounds."""
import json
import random
from pathlib import Path
from collections import Counter,defaultdict
from g9_flow_unfolding import (flow,path,unfold,decode_unfolded,endpoint,
    strict_halfspace,bridge,inverse,growth_interval_data,rational_code_bound)

OUT=Path('research/certificates/G9-flow-unfolding')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists(),'Preserve old evidence'
rng=random.Random(9292609)
samples=[];seen_sample=0;reports=[]


def inspect(rank,w):
    global seen_sample
    original=flow(rank,w)
    unfolded,spans,cuts=unfold(rank,w)
    result=flow(rank,unfolded)
    assert decode_unfolded(rank,result,spans)==original
    assert endpoint(rank,original)==path(rank,w)[-1]
    seen_sample+=1
    record=[rank,w,unfolded,spans,original,result]
    if len(samples)<240:samples.append(record)
    else:
        i=rng.randrange(seen_sample)
        if i<len(samples):samples[i]=record
    return original,result,spans


for rank,bound in ((2,10),(3,6),(1,8)):
    alphabet=tuple(range(1,rank+1))+tuple(range(-rank,0))
    elements={};half={};bridges=defaultdict(dict);codes={}
    words=0;unfoldings=0;max_pieces=0;duplicates=0
    def visit(w):
        global words,unfoldings,max_pieces,duplicates
        words+=1
        f=flow(rank,w)
        if f not in elements or len(w)<elements[f]:elements[f]=len(w)
        if strict_halfspace(rank,w):
            unfoldings+=1
            original,out,spans=inspect(rank,w)
            max_pieces=max(max_pieces,len(spans))
            code=(out,spans)
            if code in codes:assert codes[code]==original;duplicates+=1
            else:codes[code]=original
            if f not in half or len(w)<half[f]:half[f]=len(w)
            if bridge(rank,w):
                height=path(rank,w)[-1][0]
                old=bridges[height].get(f)
                if old is None or len(w)<len(old):bridges[height][f]=w
        if len(w)==bound:return
        for x in alphabet:
            if not w or x!=-w[-1]:visit(w+(x,))
    visit(())
    ball=[sum(l<=n for l in elements.values()) for n in range(bound+1)]
    halfcounts=[sum(l<=n for l in half.values()) for n in range(bound+1)]
    bridge_data=[]
    concat_checks=0
    concat_samples=[]
    for height,entries in sorted(bridges.items()):
        counts=Counter(map(len,entries.values()))
        codebound=rational_code_bound(counts)
        bridge_data.append(dict(height=height,distinct_flows=len(entries),bound=codebound))
        chosen=sorted(entries.values(),key=lambda w:(len(w),w))
        if len(chosen)>30:chosen=rng.sample(chosen,30)
        products={}
        for left in chosen:
            for right in chosen:
                product=flow(rank,left+right)
                pair=(flow(rank,left),flow(rank,right))
                assert product not in products or products[product]==pair
                products[product]=pair;concat_checks+=1
                if len(concat_samples)<8:concat_samples.append([rank,height,left,right])
    if rank==1:assert ball==[2*n+1 for n in range(bound+1)]
    if rank==2:
        assert ball[:7]==[2*3**n-1 for n in range(7)]
        assert ball[7]<2*3**7-1, 'Must reach genuine metabelian collisions'
    report=dict(rank=rank,max_length=bound,freely_reduced_words=words,
                ball=ball,halfspace_counts=halfcounts,unfoldings=unfoldings,
                largest_number_of_pieces=max_pieces,duplicate_codes=duplicates,
                bridge_codes=bridge_data,concatenation_checks=concat_checks,
                concatenation_samples=concat_samples,
                interval=growth_interval_data(rank,bound,ball[-1]))
    reports.append(report)
    print(json.dumps({k:report[k] for k in ('rank','max_length','freely_reduced_words','ball','unfoldings','largest_number_of_pieces','concatenation_checks')}),flush=True)
    print('best finite bridge code',max((d['bound']['numerator'],d['height']) for d in bridge_data),'over 1000000',flush=True)

# Long deliberate controls: cancellation, zero-flow relators, and many folds.
c=(1,2,-1,-2);d=(1,)+c+(-1,)
relation=inverse(c)+inverse(d)+c+d
assert not flow(2,relation)
controls=[(2,(1,)*5+(-1,)*4+(1,)*3+(-1,)*2+(1,)),
          (2,(1,)*4+relation+(1,2,-2)),
          (3,(1,)*4+(2,3,-2,-3)+( -1,)*3+(2,3,-2,-3)+(1,)*2),
          (2,(1,2,-1,-2,1))]
unsupported=[]
for rank,w in controls:
    if not strict_halfspace(rank,w):unsupported.append([rank,w]);continue
    original,out,spans=inspect(rank,w)
    unfolded,_,_=unfold(rank,w)
    samples.append([rank,w,unfolded,spans,original,out])
assert unsupported and not strict_halfspace(2,unsupported[0][1])

data=dict(seed=9292609,reports=reports,unfolding_samples=samples,
          deliberately_non_halfspace_controls=unsupported,
          zero_flow_relation=relation,total_unfolding_checks=seen_sample)
(OUT/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'fixtures.g').write_text('G9UnfoldingFixtures := '+json.dumps(samples)+';\n'+
    'G9ConcatenationFixtures := '+json.dumps([c for r in reports for c in r['concatenation_samples']])+';\n'+
    'G9CodeBounds := '+json.dumps([[r['rank'],d['height'],d['bound']['numerator'],d['bound']['denominator'],sorted(d['bound']['counts'].items())] for r in reports for d in r['bridge_codes']])+';\n'+
    'G9ZeroFlowRelation := '+json.dumps(relation)+';\n')
print('PASS G9 FLOW UNFOLDING: exact finite recovery and free-code controls',flush=True)
