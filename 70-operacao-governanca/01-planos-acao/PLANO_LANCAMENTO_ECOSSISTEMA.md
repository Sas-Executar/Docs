---
id: GOV-PLAN-001
folder_id: FS-OPS-002
tipo: plano-de-acao
status: ativo
projeto: ECOSSISTEMA_15-08_FILESYSTEM
schema: ECOSYSTEM_MASTER_YAML_CARDS_V1
data_inicio: 2026-08-30
---

# Plano de Lançamento do Ecossistema

## Fontes recebidas

- `ECOSYSTEM_MASTER_YAML_CARDS_V1` — modelo de 75 cards / 12 fases para cobertura completa de lançamento, operação, evolução e retirada do ecossistema (negócio, app, editorial, produtos digitais/físicos, serviços). Registrado em [[../../01-master-index/01-schemas/ECOSYSTEM_MASTER_YAML_CARDS_V1.yaml]].
- `EXECUTAR_projetosaasentrypoint_EXPANDIDO` — formulário de intake de 94 campos / 17 domínios para um projeto SaaS específico dentro do ecossistema. Registrado em [[../../01-master-index/01-schemas/EXECUTAR_projetosaasentrypoint_EXPANDIDO.schema.json]].

## Estrutura de roteamento

- Cada um dos 75 cards está mapeado a um `canonical_folder_id`/`canonical_path` existente em `CENTRAL_CONTROL.csv` — ver [[../../01-master-index/02-taxonomies/ECOSYSTEM_CARDS_REGISTER.csv]]. Nenhum Folder ID novo foi necessário: os 12 grupos do modelo já correspondem aos domínios `10`–`90` já existentes no ecossistema.
- Cada um dos 17 domínios do formulário SaaS está mapeado a uma subpasta de `500-saas-mvp` (handoff mínimo) ou ao domínio técnico/editorial correspondente — ver [[../../01-master-index/02-taxonomies/SAAS_ENTRYPOINT_DOMAIN_MAP.csv]].
- Regra: um card = um `canonical_home`. Relações cross-domain (ex.: um card de `70-operacao-governanca` que referencia um card de `20-produtos`) são links, nunca duplicação.

## Gaps identificados (precisam de confirmação)

1. **Produto-alvo do formulário SaaS**: o schema `EXECUTAR_projetosaasentrypoint_EXPANDIDO` descreve um projeto SaaS específico. Assumi como destino padrão `500-saas-mvp` (handoff mínimo já existente), mas os campos técnicos (domínios 3–4) também podem pertencer ao SOT completo em `20-produtos/10-executar-app`. **Preciso que você confirme**: este formulário é sobre o produto que já existe em `500-saas-mvp` (Scanner) ou sobre um novo produto/feature?
2. **Subpastas ainda não criadas**: `10-business` não tem uma subpasta dedicada a "mercado" — cards `MKT-020` a `MKT-024` foram roteados para a raiz de `FS-BUS-001` até decidirmos se vale criar `10-business/09-mercado` com Folder ID próprio.
3. **Domínios 15–17 do formulário** (skills, plataformas, prompts) não têm equivalente direto nos 75 cards — tratados como metadados operacionais, roteados para `80-tecnologia-plataformas` e `98-private-pointers` (credenciais).

## Ordem de execução (dependência declarada no próprio schema)

```
P00_GOVERNANCE → P01_STRATEGY → P02_MARKET_CUSTOMER → P03_BUSINESS_PORTFOLIO →
P04_OFFER_DEFINITION → P05_REQUIREMENTS → P06_ARCHITECTURE_DESIGN → P07_DELIVERY →
P08_VERIFICATION_VALIDATION → P09_GTM_LAUNCH → P10_OPERATIONS → P11_EVOLUTION_RETIREMENT
```

Cada fase só pode ser aprovada quando os `depends_on` de todos os seus cards já existirem em maturidade suficiente (`ECOSYSTEM_CARDS_REGISTER.csv`, coluna `depends_on`).

## Status por fase

| Fase | Cards | Obrigatórios | Status |
|---|---|---|---|
| P00 · Governança | 5 | 5 | **pendente — próximo grupo a enviar** |
| P01 · Estratégia | 6 | 6 | bloqueado (depende de P00) |
| P02 · Mercado e cliente | 5 | 5 | bloqueado |
| P03 · Modelo de negócio e portfólio | 6 | 6 | bloqueado |
| P04 · Definição das ofertas | 6 | 1 obrigatório + 5 condicionais | bloqueado |
| P05 · Requisitos | 10 | 7 obrigatórios + 3 condicionais | bloqueado |
| P06 · Arquitetura e design | 9 | 6 obrigatórios + 3 condicionais | bloqueado |
| P07 · Entrega e construção | 7 | 6 obrigatórios + 1 condicional | bloqueado |
| P08 · Verificação e validação | 5 | 5 | bloqueado |
| P09 · GTM e lançamento | 5 | 4 obrigatórios + 1 condicional | bloqueado |
| P10 · Operação | 7 | 6 obrigatórios + 1 condicional | bloqueado |
| P11 · Evolução e retirada | 4 | 3 obrigatórios + 1 condicional | bloqueado |

## Próximo passo

Enviar o **Grupo P00 · Governança** (5 documentos/decisões, sem dependências — raiz da cadeia):

| Card | Artefato | O que preciso de você |
|---|---|---|
| `GOV-001` | Ecosystem Charter | visão, propósito, escopo, componentes do ecossistema, fora de escopo, definição de sucesso, sponsor |
| `GOV-002` | Document and Configuration Governance | confirma se a governança documental já descrita no repo (`CENTRAL_CONTROL.csv`, Folder IDs, `01-master-index`) é suficiente ou precisa de regras extras |
| `GOV-003` | Stakeholder and Decision Rights Register | quem são os stakeholders, responsabilidades, autoridade decisória |
| `GOV-004` | Compliance and Legal Obligations Register | jurisdição, obrigações legais/contratuais conhecidas |
| `GOV-005` | Risk Assumption Issue and Constraint Register | riscos, premissas, problemas e restrições atuais do lançamento |

Pode mandar em texto corrido, um card de cada vez ou tudo junto — o Maestro classifica, resolve o `canonical_home` (`70-operacao-governanca`) e devolve o resumo executivo por rodada. Assim que P00 estiver completo, libero o Grupo P01 (Estratégia).
