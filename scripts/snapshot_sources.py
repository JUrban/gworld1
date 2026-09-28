#!/usr/bin/env python3
"""Snapshot problem pages and their local background/resources; never solve."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://shpilrain.ccny.cuny.edu/gworld/problems/'
LIMIT = 20 * 1024 * 1024


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ['href', 'src', 'background']:
            if attrs.get(key): self.links.append((tag, key, attrs[key].strip()))


def canonical(url):
    url = urllib.parse.urldefrag(url)[0]
    if url.startswith('http://shpilrain.ccny.cuny.edu/'):
        url = 'https://' + url[len('http://'):]
    return url


def download(url):
    record = {'url': url, 'retrieved_utc': datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'GroupWorld-research-preparation/1.0 (source archival only)'})
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read(LIMIT + 1)
            if len(data) > LIMIT: raise ValueError('File exceeds 20 MiB preparation limit')
            name = urllib.parse.unquote(url[len(BASE):])
            assert name and '..' not in Path(name).parts and not name.startswith('/')
            path = ROOT / 'sources/raw' / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            record.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get('Content-Type'),
                          last_modified=response.headers.get('Last-Modified'),
                          path=str(path.relative_to(ROOT)), bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest())
            found = []
            if 'html' in (record['content_type'] or '') or name.lower().endswith(('.htm', '.html')):
                text = data.decode('latin-1')
                parser = Links(); parser.feed(text)
                record['links'] = [{'tag': t, 'attribute': k, 'target': v,
                                    'absolute_url': urllib.parse.urljoin(url, v)} for t,k,v in parser.links]
                for _, _, target in parser.links:
                    candidate = canonical(urllib.parse.urljoin(url, target))
                    if candidate.startswith(BASE) and not urllib.parse.urlsplit(candidate).query:
                        suffix = Path(urllib.parse.urlsplit(candidate).path).suffix.lower()
                        if suffix in {'.html','.htm','.gif','.png','.jpg','.jpeg','.svg','.css','.pdf','.ps','.tex','.txt','.dvi'}:
                            found.append(candidate)
            return record, found
    except (urllib.error.URLError, OSError, ValueError) as error:
        record.update(status='error', error=str(error))
        return record, []


def main():
    session = ROOT / 'state/session.json'
    if session.exists() and json.loads(session.read_text()).get('phase') != 'preparation':
        raise SystemExit('Do not overwrite the frozen corpus after the run starts.')
    manifest = ROOT / 'sources/manifest.json'
    if manifest.exists():
        raise SystemExit('Snapshot already exists; preserve it and make an explicitly dated new snapshot instead.')
    pending = {BASE + 'oproblems.html', BASE + 'Halloffame.html'}
    seen = set(); records = []
    while pending:
        batch = sorted(pending - seen); pending = set()
        if not batch: break
        seen.update(batch)
        with ThreadPoolExecutor(max_workers=3) as pool:
            for record, links in pool.map(download, batch):
                records.append(record); pending.update(set(links) - seen)
                print(record['status'], record['url'], flush=True)
        assert len(seen) < 500, 'Unexpected crawl growth; inspect scope.'
    out = {'snapshot_date': datetime.now(timezone.utc).date().isoformat(),
           'scope': 'Both supplied pages and recursively linked resources under /gworld/problems/. External references are indexed but not recursively crawled.',
           'base_url': BASE, 'records': sorted(records, key=lambda r:r['url'])}
    manifest.write_text(json.dumps(out, indent=2) + '\n')
    print('Saved',len(records),'records;',sum(r['status']=='error' for r in records),'failures.')


if __name__ == '__main__': main()
