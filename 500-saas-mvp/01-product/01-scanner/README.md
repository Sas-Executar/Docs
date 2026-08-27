---
id: MVP-SCN-001
folder_id: FS-MVP-006
tipo: feature-spec-readme
status: ativo
classification: DECISÃO
canonical_home: 500-saas-mvp/01-product/01-scanner
feature: Scanner
aliases:
  - QR
  - Atalhos
  - Paper Scanner
---

# Scanner · QR · Atalhos

## 1. Definição

O **Scanner** é a superfície físico-digital do EXECUTAR para identificar contexto, recuperar o estado atual de um objeto de execução e permitir ações operacionais sem obrigar o usuário a navegar pelo aplicativo.

Sua função não é apenas “ler QR Code”. O Scanner conecta papel, documentos, evidências, atalhos e objetos digitais ao **mesmo estado compartilhado de execução** usado pelo app, agentes de IA, canais de comunicação e demais superfícies do sistema.

Em uma frase:

> Do papel para a ação. Do contexto para o próximo passo.

Frase de posicionamento:

> Menos navegação entre sistemas. Mais acesso direto ao que precisa ser executado.

## 2. Problema que resolve

O EXECUTAR parte da premissa de que o usuário não deveria precisar lembrar onde uma tarefa está, abrir múltiplos sistemas, reconstruir contexto ou navegar por várias telas apenas para registrar uma mudança simples.

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

O Scanner **não possui um banco de estado próprio** e não é um segundo gerenciador de projetos.

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

App, papel + Scanner, comunicação e agente de IA devem ser capazes de operar de forma independente do ponto de vista da interface, porém todas as superfícies convergem para as mesmas regras de domínio, autoridade, eventos, evidências e projeções.

Consequência obrigatória:

> Uma ação concluída pelo Scanner deve produzir o mesmo estado final que a ação equivalente executada pelo app ou por outro canal autorizado.

## 4. O que o Scanner reconhece

Ao resolver uma entrada, o Scanner deve ser capaz de associá-la, conforme o binding disponível, a um ou mais contextos do EXECUTAR:

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

O Scanner não deve obrigar o usuário a reconstruir manualmente o contexto que já está associado ao objeto escaneado.

## 5. Formas de entrada

### 5.1 QR Code

Principal mecanismo de binding físico-digital.

O QR identifica ou resolve um objeto/contexto e conduz o Scanner à versão **atual** daquele estado.

### 5.2 Documento / folha física

Uma folha de execução, Mapa-OS, relatório, cartão ou artefato impresso pode conter QR e outros elementos de identificação para recuperar seu contexto operacional.

### 5.3 Captura por câmera

A câmera pode ser usada para:

- ler QR;
- capturar evidência visual;
- anexar documento/imagem;
- registrar artefato relacionado ao objeto atual.

### 5.4 Atalho

Um binding pode resolver diretamente uma ação ou destino configurado, reduzindo etapas de navegação.

Atalhos não devem criar lógica de domínio paralela: devem disparar capacidades já existentes no sistema.

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

## 7. Experiência imediata após o scan

Depois que o contexto é resolvido, a interface não deve abrir um dashboard genérico.

Ela deve apresentar o objeto identificado e as ações relevantes para o estado atual.

Controles contextuais prioritários:

- **COMPLETE** — concluir quando permitido;
- **RESCHEDULE** — reagendar;
- **BLOCK** — registrar bloqueio;
- **EVIDENCE** — anexar/consultar evidência;
- **DETAILS** — consultar o contexto necessário.

Os controles visíveis variam conforme:

- tipo do objeto;
- estado atual;
- dependências;
- autoridade do usuário/canal;
- regras do workflow;
- Definition of Done;
- ações válidas naquele momento.

## 8. Capacidades operacionais

O contrato funcional do Scanner deve suportar as seguintes operações quando autorizadas:

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

Nem toda operação aparece em todo scan. O sistema deve derivar as ações válidas do contexto atual.

## 9. Emit: como o Scanner altera o sistema

O Scanner não deve editar projeções ou documentos de apresentação diretamente.

Uma ação mutável deve ser traduzida para um **comando observável** e emitida para o mesmo domínio utilizado pelas outras superfícies.

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

Fluxo:

```text
Scanner
  → command
  → authority check
  → domain decision
  → event(s)
  → state update
  → projection refresh
```

Isso preserva consistência entre Scanner, app, agente e demais canais.

