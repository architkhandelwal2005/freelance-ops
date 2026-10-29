const entries=window.NILA_KNOWLEDGE||[];
function respond(question){
  const q=question.toLowerCase().replace(/[^a-z0-9 ]/g,' ').split(/\s+/).filter(x=>x.length>2);
  let best=null,score=0;
  for(const row of entries){const words=row.question.toLowerCase().split(/\W+/);const n=q.filter(word=>words.includes(word)).length;if(n>score){score=n;best=row}}
  return score>=2?{answer:best.answer,source:best.source}:{answer:'I cannot answer that from the approved pages. Please ask a human through the project owner.',source:null};
}
document.getElementById('ask').onclick=()=>{const r=respond(document.getElementById('question').value);const target=document.getElementById('answer');target.replaceChildren();const p=document.createElement('p');p.textContent=r.answer;target.append(p);if(r.source){const a=document.createElement('a');a.href=r.source;a.textContent='Source: '+r.source;target.append(a)}};
document.getElementById('question').addEventListener('keydown',e=>{if(e.key==='Enter')document.getElementById('ask').click()});
