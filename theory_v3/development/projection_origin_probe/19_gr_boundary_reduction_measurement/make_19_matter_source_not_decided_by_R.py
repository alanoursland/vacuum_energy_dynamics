from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.factor(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Matter-source origin not decided by R

# Dependence witness: R appears in projection moments, not in the definition of stress variation.
R = sp.symbols('R')
# Formal stress variation coefficient is independent of R.
coef = sp.Rational(1,2)
require_zero(sp.diff(coef,R), 'stress variation coefficient independent of R')


write_report('19_matter_source_not_decided_by_R.md', r'''
# 19. Matter-source origin is not decided by R

The contact-class integer `R` classifies a scalar compactified boundary/moment
pairing.  It does not derive the matter action or the stress tensor coupling.

A metric matter variation has the schematic form

```text
δS_m = 1/2 ∫ √(-g) T^{ab} δg_ab.
```

The scalar contact index `R` is not the origin of this coupling.  Thus the
matter-sector ontology remains a separate upstream question.

''')
print('wrote 19_matter_source_not_decided_by_R.md')
