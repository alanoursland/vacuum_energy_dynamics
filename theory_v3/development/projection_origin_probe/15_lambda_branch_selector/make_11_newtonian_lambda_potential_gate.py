
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


r, G, M, Lam = sp.symbols('r G M Lambda', positive=True)
Phi = -G*M/r - Lam*r**2/6
field = -sp.diff(Phi,r)
expected = -G*M/r**2 + Lam*r/3
require_zero(field-expected, 'Newtonian field with Lambda')
lap = sp.diff(Phi,r,2) + 2*sp.diff(Phi,r)/r
require_zero(lap + Lam, 'Laplacian of Lambda potential plus point-free part')


write_md(r'''
# 11. Newtonian Lambda Potential Gate

For the weak static branch away from the point source,

```text
Phi = -GM/r - Lambda r^2/6
```

produces

```text
- Phi' = -GM/r^2 + Lambda r/3.
```

The script also checks the smooth radial Laplacian contribution
`Delta Phi = -Lambda` away from the origin. Again, the Lambda term is a
large-scale asymptotic/background contribution, not another finite monopole.
''')
