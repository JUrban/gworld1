#!/usr/bin/env python3
"""Candidate degree-two iterated-adjoint family; unsupported inputs return None."""
from functools import reduce
from itertools import product
from math import gcd
from sympy import Matrix,Poly,divisors,factor_list,symbols
from n8_iterated_adjoint import (Magnus,ONE,adjoint,lie_tensor,bracket,first,
    apply,finished,short_particular,polynomial_system,differences,evaluate)
from n8_central import primitive_lie_line


def leading_family(m,w):
    assert m.degree>=9 and m.degree%2==1
    n=(m.degree-7)//2;q=m.degree-4;degree=m.degree-2
    quadratics={}
    for word,value in w.items():
        assert len(word)==degree
        row=quadratics.setdefault(word[2:-2],{})
        key=tuple(sorted((word[:2],word[-2:])))
        row[key]=row.get(key,0)+value
    row=next((r for _,r in sorted(quadratics.items()) if any(r.values())),None)
    if row is None:return None
    blocks=list(product(range(m.rank),repeat=2));variables=symbols('a:'+str(len(blocks)))
    positions={word:i for i,word in enumerate(blocks)}
    expression=sum(value*variables[positions[a]]*variables[positions[b]]
                   for (a,b),value in row.items())
    recognized=[];seen=set()
    for factor,_ in factor_list(expression,*variables)[1]:
        poly=Poly(factor,*variables)
        if poly.total_degree()!=1 or poly.coeff_monomial(1):continue
        tensor={word:poly.coeff_monomial(var) for word,var in zip(blocks,variables)
                if poly.coeff_monomial(var)}
        cc=primitive_lie_line(m,tensor,2)
        if cc is None or tuple(cc) in seen:continue
        seen.add(tuple(cc));C=lie_tensor(m,cc,2)
        columns=[adjoint(m,C,m.layer(h['value'],3),n+1) for h in m.bydegree[3]]
        matrix=Matrix([m.coordinates(col,degree) for col in columns]).T
        try:t,parameters=matrix.gauss_jordan_solve(Matrix(m.coordinates(w,degree)))
        except ValueError:continue
        assert parameters.rows==0 and any(t)
        assert adjoint(m,C,lie_tensor(m,list(t),3),n+1)==w
        previous=Matrix([m.coordinates(adjoint(m,C,m.layer(h['value'],3),n),q)
                         for h in m.bydegree[3]]).T
        recognized.append((cc,list(previous*t),list(t)))
    if not recognized:return None
    assert len(recognized)==1,'the degree-two leading direction must be unique'
    cc,dd,t=recognized[0]
    evidence=dict(C0=cc,D0=[[int(v.p),int(v.q)] for v in dd],
                  T0=[[int(v.p),int(v.q)] for v in t])
    if any(v.q!=1 for v in dd):return [],evidence
    dd=list(map(int,dd));content=reduce(gcd,dd,0);pairs=[]
    for a in divisors(content):
        for k in [int(a),-int(a)]:
            scaled=[v/k**(n+1) for v in t]
            pairs.append(([k*v for v in cc],[v//k for v in dd],
                          [[int(v.p),int(v.q)] for v in scaled]))
    return pairs,evidence


def decide_degree2_iterated(m,word,audit=None):
    assert m.rank>=2
    outside=dict(answer=None,case='outside_degree2_iterated_scope',trace=[])
    if m.degree<9 or m.degree%2==0:return outside
    c=m.degree;p=2;q=c-4;n=(c-7)//2;g=m.expansion(word)
    if g==ONE or min(len(w) for w in g if w)!=c-2:return outside
    family=leading_family(m,m.layer(g,c-2))
    if family is None:return outside
    pairs,evidence=family
    def conclude(result):result['leading_family']=evidence;return result
    trace=[]
    for branch,(cc,dd,t) in enumerate(pairs):
        x0,y0=m.lift(cc,p),m.lift(dd,q)
        step=first(m,g,x0,y0,p,q,1,audit)
        record=dict(branch=branch,C=cc,D=dd,T=t,total_branches=len(pairs),
                    first_soluble=step is not None,n=n)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)==int(n%2==0)
        record['first_kernel_dimension']=len(kernel)
        if not kernel:
            pair=apply(m,x0,y0,p,q,1,vector)
            last=first(m,g,*pair,p,q,2,audit)
            if last is None:continue
            return conclude(finished(m,g,*apply(m,*pair,p,q,2,last[0]),trace,'degree2_iterated'))
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,p,q,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=c for w in delta if w)
            return m.coordinates(m.layer(delta,c),c)
        coefficients=differences([residual(k) for k in range(3)])
        for k in [-2,-1,3]:assert evaluate(coefficients,k)==residual(k)
        C,D=m.layer(x0,p),m.layer(y0,q)
        columns=([bracket(m,m.layer(h['value'],p+2),D) for h in m.bydegree[p+2]]
                 +[bracket(m,C,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,c) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2])
        record['polynomial_degree']=c;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,p=p,q=q,degree=c,word=list(word),
                              x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,
                              kernel=direction,certificate=system['certificate'],
                              samples=[[k,*[m.collect(z)[0] for z in pair(k)]]
                                       for k in [-1,0,1,2,3]]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),p,q,2,list(map(int,correction)))
            assert m.comm(*result)==g;record['selected_parameter']=k
            return conclude(finished(m,g,*result,trace,'degree2_iterated'))
    return conclude(dict(answer=False,case='all_degree2_iterated_branches_failed',trace=trace))
