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


J = sp.Matrix([[0,1],[-1,0]])
S = J + J.T
for i in range(2):
    for j in range(2):
        require_zero(S[i,j], f'J antisym {i}{j}')
require_equal(J.det(), 1, 'canonical determinant')


write_report('# Canonical two-form matrix gate\n\nA boundary canonical pair has symplectic matrix `J = [[0,1],[-1,0]]`. The script verifies antisymmetry and nondegeneracy.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_3_canonical_two_form_matrix_gate.py` passed.\n')
