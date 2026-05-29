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
bulk_plus_boundary = -sp.diff(phi,x,2)*eta + sp.diff(sp.diff(phi,x)*eta,x)
var_density = sp.diff(phi,x)*sp.diff(eta,x)
require_zero(var_density - bulk_plus_boundary, 'Hamiltonian variation split')


write_report('# Hamiltonian boundary differentiability\n\nThe Hamiltonian variation of a gradient energy splits into bulk plus boundary terms. The boundary term must be killed by boundary conditions or owned by a boundary generator.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_5_hamiltonian_boundary_differentiability.py` passed.\n')
