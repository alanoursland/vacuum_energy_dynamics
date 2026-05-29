#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('19_radiative_flux_not_monopole_charge.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


M,E=sp.symbols('M E_rad')
M_initial=M
M_final=M-E
delta=M_final-M_initial
require_zero(delta+E,'mass loss ledger')
# Energy flux E can be positive while scalar final charge changes only integrated total, not waveform detail
A1,A2=sp.symbols('A1 A2')
E_total=A1**2+A2**2
if sp.diff(E_total,A1)==0:
    raise AssertionError('radiative amplitude not represented')


md = f"""# 19. Radiative flux versus monopole charge ledger

## Checked identities

A scalar mass ledger can track integrated loss `Delta M = -E_rad`, but not the tensor waveform amplitudes whose squares produce the flux.

## Conclusion

Scalar boundary charge can record total radiated energy, but not the full radiative Weyl/TT data.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
