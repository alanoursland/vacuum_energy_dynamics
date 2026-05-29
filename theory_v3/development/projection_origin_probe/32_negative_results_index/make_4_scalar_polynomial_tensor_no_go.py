import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
phi, eps = sp.symbols('phi eps')
S=phi + eps*phi**2
# scalar polynomial has one coefficient direction per power; cannot encode independent tensor components
m=3
tensor_components=m*(m+1)//2
scalar_components=1
gap=tensor_components-scalar_components
assert gap==5
md=f"""# 4. Scalar Polynomial / Tensor No-Go

Scalar nonlinear dressing produces more scalar powers, not tensor components.

For a 3-dimensional boundary, a symmetric tensor has

```text
m(m+1)/2 = {tensor_components}
```

components. A scalar channel supplies one component. The rank gap is

```text
{tensor_components} - {scalar_components} = {gap}.
```

A scalar polynomial such as

```text
phi + eps phi^2
```

still depends on one scalar variable. It does not create the missing shear,
off-diagonal, or TT data.
"""
Path('4_scalar_polynomial_tensor_no_go.md').write_text(md)
