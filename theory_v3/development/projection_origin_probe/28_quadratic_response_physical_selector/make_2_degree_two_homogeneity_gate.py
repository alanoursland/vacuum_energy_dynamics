
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

l,x,y,eps = sp.symbols('lambda x y eps')
Q2 = x**2+y**2
Q4 = x**2+y**2+eps*x**4
def homog_defect(Q):
    return sp.expand(Q.subs({x:l*x,y:l*y}) - l**2*Q)
h2=require_zero(homog_defect(Q2),'Q2 homogeneity defect')
h4=require_nonzero(homog_defect(Q4),'Q4 homogeneity defect')
write(f'''# 2. Degree-Two Homogeneity Gate

Metric interval response is homogeneous of degree two:

```text
Q(lambda v) = lambda^2 Q(v)
```

The quadratic branch has defect:

```text
{h2}
```

The quartic branch has defect:

```text
{sp.factor(h4)}
```

So exact scale-homogeneous interval response kills quartic residuals unless `eps = 0` or `lambda` is fixed rather than arbitrary.
''')
