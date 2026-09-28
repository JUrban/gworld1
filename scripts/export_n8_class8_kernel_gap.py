#!/usr/bin/env python3
"""Translate saved class-eight kernel and obstruction records to GAP syntax."""
import json
from pathlib import Path
p=Path('research/certificates/N8-class8')
k=json.loads((p/'kernels.json').read_text())
o=json.loads((p/'obstruction.json').read_text())
h=json.loads((p/'kernel-halls.json').read_text())
rows=[[r['rank'],r['p'],r['q'],r['j'],r['C'],r['D'],r['nullity']] for r in k['records']]
obs=[[r['rank'],r['z'],r['T'],r['D'],r['Q'],r['ranks']] for r in o['records']]
halls=[[[int(r),int(d)],words] for r,dd in h.items() for d,words in dd.items()]
(p/'kernel-fixtures.g').write_text('N8C8KernelRows := '+json.dumps(rows)+';\n'
    +'N8C8ObstructionRows := '+json.dumps(obs)+';\n'
    +'N8C8KernelHalls := '+json.dumps(halls)+';\n')