## 10. Completion Authority

Conclusão não é sinônimo de tocar em “Feito”.

O Scanner deve respeitar o contrato de **Completion Authority** antes de produzir uma transição de conclusão.

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

O modelo aceito possui **níveis de autoridade 0–4**. A existência desses cinco níveis é parte do contrato do Scanner; a matriz semântica exata de cada nível deve ser recuperada/confirmada nos contratos-fonte antes da implementação final. Este README não inventa a matriz.

### Invariante

O Scanner jamais pode transformar uma solicitação de conclusão em conclusão efetiva quando a política exigir evidência, validação ou aprovação adicional.

## 11. Evidência

Evidência é uma capacidade de primeira classe.

O Scanner pode funcionar como ponto de captura para:

- foto;
- documento;
- arquivo;
- registro visual;
- comentário contextual;
- artefato produzido;
- comprovação associada a uma entrega/tarefa.

Fluxo mínimo:

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

A evidência não deve existir apenas como mídia solta. Deve possuir vínculo estável com o objeto operacional correspondente.

## 12. QR como binding, não como fonte de verdade

O QR funciona como **identificador/binding de entrada**.

O estado mutável — por exemplo, progresso, responsável, bloqueio ou conclusão — deve ser recuperado do sistema canônico após a resolução do binding.

Isso evita que uma folha impressa antiga se transforme em uma fonte de verdade concorrente.

Consequência:

- o QR pode permanecer fisicamente estável;
- o conteúdo exibido após o scan reflete o estado atual;
- uma impressão antiga continua apontando para o objeto correto, sujeito às regras de validade do binding.

## 13. Atalhos

Atalhos reduzem navegação e podem ser associados a objetos físicos/digitais.

Um atalho pode resolver, por exemplo:

- abrir o objeto atual;
- iniciar copiloto contextual;
- registrar entrada/saída de uma rotina;
- concluir uma ação elegível;
- abrir um destino configurado;
- executar uma ação previamente habilitada.

A configuração de atalhos deve respeitar autoridade e não pode permitir que um binding físico contorne políticas do domínio.

## 14. Relação com Mapa-OS, Prisma e papel

O Scanner é o mecanismo que torna o papel uma **superfície conectada**.

O papel pode mostrar estado, estrutura, rotina, roadmap ou notas; o Scanner permite recuperar o objeto digital e executar ações sem exigir que o usuário abandone a superfície física para navegar pelo app.

Princípio de produto:

> O papel não é uma exportação morta do app. É uma superfície operacional que pode iniciar interações com o mesmo sistema de execução.

A geometria física do artefato pode variar, mas o binding deve continuar apontando para o mesmo objeto/estado canônico.

## 15. Independência entre superfícies

A decisão canônica é que as superfícies principais possam ser usadas de forma autônoma:

- app;
- papel + Scanner;
- comunicação;
- agente de IA.

Autonomia de superfície **não significa autonomia de estado**.

Todas operam sobre:

- mesmos objetos;
- mesmos contratos;
- mesma autoridade;
- mesmas transições;
- mesmo ledger/evidência;
- mesma lógica de progresso;
- mesmas projeções derivadas.

## 16. Integração com o núcleo EXECUTAR

O Scanner depende conceitualmente das seguintes capacidades do sistema:

### Core / Project Domain

Autoridade sobre estados, transições, dependências, progresso e regras do objeto de execução.

### Authority Registry

Resolve quem/canal pode executar qual ação sobre determinado workspace/projeto/objeto.

### Evidence

Registra e relaciona evidências.

### QR / Binding Registry

Relaciona identificadores físicos/digitais aos objetos canônicos.

### Interpreter / Orchestrator

Quando necessário, transforma uma intenção contextual em comando estruturado.

### MCP / Tools

Expõe capacidades do domínio a agentes e canais sem duplicar regra de negócio.

### Projection Service

Atualiza views e superfícies de leitura depois das mudanças no domínio.

## 17. Regra de Source of Truth

O Scanner é uma origem de **comandos e evidências**, não a autoridade final de todos os dados.

Regra geral:

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

Painel, folha impressa, relatório ou preview são projeções. Eles não devem escrever estado de volta sem passar pelo mesmo contrato de comando/autoridade.

## 18. Auditoria

Toda ação relevante originada pelo Scanner deve ser auditável.

O registro observável deve permitir responder, quando aplicável:

