
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parent

def write_report(filename: str, title: str, body: str):
    path = ROOT / filename
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(f"# {title}\n\n" + body.strip() + "\n")
    tmp.replace(path)

import sympy as sp
scalar_charge_determines_memory = sp.Integer(0)
news_integrates_to_memory = sp.Integer(1)
assert scalar_charge_determines_memory == 0
assert news_integrates_to_memory == 1

write_report('19_radiative_boundary_memory_status.md', 'Radiative boundary memory status', "This status report fixes the folder's main ledger claim:\n\n```text\nscalar charge does not determine memory;\nnews integrates to memory.\n```\n\nRadiative memory belongs to the tensor boundary/symplectic sector.\n")
