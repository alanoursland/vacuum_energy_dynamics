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

x, y, j = sp.symbols('x y j', positive=True)
# y=x^2 gives dy=2x dx; x^(2j)*(1-x^2) dx -> 1/2 y^j (1-y)y^(-1/2) dy.
expr_x_measure_to_y = sp.simplify(sp.Rational(1,2)*y**j*(1-y)*y**(-sp.Rational(1,2)))
expected = sp.Rational(1,2)*y**(j-sp.Rational(1,2))*(1-y)
require_equal(expr_x_measure_to_y, expected, 'y=x^2 Jacobian weight')

write_report('11_compactification_weight_convention_gate.md', r'''
# 11. Compactification weight convention gate

Under

```text
y=x²,
```

a radial even-power moment in `x` maps to a beta-type moment in `y` with the
Jacobian factor

```text
dx = (1/2)y^{-1/2}dy.
```

Thus the displayed compactified weight

```text
(1-y)y^{-1/2}
```

contains both endpoint contact and variable/Jacobian convention.

Interpretation: raw displayed weights are not by themselves invariant physical
objects. The invariant comparison target is the admissibility functional after
variable normalization.
''')
print('wrote', '11_compactification_weight_convention_gate.md')
