#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('3_traceless_matrix_scalar_probe_zero.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


a,b=sp.symbols('a b')
T=sp.Matrix([[a,0,0],[0,b,0],[0,0,-a-b]])
require_zero(sp.trace(T), 'traceless witness trace')
invariant=sp.simplify(sp.trace(T*T))
if sp.simplify(invariant)==0:
    raise AssertionError('nonzero invariant collapsed')


md = f"""# 3. Traceless matrix scalar probe zero

## Checked identities

A traceless witness

```text
diag(a, b, -a-b)
```

has zero scalar trace but nonzero quadratic invariant `Tr(T^2)`.

## Conclusion

Trace-only data can report zero while genuine traceless tensor content remains present.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
