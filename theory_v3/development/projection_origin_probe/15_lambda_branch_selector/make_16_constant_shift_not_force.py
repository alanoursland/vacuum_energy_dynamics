
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


r, C = sp.symbols('r C')
Phi = C
field = -sp.diff(Phi,r)
require_zero(field, 'constant potential has no force')
# But a Lambda term is not a constant potential; it is quadratic in r in the reduction.
Lam = sp.symbols('Lambda')
Phi_l = -Lam*r**2/6
field_l = -sp.diff(Phi_l,r)
require_zero(field_l - Lam*r/3, 'Lambda is not constant potential shift')


write_md(r'''
# 16. Constant Shift Is Not a Force Gate

A constant potential shift has zero field. The Lambda contribution in the
Newtonian reduction is different: it is quadratic in radius and therefore gives
a linear radial field.

The script checks both statements. This separates harmless potential offsets
from genuine vacuum-baseline curvature branches.
''')