- **WHAT** — o que foi solicitado/alterado;
- **WHEN** — quando;
- **WHO** — quem/qual ator;
- **WHERE** — qual superfície/binding/origem;
- **WHY** — motivo informado ou regra aplicada;
- resultado;
- evidência associada;
- estado anterior/posterior;
- erro/rejeição quando houver.

Não armazenar raciocínio privado de agentes como requisito de auditoria. Registrar entrada, decisão observável, ação, resultado e evidência.

## 19. Estados de interface

O Scanner deve tratar explicitamente:

### Ready

Câmera pronta para leitura/captura.

### Resolving

Binding identificado e contexto sendo recuperado.

### Resolved

Objeto encontrado; estado e ações válidas disponíveis.

### Acting

Comando enviado e aguardando resultado.

### Success

Mudança confirmada pelo domínio.

### Rejected

Ação inválida por estado, dependência, autoridade, DoD ou política.

### Invalid binding

QR/identificador inexistente, expirado, revogado ou incompatível.

### Conflict

O estado mudou desde a materialização do artefato/scan; recuperar estado atual e impedir sobrescrita silenciosa.

### Connectivity failure

Não declarar sucesso sem confirmação de persistência. Capturas locais, quando suportadas por uma versão offline, devem permanecer claramente pendentes até sincronização confirmada.

## 20. Segurança e multi-tenant

P0:

- binding nunca concede autoridade por si só;
- QR não substitui autenticação/autorização;
- todo comando mutável deve carregar/resolver tenant/workspace;
- bindings devem poder ser revogados;
- uma identificação válida não pode expor dados de outro tenant;
- IDs apresentados ao cliente não devem ser tratados como segredo;
- conclusão, delegação, cancelamento e mudanças sensíveis exigem policy check.

## 21. User stories principais

### Executor

Como pessoa executando trabalho, quero escanear um artefato e chegar diretamente à ação relevante para não precisar reconstruir contexto ou navegar pelo sistema.

### Executor no papel

Como pessoa trabalhando principalmente em uma superfície física, quero concluir, reagendar, bloquear ou anexar evidência pelo Scanner para continuar operando sem abrir manualmente o app.

### Gestor

Como responsável por um projeto, quero que ações originadas no Scanner respeitem as mesmas regras, dependências e critérios do app para que o estado permaneça confiável.

### Auditor / sistema

Como sistema, quero registrar a origem e o resultado de cada ação para permitir rastreabilidade e reconstrução do estado.

### Agente

Como agente autorizado, quero operar as mesmas capacidades por contratos compartilhados para que não exista uma implementação paralela específica do Scanner.

## 22. Requisitos P0

- [ ] Resolver QR/binding para objeto canônico.
- [ ] Recuperar estado atual após resolver o binding.
- [ ] Exibir ações contextuais válidas.
- [ ] Suportar `VIEW`, `COMPLETE`, `DEFER/RESCHEDULE`, `BLOCK`, `ATTACH/EVIDENCE` e `DETAILS` no escopo aplicável.
- [ ] Emitir comandos pelo domínio compartilhado.
- [ ] Aplicar autoridade antes de mutações.
- [ ] Aplicar Completion Authority para conclusão.
- [ ] Registrar evidência vinculada ao objeto.
- [ ] Registrar auditoria da ação.
- [ ] Atualizar projeções após confirmação do domínio.
- [ ] Manter consistência cross-surface.
- [ ] Não permitir que QR/papel se torne fonte de verdade concorrente.
- [ ] Tratar binding inválido, ação rejeitada e conflito de estado.
- [ ] Respeitar isolamento multi-tenant.

## 23. Requisitos P1

- atalhos personalizáveis por contexto;
- capture-first para evidência;
- preview antes de ações de maior impacto;
- recuperação rápida de contexto recente;
- experiências específicas para diferentes tipos de artefato físico;
- suporte offline controlado com fila explícita de sincronização, se incluído na versão-alvo.

## 24. Não objetivos

O Scanner não deve:

- substituir o domínio de projetos/tarefas;
- manter estado operacional independente;
- transformar QR em mecanismo de autorização;
- duplicar regras de conclusão;
- criar uma segunda lógica de progresso;
- exigir navegação completa pelo app para ações simples;
- editar projeções como se fossem fonte canônica;
- declarar sucesso antes de confirmação do sistema.

## 25. Critérios de aceite críticos

### Scan de tarefa

**Dado** um QR válido ligado a uma tarefa,
**quando** o usuário escaneia,
**então** o Scanner mostra o estado atual e somente ações válidas para aquele contexto.

