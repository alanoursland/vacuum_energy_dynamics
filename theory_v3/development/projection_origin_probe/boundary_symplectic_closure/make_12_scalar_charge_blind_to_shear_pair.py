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


s = sp.symbols('s')
M = sp.Matrix([[s,0],[0,-s]])
trace = sp.trace(M)
norm2 = sum(M[i,j]**2 for i in range(2) for j in range(2))
require_zero(trace, 'shear trace')
require_equal(norm2, 2*s**2, 'shear nonzero norm')


write_report('# Scalar charge blind to shear pair\n\nA traceless shear matrix can have zero scalar trace but nonzero invariant content.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_12_scalar_charge_blind_to_shear_pair.py` passed.\n')
