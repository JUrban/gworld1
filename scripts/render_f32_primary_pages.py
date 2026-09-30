#!/usr/bin/env python3
"""Render only the primary F32 pages whose statements are being audited."""
from pathlib import Path
import subprocess

for name, pages in [('F32-Ershov-2601.01377v1', [2]),
                    ('F32-Bardakov-Mikhailov-0701441v1', [9, 10])]:
    for page in pages:
        out = Path('literature/figures') / f'{name}-page{page}'
        assert not out.with_suffix('.png').exists()
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
                        '-scale-to', '1600', '-png', 'literature/raw/' + name + '.pdf',
                        str(out)], check=True)
print('PASS F32 primary pages rendered; visual inspection pending')
