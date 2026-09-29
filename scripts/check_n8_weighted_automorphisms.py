#!/usr/bin/env python3
"""Deterministic exact fixtures for the weighted free-generator construction."""
import argparse
import json
from pathlib import Path

from n8_weighted_automorphisms import Auto, Tensor, Weighted, add, integral_terms, scale

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--case', type=int, required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
out = ROOT / args.output
out.mkdir(parents=True, exist_ok=False)

# Hall indices are zero-based. The entire Hall bracket table is exported.
cases = [
    dict(rank=2, degree=4, p=1, q=2, x=[[0,1]], y=[[2,1]], all_maps=True),
    dict(rank=2, degree=5, p=1, q=2, x=[[0,2]], y=[[2,3]], all_maps=False),
    dict(rank=3, degree=5, p=2, q=2, x=[[3,2]], y=[[4,3]], all_maps=False),
    dict(rank=2, degree=6, p=2, q=3, x=[[2,2]], y=[[3,3]], all_maps=False),
    dict(rank=2, degree=6, p=1, q=3, x=[[0,1]], y=[[4,2]], all_maps=False),
    dict(rank=2, degree=7, p=3, q=4, x=[[3,2]], y=[[5,3]], all_maps=False),
]
case = cases[args.case]
print('CASE', args.case, case, flush=True)
m = Tensor(case['rank'], case['degree'])
a = Weighted(m, case['x'], case['y'], case['p'], case['q'])
print('BUILT', len(m.hall), 'ambient;', len(a.nodes), 'subalgebra;',
      len(a.generators), 'free generators', flush=True)
data = dict(case=case, ambient_dimension=len(m.hall), dimension=len(a.nodes),
            generator_weights=[g['weight'] for g in a.generators],
            decomposable_dimensions=a.decomposable_dimensions, maps=[], controls=[])
fixtures = []


def save():
    (out/'checks.json').write_text(json.dumps(data, indent=2)+'\n')
    (out/'fixtures.g').write_text('N8WeightedFixtures := '+json.dumps(fixtures)+';\n')


table = [[h['weight'], [] if h['pair'] is None else list(h['pair'])] for h in m.hall]
corrections = []
for label, weight in [('C', a.p), ('D', a.q)]:
    for d in range(weight+1, m.degree+1):
        indices = m.layers[d][0]
        selected = indices if case['all_maps'] else indices[:1]
        for i in selected:
            corrections.append((label, i, m.hall[i]['lie']))

for label, hall_index, correction in corrections:
    alpha = a.auto(label, correction)
    lie_checks = alpha.check_lie()
    power, failures = alpha.integral_power()
    direct_images, inverse_images = [], []
    for v in a.klogs:
        plus, minus = alpha.power_on(v, power), alpha.power_on(v, -power)
        assert alpha.power_on(plus, -power) == v
        assert alpha.power_on(minus, power) == v
        direct_images.append(integral_terms(m, plus))
        inverse_images.append(integral_terms(m, minus))
    t = m.hall[hall_index]['weight'] - (a.p if label == 'C' else a.q)
    # The increments must be diagonal on every pair, not just on chosen lifts.
    x = m.mul(a.x, m.group_hall(m.layers[a.p+1][0][0]))
    y = m.mul(a.y, m.power(m.group_hall(m.layers[a.q+1][0][-1]), -2))
    bx, by = m.log(x), m.log(y)
    ax, ay = alpha.power_on(bx, power), alpha.power_on(by, power)
    dx, dy = add(ax,bx,-1), add(ay,by,-1)
    assert all(len(w)>=a.p+t for w in dx)
    assert all(len(w)>=a.q+t for w in dy)
    assert m.layer(dx,a.p+t) == (scale(correction,power) if label=='C' else {})
    assert m.layer(dy,a.q+t) == (scale(correction,power) if label=='D' else {})
    original = m.log(m.comm(x,y))
    changed = m.log(m.comm(m.exp(ax),m.exp(ay)))
    assert changed == alpha.power_on(original,power)
    fixtures.append([m.rank,m.degree,table,a.kterms,direct_images,inverse_images,
                     integral_terms(m,bx),integral_terms(m,by),
                     integral_terms(m,ax),integral_terms(m,ay),
                     integral_terms(m,original),integral_terms(m,changed)])
    data['maps'].append(dict(label=label, correction_hall_index=hall_index,
                             offset=t, integral_power=power, rejected_powers=failures,
                             lie_bracket_checks=lie_checks,
                             integral_images=len(a.klogs)*2))
    save()
    print('MAP',label,hall_index,'power',power,'rejected',len(failures),flush=True)

# An actual decomposable leading factor must not be admitted as a free generator.
if a.p==1 and m.rank==2:
    try:
        Weighted(m, [[0,1]], [[3,1]], 1, 3)
    except ValueError as error:
        assert 'decomposable' in str(error)
        data['controls'].append('D=[[b,a],a] rejected as decomposable')
    else:
        raise AssertionError('Decomposable D was allowed as a free generator')
outside=m.letters[-1]
try:
    a.kcoordinates(outside)
except (ValueError,AssertionError):
    data['controls'].append('ambient generator outside K rejected')
else:
    raise AssertionError('Outside-K element accepted')
save()
print('PASS N8 weighted construction:',args.case,len(data['maps']),'maps;',
      len(data['controls']),'controls',flush=True)
