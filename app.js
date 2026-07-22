const states={
 collections:{active:'authority',status:'Human authority exposed',posture:'Build an agent-assisted collections workflow with named escalation and recovery paths.',proof:'Resolution quality · compliance exceptions · operator acceptance',return:'Collections decision pattern + evaluation suite'},
 compliance:{active:'evidence',status:'Audit trail required',posture:'Structure the workflow around evidence, traceability, and explicit approval boundaries.',proof:'Decision trace · policy match · exception handling',return:'Reusable compliance controls + audit schema'},
 customer:{active:'work',status:'Operator reality mapped',posture:'Embed with service teams, model the real work, then automate the repeatable path.',proof:'Handle time · repeat contact · trust signal',return:'Service workflow primitive + adoption playbook'},
 operations:{active:'recovery',status:'Failure path designed',posture:'Ship the smallest working automation with rollback, owner, and measurable operating outcome.',proof:'Cycle time · rework · recovery time',return:'Operational primitive + recovery pattern'}
};
const build=document.querySelector('.buildline');
const buttons=[...document.querySelectorAll('[data-scenario]')];
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
let replayToken=0;
let currentKey='collections';
function apply(key,{animate=true}={}){
 currentKey=key;
 const s=states[key];
 buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.scenario===key)));
 document.querySelectorAll('.layer').forEach(l=>l.classList.toggle('active',l.dataset.layer===s.active));
 document.querySelector('#status').textContent=s.status;
 document.querySelector('#posture').textContent=s.posture;
 document.querySelector('#proof').textContent=s.proof;
 document.querySelector('#return').textContent=s.return;
 replayToken+=1; const token=replayToken;
 build.classList.remove('resolved');
 if(reduce||!animate){build.classList.add('resolved');return;}
 requestAnimationFrame(()=>requestAnimationFrame(()=>{if(token===replayToken)build.classList.add('resolved')}));
}
buttons.forEach((b,i)=>{
 b.addEventListener('click',()=>apply(b.dataset.scenario));
 b.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;e.preventDefault();let n=i;if(e.key==='ArrowRight')n=(i+1)%buttons.length;if(e.key==='ArrowLeft')n=(i-1+buttons.length)%buttons.length;if(e.key==='Home')n=0;if(e.key==='End')n=buttons.length-1;buttons[n].focus();buttons[n].click()});
});
document.querySelector('#resetScenario')?.addEventListener('click',()=>apply('collections'));
apply('collections',{animate:false});
const observer=new IntersectionObserver(entries=>{if(entries.some(e=>e.isIntersecting)){apply(currentKey);observer.disconnect()}},{threshold:.25});
if(build)observer.observe(build);
