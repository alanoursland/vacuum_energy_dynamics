# 7. Epsilon Residual Definition

`ε` is a bookkeeping symbol for whatever remains after the GR-compatible metric strain branch is extracted.

The schematic decomposition is:

```text
K_strain = K_GR + ε K_residual.
```

## What epsilon is not

`ε` is not the original scalar projection coefficient.

It is not `r_k`.

It is not the scalar contact index `R`.

It is not a boundary normalization constant.

## What epsilon represents

`ε` represents the non-GR residual in the vacuum strain/gradient functional.

Depending on the branch, it may encode:

```text
nonquadratic directional response
Finsler-like corrections
higher-curvature corrections
nonmetric calibration drift
extra affine/torsion sectors
medium-like vacuum elasticity
nonlocal relaxation behavior
scale-dependent propagation
```

## Why epsilon has not been computed

`ε` cannot be computed from the local Hessian alone.

It depends on `K_strain`, not merely `V_local`.

The current chain has localized the residual to the strain functional. That is the achievement.

The next task is to determine whether the accumulated gates force:

```text
ε = 0
```

or allow:

```text
ε != 0.
```

## Possible outcomes

Outcome 1:

```text
constraints force ε = 0.
```

Then the ontology recovers exact GR in the classical branch.

Outcome 2:

```text
constraints allow ε != 0.
```

Then the ontology predicts an extension or residual branch.

Outcome 3:

```text
ε is underdetermined.
```

Then the current ontology is incomplete and needs a new strain axiom.
