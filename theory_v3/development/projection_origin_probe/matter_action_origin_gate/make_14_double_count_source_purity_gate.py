#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("14_double_count_source_purity_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

T,h,lam=sp.symbols('T h lam')
metric_source=T*h
aux_copy=lam*T*h
total=(1+lam)*T*h
# Count-once requires lam=0 for equality with metric source.
require_equal(total-metric_source, lam*T*h, 'duplicate source residual')


content = r"""# Double-Count Source Purity Gate

If the same stress tensor is inserted both through the metric route and an
auxiliary copy, the source is duplicated by a factor `λ`.

Count-once source purity requires the auxiliary copy to vanish or be physically
independent and explicitly routed.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
