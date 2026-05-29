
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expr'):
    s = sp.simplify(expr)
    if s != 0:
        raise AssertionError(f"{name} expected 0, got {s}")
    return s

def require_nonzero(expr, name='expr'):
    s = sp.simplify(expr)
    if s == 0:
        raise AssertionError(f"{name} expected nonzero")
    return s

def write(md):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(md.strip() + '\n')
    tmp.replace(OUT)

x,y,eps = sp.symbols('x y eps')
Q2 = x**2 + y**2
Q4 = x**2 + y**2 + eps*x**4
u = {x: sp.symbols('u1'), y: sp.symbols('u2')}
v = {x: sp.symbols('v1'), y: sp.symbols('v2')}
u1,u2,v1,v2 = u[x],u[y],v[x],v[y]
def evalQ(Q,a,b): return Q.subs({x:a,y:b})
def para(Q):
    return sp.expand(evalQ(Q,u1+v1,u2+v2)+evalQ(Q,u1-v1,u2-v2)-2*evalQ(Q,u1,u2)-2*evalQ(Q,v1,v2))
p2 = require_zero(para(Q2),'quadratic parallelogram defect')
p4 = require_nonzero(para(Q4),'quartic parallelogram defect')
write(f'''# 1. Parallelogram Physical Gate

The parallelogram identity is the exact algebraic signature of quadratic interval response.

For `Q2 = x^2 + y^2`, the defect is:

```text
{p2}
```

For `Q4 = x^2 + y^2 + eps*x^4`, the defect is:

```text
{sp.factor(p4)}
```

Thus a quartic residual is not invisible to the metric gate. It violates the exact parallelogram law unless `eps = 0`.
''')
