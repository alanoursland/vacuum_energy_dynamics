import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
B,U=sp.symbols('B U')
# truth table possible: B True and U False not contradiction
md="""# 8. Same Boundary Does Not Mean No Ontology Work

Matching a GR-compatible scalar boundary ledger does not prove the vacuum
ontology is idle.

It only says the ontology is not doing distinctive work inside the already
reduced scalar boundary algebra.

The possible upstream work remains:

```text
quadratic metric branch,
calibration-coherent transport,
EH/GHY variational selection,
matter interval coupling,
Weyl/TT tensor sector.
```

## Closed result

```text
same reduced boundary != no upstream assumption reduction.
```
"""
Path('8_same_boundary_not_no_ontology_no_go.md').write_text(md)
