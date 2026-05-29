import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
rho1,rho2,p1,p2=sp.symbols('rho1 rho2 p1 p2')
Tsum=sp.Matrix([[rho1+rho2,0],[0,p1+p2]])
# many decompositions share same total
md=f"""# 6. Stress Tensor / Matter Ontology No-Go

The stress tensor is an additive source ledger, not a microscopic ontology.

Two matter sectors can combine as

```text
T_total = [[rho1 + rho2, 0], [0, p1 + p2]].
```

Only the sums are visible to the total metric source. The decomposition into
species, charges, masses, or internal states is not recovered from `T_total`
alone.

## Closed result

```text
stress route closed != matter ontology derived.
```
"""
Path('6_stress_does_not_determine_matter_no_go.md').write_text(md)
