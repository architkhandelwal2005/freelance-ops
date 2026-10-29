"""Email -> summary -> task starter. Local fixture only; no inbox/API calls."""
from email import policy
from email.parser import BytesParser
from pathlib import Path
import json, re

ROOT=Path(__file__).parent

def summarize(text):
    """Safe local placeholder. Replace with an approved AI API adapter and review."""
    return re.sub(r'\s+', ' ', text).strip()[:240]

def run(path):
    message=BytesParser(policy=policy.default).parsebytes(Path(path).read_bytes())
    body=message.get_body(preferencelist=('plain',))
    text=body.get_content() if body else ''
    task={'source_subject':message['subject'],'summary':summarize(text),'owner':'[TO CONFIRM]','status':'review-needed'}
    (ROOT/'task-preview.json').write_text(json.dumps(task,indent=2),encoding='utf-8')
    return task

if __name__=='__main__':
    print(run(ROOT/'sample.eml'))
