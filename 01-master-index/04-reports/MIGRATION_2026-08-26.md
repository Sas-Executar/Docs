# Migração · 2026-08-26

## Fontes recebidas

- `ECOSSISTEMA_15-08_OBSIDIAN.zip` — referência de MOCs, IDs de objetos e fluxo do vault.
- `Mapa .zip` / `Index.pdf` — referência da árvore física e Folder IDs.

## Alterações

- materializada a árvore do ECOSSISTEMA 15-08 no repositório `Sas-Executar/Docs`;
- preservados os IDs de MOC originais e separados dos Folder IDs;
- criada a extensão `FS-MVP-001` para `500-saas-mvp`;
- movido o Maestro para `FS-TEC-029` em `80-tecnologia-plataformas/05-gpt/02-agents/maestro`;
- movidas as Knowledge Work Skills Anthropic para `FS-TEC-036` em `80-tecnologia-plataformas/05-gpt/03-skills/anthropic-knowledge-work-plugins`;
- estabelecido `CENTRAL_CONTROL.csv` como registry de Folder IDs.

## Regra

Novo diretório canônico requer Folder ID; novo objeto persistente deve ter object ID quando aplicável. Um objeto possui um único `canonical_home` e relações cross-domain são links.
