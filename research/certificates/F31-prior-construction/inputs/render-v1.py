#!/usr/bin/env python3
"""Capture original F31 HTML and three retained primary PDF pages."""
import os
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[1]
env=dict(os.environ)
env['LD_LIBRARY_PATH']=str(root/'scratch/browser-libs/root/usr/lib/x86_64-linux-gnu')
subprocess.run([str(root/'.venv/bin/python'),'scripts/render_statement.py','F31'],
               cwd=root,env=env,check=True)
for page in [7,9,11]:
    out=root/'literature/figures'/f'F31-Lei-Zhang-page{page}'
    assert not out.with_suffix('.png').exists()
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600',
                    '-png','literature/raw/F31-Lei-Zhang-2604.24502.pdf',str(out)],
                   cwd=root,check=True)
print('PASS F31 source renders; visual inspection still required')
