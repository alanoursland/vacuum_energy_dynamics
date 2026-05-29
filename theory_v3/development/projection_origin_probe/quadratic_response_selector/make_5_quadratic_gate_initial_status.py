#!/usr/bin/env python3
"""
Initial status after exact quadratic metric gate.

Output:
    5_quadratic_gate_initial_status.md
"""
from pathlib import Path

required = [
    '1_parallelogram_identity_quadratic_gate.md',
    '2_polarization_recovers_bilinear_form.md',
    '3_bilinear_axioms_from_parallelogram.md',
    '4_quadratic_gate_not_metric_ontology_derivation.md',
]
missing = [name for name in required if not Path(__file__).with_name(name).exists()]
if missing:
    raise AssertionError(f'missing prerequisite reports: {missing}')

md = """# Quadratic Response Selector 5: Quadratic Gate Initial Status

## Status

The first batch closes the algebraic metric gate:

```text
exact quadratic response
  -> parallelogram law
  -> polarization reconstruction
  -> symmetric bilinear metric-like form.
```

## Important Limitation

This does not yet prove that the vacuum interval response is exact quadratic.
It only proves that exact quadraticity is sufficient for the metric branch and
that the metric branch should not be used upstream of this gate.

## Next Step

Separate exact metric response from the weaker statement that any smooth
response has a local Hessian approximation near a reference state.
"""

out = Path(__file__).with_name('5_quadratic_gate_initial_status.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Quadratic initial status passed.')
print(f'Wrote {out.resolve()}')
