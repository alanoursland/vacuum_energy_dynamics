#!/usr/bin/env python3
"""
make_4_boundary_source_count_once_routing.py

Validate the boundary-source count-once routing gate for independent flux
channels.

Output:
    4_boundary_source_count_once_routing.md
"""

from pathlib import Path
import sympy as sp


i_A, i_res, i_proj = sp.symbols("i_A i_res i_proj")
F_A, F_res, F_proj = sp.symbols("F_A F_res F_proj")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

total_flux = i_A * F_A + i_res * F_res + i_proj * F_proj
target_flux = F_A
error = sp.Poly(sp.expand(total_flux - target_flux), F_A, F_res, F_proj)
coeffs = {
    "F_A": error.coeff_monomial(F_A),
    "F_res": error.coeff_monomial(F_res),
    "F_proj": error.coeff_monomial(F_proj),
}

solution = sp.solve(
    [sp.Eq(coeffs["F_A"], 0), sp.Eq(coeffs["F_res"], 0), sp.Eq(coeffs["F_proj"], 0)],
    [i_A, i_res, i_proj],
    dict=True,
)
if solution != [{i_A: 1, i_res: 0, i_proj: 0}]:
    raise AssertionError(f"unexpected routing solution: {solution}")
checks.append("independent-flux count-once routing selects A only")

require_zero(
    "A-only route",
    (total_flux - target_flux).subs({i_A: 1, i_res: 0, i_proj: 0}),
)
checks.append("A-only route has zero source-routing error")

rejected_rows = []
for a_on in (0, 1):
    for res_on in (0, 1):
        for proj_on in (0, 1):
            err = simplify_expr(
                (total_flux - target_flux).subs({i_A: a_on, i_res: res_on, i_proj: proj_on})
            )
            status = "clean" if err == 0 else "rejected"
            rejected_rows.append((a_on, res_on, proj_on, err, status))

clean_rows = [row for row in rejected_rows if row[-1] == "clean"]
if clean_rows != [(1, 0, 0, 0, "clean")]:
    raise AssertionError(f"unexpected clean rows: {clean_rows}")
checks.append("binary routing audit has exactly one clean row")

table = "\n".join(
    f"| {a_on} | {res_on} | {proj_on} | `{err}` | {status} |"
    for a_on, res_on, proj_on, err, status in rejected_rows
)

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 4: Boundary Source Count-Once Routing

## Purpose

This proof validates the strongest reduced source-routing gate:

```text
ordinary boundary/source flux is carried by the A-sector once.
```

Residual and projection channels may exist as diagnostics or admissibility
objects, but they cannot independently carry the same ordinary source flux
without a routing theorem.

## Validated Checks

{validation_bullets}

## Symbolic Setup

Let the routed flux be:

```text
F_total = i_A F_A + i_res F_res + i_proj F_proj.
```

The count-once ordinary source target is:

```text
F_target = F_A.
```

For independent flux channels, requiring:

```text
F_total - F_target = 0
```

for all `F_A`, `F_res`, and `F_proj` gives:

```text
i_A = 1
i_res = 0
i_proj = 0.
```

## Exhaustive Binary Routing Check

| i_A | i_res | i_proj | error | status |
|---:|---:|---:|---|---|
{table}

## Gate Interpretation

This proof does not claim residual or projection sectors are meaningless. It
claims they are not allowed to carry an independent ordinary source flux unless
the theory supplies a separate routing rule and redoes the count-once ledger.
"""

out = Path(__file__).with_name("4_boundary_source_count_once_routing.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary source count-once routing passed.")
print(f"Wrote {out.resolve()}")
