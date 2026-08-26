#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
git submodule update --init --recursive
python3 "$ROOT/scripts/index_skills.py"
mkdir -p "$ROOT/runtime/inbox" "$ROOT/runtime/outbox" "$ROOT/runtime/registry"
echo 'Maestro ready.'
