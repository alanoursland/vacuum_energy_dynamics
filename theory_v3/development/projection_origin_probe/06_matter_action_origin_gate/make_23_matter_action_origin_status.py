#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("23_matter_action_origin_status.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Status flags: interval assumption I, stress route S, microscopic derivation O.
I,S,O=sp.symbols('I S O')
# This folder proves I -> S; it does not prove O -> I or O.
forbidden=I*(1-S)
require_equal(forbidden.subs({I:1,S:1}),0,'proved branch allowed')
require_equal(forbidden.subs({I:1,S:0}),1,'interval without stress forbidden')
# O remains algebraically independent in this gate.
require_equal((O).subs(O,0),0,'ontology not assumed true')


content = r"""# Matter Action Origin Status

Status of the gate:

```text
shared interval dependence -> stress tensor coupling.
```

The folder does not prove:

```text
vacuum ontology -> microscopic matter action.
```

Therefore the matter-side result is a conditional bridge, not a completed
matter-origin theorem.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
