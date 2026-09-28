#!/usr/bin/env python3
"""Archive a cited public source with retrieval metadata; never overwrite evidence."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import urllib.request

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('key');p.add_argument('url');p.add_argument('--pdf',action='store_true');args=p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+',args.key):p.error('Unsafe source key')
    out=ROOT/'literature/raw';out.mkdir(parents=True,exist_ok=True)
    record_path=out/(args.key+'.json')
    if record_path.exists():raise SystemExit('Source already archived; choose a new dated/versioned key.')
    req=urllib.request.Request(args.url,headers={'User-Agent':'GroupWorld-mathematical-research/1.0'})
    record={'url':args.url,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
    with urllib.request.urlopen(req,timeout=45) as response:
        data=response.read(20*1024*1024+1)
        if len(data)>20*1024*1024:raise SystemExit('Source exceeds 20 MiB; inspect before downloading.')
        if args.pdf and not data.startswith(b'%PDF'):raise SystemExit('Expected a PDF; response is not a PDF.')
        path=out/(args.key+('.pdf' if args.pdf else '.html'));path.write_bytes(data)
        record.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),
                      path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    record_path.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))

if __name__=='__main__':main()
