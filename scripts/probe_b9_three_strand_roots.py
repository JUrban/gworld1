#!/usr/bin/env python3
"""Necessary Burau equations for right square roots of sigma2 sigma1."""
import json
from pathlib import Path
import sympy as s

a,b,c,d=s.symbols('a b c d')
P=s.Matrix([[1,0,1],[1,1,1],[0,1,1]])
M=P*s.diag(s.Matrix([[a,b],[c,d]]),1)*P.inv()
X=s.eye(4); X[:3,:3]=M
Y=s.eye(4); Y[1:,1:]=M
T=[]
for i in range(3):
    t=s.eye(4); t[i:i+2,i:i+2]=s.Matrix([[2,-1],[1,0]])
    T.append(t)
residual=X*Y*T[0]-T[1]*T[0]*Y
equations=[s.expand(z) for z in residual if z!=0]+[a*d-b*c-1]
G=s.groebner(equations,a,b,c,d)
print('Matrix:',M)
print('Necessary equations:', equations)
print('Groebner basis:',list(G))
k=s.symbols('k',integer=True)
family={a:k*k-k+1,b:-k,c:1-k,d:1}
assert all(s.expand(z.subs(family))==0 for z in equations)
out=Path('research/certificates/B9-small-strands')
out.mkdir(exist_ok=False)
(out/'three-strand-matrix-v1.json').write_text(json.dumps({
    'basis_change':P.tolist(),
    'matrix':[[str(z) for z in row] for row in M.tolist()],
    'equations':[str(z) for z in equations],
    'groebner':[str(z) for z in G],
    'scope':'Necessary representation equations; braid and specialness classification require separate proofs.'
},indent=2,default=str)+'\n')
print('PASS three-strand necessary matrix equations')
