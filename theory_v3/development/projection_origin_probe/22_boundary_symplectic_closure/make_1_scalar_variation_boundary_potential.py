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


x = sp.symbols('x')
phi = sp.Function('phi')(x)
eta = sp.Function('eta')(x)
Lvar = sp.diff(phi,x)*sp.diff(eta,x)
bulk = -sp.diff(phi,x,2)*eta
boundary_derivative = sp.diff(sp.diff(phi,x)*eta, x)
require_zero(Lvar - (bulk + boundary_derivative), 'IBP decomposition')


write_report("# Scalar variation boundary potential\n\nThe scalar Dirichlet variation has the integration-by-parts split\n\n```text\nphi' eta' = -phi'' eta + d(phi' eta)/dx.\n```\n\nThe boundary potential in this model is `theta = phi' delta phi`. This is the prototype for the later symplectic boundary ledger.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_1_scalar_variation_boundary_potential.py` passed.\n")
