#!/usr/bin/env python3
"""Target the reverse-direction branch and a transported negative witness."""
import json
from pathlib import Path
from f38_stabilizer_obstruction import necessary_condition

out = Path('research/certificates/F38-stabilizer-obstruction')
assert not (out/'checks-supplement.json').exists()
records, fixtures = [], []
for label, rank, u, v, expected_reports in [
    ('one-sided-finite-orbit-is-insufficient', 2, (1,), (1, 2, -1, -2), 2),
    ('nonminimal-negative-witness-transport', 3, (1, 2), (3,), 1),
]:
    result = necessary_condition(rank, u, v)
    assert result['status'] == 'not_boundedly_equivalent'
    assert len(result['reports']) == expected_reports
    records.append(dict(label=label, rank=rank, u=u, v=v, result=result))
    for report in result['reports']:
        check = report['orbit_check']
        if check['finite']:
            fixtures.append([rank, report['fixed'], report['moved'],
                             'finite_orbit', report['generators'], check['orbit']])
        else:
            fixtures.append([rank, report['fixed'], report['moved'],
                             'infinite_orbit_witness', check['witness'], []])
    print(label, result['status'], flush=True)
(out/'checks-supplement.json').write_text(json.dumps(records, indent=2)+'\n')
(out/'fixtures-supplement.g').write_text('F38StabilizerFixtures := '+json.dumps(fixtures)+';\n')
print('PASS F38 stabilizer supplement: 2 branch controls;', len(fixtures), 'GAP fixtures')
