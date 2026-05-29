#!/usr/bin/env python3
"""
Show degree-four corrections create scale-dependent calibration ratios.

Output:
    16_calibration_scale_drift_gate.md
"""
from pathlib import Path
import sympy as sp

s, eps = sp.symbols('s eps')
Q = s**2 + eps*s**4
ratio = sp.simplify(Q / s**2)
drift = sp.simplify(ratio - ratio.subs(s,1))
if sp.simplify(drift) == 0:
    raise AssertionError('scale drift unexpectedly vanished')
if sp.simplify(drift.subs(eps,0)) != 0:
    raise AssertionError('quadratic limit should have no scale drift')

md = f"""# Quadratic Response Selector 16: Calibration Scale Drift Gate

## Purpose

This proof checks whether a nonquadratic response preserves a scale-independent
interval calibration.

## Computation

For a one-direction response:

```text
Q(s) = s^2 + eps s^4,
```

the normalized ratio is:

```text
Q(s)/s^2 = {sp.sstr(ratio)}
```

Compared to the unit calibration, the drift is:

```text
{sp.sstr(drift)}
```

## Interpretation

A quartic correction makes calibration depend on probe scale. Exact metric
response avoids this because it is homogeneous of degree two.
"""

out = Path(__file__).with_name('16_calibration_scale_drift_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Calibration scale drift gate passed.')
print(f'Wrote {out.resolve()}')
