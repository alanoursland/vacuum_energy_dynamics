#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('5_higher_multipole_zero_net_flux.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


r=sp.symbols('r', positive=True)
mu=sp.symbols('mu')
for ell in range(1,6):
    phi=sp.legendre(ell,mu)/r**(ell+1)
    radial_flux_density=sp.diff(phi,r)*r**2
    net=sp.integrate(radial_flux_density,(mu,-1,1))
    require_zero(net, f'net flux ell={ell}')
# ell=0 has nonzero flux
phi0=1/r
net0=sp.integrate(sp.diff(phi0,r)*r**2,(mu,-1,1))
require_zero(net0+2,'monopole flux sign')


md = f"""# 5. Higher multipole zero net flux

## Checked identities

For exterior multipoles `phi_l = P_l(mu)/r^(l+1)`, the net scalar flux over angle vanishes for `l>0`. The monopole `1/r` has nonzero net flux.

## Conclusion

Total scalar charge measures the monopole, not the higher multipole/Weyl-like shape data.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
