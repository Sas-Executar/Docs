# Workbook PMBOK 8 · Ecossistema EXECUTAR

Versão V1 · gerado em 2026-08-31 · data de corte das fontes 2026-08-31

## O que é

Entrega consolidada do preenchimento estratégico, gerencial e mercadológico do ecossistema
EXECUTAR, produzida sobre a base documental C01–C18 (214 arquivos).

## Integridade da base

Os 214 arquivos do pacote `DOCUMENTOS.zip` foram conferidos contra o registro documental MECE:
**214/214 casaram por SHA-256**. São 202 hashes únicos — os 12 exemplares restantes são as
duplicatas exatas dos 9 grupos previstos. Cadeia rastreável completa:
`REG-nnnn → DOC-Cxx-nnn → Cxx → Txx → caminho original → SHA-256`.

## Arquivos desta entrega

| Arquivo | Conteúdo |
|---|---|
| `WORKBOOK_PMBOK8_ECOSSISTEMA_EXECUTAR.xlsx` | Workbook com 10 abas (OUT-63) |
| `WORKBOOK_ECOSSISTEMA_EXECUTAR.json` | Mesmo conteúdo, hierárquico (OUT-61) |
| `WORKBOOK_ECOSSISTEMA_EXECUTAR.yaml` | Mesmo conteúdo, para agentes (OUT-62) |
| `WORKBOOK_FORMULARIO.csv` | Os 122 campos do formulário, normalizados (OUT-60) |

Os quatro formatos carregam os mesmos IDs, status e conteúdo (OUT-65).

## Números

- **279 insights estratégicos** — 189 fact · 44 gap · 25 conflict · 19 inference · 2 hypothesis
- **122 campos** do formulário — 20 preenchidos · 14 parciais · 10 lacunas · 1 conflito · 77 pendentes
- **680 pares** afirmação ↔ documento_id
- **86 de 214 documentos** efetivamente citados como evidência

## Regra epistemológica

Nada foi inventado. Toda afirmação aponta para um `documento_id` real e transcreve a evidência.
Ausência de dado virou lacuna descrita, nunca estimativa. Conflitos entre fontes ficam
registrados com as duas versões — nenhum foi arbitrado em silêncio.

`status`: `fact` evidência explícita · `inference` derivação a partir de evidência citada ·
`hypothesis` sem evidência · `conflict` fontes incompatíveis · `gap` pergunta sem dado.

## Alertas materiais

- TAM/SAM/SOM sem base defensável: números vêm de transcrição de imagem, base amostral não informada, bibliografia ausente; há um segundo valor de SAM no mesmo dashboard.
- Nenhuma das 8 unidades tem pesquisa primária com clientes reais.
- Timer 45: custo de fornecedor R$39 contra concorrente a R$28,46 no AliExpress.
- Economia unitária incompleta: sem custo de produção e sem CAC em nenhuma linha; landed cost com campos a preencher; sem fornecedor, MOQ ou lead time.
- Conflito entre a sequência editorial (categoria antes do produto) e o GTM de 07/09 (tudo no dia um).
- Fronteira Livro × Infoprodutos: aninhamento na árvore e homonímia entre e-books comerciais e livro autoral.

## Como continuar

Faltam os dias 3 a 6 do formulário (áreas 11 · 12–17 · 5–7 · 3–4), somando 77 campos.

Reprodutibilidade: `80-tecnologia-plataformas/05-gpt/02-agents/maestro/scripts/gen_registros_auxiliares.py`
regenera os registros OUT-54..59 a partir dos insights e do formulário. IDs derivam de hash do
conteúdo, estáveis entre execuções.
