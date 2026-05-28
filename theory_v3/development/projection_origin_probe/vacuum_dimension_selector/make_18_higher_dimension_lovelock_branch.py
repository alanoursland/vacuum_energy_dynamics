#!/usr/bin/env python3
"""
make_18_higher_dimension_lovelock_branch.py

Validate that dimensions above four open additional Lovelock curvature branches.

Output:
    18_higher_dimension_lovelock_branch.md
"""

from pathlib import Path


def lovelock_status(D, p):
    if D < 2 * p:
        return "vanishes"
    if D == 2 * p:
        return "topological"
    return "dynamical"


checks = {
    (5, 2): "dynamical",
    (6, 2): "dynamical",
    (6, 3): "topological",
    (7, 3): "dynamical",
}

for key, expected in checks.items():
    got = lovelock_status(*key)
    if got != expected:
        raise AssertionError(f"higher-dimensional Lovelock check failed for {key}: {got}")

md = f"""# Vacuum Dimension Selector 18: Higher-Dimension Lovelock Branch

## Purpose

This proof checks why dimensions above four are not the same action branch as
the four-dimensional Einstein-Hilbert selector.

## Validated Checks

- in `D=5`, Gauss-Bonnet (`p=2`) is dynamical: passed
- in `D=6`, Gauss-Bonnet remains dynamical and `p=3` is topological: passed
- in `D=7`, the cubic Lovelock term (`p=3`) is dynamical: passed

## Computation

```text
status(D=5, p=2) = {lovelock_status(5, 2)}
status(D=6, p=2) = {lovelock_status(6, 2)}
status(D=6, p=3) = {lovelock_status(6, 3)}
status(D=7, p=3) = {lovelock_status(7, 3)}
```

## Interpretation

Higher-dimensional metric theories have additional local second-order curvature
branches. A higher-dimensional lift is therefore not automatically the same
Einstein-Hilbert branch with extra coordinates; it must explain why those extra
Lovelock terms are absent or suppressed.
"""

out = Path(__file__).with_name("18_higher_dimension_lovelock_branch.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Higher-dimension Lovelock branch check passed.")
print(f"Wrote {out.resolve()}")

