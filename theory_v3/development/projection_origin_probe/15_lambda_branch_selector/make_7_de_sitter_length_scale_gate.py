
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


D, Lam, H2 = sp.symbols('D Lambda H2', positive=True)
expr = sp.Eq(H2, 2*Lam/((D-1)*(D-2)))
D4 = sp.simplify(expr.rhs.subs(D,4))
require_zero(D4 - Lam/3, 'D=4 de Sitter H^2')
# Verify undefined/singular at D=2, which is not an EH dynamical branch.
den = (D-1)*(D-2)
require_zero(den.subs(D,2), 'singular denominator at D=2')


write_md(r'''
# 7. De Sitter Length Scale Gate

For the Einstein branch in `D` spacetime dimensions, a constant-curvature
vacuum has scale

```text
H^2 = 2 Lambda / ((D-1)(D-2)).
```

The script checks that in `D=4`,

```text
H^2 = Lambda/3.
```

This records that nonzero `Lambda` creates a curvature scale rather than a
localized inverse-square flux contribution.
''')
