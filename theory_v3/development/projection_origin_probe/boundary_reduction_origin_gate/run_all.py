#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, re
root=Path(__file__).resolve().parent
scripts=sorted(root.glob('make_*.py'), key=lambda p:int(re.match(r'make_(\d+)_',p.name).group(1)))
for s in scripts:
    print(f'RUN {s.name}')
    subprocess.run([sys.executable, str(s)], check=True)
print(f'OK: ran {len(scripts)} generators')
