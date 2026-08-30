# Relations

Cada objeto tem um único `canonical_home`; relações cross-domain são links, não cópias.

## SaaS MVP

`FS-MVP-001` consolida o handoff de produção, mas não substitui:

- `FS-EXE-001` para o produto EXECUTAR App;
- `FS-TEC-001` para tecnologia;
- `FS-AST-001` para assets compartilhados;
- `FS-OPS-001` para governança operacional.

## Maestro

- agente: `FS-TEC-029` · `80-tecnologia-plataformas/05-gpt/02-agents/maestro`
- skills upstream: `FS-TEC-036` · `80-tecnologia-plataformas/05-gpt/03-skills/anthropic-knowledge-work-plugins`

## Ecosystem Master Cards

`ECOSYSTEM_MASTER_YAML_CARDS_V1` (`FS-IDX-002`) não cria domínios novos; distribui 75 cards sobre os domínios já existentes:

- Governança (`GOV-*`), Entrega (`DEL-*`), Operação (`OPS-*`), Evolução (`EVO-*`) → `FS-OPS-001` · `70-operacao-governanca`
- Estratégia e Mercado (`STR-*`, `MKT-*`) → `FS-BUS-001` · `10-business`
- Modelo de negócio e portfólio (`BUS-*`) → `FS-BUS-003` · `10-business/02-modelo-negocio`
- Ofertas e requisitos de app (`OFF-040`, `REQ-*`) → `FS-EXE-001` · `20-produtos/10-executar-app`
- Ofertas físicas/serviços/editorial (`OFF-042/043/044/045`) → `FS-PHY-001`, `FS-COM-001`, `FS-EDT-001`
- Arquitetura (`ARC-*`) → `FS-TEC-001` · `80-tecnologia-plataformas`
- Verificação e validação (`VAL-*`) → `FS-EXE-001/11-qa` ou `FS-TEC-001`
- GTM (`GTM-*`) → `FS-EDT-001` ou `FS-COM-001`

Registro completo, com `depends_on` e status por card: `01-master-index/02-taxonomies/ECOSYSTEM_CARDS_REGISTER.csv`.
Plano de execução por fase: `70-operacao-governanca/01-planos-acao/PLANO_LANCAMENTO_ECOSSISTEMA.md`.

## SaaS Entrypoint

`EXECUTAR_projetosaasentrypoint_EXPANDIDO` (`FS-IDX-002`) é o formulário de intake de um projeto SaaS específico. Destino padrão assumido: `FS-MVP-001` · `500-saas-mvp` (handoff mínimo já existente), com domínios técnicos podendo também alimentar `FS-EXE-001` · `20-produtos/10-executar-app`. **Confirmação pendente do usuário** — ver gap #1 em `PLANO_LANCAMENTO_ECOSSISTEMA.md`. Mapa de domínio completo: `01-master-index/02-taxonomies/SAAS_ENTRYPOINT_DOMAIN_MAP.csv`.
