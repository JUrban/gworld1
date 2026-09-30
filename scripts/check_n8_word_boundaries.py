#!/usr/bin/env python3
"""Elementary boundary controls, including invalid input rejection."""
import argparse,json
from pathlib import Path
from n8_general_word import decide,validate


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    cases=[(0,0,[],True),(0,5,[],True),(2,0,[1],True),
           (1,1,[1,-1],True),(1,9,[1,1,-1],False),(1,9,[],True),
           (3,1,[1,2,-1,-2],True),(3,1,[1,2,-1],False)]
    records=[]
    for r,c,w,expected in cases:
        source=dict(rank=r,class_bound=c,word=w);events=[]
        result=decide(source,events.append);assert result['answer']==expected
        records.append(dict(input=source,result=result,events=events))
    invalid=[dict(rank=2,class_bound=3,word=[0]),dict(rank=2,class_bound=3,word=[3]),
             dict(rank=True,class_bound=2,word=[]),dict(rank=2,class_bound=-1,word=[])]
    for source in invalid:
        try:validate(source)
        except ValueError:pass
        else:raise AssertionError(('invalid input accepted',source))
    (args.output/'checks.json').write_text(json.dumps(dict(cases=records,rejected=invalid),indent=2)+'\n')
    print('PASS N8 word boundaries',len(cases),len(invalid))


if __name__=='__main__':main()
