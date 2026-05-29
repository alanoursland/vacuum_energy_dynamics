from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expression'):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{name} did not simplify to zero: {val}")

def require_equal(a, b, name='equality'):
    require_zero(sp.simplify(a-b), name)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


q, p = sp.symbols('q p')
A = 2*q + p
B = q + 3*p
condition = sp.diff(A,p) - sp.diff(B,q)
require_zero(condition, 'integrability condition')
Q = q**2 + q*p + sp.Rational(3,2)*p**2
require_zero(sp.diff(Q,q)-A, 'dQdq')
require_zero(sp.diff(Q,p)-B, 'dQdp')


write_report('# Charge integrability condition\n\nA boundary charge variation `delta Q = A dq + B dp` is integrable only if `partial_p A = partial_q B`.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_7_charge_integrability_condition.py` passed.\n')
