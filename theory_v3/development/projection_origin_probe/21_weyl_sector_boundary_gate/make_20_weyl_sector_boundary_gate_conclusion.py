#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('20_weyl_sector_boundary_gate_conclusion.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


# Summary consistency checks
m=sp.Integer(3)
missing=m*(m+1)/2-1
require_zero(missing-5,'missing boundary tensor components')
D=sp.Integer(4)
weyl=D*(D+1)*(D+2)*(D-3)/12
require_zero(weyl-10,'4D Weyl components')
TT=D*(D-3)/2
require_zero(TT-2,'4D TT modes')


md = f"""# 20. Weyl sector boundary gate conclusion

## Checked identities

The concluding checks collect three facts:

```text
3D boundary tensor missing-from-scalar components = 5,
4D Weyl components = 10,
4D TT polarizations = 2.
```

## Conclusion

The scalar `r_k` boundary ladder captures the trace/monopole/Newtonian sector. The Weyl/TT/radiative sector requires tensorial directional boundary data, shear-sensitive probes, or boundary symplectic/radiative flux. The scalar boundary is blind only because it is scalar, not because all boundaries are blind.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
