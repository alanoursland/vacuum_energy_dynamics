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


q,p = sp.symbols('q p')
coeff = sp.Integer(1)
require_zero(sp.diff(coeff,q), 'd coeff dq')
require_zero(sp.diff(coeff,p), 'd coeff dp')


write_report('# Boundary symplectic form closure\n\nThe canonical symplectic form `Omega=dq wedge dp` is closed for constant canonical coefficient.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_17_boundary_symplectic_form_closure.py` passed.\n')
