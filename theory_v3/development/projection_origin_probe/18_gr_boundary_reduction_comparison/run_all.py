from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
scripts = sorted(root.glob('make_*.py'), key=lambda p: int(p.name.split('_')[1]))
for script in scripts:
    print(f'RUN {script.name}')
    subprocess.run([sys.executable, str(script)], check=True)
print(f'OK: ran {len(scripts)} scripts')