### Conclusão autorizada

**Dado** um objeto elegível e autoridade suficiente,
**quando** o usuário solicita `COMPLETE`,
**então** o comando passa por Completion Authority, produz a transição prevista e o novo estado fica visível nas demais superfícies.

### Conclusão não autorizada

**Dado** um objeto que exige evidência/aprovação adicional,
**quando** o usuário solicita `COMPLETE`,
**então** o Scanner não declara conclusão e informa o requisito pendente.

### Evidência

**Dado** um objeto resolvido,
**quando** o usuário captura uma evidência,
**então** a evidência recebe vínculo estável, origem e auditoria e pode ser usada pelas regras de validação/DoD.

### Estado desatualizado

**Dado** um artefato físico antigo,
**quando** ele é escaneado,
**então** o Scanner recupera o estado atual do objeto em vez de assumir que o estado impresso ainda é válido.

### Cross-surface

**Dado** uma ação confirmada pelo Scanner,
**quando** o mesmo objeto é aberto no app ou por outra superfície,
**então** o estado observado deve ser equivalente.

## 26. Dependências para produção

Antes de considerar o Scanner production-ready, a implementação precisa estar conectada a:

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

Existiram implementações e ativos maduros específicos do Scanner em repositórios-fonte anteriores. O destino operacional atual é o repositório canônico do SaaS; portanto, a estratégia é **portar contratos e algoritmos úteis, adaptar infraestrutura e evitar reimplementar regras maduras**.

Capacidades a preservar na migração quando encontradas nos fontes:

- QR e bindings;
- ingest/capture;
- evidence;
- emit/command flow;
- Completion Authority;
- FractalPlan relacionado ao contexto de execução;
- MCP/tools relacionados;
- runtime/projections;
- contratos de documentos e evidências.

Infraestrutura legada não deve substituir a stack canônica apenas por já existir no código-fonte.

## 28. Lacunas explicitamente abertas

### PENDENTE · matriz Completion Authority 0–4

A existência dos níveis 0–4 está consolidada, porém a semântica exata de cada nível precisa ser recuperada dos contratos-fonte antes de congelar a spec de engenharia.

### PENDENTE · schema definitivo do QR payload/binding

Este README define o comportamento, não congela o payload técnico final.

### PENDENTE · comportamento offline da versão SaaS

A arquitetura deve evitar perda silenciosa, mas o escopo exato de offline/sync depende da versão de lançamento.

### PENDENTE · matriz de ações por tipo de objeto

`CREATE/VIEW/UPDATE/COMPLETE/DEFER/REPLAN/BLOCK/ATTACH/COMMENT/DELEGATE/CANCEL` formam o capability set; a matriz de disponibilidade por objeto/estado deve ser fechada na Functional Spec.

## 29. Proveniência e status da especificação

### CONFIRMADO em documentação de posicionamento

Scanner / QR / Atalhos é uma das features de destaque do EXECUTAR e funciona como ponte de acesso/captura entre superfícies físicas e digitais.

### DECISÕES CANÔNICAS consolidadas posteriormente

- papel + Scanner pode operar projetos/tarefas sem exigir navegação manual pelo app;
- app, papel + Scanner, comunicação e agente operam sobre um estado compartilhado;
- ações do Scanner devem respeitar autoridade e contratos de domínio;
- Scanner reconhece contexto e apresenta controles operacionais contextuais;
- evidência e conclusão são capacidades de primeira classe;
- mudanças são emitidas para o domínio e não escritas diretamente em projeções.

### Referências documentais

- `Evidencias-24-25.08.md`
- `Sas-06.md`
- materiais de desenvolvimento/migração do EXECUTAR
- contratos históricos do Scanner a recuperar durante o handoff de engenharia

## 30. Resumo executivo

O Scanner é a ponte operacional entre o mundo físico e o estado digital do EXECUTAR. Um scan identifica o contexto, recupera o estado atual, calcula as ações permitidas, aplica autoridade e transforma a escolha do usuário em comando do domínio. O mesmo pipeline registra eventos/evidências e atualiza as projeções usadas por app, papel, agentes e canais.

O diferencial da feature é permitir que a pessoa continue executando a partir do objeto que já está diante dela — especialmente papel, QR ou documento — sem transformar essa superfície em um sistema isolado. O Scanner reduz navegação, preserva contexto e mantém consistência de estado.
