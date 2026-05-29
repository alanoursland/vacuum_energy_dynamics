
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


r, M, Lam, D = sp.symbols('r M Lambda D')
N_TT = D*(D-3)/2
D_solutions = sp.solve(sp.Eq(N_TT,2), D)
if 4 not in D_solutions:
    raise AssertionError(D_solutions)
flux = M - Lam*r**3/3
coeff = sp.Poly(flux, r).coeff_monomial(r**3)
Lam_solution = sp.solve(sp.Eq(coeff,0), Lam)
if Lam_solution != [0]:
    raise AssertionError(Lam_solution)


write_md(r'''
# 21. Branch Intersection Selector

Intersecting two separate selectors gives the familiar weak branch:

```text
N_TT = 2  ->  D = 4,
finite asymptotic flux -> Lambda = 0.
```

The script checks both algebraic gates. This is an intersection of assumptions
and boundary conditions, not a proof that all other branches are impossible.
''')
