
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('14_raw_weight_not_invariant.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

y,z=sp.symbols('y z', positive=True)
y_of_z=z**2
jac=sp.diff(y_of_z,z)
w_y=y**sp.Rational(-1,2)
w_z=sp.simplify(w_y.subs(y,y_of_z)*jac)
require_zero(w_z-2)

OUT.write_text('# Raw Weight Is Not Invariant\n\nA displayed weight is not invariant under variable changes.\n\nThe invariant comparison is the full pushforward of:\n\n```text\nfield variable + compactification + Jacobian + test pairing.\n```\n\nTherefore `same raw weight` is too strong and `different raw weight` is too weak as a physical comparison.\n')
print('wrote', OUT.name)
