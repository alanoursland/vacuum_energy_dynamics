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


p, dq = sp.symbols('p dq')
residual = p*dq + (-p*dq)
require_zero(residual, 'boundary generator cancellation')


write_report('# Boundary generator cancels variation\n\nIf the bulk variation leaves `+p delta q`, adding a boundary generator with variation `-p delta q` cancels the residue.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_6_boundary_generator_cancels_variation.py` passed.\n')
