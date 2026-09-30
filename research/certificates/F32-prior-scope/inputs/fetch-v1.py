#!/usr/bin/env python3
"""Preserve versioned primary F32 sources and render the source statements."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.request import Request, urlopen

records = []
for name, url in [
    ('F32-Ershov-2601.01377v1', 'https://arxiv.org/pdf/2601.01377v1'),
    ('F32-Bardakov-Mikhailov-0701441v1', 'https://arxiv.org/pdf/math/0701441v1'),
]:
    pdf = Path('literature/raw') / (name + '.pdf')
    assert not pdf.exists(), 'Preserve existing source'
    with urlopen(Request(url, headers={'User-Agent': 'GroupWorld research source audit'}), timeout=45) as response:
        raw = response.read(20_000_001)
        assert len(raw) < 20_000_000 and raw.startswith(b'%PDF'), 'Unexpected source'
        final_url = response.url
    pdf.write_bytes(raw)
    text = Path('literature/text') / (name + '.txt')
    assert not text.exists()
    subprocess.run(['pdftotext', '-layout', str(pdf), str(text)], check=True)
    records.append({'url': url, 'final_url': final_url, 'path': str(pdf),
                    'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
                    'downloaded_utc': datetime.now(timezone.utc).isoformat(),
                    'reading_status': 'pending'})
    Path('literature/F32-scope-sources-v1.json').write_text(json.dumps(records, indent=2) + '\n')

# Reuse the already retained complete original-page print rendering. Its
# original HTML source is unchanged; select F32 without retyping the statement.
old = Path('research/statement-audits/F31')
metadata = json.loads((old / 'render.json').read_text())
source = Path('sources/raw/probfree.html')
assert metadata['source_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
pdf = old / 'original-page.pdf'
content = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-']).decode()
pages = [i + 1 for i, page in enumerate(content.split('\f')) if '(F32)' in page]
assert len(pages) == 1
out = Path('research/statement-audits/F32')
out.mkdir(parents=True, exist_ok=True)
assert not (out / 'statement.png').exists()
subprocess.run(['pdftoppm', '-f', str(pages[0]), '-l', str(pages[0]), '-singlefile',
                '-scale-to', '1600', '-png', str(pdf), str(out / 'statement')], check=True)
(out / 'render.json').write_text(json.dumps({
    'problem_id': 'F32', 'captured_utc': datetime.now(timezone.utc).isoformat(),
    'source_path': str(source), 'source_sha256': metadata['source_sha256'],
    'renderer': metadata['renderer'], 'reused_full_original_pdf': str(pdf),
    'reused_pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'selected_page': pages[0], 'visual_inspection': 'pending'}, indent=2) + '\n')
print('PASS F32 sources downloaded and original statement rendered; reading and viewing pending')
