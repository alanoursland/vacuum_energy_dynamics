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

# Projection base class R=0

k, R = sp.symbols('k R', positive=True, integer=True)
rR = (2*k-1)/(2*k+2*R+3)
r0 = sp.simplify(rR.subs(R,0))
expected = (2*k-1)/(2*k+3)
require_equal(r0, expected, 'R=0 projection ratio')


write_report('11_projection_base_class_R0.md', r'''
# 11. Projection base class R = 0

The observed projection-origin coefficient is the `R=0` base case:

```text
r_(0,k) = (2k - 1)/(2k + 3).
```

This is the class the GR scalar reduction must be compared against after the
same projection variable and moment pairing have been chosen.

''')
print('wrote 11_projection_base_class_R0.md')
