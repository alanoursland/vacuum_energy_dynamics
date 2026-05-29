#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
base=Path(__file__).parent
scripts=sorted(base.glob('make_*.py'), key=lambda p:int(p.name.split('_')[1]))
for s in scripts:
    print('Running', s.name)
    subprocess.check_call([sys.executable, str(s)])
print(f'Generated {len(scripts)} reports.')
