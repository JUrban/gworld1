#!/usr/bin/env python3
"""Complete finite/periodic decision certificates and independent-input controls."""
from pathlib import Path
import argparse,json,time
import sympy as S
from parametric_integer_linear import T,solve,accepted,integer_solve,specialize,gap_value

cases=[
 ('divisor',[[T]],[1]),
 ('fraction_no_roots',[[T*T+2]],[1]),
 ('fraction_with_large_solutions',[[T]],[60]),
 ('zero_row_integer_roots',[[1],[0]],[T,(T-3)*(T+7)]),
 ('zero_row_no_integer_roots',[[1],[0]],[T,T*T-2]),
 ('rational_but_not_integer',[[2]],[1]),
 ('parity',[[2]],[T]),
 ('nonlinear_residues',[[6]],[T*T+T]),
 ('bezout_parity',[[T,2]],[1]),
 ('polynomial_bezout',[[T,T+1]],[1]),
 ('resultant_mod4',[[T*T,T+2]],[1]),
 ('rank_drop_extra',[[2*T]],[T]),
 ('rank_drop_all',[[T]],[T*T]),
 ('two_parameter_coordinates',[[2,T,0],[0,3,T]],[1,T*T]),
 ('rectangular_consistent',[[T,2],[2*T,4]],[1,2]),
 ('rectangular_inconsistent',[[T,2],[2*T,4]],[1,3]),
 ('fractional_coefficients',[[T/2,S.Rational(3,2)]],[S.Rational(1,2)]),
 ('zero_matrix_consistent',[[0,0],[0,0]],[0,0]),
 ('zero_matrix_isolated',[[0,0],[0,0]],[T-4,0]),
 ('zero_matrix_impossible',[[0,0],[0,0]],[0,1]),
 ('polynomial_unimodular',[[1,T],[T,T*T+1]],[T**3+1,T*T-2]),
 ('nonconstant_determinant',[[T,1],[1,T]],[1,0]),
 ('constant_lattice_period17',[[17,T]],[T+2]),
 ('rational_root_excluded',[[2*T-1]],[1]),
]
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
out=args.output;out.mkdir(parents=True,exist_ok=False)
records=[];samples=0
for name,A,b in cases:
    begin=time.monotonic();P=S.Matrix(A);rhs=S.Matrix(b);rec=solve(P,rhs);rec['name']=name
    # These probes compare exact fixed-parameter integer equations against
    # the *complete* answer, not a bounded search substituted for it.
    scale=rec['input_scale']
    vals=sorted(set(range(-40,41))|{-10000,-101,101,10000})
    for t in vals:
        direct=integer_solve(specialize(scale*P,t),specialize(scale*rhs,t))
        assert accepted(rec,t)==(direct is not None),(name,t,rec)
        samples+=1
    rec['sample_parameters']=vals;rec['seconds']=time.monotonic()-begin;records.append(rec)
    print(name,rec['mode'],'witness',rec['witness'],'period',rec.get('K'),'bound',rec.get('bound'),flush=True)
(out/'checks.json').write_text(json.dumps(records,indent=2)+'\n')
(out/'fixtures.g').write_text('ParametricIntegerFixtures := '+gap_value(records)+';\n')
print('PASS parametric integers:',len(records),'complete systems;',samples,'specialization checks',flush=True)
