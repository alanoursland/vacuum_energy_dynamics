#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, re

base=Path(__file__).resolve().parent
scripts=sorted(base.glob('make_*.py'), key=lambda p:int(re.match(r'make_(\d+)_', p.name).group(1)))
for script in scripts:
    print(f"==> {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)
print(f"ran {len(scripts)} scripts")
