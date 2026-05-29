
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('5_rk_from_C0_ratio.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
a=k+sp.Rational(1,2)
ap=k-sp.Rational(1,2)
M_k=1/(a*(a+1))
M_prev=1/(ap*(ap+1))
r=sp.factor(M_k/M_prev)
require_zero(r-(2*k-1)/(2*k+3))

OUT.write_text('# r_k from C0 Ratio\n\nThe original coefficient is recovered from the base moment functional:\n\n```text\nr_k = C_0[y^k] / C_0[y^(k-1)] = (2k - 1)/(2k + 3).\n```\n\nThis identifies the original `r_k` as the `R=0` compactified moment-kernel coefficient.\n')
print('wrote', OUT.name)
