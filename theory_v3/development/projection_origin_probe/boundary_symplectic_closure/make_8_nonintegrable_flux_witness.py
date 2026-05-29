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
A = p
B = 0
condition = sp.diff(A,p) - sp.diff(B,q)
require_equal(condition, 1, 'nonintegrable witness')


write_report('# Nonintegrable flux witness\n\nThe one-form `p dq` is not exact on the full `(q,p)` space. Some boundary variations are fluxes, not integrable charges.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_8_nonintegrable_flux_witness.py` passed.\n')
