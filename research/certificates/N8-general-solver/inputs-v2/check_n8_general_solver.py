#!/usr/bin/env python3
"""Bounded integration controls for the full N8 recursion; preserve traces."""
import argparse
import json
import time
from pathlib import Path
from fractions import Fraction as Q
from n8_multigraded_magnus import Magnus
from n8_general_solver import GeneralSolver
from n8_exact_universal_periods import Group, exact_period
from n8_class3 import ONE
from n8_ia_orbits import wcomm, wpow
from n8_weighted_automorphisms import scale
from check_n5_rational_lie import serial, gap
from check_n8_delayed_gauges import description


def main(args):
    args.output.mkdir(parents=True, exist_ok=False)
    records = []
    begin = time.monotonic()

    def save():
        (args.output/'checks.json').write_text(json.dumps(serial(records), indent=2)+'\n')
        (args.output/'fixtures.g').write_text('N8GeneralFixtures := '+gap(serial(records))+';\n')

    if args.mode == 'period':
        for p, q, c, offset, divisor in [(1, 2, 7, 3, 6), (1, 1, 6, 2, 1)]:
            m = Group(p, q, c)
            kernels = m.kernels(offset)
            assert kernels
            gauges = [exact_period(m, [scale(x, Q(1, divisor)) for x in pair], offset)
                      for pair in kernels]
            desc = description((p,q), c+q)
            kept = len(m.hall)
            assert [(h['weight'],h['pair']) for h in desc[:kept]] == [(h['weight'],h['pair']) for h in m.hall]
            boundary = [i for i,h in enumerate(desc) if h['weight']>c and h['pair'] and all(j<kept for j in h['pair'])]
            row = dict(label=f'period-{p}-{q}-{c}-{offset}-div{divisor}', weights=[p,q], class_bound=c,
                       hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in desc],
                       retained=kept, boundaries=boundary, gauges=gauges)
            records.append(row); save()
            fixture = [p,q,c,row['hall'],kept,boundary,[[r['offset'],r['power'],r['plus'],r['minus']] for r in gauges]]
            (args.output/(row['label']+'.g')).write_text('N8UniversalFixture := '+gap(serial(fixture))+';\n')
            print(row['label'], [r['power'] for r in gauges], flush=True)
        assert any(g['method']=='all-polynomial-coefficients' for r in records for g in r['gauges'])
    else:
        z = wcomm([2],[1])
        d = wcomm(z,[1])
        e = wcomm(d,[1])
        u = wcomm([2],z)
        delayed_d = wcomm([1],wcomm([1],u))
        fixtures = ([
            ('identity',2,3,[],True),
            ('abelian-negative',2,3,[1],False),
            ('central-positive',2,3,wcomm(z,[1]),True),
            ('scale-sensitive',2,5,wcomm([1,1]+z,wpow(d,3)),True),
            ('equal-leading-universal',2,6,wcomm([1]+wpow(d,2),[2]+wpow(z,3)),True),
            ('nonprimitive-Nielsen',2,5,wcomm([1]+d,wpow(z,3)),True),
            ('nonprimitive-universal',2,6,wcomm([1,1]+d,[2,2,2]+z),True),
            ('exceptional-quadratic',2,7,wcomm([1]+wpow(z,3),e),True),
            ('rank3-positive',3,4,wcomm([1,2]+wcomm([3],[1]),[2,3]),True),
            ('rank4-exterior-negative',4,2,wcomm([1],[2])+wcomm([3],[4]),False),
        ] if args.mode=='core' else [
            ('delayed-exception',2,10,wcomm([1]+wpow(u,2),delayed_d),True),
        ] if args.mode=='delayed' else [
            ('quadratic-negative',2,7,wcomm([1]+wpow(z,3),e),False),
        ])
        for label, rank, degree, targetword, expected in fixtures:
            print('begin',label,rank,degree,flush=True)
            m = Magnus(rank,degree)
            if args.mode=='negative':
                # For the first normalized branch this changes
                # (3T-T^2)/2 to (1+3T-T^2)/2, whose discriminant is 13.
                # The full solver must still reject every leading branch.
                targetword = targetword + m.bydegree[7][6]['word']
            target = m.expansion(targetword)
            row = dict(label=label, rank=rank, class_bound=degree, target_word=targetword,
                       hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in m.hall],
                       expected=expected, events=[])
            records.append(row)
            def emit(event):
                row['events'].append(event)
                save()
                print(label,event['event'],event.get('offset',''),flush=True)
            solver = GeneralSolver(m,target,emit=emit)
            answer = solver.solve()
            row['accepted'] = answer is not None
            if answer is not None:
                assert m.comm(*answer)==target
                # Compact integral Hall coordinates, not huge expanded words.
                row['factor_coordinates'] = [solver.coordinates(x,1,degree) for x in answer]
            save()
            assert row['accepted']==expected, label
            print('done',label,expected,flush=True)
        events = {e['event'] for r in records for e in r['events']}
        assert 'quadratic-exception' in events
        if args.mode=='core':
            assert 'period-layer' in events and 'linear-tail' in events
            periods=[p for r in records for e in r['events'] if e['event']=='period-layer' for p in e['periods']]
            assert any(p['method']=='exact-Nielsen' and p['power']>1 for p in periods)
            assert any(p['method']=='all-polynomial-coefficients' and p['power']>1 for p in periods)
    print('PASS N8 general solver',args.mode,len(records),'controls',time.monotonic()-begin,flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['core','period','delayed','negative'],required=True)
    parser.add_argument('--output',type=Path,required=True)
    main(parser.parse_args())
