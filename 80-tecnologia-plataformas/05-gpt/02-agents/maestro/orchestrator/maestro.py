#!/usr/bin/env python3
import json, sys, uuid
from .registry import load_folder_registry, load_skill_index

def main():
    payload = json.load(sys.stdin)
    print(json.dumps({
        'request_id': payload.get('request_id') or str(uuid.uuid4()),
        'folder_registry_count': len(load_folder_registry()),
        'skill_count': len(load_skill_index().get('skills', [])),
        'policy': 'context -> skills -> canonical Folder ID -> provenance -> <=300 word summary'
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
