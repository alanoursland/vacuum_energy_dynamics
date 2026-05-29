#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
r,Q,Omega=sp.symbols('r Q Omega', positive=True)
F=Q/(Omega*r**2)
flux=sp.simplify(Omega*r**2*F)
assert flux==Q

REPORT = r"""
# 5. Boundary Reduction Interface Status

## Claim

The boundary is a reduction/ledger interface. Conserved radial flux records
source content without being the underlying ontology.

## SymPy check

For a three-dimensional radial field

```text
F(r) = Q/(Omega r^2),
```

the enclosing flux is

```text
Omega r^2 F(r) = Q.
```

## Ledger status

Closed as a boundary ledger fact. It does not decide what local/bulk/relational
structure generated the flux.
"""

Path(__file__).with_name('5_boundary_reduction_interface_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 5_boundary_reduction_interface_status.md')
