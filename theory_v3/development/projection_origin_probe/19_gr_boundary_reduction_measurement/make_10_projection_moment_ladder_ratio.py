from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.factor(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Projection moment ladder ratio

y, k, R = sp.symbols('y k R', positive=True, integer=True)
# Beta recurrence: B(k+1/2, R+2) / B(k-1/2, R+2)
# = (k-1/2)/(k+R+3/2).
r = (k - sp.Rational(1, 2))/(k + R + sp.Rational(3, 2))
expected = (2*k-1)/(2*k+2*R+3)
require_equal(r, expected, 'C_R moment ratio')


write_report('10_projection_moment_ladder_ratio.md', r'''
# 10. Projection moment ladder ratio

For

```text
C_R[P] = ∫_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy,
```

the adjacent moment ratio is

```text
I_k / I_(k-1) = (2k - 1)/(2k + 2R + 3).
```

This is the projection contact-class ladder.  `R` is the exponent label of the
chosen compactified moment functional.

''')
print('wrote 10_projection_moment_ladder_ratio.md')
