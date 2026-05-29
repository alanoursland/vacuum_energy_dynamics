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


m = sp.symbols('m', integer=True, positive=True)
N = m*(m+1)/2
phase = 2*N
require_equal(phase.subs(m,3), 12, '3-boundary phase components')
require_equal((N-1).subs(m,3), 5, 'traceless configuration gap')


write_report('# Boundary tensor canonical pair count\n\nOn a three-boundary, a symmetric tensor has six configuration components and twelve phase-space components. Scalar trace data supplies only one configuration component.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_13_boundary_tensor_pair_count.py` passed.\n')
