#!/usr/bin/env python3
"""Candidate odd-adjoint family, classes 2h+5 for odd h>=3.

Outside the recognized rational family return None, not a negative answer.
All finite leading scales and all integral affine solutions are retained.
"""
from functools import reduce
from itertools import combinations_with_replacement, product
from math import comb, factorial, gcd, prod
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_iterated_adjoint import (Magnus, ONE, adjoint, lie_tensor, bracket,
    first, apply, finished, short_particular, polynomial_system, differences, evaluate)
from n8_central import add


def shape(m,z,t,h):
    assert h>=1 and h%2==1
    powers=[adjoint(m,t,z,i) for i in range(h+1)]
    d={}
    for i in range((h+1)//2):
        d=add(d,bracket(m,powers[i],powers[h-i]),-(-1)**i)
    return d


def polarization(m,z,h):
    """Integer monomial-coefficient columns, not divided-power coordinates."""
    basis=[m.layer(item['value'],2) for item in m.bydegree[2]]
    dimension=len(basis);slots=list(combinations_with_replacement(range(dimension),h))
    evaluations={};columns=[]
    def at(beta):
        if beta not in evaluations:
            t={}
            for coefficient,e in zip(beta,basis):t=add(t,e,coefficient)
            evaluations[beta]=shape(m,z,t,h)
        return evaluations[beta]
    for slot in slots:
        alpha=tuple(slot.count(i) for i in range(dimension))
        if len(set(slot))==1:
            beta=tuple(int(i==slot[0]) for i in range(dimension))
            column=at(beta)
        else:
            column={}
            for beta in product(*(range(a+1) for a in alpha)):
                coefficient=(-1)**(h-sum(beta))*prod(comb(a,b) for a,b in zip(alpha,beta))
                column=add(column,at(beta),coefficient)
            divisor=prod(factorial(a) for a in alpha)
            assert all(v%divisor==0 for v in column.values())
            column={word:v//divisor for word,v in column.items()}
        columns.append(column)
    return slots,columns


def leading_family(m,w,h):
    """Recognize scalar pure symmetric tensors, then retain integral scales."""
    degree=2*h+3
    assert m.degree>=degree and h>=3 and h%2==1
    variables=symbols('a:'+str(m.rank));quadratics={}
    for word,n in w.items():
        assert len(word)==degree
        row=quadratics.setdefault(word[1:-1],{})
        key=tuple(sorted((word[0],word[-1])))
        row[key]=row.get(key,0)+n
    row=next((r for _,r in sorted(quadratics.items()) if any(r.values())),None)
    if row is None:return None
    expression=sum(n*variables[i]*variables[j] for (i,j),n in row.items())
    recognized=[]
    if not hasattr(m,'odd_adjoint_cache'):m.odd_adjoint_cache={}
    for factor,_ in factor_list(expression,*variables)[1]:
        poly=Poly(factor,*variables)
        if poly.total_degree()!=1 or poly.coeff_monomial(1):continue
        coefficients=[poly.coeff_monomial(v) for v in variables]
        assert all(v.q==1 for v in coefficients)
        cc=list(map(int,coefficients));content=reduce(gcd,cc,0)
        if next(v for v in cc if v)<0:content=-content
        cc=[v//content for v in cc];z=lie_tensor(m,cc,1)
        key=(h,tuple(cc))
        if key not in m.odd_adjoint_cache:
            slots,columns=polarization(m,z,h)
            dmatrix=Matrix([m.coordinates(col,degree-1) for col in columns]).T
            wmatrix=Matrix([m.coordinates(bracket(m,z,col),degree) for col in columns]).T
            m.odd_adjoint_cache[key]=(slots,dmatrix,wmatrix)
        slots,dmatrix,wmatrix=m.odd_adjoint_cache[key]
        try:values,parameters=wmatrix.gauss_jordan_solve(Matrix(m.coordinates(w,degree)))
        except ValueError:continue
        assert parameters.rows==0
        entries=dict(zip(slots,values));dimension=len(m.bydegree[2])
        pivot=next((i for i in range(dimension) if entries[(i,)*h]),None)
        if pivot is None:continue
        scalar=entries[(pivot,)*h]
        t=[entries[tuple(sorted((pivot,)*(h-1)+(j,)))]/scalar for j in range(dimension)]
        if any(value!=scalar*prod(t[j] for j in slot) for slot,value in entries.items()):continue
        d=shape(m,z,lie_tensor(m,t,2),h)
        assert add({},bracket(m,z,d),scalar)==w
        dd=list(dmatrix*values)
        recognized.append((cc,dd,t,scalar))
    if not recognized:return None
    assert len(recognized)==1,'odd-adjoint leading direction must be unique'
    cc,dd,t,scalar=recognized[0]
    evidence=dict(h=h,C0=cc,D0=[[int(v.p),int(v.q)] for v in dd],
                  T0=[[int(v.p),int(v.q)] for v in t],scalar=[int(scalar.p),int(scalar.q)])
    if any(v.q!=1 for v in dd):return [],evidence
    dd=list(map(int,dd));content=reduce(gcd,dd,0)
    return [([k*v for v in cc],[v//k for v in dd])
            for a in divisors(content) for k in (int(a),-int(a))],evidence


def decide_odd_adjoint(m,word,audit=None):
    outside=dict(answer=None,case='outside_odd_adjoint_scope',trace=[])
    c=m.degree
    if m.rank<2 or c<11 or c%4!=3:return outside
    h=(c-5)//2;q=c-3;g=m.expansion(word)
    if g==ONE or min(len(w) for w in g if w)!=c-2:return outside
    family=leading_family(m,m.layer(g,c-2),h)
    if family is None:return outside
    pairs,evidence=family;trace=[]
    def conclude(result):
        result['leading_family']=evidence
        return result
    for branch,(cc,dd) in enumerate(pairs):
        x0,y0=m.lift(cc,1),m.lift(dd,q)
        step=first(m,g,x0,y0,1,q,1,audit)
        record=dict(branch=branch,C=cc,D=dd,total_branches=len(pairs),first_soluble=step is not None)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)==1
        record['first_kernel_dimension']=1
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,1,q,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=c for w in delta if w)
            return m.coordinates(m.layer(delta,c),c)
        coefficients=differences([residual(k) for k in range(3)])
        for k in (-2,-1,3):assert evaluate(coefficients,k)==residual(k)
        C,D=m.layer(x0,1),m.layer(y0,q)
        columns=([bracket(m,m.layer(item['value'],3),D) for item in m.bydegree[3]]
                 +[bracket(m,C,m.layer(item['value'],q+2)) for item in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,c) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2])
        record['polynomial_degree']=c;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,q=q,degree=c,word=list(word),
                              x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,kernel=direction,
                              certificate=system['certificate'],
                              samples=[[k,*[m.collect(z)[0] for z in pair(k)]] for k in (-1,0,1,2,3)]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),1,q,2,list(map(int,correction)))
            assert m.comm(*result)==g;record['selected_parameter']=k
            return conclude(finished(m,g,*result,trace,'odd_adjoint'))
    return conclude(dict(answer=False,case='all_odd_adjoint_branches_failed',trace=trace))
