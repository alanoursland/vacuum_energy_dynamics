
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('3_y_variable_beta_weight_origin.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

y,R=sp.symbols('y R', positive=True)
weight=(1-y)**(R+1)*y**sp.Rational(-1,2)
base=weight.subs(R,0)
require_zero(base-(1-y)*y**sp.Rational(-1,2))

OUT.write_text('# y-Variable Beta Weight Origin\n\nThe factor `y^(-1/2)` is not a new physical field.  It is the Jacobian of the even-power projection variable `y=x^2`.\n\nThe base moment family has the form\n\n```text\nC_R[P] = ∫_0^1 P(y) (1-y)^(R+1) y^(-1/2) dy.\n```\n\nThus the displayed weight already combines contact information and variable choice.\n')
print('wrote', OUT.name)
