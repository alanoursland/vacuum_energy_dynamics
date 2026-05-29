
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


r, M, Lam = sp.symbols('r M Lambda')
Phi = -M/r - Lam*r**2/6
# Coefficient of the growing r^2 term must vanish for asymptotic flatness.
coeff_r2 = sp.Poly(Phi*r, r).coeff_monomial(r**3) # Phi*r = -M - Lam r^3/6
require_zero(coeff_r2 + Lam/6, 'extract r^2 growing coefficient')
# The condition coeff_r2=0 is equivalent to Lambda=0.
solution = sp.solve(sp.Eq(coeff_r2,0), Lam)
if solution != [0]:
    raise AssertionError(solution)


write_md(r'''
# 5. Asymptotic Flatness Selects Lambda Zero

The asymptotically flat inverse-square branch forbids the growing `r^2`
potential term. For

```text
Phi = -M/r - Lambda r^2/6,
```

the coefficient of the growing term vanishes exactly when

```text
Lambda = 0.
```

The script extracts that coefficient and solves the condition. This is a
branch-selection statement, not an ontology-level proof that `Lambda` must
vanish.
''')
