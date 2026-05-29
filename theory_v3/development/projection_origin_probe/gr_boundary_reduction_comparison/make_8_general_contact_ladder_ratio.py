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

k, R = sp.symbols('k R', positive=True, integer=True)
# Beta recurrence:
# B(k+1/2,R+2)/B(k-1/2,R+2)
# = Γ(k+1/2)Γ(k+R+3/2) / [Γ(k-1/2)Γ(k+R+5/2)]
ratio = (k-sp.Rational(1,2))/(k+R+sp.Rational(3,2))
expected = (2*k-1)/(2*k+2*R+3)
require_equal(ratio, expected, 'general r_Rk beta ratio')

write_report('8_general_contact_ladder_ratio.md', r'''
# 8. General endpoint-contact ladder ratio

For the generalized contact/admissibility functional

```text
C_R[P] = ∫₀¹ P(y)(1-y)^{R+1} y^{-1/2} dy,
```

the moment ratio is

```text
r_(R,k) = B(k+1/2,R+2) / B(k-1/2,R+2)
        = (2k-1)/(2k+2R+3).
```

The observed projection ratio is the base case `R=0`.

Interpretation: the projection coefficient belongs to a standard endpoint-
contact ladder, not to a standalone physical law.
''')
print('wrote', '8_general_contact_ladder_ratio.md')
