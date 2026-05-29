#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("6_point_particle_stress_density.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

m,s=sp.symbols('m s', positive=True)
v0,v1,h00,h01,h11=sp.symbols('v0 v1 h00 h01 h11')
hvv=h00*v0**2+2*h01*v0*v1+h11*v1**2
dS=-m*hvv/(2*s)
# identify coefficient of h_ab as -1/2 T^{ab}; T proportional m v^a v^b/s
T00=m*v0**2/s; T01=m*v0*v1/s; T11=m*v1**2/s
expected=-sp.Rational(1,2)*(T00*h00+2*T01*h01+T11*h11)
require_equal(dS, expected, 'point particle stress coefficients')


content = r"""# Point Particle Stress Density

For a point particle, proper-time variation gives stress proportional to

```text
m v^a v^b / s.
```

This is the localized matter version of the same gate: once the particle clock
uses the shared metric interval, the metric source coefficient is no longer
independent.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
