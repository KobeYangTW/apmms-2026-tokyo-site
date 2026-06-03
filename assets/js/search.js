
const input=document.getElementById('q'); const results=document.getElementById('results'); let DATA=[];
function esc(s){return s.replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]))}
function render(q=''){const terms=q.trim().toLowerCase().split(/\s+/).filter(Boolean);let rows=DATA.filter(x=>!terms.length||terms.every(t=>(x.title+' '+x.text).toLowerCase().includes(t))).slice(0,80);results.innerHTML=rows.map(x=>`<div class="result"><span class="tag">${esc(x.type)}</span><h3><a href="${esc(x.url)}">${esc(x.title)}</a></h3><p class="muted">${esc(x.text.slice(0,180))}...</p></div>`).join('')||'<p class="muted">找不到結果，請換關鍵字。</p>'}
fetch('data/search-index.json').then(r=>r.json()).then(d=>{DATA=d;render();input.addEventListener('input',()=>render(input.value));});
