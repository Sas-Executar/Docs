# Portabilidade

O Maestro separa roteamento (Python/JSON/SQL), contrato (Protobuf), expertise (Markdown/SKILL.md) e execução de IA (adapter externo).

Online: `bash scripts/bootstrap.sh`.

Offline: inicialize o submódulo e depois compacte o diretório completo. O orchestrator faz shortlist; o runtime de IA deve ler cada `SKILL.md` selecionado antes de aplicar o workflow.
