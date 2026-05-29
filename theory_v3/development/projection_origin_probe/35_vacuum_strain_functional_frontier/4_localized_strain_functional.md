# 4. The Localized Strain Functional Frontier

The vacuum theory needs a functional of the schematic form:

```text
S_vac[X] = ∫_M [ V_local(X) + K_strain(X, ∇X, ∇∇X, ...) ].
```

## Local part

`V_local` is the pointwise response energy.

Its Hessian can supply the local metric-like response:

```text
∂² V_local / ∂X^A ∂X^B -> metric / interval-response Hessian.
```

This is the part the current chain has constrained most strongly.

## Strain part

`K_strain` is the localized completion object.

It tells the theory how much energy is stored in mismatch, deformation, or transport failure between neighboring vacuum configurations.

It must generate the field equations through variation:

```text
δ ∫ K_strain = 0
```

or, with sources:

```text
δ ∫ K_strain = δ S_matter.
```

## Why GR appears conditionally

If `K_strain` is chosen to be the metric EH/GHY branch, then GR appears.

But the prior work has made this sharper than a choice from an open menu. The accumulated gates already force the viable strain sector very close to the Einstein branch.

The natural residual form is:

```text
K_strain = K_EH + ε K_residual.
```

## The actual question

The frontier question is not simply:

```text
What is K_strain?
```

It is:

```text
Do the accumulated gates force ε = 0, allow controlled ε != 0, or require a
new axiom to decide?
```
