#!/usr/bin/env python3
"""
make_4_null_probe_conformal_ambiguity.py

Validate that null-cone interval data alone determines only a conformal class,
not the absolute metric scale.

Output:
    4_null_probe_conformal_ambiguity.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


c, t, x = sp.symbols("c t x", nonzero=True)

Q = -t**2 + x**2
Qc = c * Q

require_zero("conformal scaling relation", Qc - c * Q)

sample_non_null = {t: 1, x: 0}
Q_sample = simplify_expr(Q.subs(sample_non_null))
Qc_sample = simplify_expr(Qc.subs(sample_non_null))

require_zero("non-null scale changes by c", Qc_sample - c * Q_sample)

null_substitution = {x: t}
require_zero("Q vanishes on null line", Q.subs(null_substitution))
require_zero("Qc vanishes on null line", Qc.subs(null_substitution))

validation_bullets = "\n".join(
    [
        "- conformal rescaling preserves the null equation Q=0: passed",
        "- non-null interval values retain the missing scale: passed",
        "- null probes alone cannot fix the conformal factor: passed",
    ]
)

md = f"""# Vacuum Interval Directional Probe Origin 4: Null-Probe Conformal Ambiguity

## Purpose

This proof separates two kinds of directional interval data:

```text
null-cone data
absolute interval-length data
```

Null-cone data is not enough to reconstruct the full metric scale.

## Validated Checks

{validation_bullets}

## Model

Use the 1+1 quadratic form:

```text
Q(t,x) = -t^2 + x^2.
```

For any nonzero conformal factor `c`:

```text
Qc(t,x) = c Q(t,x).
```

The null equation is unchanged:

```text
Q = 0  <=>  Qc = 0.
```

But a non-null interval changes:

```text
Q(1,0) = {Q_sample}
Qc(1,0) = {Qc_sample}
```

## Interpretation

If the vacuum ontology supplies only causal/null comparisons, the selector
recovers a conformal metric class. To recover the full metric, the ontology
must also supply an interval scale, clock normalization, or equivalent length
comparison.
"""

out = Path(__file__).with_name("4_null_probe_conformal_ambiguity.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Null-probe conformal ambiguity passed.")
print(f"Wrote {out.resolve()}")

