#!/usr/bin/env python3
"""
Run all quadratic_response_selector proof generators in numeric order.
"""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parent

def key(path: Path):
    match = re.match(r"make_(\d+)_", path.name)
    return int(match.group(1)) if match else 10**9

scripts = sorted(root.glob("make_*.py"), key=key)
for script in scripts:
    print(f"RUN {script.name}")
    subprocess.run([sys.executable, str(script)], cwd=root, check=True)
print(f"Completed {len(scripts)} proof generators.")
