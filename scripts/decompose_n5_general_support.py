#!/usr/bin/env python3
import json
from pathlib import Path
from sympy import Rational
from n5_rational_lie_decomposition import decompose
from check_n5_rational_lie import serial, gap

out = Path('research/certificates/N5-general-support')
records = []
for f in json.loads((out/'input-v1.json').read_text()):
    c = [[[Rational(x) for x in v] for v in row] for row in f['structure_constants']]
    result = decompose(c)
    assert result['factor_dimensions'] == f['expected_dimensions']
    records.append(serial(dict(name=f['name'], structure_constants=c,
        expected=f['expected_dimensions'], result=result)))
    print(f['name'], result['factor_dimensions'], flush=True)
with (out/'decompositions-v1.json').open('x') as f:
    json.dump(records, f, indent=2); f.write('\n')
with (out/'decompositions-v1.g').open('x') as f:
    f.write('N5SupportLieFixtures := '+gap(records)+';\n')
print('PASS N5 support rational decompositions:', len(records), 'groups')
