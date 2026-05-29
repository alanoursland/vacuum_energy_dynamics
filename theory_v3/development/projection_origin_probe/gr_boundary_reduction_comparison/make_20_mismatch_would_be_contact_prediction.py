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
r0 = (2*k-1)/(2*k+3)
rR = (2*k-1)/(2*k+2*R+3)
# Difference vanishes iff R=0.
diff_num = sp.factor(sp.together(rR-r0).as_numer_denom()[0])
require_equal(diff_num, -2*R*(2*k-1), 'mismatch numerator')

write_report('20_mismatch_would_be_contact_prediction.md', r'''
# 20. Mismatch would be a contact prediction

The difference between a general contact class and the projection base class is

```text
r_(R,k)-r_(0,k)
```

with numerator

```text
-2R(2k-1).
```

Thus mismatch vanishes only for `R=0`.

Interpretation: if GR's normalized scalar boundary reduction produced `R≠0`,
the project would have found a genuine boundary-condition difference.
''')
print('wrote', '20_mismatch_would_be_contact_prediction.md')
