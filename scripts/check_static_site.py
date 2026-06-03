#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
missing=[]
def is_excluded(path):
    return any(part in {'_backups', '.git', '__MACOSX'} for part in path.parts)
html_files=[f for f in root.rglob('*.html') if not is_excluded(f.relative_to(root))]
for f in html_files:
    txt=f.read_text(encoding='utf-8', errors='ignore')
    for attr in ['href','src']:
        for ref in re.findall(attr+r'="([^"]+)"', txt):
            if ref.startswith(('http','https','mailto','#','data:','javascript:')):
                continue
            target=(f.parent/ref.split('#')[0]).resolve()
            if not target.exists():
                missing.append((str(f.relative_to(root)), attr, ref))
print('HTML files:', len(html_files))
print('Missing refs:', len(missing))
for item in missing:
    print('MISSING', item)
sys.exit(1 if missing else 0)
