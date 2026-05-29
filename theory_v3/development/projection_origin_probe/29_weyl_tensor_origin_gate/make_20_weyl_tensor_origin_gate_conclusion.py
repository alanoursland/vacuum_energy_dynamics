#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('20_weyl_tensor_origin_gate_conclusion.md')
def require_zero(expr, name='expr'):
    if sp.simplify(expr) != 0:
        raise AssertionError(f"{name} not zero: {sp.simplify(expr)}")
def require(cond, name='condition'):
    if not bool(cond):
        raise AssertionError(f"failed: {name}")
def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

md = """# 20. Weyl Tensor Origin Gate — Conclusion

This folder closes the local tensor-data part of the Weyl-origin question.

Closed:

```text
directional quadratic interval probes reconstruct symmetric tensor data;
trace projection extracts only the scalar/isotropic sector;
traceless shear/tidal data is invisible to scalar trace but visible to directional probes;
vacuum trace can vanish while trace-free tidal data remains;
TT witnesses are trace-free, divergence-free, and non-scalar.
```

Not closed:

```text
free Weyl dynamics;
TT propagation;
boundary news/memory law;
full nonlinear constraint closure.
```

Therefore the result is:

```text
Directional quadratic probes are sufficient to supply local traceless/Weyl-like tensor data.
They are not, by themselves, sufficient to derive full Weyl/TT dynamics.
```

This folder bridges the gap between scalar-boundary blindness and tensor geometry. It justifies moving from the scalar r_k ledger to directional metric/shear data, while keeping the radiative/dynamical Weyl sector assigned to transport, symplectic, and constraint-closure folders.
"""

write_md(md)
