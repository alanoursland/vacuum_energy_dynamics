# 6. Candidate Functional Branches

This document lists possible strain/gradient branches, but they should not be read as equally open options. The prior work constrains them as perturbations, alternatives, or explicitly routed departures from the EH branch.

## Branch 1: EH/GHY metric strain

```text
K_strain = K_EH/GHY[g]
```

This is the exact GR branch. It uses the metric as the configuration variable and gives Einstein-type dynamics under the usual assumptions.

This branch corresponds to:

```text
ε = 0.
```

## Branch 2: EH/GHY plus residual

```text
K_strain = K_EH/GHY[g] + ε K_residual[g, ∇g, ...].
```

This is the most important frontier branch.

The residual may represent higher-curvature, higher-derivative, Finsler-like, medium-like, nonlocal, or relaxation dynamics.

The task is to determine whether the accumulated gates force `ε = 0` or permit a controlled `ε != 0`.

## Branch 3: configuration-elastic strain

A direct configuration-gradient branch might take schematic forms like:

```text
K_strain = C^{ABμν} ∇_μ X_A ∇_ν X_B
```

or higher-order elastic terms.

This branch treats vacuum configuration directly as the field whose mismatch carries energy.

Its risk is introducing preferred internal structure, extra modes, or medium-like degrees of freedom. Those must be routed explicitly.

## Branch 4: curvature-as-holonomy strain

The strain energy is built from transport failure around loops:

```text
K_strain = F(holonomy / curvature).
```

The EH branch is then one possible low-order scalar contraction. Higher contractions generate residuals.

The accumulated gates restrict which contractions are admissible.

## Branch 5: Finsler/nonquadratic directional response

The strain depends on direction beyond a metric quadratic form:

```text
K_strain = K_metric + ε K_Finsler.
```

This branch can produce scale- or direction-dependent propagation unless strongly constrained.

It is not forbidden by algebra alone, but it cannot be hidden inside the pseudo-Riemannian branch.

## Branch 6: nonlocal or relaxation strain

```text
K_strain = ∫ X(x) K(x,y) X(y)
```

or a global constraint term.

This branch is relevant for Lambda relaxation or large-scale vacuum energy dynamics, but it departs from strictly local GR-type dynamics.

## Summary

The candidate list is not a loose menu. The constrained form is:

```text
K_strain = K_EH + ε K_residual.
```

The serious question is whether any residual branch survives all prior gates.
