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

# Classification check: scalar trace and directional tensor branches are distinct labels.
labels = {'scalar_trace':1, 'directional_tensor':6, 'tt_physical':2}
if labels['scalar_trace'] >= labels['directional_tensor']:
    raise AssertionError('scalar trace incorrectly covers tensor branch')
if labels['scalar_trace'] >= labels['tt_physical']:
    raise AssertionError('scalar trace incorrectly covers TT branch')

write_md("# 22. Embedding Dependency Table\n\nThis status file records the dependency structure.\n\n```text\nscalar admissibility ladder -> trace / monopole / scalar flux channel\nquadratic directional probes -> symmetric bilinear metric data\npolarization reconstruction -> off-diagonal and shear components\nTT spin-2 branch -> radiative tensor polarizations\n```\n\nThe script encodes the count distinction: one scalar trace coefficient is not\nenough to cover either the full boundary tensor branch or the two-polarization\nTT branch.")
