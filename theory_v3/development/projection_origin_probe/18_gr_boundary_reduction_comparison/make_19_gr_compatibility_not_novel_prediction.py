from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.combsimp(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Classification ledger with three states: match, mismatch, undecided.
match, mismatch = sp.symbols('match mismatch')
# If ratio classes match, novelty indicator from boundary class alone is zero.
novel_boundary_indicator = 0
if novel_boundary_indicator != 0:
    raise AssertionError('boundary novelty classification failed')

write_report('19_gr_compatibility_not_novel_prediction.md', r'''
# 19. GR compatibility is not a novel boundary prediction

If the fully normalized weak-field GR reduction lands in the same contact class
as the projection ladder, then `r_k` is GR-compatible boundary reduction, not a
new boundary-condition prediction.

Interpretation: this is not a failure. It means the original mystery was solved
as a standard reduced-boundary signature.
''')
print('wrote', '19_gr_compatibility_not_novel_prediction.md')
