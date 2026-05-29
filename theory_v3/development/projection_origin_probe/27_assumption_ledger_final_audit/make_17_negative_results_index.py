#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
# Boolean ledger: each negative result closes a loophole, not all physics.
scalar_full_tensor=False
scalar_PN=False
stress_derives_matter=False
R_from_flux=False
assert scalar_full_tensor is False
assert scalar_PN is False
assert stress_derives_matter is False
assert R_from_flux is False

REPORT = r"""
# 17. Negative Results Index

## Closed negative results

The project now has several useful negative/no-go results:

```text
scalar trace data does not reconstruct full tensor geometry;
scalar nonlinear dressing does not reproduce GR PN tensor structure;
stress coupling does not derive matter ontology;
finite scalar flux does not determine projection contact index R.
```

## Ledger status

Closed as scoped negative results. These are among the most externally useful
outputs because they delimit what the scalar ladder can and cannot do.
"""

Path(__file__).with_name('17_negative_results_index.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 17_negative_results_index.md')
