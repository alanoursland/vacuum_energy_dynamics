#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, re

def key(p):
    m=re.match(r'make_(\d+)_', p.name)
    return int(m.group(1)) if m else 999

scripts=sorted(Path(__file__).parent.glob('make_*.py'), key=key)
for s in scripts:
    print(f'RUN {s.name}')
    subprocess.check_call([sys.executable, str(s)])
print('generated', len(scripts), 'reports')
