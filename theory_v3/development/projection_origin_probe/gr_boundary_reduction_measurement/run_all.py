from pathlib import Path
import subprocess, sys, re

ROOT = Path(__file__).resolve().parent

def key(path):
    m = re.match(r"make_(\d+)_", path.name)
    return int(m.group(1)) if m else 10**9

for script in sorted(ROOT.glob('make_*.py'), key=key):
    print(f"running {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)
print('all gr_boundary_reduction_measurement reports regenerated')
