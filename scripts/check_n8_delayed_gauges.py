#!/usr/bin/env python3
"""Universal substitutions after the third exception, with exact periods.

Uses the earlier symplectic-expansion constructor. Instead of a bounded
factorial search, determine an integral power from every coefficient of
the finite Hall-coordinate polynomial. The prior proof supplies the
weight/parameter-degree bound; interpolation is not a guessed fit.
"""
from pathlib import Path
from math import lcm
from fractions import Fraction as Q
import argparse,json,time
import sympy as S
from check_n8_polynomial_group_tail import Group
from n8_universal_gauges import poly_json,terms_json
from n8_weighted_automorphisms import add,scale
from parametric_integer_linear import T,encode_poly

def description(weights,c):
    hall=[dict(weight=w,pair=None) for w in weights]
    for d in range(1,c+1):
        pending=[]
        for i,a in enumerate(hall):
            for j,b in enumerate(hall[:i]):
                if a['weight']+b['weight']!=d:continue
                if a['pair'] is not None and a['pair'][1]>j:continue
                pending.append(dict(weight=d,pair=(i,j)))
        hall.extend(pending)
    return hall

def main(args):
    begin=time.monotonic();p,q,c=1,10,26;div=6
    out=args.output;out.mkdir(parents=True,exist_ok=False)
    m=Group(p,q,c);sigma,tau,W=m.darboux();records=[];dims=[]
    for t in range(9,16):
        kernels=m.kernels(t);dims.append([t,len(kernels)])
        for j,(U,V) in enumerate(kernels):
            U,V=scale(U,Q(1,div)),scale(V,Q(1,div));direction=U,V
            def maps(n):return [m.substitute(m.exp_derivation(x,direction,n),sigma) for x in tau]
            # A power n^k requires k applications of a derivation raising
            # weight by t. BCH/group conversion preserves this filtration.
            bound=c//t;samples=[]
            for n in range(bound+1):samples.append([dict(m.collect(m.exp(x))) for x in maps(n)])
            polynomials=[]
            for side in range(2):
                polynomials.append([S.interpolate([(n,S.Rational(samples[n][side].get(i,0)))
                    for n in range(bound+1)],T).expand() for i in range(len(m.hall))])
            denoms=[]
            for side,polys in enumerate(polynomials):
                for i,f in enumerate(polys):
                    assert f.subs(T,0)==int(i==side)
                    denoms.extend(int(S.Poly(f,T).nth(k).q) for k in range(1,bound+1))
            power=lcm(1,*denoms)
            plus,minus=maps(power),maps(-power)
            coords=[m.collect(m.exp(x)) for x in plus+minus]
            assert all(x.denominator==1 for row in coords for _,x in row)
            for n in [-1,bound+1,power,-power]:
                actual=[dict(m.collect(m.exp(x))) for x in maps(n)]
                for side in range(2):
                    assert all(S.Rational(actual[side].get(i,0))==f.subs(T,n)
                               for i,f in enumerate(polynomials[side]))
            assert m.substitute(W,plus)==W and m.substitute(W,minus)==W
            for side in range(2):
                assert m.substitute(plus[side],minus)==m.letters[side]
                assert m.substitute(minus[side],plus)==m.letters[side]
                diff=add(plus[side],m.letters[side],-1);weight=[p,q][side]+t
                assert all(m.weight(w)>=weight for w in diff)
                assert m.layer(diff,weight)==scale(direction[side],power)
            records.append(dict(offset=t,kernel=j,power=power,direction=[poly_json(U),poly_json(V)],
                degree_bound=bound,polynomials=[[encode_poly(f) for f in polys] for polys in polynomials],
                plus=[terms_json(row) for row in coords[:2]],minus=[terms_json(row) for row in coords[2:]]))
            print('exact-period gauge',t,j,'power',power,'degree bound',bound,flush=True)
    hall=description((p,q),c+q);kept=len(m.hall)
    assert [[h['weight'],h['pair']] for h in hall[:kept]]==[[h['weight'],h['pair']] for h in m.hall]
    boundary=[i for i,h in enumerate(hall) if h['weight']>c and h['pair'] and all(j<kept for j in h['pair'])]
    desc=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in hall]
    data=dict(weights=[p,q],class_bound=c,direction_divisor=div,hall=desc,retained=kept,boundaries=boundary,
              kernel_dimensions=dims,records=records,seconds=time.monotonic()-begin)
    (out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
    fixture=[p,q,c,desc,kept,boundary,[[r['offset'],r['power'],r['plus'],r['minus']] for r in records]]
    (out/'fixtures.g').write_text('N8UniversalFixture := '+json.dumps(fixture)+';\n')
    print('PASS N8 delayed universal gauges:',len(records),'exact integer periods;',dims,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args())
