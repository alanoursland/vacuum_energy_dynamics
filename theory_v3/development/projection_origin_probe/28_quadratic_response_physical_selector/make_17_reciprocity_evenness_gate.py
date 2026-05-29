
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

x,a,b=sp.symbols('x a b')
Q=a*x**2+b*x**3
recip=sp.expand(Q.subs(x,-x)-Q)
require_nonzero(recip,'odd reciprocity defect')
sol=sp.solve(sp.Poly(recip,x).coeffs(),[b], dict=True)
write(f'''# 17. Reciprocity / Evenness Gate

Interval response must not change under reversing the probe orientation if it represents an unoriented interval.
For

```text
Q = a*x^2 + b*x^3
```

the reversal defect is

```text
{recip}
```

Solving the reciprocity condition gives

```text
{sol}
```

So odd response terms are excluded by interval reciprocity before the quadratic gate even acts.
''')
