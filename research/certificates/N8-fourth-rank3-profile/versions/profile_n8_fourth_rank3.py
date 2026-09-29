#!/usr/bin/env python3
"""Thirty-second diagnostic profile; not a completed mathematical decision."""
import cProfile,pstats,signal
from pathlib import Path
from n8_fourth_layer import Magnus,decide_fourth_layer
from n8_ia_orbits import wcomm,wpow
out=Path('research/certificates/N8-fourth-rank3-profile');out.mkdir(parents=True,exist_ok=False)
class ProfileStop(Exception):pass
def stop(*args):raise ProfileStop
m=Magnus(3,8);p,q=2,3
left=list(m.bydegree[p][0]['word']);right=list(m.bydegree[q][-1]['word'])
x=wpow(left,2)+wpow(m.bydegree[p+1][-1]['word'],-2)+m.bydegree[p+2][0]['word']
y=wpow(right,-3)+m.bydegree[q+1][0]['word']+m.bydegree[q+3][-1]['word']
word=wcomm(x,y);profile=cProfile.Profile();signal.signal(signal.SIGALRM,stop)
try:
 signal.alarm(30);profile.enable();answer=decide_fourth_layer(m,word,[])
 print('Completed decision',answer['answer'])
except ProfileStop:print('Stopped intentionally after diagnostic interval; no completed decision claimed.')
finally:
 profile.disable();signal.alarm(0)
 with (out/'profile.txt').open('w') as f:pstats.Stats(profile,stream=f).sort_stats('cumulative').print_stats(45)
 (out/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print('PROFILE CAPTURED N8 rank3')
