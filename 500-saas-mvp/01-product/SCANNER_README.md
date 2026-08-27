---
id: MVP-SCN-001
folder_id: FS-MVP-002
tipo: feature-spec-readme
status: ativo
classification: DECISÃO
canonical_home: 500-saas-mvp/01-product
feature: Scanner
aliases:
  - QR
  - Atalhos
  - Paper Scanner
---

# Scanner · QR · Atalhos

## 1. Definição

O **Scanner** é a superfície físico-digital do EXECUTAR para identificar contexto, recuperar o estado atual de um objeto de execução e permitir ações operacionais sem obrigar o usuário a navegar pelo aplicativo.

Sua função não é apenas ler QR Code. O Scanner conecta papel, documentos, evidências, atalhos e objetos digitais ao **mesmo estado compartilhado de execução** usado pelo app, agentes de IA, canais de comunicação e demais superfícies do sistema.

> Do papel para a ação. Do contexto para o próximo passo.

Posicionamento:

> Menos navegação entre sistemas. Mais acesso direto ao que precisa ser executado.

## 2. Problema que resolve

O usuário não deveria precisar lembrar onde uma tarefa está, abrir múltiplos sistemas, reconstruir contexto ou navegar por várias telas apenas para registrar uma mudança simples.

O Scanner reduz essa fricção ao transformar um elemento físico ou digital em um **ponto de entrada contextual**.

Exemplos:

- escanear um QR em uma folha de projeto e abrir diretamente o contexto correto;
- concluir uma tarefa a partir do papel;
- registrar um bloqueio sem navegar pelo projeto inteiro;
- anexar uma foto como evidência;
- consultar detalhes de uma entrega;
- reagendar ou replanejar uma atividade;
- abrir um atalho contextual;
- usar o papel/Mapa-OS como superfície operacional autônoma, mantendo sincronização com o estado compartilhado.

## 3. Princípio central: superfície, não sistema paralelo

O Scanner **não possui um estado de projeto independente** e não é um segundo gerenciador de projetos.

Ele é uma superfície do mesmo sistema.

```text
                     EXECUTION STATE
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
         APP          PAPER + SCANNER      AGENT
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  COMMUNICATION CHANNELS
```

App, papel + Scanner, comunicação e agente de IA devem poder operar de forma independente como interface, porém todas as superfícies convergem para as mesmas regras de domínio, autoridade, eventos, evidências e projeções.

**Invariante:** uma ação concluída pelo Scanner deve produzir o mesmo estado final que a ação equivalente executada pelo app ou por outro canal autorizado.

## 4. O que o Scanner reconhece

Conforme o binding disponível, uma entrada pode resolver:

- workspace;
- projeto;
- entregável;
- período/ciclo;
- rotina;
- workflow;
- tarefa/ação;
- documento;
- evidência;
- interação;
- atalho;
- comando contextual.

O Scanner não deve exigir que o usuário reconstrua manualmente um contexto que já está associado ao objeto escaneado.

## 5. Formas de entrada

### QR Code

Mecanismo principal de binding físico-digital. O QR identifica ou resolve um objeto/contexto e conduz o Scanner ao **estado atual** desse objeto.

### Documento / folha física

Mapa-OS, folha de execução, relatório, cartão ou outro artefato pode conter QR e elementos de identificação que recuperam seu contexto operacional.

### Captura por câmera

A câmera pode:

- ler QR;
- capturar evidência visual;
- anexar documento/imagem;
- registrar artefato relacionado ao objeto atual.

### Atalho

Um binding pode resolver diretamente uma ação ou destino configurado. O atalho nunca cria uma regra de domínio paralela; ele dispara uma capacidade já existente e autorizada.

## 6. Fluxo principal

