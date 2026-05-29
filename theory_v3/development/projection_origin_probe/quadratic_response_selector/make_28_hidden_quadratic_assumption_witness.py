#!/usr/bin/env python3
"""
Show how setting nonquadratic coefficients to zero before testing hides the key assumption.

Output:
    28_hidden_quadratic_assumption_witness.md
"""
from pathlib import Path
import sympy as sp

x,y,eps = sp.symbols('x y eps')
Q_full = x**2 + y**2 + eps*(x**2+y**2)**2
Q_hidden = Q_full.subs(eps,0)
# Test parallelogram on a witness pair.
def P(Q):
    # x-vector=(1,0), y-vector=(1,0) using variables not needed for witness.
    def evalQ(a,b):
        return Q.subs({x:a,y:b})
    return sp.simplify(evalQ(2,0) + evalQ(0,0) - 2*evalQ(1,0) - 2*evalQ(1,0))
full_res = P(Q_full)
hidden_res = P(Q_hidden)
if full_res != 12*eps:
    raise AssertionError(f'unexpected full residual: {full_res}')
if hidden_res != 0:
    raise AssertionError(f'hidden residual should pass after eps=0: {hidden_res}')

md = f"""# Quadratic Response Selector 28: Hidden Quadratic Assumption Witness

## Purpose

This proof shows how the metric branch can be smuggled: set the nonquadratic
coefficient to zero before testing the response.

## Computation

For

```text
Q_full = x^2+y^2+eps(x^2+y^2)^2,
```

a simple parallelogram witness gives:

```text
full residual = {sp.sstr(full_res)}
```

If `eps=0` is imposed first, the same test gives:

```text
hidden residual = {sp.sstr(hidden_res)}
```

## Interpretation

The project must not silently set higher directional response to zero. That is
the central selector, not a harmless simplification.
"""

out = Path(__file__).with_name('28_hidden_quadratic_assumption_witness.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Hidden quadratic assumption witness passed.')
print(f'Wrote {out.resolve()}')
