from pathlib import Path
import subprocess, sys
base=Path(__file__).parent
scripts=sorted(base.glob('make_*.py'), key=lambda p:int(p.name.split('_')[1]))
for s in scripts:
    print('running', s.name)
    subprocess.check_call([sys.executable, str(s)], cwd=base)
print('all projection_variable_identification reports regenerated')
