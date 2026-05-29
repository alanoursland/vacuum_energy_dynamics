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


# Boolean dependency sanity table: coupling_route = action_exists AND shared_metric
A,M=sp.symbols('A M')
# Use Boolean algebra with sympy symbols in text; no actual boolean needed
write_md("""
# 19. Matter ontology dependency table

## Closed by earlier/source route

```text
matter action exists + shared metric interval dependence
    -> metric stress tensor source route.
```

## Not closed by stress route alone

```text
matter existence
species count
mass spectrum
charge spectrum
spin/internal symmetry
localization/discreteness
quantization
microscopic action form
```

## Interpretation

The stress tensor is a universal source ledger after matter is present. It is
not a generator of matter ontology.
""")
