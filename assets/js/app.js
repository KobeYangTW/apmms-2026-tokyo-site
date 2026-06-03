
document.addEventListener('DOMContentLoaded',()=>{
  document.querySelectorAll('a[href^="#"]').forEach(a=>{a.addEventListener('click',e=>{const t=document.querySelector(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'});}})});
  const here=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.topnav a').forEach(a=>{if(a.getAttribute('href')&&a.getAttribute('href').endsWith(here)){a.style.background='var(--lav)';}});
});
