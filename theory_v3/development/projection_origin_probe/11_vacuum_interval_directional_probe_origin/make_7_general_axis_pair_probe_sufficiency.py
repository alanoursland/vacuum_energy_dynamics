#!/usr/bin/env python3
"""
make_7_general_axis_pair_probe_sufficiency.py

Validate the axis-plus-pair probe reconstruction formula in finite dimensions.

Output:
    7_general_axis_pair_probe_sufficiency.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def symmetric_symbol_matrix(n):
    H = sp.zeros(n)
    symbols = {}
    for i in range(n):
        for j in range(i, n):
            sym = sp.symbols(f"h{i + 1}{j + 1}")
            H[i, j] = sym
            H[j, i] = sym
            symbols[(i, j)] = sym
    return H, symbols


def basis_vector(n, index):
    return sp.Matrix([1 if i == index else 0 for i in range(n)])


def validate_dimension(n):
    H, symbols = symmetric_symbol_matrix(n)

    def Q(v):
        return simplify_expr((v.T * H * v)[0])

    for i in range(n):
        ei = basis_vector(n, i)
        require_zero(f"n={n} diagonal {i}", Q(ei) - symbols[(i, i)])

    for i in range(n):
        for j in range(i + 1, n):
            ei = basis_vector(n, i)
            ej = basis_vector(n, j)
            recovered = simplify_expr((Q(ei + ej) - Q(ei) - Q(ej)) / 2)
            require_zero(f"n={n} off diagonal {i}{j}", recovered - symbols[(i, j)])

    probe_count = n + n * (n - 1) // 2
    component_count = n * (n + 1) // 2
    if probe_count != component_count:
        raise AssertionError(f"probe count mismatch for n={n}")

    return probe_count


validated = {n: validate_dimension(n) for n in range(1, 6)}

rows = "\n".join(f"- n={n}: {count} probes for {count} components: passed" for n, count in validated.items())

md = f"""# Vacuum Interval Directional Probe Origin 7: General Axis-Pair Probe Sufficiency

## Purpose

This proof generalizes the finite probe reconstruction from the first batch.

The axis-plus-pair probe set:

```text
Q(e_i)
Q(e_i+e_j), i < j
```

contains exactly enough data to reconstruct a symmetric bilinear form in the
finite dimensions used by the bridge.

## Validated Dimensions

{rows}

## Reconstruction Formula

For every dimension checked:

```text
h_ii = Q(e_i)
h_ij = (Q(e_i+e_j)-Q(e_i)-Q(e_j))/2, i < j.
```

The probe count is:

```text
n + n(n-1)/2 = n(n+1)/2.
```

This equals the number of independent components of a symmetric `n x n`
tensor.

## Interpretation

The selector does not need an arbitrary continuum of interval comparisons. A
finite local frame and its pairwise sums are enough to recover the symmetric
metric-like data in the dimensions relevant to the field-lift chain.
"""

out = Path(__file__).with_name("7_general_axis_pair_probe_sufficiency.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("General axis-pair probe sufficiency passed.")
print(f"Wrote {out.resolve()}")

