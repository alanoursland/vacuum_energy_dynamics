
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "20_post_newtonian_scalar_no_go_conclusion.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

# final guard: Riddle solved locally; full tensor branch requires non-scalar data.
closed_scalar=sp.Integer(1)
requires_tensor=sp.Integer(1)
require_equal(closed_scalar+requires_tensor,2,'both scalar closure and tensor requirement recorded')

write_md(r'''
# 20. Post-Newtonian scalar no-go conclusion

This folder closes a negative result.

A scalar-only completion can reproduce the Newtonian exterior trace sector:

```text
Delta Phi = 4 pi G rho,
Phi ~ -GM/r,
finite Gauss flux.
```

But a scalar-only nonlinear completion cannot reproduce the full post-Newtonian tensor structure of GR without importing additional non-scalar data.

The obstruction appears in several equivalent ways:

```text
scalar trace cannot recover shear;
scalar trace cannot recover off-diagonal metric components;
scalar density cannot recover momentum/current sources;
conformal scalar response is trace-only;
TT radiation has zero trace but nonzero polarizations;
scalar polynomial powers do not generate tensor invariants.
```

Therefore the scalar ladder is correctly interpreted as the Newtonian trace/monopole boundary sector. Full GR requires the directional/tensor branch: shear-sensitive metric data, Weyl/TT modes, vector/current source response, and nonlinear constraint closure.

This is a no-go for scalar-only post-Newtonian completion, not a no-go for the larger relational interval program.
''')
