
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('4_base_moment_functional_C0.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
a=k+sp.Rational(1,2)
M=1/(a*(a+1))
require_zero(M-1/((k+sp.Rational(1,2))*(k+sp.Rational(3,2))))

OUT.write_text('# Base Moment Functional C0\n\nThe observed projection ladder uses the base functional\n\n```text\nC_0[P] = ∫_0^1 P(y) (1-y) y^(-1/2) dy.\n```\n\nFor monomials,\n\n```text\nC_0[y^k] = B(k+1/2, 2).\n```\n\nThe ratio of adjacent moments gives the observed coefficient.\n')
print('wrote', OUT.name)
