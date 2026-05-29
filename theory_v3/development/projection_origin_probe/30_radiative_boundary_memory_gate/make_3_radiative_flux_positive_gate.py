
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
Np, Nx = sp.symbols('Np Nx', real=True)
flux = sp.expand(Np**2 + Nx**2)
assert flux.subs({Np:0,Nx:0}) == 0
assert sp.diff(flux,Np,2) == 2
assert sp.diff(flux,Nx,2) == 2

write_report('3_radiative_flux_positive_gate.md', 'Radiative flux positivity gate', '\nRadiative energy flux in the weak TT sector is quadratic in the two news polarizations:\n\n```text\nF_rad ∝ N_+^2 + N_x^2.\n```\n\nThe script verifies the positive quadratic form. It vanishes only when both news\ncomponents vanish.\n')
