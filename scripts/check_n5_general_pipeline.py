#!/usr/bin/env python3
import json
from pathlib import Path
from n5_general_central_solve import solve
from check_n5_rational_lie import gap

out = Path('research/certificates/N5-general-pipeline')
inputs = json.loads((out/'input-v1.json').read_text())
results = []
for data in inputs:
    result = solve(data)
    result['name'] = data['name']
    assert result['answer'] == data['expected'], (data['name'], result['answer'])
    results.append(result)
    print(data['name'], 'decomposable:', result['answer'], 'accepted branches:',
        sum(b['answer'] for b in result['branches']), '/', len(result['branches']), flush=True)
with (out/'checks-v1.json').open('x') as f:
    json.dump(results, f, indent=2);f.write('\n')
# GAP has no None; the unused missing witness is represented by zero.
gap_results = [dict(r, witness_branch=r['witness_branch'] or 0) for r in results]
with (out/'replay-v1.g').open('x') as f:
    f.write('N5GeneralPipelineInputs := '+gap(inputs)+';\n')
    f.write('N5GeneralPipelineResults := '+gap(gap_results)+';\n')
print('PASS N5 general pipeline central decisions:', len(results), 'groups;',
    sum(r['answer'] for r in results), 'positive;', sum(len(r['branches']) for r in results), 'branches')
