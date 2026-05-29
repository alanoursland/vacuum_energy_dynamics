
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('9_same_flux_different_contact_witness.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

k=sp.symbols('k', positive=True, integer=True)
r0=(2*k-1)/(2*k+3)
r1=(2*k-1)/(2*k+5)
assert sp.simplify(r0.subs(k,1)-sp.Rational(1,5))==0
assert sp.simplify(r1.subs(k,1)-sp.Rational(1,7))==0
assert sp.simplify(r0-r1)!=0

OUT.write_text('# Same Flux, Different Contact Witness\n\nTwo compactified representatives can encode the same finite exterior flux while carrying different endpoint contact factors in the test pairing.\n\nThis is the key obstruction to reading `R_GR` directly from `Phi ~ 1/r`.\n\nThe physical flux fixes the exterior exponent.  The moment ladder fixes a chart/test pairing.\n')
print('wrote', OUT.name)
