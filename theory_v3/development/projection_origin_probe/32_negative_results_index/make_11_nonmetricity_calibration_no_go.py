import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
lam,s=sp.symbols('lam s')
scale=sp.exp(lam*s)
series=sp.series(scale,s,0,3).removeO()
md=f"""# 11. Nonmetricity Calibration Drift No-Go

A Weyl-like nonmetric scale drift changes local calibration under transport.

For a scale factor

```text
a(s)=exp(lambda s)
```

the expansion is

```text
{series}
```

Unless `lambda=0` or the drift is explicitly routed as an additional physical
channel, transported interval calibration is path/scale dependent.

## Closed result

Nonmetricity cannot be hidden inside the Levi-Civita metric branch.
"""
Path('11_nonmetricity_calibration_no_go.md').write_text(md)