```text
SCAN / CAPTURE
      │
      ▼
RESOLVE BINDING
      │
      ▼
IDENTIFY OBJECT + CONTEXT
      │
      ▼
FETCH CURRENT STATE
      │
      ▼
CHECK AUTHORITY
      │
      ▼
SHOW CONTEXTUAL ACTIONS
      │
      ▼
USER CHOOSES ACTION
      │
      ▼
EMIT COMMAND
      │
      ▼
DOMAIN VALIDATION
      │
      ├── rejected → explain / preserve state
      │
      ▼
STATE TRANSITION
      │
      ▼
EVIDENCE / AUDIT / PROJECTION
      │
      ▼
CONFIRM RESULT
```

## 7. Interface depois do scan

Depois de resolver o contexto, o Scanner não deve abrir um dashboard genérico. Deve apresentar o objeto identificado e as ações relevantes ao estado atual.

Controles prioritários:

- **COMPLETE** — concluir quando permitido;
- **RESCHEDULE** — reagendar;
- **BLOCK** — registrar bloqueio;
- **EVIDENCE** — anexar/consultar evidência;
- **DETAILS** — consultar contexto necessário.

Ações visíveis variam conforme:

- tipo do objeto;
- estado atual;
- dependências;
- autoridade do usuário/canal;
- regras do workflow;
- Definition of Done;
- ações válidas naquele momento.

## 8. Capability set

O contrato funcional do Scanner deve suportar, quando autorizado:

| Operação | Função |
|---|---|
| `CREATE` | criar objeto permitido a partir do contexto atual |
| `VIEW` | consultar estado e detalhes |
| `UPDATE` | atualizar propriedades autorizadas |
| `COMPLETE` | solicitar/concluir trabalho conforme regra de conclusão |
| `DEFER` | adiar sem apagar o trabalho |
| `REPLAN` | alterar rota/plano conforme regras do domínio |
| `BLOCK` | registrar bloqueio e motivo |
| `ATTACH` | anexar arquivo, foto ou evidência |
| `COMMENT` | registrar comentário/contexto |
| `DELEGATE` | delegar quando permitido |
| `CANCEL` | cancelar quando o tipo/estado permitir |

Nem toda operação aparece em todo scan. As ações válidas são derivadas do contexto atual.

## 9. Emit: como o Scanner altera o sistema

O Scanner não deve editar projeções, relatórios ou documentos de apresentação diretamente.

Toda ação mutável é traduzida para um **comando observável** e emitida para o mesmo domínio usado pelas outras superfícies.

Exemplo conceitual:

```json
{
  "command": "COMPLETE",
  "object_id": "task-123",
  "workspace_id": "workspace-01",
  "source": "scanner",
  "binding_id": "qr-binding-456",
  "actor_id": "user-789",
  "evidence_refs": ["evidence-001"],
  "requested_at": "timestamp"
}
```

```text
Scanner
  → command
  → authority check
  → domain decision
  → event(s)
  → state update
  → projection refresh
```

## 10. Completion Authority

Conclusão não é sinônimo de tocar em “Feito”.

O Scanner deve respeitar **Completion Authority** antes de produzir uma transição de conclusão.

A decisão pode depender de:

- identidade do ator;
- tenant/workspace;
- tipo do objeto;
- estado anterior;
- Definition of Done;
- evidências obrigatórias;
- dependências;
- regra de aprovação;
- autoridade atribuída ao canal;
- política do workflow.

O modelo aceito possui **níveis de autoridade 0–4**. A existência desses cinco níveis é parte do contrato. A matriz semântica exata de cada nível deve ser recuperada/confirmada nos contratos-fonte antes de congelar a Functional Spec; este README não inventa essa matriz.

**Invariante:** o Scanner jamais pode transformar uma solicitação de conclusão em conclusão efetiva quando a política exigir evidência, validação ou aprovação adicional.

## 11. Evidência

Evidência é capacidade de primeira classe.

O Scanner pode capturar:

- foto;
- documento;
- arquivo;
- registro visual;
- comentário contextual;
- artefato produzido;
- comprovação associada a uma entrega/tarefa.

