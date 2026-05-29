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

# Different R witness

k = sp.symbols('k', positive=True, integer=True)
r0 = (2*k-1)/(2*k+3)
r1 = (2*k-1)/(2*k+5)
diff = sp.simplify(r1-r0)
expected = sp.simplify(-2*(2*k-1)/((2*k+3)*(2*k+5)))
require_equal(diff, expected, 'R=1 differs from R=0')
require_equal(r0.subs(k,1), sp.Rational(1,5), 'k=1 R=0 witness')
require_equal(r1.subs(k,1), sp.Rational(1,7), 'k=1 R=1 witness')


write_report('12_different_R_witness.md', r'''
# 12. Different-R witness

If the GR reduction landed in `R=1` instead of `R=0`, the first ratio would be

```text
R=0: r_(0,1) = 1/5,
R=1: r_(1,1) = 1/7.
```

Validated difference:

```text
r_(1,k) - r_(0,k)
= -2(2k-1)/[(2k+3)(2k+5)].
```

So a genuine contact-class mismatch would be directly visible in the projection
coefficient.

''')
print('wrote 12_different_R_witness.md')
