#!/usr/bin/env python3
"""Capture an original archived HTML paragraph for a subsequent visual audit."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('id');p.add_argument('--containing-paragraph',action='store_true',help='Capture the whole original paragraph when BR-led entries share a paragraph.');args=p.parse_args()
    records=json.loads((ROOT/'data/problems.json').read_text());record=next(x for x in records if x['id']==args.id)
    source=ROOT/record['source_path'];out=ROOT/'research/statement-audits'/args.id;out.mkdir(parents=True,exist_ok=True)
    if (out/'render.json').exists():raise SystemExit('Existing audit capture will not be overwritten.')
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1200,'height':900},device_scale_factor=1)
        page.route('http://**/*',lambda route:route.abort());page.route('https://**/*',lambda route:route.abort())
        page.goto(source.as_uri(),wait_until='load')
        target=page.locator('p').filter(has_text='('+args.id+')').filter(has_not=page.locator('p')).first
        # For this renderer, require the numbered ID to lead the visible paragraph.
        text=target.inner_text()
        if not args.containing_paragraph and not text.lstrip().lstrip('*').lstrip().startswith('('+args.id+')'):
            raise SystemExit('Paragraph selector does not isolate the heading; inspect the DOM manually.')
        target.screenshot(path=str(out/'statement.png'))
        page.pdf(path=str(out/'original-page.pdf'),format='A4',print_background=True)
        metadata={'problem_id':args.id,'captured_utc':datetime.now(timezone.utc).isoformat(),
            'source_path':record['source_path'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'browser_version':browser.version,'paragraph_text':text,'scope':'The containing original HTML paragraph is captured, including any adjacent BR-led entries. Additional paragraphs/subparts must be checked separately.' if args.containing_paragraph else 'Only the selected HTML paragraph is in the screenshot; additional paragraphs/subparts must be checked separately.',
            'visual_inspection':'pending','screenshot_sha256':hashlib.sha256((out/'statement.png').read_bytes()).hexdigest()}
        (out/'render.json').write_text(json.dumps(metadata,indent=2)+'\n');browser.close()
    print(out)

if __name__=='__main__':main()
