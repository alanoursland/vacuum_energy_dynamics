
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

x,y,eps=sp.symbols('x y eps')
Q=x**2+y**2+eps*x**4
H0=sp.hessian(Q,(x,y)).subs({x:0,y:0})
remainder=sp.expand(Q - (sp.Matrix([x,y]).T*H0*sp.Matrix([x,y]))[0]/2)
require_nonzero(remainder,'higher-order remainder')
write(f'''# 11. Local Hessian Is Not Exact Metric

At the origin, the Hessian of

```text
Q=x^2+y^2+eps*x^4
```

is

```text
{H0}
```

The quadratic Hessian approximation leaves remainder

```text
{remainder}
```

Thus smooth stationary response gives a local metric approximation, not an exact metric ontology unless higher-order response is suppressed or routed.
''')
