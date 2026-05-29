
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('7_normalization_does_not_change_rk.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

c,a,b=sp.symbols('c a b', nonzero=True)
require_zero((c*a)/(c*b)-a/b)

OUT.write_text('# Normalization Does Not Change r_k\n\nMultiplying the moment functional by a constant does not affect the adjacent moment ratio.\n\nThus raw scale normalization is not the source of the contact-class distinction.\n\n```text\n(c C_R[y^k])/(c C_R[y^(k-1)]) = C_R[y^k]/C_R[y^(k-1)].\n```\n')
print('wrote', OUT.name)
