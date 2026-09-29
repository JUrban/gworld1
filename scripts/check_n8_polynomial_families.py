#!/usr/bin/env python3
"""Finite arithmetic controls for the one-polynomial-parameter continuation."""
from pathlib import Path
import argparse,json
import sympy as S
from n8_polynomial_families import families,member,point_at
from parametric_integer_linear import T,gap_value,integer_solve,encode_matrix,denominator

ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('research/certificates/N8-polynomial-families'))
out=ap.parse_args().output
out.mkdir(parents=True,exist_ok=False)
cases=[
 ('quadratic_residues',S.Matrix([[6,0,0],[0,10,0]]),S.Matrix([T*T-1,T**3-T])),
 ('integer_valued',S.Matrix([[1,0]]),S.Matrix([T*(T-1)/2])),
 ('finite_quadratic',S.Matrix([[2,4],[0,0]]),S.Matrix([T+1,T*T-9])),
 ('finite_negative',S.Matrix([[1],[0]]),S.Matrix([T,T*T+1])),
 ('absorbed_quadratic_negative',S.Matrix([[3,0],[2,5]]),S.Matrix([T*T-1,T**3+T])),
 ('absorbed_quadratic_positive',S.Matrix([[3,0],[2,5]]),S.Matrix([T*T-1,2*(T*T-1)/3+5*T])),
 ('free_kernel',S.Matrix([[2,4,-6],[0,0,0]]),S.Matrix([T*T+T,0])),
 ('rank_zero',S.zeros(2,3),S.Matrix([0,0])),
 ('rank_zero_finite',S.zeros(2,2),S.Matrix([T*(T-2),0])),
 ('shifted_cubic',S.Matrix([[4,6],[2,8]]),S.Matrix([(T+2)**3,2*T*T+1])),
 ('rational_matrix',S.Matrix([[S.Rational(2,3),S.Rational(4,5)]]),S.Matrix([(T*T-1)/7])),
]
records=[];checks=0
for name,A,b in cases:
    result=families(A,b);result['name']=name
    scale=denominator(list(A)+list(b))
    for t in range(-30,31):
        ans=integer_solve(scale*A,(scale*b).subs(T,t))
        assert member(result,t)==(ans is not None)
        if ans is not None:
            z=point_at(result,t)
            assert all(x.is_Integer for x in z) and A*z==b.subs(T,t)
        checks+=1
    records.append(result)
    print(name,result['mode'],len(result['families']),'complete families',flush=True)
(out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
(out/'fixtures.g').write_text('N8PolynomialFamilies := '+gap_value(records)+';\n')
arith=[dict(r['certificate'],name=r['name'],sample_parameters=list(range(-30,31))) for r in records]
(out/'arithmetic.g').write_text('ParametricIntegerFixtures := '+gap_value(arith)+';\n')
print('PASS N8 polynomial families:',len(records),'complete systems;',checks,'specializations')
