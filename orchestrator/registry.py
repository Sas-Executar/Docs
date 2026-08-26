import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'runtime' / 'registry' / 'skills-index.json'

def load_index():
    if not INDEX.exists():
        return {'skills': []}
    return json.loads(INDEX.read_text(encoding='utf-8'))
