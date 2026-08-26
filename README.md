# EXECUTAR Docs · Maestro

Repositório documental, de handoff e de orquestração de conhecimento do EXECUTAR.

## Maestro

Antes de criar, mover, editar, consolidar ou submeter qualquer material, o Maestro deve: entender o contexto; classificar domínios; descobrir plugins e skills; compor o workflow; executar; registrar proveniência; e devolver um resumo executivo de no máximo 300 palavras.

Leia primeiro: `AGENT_MAESTRO.md`, `.maestro/ROUTING.md`, `.maestro/POLICY.yaml` e `.maestro/PROVENANCE.md`.

## Estrutura

```text
Docs/
├── README.md
├── AGENT_MAESTRO.md
├── .maestro/
├── 01_PRODUCT/
├── 02_EXPERIENCE/
├── 03_ENGINEERING/
├── 04_REFERENCE/
├── orchestrator/
├── proto/
├── sql/
├── scripts/
├── vendor/
└── runtime/
```

## Knowledge Work Plugins

O upstream oficial da Anthropic está montado como submódulo em `vendor/anthropic-knowledge-work-plugins/`. O Maestro consulta as skills reais do upstream; não usa uma tabela manual fixa.

```bash
git clone --recurse-submodules https://github.com/Sas-Executar/Docs.git
cd Docs
bash scripts/bootstrap.sh
```

## Portabilidade

- Markdown/YAML: políticas e workflows.
- JSON: envelopes e índice de skills.
- SQL: registry, auditoria e proveniência.
- Protocol Buffers: contrato de transporte entre runtimes.
- Python stdlib: roteamento local e independente de fornecedor.

O mesmo diretório pode ser usado por Claude, ChatGPT/OpenAI, agentes locais ou outros runtimes.
