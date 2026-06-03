#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
missing=[]
for f in root.rglob('*.html'):
    txt=f.read_text(encoding='utf-8', errors='ignore')
    for attr in ['href','src']:
        for ref in re.findall(attr+r'="([^"]+)"', txt):
            if ref.startswith(('http','https','mailto','#','data:','javascript:')):
                continue
            target=(f.parent/ref.split('#')[0]).resolve()
            if not target.exists():
                missing.append((str(f.relative_to(root)), attr, ref))
print('HTML files:', len(list(root.rglob('*.html'))))
print('Missing refs:', len(missing))
for item in missing:
    print('MISSING', item)
sys.exit(1 if missing else 0)
