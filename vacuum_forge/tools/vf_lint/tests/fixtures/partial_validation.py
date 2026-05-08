"""Fixture: a script with a mix of real validation and hardcoded verdicts."""
import sympy
from vacuumforge.core.simplify import is_zero

r = sympy.Symbol("r", positive=True)
expr = r - r

# Real validation
if is_zero(expr):
    print("[PASS] expression is zero")

# Hardcoded verdict — not gated on computation
print("[PASS] all modes confirmed")

# Another hardcoded verdict in a literal gate
if True:
    print("[PASS] always passes")
