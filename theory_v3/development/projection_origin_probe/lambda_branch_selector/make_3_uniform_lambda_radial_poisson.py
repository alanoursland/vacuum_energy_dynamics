
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)


r, Lam, C1, C2 = sp.symbols('r Lambda C1 C2', positive=True)
Phi = -Lam*r**2/6 + C1/r + C2
lap = sp.diff(Phi,r,2) + 2*sp.diff(Phi,r)/r
require_zero(lap + Lam, 'D=3 radial Laplacian of Lambda potential')
field = -sp.diff(Phi,r)
expected = Lam*r/3 + C1/r**2
require_zero(field-expected, 'Lambda field has linear radial term')


write_md(r'''
# 3. Uniform Lambda Radial Poisson Gate

In three spatial dimensions, a uniform vacuum baseline in the Newtonian
reduction produces an `r^2` potential term:

```text
Phi(r) = - Lambda r^2 / 6 + C1/r + C2.
```

The script checks

```text
Delta Phi = - Lambda
```

and therefore

```text
- Phi'(r) = Lambda r/3 + C1/r^2.
```

So nonzero `Lambda` is not another inverse-square localized flux source. It
changes the large-radius asymptotic class.
''')
