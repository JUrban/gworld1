#!/usr/bin/env python3
"""Capture original F31 HTML and three retained primary PDF pages."""
from datetime import datetime,timezone
import hashlib
from importlib.metadata import distributions
import json
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
libs=root/'scratch/f31-render-libs'
sys.path.insert(0,str(libs))
from weasyprint import HTML,__version__
outdir=root/'research/statement-audits/F31'
outdir.mkdir(parents=True,exist_ok=True)
pdf=outdir/'original-page.pdf'
assert not pdf.exists()
source=root/'sources/raw/probfree.html'
HTML(filename=str(source)).write_pdf(str(pdf),presentational_hints=True)
text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-']).decode()
pages=[i+1 for i,p in enumerate(text.split('\f')) if '(F31)' in p]
assert len(pages)==1
subprocess.run(['pdftoppm','-f',str(pages[0]),'-l',str(pages[0]),'-singlefile',
                '-scale-to','1600','-png',str(pdf),str(outdir/'statement')],check=True)
metadata={'problem_id':'F31','captured_utc':datetime.now(timezone.utc).isoformat(),
          'source_path':'sources/raw/probfree.html',
          'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'renderer':'WeasyPrint '+__version__,'scope':'Full original archived HTML rendered without transcription; selected PDF page containing F31. Static print layout differs from Chromium.',
          'selected_page':pages[0],'visual_inspection':'pending',
          'python_dependencies':{d.metadata['Name']:d.version for d in distributions(path=[str(libs)])}}
(outdir/'render.json').write_text(json.dumps(metadata,indent=2)+'\n')
for page in [7,9,11]:
    out=root/'literature/figures'/f'F31-Lei-Zhang-page{page}'
    assert not out.with_suffix('.png').exists()
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600',
                    '-png','literature/raw/F31-Lei-Zhang-2604.24502.pdf',str(out)],
                   cwd=root,check=True)
print('PASS F31 source renders; visual inspection still required')
