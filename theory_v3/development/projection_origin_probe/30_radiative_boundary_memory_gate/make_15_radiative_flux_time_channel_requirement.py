
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
C0, a, u = sp.symbols('C0 a u')
C = C0 + a*u
N = sp.diff(C,u)
flux = sp.simplify(N**2)
assert N == a
assert flux == a**2

write_report('15_radiative_flux_time_channel_requirement.md', 'Radiative flux requires time channel', '\nRadiation is not a static boundary coefficient. If `C(u)` is shear/memory data, then\n\n```text\nN(u)=dC/du\n```\n\nis the news. The radiative flux is quadratic in time-dependent news. A static scalar\nmoment ledger has no such time-channel by itself.\n')
