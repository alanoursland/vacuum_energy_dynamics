
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)


Lam, G = sp.symbols('Lambda G')
# Model the local connection-strain density as a quadratic strain variable G^2.
strain = G**2
baseline = Lam
# In a constant metric patch, G=0 but the baseline term remains.
require_zero(strain.subs(G,0), 'zero connection strain in constant patch')
require_zero(baseline.subs(G,0)-Lam, 'baseline survives zero strain')
require_zero(sp.diff(baseline, G), 'lambda independent of strain variable')


write_md(r'''
# 2. Lambda Is Not Connection Strain

The local quadratic strain branch and the cosmological baseline are different
objects. In a constant-metric patch the schematic connection strain variable
`G` vanishes, so `G^2 = 0`, but the baseline `Lambda` remains.

The script checks that the baseline has no derivative with respect to the
strain variable. This prevents hiding `Lambda` inside the connection-strain
energy.
''')
