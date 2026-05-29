
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('8_field_rescaling_contact_shift.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

y,s,R=sp.symbols('y s R')
w=(1-y)**(R+1)*y**sp.Rational(-1,2)
w_shift=sp.simplify(w*(1-y)**s)
require_zero(w_shift-(1-y)**(R+s+1)*y**sp.Rational(-1,2))

OUT.write_text('# Field Rescaling Contact Shift\n\nMultiplying a compactified field or test factor by `(1-y)^s` shifts endpoint contact bookkeeping.\n\nThis can change the displayed projection weight without changing the physical exterior `1/r` class.\n\nTherefore contact index `R` belongs to the projection embedding, not to raw exterior falloff alone.\n')
print('wrote', OUT.name)
