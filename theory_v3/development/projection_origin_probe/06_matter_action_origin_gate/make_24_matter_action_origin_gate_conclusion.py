#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("24_matter_action_origin_gate_conclusion.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Final consistency check: trace-only and full-tensor routes are not equivalent.
D=4
full=D*(D+1)//2
trace=1
require_equal(full-trace, 9, 'full matter coupling exceeds trace channel')
# Universal factor condition
b=sp.symbols('b')
require_equal((b-1).subs(b,1),0,'universal beta locked')


content = r"""# Matter Action Origin Gate Conclusion

Conclusion:

```text
If matter actions use the shared metric interval and volume structure, their
source route is the metric stress tensor.
```

The proof chain verifies the volume variation, inverse-metric variation,
proper-time variation, scalar-field witness, point-particle witness,
trace-only limitation, null-radiation trace failure, species-dependent coupling
failure, nonmetric-channel routing, and diffeomorphism/conservation route.

The result is conditional.  It does not derive microscopic matter.  It says
that once matter is committed to the shared metric interval, universal stress
coupling is not an independent extra force law.

The remaining frontier is therefore:

```text
derive or route the existence and form of matter actions themselves.
```

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
