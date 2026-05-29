from pathlib import Path
import subprocess, sys
root=Path(__file__).parent
scripts=sorted(root.glob('make_*.py'), key=lambda p:int(p.name.split('_')[1]))
for s in scripts:
    print('running', s.name)
    subprocess.check_call([sys.executable, str(s)], cwd=root)
print('ok')
