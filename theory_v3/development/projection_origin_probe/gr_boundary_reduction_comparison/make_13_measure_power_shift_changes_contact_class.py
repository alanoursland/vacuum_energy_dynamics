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

k, R, S = sp.symbols('k R S', positive=True, integer=True)
ratio_R = (2*k-1)/(2*k+2*R+3)
ratio_S = (2*k-1)/(2*k+2*S+3)
# Equality for all k requires R=S.
condition = sp.solve(sp.Eq(2*k+2*R+3, 2*k+2*S+3), R)[0]
require_equal(condition, S, 'same ratio ladder iff same contact class')

write_report('13_measure_power_shift_changes_contact_class.md', r'''
# 13. Measure power shift changes contact class

The generalized contact ladder is

```text
r_(R,k) = (2k-1)/(2k+2R+3).
```

Two contact classes produce the same ratio for all `k` only if

```text
R = S.
```

Interpretation: unlike constant normalization, changing the endpoint-contact
power changes the admissibility class. This is the meaningful comparison point
against a GR reduction.
''')
print('wrote', '13_measure_power_shift_changes_contact_class.md')
