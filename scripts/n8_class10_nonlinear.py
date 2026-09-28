#!/usr/bin/env python3
"""Proposed class-ten nonlinear family; unsupported inputs return None.

Recognition is rational and separate from the integral factor decision.
See research/notes/N8-class10-nonlinear-kernel-lead.md and the later proof.
"""
from functools import reduce
from math import gcd
from sympy import Matrix, Poly, divisors, factor_list, symbols
from n8_iterated_adjoint import (Magnus, ONE, adjoint, lie_tensor, bracket,
    first, apply, finished, short_particular, polynomial_system,
    differences, evaluate)
from n8_central import add


def shape(m,z,t):
    jets=[adjoint(m,z,t,i) for i in range(5)]
    # Keep exact integers/rationals, never binary floating arithmetic.
    d=add(bracket(m,jets[0],jets[3]),bracket(m,jets[0],jets[3]))
    d=add(d,bracket(m,jets[1],jets[2]),3)
    v=add(bracket(m,jets[0],bracket(m,jets[0],jets[2])),
          bracket(m,jets[0],bracket(m,jets[0],jets[2])))
    v=add(v,bracket(m,jets[1],bracket(m,jets[0],jets[1])),-1)
    assert bracket(m,z,v)==bracket(m,t,d)
    return d,v


def leading_family(m,w):
    variables=symbols('a:'+str(m.rank));quadratics={}
    for word,n in w.items():
        assert len(word)==8
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
        if next(v for v in cc if v)<0:content=-content
        cc=[v//content for v in cc];z=lie_tensor(m,cc,1)
        # Invert ad_z first, without imposing integrality.
        columns=[bracket(m,z,m.layer(h['value'],7)) for h in m.bydegree[7]]
        matrix=Matrix([m.coordinates(col,8) for col in columns]).T
        try:dd,parameters=matrix.gauss_jordan_solve(Matrix(m.coordinates(w,8)))
        except ValueError:continue
        assert parameters.rows==0
        # Invert the injective linear polarization Sym^2(L2) -> L7.
        basis=[m.layer(h['value'],2) for h in m.bydegree[2]]
        diagonal=[shape(m,z,t)[0] for t in basis]
        slots=[];columns=[]
        for i in range(len(basis)):
            for j in range(i,len(basis)):
                slots.append((i,j))
                tensor=diagonal[i] if i==j else add(add(
                    shape(m,z,add(basis[i],basis[j]))[0],diagonal[i],-1),diagonal[j],-1)
                columns.append(m.coordinates(tensor,7))
        matrix=Matrix(columns).T
        try:values,parameters=matrix.gauss_jordan_solve(dd)
        except ValueError:continue
        assert parameters.rows==0
        square=Matrix.zeros(len(basis))
        for (i,j),a in zip(slots,values):square[i,j]=square[j,i]=a
        if square.rank()!=1:continue
        pivot=next(i for i in range(len(basis)) if square[i,i])
        scalar=square[pivot,pivot];t=list(square[:,pivot]/scalar)
        assert square==scalar*Matrix(t)*Matrix(t).T
        d,_=shape(m,z,lie_tensor(m,t,2))
        assert add({},bracket(m,z,d),scalar)==w
        recognized.append((cc,list(dd),t,scalar))
    if not recognized:return None
    assert len(recognized)==1,'nonlinear-family leading direction is unique'
    cc,dd,t,scalar=recognized[0]
    evidence=dict(C0=cc,D0=[[int(v.p),int(v.q)] for v in dd],
                  T0=[[int(v.p),int(v.q)] for v in t],
                  scalar=[int(scalar.p),int(scalar.q)])
    if any(v.q!=1 for v in dd):return [],evidence
    dd=list(map(int,dd));content=reduce(gcd,dd,0)
    return [([k*v for v in cc],[v//k for v in dd])
            for a in divisors(content) for k in [int(a),-int(a)]],evidence


def decide_nonlinear(m,word,audit=None):
    outside=dict(answer=None,case='outside_class10_nonlinear_scope',trace=[])
    if m.rank<2 or m.degree!=10:return outside
    g=m.expansion(word)
    if g==ONE or min(len(w) for w in g if w)!=8:return outside
    family=leading_family(m,m.layer(g,8))
    if family is None:return outside
    pairs,evidence=family;trace=[]
    def conclude(result):result['leading_family']=evidence;return result
    for branch,(cc,dd) in enumerate(pairs):
        x0,y0=m.lift(cc,1),m.lift(dd,7)
        step=first(m,g,x0,y0,1,7,1,audit)
        record=dict(branch=branch,C=cc,D=dd,total_branches=len(pairs),first_soluble=step is not None)
        trace.append(record)
        if step is None:continue
        vector,kernel=step
        assert len(kernel)==1
        record['first_kernel_dimension']=1
        vector=short_particular((vector,kernel));direction=kernel[0]
        def pair(k):return apply(m,x0,y0,1,7,1,[a+k*b for a,b in zip(vector,direction)])
        def residual(k):
            delta=m.mul(m.inv(m.comm(*pair(k))),g)
            assert all(len(w)>=10 for w in delta if w)
            return m.coordinates(m.layer(delta,10),10)
        coefficients=differences([residual(k) for k in range(3)])
        for k in [-2,-1,3]:assert evaluate(coefficients,k)==residual(k)
        C,D=m.layer(x0,1),m.layer(y0,7)
        columns=([bracket(m,m.layer(h['value'],3),D) for h in m.bydegree[3]]
                 +[bracket(m,C,m.layer(h['value'],9)) for h in m.bydegree[9]])
        system=polynomial_system([m.coordinates(col,10) for col in columns],coefficients)
        assert system['mode']=='finite_points' and len(system['values'])<=2
        assert any(v[0] for v in system['certificate']['residual'][2])
        record['polynomial_degree']=10;record['polynomial']=system['certificate']
        if audit is not None:
            audit.append(dict(kind='polynomial',rank=m.rank,q=7,degree=10,word=list(word),
                              x0=m.collect(x0)[0],y0=m.collect(y0)[0],vector=vector,
                              kernel=direction,certificate=system['certificate'],
                              samples=[[k,*[m.collect(z)[0] for z in pair(k)]]
                                       for k in [-1,0,1,2,3]]))
        for k in system['values']:
            correction=evaluate(system['particular'],k)
            assert all(v.denominator==1 for v in correction)
            result=apply(m,*pair(k),1,7,2,list(map(int,correction)))
            assert m.comm(*result)==g;record['selected_parameter']=k
            return conclude(finished(m,g,*result,trace,'class10_nonlinear'))
    return conclude(dict(answer=False,case='all_nonlinear_branches_failed',trace=trace))
