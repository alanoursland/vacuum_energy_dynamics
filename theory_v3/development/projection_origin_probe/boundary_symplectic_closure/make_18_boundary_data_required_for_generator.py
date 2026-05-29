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


q, p, eps = sp.symbols('q p eps')
G = eps*p
require_equal(sp.diff(G,p), eps, 'q transformation')
require_zero(-sp.diff(G,q), 'p transformation')


write_report('# Boundary data required for generator\n\nA boundary generator acts on canonical boundary data. For `G=epsilon p`, `delta q=epsilon` and `delta p=0`.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_18_boundary_data_required_for_generator.py` passed.\n')
