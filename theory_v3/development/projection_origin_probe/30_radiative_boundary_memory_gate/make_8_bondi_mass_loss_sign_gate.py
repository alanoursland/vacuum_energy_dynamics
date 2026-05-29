
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
M0, u, k, N0 = sp.symbols('M0 u k N0', positive=True)
M = M0 - k*N0**2*u
loss = sp.diff(M,u)
assert sp.simplify(loss + k*N0**2) == 0

write_report('8_bondi_mass_loss_sign_gate.md', 'Bondi-type mass-loss sign gate', '\nA schematic Bondi-type loss law has the sign form\n\n```text\ndM/du = - k N^2.\n```\n\nThe script verifies that positive news-squared flux lowers the Coulombic mass aspect in\nthis simple model. Radiative flux can change the charge over time, but the channel is\nnews-squared flux, not scalar moment-kernel charge insertion.\n')
