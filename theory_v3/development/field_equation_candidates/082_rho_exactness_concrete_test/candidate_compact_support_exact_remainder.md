# candidate_compact_support_exact_remainder — Analysis Note

## Result

`candidate_compact_support_exact_remainder.py` constructs a concrete compact-support exact remainder:

```text
w = (1 - y^2)^2
Xi = (1 - y^2)^3
J = -6*y*(y^2 - 1)^4
rho = (6 - 54*y^2)*(y^2 - 1)^3
```

It finds:

```text
J(-1) = 0
J(1) = 0
∫[-1,1] rho dy = 0
```

## Interpretation

This is the strongest positive result in Group 82.

Before this script, the rho exactness route was a possible idea. After this script, we have an explicit compact-support model where the endpoint flux condition is satisfied and flat integrated neutrality follows.

That is not just bookkeeping. It shows that a local nonzero remainder can be organized as an internal layer redistribution with no net flat charge.

In the theory language, this means:

```text
rho does not necessarily have to behave like a net source.
```

But the wording matters. The result does not say:

```text
rho is not a source locally;
rho is covariantly harmless;
rho can be dropped from the lift equation.
```

It says:

```text
in this reduced layer model, rho can be globally flat-neutral as an exact compact-support divergence.
```

## Conceptual Consequence

This result strengthens the exactness route from “speculative” to “partially demonstrated in a toy/reduced model.”

That should affect future status language. I would not keep saying merely:

```text
rho exactness route retained as theorem target
```

I would upgrade it to something like:

```text
RHO_EXACTNESS_FLAT_NEUTRALITY_DERIVED_IN_REDUCED_CLASS
RHO_EXACTNESS_ROUTE_PARTIALLY_STRENGTHENED
```

but still not:

```text
RHO_REMOVED
RHO_INERT
RHO_COVARIANTLY_NEUTRAL
```

## Boundary

The result is one-dimensional and flat-measure. It is not yet a covariant theorem and not yet a physical inertness theorem.

## Steering Consequence

This is a real foothold. The next hard question is not whether exactness can do anything. It can. The next question is whether this flat-neutral exact structure survives geometry.
