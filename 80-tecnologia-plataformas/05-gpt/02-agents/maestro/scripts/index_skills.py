#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[7]
VENDOR = ROOT / '80-tecnologia-plataformas' / '05-gpt' / '03-skills' / 'anthropic-knowledge-work-plugins'
OUT = Path(__file__).resolve().parents[1] / 'runtime' / 'registry' / 'skills-index.json'
skills=[]
for p in sorted(VENDOR.glob('*/skills/*/SKILL.md')):
    rel=p.relative_to(VENDOR); text=p.read_text(encoding='utf-8',errors='replace')
    skills.append({'plugin_id':rel.parts[0],'name':rel.parts[2],'path':str(rel),'sha256':hashlib.sha256(text.encode()).hexdigest()})
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps({'skills':skills},indent=2),encoding='utf-8')
print(f'Indexed {len(skills)} skills')
