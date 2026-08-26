#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
git submodule update --init --recursive
python3 "$ROOT/80-tecnologia-plataformas/05-gpt/02-agents/maestro/scripts/index_skills.py"
echo "Maestro ready."
