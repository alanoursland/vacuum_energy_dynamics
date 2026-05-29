#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('16_memory_as_tensor_boundary_shift.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


cp,cx=sp.symbols('Delta_plus Delta_cross')
Delta=sp.Matrix([[cp,cx],[cx,-cp]])
require_zero(sp.trace(Delta),'memory trace')
inv=sp.trace(Delta*Delta)
require_zero(sp.simplify(inv-2*(cp**2+cx**2)),'memory invariant')


md = f"""# 16. Memory as tensor boundary shift

## Checked identities

A permanent tensor boundary shift of trace-free form has zero scalar trace but nonzero quadratic size.

## Conclusion

Memory-type boundary effects are tensorial shifts, not scalar monopole charge changes.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
