from pathlib import Path
import subprocess, sys, re

base = Path(__file__).parent
scripts = sorted(base.glob('make_*.py'), key=lambda p: int(re.match(r'make_(\d+)_', p.name).group(1)))
for script in scripts:
    print(f"running {script.name}")
    subprocess.check_call([sys.executable, str(script)], cwd=base)
print(f"generated {len(scripts)} reports")
