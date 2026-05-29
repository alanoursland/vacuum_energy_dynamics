
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "14_source_motion_not_density_only.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

rho, vx, vy, vz = sp.symbols('rho vx vy vz')
T00=rho
T0x=rho*vx
# density-only scalar knows rho, not vx.
require_zero(sp.diff(T00,vx),'density source does not encode velocity')
require_equal(sp.diff(T0x,vx), rho, 'momentum source depends on velocity')

write_md(r'''
# 14. Source motion not density-only gate

Post-Newtonian structure depends not only on mass density but also on momentum/current source components:

```text
T_00 ~ rho,
T_0i ~ rho v_i.
```

A density-only scalar source does not encode these current components.
''')
