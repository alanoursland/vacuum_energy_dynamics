#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('18_weyl_not_fixed_by_ricci_trace.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


D=sp.Integer(4)
riem=D**2*(D**2-1)/12
ricci=D*(D+1)/2
scalar=1
weyl=riem-ricci
trace_blind=riem-scalar
require_zero(weyl-10,'Weyl count')
require_zero(trace_blind-19,'Riemann minus scalar trace')


md = f"""# 18. Weyl not fixed by Ricci trace count

## Checked identities

In `D=4`, scalar trace information is one component. Riemann has `20`, Ricci has `10`, and Weyl has `10`.

## Conclusion

A scalar trace ledger cannot determine the full Ricci tensor, much less the Weyl tensor.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
