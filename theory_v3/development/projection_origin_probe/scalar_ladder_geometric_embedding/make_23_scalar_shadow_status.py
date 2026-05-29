from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

# Required preceding reports in this folder.
required = [
    '1_scalar_trace_projection_gate.md',
    '6_monopole_projection_legendre_gate.md',
    '12_symmetric_tensor_rank_gap.md',
    '15_polarization_recovers_metric_components.md',
    '17_tt_mode_scalar_projection_zero.md',
]
missing = [name for name in required if not Path(__file__).with_name(name).exists()]
if missing:
    raise AssertionError(f'missing prerequisite reports: {missing}')

write_md("# 23. Scalar Shadow Status\n\nThe preceding reports establish the placement of the scalar ladder:\n\n```text\nscalar ladder = trace / isotropic / monopole shadow\n```\n\nIt captures the scalar admissibility and boundary-flux channel. It does not\nsupply shear, off-diagonal, higher multipole, or TT tensor data. Those require\ndirectional probes and polarization reconstruction.")
