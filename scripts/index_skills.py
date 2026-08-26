#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VENDOR=ROOT/'vendor'/'anthropic-knowledge-work-plugins'
OUT=ROOT/'runtime'/'registry'/'skills-index.json'

def fm(text):
    if not text.startswith('---'): return {}
    end=text.find('\n---',3)
    if end<0:return {}
    data={}
    for line in text[3:end].strip().splitlines():
        if ':' in line:
            k,v=line.split(':',1);data[k.strip()]=v.strip().strip('"').strip("'")
    return data

skills=[]
for path in sorted(VENDOR.glob('*/skills/*/SKILL.md')):
    rel=path.relative_to(VENDOR); text=path.read_text(encoding='utf-8',errors='replace'); meta=fm(text)
    skills.append({'plugin_id':rel.parts[0],'name':meta.get('name',rel.parts[2]),'description':meta.get('description',''),'path':str(rel),'sha256':hashlib.sha256(text.encode()).hexdigest()})
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps({'source':'anthropics/knowledge-work-plugins','skills':skills},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Indexed {len(skills)} skills -> {OUT}')
