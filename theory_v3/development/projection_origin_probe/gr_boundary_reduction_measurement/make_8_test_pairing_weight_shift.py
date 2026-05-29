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

# Test-pairing weight shift

y, R, sigma = sp.symbols('y R sigma', positive=True)
base_weight = (1-y)**(R+1)*y**sp.Rational(-1,2)
shifted_weight = sp.simplify((1-y)**sigma * base_weight)
expected = (1-y)**(R+sigma+1)*y**sp.Rational(-1,2)
require_equal(shifted_weight, expected, 'test weight contact exponent shifts R')


write_report('8_test_pairing_weight_shift.md', r'''
# 8. Test-pairing weight shift

The projection ladder is defined by a moment functional

```text
C_R[P] = ∫ P(y) (1-y)^(R+1) y^(-1/2) dy.
```

Multiplying the test/source pairing by an extra endpoint-contact factor

```text
(1-y)^σ
```

shifts the ladder to

```text
R -> R + σ.
```

Validated identity:

```text
(1-y)^σ (1-y)^(R+1) y^(-1/2)
= (1-y)^(R+σ+1) y^(-1/2).
```

This shows why `R` is a property of the chosen compactified pairing, not of the
physical exterior flux alone.

''')
print('wrote 8_test_pairing_weight_shift.md')
