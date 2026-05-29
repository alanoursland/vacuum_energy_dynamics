
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

a,b,c,d,eps=sp.symbols('a b c d eps')
x,y=sp.symbols('x y')
Q=x**2+y**2+eps*x**4
def B(u1,u2,v1,v2):
    return sp.expand((Q.subs({x:u1+v1,y:u2+v2})-Q.subs({x:u1,y:u2})-Q.subs({x:v1,y:v2}))/2)
B1=B(a,0,b,0)
B2=B(a+c,0,b,0)-B(c,0,b,0)
shift=sp.expand(B2-B1)
require_nonzero(shift,'polarization background shift')
write(f'''# 4. Polarization Path-Independence Gate

For exact quadratic response, polarization gives a bilinear form independent of background amplitude.
For a quartic residual, the polarized cross-term changes when evaluated around a shifted probe.

Base polarized response along `x`:

```text
{sp.factor(B1)}
```

Shifted-background difference:

```text
{sp.factor(shift)}
```

Thus quartic response cannot be owned by one direction-independent metric bilinear form.
''')
