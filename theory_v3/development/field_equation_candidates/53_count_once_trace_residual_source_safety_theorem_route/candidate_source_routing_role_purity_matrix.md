# candidate_source_routing_role_purity_matrix — Result Note

## Result

The script refines source no-double-counting into an A-sector-only role-purity condition.

It uses the source duplicate residual:

```text
S_M*(i_A + i_Bs + i_kappa + i_zeta - 1)
```

and classifies key patterns:

```text
A-only target:
  residual = 0

missing A:
  residual = -S_M

A+B_s:
  residual = S_M

A+zeta+kappa:
  residual = 2*S_M
```

## Main Findings

The clean source-routing target is explicit:

```text
i_A=1
i_Bs=0
i_zeta=0
i_kappa=0
```

This says ordinary source load belongs in the A-sector, while `B_s/F_zeta`, `zeta`, and `kappa` must remain source-pure.

The script also identifies three bad patterns. Ordinary source cannot disappear. Ordinary source also cannot be duplicated through `B_s/F_zeta` or through residual `zeta/kappa` channels.

This strengthens the earlier source witness from Group 52. It turns “source duplication exists” into a precise source role-purity theorem target.

## Boundary

The matrix does not prove ordinary matter separation. It does not derive the source-routing theorem. It states the clean incidence target and obstruction patterns.

## Steering Consequence

The residual/source safety route now requires a source no-double-counting theorem: ordinary source incidence must be A-sector-only under the retained trace-normalization candidate.
