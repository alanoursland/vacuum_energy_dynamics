
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('2_compactification_jacobian_gate.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

y=sp.symbols('y', positive=True)
x=sp.sqrt(y)
dxdy=sp.diff(x,y)
require_zero(dxdy-1/(2*sp.sqrt(y)))

OUT.write_text('# Compactification Jacobian Gate\n\nA compactified variable changes the integration measure.  The projection weight is therefore partly a chart/test-pairing object.\n\n## SymPy check\n\nFor `y=x^2`,\n\n```text\ndx = (1/(2 sqrt(y))) dy.\n```\n\nThis accounts for the ubiquitous beta-factor `y^(-1/2)` in the moment functional.\n')
print('wrote', OUT.name)
