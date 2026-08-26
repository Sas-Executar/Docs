import re
from .registry import load_index

DOMAIN_SIGNALS = {
 'sales':['sales','sell','prospect','pipeline','deal','outreach','revenue','commercial'],
 'marketing':['marketing','campaign','brand','content','seo','launch','audience','positioning'],
 'productivity':['task','calendar','workflow','daily','productivity','planning'],
 'data':['data','sql','metric','analysis','dashboard','dataset','statistics'],
 'finance':['finance','budget','reconciliation','forecast','accounting','audit'],
 'legal':['legal','contract','nda','compliance','privacy','terms','risk'],
 'customer-support':['support','ticket','customer issue','escalation','knowledge base'],
 'product-management':['product','roadmap','spec','feature','requirements','sprint','research'],
 'engineering':['code','api','architecture','implementation','bug','deploy','repository'],
 'human-resources':['hr','hiring','employee','people','recruiting','performance'],
 'operations':['operations','process','sop','capacity','vendor','procedure'],
 'design':['design','ui','ux','visual','component','handoff','accessibility'],
 'enterprise-search':['search','find','knowledge','retrieve','company docs'],
 'bio-research':['biology','genomics','clinical','target','preclinical','literature'],
 'small-business':['small business','smb','business owner','local business','business plan']
}

def score_domains(context, raw):
    text = ' '.join([raw] + [str(v) for v in context.values() if v]).lower()
    scored=[]
    for domain, signals in DOMAIN_SIGNALS.items():
        hits=[s for s in signals if s in text]
        if hits: scored.append({'domain_id':domain,'score':min(5,len(hits)+1),'hits':hits})
    scored.sort(key=lambda x:(-x['score'],x['domain_id']))
    if scored:
        scored[0]['role']='PRIMARY'
        for row in scored[1:]: row['role']='SUPPORTING' if row['score']>=3 else 'CANDIDATE'
    return scored

def shortlist_skills(domains, context, raw, limit_per_domain=4):
    index=load_index().get('skills',[])
    text=' '.join([raw]+[str(v) for v in context.values() if v]).lower()
    tokens=set(re.findall(r'[a-z0-9-]+',text))
    out=[]
    for domain in domains:
        if domain.get('role')=='CANDIDATE': continue
        candidates=[]
        for skill in index:
            if skill.get('plugin_id')!=domain['domain_id']: continue
            hay=' '.join([skill.get('name',''),skill.get('description',''),skill.get('path','')]).lower()
            score=sum(1 for t in tokens if len(t)>3 and t in hay)
            candidates.append((score,skill))
        candidates.sort(key=lambda x:(-x[0],x[1].get('name','')))
        for _,skill in candidates[:limit_per_domain]:
            out.append({**skill,'role':domain['role'],'domain_score':domain['score'],'rationale':'Shortlist only; read SKILL.md before applying.'})
    return out
