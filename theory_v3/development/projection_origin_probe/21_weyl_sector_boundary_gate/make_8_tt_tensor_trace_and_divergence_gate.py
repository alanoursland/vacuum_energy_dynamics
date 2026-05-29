#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('8_tt_tensor_trace_and_divergence_gate.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


k,hp,hx=sp.symbols('k hp hx')
# Plane wave along z with spatial tensor in x/y plane
H=sp.Matrix([[hp,hx,0],[hx,-hp,0],[0,0,0]])
require_zero(sp.trace(H),'TT trace')
# divergence k_j H_ij for k along z = k * H_i3
for i in range(3):
    require_zero(k*H[i,2], f'TT divergence component {i}')
invariant=sp.simplify(sp.trace(H*H))
require_zero(invariant-2*(hp**2+hx**2),'TT invariant')


md = f"""# 8. TT tensor trace/divergence gate

## Checked identities

A plane-wave TT witness propagating along `z` was checked:

```text
H = [[h_+, h_x, 0], [h_x, -h_+, 0], [0,0,0]].
```

It has zero trace and zero longitudinal divergence, but nonzero invariant `2(h_+^2+h_x^2)`.

## Conclusion

TT radiative data is invisible to scalar trace projection while carrying real tensor content.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
