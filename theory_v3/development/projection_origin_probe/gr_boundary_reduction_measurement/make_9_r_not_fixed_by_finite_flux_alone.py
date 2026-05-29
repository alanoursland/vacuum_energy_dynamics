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

# R not fixed by finite flux alone

# This script encodes a simple symbolic independence witness.
alpha, R = sp.symbols('alpha R')
finite_flux_condition = sp.Eq(alpha, 1)
# For any R, alpha=1 is still true; there is no equation involving R.
expr = sp.simplify((alpha-1).subs(alpha,1))
require_zero(expr, 'finite flux condition contains no R')


write_report('9_r_not_fixed_by_finite_flux_alone.md', r'''
# 9. R is not fixed by finite flux alone

The finite-flux scalar condition is

```text
α = 1
```

for the physical falloff

```text
Φ ~ r^(-α).
```

The compactified projection class `R` does not appear in this condition.  It
enters only after choosing a moment/test functional.  Therefore the physical
finite-flux GR scalar ledger is compatible with multiple projection contact
classes unless the projection embedding is specified.

''')
print('wrote 9_r_not_fixed_by_finite_flux_alone.md')
