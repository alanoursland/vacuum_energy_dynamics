#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
scripts = sorted(base.glob('make_*.py'), key=lambda p: int(p.name.split('_')[1]))
for script in scripts:
    print(f'==> {script.name}')
    subprocess.check_call([sys.executable, str(script)], cwd=base)
print(f'generated {len(scripts)} reports')
