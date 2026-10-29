"""Crawl only the fictional local pages linked from pages/index.html."""
from pathlib import Path
from html.parser import HTMLParser
import json

ROOT=Path(__file__).parent
PAGES=ROOT/'pages'

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.faq=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if a.get('data-question') and a.get('data-answer'):
            self.faq.append({'question':a['data-question'],'answer':a['data-answer']})

queue=['index.html'];seen=set();records=[]
while queue:
    rel=queue.pop(0)
    path=(PAGES/rel).resolve()
    if path in seen or PAGES.resolve() not in path.parents or not path.is_file():continue
    seen.add(path);page=Page();page.feed(path.read_text(encoding='utf-8'))
    records.extend(dict(row,source='pages/'+rel) for row in page.faq)
    queue.extend(link for link in page.links if not link.startswith(('http:','https:','#')))
(ROOT/'knowledge.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(ROOT/'knowledge.js').write_text('window.NILA_KNOWLEDGE='+json.dumps(records,ensure_ascii=False)+';',encoding='utf-8')
print(f'Crawled {len(seen)} local pages; indexed {len(records)} sourced answers')
