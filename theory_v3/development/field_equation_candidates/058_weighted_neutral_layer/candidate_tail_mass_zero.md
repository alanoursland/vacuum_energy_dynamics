# candidate_tail_mass_zero — Result Note

## Result

The script verifies the reduced exterior tail and mass-shift diagnostics for the weighted-neutral profile.

It obtains:

```text
Q_weighted = 0
phi_ext = C0
phi_ext with C0=0 = 0
Delta_M = 0
```

## Main Findings

This confirms the reduced diagnostic value of the weighted-neutral profile.

Because the weighted scalar charge is zero, the charge-driven exterior tail term vanishes. With the additional zero-offset condition:

```text
C0=0
```

the reduced exterior scalar is silent.

The mass-shift diagnostic also vanishes:

```text
Delta_M = alpha*Q = 0
```

This is a meaningful improvement over Group 57. The layer now has a concrete profile that avoids the reduced scalar-charge and charge-driven mass-shift diagnostics.

## Boundary

This is not full boundary neutrality and not a full mass theorem. The zero-offset condition still matters. Source safety and covariant lift remain open.

## Steering Consequence

The next check should verify whether the same weighted-neutral shape can support reduced divergence-silent closure.
