
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


r, Lam = sp.symbols('r Lambda', positive=True)
f = 1 - Lam*r**2/3
roots = sp.solve(sp.Eq(f,0), r)
# solve gives [-sqrt(3)/sqrt(Lambda), sqrt(3)/sqrt(Lambda)] maybe order
positive = sp.sqrt(3/Lam)
if positive not in roots and sp.sqrt(3)/sp.sqrt(Lam) not in roots:
    raise AssertionError(roots)
require_zero(f.subs(r, positive), 'de Sitter horizon root')


write_md(r'''
# 17. Positive Lambda Horizon Scale

For the pure positive-Lambda static factor

```text
f(r) = 1 - Lambda r^2/3,
```

the positive root is

```text
r = sqrt(3/Lambda).
```

The script checks the root. This records that positive `Lambda` introduces a
large-scale horizon/asymptotic change, not merely a local source correction.
''')
