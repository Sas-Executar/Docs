# ECOSSISTEMA 15-08 · Docs

Este repositório opera como camada documental, de handoff e de orquestração do ECOSSISTEMA 15-08.

Todo material deve ser classificado por Folder ID antes de ser registrado.

## Fluxo

1. Entrada sem classificação -> `00-dropzone/`.
2. Maestro lê o mapa e o `01-master-index/CENTRAL_CONTROL.csv`.
3. Maestro triangula contexto, domínios, plugins e skills.
4. Um único `canonical_home` é escolhido.
5. Relações cross-domain são links, não cópias.
6. O resultado recebe proveniência e resumo executivo de no máximo 300 palavras.

## Áreas

`00-dropzone` · `01-master-index` · `10-business` · `20-produtos` · `30-editorial-marketing` · `40-comercial-servicos` · `50-portfolio-carreira` · `60-dados` · `70-operacao-governanca` · `80-tecnologia-plataformas` · `90-assets-compartilhados` · `98-private-pointers` · `99-archive` · `500-saas-mvp`.

## Maestro

Canônico em `80-tecnologia-plataformas/05-gpt/02-agents/maestro/`.

Skills Anthropic em `80-tecnologia-plataformas/05-gpt/03-skills/anthropic-knowledge-work-plugins/`.

```bash
git clone --recurse-submodules https://github.com/Sas-Executar/Docs.git
cd Docs
bash 80-tecnologia-plataformas/05-gpt/02-agents/maestro/scripts/bootstrap.sh
```
