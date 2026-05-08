"""Fixture: a script where PASS verdicts are gated on real computation."""
import sympy
from vacuumforge.core.simplify import is_zero

r = sympy.Symbol("r", positive=True)
expr = sympy.simplify(r - r)

if is_zero(expr):
    print("[PASS] expression is zero")
else:
    print("[FAIL] expression is not zero")

result = is_zero(sympy.Integer(0))
if result:
    print("[PASS] zero check works")
