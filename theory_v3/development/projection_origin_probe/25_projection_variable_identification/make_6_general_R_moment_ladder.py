
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('6_general_R_moment_ladder.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k,R=sp.symbols('k R', positive=True, integer=True)
# Adjacent beta ratio B(a+1,b)/B(a,b)=a/(a+b) with a=k-1/2, b=R+2
r=sp.factor((k-sp.Rational(1,2))/(k+R+sp.Rational(3,2)))
require_zero(r-(2*k-1)/(2*k+2*R+3))

OUT.write_text('# General R Moment Ladder\n\nAdding endpoint contact weight `(1-y)^R` shifts the adjacent moment ratio.\n\n```text\nC_R[P] = ∫ P(y)(1-y)^(R+1)y^(-1/2)dy\nr_(R,k) = (2k - 1)/(2k + 2R + 3).\n```\n\nSo `R` classifies the chosen contact/test-pairing ladder.\n')
print('wrote', OUT.name)
