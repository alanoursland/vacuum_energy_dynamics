# candidate_boundary_scalar_silence_dependency_audit — Result Note

## Result

The boundary/scalar-silence audit identifies a concrete exterior scalar-tail witness.

For a trace-sector exterior scalar tail,

```text
phi_tail = q_zeta/r
```

the script computes:

```text
4*pi*r^2*d(phi_tail)/dr = -4*pi*q_zeta
```

This is nonzero when `q_zeta` is nonzero. Setting `q_zeta=0` kills both the tail and the flux, but that is only a condition, not a theorem.

## Main Findings

This script sharpens the exterior scalar-silence burden. If trace normalization permits an exterior scalar charge, that charge produces an exterior scalar tail and nonzero scalar flux. That is not allowed for the ordinary exterior branch unless a separate theorem proves the charge is absent, inert, compactly supported, or otherwise neutralized.

The zero-charge diagnostic is useful but limited. It shows what silence would require:

```text
q_zeta = 0
```

It does not show why that condition holds.

The script also preserves the boundary neutrality burden. Trace normalization must not create shell sources, boundary counterterms, far-zone scalar charge, or `M_ext` shifts.

## Boundary

Boundary neutrality is not proven. Exterior scalar silence is not proven. The script only identifies a scalar-tail obstruction and the zero-charge condition needed to avoid it.

## Steering Consequence

Boundary/scalar silence should be treated as a serious theorem route, not a caveat. Any insertion attempt before boundary neutrality and exterior scalar silence would risk scalar tail leakage or boundary repair behavior.
