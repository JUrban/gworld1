#!/usr/bin/env python3
"""Export selected bounded C4 records for a separately implemented GAP replay."""
import json
from pathlib import Path
from c4_handle_probe import run,decode,PUBLISHED
root=Path(__file__).resolve().parents[1]
out=root/'research/certificates/C4-handle-probe'
s=json.loads((out/'probe.json').read_text())
rows=[('published',run(decode(PUBLISHED[0]),trace=True))]
rows += [(f'exhaustive-B{r["strands"]}-n{r["length"]}',r['best']) for r in s['exhaustive']]
rows += [(f'family-{r["conjugator_pattern"]}-{r["central_generator"]}-{r["power"]}',r['record']) for r in s['families']]
rows += [(f'evolution-B{r["strands"]}-n{r["raw_length"]}',r['best']) for r in s['evolution']]
rows += [(f'champion-ambient-B{k}',r) for k,r in s['champions'].items()]
fixtures=[]
for label,r in rows:
    assert r['status']=='complete'
    t=run(r['input'],trace=True)
    for key in ['output','steps','expanded_adjacent_letters','peak_raw','peak_after_free']:
        assert t[key]==r[key],(label,key)
    trace=[[v['p']+1,v['q']+1,v['generator'],v['expanded_adjacent_letters'],v['raw_length'],v['after_length'],v['free_cancellations']] for v in t['trace']]
    fixtures.append([label,t['input'],t['output'],t['steps'],t['expanded_adjacent_letters'],t['peak_raw'],t['peak_after_free'],trace])
(out/'gap-fixtures.g').write_text('C4Fixtures := '+json.dumps(fixtures)+';;\n')
print('PASS C4 GAP fixtures exported',len(fixtures),'records',sum(r[3] for r in fixtures),'steps')
