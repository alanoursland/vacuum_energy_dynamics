from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    expr = sp.simplify(expr)
    if expr != 0:
        raise AssertionError(f"{label} not zero: {expr}")

def require_nonzero(expr, label):
    expr = sp.simplify(expr)
    if expr == 0:
        raise AssertionError(f"{label} unexpectedly zero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text.strip() + "\n")
    tmp.replace(OUT)


write_md("""
# 20. Matter ontology gap audit conclusion

## Result

This folder closes the scope of the matter source route:

```text
shared metric interval dependence -> universal stress coupling.
```

It also closes the negative audit:

```text
stress coupling does not derive matter ontology.
```

The following remain imported or require later proof:

```text
existence of matter actions;
species/internal symmetry;
mass and charge spectra;
spin/torsion source structure;
particle discreteness/localization;
quantization;
matter-source origin from vacuum configuration.
```

## Impact

The vacuum/interval program can still do real work if it derives why matter
uses the shared metric interval. But the metric stress tensor by itself is only
the source ledger. It is not the microscopic matter generator.

## Final status

```text
Matter coupling route: conditionally closed.
Matter ontology: open frontier.
```
""")
