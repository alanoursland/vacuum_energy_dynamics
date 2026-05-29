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

k, Rgr = sp.symbols('k Rgr', positive=True, integer=True)
r_proj = (2*k-1)/(2*k+3)
r_gr = (2*k-1)/(2*k+2*Rgr+3)
# The difference numerator is -2 Rgr (2k-1), so equality for all k requires Rgr=0.
num = sp.factor(sp.together(r_gr-r_proj).as_numer_denom()[0])
require_equal(num, -2*Rgr*(2*k-1), 'GR contact class difference numerator')
require_zero(num.subs(Rgr,0), 'same universality at Rgr=0')

write_report('14_gr_boundary_same_universality_condition.md', r'''
# 14. GR same-universality condition

If the weak-field GR reduction lands in the same compactified contact ladder,
then matching the projection-origin base ratio requires

```text
r_GR(k) = r_proj(k)
```

for all `k`. With

```text
r_GR(k)=(2k-1)/(2k+2R_GR+3),
r_proj(k)=(2k-1)/(2k+3),
```

the condition is

```text
R_GR = 0.
```

Interpretation: the finite comparison is not vague. It asks whether GR's
reduced scalar boundary problem lands in the same base contact class after
normalization.
''')
print('wrote', '14_gr_boundary_same_universality_condition.md')
