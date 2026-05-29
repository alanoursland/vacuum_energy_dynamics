#!/usr/bin/env python3
"""
Status after nonquadratic obstruction witnesses.

Output:
    15_nonquadratic_branch_status.md
"""
from pathlib import Path
required = [
    '11_quartic_finsler_obstruction_witness.md',
    '12_nonquadratic_polarization_failure.md',
    '13_direction_dependent_metric_witness.md',
    '14_null_cone_instability_witness.md',
]
missing = [name for name in required if not Path(__file__).with_name(name).exists()]
if missing:
    raise AssertionError(f'missing prerequisite reports: {missing}')

md = """# Quadratic Response Selector 15: Nonquadratic Branch Status

## Status

The third batch gives explicit obstruction witnesses:

```text
quartic directional correction
  -> parallelogram failure
  -> polarization contamination
  -> direction-dependent effective metric
  -> possible null-cone drift.
```

## Interpretation

Nonquadratic response is not automatically inconsistent, but it is not the
pseudo-Riemannian metric branch. It must be treated as an explicit Finsler-like,
medium-like, or higher-response branch unless later ontology excludes it.
"""

out = Path(__file__).with_name('15_nonquadratic_branch_status.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Nonquadratic branch status passed.')
print(f'Wrote {out.resolve()}')
