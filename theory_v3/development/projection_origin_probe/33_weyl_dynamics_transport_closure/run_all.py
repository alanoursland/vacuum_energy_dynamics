#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, re

here = Path(__file__).resolve().parent
files = sorted(here.glob('make_*.py'), key=lambda p: int(re.match(r'make_(\d+)_', p.name).group(1)))
for f in files:
    print(f'Running {f.name}...')
    subprocess.check_call([sys.executable, str(f)], cwd=str(here))
print(f'Generated {len(files)} reports.')
