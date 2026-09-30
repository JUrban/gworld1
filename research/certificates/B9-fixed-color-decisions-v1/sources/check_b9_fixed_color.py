#!/usr/bin/env python3
"""Fixed-color decisions on existing first colors, with finite proof data."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from b9_fixed_color import ResourceLimit, delete, equal, exponent, fibre, positive_fraction, special
from b9_special_braids import inverse, reduce_word, shift


def gap(value):
    if isinstance(value, (list, tuple)):
        return '['+','.join(gap(x) for x in value)+']'
    if isinstance(value, dict):
        return 'rec('+','.join(k+':='+gap(v) for k, v in value.items())+')'
    if value is None:
        return 'fail'
    return json.dumps(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    source = Path('research/certificates/B9/height4.json')
    inputs = json.loads(source.read_text())['records']
    controls = []
    for name, w, wanted in [('identity', (), True), ('positive_nonspecial', (2,), False),
                            ('nontrivial_zero_exponent', (1, -2), False),
                            ('special_nonliteral', (-2, -1, 2, 2, 1), True),
                            ('negative_generator', (-1,), False),
                            ('shifted_positive', (3,), False)]:
        result = special(w)
        assert result['special'] == wanted, name
        controls.append(dict(name=name, classification=result))
    reversal_controls = []
    for w in [(-1, 2), (-2, 1), (-1, 3), (-1, 1), (1, -2, -1, 2)]:
        fraction, count = positive_fraction(w)
        assert equal(w, fraction)
        reversal_controls.append(dict(word=w, fraction=fraction, steps=count))
    # Groupoid deletion: a prefix in B3 remains unchanged, while a shifted
    # suffix becomes a power of sigma2 on the two other retained strands.
    product_controls = []
    for A in [(), (1,), (2, 1, -2), (1, 1, -2)]:
        for h in [(), (2,), (2, 3, -2), (4, 2, -3, -2)]:
            word = A+h
            parameter, _ = delete(word, 5, (1, 2, 3))
            tail, _ = delete(h, 5, (1, 2, 3))
            assert all(abs(a) == 2 for a in tail)
            assert equal(parameter, A+tail)
            product_controls.append(dict(A=A, h=h, word=word, parameter=parameter, tail=tail))
    records = []
    for index, record in enumerate(inputs):
        try:
            result = fibre(record['word'])
        except ResourceLimit as error:
            result = dict(word=record['word'],status='incomplete',reason=str(error))
        result['source_index'] = index
        records.append(result)
        print('INPUT',index,'STATUS',result['status'],'REASON',result['reason'],
              'SOLUTIONS',len(result.get('solutions',[])),flush=True)
    stats = Counter(r['status'] for r in records)
    stats['first_colors_with_solutions'] = sum(bool(r.get('solutions')) for r in records)
    stats['all_solutions'] = sum(len(r.get('solutions',[])) for r in records)
    stats['candidate_specialness_tests'] = sum(len(r.get('candidates',[])) for r in records)
    result = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Complete fibre per completed supplied first color; all52 old height-four inputs, no new term enumeration',
                  input=dict(path=str(source),sha256=hashlib.sha256(source.read_bytes()).hexdigest()),
                  summary=dict(stats), records=records, controls=controls,
                  reversal_controls=reversal_controls, product_controls=product_controls)
    (out/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    export={k:v for k,v in result.items() if k not in ['created_utc','scope','input']}
    (out/'fixtures.g').write_text('B9FixedColor:='+gap(export)+';\n')
    print(json.dumps(dict(stats),indent=2))
    assert stats['complete'] == len(inputs) and not stats['incomplete']
    print('PASS B9 fixed first color decisions')


if __name__ == '__main__':
    main()
