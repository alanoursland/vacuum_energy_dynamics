from pathlib import Path
import subprocess, sys

here = Path(__file__).parent
scripts = sorted(here.glob('make_*.py'), key=lambda p: int(p.name.split('_')[1]))
for script in scripts:
    print(f'Running {script.name}')
    subprocess.check_call([sys.executable, str(script)], cwd=here)
print(f'Ran {len(scripts)} scripts.')
