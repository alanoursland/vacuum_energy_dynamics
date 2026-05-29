from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.combsimp(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

y = sp.symbols('y', positive=True)
j = sp.symbols('j', nonnegative=True, integer=True)
# Moment M_j = B(j+1/2,2).  Use the gamma recurrence
# Γ(j+5/2)=(j+3/2)(j+1/2)Γ(j+1/2).
closed = sp.Rational(4,1)/((2*j+1)*(2*j+3))
recurrence_form = 1/((j+sp.Rational(1,2))*(j+sp.Rational(3,2)))
require_equal(recurrence_form, closed, 'beta moment closed form by gamma recurrence')
# Spot-check the first three direct integrals.
for jj in range(3):
    direct = sp.integrate(y**jj*(1-y)*y**(-sp.Rational(1,2)), (y,0,1))
    require_equal(direct, closed.subs(j,jj), f'direct beta moment j={jj}')

write_report('6_compactified_beta_moment_functional.md', r'''
# 6. Compactified beta-moment functional

The projection-origin scalar admissibility functional uses moments

```text
M_j = ∫₀¹ y^j (1-y)y^{-1/2} dy.
```

SymPy verifies

```text
M_j = B(j+1/2,2) = 4 / [(2j+1)(2j+3)].
```

Interpretation: the projection ratio is controlled by a standard compactified
beta-moment ledger.
''')
print('wrote', '6_compactified_beta_moment_functional.md')
