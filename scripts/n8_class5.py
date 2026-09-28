#!/usr/bin/env python3
"""Exact class-five prototype for N8(b); see the candidate proof, not just tests.

Words use signed one-based generators; group commutator is x^-1 y^-1 x y.
All linear algebra is over Z, and all polynomial factorization is over Q.
"""
from functools import lru_cache, reduce
from itertools import combinations, product
from math import gcd, lcm
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_class3 import ONE, add, winv, wcomm, wpow, lift_vector, lift_exterior, smith
from n8_class4 import factor_wedge

DEGREE=5

def reduced(word):
    out=[]
    for s in word:
        if out and out[-1]==-s:out.pop()
        else:out.append(int(s))
    return out

def mul(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            if len(u)+len(v)<=DEGREE:
                w=u+v;out[w]=out.get(w,0)+x*y
    return {w:c for w,c in out.items() if c}

def inv(a):
    assert a.get(())==1
    b=add(a,ONE,-1);term=dict(ONE);out=dict(ONE)
    for k in range(1,DEGREE+1):
        term=mul(term,b);out=add(out,term,(-1)**k)
    return out

def comm(a,b):return mul(mul(mul(inv(a),inv(b)),a),b)
def bracket(a,b):return add(mul(a,b),mul(b,a),-1)
def layer(a,k):return {w:c for w,c in a.items() if len(w)==k}

@lru_cache(maxsize=512)
def _expansion(word):
    out=dict(ONE)
    # Multiplication by a generator needs only suffix extensions, not a dense product.
    for s in word:
        i=abs(s)-1;updated=dict(out)
        for w,c in out.items():
            for k in range(1,(1 if s>0 else DEGREE-len(w))+1):
                if len(w)+k>DEGREE:break
                t=w+(i,)*k;updated[t]=updated.get(t,0)+c*((-1)**k if s<0 else 1)
        out={w:c for w,c in updated.items() if c}
    return out

def expansion(word):return _expansion(tuple(reduced(word)))

@lru_cache(maxsize=None)
def bases(rank):
    # Ordinary ordered basic Hall commutators through weight four.
    hall=[{'weight':1,'word':[i+1],'pair':None} for i in range(rank)]
    bydegree={1:[(i+1,) for i in range(rank)]}
    for degree in range(2,5):
        new=[]
        for i,x in enumerate(hall):
            for j in range(i):
                y=hall[j]
                if x['weight']+y['weight']!=degree:continue
                if x['pair'] is not None and x['pair'][1]>j:continue
                new.append({'weight':degree,'word':reduced(wcomm(x['word'],y['word'])),'pair':(i,j)})
        hall.extend(new);bydegree[degree]=[tuple(x['word']) for x in new]
    # Use positive exterior coordinates in degree two, matching the earlier solvers.
    bydegree[2]=[tuple(wcomm([i+1],[j+1])) for i,j in combinations(range(rank),2)]
    return {k:tuple(v) for k,v in bydegree.items()}

@lru_cache(maxsize=None)
def lie_bases(rank,degree):return tuple(layer(expansion(w),degree) for w in bases(rank)[degree])

def lift_basis(basis,coeffs):
    return reduced(s for w,k in zip(basis,coeffs) for s in wpow(w,k))

def affine_solve(columns,rhs):
    """An integral particular solution and a full primitive kernel lattice basis."""
    rows=[];target=[];n=len(columns)
    for j,b in enumerate(rhs):
        row=[c[j] for c in columns]
        if any(row):rows.append(row);target.append(b)
        elif b:return None
    if not rows:return [0]*n,[[int(i==j) for i in range(n)] for j in range(n)]
    a=Matrix(rows);d,s,t=smith(a);sb=s*Matrix(target);z=[0]*n
    nonzero=[]
    for i in range(a.rows):
        diagonal=d[i,i] if i<n else 0
        if diagonal:
            if sb[i]%diagonal:return None
            z[i]=sb[i]//diagonal;nonzero.append(i)
        elif sb[i]:return None
    answer=[int(v) for v in t*Matrix(z)]
    kernel=[[int(v) for v in t[:,j]] for j in range(n) if j not in nonzero]
    assert a*Matrix(answer)==Matrix(target)
    assert all(a*Matrix(v)==Matrix.zeros(a.rows,1) for v in kernel)
    return answer,kernel

def tensor_solve(columns,target):
    indices=sorted(set(target).union(*(set(v) for v in columns)))
    return affine_solve([[v.get(w,0) for w in indices] for v in columns],
                        [target.get(w,0) for w in indices])

def coordinates(target,rank,degree):
    result=tensor_solve(lie_bases(rank,degree),target)
    if result is None:return None
    answer,kernel=result;assert not kernel
    return answer

def correction_data(g,x,y,cbasis,dbasis,degree):
    ex,ey=expansion(x),expansion(y)
    delta=mul(inv(comm(ex,ey)),g)
    if any(0<len(w)<degree for w in delta):return None
    columns=([layer(comm(expansion(c),ey),degree) for c in cbasis]
             +[layer(comm(ex,expansion(d)),degree) for d in dbasis])
    return tensor_solve(columns,layer(delta,degree))

def apply_correction(x,y,cbasis,dbasis,coeffs):
    cut=len(cbasis)
    return (reduced(list(x)+lift_basis(cbasis,coeffs[:cut])),
            reduced(list(y)+lift_basis(dbasis,coeffs[cut:])))

def correct(g,x,y,cbasis,dbasis,degree):
    result=correction_data(g,x,y,cbasis,dbasis,degree)
    if result is None:return None
    return apply_correction(x,y,cbasis,dbasis,result[0])

def residues(particular,kernel,gauge):
    assert len(kernel)==1,('unexpected kernel dimension',len(kernel))
    primitive=kernel[0];i=next(i for i,v in enumerate(primitive) if v)
    assert gauge[i]%primitive[i]==0
    period=gauge[i]//primitive[i]
    assert period and all(a==period*b for a,b in zip(gauge,primitive))
    for n in range(abs(period)):
        yield [a+n*b for a,b in zip(particular,primitive)],abs(period),n

def hnf_pairs(w):
    plane,index=factor_wedge(w)
    for a in divisors(index):
        a=int(a);c=index//a
        for b in range(a):
            yield [int(v) for v in a*plane[:,0]],[int(v) for v in b*plane[:,0]+c*plane[:,1]]

def degree4_wedge(g4,rank):
    pairs=list(combinations(range(rank),2));n=len(pairs)
    w=Matrix(n,n,lambda i,j:g4.get(pairs[i]+pairs[j],0))
    if w!=-w.T or w.rank()!=2:return None
    lb=lie_bases(rank,2);total={}
    for i,j in combinations(range(n),2):total=add(total,bracket(lb[i],lb[j]),int(w[i,j]))
    return w if total==g4 else None

def primitive(values):
    denominator=lcm(*(int(v.q) for v in values))
    ints=[int(v*denominator) for v in values];content=reduce(gcd,map(abs,ints))
    assert content
    ints=[v//content for v in ints]
    return ints if next(v for v in ints if v)>0 else [-v for v in ints]

def factor_candidates(gpq,rank,p,q):
    """All primitive first-factor directions and integral second factors.

    Used only for p=1<q or (p,q)=(2,3); the cyclic lemma proves completeness.
    Each answer is a pair of integral Hall-coordinate vectors.
    """
    assert p==1 and q>=2 or (p,q)==(2,3)
    blocks=list(product(range(rank),repeat=p));ts=symbols('t:'+str(len(blocks)))
    polynomial=None
    for middle in product(range(rank),repeat=q-p):
        candidate=sum(gpq.get(i+middle+k,0)*ts[a]*ts[b]
                      for a,i in enumerate(blocks) for b,k in enumerate(blocks)).expand()
        if candidate:polynomial=candidate;break
    if polynomial is None:return []
    _,factors=factor_list(polynomial,*ts);out=[];seen=set()
    for factor,_ in factors:
        poly=Poly(factor,*ts)
        if poly.total_degree()!=1 or poly.coeff_monomial(1):continue
        vals=primitive([poly.coeff_monomial(t) for t in ts]);key=tuple(vals)
        if key in seen:continue
        seen.add(key);c={w:v for w,v in zip(blocks,vals) if v}
        cc=coordinates(c,rank,p)
        if cc is None:continue
        result=tensor_solve([bracket(c,y) for y in lie_bases(rank,q)],gpq)
        if result is None:continue
        dd,kernel=result
        # ad_C is injective in the unequal-degree cases used here; not needed to decide.
        assert not kernel
        out.append((cc,dd))
    return out

def scaled_pairs(first,second):
    content=reduce(gcd,map(abs,second));assert content
    for a in divisors(content):
        for sign in (-1,1):
            k=sign*int(a)
            yield [k*v for v in first],[v//k for v in second]

def solve(word,rank):
    assert rank>=1 and all(0<abs(s)<=rank for s in word)
    g=expansion(word);bb=bases(rank)
    b1,b2,b3,b4=(bb[i] for i in range(1,5))
    def yes(pair,case,**extra):
        x,y=pair;assert comm(expansion(x),expansion(y))==g,(case,x,y)
        return dict(answer=True,case=case,x=x,y=y,**extra)
    def no(case):return dict(answer=False,case=case)
    if g==ONE:return yes(([],[]),'identity')
    if layer(g,1):return no('outside_derived')
    g2,g3,g4,g5=(layer(g,i) for i in range(2,6))
    if g2:
        w=Matrix(rank,rank,lambda i,j:g2.get((i,j),0));assert w==-w.T
        if w.rank()!=2:return no('nondecomposable_degree2')
        for u,v in hnf_pairs(w):
            pair=correct(g,lift_vector(u),lift_vector(v),b2,b2,3)
            if pair is None:continue
            x,y=pair;data=correction_data(g,x,y,b3,b3,4)
            if data is None:continue
            gauge=(coordinates(layer(comm(expansion(x),g),3),rank,3)
                   +coordinates(layer(comm(expansion(y),g),3),rank,3))
            for coeffs,period,residue in residues(*data,gauge):
                pair4=apply_correction(x,y,b3,b3,coeffs)
                pair5=correct(g,*pair4,b4,b4,5)
                if pair5 is not None:return yes(pair5,'nonzero_degree2',period=period,residue=residue)
        return no('nonzero_degree2')
    if g3:
        for first,second in factor_candidates(g3,rank,1,2):
            for z,yy in scaled_pairs(first,second):
                x,y=lift_basis(b1,z),lift_basis(b2,yy)
                data=correction_data(g,x,y,b2,b3,4)
                if data is None:continue
                gauge=yy+[0]*len(b3)
                for coeffs,period,residue in residues(*data,gauge):
                    pair4=apply_correction(x,y,b2,b3,coeffs)
                    pair5=correct(g,*pair4,b3,b4,5)
                    if pair5 is not None:return yes(pair5,'nonzero_degree3',period=period,residue=residue)
        return no('nonzero_degree3')
    if g4:
        w=degree4_wedge(g4,rank)
        if w is not None:
            for c,d in hnf_pairs(w):
                x,y=lift_basis(b2,c),lift_basis(b2,d)
                pair=correct(g,x,y,b3,b3,5)
                if pair is not None:return yes(pair,'degree4_22')
        for first,second in factor_candidates(g4,rank,1,3):
            for z,yy in scaled_pairs(first,second):
                x,y=lift_basis(b1,z),lift_basis(b3,yy)
                pair=correct(g,x,y,b2,b4,5)
                if pair is not None:return yes(pair,'degree4_13')
        return no('nonzero_degree4')
    for p,q in [(2,3),(1,4)]:
        for first,second in factor_candidates(g5,rank,p,q):
            return yes((lift_basis(bb[p],first),lift_basis(bb[q],second)),f'central_{p}{q}')
    return no('central_degree5')

if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rank',type=int);parser.add_argument('word',help='JSON signed-generator word')
    args=parser.parse_args();print(json.dumps(solve(json.loads(args.word),args.rank)))
