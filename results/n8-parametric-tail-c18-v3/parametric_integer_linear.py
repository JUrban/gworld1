#!/usr/bin/env python3
"""Decide P(t)z=b(t), t and z integral, with rational polynomial entries.

One-parameter linear Diophantine decidability is prior work. This implements
an elementary Q[T]-Smith proof and exports complete finite/periodic evidence.
There are no search caps in the decision algorithm.
"""
from math import lcm
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

T=S.Symbol('T')

def coeffs(p):
    p=S.Poly(S.expand(p),T,domain=S.QQ)
    return [p.nth(i) for i in range(max(0,p.degree())+1)] if p else [S.Integer(0)]

def denominator(entries):
    return lcm(1,*(int(c.q) for p in entries for c in coeffs(p)))

def normal_form(A,domain):
    m,n=A.shape
    if not m or not n:return S.zeros(m,n),S.eye(m),S.eye(n)
    D,U,V=(x.to_Matrix() for x in smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(domain)))
    assert (U*A*V-D).applyfunc(S.expand)==S.zeros(m,n)
    assert S.Poly(U.det(),T).degree()==0 and U.det()!=0
    assert S.Poly(V.det(),T).degree()==0 and V.det()!=0
    return D,U,V

def integer_solve(A,b):
    # Full integer Smith transformations can explode on the larger group
    # fixtures. The already-audited component Hermite routine retains the
    # unimodular transform and returns the same complete affine Z-lattice.
    from n8_component_linear import affine_solution
    A,b=S.Matrix(A),S.Matrix(b)
    m,n=A.shape
    assert b.shape==(m,1)
    assert all(x.is_Integer for x in list(A)+list(b))
    if m==0:return S.zeros(n,1),S.eye(n)
    answer=affine_solution([[int(A[i,j]) for i in range(m)] for j in range(n)],
                           [int(x) for x in b])
    if answer is None:return None
    z=S.Matrix(n,1,answer[0]);k=len(answer[1])
    kernel=S.Matrix(n,k,lambda i,j:answer[1][j][i])
    assert A*z==b and A*kernel==S.zeros(m,k)
    return z,kernel

def integer_roots(p):
    p=S.Poly(p,T,domain=S.QQ)
    assert p
    return sorted(int(v) for v in p.ground_roots() if v.q==1)

def specialize(A,t):return A.applyfunc(lambda p:S.expand(p).subs(T,t))

def encode_poly(p):return [[int(c.p),int(c.q)] for c in coeffs(p)]
def encode_matrix(A):
    return dict(rows=A.rows,cols=A.cols,entries=[[encode_poly(A[i,j]) for j in range(A.cols)] for i in range(A.rows)])
def decode_matrix(data):
    return S.Matrix(data['rows'],data['cols'],lambda i,j:sum(S.Rational(a,b)*T**k for k,(a,b) in enumerate(data['entries'][i][j])))

