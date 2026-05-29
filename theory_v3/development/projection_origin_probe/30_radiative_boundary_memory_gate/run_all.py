from pathlib import Path
import subprocess, sys, re
ROOT=Path(__file__).resolve().parent

def key(p):
    m=re.match(r'make_(\d+)_', p.name)
    return int(m.group(1)) if m else 10**9

scripts=sorted(ROOT.glob('make_*.py'), key=key)
for s in scripts:
    print(f'RUN {s.name}')
    subprocess.check_call([sys.executable, str(s)], cwd=str(ROOT))
print(f'OK: {len(scripts)} scripts regenerated reports')
