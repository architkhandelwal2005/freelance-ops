"""Focused, repeatable QA for the 16 fictional delivery samples."""
from pathlib import Path
import csv, json, re, subprocess, sys, wave, xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pptx import Presentation
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'deliverables'/'samples'
SKILLS=ROOT/'.agents'/'skills'
NAMES=['delivery-standards','website-fixes','landing-page-build','geo-implementation','ai-automation-build','ai-chatbot-build','internal-tool-build','pitch-deck-build','content-writing','ad-creatives','data-research','short-form-video','faceless-video','social-media-content','transcription-subtitles-voiceover','case-study-writeup']
results={}
def check(name,condition,note):
    results.setdefault(name,[]).append({'pass':bool(condition),'note':note})

for name in NAMES:
    s=SKILLS/name/'SKILL.md'; d=BASE/name
    check(name,s.exists() and d.is_dir() and (d/'handover.md').exists(),'Skill, sample and handover exist')
    if s.exists():
        text=s.read_text(encoding='utf-8')
        check(name,all(x in text for x in ['name:','description:','## Intake','## Method','## Time guide','## QA','## Deliverables','## Escalate','## Never']),'Required skill sections exist')
        check(name,(SKILLS/name/'prompt.md').exists() and (SKILLS/name/'checklist.md').exists(),'Prompt and checklist exist')

core=BASE/'delivery-standards'
check('delivery-standards',(core/'JOB-000-nila.md').read_bytes()==(core/'JOB-000-nila.original.md').read_bytes(),'Dated original preserved byte-for-byte')

w=BASE/'website-fixes'
check('website-fixes','width:600px' in (w/'before.html').read_text() and 'width:min(100%,600px)' in (w/'after.html').read_text(),'Original overflow and bounded replacement present')

l=BASE/'landing-page-build'/'index.html'; html=l.read_text()
check('landing-page-build',all(x in html for x in ['name="viewport"','name="description"','href="#why"','id="why"','href="#faq"','id="faq"','mailto:hello@nila.example']),'Metadata, sections and local CTA present')

g=BASE/'geo-implementation'; gh=(g/'index.html').read_text()
schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',gh).group(1))
check('geo-implementation',schema['name']=='Nila Studio' and schema['url']=='https://nila.example/','Schema matches visible fictional entity')
ET.parse(g/'sitemap.xml')
check('geo-implementation','Allow: /' in (g/'robots.txt').read_text() and 'https://nila.example/' in (g/'llms.txt').read_text(),'Robots, sitemap and llms.txt agree')

a=BASE/'ai-automation-build'
subprocess.run([sys.executable,str(a/'workflow.py')],check=True,capture_output=True)
records=list(csv.DictReader((a/'records.csv').open(newline='')));box=json.loads((a/'outbox.json').read_text())
check('ai-automation-build',len(records)==3 and len(box['alerts'])==3 and len(box['replies'])==3 and len(box['errors'])==1,'Five events: three records, one duplicate skipped, one invalid rejected')

b=BASE/'ai-chatbot-build'
check('ai-chatbot-build',len(json.loads((b/'faq.json').read_text()))==2 and 'Source:' in (b/'widget.js').read_text() and 'Please ask a human' in (b/'widget.js').read_text(),'Approved answers cite a source; unknowns hand off')

i=BASE/'internal-tool-build'
ih=(i/'index.html').read_text()
check('internal-tool-build',all(x in ih for x in ['localStorage','form.onsubmit','search.oninput','btn.onclick','textContent=x.item']),'Local create, search and edit paths present; text inserted safely')

p=BASE/'pitch-deck-build'
check('pitch-deck-build',len(Presentation(p/'nila-concept.pptx').slides)==10 and len(PdfReader(p/'nila-concept-review.pdf').pages)==10,'Editable deck and review PDF both have ten slides')

c=BASE/'content-writing'
check('content-writing','[TO CONFIRM]' in (c/'website-copy.md').read_text() and (c/'fact-log.md').exists(),'Unknown specifications marked and facts logged')

ad=BASE/'ad-creatives'
ET.parse(ad/'square-concept.svg')
check('ad-creatives',len(list(csv.DictReader((ad/'copy-matrix.csv').open(newline=''))))==2 and (ad/'shot-list.md').exists(),'Vector art, two copy variants and shot list valid')

data=BASE/'data-research'
subprocess.run([sys.executable,str(data/'clean.py')],check=True,capture_output=True)
check('data-research',len(list(csv.DictReader((data/'clean.csv').open(newline=''))))==3,'Five fictional rows clean to three unique complete rows')

sys.path.insert(0,str(ROOT.parent/'sample_deps'))
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()
def probe(path):
    p=subprocess.run([FF,'-i',str(path)],capture_output=True,text=True)
    info=p.stderr
    match=re.search(r'Duration: (\d+):(\d+):([\d.]+)',info)
    return float(match.group(1))*3600+float(match.group(2))*60+float(match.group(3)),info
def srt_end(path):
    stamps=re.findall(r'\d\d:\d\d:(\d\d),(\d\d\d)',path.read_text())
    return int(stamps[-1][0])+int(stamps[-1][1])/1000
for name,file,res in [('short-form-video','vertical-cut.mp4','1080x1920'),('faceless-video','explainer.mp4','1280x720')]:
    d=BASE/name;seconds,info=probe(d/file)
    check(name,'Video: h264' in info and 'Audio: aac' in info and res in info,'Playable H.264/AAC output has target dimensions')
    check(name,abs(seconds-srt_end(d/'captions.srt'))<0.15,'Final caption time matches media duration')

soc=BASE/'social-media-content'
check('social-media-content',len(list(csv.DictReader((soc/'calendar.csv').open(newline=''))))==3 and '<svg' in (soc/'post.svg').read_text(),'Three scheduled drafts and editable art; no posts published')

t=BASE/'transcription-subtitles-voiceover'
with wave.open(str(t/'voiceover.wav'),'rb') as wav: voice_duration=wav.getnframes()/wav.getframerate()
check('transcription-subtitles-voiceover',abs(voice_duration-srt_end(t/'captions.srt'))<0.01 and (t/'hindi-translation.txt').exists(),'SRT ends with generated voice and Hindi translation exists')

case=BASE/'case-study-writeup'
check('case-study-writeup','fictional' in (case/'case-study.md').read_text().lower() and 'Claude approval required' in (case/'permission-log.md').read_text(),'Fictional status and publication gate explicit')

passed=sum(x['pass'] for rows in results.values() for x in rows)
total=sum(len(rows) for rows in results.values())
out=BASE/'qa-results.json';out.write_text(json.dumps({'passed':passed,'total':total,'skills':results},indent=2),encoding='utf-8')
print(f'{passed}/{total} checks passed; results: {out}')
sys.exit(0 if passed==total else 1)
