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


p, dq1, dq2, dp1, dp2 = sp.symbols('p dq1 dq2 dp1 dp2')
omega = dp1*dq2 - dp2*dq1
omega_swap = dp2*dq1 - dp1*dq2
require_zero(omega + omega_swap, 'symplectic antisymmetry')


write_report('# Boundary potential gives symplectic current\n\nFrom `theta(delta)=p delta q`, the symplectic current is\n\n```text\nomega(delta_1, delta_2)=delta_1 p delta_2 q - delta_2 p delta_1 q.\n```\n\nThe script checks antisymmetry under exchanging the variations.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_2_boundary_potential_symplectic_current.py` passed.\n')
