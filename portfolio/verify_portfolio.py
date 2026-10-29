"""Check portfolio facts, links and metadata in the assembled Pages artifact."""
from pathlib import Path
from html.parser import HTMLParser
import json, re, sys, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
PUBLIC=ROOT.parent/'public'

class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if tag=='a' and a.get('href'):self.links.append(a['href'])

errors=[]
for rel in ['index.html','geo-sample.html']:
    path=PUBLIC/rel
    html=path.read_text(encoding='utf-8')
    page=Page();page.feed(html)
    for href in page.links:
        if href.startswith('#'):
            if href[1:] not in page.ids:errors.append(f'{rel}: missing anchor {href}')
        elif href.startswith(('http:','https:','mailto:')):continue
        else:
            target=(path.parent/href.split('#',1)[0]).resolve()
            if target.is_dir():target=target/'index.html'
            if not target.is_file():errors.append(f'{rel}: missing local target {href}')
    for banned in ['hand-coded','basically helping','clinics','free']:
        if re.search(r'(?<!\w)'+re.escape(banned)+r'(?!\w)', html, re.I):
            errors.append(f'{rel}: disallowed or unsupported copy {banned}')

html=(PUBLIC/'index.html').read_text(encoding='utf-8')
match=re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S)
schema=json.loads(match.group(1)) if match else {}
if len(schema.get('@graph',[]))!=2:errors.append('Person and ProfessionalService schema missing')
if 'wa.me/919893351932?text=Hi%20Archit%2C%20I%27d%20like%20to%20discuss%20a%20project' not in html:errors.append('WhatsApp CTA incorrect')
if 'Built with AI tools, checked by hand.' not in html:errors.append('AI-tools disclosure missing')
ET.parse(PUBLIC/'sitemap.xml')
for rel in ['demos/lead-capture','demos/faq-chatbot','demos/d2c-landing','demos/mini-dashboard']:
    if not (PUBLIC/rel/'index.html').is_file():errors.append(f'Missing demo {rel}')

print('Portfolio local checks:', 'PASS' if not errors else 'FAIL')
for error in errors:print('-',error)
sys.exit(0 if not errors else 1)
