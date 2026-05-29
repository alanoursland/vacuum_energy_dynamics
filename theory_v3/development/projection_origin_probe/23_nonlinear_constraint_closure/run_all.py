#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
here = Path(__file__).resolve().parent
scripts = sorted(here.glob("make_*.py"), key=lambda p: int(p.name.split("_")[1]))
for script in scripts:
    print(f"running {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)
print(f"ran {len(scripts)} scripts")