```text
CAPTURE
   ↓
IDENTIFY CONTEXT
   ↓
CREATE EVIDENCE RECORD
   ↓
ATTACH TO OBJECT
   ↓
VALIDATE REQUIREMENTS / DoD
   ↓
PERSIST + AUDIT
```

Evidência não deve existir apenas como mídia solta. Deve possuir vínculo estável com o objeto operacional correspondente.

## 12. QR como binding, não como Source of Truth

O QR funciona como **identificador/binding de entrada**.

Estado mutável — progresso, responsável, bloqueio, conclusão etc. — deve ser recuperado do sistema canônico depois que o binding é resolvido.

Isso impede que uma folha impressa antiga se transforme em fonte de verdade concorrente.

Consequências:

- o QR pode permanecer fisicamente estável;
- a leitura após o scan reflete o estado atual;
- uma impressão antiga continua apontando para o objeto correto, sujeita às regras de validade/revogação do binding.

## 13. Atalhos

Atalhos podem resolver:

- abrir o objeto atual;
- iniciar copiloto contextual;
- registrar entrada/saída de uma rotina;
- concluir uma ação elegível;
- abrir um destino configurado;
- executar uma ação previamente habilitada.

Atalhos obedecem autoridade e nunca podem contornar política do domínio.

## 14. Relação com Mapa-OS, Prisma e papel

O Scanner é o mecanismo que torna o papel uma **superfície conectada**.

O papel pode apresentar estado, estrutura, rotina, roadmap ou notas; o Scanner recupera o objeto digital e executa ações sem exigir que o usuário abandone a superfície física para navegar pelo app.

> O papel não é uma exportação morta do app. É uma superfície operacional que inicia interações com o mesmo sistema de execução.

A geometria física pode variar sem alterar o binding para o objeto/estado canônico.

## 15. Independência entre superfícies

Superfícies principais:

- app;
- papel + Scanner;
- comunicação;
- agente de IA.

Autonomia de superfície **não significa autonomia de estado**.

Todas operam sobre os mesmos:

- objetos;
- contratos;
- authority checks;
- transições;
- ledger/evidências;
- lógica de progresso;
- projeções derivadas.

## 16. Integração com o núcleo EXECUTAR

### Core / Project Domain

Estados, transições, dependências, progresso e regras do objeto de execução.

### Authority Registry

Resolve quem/canal pode executar qual ação sobre workspace/projeto/objeto.

### Evidence

Registra, persiste e relaciona evidências.

### QR / Binding Registry

Relaciona identificadores físicos/digitais a objetos canônicos.

### Interpreter / Orchestrator

Quando necessário, transforma intenção contextual em comando estruturado.

### MCP / Tools

Expõe capacidades do domínio a agentes e canais sem duplicar regra de negócio.

### Projection Service

Atualiza views e superfícies de leitura depois das mudanças do domínio.

## 17. Regra de autoridade de dados

O Scanner é origem de **comandos e evidências**, não autoridade final de todos os dados.

```text
INPUT / SCAN
    ↓
COMMAND
    ↓
DOMAIN AUTHORITY
    ↓
EVENT / STATE
    ↓
PROJECTIONS
```

Painel, folha impressa, relatório ou preview são projeções. Não escrevem estado de volta sem passar pelo contrato de comando/autoridade.

## 18. Auditoria

Toda ação relevante originada pelo Scanner deve permitir responder, quando aplicável:

- **WHAT** — o que foi solicitado/alterado;
- **WHEN** — quando;
- **WHO** — ator;
- **WHERE** — superfície/binding/origem;
- **WHY** — motivo informado ou regra aplicada;
- resultado;
- evidência associada;
- estado anterior/posterior;
- erro/rejeição.

Registrar entrada, decisão observável, ação, resultado e evidência. Não é requisito armazenar raciocínio privado de agentes.

## 19. Estados da interface

