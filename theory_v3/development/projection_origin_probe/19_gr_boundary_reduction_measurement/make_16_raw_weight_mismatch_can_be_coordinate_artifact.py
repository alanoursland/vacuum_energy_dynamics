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

# Raw weight mismatch can be coordinate artifact

y, z, R = sp.symbols('y z R', positive=True)
# y = z^2. Pushforward of y^(-1/2) dy is 2 dz; raw weight changes.
expr = sp.simplify((z**2)**sp.Rational(-1,2) * sp.diff(z**2,z))
require_equal(expr, 2, 'y^(-1/2) dy becomes 2 dz under y=z^2')


write_report('16_raw_weight_mismatch_can_be_coordinate_artifact.md', r'''
# 16. Raw weight mismatch can be a coordinate artifact

Under the change

```text
y = z²,
```

the factor

```text
y^(-1/2) dy
```

pushes forward to

```text
2 dz.
```

Validated identity:

```text
(z²)^(-1/2) d(z²) = 2 dz.
```

So comparing raw displayed weights is not sufficient.  The invariant comparison
must track the full variable map, test space, and endpoint-contact class.

''')
print('wrote 16_raw_weight_mismatch_can_be_coordinate_artifact.md')
