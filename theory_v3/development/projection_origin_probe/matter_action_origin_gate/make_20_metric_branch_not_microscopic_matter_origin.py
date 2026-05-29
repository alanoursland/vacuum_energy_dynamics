#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("20_metric_branch_not_microscopic_matter_origin.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Logical flag algebra: metric dependence implies stress route, but not existence of a matter action.
M,S=sp.symbols('M S')
# Let M=1 mean matter action exists and uses metric; S=1 stress route exists.
# Implication M -> S is encoded by forbidden state M=1,S=0.
forbidden = M*(1-S)
# The state M=0,S=0 is allowed: no matter action, no stress route.
require_equal(forbidden.subs({M:0,S:0}), 0, 'no matter no stress allowed')
require_equal(forbidden.subs({M:1,S:1}), 0, 'metric matter stress allowed')
require_equal(forbidden.subs({M:1,S:0}), 1, 'metric matter without stress forbidden witness')


content = r"""# Metric Branch Not Microscopic Matter Origin

This script records the logical status of the folder.  Metric matter action
implies a stress route, but the implication does not derive the existence of
matter:

```text
matter uses metric interval -> stress coupling.
```

The converse is not proved here, and microscopic matter ontology remains open.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
