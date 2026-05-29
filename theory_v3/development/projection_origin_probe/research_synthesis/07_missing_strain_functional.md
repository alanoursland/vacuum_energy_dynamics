# The Missing Strain Functional

This is the current center of the project.

The proof chain has constrained the local response structure strongly. It has not yet specified the gradient or strain functional that determines field dynamics.

A schematic vacuum functional should have the form

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) ).
```

The local part `V_local` determines pointwise response. Its Hessian gives metric-like data:

```text
d^2 V_local / dX^a dX^b -> g_ab.
```

This is the part of the ontology the project has developed most successfully.

The strain part `K_strain` determines how configurations compare across neighboring points. This is the part that should generate:

```text
transport law,
connection dynamics,
curvature,
wave propagation,
field equations,
radiative sectors,
constraint propagation,
epsilon deviations from GR.
```

This strain sector is not yet written.

## Why this matters

Many imported assumptions across the chain are symptoms of the same missing object.

When the chain imports a transport law, that is a sign that `K_strain` has not been specified.

When the chain imports EH/GHY as the action closure, that is a sign that `K_strain` has not been derived from vacuum ontology.

When the chain cannot compute `epsilon`, that is a sign that the nonquadratic or nonmetric residual of `K_strain` is unknown.

When the chain reconstructs GR at `epsilon = 0`, it is effectively choosing the GR strain branch rather than deriving it.

## The epsilon diagnosis

The parameter `epsilon` should not be treated as an isolated correction coefficient floating outside the theory.

It is a diagnostic for the unknown strain sector.

A schematic expansion would look like

```text
K_strain = K_GR + epsilon K_residual + higher terms.
```

If the vacuum ontology forces

```text
epsilon = 0,
```

then the project becomes an exact ontology-based rederivation of GR.

If the ontology predicts

```text
epsilon != 0,
```

then the project becomes a possible extension of GR.

If the ontology cannot determine `epsilon`, then the ontology is under-specified.

## What the next axiom must do

The next axiom should not merely restate metricity. It must specify the energy cost of configuration mismatch between neighboring vacuum states.

It should answer:

```text
What is the vacuum configuration variable X?
What counts as a neighboring mismatch?
What local invariants can the strain energy depend on?
Why is the leading strain term EH-like or not?
Are nonquadratic residuals forbidden, suppressed, or physical?
What boundary term makes the variation well-posed?
```

The current project has reached the point where the missing axiom can be named precisely:

```text
Specify the vacuum strain/gradient functional.
```

That is the next field-equation-generating move.
