"""Generate fact-limited Organization JSON-LD from an approved entity file."""
from pathlib import Path
from urllib.parse import urlparse
import json, sys

src=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'entity-example.json'
data=json.loads(src.read_text(encoding='utf-8'))
required=['name','url','description']
if any(not data.get(key) for key in required):raise SystemExit('Missing approved name, url or description')
url=urlparse(data['url'])
if url.scheme!='https' or not url.netloc:raise SystemExit('Use an approved HTTPS canonical URL')
schema={'@context':'https://schema.org','@type':'Organization','name':data['name'],'url':data['url'],'description':data['description']}
if data.get('sameAs'):schema['sameAs']=data['sameAs']
out=src.with_name('organization.jsonld')
out.write_text(json.dumps(schema,ensure_ascii=False,indent=2),encoding='utf-8')
print(out)
