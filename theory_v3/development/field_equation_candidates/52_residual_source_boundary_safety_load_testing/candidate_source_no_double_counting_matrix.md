# candidate_source_no_double_counting_matrix — Result Note

## Result

The source no-double-counting matrix produces a concrete source-duplication diagnostic.

It models ordinary mass source load `S_M` entering possible scalar channels:

```text
A-sector
B_s/F_zeta
zeta residual
kappa residual
```

The duplicate residual is:

```text
S_M*(i_A + i_Bs + i_kappa + i_zeta - 1)
```

The protected A-only case gives zero residual. But adding `B_s` as an additional source channel gives:

```text
S_M
```

and adding both residual channels gives:

```text
2*S_M
```

## Main Findings

This is a strong diagnostic result. It does not prove the full source theorem, but it shows why ordinary source load cannot be casually routed into scalar trace-normalization or residual channels.

The A-only case is clean at this bookkeeping level. Once ordinary source load appears in `B_s/F_zeta`, `zeta`, or `kappa` in addition to the A-sector, the matrix reports extra source load.

The script therefore protects the reduced A-sector source role. It rejects source-by-label, hidden source in coefficients, and treating the matrix itself as a source-safety proof.

## Boundary

The source matrix is diagnostic. It does not derive the ordinary matter separation theorem. It does not prove source safety. It only identifies explicit double-count witnesses.

## Steering Consequence

Any future physical-use route for trace normalization must prove ordinary mass source routing. The safest current rule remains: ordinary mass response belongs to the A-sector unless a separate source theorem says otherwise. `B_s`, `zeta`, `kappa`, residual variables, curvature accounting, and exchange labels cannot be source channels by bookkeeping.
