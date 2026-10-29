import csv,pathlib
p=pathlib.Path(__file__).parent
rows=list(csv.DictReader((p/'raw.csv').open(newline='')));seen=set();out=[]
for r in rows:
 if not r['item'] or r['id'] in seen:continue
 seen.add(r['id']);out.append(r)
with (p/'clean.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['id','category','item']);w.writeheader();w.writerows(out)
print({'input':len(rows),'output':len(out),'removed':len(rows)-len(out)})
