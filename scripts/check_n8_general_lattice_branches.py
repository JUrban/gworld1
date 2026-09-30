#!/usr/bin/env python3
"""Targeted full-recursion probe for fixed and nonunit exceptional parameters."""
import argparse,json,time
from pathlib import Path
from n8_multigraded_magnus import Magnus
from n8_general_solver import GeneralSolver
from n8_ia_orbits import wcomm,wpow
from check_n5_rational_lie import serial
from check_n8_general_solver import gap_native


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    args.output.mkdir(parents=True,exist_ok=False);begin=time.monotonic();records=[]
    def save():
        (args.output/'checks.json').write_text(json.dumps(serial(records),indent=2)+'\n')
        (args.output/'fixtures.g').write_text('N8GeneralFixtures := '+gap_native(serial(records))+';\n')
    m=Magnus(2,10);z=wcomm([2],[1]);u=wcomm([2],z);d=wcomm([1],wcomm([1],u))
    for label,x,y in [
        ('fixed-earlier-prefix',[1]+z+wpow(u,2),d),
        ('scaled-delayed',[1,1]+wpow(u,2),wpow(d,3)),
        ('scaled-fixed-prefix',[1,1]+z+wpow(u,2),wpow(d,3)),
    ]:
        targetword=wcomm(x,y);target=m.expansion(targetword)
        row=dict(label=label,rank=2,class_bound=10,target_word=targetword,
                 planted_words=[x,y],hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in m.hall],events=[])
        records.append(row)
        def emit(e):
            row['events'].append(e);save();print(label,e['event'],e.get('offset',''),e.get('parameter_step',''),flush=True)
        solver=GeneralSolver(m,target,emit=emit);answer=solver.solve()
        row['accepted']=answer is not None
        if answer is not None:
            assert m.comm(*answer)==target;row['factor_coordinates']=solver.prefix(answer)
        save();assert row['accepted'],'Planted commutator was not recognized'
    events=[e for r in records for e in r['events']]
    summary=dict(fixed_exception_count=sum(e['event']=='fixed-exception' for e in events),
        parameter_steps=[e['parameter_step'] for e in events if e['event']=='quadratic-exception'],seconds=time.monotonic()-begin)
    (args.output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)
    print('COMPLETE N8 lattice branch probe; inspect actual branch coverage',flush=True)


if __name__=='__main__':main()
