#!/usr/bin/env python3
"""Candidate N8 algorithm for the iterated-adjoint third-from-last stratum.

Outside the proved scope the answer is None, never a negative decision.
All finite leading scales and all integral affine solutions are retained.
"""
from functools import reduce
from math import gcd
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_multigraded_magnus import Magnus
from n8_penultimate import lie_tensor
from n8_central import bracket
from n8_class6 import ONE, apply, finished
from n8_class7 import short_particular
from n8_class9_linear import first
from n8_sparse_polynomial_lattice import polynomial_system, differences, evaluate


def adjoint(m,z,t,n):
    for _ in range(n):t=bracket(m,z,t)
    return t


def leading_family(m,w):
    """Recognize rational scope before testing integral factorization.

    A missing integral leading pair is a negative decision within the scope,
    not a failure to recognize the scope. Q_J factors supply every possible
    degree-one direction; this calculation does not search a height bound.
    """
    degree=m.degree-2;quadratics={};variables=symbols('a:'+str(m.rank))
    for word,n in w.items():
        assert len(word)==degree
        row=quadratics.setdefault(word[1:-1],{})
        key=tuple(sorted((word[0],word[-1])))
        row[key]=row.get(key,0)+n
    row=next((r for _,r in sorted(quadratics.items()) if any(r.values())),None)
    if row is None:return None
    expression=sum(n*variables[i]*variables[j] for (i,j),n in row.items())
    recognized=[]
    for factor,_ in factor_list(expression,*variables)[1]:
        poly=Poly(factor,*variables)
        if poly.total_degree()!=1 or poly.coeff_monomial(1):continue
        cc=[int(poly.coeff_monomial(v)) for v in variables]
        content=reduce(gcd,cc,0)
        if next(x for x in cc if x)<0:content=-content
        cc=[x//content for x in cc];z=lie_tensor(m,cc,1)
        columns=[adjoint(m,z,m.layer(h['value'],2),degree-2) for h in m.bydegree[2]]
        matrix=Matrix([m.coordinates(col,degree) for col in columns]).T
        try:t,parameters=matrix.gauss_jordan_solve(Matrix(m.coordinates(w,degree)))
        except ValueError:continue
        assert parameters.rows==0 and any(t)
        assert adjoint(m,z,lie_tensor(m,list(t),2),degree-2)==w
        # D0 = ad_z^(c-5)(T), retaining rational coordinates for recognition.
        previous=Matrix([m.coordinates(adjoint(m,z,m.layer(h['value'],2),degree-3),degree-1)
                         for h in m.bydegree[2]]).T
        dd=previous*t
        recognized.append((cc,list(dd),list(t)))
    if not recognized:return None
    assert len(recognized)==1,'the degree-one direction must be unique'
    cc,dd,t=recognized[0]
    evidence=dict(C0=cc,D0=[[int(v.p),int(v.q)] for v in dd],
                  T0=[[int(v.p),int(v.q)] for v in t])
    if any(v.q!=1 for v in dd):return [],evidence
    dd=list(map(int,dd));content=reduce(gcd,dd,0)
    pairs=[]
    for a in divisors(content):
        for k in [int(a),-int(a)]:
            # [k*z,D0/k]=w and D0/k=ad_(k*z)^(c-5)(T0/k^(c-4)).
            scaled=t if k==1 else [v/k**(degree-2) for v in t]
            pairs.append(([k*v for v in cc],[v//k for v in dd],
                          [[int(v.p),int(v.q)] for v in scaled]))
    return pairs,evidence


def decide_iterated_adjoint(m,word,audit=None):
    assert m.rank>=2 and m.degree>=6
    g=m.expansion(word);c=m.degree;q=c-3;n=c-5
    outside=dict(answer=None,case='outside_iterated_adjoint_scope',trace=[])
    if g==ONE or min(len(w) for w in g if w)!=c-2:return outside
    leading=m.layer(g,c-2)
    family=leading_family(m,leading)
    if family is None:return outside
    pairs,evidence=family
    def conclude(result):
        result['leading_family']=evidence
        return result
    trace=[]
    for branch,(cc,dd,t) in enumerate(pairs):
        x0,y0=m.lift(cc,1),m.lift(dd,q)
        step=first(m,g,x0,y0,1,q,1,audit)
        record=dict(branch=branch,C=cc,D=dd,T=t,total_branches=len(pairs),
                    first_soluble=step is not None,n=n)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)==int(n%2==0)
        record['first_kernel_dimension']=len(kernel)
        if not kernel:
            pair=apply(m,x0,y0,1,q,1,vector)
            last=first(m,g,*pair,1,q,2,audit)
            if last is None:continue
            return conclude(finished(m,g,*apply(m,*pair,1,q,2,last[0]),trace,'iterated_adjoint'))
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,1,q,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=c for w in delta if w)
            return m.coordinates(m.layer(delta,c),c)
        coefficients=differences([residual(k) for k in range(3)])
        for k in [-2,-1,3]:assert evaluate(coefficients,k)==residual(k)
        z,d=m.layer(x0,1),m.layer(y0,q)
        columns=([bracket(m,m.layer(h['value'],3),d) for h in m.bydegree[3]]
                 +[bracket(m,z,m.layer(h['value'],q+2)) for h in m.bydegree[q+2]])
        system=polynomial_system([m.coordinates(col,c) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(system['certificate']['residual'][2][i][0]
                   for i in range(len(coefficients[0])))
        record['polynomial_degree']=c;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,q=q,degree=c,word=list(word),
                              x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,
                              kernel=direction,certificate=system['certificate'],
                              samples=[[k,*[m.collect(z)[0] for z in pair(k)]]
                                       for k in [-1,0,1,2,3]]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),1,q,2,list(map(int,correction)))
            assert m.comm(*result)==g
            record['selected_parameter']=k
            return conclude(finished(m,g,*result,trace,'iterated_adjoint'))
    return conclude(dict(answer=False,case='all_iterated_adjoint_branches_failed',trace=trace))
