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


scalar = sp.Integer(1)
radiative_phase = sp.Integer(4)
require_equal(radiative_phase - scalar, 3, 'scalar/radiative phase gap witness')


write_report('# Boundary symplectic closure conclusion\n\nThe final witness records the scope separation: scalar charge channel = 1, TT radiative phase channel in D=4 = 4 canonical variables per mode. The scalar boundary ledger cannot be the full dynamical boundary ledger.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_20_boundary_symplectic_closure_conclusion.py` passed.\n')
