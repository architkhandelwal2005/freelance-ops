"""Fictional lead intake. Writes local files only; sends no messages."""
import csv, json, pathlib, re, sys
ROOT=pathlib.Path(__file__).parent
FIELDS=['id','name','email','request']
def run(events):
    seen=set(); rows=[]; alerts=[]; replies=[]; errors=[]
    for e in events:
        if not all(e.get(k) for k in FIELDS): errors.append({'id':e.get('id'),'error':'missing field'}); continue
        if not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+',e['email']): errors.append({'id':e['id'],'error':'invalid email'}); continue
        if e['id'] in seen: continue
        seen.add(e['id']); rows.append({k:e[k] for k in FIELDS})
        alerts.append({'to':'owner@example.test','subject':'New fictional enquiry','id':e['id']})
        replies.append({'to':e['email'],'subject':'We received your enquiry','id':e['id']})
    with (ROOT/'records.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
    (ROOT/'outbox.json').write_text(json.dumps({'alerts':alerts,'replies':replies,'errors':errors},indent=2))
    return len(rows),len(errors)
if __name__=='__main__':
    print(run(json.loads((ROOT/'events.json').read_text())))
