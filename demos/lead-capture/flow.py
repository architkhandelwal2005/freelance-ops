"""Local integration contract. No email, WhatsApp or Google API calls."""
from pathlib import Path
import csv, json, re, sys

ROOT=Path(__file__).parent
FIELDS=['id','received_at','name','email','request']

def run(events):
    seen=set(); records=[]; outbox=[]; rejected=[]
    for item in events:
        if not all(item.get(k) for k in FIELDS):
            rejected.append({'id':item.get('id'),'reason':'missing field'});continue
        if not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+',item['email']):
            rejected.append({'id':item['id'],'reason':'invalid email'});continue
        if item['id'] in seen:continue
        seen.add(item['id']);records.append({k:item[k] for k in FIELDS})
        outbox.append({'kind':'owner-alert','to':'owner@example.test','record_id':item['id']})
        outbox.append({'kind':'lead-reply','to':item['email'],'record_id':item['id']})
    with (ROOT/'records.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(records)
    (ROOT/'outbox.json').write_text(json.dumps({'messages':outbox,'rejected':rejected},indent=2),encoding='utf-8')
    return len(records),len(outbox),len(rejected)

if __name__=='__main__':
    print(run(json.loads((ROOT/'examples.json').read_text(encoding='utf-8'))))
