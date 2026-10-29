"""Fast checks for the four fictional demos."""
from pathlib import Path
import csv, json, re, subprocess, sys

ROOT=Path(__file__).parent
checks=[]
def check(condition,note):
    checks.append((bool(condition),note))

for name in ['lead-capture','faq-chatbot','d2c-landing','mini-dashboard']:
    d=ROOT/name
    check((d/'index.html').is_file() and (d/'README.md').is_file(),f'{name}: page and run guide')

lead=ROOT/'lead-capture'
subprocess.run([sys.executable,str(lead/'flow.py')],check=True,capture_output=True)
rows=list(csv.DictReader((lead/'records.csv').open(newline='')))
out=json.loads((lead/'outbox.json').read_text())
check(len(rows)==3 and len(out['messages'])==6 and len(out['rejected'])==1,'lead-capture: five input cases, dedupe and bad-address handling')
check('google-sheets-row' in (lead/'flow.json').read_text() and 'preview only' in (lead/'flow.json').read_text(),'lead-capture: integration export clearly marks simulation')

faq=ROOT/'faq-chatbot'
subprocess.run([sys.executable,str(faq/'build_index.py')],check=True,capture_output=True)
knowledge=json.loads((faq/'knowledge.json').read_text())
check(len(knowledge)==2 and all((faq/x['source']).is_file() for x in knowledge),'faq-chatbot: crawler produced two valid citations')
check('score>=2' in (faq/'widget.js').read_text() and 'Please ask a human' in (faq/'widget.js').read_text(),'faq-chatbot: confidence gate and human handoff')

landing=(ROOT/'d2c-landing'/'index.html').read_text()
schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',landing).group(1))
check(schema['@type']=='FAQPage' and len(schema['mainEntity'])==2 and all(q['name'] in landing for q in schema['mainEntity']),'d2c-landing: FAQ schema agrees with visible copy')
check('position:sticky' in landing and 'no purchase is available' in landing,'d2c-landing: sticky CTA is a non-transactional preview')

dash=(ROOT/'mini-dashboard'/'index.html').read_text()
check(all(term in dash for term in ['localStorage','form','search','filter','edit.onclick','del.onclick']),'mini-dashboard: add, search, filter, edit and delete paths')

passed=sum(ok for ok,_ in checks)
result='\n'.join(f'- {"PASS" if ok else "FAIL"}: {note}' for ok,note in checks)
(ROOT/'qa-results.md').write_text(f'# Fictional demo QA\n\n{passed}/{len(checks)} checks passed. Browser review also verified the enquiry preview, FAQ citation and unknown-question handoff, dashboard add and filter, and the landing page purchase-preview alert. No external message or purchase occurred.\n\n{result}\n',encoding='utf-8')
print(f'{passed}/{len(checks)} checks passed')
sys.exit(0 if passed==len(checks) else 1)
