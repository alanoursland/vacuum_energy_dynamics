
from pathlib import Path
import subprocess
import sys

base = Path(__file__).parent
scripts = sorted(base.glob('make_*.py'), key=lambda p: int(p.name.split('_')[1]))
for script in scripts:
    print(f"running {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)
print(f"ran {len(scripts)} scripts")
