# candidate_shared_identity_requirements — Result Note

## Result

`candidate_shared_identity_requirements.py` states the legal requirements for a shared lift identity.

The model is:

```text
L_bulk = K
L_gauge = -K + rho
R_lift = rho
```

The exact-pair residual is zero only when:

```text
rho = 0
```

## Main Findings

A legal shared lift identity requires:

```text
common generator K;
opposite sign relation;
rho = 0 or proven inert/gauge-exact.
```

The important result is that the obstruction is now named directly:

```text
rho
```

The script correctly rejects:

```text
free sign;
free coefficients;
dropped rho;
repair current;
active O by label.
```

## Boundary

The script states requirements. It does not derive `K`, the sign relation, or the vanishing/inertness of `rho`.

## Steering Consequence

Proceed to exact-pair scaffold. The ideal cancellation should be tested, but kept as compatibility unless the shared origin is derived.
