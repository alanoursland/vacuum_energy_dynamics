#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, re
base=Path(__file__).resolve().parent
scripts=sorted(base.glob('make_*.py'), key=lambda p:int(re.match(r'make_(\d+)_',p.name).group(1)))
for s in scripts:
    print(f"==> {s.name}")
    subprocess.check_call([sys.executable, str(s)], cwd=str(base))
print(f"ran {len(scripts)} scripts")