- **Ready** — câmera pronta.
- **Resolving** — binding resolvido e contexto sendo recuperado.
- **Resolved** — objeto encontrado; estado e ações válidas disponíveis.
- **Acting** — comando enviado.
- **Success** — mudança confirmada pelo domínio.
- **Rejected** — ação inválida por estado, dependência, autoridade, DoD ou política.
- **Invalid binding** — identificador inexistente, expirado, revogado ou incompatível.
- **Conflict** — estado atual diverge do materializado; atualizar e não sobrescrever silenciosamente.
- **Connectivity failure** — não declarar sucesso sem confirmação de persistência.

## 20. Segurança e multi-tenant

P0:

- binding nunca concede autoridade por si só;
- QR não substitui autenticação/autorização;
- comando mutável resolve tenant/workspace;
- bindings podem ser revogados;
- um binding não pode expor dados de outro tenant;
- IDs visíveis não são tratados como segredo;
- conclusão, delegação, cancelamento e mudanças sensíveis exigem policy check.

## 21. User stories

### Executor

Como pessoa executando trabalho, quero escanear um artefato e chegar diretamente à ação relevante para não precisar reconstruir contexto ou navegar pelo sistema.

### Executor no papel

Como pessoa trabalhando em superfície física, quero concluir, reagendar, bloquear ou anexar evidência pelo Scanner para continuar operando sem abrir manualmente o app.

### Gestor

Como responsável por um projeto, quero que ações do Scanner respeitem as mesmas regras, dependências e critérios do app para manter o estado confiável.

### Auditor / sistema

Como sistema, quero registrar origem e resultado de cada ação para permitir rastreabilidade e reconstrução do estado.

### Agente

Como agente autorizado, quero operar as mesmas capacidades por contratos compartilhados para não existir implementação paralela específica do Scanner.

## 22. Requisitos P0

- [ ] Resolver QR/binding para objeto canônico.
- [ ] Recuperar estado atual depois do binding.
- [ ] Exibir ações contextuais válidas.
- [ ] Suportar `VIEW`, `COMPLETE`, `DEFER/RESCHEDULE`, `BLOCK`, `ATTACH/EVIDENCE` e `DETAILS` no escopo aplicável.
- [ ] Emitir comandos pelo domínio compartilhado.
- [ ] Aplicar autoridade antes de mutações.
- [ ] Aplicar Completion Authority para conclusão.
- [ ] Registrar evidência vinculada ao objeto.
- [ ] Registrar auditoria.
- [ ] Atualizar projeções após confirmação do domínio.
- [ ] Manter consistência cross-surface.
- [ ] Não permitir QR/papel como fonte de verdade concorrente.
- [ ] Tratar binding inválido, ação rejeitada e conflito de estado.
- [ ] Respeitar isolamento multi-tenant.

## 23. Requisitos P1

- atalhos personalizáveis por contexto;
- capture-first para evidência;
- preview antes de ações de maior impacto;
- recuperação rápida de contexto recente;
- experiências específicas por tipo de artefato físico;
- offline controlado com fila explícita de sincronização, se fizer parte da versão-alvo.

## 24. Não objetivos

O Scanner não deve:

- substituir o domínio de projetos/tarefas;
- manter estado operacional independente;
- transformar QR em autorização;
- duplicar regras de conclusão;
- criar segunda lógica de progresso;
- exigir navegação completa pelo app para ações simples;
- editar projeções como fonte canônica;
- declarar sucesso antes de confirmação do sistema.

## 25. Critérios de aceite críticos

### Scan de tarefa

**Dado** um QR válido ligado a uma tarefa, **quando** o usuário escaneia, **então** o Scanner mostra estado atual e somente ações válidas.

### Conclusão autorizada

**Dado** objeto elegível e autoridade suficiente, **quando** o usuário solicita `COMPLETE`, **então** o comando passa por Completion Authority, produz a transição prevista e o novo estado fica visível nas demais superfícies.

### Conclusão não autorizada

**Dado** objeto que exige evidência/aprovação adicional, **quando** o usuário solicita `COMPLETE`, **então** o Scanner não declara conclusão e informa o requisito pendente.

