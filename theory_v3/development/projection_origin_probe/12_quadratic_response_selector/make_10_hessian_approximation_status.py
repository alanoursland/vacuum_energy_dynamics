#!/usr/bin/env python3
"""
Status after Hessian approximation batch.

Output:
    10_hessian_approximation_status.md
"""
from pathlib import Path
required = [
    '6_hessian_local_quadratic_sector.md',
    '7_stationary_point_first_variation_gate.md',
    '8_higher_order_remainder_witness.md',
    '9_homogeneity_degree_two_gate.md',
]
missing = [name for name in required if not Path(__file__).with_name(name).exists()]
if missing:
    raise AssertionError(f'missing prerequisite reports: {missing}')

md = """# Quadratic Response Selector 10: Hessian Approximation Status

## Status

The second batch separates two claims:

```text
smooth stationary response -> local Hessian quadratic sector
```

versus

```text
exact interval geometry -> exact quadratic / degree-two homogeneous response.
```

The first is broadly available. The second is the actual metric selector.

## Consequence

A parent ontology that supplies only a local Hessian has not yet supplied a
pseudo-Riemannian metric theory. It has supplied a quadratic approximation plus
unrouted higher-order terms.
"""

out = Path(__file__).with_name('10_hessian_approximation_status.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Hessian approximation status passed.')
print(f'Wrote {out.resolve()}')
