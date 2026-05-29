
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

x,y,eps,l=sp.symbols('x y eps lambda')
Q=x**2+y**2+eps*x**4
H=sp.hessian(Q,(x,y))
H_scaled=H.subs({x:l*x,y:l*y})
diff=sp.simplify(H_scaled-H)
require_nonzero(diff[0,0],'scale-dependent Hessian component')
require_zero(diff[1,1],'y Hessian component')
write(f'''# 3. Scale-Independent Hessian Gate

A metric tensor is a direction/scale-independent bilinear object at a point.
For

```text
Q = x^2 + y^2 + eps*x^4
```

the Hessian is

```text
{H}
```

After scaling `(x,y) -> (lambda x, lambda y)`, the Hessian shift is

```text
{diff}
```

The effective quadratic form depends on the magnitude of the probe unless `eps = 0`.
''')
