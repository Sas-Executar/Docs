#!/usr/bin/env python3
import argparse, json, sys, uuid
from .router import score_domains, shortlist_skills

def main():
    p=argparse.ArgumentParser(description='Maestro portable routing planner')
    p.add_argument('--input')
    a=p.parse_args()
    payload=json.load(open(a.input,encoding='utf-8')) if a.input else json.load(sys.stdin)
    request_id=payload.get('request_id') or str(uuid.uuid4())
    raw=payload.get('raw_input','')
    context=payload.get('context',{})
    domains=score_domains(context,raw)
    skills=shortlist_skills(domains,context,raw)
    result={'request_id':request_id,'domains':domains,'selected_skills':skills,'workflow_steps':['Read PRIMARY SKILL.md','Apply PRIMARY workflow','Read/apply SUPPORTING skills','Apply VALIDATION skills when selected','Write one canonical destination','Record provenance','Return executive summary <=300 words'],'note':'Planner only; AI runtime must read selected SKILL.md files.'}
    json.dump(result,sys.stdout,ensure_ascii=False,indent=2); sys.stdout.write('\n')

if __name__=='__main__': main()
