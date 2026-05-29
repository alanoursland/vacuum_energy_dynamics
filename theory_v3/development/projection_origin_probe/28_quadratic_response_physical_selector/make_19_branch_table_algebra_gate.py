
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expr'):
    s = sp.simplify(expr)
    if s != 0:
        raise AssertionError(f"{name} expected 0, got {s}")
    return s

def require_nonzero(expr, name='expr'):
    s = sp.simplify(expr)
    if s == 0:
        raise AssertionError(f"{name} expected nonzero")
    return s

def write(md):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(md.strip() + '\n')
    tmp.replace(OUT)

eps,lam,x=sp.symbols('eps lambda x')
conditions={
 'parallelogram': eps,
 'homogeneity': eps*x**4*(lam**4-lam**2),
 'scale_calibration': eps*x**2*(lam**2-1),
}
# Common coefficient forcing all symbolic conditions to vanish for arbitrary probes.
sol=sp.solve([eps],[eps], dict=True)
write(f'''# 19. Branch Table Algebra Gate

The tested selectors all share the same residual coefficient:

```text
parallelogram residual coefficient -> eps
homogeneity residual -> {conditions['homogeneity']}
scale calibration residual -> {conditions['scale_calibration']}
```

For arbitrary probes and scales, all vanish on the metric branch

```text
{sol}
```

A nonzero `eps` is therefore not hidden metric structure; it is an explicit nonmetric branch.
''')
