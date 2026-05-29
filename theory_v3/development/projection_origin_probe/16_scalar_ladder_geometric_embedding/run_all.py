from pathlib import Path
import runpy
import re

here = Path(__file__).parent
scripts = sorted(here.glob('make_*.py'), key=lambda p: int(re.match(r'make_(\d+)_', p.name).group(1)))
for script in scripts:
    print(f'Running {script.name}')
    runpy.run_path(str(script), run_name='__main__')
print(f'Generated {len(scripts)} reports.')
