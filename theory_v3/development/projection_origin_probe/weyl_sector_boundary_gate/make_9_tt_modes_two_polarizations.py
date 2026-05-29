#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('9_tt_modes_two_polarizations.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


D=sp.symbols('D', integer=True, positive=True)
N=sp.simplify(D*(D-3)/2)
require_zero(N.subs(D,4)-2,'D4 TT count')
require_zero(N.subs(D,3),'D3 TT count')


md = f"""# 9. Two TT polarizations in D=4

## Checked identities

The massless spin-2 polarization count

```text
D(D-3)/2
```

gives `2` in `D=4` and `0` in `D=3`.

## Conclusion

The radiative GR sector has tensor polarizations absent from scalar boundary flux accounting.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
