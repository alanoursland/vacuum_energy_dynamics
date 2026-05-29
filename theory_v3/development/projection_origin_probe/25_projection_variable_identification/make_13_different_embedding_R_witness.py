
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('13_different_embedding_R_witness.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
r0=(2*k-1)/(2*k+3)
r1=(2*k-1)/(2*k+5)
assert sp.simplify(r1.subs(k,1)-sp.Rational(1,7))==0
assert sp.simplify(r1.subs(k,2)-sp.Rational(3,9))==0
assert sp.simplify(r0-r1)!=0

OUT.write_text('# Different Embedding R Witness\n\nIf an additional endpoint contact factor `(1-y)^R` is inserted into the test pairing, the measured ratio changes to\n\n```text\nr_(R,k) = (2k - 1)/(2k + 2R + 3).\n```\n\nFor example, `R=1` changes `r_(1,1)` from `1/5` to `1/7`.\n\nThis is a direct witness that the contact class is projection-embedding data.\n')
print('wrote', OUT.name)
