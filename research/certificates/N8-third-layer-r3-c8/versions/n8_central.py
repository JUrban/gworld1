#!/usr/bin/env python3
"""All-class last-central-layer commutator algorithm; exact integral arithmetic.

See problems/N8/central-target-proof.md, including the Klyachko dependency.
Uses the common Magnus/Hall representation, not the IA orbit algorithm.
"""
from functools import reduce
from itertools import combinations,product
from math import gcd,lcm
from sympy import Matrix,Poly,factor_list,symbols
from n8_ia_orbits import Magnus,add,ONE,affine_solve,factor_wedge


def bracket(m,a,b):return add(m.mul(a,b),m.mul(b,a),-1)


def primitive_lie_line(m,tensor,degree):
    words,rows,inverse,basis=m.projections[degree]
    vector=inverse*Matrix([tensor.get(words[i],0) for i in rows])
    reconstructed={}
    for a,n in zip(basis,vector):reconstructed=add(reconstructed,a,n)
    if reconstructed!=tensor:return None
    denominator=lcm(*(int(v.q) for v in vector))
    integers=[int(v*denominator) for v in vector]
    content=reduce(gcd,integers,0)
    if not content:return None
    first=next(n for n in integers if n)
    content=content if first>0 else -content
    return [n//content for n in integers]


def linear_solution(columns,rhs):
    words=sorted(set(rhs).union(*(set(x) for x in columns)))
    return affine_solve([[x.get(w,0) for w in words] for x in columns],
                        [rhs.get(w,0) for w in words])


def mixed_type(m,w,p,q):
    assert 1<=p<q and p+q<=m.degree
    # Aggregate commutative coefficients before constructing any polynomial.
    quadratics={}
    for word,n in w.items():
        assert len(word)==p+q
        i,j,k=word[:p],word[p:q],word[q:]
        key=tuple(sorted((i,k)));row=quadratics.setdefault(j,{})
        row[key]=row.get(key,0)+n
    nonzero=[(j,{key:n for key,n in row.items() if n}) for j,row in sorted(quadratics.items())]
    nonzero=[(j,row) for j,row in nonzero if row]
    if not nonzero:return None,dict(reason='all_block_quadratics_zero')
    middle,row=nonzero[0]
    blocks=list(product(range(m.rank),repeat=p));variables=symbols('t:'+str(len(blocks)))
    positions={word:i for i,word in enumerate(blocks)}
    expression=sum(n*variables[positions[i]]*variables[positions[k]] for (i,k),n in row.items())
    factors=factor_list(expression,*variables)[1]
    tried=[]
    for polynomial,multiplicity in factors:
        poly=Poly(polynomial,*variables)
        if poly.total_degree()!=1 or poly.coeff_monomial(1)!=0:continue
        tensor={word:poly.coeff_monomial(var) for word,var in zip(blocks,variables)
                if poly.coeff_monomial(var)}
        cc=primitive_lie_line(m,tensor,p)
        if cc is None:
            tried.append(dict(lie_line=False));continue
        c={}
        for h,n in zip(m.bydegree[p],cc):c=add(c,m.layer(h['value'],p),n)
        columns=[bracket(m,c,m.layer(h['value'],q)) for h in m.bydegree[q]]
        result=linear_solution(columns,w)
        tried.append(dict(lie_line=True,primitive_coordinates=cc,integral_solution=result is not None))
        if result is not None:return (cc,result[0]),dict(middle=list(middle),tried=tried)
    return None,dict(middle=list(middle),tried=tried)


def equal_type(m,w,p):
    basis=[m.layer(h['value'],p) for h in m.bydegree[p]]
    pairs=list(combinations(range(len(basis)),2))
    columns=[bracket(m,basis[i],basis[j]) for i,j in pairs]
    result=linear_solution(columns,w)
    if result is None:return None,dict(reason='outside_integral_exterior_image')
    coordinates,kernel=result;assert not kernel
    a=Matrix.zeros(len(basis))
    for (i,j),n in zip(pairs,coordinates):a[i,j]=n;a[j,i]=-n
    rank=a.rank()
    if rank!=2:return None,dict(reason='exterior_rank',rank=rank)
    plane,index=factor_wedge(a)
    return (list(map(int,index*plane[:,0])),list(map(int,plane[:,1]))),dict(exterior_rank=rank)


def decide_central(m,word):
    g=m.expansion(word)
    assert all(len(w) in (0,m.degree) for w in g),'target must lie in gamma_c'
    if g==ONE:return dict(answer=True,x=[],y=[],case='identity',trace=[])
    w=m.layer(g,m.degree);trace=[]
    for p in range(1,m.degree//2+1):
        q=m.degree-p
        result,evidence=mixed_type(m,w,p,q) if p<q else equal_type(m,w,p)
        trace.append(dict(p=p,q=q,soluble=result is not None,evidence=evidence))
        if result is None:continue
        xx,yy=m.lift(result[0],p),m.lift(result[1],q)
        assert m.comm(xx,yy)==g
        return dict(answer=True,p=p,q=q,x=m.collect(xx)[0],y=m.collect(yy)[0],trace=trace)
    return dict(answer=False,trace=trace)
