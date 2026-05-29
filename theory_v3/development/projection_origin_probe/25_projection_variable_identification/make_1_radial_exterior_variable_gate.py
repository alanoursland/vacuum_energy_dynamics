
import sympy as sp
from pathlib import Path

OUT = Path(__file__).with_name('1_radial_exterior_variable_gate.md')

def require_zero(expr):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f'Expected zero, got {expr}')

r,q,A=sp.symbols('r q A', positive=True)
Phi_r=A/r
Phi_q=sp.simplify(Phi_r.subs(r,1/q))
require_zero(Phi_q-A*q)
assert sp.diff(Phi_q,q).subs(q,0)==A

OUT.write_text('# Radial Exterior Variable Gate\n\nThe weak-field scalar exterior is represented by a finite-flux monopole potential.  The physical exterior datum is the falloff class `Phi ~ A/r`, not a unique compactified projection variable.\n\n## SymPy check\n\nSet `q=1/r`.  Then `Phi=A/r` becomes `Phi=A*q`.  The compactified boundary at infinity is `q=0`; the exterior solution has first-order contact in `q`.\n\n```text\nPhi(r)=A/r -> Phi(q)=A q\n```\n\nThis closes only the physical exterior falloff, not the projection chart.\n')
print('wrote', OUT.name)
