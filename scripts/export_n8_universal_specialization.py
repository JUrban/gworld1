#!/usr/bin/env python3
"""Retain the complete weighted target presentation for independent GAP."""
from pathlib import Path
import json
from n8_universal_gauges import WeightedTensor
p,q,c=1,2,12
m=WeightedTensor(p,q,c);allhall=WeightedTensor(p,q,c+q).hall
kept=len(m.hall)
boundaries=[i for i,h in enumerate(allhall) if h['weight']>c and h['pair'] is not None and all(j<kept for j in h['pair'])]
payload=[p,q,c,[[h['weight'],list(h['pair']) if h['pair'] else []] for h in allhall],kept,boundaries]
p=Path('research/certificates/N8-universal-gauges/specialization-target.g')
if p.exists():raise SystemExit('Refuse overwrite')
p.write_text('N8UniversalTarget := '+json.dumps(payload)+';\n')
print('PASS N8 universal specialization target:',kept,'retained Hall generators')
