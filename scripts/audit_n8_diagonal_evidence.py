#!/usr/bin/env python3
"""Compare independent finite outputs and check polynomial interpolation scope."""
import ast,json
from pathlib import Path
from flint import fmpz_mat

records=json.loads(Path('research/certificates/N8-diagonal-quadratic-v1.json').read_text())['records']
gap=Path('research/certificates/N8-diagonal-quadratic-gap-v1.g').read_text()
native=ast.literal_eval(gap.split(':=',1)[1].strip().removesuffix(';'))
keys=['E_letters','index_sum','D_dimension','V_dimension','compatible_dimension','restriction_rank']
assert native==[[r[k] for k in keys] for r in records]
assert len(native)==44
group=json.loads(Path('research/certificates/N8-nonzero-column-block-v3/checks.json').read_text())
samples=group['samples']
monomials=[[1,t,s,t*t,t*s,s*s] for t,s in samples]
rank=fmpz_mat(monomials).rank()
assert rank==6 and len(samples)==7
# The native group verifier checked all seven values. The weight bound in
# the accompanying audit gives total parameter degree <=2. Therefore these
# values determine ALL six possible polynomial coefficients, including the
# mixed and S-squared terms; this is stronger than testing arbitrary points.
assert group['class_bound']==17 and group['p']==1 and group['q']==10 and group['t']==3
assert group['separation_ranks']==[11,12,13]
result=dict(complete_lie_spaces=44,independent_dimension_vectors_equal=True,
            quadratic_sample_matrix=monomials,quadratic_sample_rank=rank,
            quadratic_monomials=['1','T','S','T^2','TS','S^2'],
            group_separation_ranks=group['separation_ranks'],
            group_parameter_steps=group['steps'],
            accepted_parameters=group['families']['certificate']['accepted'])
out=Path('research/certificates/N8-diagonal-evidence-audit-v1.json')
assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
print('PASS N8 diagonal evidence comparison and complete quadratic interpolation')