### Evidência

**Dado** objeto resolvido, **quando** o usuário captura evidência, **então** ela recebe vínculo estável, origem e auditoria e pode ser utilizada por validação/DoD.

### Artefato desatualizado

**Dado** um artefato físico antigo, **quando** ele é escaneado, **então** o Scanner recupera o estado atual em vez de assumir que o estado impresso permanece válido.

### Cross-surface

**Dado** uma ação confirmada pelo Scanner, **quando** o objeto é aberto em outra superfície, **então** o estado observado deve ser equivalente.

## 26. Dependências para produção

1. contratos canônicos do domínio;
2. identidade e tenant;
3. authority registry;
4. QR/binding registry;
5. evidence store/ledger;
6. Completion Authority;
7. event/state persistence;
8. projections;
9. observabilidade/auditoria;
10. testes de equivalência cross-surface.

## 27. Migração e legado

Existiram ativos maduros específicos do Scanner em repositórios-fonte anteriores. O destino operacional atual é o repositório canônico do SaaS; portanto, a estratégia é **portar contratos e algoritmos úteis, adaptar infraestrutura e evitar reimplementar regras maduras**.

Capacidades a preservar quando encontradas nos fontes:

- QR e bindings;
- ingest/capture;
- evidence;
- emit/command flow;
- Completion Authority;
- FractalPlan relacionado ao contexto de execução;
- MCP/tools;
- runtime/projections;
- contratos de documentos e evidências.

Infraestrutura legada não deve substituir a stack canônica apenas por já existir no código-fonte.

## 28. Lacunas abertas

### PENDENTE · matriz Completion Authority 0–4

A existência dos níveis está consolidada, mas a semântica exata de cada nível precisa ser recuperada dos contratos-fonte.

### PENDENTE · schema definitivo do QR binding

Este README congela comportamento de produto, não o payload técnico final.

### PENDENTE · offline da versão SaaS

A arquitetura deve evitar perda silenciosa; o escopo exato de offline/sync depende da versão de lançamento.

### PENDENTE · matriz de ações por tipo de objeto

`CREATE/VIEW/UPDATE/COMPLETE/DEFER/REPLAN/BLOCK/ATTACH/COMMENT/DELEGATE/CANCEL` formam o capability set; a disponibilidade por objeto/estado deve ser fechada na Functional Spec.

## 29. Proveniência e status

### CONFIRMADO em documentação de posicionamento

Scanner / QR / Atalhos é uma das features de destaque do EXECUTAR e funciona como ponte de acesso/captura entre superfícies físicas e digitais.

### DECISÕES CANÔNICAS consolidadas posteriormente

- papel + Scanner pode operar projetos/tarefas sem exigir navegação manual pelo app;
- app, papel + Scanner, comunicação e agente operam sobre estado compartilhado;
- ações do Scanner respeitam autoridade e contratos de domínio;
- Scanner reconhece contexto e apresenta controles operacionais contextuais;
- evidência e conclusão são capacidades de primeira classe;
- mudanças são emitidas para o domínio, não escritas diretamente em projeções.

### Referências

- `Evidencias-24-25.08.md`
- `Sas-06.md`
- materiais de desenvolvimento/migração do EXECUTAR
- contratos históricos do Scanner a recuperar no handoff de engenharia

## 30. Resumo

O Scanner é a ponte operacional entre mundo físico e estado digital do EXECUTAR. Um scan identifica o contexto, recupera o estado atual, calcula ações permitidas, aplica autoridade e transforma a escolha do usuário em comando do domínio. O pipeline registra eventos/evidências e atualiza as projeções usadas por app, papel, agentes e canais.

O diferencial é permitir que a pessoa continue executando a partir do objeto que já está diante dela — especialmente papel, QR ou documento — sem transformar essa superfície em um sistema isolado. O Scanner reduz navegação, preserva contexto e mantém consistência de estado.
