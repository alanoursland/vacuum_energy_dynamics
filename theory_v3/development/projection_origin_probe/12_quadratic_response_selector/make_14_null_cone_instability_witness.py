#!/usr/bin/env python3
"""
Show nonquadratic corrections can alter the null condition away from one fixed cone.

Output:
    14_null_cone_instability_witness.md
"""
from pathlib import Path
import sympy as sp

t,x,eps = sp.symbols('t x eps')
Q_lor = -t**2 + x**2
Q_corr = Q_lor + eps*(t**2 + x**2)**2
on_metric_null = sp.factor(Q_corr.subs(x,t))
if on_metric_null != 4*eps*t**4:
    raise AssertionError(f'unexpected null shift: {on_metric_null}')
if sp.simplify(on_metric_null.subs(eps,0)) != 0:
    raise AssertionError('metric null cone should be restored at eps=0')

md = f"""# Quadratic Response Selector 14: Null-Cone Instability Witness

## Purpose

This proof shows that a nonquadratic correction can move or thicken the null
condition relative to a fixed metric cone.

## Computation

Start with the 1+1 metric branch:

```text
Q_lor = -t^2 + x^2.
```

Add a quartic directional correction:

```text
Q = Q_lor + eps (t^2+x^2)^2.
```

On the original metric null line `x=t`, SymPy finds:

```text
Q(t,t) = {sp.sstr(on_metric_null)}
```

## Interpretation

Unless `eps=0`, the original null cone is no longer a universal zero set of
the response. Nonquadratic response therefore threatens the shared causal cone
unless routed as a separate medium/Finsler correction.
"""

out = Path(__file__).with_name('14_null_cone_instability_witness.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Null-cone instability witness passed.')
print(f'Wrote {out.resolve()}')
