import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
D=sp.symbols('D')
N=D*(D-3)/2
solutions=sp.solve(sp.Eq(N,2),D)
md=f"""# 13. Dimension From Pure Logic No-Go

The two-polarization selector gives `D=4` only after importing the massless
spin-2/diffeomorphism framework.

The count is

```text
D(D-3)/2 = 2
```

with solutions

```text
{solutions}
```

## Closed result

`D=4` is selected under the spin-2/two-polarization branch assumptions, not
from pure scalar boundary logic alone.
"""
Path('13_dimension_pure_logic_no_go.md').write_text(md)
