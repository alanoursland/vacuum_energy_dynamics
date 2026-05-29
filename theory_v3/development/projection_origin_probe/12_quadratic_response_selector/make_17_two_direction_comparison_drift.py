#!/usr/bin/env python3
"""
Show anisotropic nonquadratic response produces direction-dependent calibration shifts.

Output:
    17_two_direction_comparison_drift.md
"""
from pathlib import Path
import sympy as sp

s, eps1, eps2 = sp.symbols('s eps1 eps2')
Qx = s**2 + eps1*s**4
Qy = s**2 + eps2*s**4
rx = sp.simplify(Qx/s**2)
ry = sp.simplify(Qy/s**2)
diff = sp.simplify(rx - ry)
if diff != s**2*(eps1-eps2):
    raise AssertionError(f'unexpected direction drift: {diff}')
if sp.simplify(diff.subs(eps1,eps2)) != 0:
    raise AssertionError('matched nonlinear coefficients should remove anisotropic drift')

md = f"""# Quadratic Response Selector 17: Two-Direction Comparison Drift

## Purpose

This proof checks whether two directions can keep the same calibration when
nonquadratic corrections differ by direction.

## Computation

For

```text
Qx(s)=s^2+eps1 s^4
Qy(s)=s^2+eps2 s^4,
```

the normalized calibration difference is:

```text
Qx/s^2 - Qy/s^2 = {sp.sstr(diff)}
```

## Interpretation

Direction-dependent higher response creates anisotropic calibration drift. A
single shared metric branch requires these effects to vanish or be routed as
explicit nonmetric structure.
"""

out = Path(__file__).with_name('17_two_direction_comparison_drift.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Two-direction comparison drift passed.')
print(f'Wrote {out.resolve()}')
