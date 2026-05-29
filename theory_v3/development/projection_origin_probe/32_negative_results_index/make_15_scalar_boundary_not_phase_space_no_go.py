import os
os.chdir(os.path.dirname(__file__))

from pathlib import Path
m=3
config=m*(m+1)//2
phase=2*config
scalar_phase=2
gap=phase-scalar_phase
md=f"""# 15. Scalar Boundary Is Not Full Phase Space

A three-dimensional boundary symmetric tensor has

```text
configuration components = {config}
phase-space components = {phase}
```

A scalar trace channel supplies at most one configuration variable and one
canonical partner:

```text
scalar phase components = {scalar_phase}
phase-space gap = {gap}
```

## Closed result

The scalar ladder is a constraint/monopole ledger, not a full boundary
symplectic phase space.
"""
Path('15_scalar_boundary_not_phase_space_no_go.md').write_text(md)
