import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[7]
FOLDER_REGISTRY = ROOT / '01-master-index' / 'CENTRAL_CONTROL.csv'
SKILL_INDEX = Path(__file__).resolve().parents[1] / 'runtime' / 'registry' / 'skills-index.json'

def load_folder_registry():
    with FOLDER_REGISTRY.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_skill_index():
    if not SKILL_INDEX.exists():
        return {'skills': []}
    return json.loads(SKILL_INDEX.read_text(encoding='utf-8'))
