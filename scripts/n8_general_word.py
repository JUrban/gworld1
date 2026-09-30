#!/usr/bin/env python3
"""N8 candidate decision algorithm on a word in a free nilpotent group.

Input JSON: {"rank": r, "class_bound": c, "word": [signed generator indices]}.
The group is F_r/gamma_(c+1); class zero denotes the trivial quotient.
Positive witnesses are compact Hall words with zero-based commutator pairs.
Use the recorded runner. A failed or timed-out process is not a decision.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from n8_multigraded_magnus import Magnus
from n8_general_solver import GeneralSolver
from check_n5_rational_lie import serial


def validate(source):
    r,c,w=source['rank'],source['class_bound'],source['word']
    if type(r) is not int or r<0 or type(c) is not int or c<0:
        raise ValueError('rank and class_bound must be nonnegative integers')
    if not isinstance(w,list) or any(type(x) is not int or not 1<=abs(x)<=r for x in w):
        raise ValueError('word must be a list of nonzero signed generator indices within rank')
    return r,c,w


def decide(source, emit):
    rank,degree,word=validate(source)
    if rank==0 or degree==0:
        emit(dict(event='trivial-group'))
        return dict(answer=True,hall=[],factor_coordinates=[[],[]],route='trivial-group')
    if rank==1 or degree==1:
        exponents=[0]*rank
        for x in word:exponents[abs(x)-1]+=1 if x>0 else -1
        answer=not any(exponents)
        emit(dict(event='abelian-group',exponent_sums=exponents))
        return dict(answer=answer,hall=[[1,[]] for _ in range(rank)],
                    factor_coordinates=[[0]*rank,[0]*rank] if answer else None,
                    route='abelian-group')
    m=Magnus(rank,degree)
    target=m.expansion(word)
    solver=GeneralSolver(m,target,emit=emit)
    factors=solver.solve()
    if factors is not None:assert m.comm(*factors)==target
    return dict(answer=factors is not None,
        hall=[[h['weight'],list(h['pair']) if h['pair'] else []] for h in m.hall],
        factor_coordinates=solver.prefix(factors) if factors is not None else None,
        route='complete-integral-recursion')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    raw=args.input.read_bytes();source=json.loads(raw);validate(source)
    args.output.mkdir(parents=True,exist_ok=False)
    (args.output/'input.json').write_bytes(raw)
    status=dict(phase='running',started_utc=datetime.now(timezone.utc).isoformat(),
        input_sha256=hashlib.sha256(raw).hexdigest(),
        scope='N8(b) candidate algorithm; written general proof and novelty require specialist review')
    status_path=args.output/'status.json'
    def save_status():status_path.write_text(json.dumps(status,indent=2)+'\n')
    save_status()
    try:
        with (args.output/'trace.jsonl').open('x') as trace:
            def emit(event):
                trace.write(json.dumps(serial(event))+'\n');trace.flush()
                print(event['event'],event.get('offset',''),flush=True)
            result=decide(source,emit)
        decision=args.output/'decision.json'
        decision.write_text(json.dumps(serial(dict(input=source,**result)),indent=2)+'\n')
        status.update(phase='completed',answer=result['answer'],
            decision_sha256=hashlib.sha256(decision.read_bytes()).hexdigest(),
            ended_utc=datetime.now(timezone.utc).isoformat())
        save_status()
    except BaseException as error:
        status.update(phase='failed',error=repr(error),ended_utc=datetime.now(timezone.utc).isoformat())
        save_status();raise
    print('PASS N8 general word command',result['answer'])


if __name__=='__main__':main()
