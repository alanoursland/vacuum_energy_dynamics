#!/usr/bin/env python3
"""
Validate that scalar trace projection cannot see traceless shear.

Output:
    23_scalar_trace_projection_limit.md
"""
from pathlib import Path
import sympy as sp

phi,s = sp.symbols('phi s')
# 2D symmetric perturbation decomposed into trace phi and shear s.
h11 = phi + s
h22 = phi - s
trace = sp.simplify(h11 + h22)
shear_difference = sp.simplify(h11 - h22)
if trace != 2*phi:
    raise AssertionError(f'trace mismatch: {trace}')
if sp.diff(trace,s) != 0:
    raise AssertionError('trace should be blind to shear')
if shear_difference != 2*s:
    raise AssertionError('shear witness mismatch')

md = f"""# Quadratic Response Selector 23: Scalar Trace Projection Limit

## Purpose

This proof rechecks the historical limitation of the scalar projection ladder:
trace data cannot recover shear/traceless metric data.

## Computation

Use

```text
h11 = phi + s
h22 = phi - s.
```

Then:

```text
trace = h11+h22 = {sp.sstr(trace)}
d(trace)/ds = {sp.sstr(sp.diff(trace,s))}
h11-h22 = {sp.sstr(shear_difference)}
```

## Interpretation

The scalar ladder can detect the isotropic trace sector. It cannot prove exact
directional quadratic response or recover the full metric tensor by itself.
"""

out = Path(__file__).with_name('23_scalar_trace_projection_limit.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Scalar trace projection limit passed.')
print(f'Wrote {out.resolve()}')
