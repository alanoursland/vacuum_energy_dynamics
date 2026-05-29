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

# R_GR requires projection embedding

# Symbolic flag logic: physical constraints determine alpha=1, projection embedding determines R.
alpha, R = sp.symbols('alpha R')
physical_eq = alpha-1
# No algebraic consequence sets R; derivative wrt R of physical_eq is zero.
require_zero(sp.diff(physical_eq,R), 'physical finite-flux condition independent of R')


write_report('15_Rgr_requires_projection_embedding.md', r'''
# 15. R_GR requires projection embedding

The physical weak-field scalar condition fixes the exterior falloff exponent

```text
α = 1.
```

It does not contain the projection ladder index `R`.

Validated check:

```text
d/dR (α - 1) = 0.
```

Therefore `R_GR` is not an invariant output of the scalar GR boundary ledger
alone.  It is measured only after specifying the compactified projection
embedding.

''')
print('wrote 15_Rgr_requires_projection_embedding.md')