def solve(P,b):
    P,b=S.Matrix(P),S.Matrix(b);m,n=P.shape
    assert b.shape==(m,1)
    scale=denominator(list(P)+list(b));P=(scale*P).applyfunc(S.expand);b=(scale*b).applyfunc(S.expand)
    D,U,V=normal_form(P,S.QQ.poly_ring(T));Vi=V.inv().applyfunc(S.cancel)
    assert all(S.denom(x).free_symbols==set() for x in Vi)
    assert (V*Vi-S.eye(n)).applyfunc(S.expand)==S.zeros(n,n)
    beta=(U*b).applyfunc(S.expand);r=sum(D[i,i]!=0 for i in range(min(m,n)))
    roots=sorted(set(x for i in range(r) for x in integer_roots(D[i,i])))
    M=denominator(list(Vi))
    rec=dict(P=encode_matrix(P),b=encode_matrix(b),input_scale=scale,
             D=encode_matrix(D),U=encode_matrix(U),V=encode_matrix(V),Vi=encode_matrix(Vi),
             beta=encode_matrix(beta),rank=int(r),M=M,rank_drop=roots)
    candidates=None
    for j in range(r,m):
        if beta[j]!=0:
            rec.update(mode='finite_zero_row',critical_row=j)
            candidates=sorted(set(integer_roots(beta[j]))|set(roots));break
    if candidates is None:
        quotients=[]
        for i in range(r):
            q,rem=S.div(beta[i],D[i,i],T,domain=S.QQ);quotients.append(q)
            if rem!=0:
                N=denominator([M*q]);R=S.Poly(N*M*rem,T,domain=S.QQ);di=S.Poly(D[i,i],T,domain=S.QQ)
                lead=abs(di.LC());lower=sum(abs(x) for x in di.all_coeffs()[1:]);total=sum(abs(x) for x in R.all_coeffs())
                root_bound=1+sum(abs(x) for x in R.all_coeffs()[1:])/abs(R.LC())
                B=int(S.ceiling(max(1,2*lower/lead,2*total/lead,root_bound)))
                rec.update(mode='finite_fraction',critical_row=i,quotient=encode_poly(q),
                           remainder=encode_poly(rem),N=N,R=encode_poly(R.as_expr()),bound=B)
                candidates=sorted(set(range(-B,B+1))|set(roots));break
    if candidates is not None:
        rec['finite_checks']=[]
        for t in candidates:
            ans=integer_solve(specialize(P,t),specialize(b,t))
            rec['finite_checks'].append(dict(t=t,witness=None if ans is None else [int(x) for x in ans[0]]))
        rec['accepted']=[x['t'] for x in rec['finite_checks'] if x['witness'] is not None]
        rec['witness']=next((x for x in rec['finite_checks'] if x['witness'] is not None),None)
        return rec
    y0=S.zeros(n,1)
    for i,q in enumerate(quotients):y0[i]=q
    z0=(V*y0).applyfunc(S.expand);W=(V[:,r:]/M).applyfunc(S.expand)
    K=denominator(list(z0)+list(W));Z=(K*z0).applyfunc(S.expand);L=(K*W).applyfunc(S.expand)
    assert (P*z0-b).applyfunc(S.expand)==S.zeros(m,1) and (P*W).applyfunc(S.expand)==S.zeros(m,n-r)
    rec.update(mode='periodic',K=K,Z=encode_matrix(Z),L=encode_matrix(L),residue_checks=[])
    for t in range(K):
        A=specialize(L,t).row_join(K*S.eye(n));rhs=-specialize(Z,t)
        ans=integer_solve(A,rhs)
        ell=None if ans is None else [int(x)%K for x in ans[0][:n-r,0]]
        rec['residue_checks'].append(dict(residue=t,ell=ell))
    rec['rank_drop_checks']=[]
    for t in roots:
        ans=integer_solve(specialize(P,t),specialize(b,t))
        rec['rank_drop_checks'].append(dict(t=t,witness=None if ans is None else [int(x) for x in ans[0]]))
    rec['accepted_residues']=[x['residue'] for x in rec['residue_checks'] if x['ell'] is not None]
    rec['witness']=next((x for x in rec['rank_drop_checks'] if x['witness'] is not None),None)
    if rec['witness'] is None and rec['accepted_residues']:
        row=next(x for x in rec['residue_checks'] if x['ell'] is not None);t=row['residue']
        while t in roots:t+=K
        ell=S.Matrix(n-r,1,row['ell']);z=(specialize(Z,t)+specialize(L,t)*ell)/K
        assert all(x.is_Integer for x in z) and specialize(P,t)*z==specialize(b,t)
        rec['witness']=dict(t=t,witness=[int(x) for x in z])
    return rec

def accepted(rec,t):
    if rec['mode']!='periodic':return t in rec['accepted']
    if t in rec['rank_drop']:
        return next(x['witness'] is not None for x in rec['rank_drop_checks'] if x['t']==t)
    return t%rec['K'] in rec['accepted_residues']

def gap_value(x):
    if x is None:return 'fail'
    if isinstance(x,bool):return str(x).lower()
    if isinstance(x,str):
        import json
        return json.dumps(x)
    if isinstance(x,dict):return 'rec('+','.join(k+':='+gap_value(v) for k,v in x.items())+')'
    if isinstance(x,(list,tuple)):return '['+','.join(gap_value(v) for v in x)+']'
    return str(x)
