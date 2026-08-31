#!/usr/bin/env python3
"""Gera os registros auxiliares OUT-54..OUT-59 a partir dos insights
estrategicos e do formulario fundido. Deterministico e reexecutavel."""
import csv, glob, os, yaml, hashlib

SC='/tmp/claude-0/-home-user-Docs/d4a8bd8f-cfce-5097-8526-923ed22a8003/scratchpad'
OUT='/home/user/Docs/60-dados/90-evidence'
FORM='/home/user/Docs/01-master-index/01-schemas/FORMULARIO_FUNDACIONAL_FUSIONADO_V1.yaml'
os.makedirs(OUT, exist_ok=True)

insights=[]
for p in sorted(glob.glob(f'{SC}/strategic_insights*.csv')):
    if 'CONSOLIDADO' in p.upper(): continue
    rodada = 'r2' if '_r2' in p else 'r1'
    for r in csv.DictReader(open(p, encoding='utf-8')):
        r['_rodada']=rodada; insights.append(r)

form=yaml.safe_load(open(FORM))
campos=[(a['area_id'],a['area_name'],f) for a in form['areas'] for f in a['fields']]

def rid(*parts):
    return hashlib.sha256('|'.join(parts).encode()).hexdigest()[:10]

def dump(nome, cols, linhas):
    p=f'{OUT}/{nome}'
    with open(p,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
        for l in linhas: w.writerow(l)
    print(f'{nome}: {len(linhas)} linhas')

# OUT-54 evidence register: toda afirmacao com sua fonte
ev=[]
for r in insights:
    for d in [x.strip() for x in r['evidence_record_ids'].split(';') if x.strip()]:
        ev.append(dict(evidencia_id='EV-'+rid(r['framework'],r['claim'],d), origem='strategic_analysis',
            rodada=r['_rodada'], claim_ou_campo=r['claim'], framework=r['framework'], dimensao=r['dimension'],
            unidade=r['entity'], documento_id=d, evidencia=r['evidence'],
            forca=r['evidence_strength'], confianca=r['confidence'], status=r['status']))
for aid,anome,f in campos:
    for d in (f.get('documento_ids') or []):
        ev.append(dict(evidencia_id='EV-'+rid(f['field_id'],d), origem='formulario',
            rodada='dia1-2', claim_ou_campo=f"{f['field_id']} {f['title']}", framework='', dimensao=anome,
            unidade=f.get('eco_unit',''), documento_id=d, evidencia=f.get('evidencia',''),
            forca='', confianca=f.get('confianca',''), status=f['status']))
dump('OUT-54_EVIDENCE_REGISTER.csv',
     ['evidencia_id','origem','rodada','claim_ou_campo','framework','dimensao','unidade',
      'documento_id','evidencia','forca','confianca','status'], ev)

# OUT-55 hypothesis register
hy=[dict(hipotese_id='HY-'+rid(r['framework'],r['claim']), unidade=r['entity'], framework=r['framework'],
         hipotese=r['claim'], evidencia_atual=r['evidence'], documento_ids=r['evidence_record_ids'],
         confianca=r['confidence'], teste_necessario=r['recommendation'], origem='strategic_analysis')
    for r in insights if r['status']=='hypothesis']
hy+=[dict(hipotese_id='HY-'+rid(f['field_id']), unidade=f.get('eco_unit',''), framework='',
          hipotese=f"{f['field_id']} {f['title']}: {str(f.get('valor'))[:200]}",
          evidencia_atual=f.get('evidencia',''), documento_ids=';'.join(f.get('documento_ids') or []),
          confianca=f.get('confianca',''), teste_necessario=f.get('proxima_acao',''), origem='formulario')
     for aid,an,f in campos if f.get('tipo_informacao')=='hipotese' or f['status']=='hipotese']
dump('OUT-55_HYPOTHESIS_REGISTER.csv',
     ['hipotese_id','unidade','framework','hipotese','evidencia_atual','documento_ids',
      'confianca','teste_necessario','origem'], hy)

# OUT-56 decision log
dec=[]
for c in form.get('conflitos_registrados',[]):
    dec.append(dict(decisao_id='DEC-'+rid(c['id']), contexto=c['descricao'], decisao=c.get('resolucao','') or 'em aberto',
        alternativas='', justificativa=c.get('acao',''), data='2026-08-31', impacto=c['campo'], origem='maestro'))
for r in insights:
    if r['status']=='conflict':
        dec.append(dict(decisao_id='DEC-'+rid(r['framework'],r['claim']), contexto=r['claim'],
            decisao='NAO ARBITRADO — conflito preservado', alternativas=r['evidence'],
            justificativa=r['recommendation'], data='2026-08-31', impacto=f"{r['entity']}/{r['framework']}",
            origem='strategic_analysis'))
dump('OUT-56_DECISION_LOG.csv',
     ['decisao_id','contexto','decisao','alternativas','justificativa','data','impacto','origem'], dec)

# OUT-57 risk register
ri=[dict(risco_id='RI-'+rid(r['framework'],r['claim']), unidade=r['entity'], framework=r['framework'],
         evento=r['claim'], causa_evidencia=r['evidence'], documento_ids=r['evidence_record_ids'],
         impacto=r['impact'], urgencia=r['urgency'], controle=r['recommendation'], status_evidencia=r['status'])
    for r in insights if r['impact']=='high' or r['status']=='conflict']
dump('OUT-57_RISK_REGISTER.csv',
     ['risco_id','unidade','framework','evento','causa_evidencia','documento_ids',
      'impacto','urgencia','controle','status_evidencia'], ri)

# OUT-58 gap register
ga=[dict(lacuna_id='GA-'+rid(r['framework'],r['dimension'],r['entity']), origem='strategic_analysis',
         unidade=r['entity'], alvo=f"{r['framework']}/{r['dimension']}", descricao=r['claim'],
         pesquisa_necessaria=r['recommendation'], prioridade=r['urgency'])
    for r in insights if r['status']=='gap']
ga+=[dict(lacuna_id='GA-'+rid(f['field_id']), origem='formulario', unidade=f.get('eco_unit',''),
          alvo=f"{f['field_id']} {f['title']}", descricao=f.get('lacuna',''),
          pesquisa_necessaria=f.get('proxima_acao',''), prioridade='')
     for aid,an,f in campos if f['status'] in ('lacuna','parcial') and f.get('lacuna')]
dump('OUT-58_GAP_REGISTER.csv',
     ['lacuna_id','origem','unidade','alvo','descricao','pesquisa_necessaria','prioridade'], ga)

# OUT-59 source register: dedup por documento, com relacoes
reg={r['documento_id']:r for r in csv.DictReader(
        open('/home/user/Docs/60-dados/40-canonical/REGISTRO_DOCUMENTAL_MECE_V1.csv',encoding='utf-8-sig'))}
usos={}
for e in ev: usos.setdefault(e['documento_id'],[]).append(e['evidencia_id'])
src=[]
for d,ids in sorted(usos.items()):
    m=reg.get(d,{})
    src.append(dict(documento_id=d, classificacao_id=m.get('classificacao_id',''),
        nome_arquivo=m.get('nome_arquivo',''), caminho_relativo=m.get('caminho_relativo',''),
        sha256=m.get('sha256',''), tipo_documental=m.get('tipo_documental',''),
        vezes_citado=len(ids), evidencia_ids=';'.join(ids[:20])))
dump('OUT-59_SOURCE_REGISTER.csv',
     ['documento_id','classificacao_id','nome_arquivo','caminho_relativo','sha256',
      'tipo_documental','vezes_citado','evidencia_ids'], src)

print(f'\ninsights processados: {len(insights)} | documentos-fonte citados: {len(usos)}/214')
