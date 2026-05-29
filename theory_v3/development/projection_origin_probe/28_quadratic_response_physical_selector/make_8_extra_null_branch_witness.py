
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

t,x,eps=sp.symbols('t x eps')
Q=-t**2+x**2+eps*x**4
# Solve for t^2 as expression
s=sp.solve(sp.Eq(Q,0), t**2)[0]
require_nonzero(sp.simplify(s-x**2),'null relation correction')
write(f'''# 8. Null Relation Correction Witness

For

```text
Q = -t^2 + x^2 + eps*x^4
```

the null condition gives

```text
t^2 = {s}
```

The correction relative to the metric cone `t^2=x^2` is

```text
{sp.simplify(s-x**2)}
```

Thus the causal relation becomes amplitude/direction dependent unless the nonquadratic term is absent or separately routed.
''')
