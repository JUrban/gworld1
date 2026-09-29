#!/usr/bin/env python3
"""Complete finite Pell certificates and constrained-quadratic identities.

This does not implement the enormous degree>=3 height-bound enumeration,
nor the proposed group-theoretic reduction. No random data or search caps.
"""
from math import isqrt, lcm
from pathlib import Path
import argparse,json
import sympy as S
from parametric_integer_linear import gap_value

T,R,Z=S.symbols('T R Z')

def ceilroot(n):
    s=isqrt(n)
    return s+(s*s<n)

def unit(d):
    assert d>0 and isqrt(d)**2!=d
    j=1
    while True:
        h=isqrt(1+d*j*j)
        if h*h-d*j*j==1:return h,j
        j+=1

def advance(pair,d,h,j):
    x,w=pair
    return h*x+d*j*w,j*x+h*w

def value(terms,x,w):return sum(c*x**i*w**j for c,i,j in terms)

def allowed(conditions,pair):
    return all(value(terms,*pair)%modulus==0 for terms,modulus in conditions)

def pell(d,n,conditions,exclude_seeds=False):
    assert n!=0
    h,j=unit(d)
    E=h+j*ceilroot(d);K=ceilroot(abs(n));bound=((E+1)*K+1)//2
    seeds=set()
    # Constructor scans W; independent GAP verifier scans X.
    for w in range(-bound,bound+1):
        x2=n+d*w*w
        if x2<0:continue
        x=isqrt(x2)
        if x*x==x2 and x<=bound:seeds.update([(x,w),(-x,w)])
    seeds=sorted(seeds)
    modulus=lcm(1,*(m for _,m in conditions))
    cycles=[];lookup={};seed_refs=[]
    for seed in seeds:
        start=tuple(v%modulus for v in seed)
        if start not in lookup:
            states=[];p=start
            while p not in lookup:
                lookup[p]=(len(cycles),len(states));states.append(p)
                p=tuple(v%modulus for v in advance(p,d,h,j))
            assert p==start
            cycles.append(dict(states=states,good=[i for i,s in enumerate(states) if allowed(conditions,s)]))
        seed_refs.append(lookup[start])
    forbidden=set(seeds) if exclude_seeds else set()
    witness=None
    for i,(seed,(ci,pos)) in enumerate(zip(seeds,seed_refs)):
        cycle=cycles[ci];period=len(cycle['states'])
        if not cycle['good']:continue
        k=(cycle['good'][0]-pos)%period;p=seed
        for _ in range(k):p=advance(p,d,h,j)
        skipped=0
        while p in forbidden:
            for _ in range(period):p=advance(p,d,h,j)
            k+=period;skipped+=1
        assert p[0]**2-d*p[1]**2==n and allowed(conditions,p)
        witness=dict(seed=i,exponent=k,pair=p,skipped=skipped)
        break
    return dict(d=d,n=n,unit=[h,j],bound=bound,seeds=seeds,modulus=modulus,
                conditions=conditions,cycles=cycles,seed_refs=seed_refs,
                forbidden=sorted(forbidden),witness=witness,decision=witness is not None)

def coeffs(p):
    p=S.Poly(S.expand(p),T,domain=S.ZZ)
    return [int(p.nth(i)) for i in range(max(0,p.degree())+1)] if p else [0]

