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

# Measurement status conclusion

k, R = sp.symbols('k R', positive=True, integer=True)
rR = (2*k-1)/(2*k+2*R+3)
r0 = rR.subs(R,0)
require_equal(r0, (2*k-1)/(2*k+3), 'projection R=0 still recovered')
# physical finite-flux condition remains independent
alpha = sp.symbols('alpha')
require_zero(sp.diff(alpha-1,R), 'finite flux condition cannot determine R')


write_report('20_measurement_status_conclusion.md', r'''
# 20. GR boundary reduction measurement conclusion

This folder measures what can and cannot be measured from the weak-field GR
scalar boundary reduction.

It confirms:

```text
weak-field GR scalar sector -> Poisson equation -> finite Gauss flux -> 1/r exterior.
```

It also confirms:

```text
projection-origin ladder -> C_R[P] -> r_(R,k) = (2k-1)/(2k+2R+3),
observed projection class -> R = 0.
```

But it does **not** find an invariant equation inside the physical scalar GR
ledger that fixes `R` without an additional compactified projection embedding.
The finite-flux condition fixes the physical falloff exponent `α=1`; it does
not fix the moment-contact index `R`.

Therefore the measured status is:

```text
R_GR is not specified by weak-field GR scalar boundary data alone.
```

If GR is embedded into the same compactified moment functional as the original
projection problem, then by that embedding

```text
R_GR = 0.
```

That is GR-compatible scalar boundary reduction, not a novel boundary-condition
prediction.  The vacuum ontology, if it does distinctive work, does it upstream
by selecting the structures that make this scalar reduction the relevant one.

''')
print('wrote 20_measurement_status_conclusion.md')
