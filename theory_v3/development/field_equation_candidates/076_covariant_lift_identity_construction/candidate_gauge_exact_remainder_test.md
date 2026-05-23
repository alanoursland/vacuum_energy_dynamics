# candidate_gauge_exact_remainder_test — Result Note

## Result

`candidate_gauge_exact_remainder_test.py` decomposes the remainder as:

```text
rho = dXi*i_exact + i_phys*rho_phys
```

The physical remainder after removing the exact part is:

```text
i_phys*rho_phys
```

The unresolved exact-plus-physical remainder is:

```text
dXi + rho_phys
```

## Main Findings

The gauge-exact route is possible only as a theorem target.

It requires both:

```text
the exact part is proven nonphysical / boundary-exact / inert;
rho_phys = 0 is derived.
```

The script correctly rejects:

```text
calling rho gauge-exact by prose;
leaving a physical remainder.
```

This result is important because it prevents "gauge" language from becoming another repair patch.

## Boundary

No gauge-exact theorem is proven. The physical remainder remains an obligation.

## Steering Consequence

Proceed to the identity-vs-repair sieve. The next script should preserve only derived exact-pair and derived gauge-exact routes.
