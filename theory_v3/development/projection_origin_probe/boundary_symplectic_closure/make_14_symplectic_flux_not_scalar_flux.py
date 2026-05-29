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


Q, C, P = sp.symbols('Q C P')
scalar = Q
symp = C*P
require_zero(sp.diff(scalar,C), 'scalar blind to shear coordinate')
require_equal(sp.diff(symp,C), P, 'symplectic sees conjugate')


write_report('# Symplectic flux not scalar flux\n\nA scalar ledger can be insensitive to a shear coordinate while the symplectic ledger detects its conjugate momentum.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_14_symplectic_flux_not_scalar_flux.py` passed.\n')
