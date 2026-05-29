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

# Normalization cannot change R

y, R, c = sp.symbols('y R c', positive=True)
weight = (1-y)**(R+1)*y**sp.Rational(-1,2)
scaled = c*weight
# log derivative near endpoint with respect to (1-y) ignores multiplicative constant.
# Compute d log(weight)/d log(1-y) = R+1.
t = sp.symbols('t', positive=True)
w_t = c*t**(R+1)  # y factors regular in this endpoint witness
exp = sp.simplify(t*sp.diff(w_t,t)/w_t)
require_equal(exp, R+1, 'multiplicative normalization preserves exponent')


write_report('13_normalization_cannot_change_R.md', r'''
# 13. Normalization cannot change R

A global multiplicative normalization of the moment functional cannot change
the endpoint exponent.  For a boundary factor

```text
c (1-y)^(R+1),
```

the logarithmic exponent is

```text
(1-y) d/d(1-y) log[c(1-y)^(R+1)] = R+1.
```

Thus `R` is insensitive to overall constants, but sensitive to endpoint-contact
factors and field/test normalizations.

''')
print('wrote 13_normalization_cannot_change_R.md')
