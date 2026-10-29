"""Create a concise llms.txt from approved public pages only."""
from pathlib import Path
from urllib.parse import urlparse
import json, sys

src=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'entity-example.json'
data=json.loads(src.read_text(encoding='utf-8'))
base=urlparse(data['url']).netloc
lines=[f"# {data['name']}","",data['description'],"","## Public pages"]
for page in data.get('pages',[]):
    u=urlparse(page['url'])
    if u.scheme!='https' or u.netloc!=base:raise SystemExit('Public page URL must be HTTPS on the approved site')
    lines.append(f"- {page['title']}: {page['url']}")
out=src.with_name('llms.txt');out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(out)
