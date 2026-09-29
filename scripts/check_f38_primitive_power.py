#!/usr/bin/env python3
"""Exact finite controls of the primitive-power theorem and Nielsen formula."""
from itertools import product
import json
from pathlib import Path
from f38_stabilizer_obstruction import apply, cyclic, compose, identity, inv
from f38_primitive_power import (nielsen, nielsen_profile, profile_length,
    witness_twists, primitive_power_comparison)

OUT=Path('research/certificates/F38-primitive-power')
OUT.mkdir(parents=True,exist_ok=True)
assert not (OUT/'checks.json').exists(), 'Preserve evidence'
formulas=[]
records=[]
powers=(-3,-1,0,1,2,5)
counts={}
for rank,maxlength in ((3,5),(4,4),(5,3)):
    alphabet=tuple(range(-rank,0))+tuple(range(1,rank+1))
    words=set()
    def visit(w):
        if w and w[0]!=-w[-1]: words.add(cyclic(w))
        if len(w)==maxlength:return
        for x in alphabet:
            if not w or x!=-w[-1]:visit(w+(x,))
    visit(())
    counts[rank]=len(words)
    for w in sorted(words):
        growth=[]
        for b,c in witness_twists(rank):
            profile=nielsen_profile(w,b,c)
            lengths=[]
            for power in powers:
                exact=len(cyclic(apply(nielsen(rank,b,c,power)[0],w)))
                assert exact==profile_length(profile,power)
                if power>=profile['threshold']:
                    assert exact==profile['growth']*power+profile['eventual_intercept']
                lengths.append(exact)
            growth.append(profile['growth'])
            formulas.append([rank,w,b,c,lengths,profile['growth'],profile['threshold'],profile['eventual_intercept']])
        assert (not any(growth)) == all(abs(x)==1 for x in w)

# Full normalization/transport cases, including negative roots and conjugates.
for rank in (3,4,5):
    psi=compose(nielsen(rank,1,2),compose(nielsen(rank,2,3),nielsen(rank,3,1)))
    for j,(u,v,kind) in enumerate([
        ((1,1),(-1,-1,-1),'positive'),
        ((1,),(1,1,2,-1,-2),'negative'),
        ((1,),(2,3,-2,-3),'negative'),
        ((1,), (rank,), 'negative'),
        ((1,1),(1,1,1),'positive'),
        ((1,2,-1,-2),(1,),'negative_swapped'),
    ]):
        u=apply(psi[0],u);v=apply(psi[0],v)
        # Use conjugation and a negative primitive root on an additional branch.
        if j==4:u=inv(u)
        u=(rank,)+u+(-rank,)
        result=primitive_power_comparison(rank,u,v)
        assert result['status']==('bounded_same_primitive_cyclic_group' if kind=='positive' else 'not_boundedly_equivalent')
        if kind=='negative_swapped':assert result['swapped']
        if kind!='positive':
            mu=result['normalization']['automorphism']
            for n in (0,1,3,7):
                image=result['moved']
                for _ in range(n):image=apply(result['witness'][0],image)
                normalized=cyclic(apply(mu[0],image))
                assert len(normalized)==profile_length(result['profile'],n)
                assert len(normalized)<=result['normalization_lipschitz']*len(cyclic(image))
        records.append(result)
assert primitive_power_comparison(2,(1,),(1,1,2,-1,-2))['status']=='unsupported_rank'
assert primitive_power_comparison(3,(1,2,-1,-2),(1,3,-1,-3))['status']=='unsupported_no_primitive_power'
data=dict(cyclic_word_counts=counts,powers=powers,formula_records=formulas,normalization_cases=records)
(OUT/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
(OUT/'formulas.g').write_text('F38Powers := '+json.dumps(powers)+';\nF38NielsenFormulas := '+json.dumps(formulas)+';\n')
gap_records=[]
for r in records:
    mu=r['normalization']['automorphism']
    if r['status']=='not_boundedly_equivalent':
        gap_records.append([r['rank'],r['fixed'],r['moved'],mu,r['normalization']['exponent'],0,
                            r['changed'],r['multiplier'],r['witness'],r['profile']['growth'],
                            r['profile']['threshold'],r['profile']['eventual_intercept']])
    else:
        gap_records.append([r['rank'],r['fixed'],r['moved'],mu,r['normalization']['exponent'],r['moved_exponent'],0,0,[],0,0,0])
(OUT/'normalizations.g').write_text('F38PrimitiveCases := '+json.dumps(gap_records)+';\n')
print(json.dumps(dict(cyclic_words=counts,nielsen_formulas=len(formulas),substitutions=len(formulas)*len(powers),normalizations=len(records))))
print('PASS F38 PRIMITIVE POWER CONTROLS')