def factor_record(a,b,c):
    F=S.expand(b*b-4*a*c)
    if F==0:A=0;G=0;roots=[]
    else:
        content,factors=S.factor_list(F,T)
        A=S.prod(f**(e//2) for f,e in factors)
        G=S.expand(content*S.prod(f for f,e in factors if e%2))
        roots=sorted(int(r) for r in S.Poly(A,T).ground_roots() if r.q==1)
        assert S.expand(A*A*G-F)==0
        if S.degree(G,T)>0:assert S.degree(S.gcd(G,S.diff(G,T)),T)==0
    assert S.expand((2*a*R+b)**2-F-4*a*(a*R*R+b*R+c))==0
    h=R*R+T*R+2
    H=S.expand((2*a)**2*h.subs(R,(A*Z-b)/(2*a))) if F else S.expand((2*a)**2*h.subs(R,-b/(2*a)))
    assert S.Poly(H,T,Z,domain=S.ZZ)
    grid=0
    for t in range(-7,8):
        for z in range(-7,8):
            aa=S.sympify(A).subs(T,t);bb=S.sympify(b).subs(T,t)
            r=S.cancel((aa*z-bb)/(2*a))
            if not r.is_Integer:continue
            lhs=int(h.subs({T:t,R:r}))%5==0
            rhs=int(H.subs({T:t,Z:z}))%(5*(2*a)**2)==0
            assert lhs==rhs;grid+=1
    return dict(a=a,b=coeffs(b),c=coeffs(c),F=coeffs(F),A=coeffs(A),G=coeffs(G),roots=roots,
                H=[[int(v),int(i),int(j)] for (i,j),v in S.Poly(H,T,Z).terms()],grid=grid)

def intersection_record(d,n,H):
    Q=T*T-d*Z*Z-n
    quotient,remainder=S.div(H,Q,Z,domain=S.QQ.poly_ring(T))
    if remainder==0:
        return dict(d=d,n=n,H=[[int(v),int(i),int(j)] for (i,j),v in S.Poly(H,T,Z).terms()],
                    identical=True,resultant=[0],roots=[],points=[])
    resultant=S.resultant(Q,H,Z)
    assert resultant!=0
    roots=sorted(int(v) for v in S.Poly(resultant,T).ground_roots() if v.q==1)
    points=[]
    for x in roots:
        w2=S.Rational(x*x-n,d)
        if not w2.is_Integer or w2<0:continue
        w=isqrt(int(w2))
        if w*w!=w2:continue
        for y in sorted(set([w,-w])):
            if H.subs({T:x,Z:y})==0:points.append([x,y])
    return dict(d=d,n=n,H=[[int(v),int(i),int(j)] for (i,j),v in S.Poly(H,T,Z).terms()],
                identical=False,resultant=coeffs(resultant),roots=roots,points=points)

def main(out):
    out.mkdir(exist_ok=False)
    records=[]
    for di,d in enumerate([2,3,5,6,7,10,11,12,13,17]):
        for n in [*range(-12,0),*range(1,13)]:
            m=[1,2,3,4,5,8,12][(di+n)%7]
            conditions=[([[1,2,0],[3,0,1],[di-n,0,0]],m)]
            records.append(pell(d,n,conditions,exclude_seeds=(n==1)))
    # Explicit modular impossibility, both signs of N, finite-exclusion,
    # and a nonsquare coefficient containing a square factor.
    records.extend([pell(2,1,[([[1,0,0]],2)]),pell(2,1,[],True),
                    pell(2,-1,[],True),pell(12,1,[([[1,1,0],[-1,0,0]],4)],True)])
    factors=[factor_record(*f) for f in [
        (1,0,1-T*T),(2,4*T,-2*(T**3-T)),(3,6*T*T+3,3*T**4+3*T*T-3),
        (2,4*T,2*T*T),(1,0,-(T-1)**2*(2*T*T+3*T+1)),
        (1,0,-(T+2)**4*(3*T-1)),(-2,4*T,-2*T*T+8),
        (1,0,3*(T-3)**2),(1,T,T*T+1),(2,1,T*T+1),
        (5,10*T,5*T*T-5)]]
    # On this actual curve point, reducing the cleared polynomial modulo
    # 5 instead of 5*(2a)^2 gives a false positive.
    a=5;t=0;z=10;r=1
    assert z*z==100 and a*r*r+10*t*r+5*t*t-5==0
    h=r*r+t*r+2;scaled=(2*a)**2*h
    wrong_modulus=dict(a=a,t=t,z=z,r=r,original=h,scaled=scaled,modulus=5)
    assert h%5!=0 and scaled%5==0 and scaled%(5*(2*a)**2)!=0
    Q=T*T-2*Z*Z-7
    intersections=[intersection_record(2,7,H) for H in
                   [Z-T+2,Z-1,T-3,S.Integer(1),(Z-T+2)*(Z+1),Q*(Z+T),Z]]
    total=dict(pell_systems=len(records),positive=sum(r['decision'] for r in records),
               negative=sum(not r['decision'] for r in records),
               seeds=sum(len(r['seeds']) for r in records),
               residue_states=sum(sum(len(c['states']) for c in r['cycles']) for r in records),
               exclusions_avoided=sum(r['witness']['skipped'] for r in records if r['witness']),
               factor_identities=len(factors),congruence_grid=sum(r['grid'] for r in factors),
               intersections=len(intersections),intersection_points=sum(len(r['points']) for r in intersections))
    assert total['positive'] and total['negative'] and total['exclusions_avoided']
    data=dict(pell=records,factors=factors,intersections=intersections,wrong_modulus=wrong_modulus,totals=total)
    (out/'checks.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'fixtures.g').write_text('N8CurveFixtures:='+gap_value(data)+';;\n')
    print(json.dumps(total));print('PASS N8 constrained curve arithmetic Python')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    main(p.parse_args().output)
