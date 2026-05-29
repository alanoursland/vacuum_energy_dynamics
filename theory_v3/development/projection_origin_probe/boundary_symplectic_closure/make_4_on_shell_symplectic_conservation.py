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


t, x = sp.symbols('t x')
q1 = sp.Function('q1')(t,x)
q2 = sp.Function('q2')(t,x)
jt = sp.diff(q1,t)*q2 - sp.diff(q2,t)*q1
jx = -(sp.diff(q1,x)*q2 - sp.diff(q2,x)*q1)
div = sp.diff(jt,t)+sp.diff(jx,x)
E1 = sp.diff(q1,t,2)-sp.diff(q1,x,2)
E2 = sp.diff(q2,t,2)-sp.diff(q2,x,2)
require_zero(sp.expand(div - (E1*q2 - E2*q1)), 'symplectic current divergence identity')


write_report('# On-shell symplectic conservation\n\nFor the linear wave equation, `d_mu j^mu = E[q1] q2 - E[q2] q1`. On shell, the symplectic current is conserved.\n\n## Validation\n\nThis report was generated only after the SymPy checks in `make_4_on_shell_symplectic_conservation.py` passed.\n')
