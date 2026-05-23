# candidate_source_filter — Result Note

## Result

The source filter applies A-sector-only source routing to insertion families.

It uses the source residual:

```text
S_M*(i_A + i_Bs + i_kappa + i_zeta - 1)
```

and obtains:

```text
A-only residual = 0
A+B_s source residual = S_M
A+zeta+kappa source residual = 2*S_M
missing A residual = -S_M
```

## Main Findings

The filter rejects source-carrying insertion routes:

```text
B_s carries ordinary source load;
zeta/kappa carry ordinary source load;
ordinary source disappears from the A-sector.
```

The only clean source-routing target is:

```text
i_A=1
i_Bs=0
i_zeta=0
i_kappa=0
```

That is still a theorem target, not proof.

This result protects the reduced A-sector ordinary source role. `B_s`, `zeta`, and `kappa` cannot become ordinary source channels by insertion, bookkeeping, or relabeling.

## Boundary

The source filter does not prove source no-double-counting. It states and applies a necessary condition.

## Steering Consequence

Any insertion route that makes `B_s`, `zeta`, or `kappa` carry ordinary source load is excluded. A future route must preserve A-sector-only source routing.
